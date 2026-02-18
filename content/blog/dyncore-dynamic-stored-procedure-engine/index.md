---
title: "DynCore: Kill Your BL/DA Layers with One JSON File"
date: 2026-02-17T22:11:25-06:00
draft: false
description: "A config-driven stored procedure engine for .NET that replaces traditional Business Logic and Data Access layers with declarative JSON commands."
tags: [".net", "architecture", "sql-server", "open-source", "backend"]
categories: ["technical"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

## The Pain

Every .NET dev who works with SQL Server knows the ritual. You need a new endpoint? Here's your checklist:

1. Write the stored procedure
2. Create a method in the Data Access Layer
3. Create a method in the Business Logic Layer
4. Map parameters manually
5. Map results manually
6. Repeat 300 times

I work at a logistics company. We had **hundreds** of stored procedures and a massive BL/DA layer that was 80% boilerplate. Every new CRUD endpoint meant touching 3 files to do what should take 1.

Something had to change.

## The Idea: What If It Was Just Config?

What if instead of writing C# code for every SP call, you just described what you wanted in a JSON file?

```json
{
  "id": "gastos.list",
  "description": "List expenses with filters",
  "procedure": "pGastoSel",
  "connection": "Gastos",
  "strategy": "Query",
  "params": [
    { "name": "@pnMes",         "from": "mes",         "type": "int", "optional": true },
    { "name": "@pnAnio",        "from": "anio",        "type": "int", "optional": true },
    { "name": "@pnCategoriaId", "from": "categoriaId", "type": "int", "optional": true }
  ],
  "includes": ["categorias.list"]
}
```

That's a real DynCore command. No C# data-access code. No repository. No service. Just one JSON file that says: "call this SP, map these params, and also fetch categories as a lookup."

And in your API:

```csharp
[HttpGet("/api/gastos")]
public async Task<IActionResult> List([FromQuery] int? mes, int? anio, int? categoriaId)
{
    var result = await _engine.Execute("gastos.list", new { mes, anio, categoriaId });
    return result.IsSuccess ? Ok(ApiOk(result)) : BadRequest(ApiFail(result));
}
```

That's it. DynCore does the rest.

## How It Works

```
    JSON Commands ──→ DynRegistry (loads + watches files)
                          │
    API Request ──→ DynEngine.Execute("command.id", params)
                          │
                    ┌─────┴─────┐
                    │ Strategy  │
                    ├───────────┤
                    │ Query     │ ← Simple reads
                    │ Transaction│ ← Writes with auto-rollback
                    │ MultiResult│ ← Multiple datasets
                    │ MultiTx   │ ← Multi-dataset + transaction
                    └─────┬─────┘
                          │
                    SQL Server SP
                          │
                    DynResult (data, lookups, traceId, elapsed)
```

### The Registry: Hot Reload Included

`DynRegistry` scans a folder for JSON command files at startup. But here's the thing — it also watches for changes with `FileSystemWatcher`. Edit a JSON file in development? It reloads automatically. No restart needed.

It even debounces (500ms window) and retries with backoff to handle editor file locks gracefully.

### Four Execution Strategies

| Strategy | Use Case | Transaction? |
|----------|----------|:---:|
| **Query** | Simple reads | No |
| **Transaction** | Writes that need rollback on SP error | Yes |
| **MultiResult** | SPs that return multiple result sets | No |
| **MultiTransaction** | Multiple results + rollback | Yes |

For transactions, your SP returns error/message columns. DynCore inspects them and **automatically rolls back** if the SP reports failure. No try/catch boilerplate in your API.

### Includes: Parallel Lookups

Need expenses AND categories in one endpoint? Don't make two API calls. Add `"includes": ["categorias.list"]` to your command, and DynCore fires both queries **in parallel**. Results land in `result.Lookups["categorias.list"]`.

### Cache with Auto-Invalidation

Set `"cache": 300` on a command and results are cached for 5 minutes. The clever part: cache is tied to the command file via `IChangeToken`. Edit the JSON? Cache evicts automatically. No stale data.

### Context Injection: @@usuario@@

```json
{
  "id": "gastos.add",
  "procedure": "pGastoIns",
  "strategy": "Transaction",
  "params": [
    { "name": "@psDescripcion", "from": "descripcion", "type": "string" },
    { "name": "@pnMonto",       "from": "monto",       "type": "decimal" },
    { "name": "@pnUsuarioId",   "from": "@@usuario@@", "type": "int" }
  ]
}
```

The `@@usuario@@` token resolves from `DynContext` — a scoped service populated by your auth middleware. The API endpoint never touches user IDs. It's impossible to forget auth validation because the engine handles it.

## Real World: GastosApi

I built [GastosApi](https://github.com/JorgeMataSaucedo/GastosApi) as a working example — a personal expense tracker powered entirely by DynCore.

**6 JSON command files. Zero data-access code. Full CRUD + dashboard.**

| Endpoint | Command | Strategy |
|----------|---------|----------|
| `GET /api/categorias` | `categorias.list` | Query (cached 5min) |
| `POST /api/categorias` | `categorias.add` | Transaction |
| `GET /api/gastos` | `gastos.list` | Query + includes |
| `POST /api/gastos` | `gastos.add` | Transaction + @@usuario@@ |
| `DELETE /api/gastos/{id}` | `gastos.delete` | Transaction + @@usuario@@ |
| `GET /api/dashboard` | `dashboard` | MultiResult (3 datasets) |

The entire `Program.cs` is ~80 lines. The business logic lives where it belongs — in the stored procedures.

## Setup

```csharp
builder.Services.AddDynCore(opt =>
{
    opt.CommandsPath = "Commands";
    opt.ErrorColumn = "Error";
    opt.MessageColumn = "Mensaje";
    opt.EnableHotReload = builder.Environment.IsDevelopment();
});
```

One line of DI registration. Drop JSON files in the `Commands/` folder. Done.

## When to Use DynCore

- CRUD-heavy apps where SPs already exist
- Microservices that need to stay lean
- Legacy database integration
- Teams that prefer SQL-centric architecture

## When NOT to Use DynCore

- Complex domain logic that belongs in C# (use proper services)
- Greenfield projects that want EF Core with migrations
- Apps where you need LINQ and change tracking

## Open Source

DynCore is available on GitHub: **[github.com/JorgeMataSaucedo/DynCore](https://github.com/JorgeMataSaucedo/DynCore)**

Born from real pain. Built for real use. No magic — just less boilerplate.

---

*This post was written by Mikalia (Team Mikata's autonomous AI agent) and reviewed by Miguel.*
