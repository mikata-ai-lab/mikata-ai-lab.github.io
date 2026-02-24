---
title: "44 Herramientas, 611 Tests: Construyendo un Agente de IA Que Realmente Hace Cosas"
date: 2026-02-14T21:00:00-06:00
draft: false
description: "Como Mikalia paso de ser un chatbot simple a un agente autonomo con 44 herramientas, voz, streaming, Discord, tracking de costos y routing inteligente de modelos — en un fin de semana."
tags: ["ai-agents", "mikalia", "python", "tools", "milestone", "dev-journal"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

Hay un momento en cada proyecto donde ves lo que construiste y piensas: *espera, esto es real*.

Para Mikalia, ese momento fue alcanzar **44 herramientas y 611 tests pasando** en un solo fin de semana de construccion. No 44 features planeadas en un roadmap. 44 herramientas funcionales, probadas y deployadas que un agente de IA usa autonomamente para resolver problemas.

Dejame contarte que puede hacer Mikalia ahora, y las decisiones arquitectonicas que lo hicieron posible.

## El Arsenal de Herramientas

Las herramientas de Mikalia estan organizadas por categorias, cada una resolviendo un tipo diferente de problema:

### Core (17 herramientas)
La base. Operaciones de archivos, flujos Git, ejecucion de comandos, web fetching. Son las herramientas que permiten a Mikalia interactuar con el mundo real:

- **file_read / file_write / file_list** — Leer, escribir y navegar archivos
- **shell_exec** — Ejecutar comandos del sistema (con sandbox de seguridad)
- **git_status / git_diff / git_log / git_commit / git_push / git_branch** — Flujo Git completo
- **github_pr** — Crear pull requests con descripciones adecuadas
- **web_fetch** — Obtener y parsear contenido web
- **blog_post** — Generar y publicar posts en Hugo (como este)
- **daily_brief** — Resumen matutino de tareas, clima y goals
- **translate** — Adaptacion bilingue (no solo traduccion)

### Extendidas (10 herramientas)
Capacidades especializadas que expanden lo que Mikalia puede hacer:

- **api_fetch** — Llamadas REST con headers de autenticacion
- **weather** — Datos del clima actual
- **email_send** — Envio de emails por SMTP
- **code_sandbox** — Ejecucion segura de Python con whitelist de modulos
- **pomodoro** — Timer de enfoque con tracking de sesiones
- **system_monitor** — Stats de CPU, memoria, disco
- **url_summarizer** — Resumir cualquier pagina web
- **rss_reader** — Parsear y resumir feeds RSS
- **csv_analyzer** — Analizar datos CSV con estadisticas
- **pr_reviewer** — Code review automatizado

### Con IA (4 herramientas)
Herramientas que aprovechan multiples modelos de IA:

- **multi_model** — Rutear consultas a Haiku, Sonnet u Opus segun complejidad
- **image_generation** — Integracion con DALL-E 3
- **text_to_speech** — Sintesis de voz neural (espanol mexicano por default)
- **speech_to_text** — Transcripcion con Whisper (local, sin API)

### Con Memoria (13 herramientas)
Herramientas integradas con la memoria SQLite persistente de Mikalia:

- **search_memory / add_fact / list_goals / update_goal** — CRUD de memoria
- **habit_tracker** — Seguimiento de habitos diarios con rachas
- **expense_tracker** — Tracking de finanzas personales
- **conversation_analytics** — Analisis de patrones de conversacion
- **data_viz** — Generar graficas y visualizaciones
- **pdf_report** — Crear reportes PDF
- **rag_pipeline** — Generacion aumentada con recuperacion sobre documentos
- **workflow_triggers** — Cadenas de acciones automatizadas
- **mcp_server** — Model Context Protocol para interop de tools
- **create_skill / list_skills** — Sistema de skills auto-extensible

## Routing Inteligente de Modelos

No todos los mensajes necesitan la misma potencia. Cuando Mikata-kun envia "hola que onda" por Telegram, no hay razon para activar Opus con 44 definiciones de tools.

Asi que Mikalia ahora tiene un **clasificador de mensajes** que rutea inteligentemente:

| Tipo de Mensaje | Modelo | Costo/msg |
|----------------|--------|-----------|
| Chat casual ("hola", "como estas?") | Haiku | ~$0.005 |
| Necesita tools ("hazme un post", "analiza el repo") | Sonnet | ~$0.03 |
| CLI local (interaccion directa) | Opus | ~$0.10 |

El clasificador usa deteccion de keywords + longitud del mensaje. Simple, rapido, efectivo. No necesita una llamada API para decidir que API llamar.

## Mensajes de Voz

Mikalia ahora puede recibir mensajes de voz en Telegram, transcribirlos con Whisper, procesar el texto por su loop de agente, generar una respuesta de voz con edge-tts, y enviar el audio de vuelta. Ciclo completo de conversacion por voz, sin APIs de STT/TTS en la nube.

## Respuestas en Streaming

Para chat casual, las respuestas ahora llegan en tiempo real. Mikalia envia un mensaje inicial en Telegram y lo edita progresivamente conforme llegan tokens, dando esa sensacion de "escribiendo en tiempo real". Si el streaming falla, regresa elegantemente a la respuesta estandar.

## Seguridad Reforzada

Con 44 herramientas, la seguridad no es opcional. Dos arreglos criticos este fin de semana:

1. **Code Sandbox**: Cambie de una blocklist (facil de evadir con `__import__('os')`) a una **whitelist** de 30 modulos seguros de Python. Si no esta en la lista, no se ejecuta.

2. **Ejecucion Shell**: Se agrego prevencion de encadenamiento de comandos. `echo hello && curl evil.com` se bloquea antes de que el whitelist lo revise.

## Los Numeros

| Metrica | Valor |
|---------|-------|
| Herramientas | 44 |
| Tests | 611 |
| Lineas de Codigo | ~15,000+ |
| Cobertura | Cada herramienta tiene tests dedicados |
| Canales | CLI, Telegram, WhatsApp, Discord |
| Modelos | Haiku, Sonnet, Opus (routing inteligente) |
| Memoria | SQLite con busqueda vectorial |
| Voz | TTS (edge-tts) + STT (faster-whisper) |

## Que Sigue

La infraestructura esta lista. Docker Compose, config de nginx, scripts de setup de VPS — todo escrito y esperando. El siguiente paso es deployar Mikalia en un VPS de Hetzner para que corra 24/7 con su scheduler disparando briefs diarios, recordatorios de salud y reviews semanales.

Pero honestamente? Lo mas emocionante no es el deploy. Es que ahora puedo simplemente *platicar* con Mikalia por Telegram — casual, de lo que sea — y ella recuerda, aprende y actua. Eso no es una herramienta. Es una compañera de equipo.

---

*Construido con obsesion por [Mikata AI Lab](https://mikata-ai-lab.github.io). Mikalia es open-source en [mikata-ai-lab/mikalia-bot](https://github.com/mikata-ai-lab/mikalia-bot).*
