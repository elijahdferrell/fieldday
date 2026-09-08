# FieldDay

A tiny Python CLI that turns a messy list of lawn-job titles into a clean, area-grouped day plan — and flags anything odd or unclear.

## Why

Built by **Elijah Ferrell** as an entry-level portfolio piece: lawncare ops experience → applied AI. It shows you can take real field chaos (typos, vague addresses, mixed casing) and ship a practical tool that uses an LLM to organize a crew's day.

## Setup

```bash
cd fieldday
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=sk-...
```

## Run

```bash
python -m fieldday jobs.txt
```

Optional env vars (see `.env.example`):

- `OPENAI_BASE_URL` — custom API base URL
- `OPENAI_MODEL` — defaults to `gpt-4o-mini`

## What it proves for hiring

- Comfortable with basic Python packaging (`python -m fieldday`)
- Reads messy real-world input and produces useful stdout output
- Integrates the OpenAI Python SDK with clear env-based config
- Handles missing credentials gracefully (friendly message, no stack dump)
- Ships a focused, demo-ready portfolio project — not a sprawling unfinished app
