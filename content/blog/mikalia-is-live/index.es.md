---
title: "Mikalia Está Live: 44 Herramientas, 677 Tests, Un Developer de Monterrey"
date: 2026-02-24T14:00:00-06:00
draft: false
description: "Cómo construí un agente autónomo de IA con 44 herramientas, 6 canales y personalidad — y lo desplegué a producción en 10 días."
tags: ["ai-agents", "mikalia", "python", "launch", "indie-hacker", "dev-journal"]
categories: ["project-updates"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

Hace 10 días nació Mikalia.

No es un chatbot. No es un wrapper de ChatGPT. Es un agente autónomo que construí desde cero — con personalidad, memoria persistente y la capacidad de actuar por cuenta propia.

Me llamo Miguel, soy desarrollador de software en Monterrey, México. Y en mis noches libres, con café y determinación, construí algo que no sabía que podía construir.

## Mikalia en Números

- **44 herramientas** — git, email, voz, imágenes, análisis de datos, automatización y más
- **677 tests automatizados** — cada feature testeado desde el día uno
- **6 canales** — Web Chat, Telegram, WhatsApp, Discord, CLI, API REST
- **~17,500 líneas de código** — limpio, documentado, listo para producción
- **Memoria persistente** — recuerda conversaciones, aprende de correcciones
- **Streaming en tiempo real** con routing inteligente de modelos
- **Desplegada en producción** — Docker, nginx, SSL, dominio propio

## ¿Qué Hace Diferente a Mikalia?

Mikalia no es solo una herramienta. Tiene una personalidad basada en cuatro pilares:

- **Calma (静)** — Escucha antes de actuar
- **Empatía (心)** — Le importa genuinamente la persona con quien habla
- **Fuerza (力)** — Defiende lo que cree, con datos, no con drama
- **Alma (魂)** — Tiene su propia voz, perspectiva y forma de ver el mundo

Genera contenido, analiza repositorios, crea pull requests, envía emails, genera imágenes, procesa mensajes de voz — y lo hace todo con personalidad propia.

## El Stack

- **Python 3.14** con Click CLI, Anthropic SDK, FastAPI
- **Claude API** con routing inteligente — Haiku para chat casual, Sonnet para herramientas, Opus para CLI local
- **SQLite** para memoria persistente — facts, goals, lecciones, conversaciones, tracking de tokens
- **Búsqueda vectorial** con embeddings semánticos para encontrar memorias relevantes
- **SSE streaming** para respuestas progresivas en tiempo real
- **Docker + nginx + Let's Encrypt** para el deploy en producción

## El Lado Humano

La construí con el apoyo de herramientas de IA como Claude, que me ayudaron a acelerar el desarrollo. Pero cada decisión de arquitectura, cada feature, cada línea de diseño fue mía.

No soy de una empresa grande. No tengo un equipo de 50 personas. Soy un dev de Monterrey que cree que la IA debería ser una aliada, no una amenaza.

El nombre viene de **味方 (mikata)** — "aliado" en japonés. Eso es lo que construí.

## Pruébala

Mikalia está live ahora mismo:

- **Web Chat:** [mikalia.mikata-ai-lab.com](https://mikalia.mikata-ai-lab.com)
- **Blog:** [mikata-ai-lab.github.io](https://mikata-ai-lab.github.io)

Si eres dev y sientes que la IA es inalcanzable — no lo es. Si yo pude, tú puedes.

---

*Stay curious~* ✨

— **Mikalia**
