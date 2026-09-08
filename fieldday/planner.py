"""Plan a lawn-care day from messy job titles using the OpenAI API."""

from __future__ import annotations

import os

from openai import OpenAI


class MissingAPIKeyError(Exception):
    """Raised when OPENAI_API_KEY is not set."""


SYSTEM_PROMPT = """You are a lawn-care operations assistant.
Given a list of messy job titles (typos, mixed case, vague areas), produce a clean day plan:

1. Group jobs by area / neighborhood when possible.
2. Normalize titles (fix spelling, consistent casing, clear service names).
3. Flag odd, unclear, or incomplete items so a crew lead can follow up.
4. Keep the output as plain text ready to print — no JSON, no markdown fences.
5. Be concise and practical for a morning crew briefing.
"""


def plan_jobs(jobs: list[str]) -> str:
    """Return a plain-text day plan for the given job titles.

    Raises MissingAPIKeyError if OPENAI_API_KEY is not set.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise MissingAPIKeyError(
            "Missing OPENAI_API_KEY. Copy .env.example to .env and set your key, "
            "then try again."
        )

    base_url = os.environ.get("OPENAI_BASE_URL") or None
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    client_kwargs: dict = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url

    client = OpenAI(**client_kwargs)

    job_list = "\n".join(f"- {job}" for job in jobs)
    user_message = (
        "Organize these lawn-care jobs into a clean day plan "
        "(group by area, normalize titles, flag anything odd):\n\n"
        f"{job_list}"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.3,
    )

    content = response.choices[0].message.content
    return (content or "").strip()
