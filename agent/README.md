# Mikalia Agent

Autonomous AI blog post generator for Mikata AI.

## Setup

```bash
cd agent
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Usage

```bash
# Generate and publish a post
python mikalia.py "Why RAG is the future of enterprise AI"

# Interactive mode
python mikalia.py --interactive

# Generate without publishing (local only)
python mikalia.py "Topic here" --no-publish

# Save as draft
python mikalia.py "Topic here" --draft
```

## How It Works

1. Reads `MIKALIA.md` from project root as personality/system prompt
2. Generates an English blog post using Claude API
3. Runs ethical content filter
4. Translates to Spanish (adapted, not literal)
5. Saves both as Hugo-compatible markdown in `content/blog/`
6. Commits and pushes to GitHub (auto-deploys via GitHub Actions)
