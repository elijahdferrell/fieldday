# FieldDay

Messy lawn-job list in → clean, area-grouped day plan out. Tiny Python CLI + LLM.

## Why

**Elijah Ferrell** — lawncare ops → AI. Built to prove I can ship: take real crew chaos (typos, vague addresses, mixed casing) and turn it into something a lead can brief from in the morning.

## What it proves for hiring

- Ships a working CLI (`python -m fieldday`), not a slide deck
- Uses an LLM API (xAI Grok) with clear env-based config
- Turns messy real-world input into scannable stdout
- Fails clean when the key is missing — no stack dump
- Scope stays tiny on purpose so employers can clone and run in minutes

## Example output

Real run from sample `jobs.txt` with **Grok** (`grok-4.3`):

```
North Side
- Mow Mrs. Smith
- Mow Northside Duplexes (3 units)

Oak/Elm Area
- Edge and blow driveway, 12 Oak St
- Mow, edge, bag, 8 Elm Court

Johnson Property
- Weed eat fence line, Johnson

South Side
- Mow and edge, Southside (park area)

Pine Street
- Bag clippings, 44 Pine (backyard only)

Thompson Property
- Fertilizer application, Thompson

West Side
- Leaf cleanup, West Side lots

Garcia Property
- Mow, edge, mulch beds, Garcia

River Road
- Aerate front lawn, River Rd

Mrs. Lee
- Trim around mailbox, Mrs. Lee

Chestnut
- Weed and feed, corner lot Chestnut

Church Area
- Mow lawn by church parking

Flags for crew lead
- Hedge trim Maple Ave: location and scope unclear
- Bush trimming behind garage: missing property name
- Prune fruit trees: confirm if needed or skip
- Blow sidewalks downtown: confirm exact location and scope
```

## Setup

```bash
git clone https://github.com/elijahdferrell/fieldday.git
cd fieldday
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Run with Grok (xAI)

FieldDay uses the OpenAI-compatible SDK. For Grok, set `.env` like this (API key from [console.x.ai](https://console.x.ai/) — **SuperGrok chat ≠ API access**):

```bash
OPENAI_API_KEY=xai-...
OPENAI_BASE_URL=https://api.x.ai/v1
OPENAI_MODEL=grok-4.3
```

`grok-4.3` is a cheap/fast chat model for this demo. Swap to `grok-4.6` or another id from [xAI models](https://docs.x.ai/docs/models) if you want.

```bash
python -m fieldday jobs.txt
```

Other OpenAI-compatible providers work the same way — change key, base URL, and model in `.env`.

## Next for employers

Clone the repo, put an xAI API key in `.env`, run `python -m fieldday jobs.txt` — you should see a plan like the example above.
