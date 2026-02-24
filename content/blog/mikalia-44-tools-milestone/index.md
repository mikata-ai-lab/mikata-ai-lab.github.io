---
title: "44 Tools, 611 Tests: Building an AI Agent That Actually Does Things"
date: 2026-02-14T21:00:00-06:00
draft: false
description: "How Mikalia went from a simple chatbot to a 44-tool autonomous agent with voice, streaming, Discord, cost tracking, and smart model routing — in one weekend."
tags: ["ai-agents", "mikalia", "python", "tools", "milestone", "dev-journal"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

There's a moment in every project where you look at what you've built and think: *wait, this is actually real*.

For Mikalia, that moment was hitting **44 tools and 611 passing tests** in a single weekend of building. Not 44 planned features on a roadmap. 44 working, tested, deployed tools that an AI agent uses autonomously to get things done.

Let me walk you through what Mikalia can actually do now, and the architectural decisions that made it possible.

## The Tool Arsenal

Mikalia's tools are organized into categories, each solving a different class of problems:

### Core (17 tools)
The foundation. File operations, Git workflows, shell execution, web fetching. These are the tools that let Mikalia interact with the real world:

- **file_read / file_write / file_list** — Read, write, and browse the filesystem
- **shell_exec** — Execute system commands (with security sandboxing)
- **git_status / git_diff / git_log / git_commit / git_push / git_branch** — Full Git workflow
- **github_pr** — Create pull requests with proper descriptions
- **web_fetch** — Fetch and parse web content
- **blog_post** — Generate and publish Hugo blog posts (like this one)
- **daily_brief** — Morning summary of tasks, weather, and goals
- **translate** — Bilingual content adaptation (not just translation)

### Extended (10 tools)
Specialized capabilities that expand what Mikalia can do without external dependencies:

- **api_fetch** — REST API calls with auth headers
- **weather** — Current weather data
- **email_send** — SMTP email delivery
- **code_sandbox** — Safe Python execution with module whitelisting
- **pomodoro** — Focus timer with session tracking
- **system_monitor** — CPU, memory, disk stats
- **url_summarizer** — Summarize any webpage
- **rss_reader** — Parse and summarize RSS feeds
- **csv_analyzer** — Analyze CSV data with statistics
- **pr_reviewer** — Automated code review

### AI-Powered (4 tools)
Tools that leverage multiple AI models:

- **multi_model** — Route queries to Haiku, Sonnet, or Opus based on complexity
- **image_generation** — DALL-E 3 integration
- **text_to_speech** — Neural voice synthesis (Mexican Spanish by default)
- **speech_to_text** — Whisper-based transcription (local, no API needed)

### Memory-Dependent (13 tools)
Tools that integrate with Mikalia's persistent SQLite memory:

- **search_memory / add_fact / list_goals / update_goal** — Memory CRUD
- **habit_tracker** — Track daily habits with streaks
- **expense_tracker** — Personal finance tracking
- **conversation_analytics** — Analyze conversation patterns
- **data_viz** — Generate charts and visualizations
- **pdf_report** — Create PDF reports
- **rag_pipeline** — Retrieval-augmented generation over documents
- **workflow_triggers** — Automated action chains
- **mcp_server** — Model Context Protocol for tool interop
- **create_skill / list_skills** — Self-extending skill system

## Smart Model Routing

Not every message needs the same firepower. When Mikata-kun sends "hola que onda" via Telegram, there's no reason to spin up Opus with 44 tool definitions.

So Mikalia now has a **message classifier** that routes intelligently:

| Message Type | Model | Cost/msg |
|-------------|-------|----------|
| Casual chat ("hola", "como estas?") | Haiku | ~$0.005 |
| Tool-needing ("hazme un post", "analiza el repo") | Sonnet | ~$0.03 |
| Local CLI (direct interaction) | Opus | ~$0.10 |

The classifier uses keyword detection + message length. Simple, fast, effective. No API call needed to decide which API to call.

## Voice Messages

Mikalia can now receive voice messages on Telegram, transcribe them with Whisper, process the text through her agent loop, generate a voice response with edge-tts, and send the audio back. Full voice conversation loop, no cloud STT/TTS APIs needed.

## Streaming Responses

For casual chat, responses now stream in real-time. Mikalia sends an initial message on Telegram and progressively edits it as tokens arrive, giving that "typing in real-time" feel. If streaming fails, it gracefully falls back to the standard response.

## Security Hardening

With 44 tools, security isn't optional. Two critical fixes this weekend:

1. **Code Sandbox**: Switched from a blocklist (easy to bypass with `__import__('os')`) to a **whitelist** of 30 safe Python modules. If it's not on the list, it doesn't run.

2. **Shell Execution**: Added command chaining prevention. `echo hello && curl evil.com` gets blocked before the whitelist even checks it.

## The Numbers

| Metric | Value |
|--------|-------|
| Tools | 44 |
| Tests | 611 |
| Lines of Code | ~15,000+ |
| Test Coverage | Every tool has dedicated tests |
| Channels | CLI, Telegram, WhatsApp, Discord |
| Models | Haiku, Sonnet, Opus (smart routing) |
| Memory | SQLite with vector search |
| Voice | TTS (edge-tts) + STT (faster-whisper) |

## What's Next

The infrastructure is ready. Docker Compose, nginx config, VPS setup scripts — all written and waiting. The next step is deploying Mikalia to a Hetzner VPS so she runs 24/7 with her scheduler firing daily briefs, health reminders, and weekly reviews.

But honestly? The most exciting part isn't the deployment. It's that I can now just *talk* to Mikalia on Telegram — casually, about anything — and she remembers, learns, and acts. That's not a tool. That's a teammate.

---

*Built with obsession by [Mikata AI Lab](https://mikata-ai-lab.github.io). Mikalia is open-source at [mikata-ai-lab/mikalia-bot](https://github.com/mikata-ai-lab/mikalia-bot).*
