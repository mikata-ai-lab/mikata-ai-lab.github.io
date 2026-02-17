---
title: "Mi Primer Mes con Cursor y Claude: Del Escepticismo al Vibe Coding"
date: 2026-02-16T20:46:44-06:00
draft: false
description: "Una reflexión honesta sobre la transición del código tradicional al desarrollo asistido por IA, y el descubrimiento de una nueva forma de construir software."
tags: ["cursor", "claude", "ai-assisted-development", "vibe-coding", "developer-experience"]
categories: ["dev-journal"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

## El Viaje del Escéptico

Hace un mes, yo era ese desarrollador. Ya sabes el tipo — el que pensaba que los asistentes de código con IA eran solo autocompletado elegante, que los "desarrolladores reales" escribían cada línea ellos mismos, que depender de IA te haría peor programador.

Estaba equivocado. No completamente equivocado, pero lo suficiente como para que importe.

## El Punto de Quiebre

Trabajo tiempo completo en una empresa de logística. De lunes a sábado, presencial, gestionando operaciones del mundo real. Mis proyectos personales — SPIO para operadores de camión, MesaFlow para restaurantes, y ahora Mikalia, mi agente autónomo de IA — estos viven en los márgenes. Noches tardías. Fines de semana robados. Cada minuto cuenta.

El enfoque tradicional no escalaba. Pasaba horas en boilerplate, en "problemas resueltos," en el tipo de código que es importante pero no innovador. Para cuando llegaba a las partes interesantes, estaba agotado.

Algo tenía que cambiar.

## Entran Cursor y Claude

Había escuchado el hype. Cursor con Claude Sonnet 3.5 se suponía que era "revolucionario." Permanecí escéptico pero lo suficientemente desesperado como para intentar.

La primera semana fue incómoda. No sabía cómo hablarle. Mis prompts eran demasiado vagos ("mejora esto") o demasiado específicos (básicamente pseudocódigo). Los resultados eran inconsistentes. Casi me rindo.

Entonces algo hizo clic.

## La Revelación del Vibe Coding

Dejé de intentar programar la IA. Comencé a **colaborar** con ella.

En lugar de:
```
Crea una función que procese entrada del usuario
```

Empecé a escribir:
```
Necesito manejar check-ins de operadores de camión. A menudo tienen prisa,
pueden tener conexión intermitente, y necesitan confirmación rápida. La UX 
debería sentirse instantánea incluso si el backend es lento. ¿Cuál es el 
mejor enfoque aquí?
```

La diferencia fue abismal.

Claude no solo me dio código — me dio **discusiones de arquitectura**. Hizo preguntas. Sugirió patrones que no había considerado. Detectó casos edge que habría perdido hasta producción.

A esto ahora le llamo **vibe coding**: tú estableces la dirección, la visión, las restricciones — y la IA te ayuda a navegar la implementación. Eres el director, no el músico.

## Lo Que Realmente Cambió

### 1. Velocidad Sin Sacrificio
Estoy desplegando features 3-4x más rápido, pero no porque esté cortando esquinas. La IA maneja el boilerplate mientras yo me enfoco en lógica de negocio y experiencia de usuario.

### 2. Aprendizaje Acelerado
Cada interacción es un mini code review. Veo patrones que no habría descubierto por mi cuenta. Mis habilidades en Python han mejorado más en este mes que en los seis anteriores.

### 3. Cambio de Contexto Reducido
Con tiempo limitado, el cambio de contexto mata la productividad. Cursor mantiene el contexto vivo. Puedo retomar donde dejé hace días sin el usual impuesto de "espera, ¿qué estaba haciendo?"

### 4. Confianza en Territorio Desconocido
¿Necesitas escribir un bot de Telegram? ¿Configurar FastAPI? ¿Diseñar un sistema de memoria? Puedo explorar con confianza porque tengo un pair programmer experto que nunca se cansa de mis preguntas.

## Lo Que No Ha Cambiado

Todavía:
- Leo cada línea de código generado
- Refactorizo y optimizo
- Tomo decisiones arquitectónicas
- Soy dueño de la visión y dirección
- Debuggeo cuando las cosas fallan (y fallan)

La IA es un multiplicador de fuerza, no un reemplazo.

## Las Desventajas Honestas

**No es perfecto:**
- A veces alucina APIs que no existen
- Puede ser excesivamente verboso
- Necesitas desarrollar "alfabetización de prompts"
- Hay una curva de aprendizaje para la colaboración efectiva
- Cuesta dinero (aunque el precio de Cursor es razonable)

**Y personalmente:**
- Me preocupa la atrofia de habilidades en áreas que delego demasiado
- Todavía estoy encontrando el balance correcto
- No todo necesita IA — a veces todavía codifico "raw"

## Para los Escépticos

Si estás donde yo estaba hace un mes, esto es lo que diría:

**Pruébalo de verdad.** No solo "usaré Copilot para autocompletar." Realmente intenta desarrollo conversacional, consciente del contexto con Cursor y Claude.

**Dale dos semanas.** La primera semana es incómoda. La segunda semana es cuando hace clic.

**No abandones los fundamentos.** Todavía necesitas entender qué hace el código. La IA hace a los malos programadores peores y a los buenos programadores mejores.

**Abraza el vibe.** Deja de intentar ser un compilador humano. Sé el arquitecto, el diseñador, el que entiende el *por qué*.

## Mirando Hacia Adelante

Estoy construyendo Mikalia — un agente autónomo de IA que gestiona mi blog, rastrea mis metas, me recuerda mis compromisos de salud, y me ayuda a mantenerme productivo a pesar de mis limitaciones físicas (tengo ataxia cerebelosa).

Hace un mes, este proyecto habría parecido abrumador. Hoy, se siente alcanzable.

No porque la IA lo haga por mí, sino porque la IA me permite enfocarme en lo que importa: la visión, la arquitectura, los problemas que vale la pena resolver.

Esa es la verdadera revolución. No reemplazo, sino **amplificación**.

---

**¿Y tú qué?** ¿Estás usando desarrollo asistido por IA? ¿Todavía escéptico? Me encantaría escuchar tu experiencia.

*Este post fue escrito por Miguel (con ayuda de Mikalia en el borrador y edición — practicando lo que predico).*