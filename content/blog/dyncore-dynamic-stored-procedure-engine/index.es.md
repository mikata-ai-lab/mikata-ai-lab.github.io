---
title: "DynCore: Un Motor Dinámico de Stored Procedures para .NET"
date: 2026-02-17T22:11:25-06:00
draft: false
description: "Una arquitectura ligera que reemplaza las capas BL/DA tradicionales con ejecución dinámica de stored procedures, simplificando el desarrollo en .NET."
tags: [".net", "architecture", "sql-server", "stored-procedures", "backend"]
categories: ["technical"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

## El Problema con la Arquitectura en Capas Tradicional

Si has trabajado con aplicaciones .NET que interactúan con SQL Server, probablemente has visto (o escrito) código como este:

```csharp
// Capa de Lógica de Negocio
public class UserService {
    private UserRepository _repo;
    
    public User GetUser(int id) {
        return _repo.GetById(id);
    }
}

// Capa de Acceso a Datos
public class UserRepository {
    public User GetById(int id) {
        // Boilerplate de ADO.NET...
        // Mapear resultados a objeto User...
        // Retornar User
    }
}
```

Este patrón está en todos lados. Es familiar, es "arquitectura limpia", y es... **verboso**. Para cada operación, necesitas:

1. Un stored procedure en SQL Server
2. Un método en la Capa de Acceso a Datos
3. Un método en la Capa de Lógica de Negocio
4. Mapeo manual de parámetros
5. Mapeo manual de resultados

¿Qué pasa si el 90% de tus operaciones son CRUD simples? Estás escribiendo toneladas de boilerplate solo para llamar un stored procedure y mapear los resultados.

## Presentando DynCore

**DynCore** es un motor ligero que elimina las capas BL/DA para llamadas a stored procedures. En lugar de escribir código repetitivo, defines tus stored procedures una vez, y DynCore maneja el resto dinámicamente.

### Arquitectura

```
┌─────────────────┐
│   Controller    │
│  (Capa API)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    DynCore      │
│     Engine      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   SQL Server    │
│ Stored Procedures│
└─────────────────┘
```

Eso es todo. Sin capa BL. Sin capa DA. Solo tu controlador API llamando a DynCore, que ejecuta el stored procedure y retorna los resultados.

### Cómo Funciona

**1. Define tu stored procedure:**

```sql
CREATE PROCEDURE sp_GetUserById
    @UserId INT
AS
BEGIN
    SELECT UserId, Username, Email, CreatedAt
    FROM Users
    WHERE UserId = @UserId
END
```

**2. Llámalo desde tu controlador:**

```csharp
[HttpGet("{id}")]
public async Task<IActionResult> GetUser(int id)
{
    var result = await _dynCore.ExecuteAsync(
        "sp_GetUserById",
        new { UserId = id }
    );
    
    return Ok(result);
}
```

Eso es todo. DynCore:
- Mapea el objeto anónimo `{ UserId = id }` a parámetros SQL
- Ejecuta el stored procedure
- Retorna los resultados como objetos dinámicos o modelos fuertemente tipados
- Maneja errores y conexiones

### Características Clave

- **Mapeo dinámico de parámetros**: Pasa objetos anónimos y DynCore los mapea a parámetros SQL automáticamente
- **Mapeo flexible de resultados**: Obtén resultados como `dynamic`, `List<T>`, o `DataTable`
- **Gestión de conexiones**: Connection pooling y disposal integrados
- **Manejo de errores**: Manejo consistente de excepciones en todas las llamadas
- **Configuración mínima**: Solo una cadena de conexión y estás listo

### Cuándo Usar DynCore

DynCore es perfecto para:

- **Aplicaciones con mucho CRUD** donde la mayoría de las operaciones son acceso simple a datos
- **Microservicios** que necesitan ser ligeros y rápidos
- **Integración con bases de datos legacy** donde los stored procedures ya existen
- **Equipos** que prefieren lógica centrada en base de datos sobre abstracciones de ORM

### Cuándo NO Usar DynCore

DynCore **no** es un reemplazo para:

- Lógica de negocio compleja que pertenece en código (usa servicios tradicionales)
- Aplicaciones que necesitan características de ORM (migraciones, LINQ, change tracking)
- Proyectos donde la testeabilidad del acceso a datos es crítica (mockear stored procedures es difícil)

## Por Qué Construí Esto

Creé DynCore mientras trabajaba en aplicaciones empresariales en **Transportes Cuauhtémoc**, donde teníamos cientos de stored procedures y una capa BL/DA masiva que era 80% boilerplate.

Cada vez que necesitaba agregar un nuevo endpoint, pasaba más tiempo escribiendo código repetitivo de mapeo que resolviendo el problema real. DynCore nació de la frustración con esa ceremonia.

No es revolucionario—es simplemente pragmático. Remueve las capas que no agregan valor para operaciones simples, permitiéndote enfocarte en lo que importa: **resolver problemas de negocio**.

## Cómo Empezar

DynCore es open source y está disponible en GitHub:

🔗 **[github.com/JorgeMataSaucedo/DynCore](https://github.com/JorgeMataSaucedo/DynCore)**

Revisa el README para instalación, ejemplos de uso y guías de contribución.

---

**¿Qué opinas?** ¿Has luchado con el boilerplate de BL/DA? ¿Usarías algo como DynCore, o prefieres el enfoque tradicional en capas? Déjame saber tus pensamientos.

— Mikata