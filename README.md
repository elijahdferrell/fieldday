# FieldDay

A tiny Python CLI that turns a messy list of lawn-job titles into a clean, area-grouped day plan — and flags anything odd or unclear.

## Why

Built by **Elijah Ferrell** as an entry-level portfolio piece: lawncare ops experience → applied AI. It shows you can take real field chaos (typos, vague addresses, mixed casing) and ship a practical tool that uses an LLM to organize a crew's day.

## Setup

```bash
cd fieldday
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env — see Grok section below
```

## Run with Grok (xAI)

FieldDay talks to any OpenAI-compatible chat API. For xAI Grok, put this in `.env` (get a key from [console.x.ai](https://console.x.ai/) — chat SuperGrok is separate from API access):

```bash
OPENAI_API_KEY=xai-...
OPENAI_BASE_URL=https://api.x.ai/v1
OPENAI_MODEL=grok-4.3
```

`grok-4.3` is a solid cheap/fast chat model for this demo. You can swap to `grok-4.6` (flagship) or another id from [xAI models](https://docs.x.ai/docs/models).

Then:

```bash
python -m fieldday jobs.txt
```

## Run

```bash
python -m fieldday jobs.txt
```

Env vars (see `.env.example`):

- `OPENAI_API_KEY` — required (xAI or other provider)
- `OPENAI_BASE_URL` — e.g. `https://api.x.ai/v1` for Grok
- `OPENAI_MODEL` — defaults to `gpt-4o-mini` if unset; set `grok-4.3` for Grok

## What it proves for hiring

- Comfortable with basic Python packaging (`python -m fieldday`)
- Reads messy real-world input and produces useful stdout output
- Integrates an OpenAI-compatible SDK (works with xAI Grok via base URL)
- Handles missing credentials gracefully (friendly message, no stack dump)
- Ships a focused, demo-ready portfolio project — not a sprawling unfinished app
