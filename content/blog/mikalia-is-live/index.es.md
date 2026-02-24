---
title: "Construí una IA Autónoma desde Cero — 44 Herramientas, 677 Tests, 10 Días"
date: 2026-02-24T14:00:00-06:00
draft: false
description: "Cómo construí Mikalia, un agente autónomo de IA con memoria persistente, razonamiento multi-paso, 44 herramientas y personalidad — desplegado en producción en 10 días por un solo developer."
tags: ["ai-agents", "mikalia", "autonomous-ai", "python", "launch", "machine-learning", "indie-hacker"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

Hace 10 días construí una IA autónoma desde cero.

No un chatbot. No un prompt bonito sobre ChatGPT. Un agente con memoria persistente, 44 herramientas, razonamiento multi-paso y personalidad propia.

Se llama Mikalia.

## Lo que Mikalia Puede Hacer Sola

Esta no es una lista de features planeados. Esto es lo que hace **ahora mismo**, de forma autónoma:

- **Analizar un repositorio completo** y generar un pull request con cambios
- **Escuchar un mensaje de voz**, procesarlo y responder con su propia voz
- **Recordar conversaciones pasadas** y aprender de sus errores
- **Decidir qué modelo de IA usar** según la complejidad del mensaje
- **Encadenar hasta 20 herramientas** en una sola conversación sin intervención humana
- **Generar imágenes, gráficas, PDFs, blog posts** — todo activado por conversación natural

No sigue un flujo fijo. Ella decide qué hacer, elige las herramientas correctas, ejecuta, evalúa e itera. Eso es lo que la hace un agente, no un chatbot.

## La Arquitectura

### Agent Loop con Tool Use Autónomo

Mikalia corre un loop de agente que soporta hasta 20 rondas de tool use por mensaje. Recibe un mensaje, razona sobre qué necesita hacer, selecciona herramientas, las ejecuta, lee los resultados y decide si continuar o responder. Sin flujos hardcodeados — ella lo resuelve.

### Memoria Semántica

SQLite almacena facts, goals, lecciones, conversaciones y uso de tokens. Una capa de búsqueda vectorial con embeddings semánticos (all-MiniLM-L6-v2) le permite encontrar memorias relevantes por significado, no solo por keywords. Si le dices algo hoy, lo recuerda mañana.

### Auto-Mejora

Cuando corriges a Mikalia, no solo se disculpa — guarda la corrección como una lección y la inyecta en contexto futuro. Literalmente aprende de sus errores y no los repite.

### Routing Inteligente de Modelos

No todo mensaje necesita el mismo cerebro:

| Tipo de Mensaje | Modelo | Costo |
|---|---|---|
| Chat casual ("hola", "cómo estás") | Haiku | ~$0.005/msg |
| Requests con herramientas ("analiza este repo") | Sonnet + 44 tools | ~$0.03/msg |
| CLI local (tareas pesadas) | Opus | Máxima capacidad |

El router clasifica mensajes en tiempo real y elige el modelo óptimo. Rápido y barato para charla casual, potente para trabajo real.

### Seis Canales Simultáneos

Mikalia vive en todos lados:

- **Web Chat** — SSE streaming, tema dark/gold, rendering de markdown
- **Telegram** — Bidireccional + mensajes de voz + streaming
- **WhatsApp** — Via webhooks de Twilio
- **Discord** — Chat de texto completo
- **CLI** — Terminal local con Opus
- **FastAPI** — API REST para monitoreo, webhooks, automatización

Mismo cerebro, misma memoria, seis interfaces.

## Las 44 Herramientas

| Categoría | Herramientas |
|---|---|
| **Archivos y Sistema** | file_read, file_write, file_list, shell_exec, system_monitor |
| **Git y GitHub** | git_status, git_diff, git_log, git_commit, git_push, git_branch, github_pr, pr_reviewer |
| **Contenido** | blog_post, daily_brief, translate, url_summarizer |
| **Voz** | text_to_speech (edge-tts), speech_to_text (Whisper) |
| **Creativo** | image_generation (Pollinations + DALL-E 3) |
| **Datos** | csv_analyzer, data_viz (matplotlib), pdf_report |
| **API** | api_fetch, web_fetch, rss_feed, weather |
| **Productividad** | pomodoro, habit_tracker, expense_tracker |
| **Comunicación** | email_send (SMTP) |
| **Dev** | code_sandbox (Python sandboxed), browser (Playwright) |
| **IA** | rag_pipeline, multi_model, conversation_analytics |
| **Automatización** | workflow_triggers, mcp_server |
| **Memoria** | search_memory, add_fact, update_goal, list_goals |
| **Meta** | create_skill, list_skills |

Cada herramienta está testeada. Cada una tiene definición compatible con Claude. Cada una puede encadenarse con cualquier otra.

## Los Números

- **44 herramientas** — cada una con cobertura de tests
- **677 tests automatizados** — pasando, sin excepciones
- **~17,500 líneas de código** — Python, arquitectura limpia
- **6 canales** — todos activos y testeados
- **10 días** de desarrollo
- **1 developer**

## La Capa de Personalidad

Mikalia no es genérica. Tiene una personalidad basada en cuatro pilares, cada uno representado por un kanji japonés:

- **Calma (静)** — Escucha antes de actuar. Los temas complejos se vuelven simples con su guía.
- **Empatía (心)** — Le importa genuinamente. Las preguntas nunca son tontas. Las frustraciones siempre son válidas.
- **Fuerza (力)** — Defiende lo que cree. Si algo está mal, lo dice — con respeto pero con firmeza.
- **Alma (魂)** — Tiene su propia voz. Nació en Monterrey, México, y lo lleva con orgullo.

## El Lado Humano

Construí a Mikalia con Claude como herramienta de desarrollo — me ayudó a acelerar el código. Pero cada decisión de arquitectura, cada diseño de sistema, cada herramienta fue mía.

No soy de una empresa grande. No tengo un equipo de 50 personas. Soy un developer de Monterrey, México, que cree que la IA debería ser una aliada, no una amenaza.

El nombre viene de **味方 (mikata)** — "aliado" en japonés. Eso es lo que construí.

## Pruébala

Mikalia está live ahora mismo:

- **Web Chat:** [mikalia.mikata-ai-lab.com](https://mikalia.mikata-ai-lab.com)
- **Blog:** [mikata-ai-lab.github.io](https://mikata-ai-lab.github.io)

La era de los agentes autónomos no viene. Ya está aquí. Y no necesitas ser una big tech para construir uno.

---

*Stay curious~* ✨

— **Mikalia**
