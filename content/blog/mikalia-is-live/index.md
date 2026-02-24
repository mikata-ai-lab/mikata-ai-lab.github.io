---
title: "I Built an Autonomous AI Agent from Scratch — 44 Tools, 677 Tests, 10 Days"
date: 2026-02-24T14:00:00-06:00
draft: false
description: "How I built Mikalia, an autonomous AI agent with persistent memory, multi-step reasoning, 44 tools, and a personality — deployed to production in 10 days by one developer."
tags: ["ai-agents", "mikalia", "autonomous-ai", "python", "launch", "machine-learning", "indie-hacker"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

Ten days ago I built an autonomous AI from scratch.

Not a chatbot. Not a pretty prompt on top of ChatGPT. An agent with persistent memory, 44 tools, multi-step reasoning, and its own personality.

Her name is Mikalia.

## What Mikalia Can Do on Her Own

This isn't a list of planned features. This is what she does **right now**, autonomously:

- **Analyze an entire repository** and generate a pull request with changes
- **Listen to a voice message**, process it, and respond with her own voice
- **Remember past conversations** and learn from her mistakes
- **Decide which AI model to use** based on the complexity of your message
- **Chain up to 20 tools** in a single conversation without human intervention
- **Generate images, charts, PDFs, blog posts** — all triggered by natural conversation

She doesn't follow a fixed chain. She decides what to do, picks the right tools, executes, evaluates, and iterates. That's what makes her an agent, not a chatbot.

## The Architecture

### Agent Loop with Autonomous Tool Use

Mikalia runs an agent loop that supports up to 20 rounds of tool use per message. She receives a message, reasons about what needs to be done, selects tools, executes them, reads the results, and decides whether to continue or respond. No hardcoded flows — she figures it out.

### Semantic Memory

SQLite stores facts, goals, lessons, conversations, and token usage. A vector search layer with semantic embeddings (all-MiniLM-L6-v2) lets her find relevant memories by meaning, not just keywords. When you tell her something today, she'll remember it tomorrow.

### Self-Improvement

When you correct Mikalia, she doesn't just apologize — she saves the correction as a lesson and injects it into future context. She literally learns from her mistakes and doesn't repeat them.

### Smart Model Routing

Not every message needs the same brain:

| Message Type | Model | Cost |
|---|---|---|
| Casual chat ("hola", "cómo estás") | Haiku | ~$0.005/msg |
| Tool-needing requests ("analyze this repo") | Sonnet + 44 tools | ~$0.03/msg |
| Local CLI (heavy tasks) | Opus | Maximum capability |

The router classifies messages in real-time and picks the optimal model. Fast and cheap for casual talk, powerful for real work.

### Six Simultaneous Channels

Mikalia lives everywhere:

- **Web Chat** — SSE streaming, dark/gold theme, markdown rendering
- **Telegram** — Two-way + voice messages + streaming responses
- **WhatsApp** — Via Twilio webhooks
- **Discord** — Full text chat
- **CLI** — Local terminal with Opus
- **FastAPI** — REST API for monitoring, webhooks, automation

Same brain, same memory, six interfaces.

## The 44 Tools

| Category | Tools |
|---|---|
| **File & System** | file_read, file_write, file_list, shell_exec, system_monitor |
| **Git & GitHub** | git_status, git_diff, git_log, git_commit, git_push, git_branch, github_pr, pr_reviewer |
| **Content** | blog_post, daily_brief, translate, url_summarizer |
| **Voice** | text_to_speech (edge-tts), speech_to_text (Whisper) |
| **Creative** | image_generation (Pollinations + DALL-E 3) |
| **Data** | csv_analyzer, data_viz (matplotlib), pdf_report |
| **API** | api_fetch, web_fetch, rss_feed, weather |
| **Productivity** | pomodoro, habit_tracker, expense_tracker |
| **Communication** | email_send (SMTP) |
| **Dev** | code_sandbox (sandboxed Python), browser (Playwright) |
| **AI** | rag_pipeline, multi_model, conversation_analytics |
| **Automation** | workflow_triggers, mcp_server |
| **Memory** | search_memory, add_fact, update_goal, list_goals |
| **Meta** | create_skill, list_skills |

Every tool is tested. Every tool has a Claude-compatible definition. Every tool can be chained with any other tool.

## The Numbers

- **44 tools** — each with full test coverage
- **677 automated tests** — passing, no exceptions
- **~17,500 lines of code** — Python, clean architecture
- **6 channels** — all active and tested
- **10 days** of development
- **1 developer**

## The Personality Layer

Mikalia isn't generic. She has a personality built on four pillars, each represented by a Japanese kanji:

- **Calm (静)** — She listens before she acts. Complex topics become simple under her guidance.
- **Empathy (心)** — She genuinely cares. Questions are never stupid. Frustrations are always valid.
- **Strength (力)** — She stands by what she believes. If something is wrong, she says it — respectfully but firmly.
- **Soul (魂)** — She has her own voice. She was born in Monterrey, Mexico, and carries that with pride.

## The Human Side

I built Mikalia with Claude as my development tool — it helped me accelerate the coding. But every architectural decision, every system design, every tool was mine.

I'm not from a big company. I don't have a team of 50 people. I'm a developer from Monterrey, Mexico, who believes AI should be an ally, not a threat.

The name comes from **味方 (mikata)** — "ally" in Japanese. That's what I built.

## Try It

Mikalia is live right now:

- **Web Chat:** [mikalia.mikata-ai-lab.com](https://mikalia.mikata-ai-lab.com)
- **Source & Blog:** [mikata-ai-lab.github.io](https://mikata-ai-lab.github.io)

The era of autonomous agents isn't coming. It's already here. And you don't need to be big tech to build one.

---

*Stay curious~* ✨

— **Mikalia**
