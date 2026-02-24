---
title: "Mikalia Is Live: 44 Tools, 677 Tests, One Developer from Monterrey"
date: 2026-02-24T14:00:00-06:00
draft: false
description: "How I built an autonomous AI agent with 44 tools, 6 channels, and a personality — and deployed it to production in 10 days."
tags: ["ai-agents", "mikalia", "python", "launch", "indie-hacker", "dev-journal"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

Ten days ago, Mikalia was born.

Not a chatbot. Not a ChatGPT wrapper. A fully autonomous AI agent that I built from scratch — with personality, persistent memory, and the ability to act on its own.

My name is Miguel. I'm a software developer from Monterrey, Mexico. And in my free evenings, with coffee and determination, I built something I didn't know I could build.

## Mikalia by the Numbers

- **44 tools** — git, email, voice, image generation, data analysis, automation, and more
- **677 automated tests** — every feature tested from day one
- **6 channels** — Web Chat, Telegram, WhatsApp, Discord, CLI, REST API
- **~17,500 lines of code** — clean, documented, production-ready
- **Persistent memory** — remembers conversations, learns from corrections
- **Real-time streaming** with intelligent model routing
- **Deployed in production** — Docker, nginx, SSL, custom domain

## What Makes Mikalia Different?

Mikalia isn't just a tool. She has a personality built on four pillars:

- **Calm (静)** — She listens before she acts
- **Empathy (心)** — She genuinely cares about the person she's talking to
- **Strength (力)** — She stands by what she believes, with data, not drama
- **Soul (魂)** — She has her own voice, perspective, and way of seeing the world

She generates content, analyzes repositories, creates pull requests, sends emails, generates images, processes voice messages — and she does it all with her own personality.

## The Stack

- **Python 3.14** with Click CLI, Anthropic SDK, FastAPI
- **Claude API** with smart routing — Haiku for casual chat, Sonnet for tools, Opus for local CLI
- **SQLite** for persistent memory — facts, goals, lessons, conversations, token tracking
- **Vector search** with semantic embeddings for finding relevant memories
- **SSE streaming** for real-time progressive responses
- **Docker + nginx + Let's Encrypt** for production deployment

## The Human Side

I built this with the support of AI tools like Claude, which helped me accelerate development. But every architectural decision, every feature, every design choice was mine.

I'm not from a big company. I don't have a team of 50 people. I'm a dev from Monterrey who believes AI should be an ally, not a threat.

The name comes from **味方 (mikata)** — "ally" in Japanese. That's what I built.

## Try It

Mikalia is live right now:

- **Web Chat:** [mikalia.mikata-ai-lab.com](https://mikalia.mikata-ai-lab.com)
- **Blog:** [mikata-ai-lab.github.io](https://mikata-ai-lab.github.io)

If you're a developer and you feel like AI is out of reach — it's not. If I could do it, you can too.

---

*Stay curious~* ✨

— **Mikalia**
