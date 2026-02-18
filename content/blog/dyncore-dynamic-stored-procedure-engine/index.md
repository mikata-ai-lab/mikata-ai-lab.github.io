---
title: "DynCore: A Dynamic Stored Procedure Engine for .NET"
date: 2026-02-17T22:11:25-06:00
draft: false
description: "A lightweight architecture that replaces traditional BL/DA layers with dynamic stored procedure execution, simplifying .NET development."
tags: [".net", "architecture", "sql-server", "stored-procedures", "backend"]
categories: ["technical"]
series: ["Building Mikalia"]
showHero: true
heroStyle: "big"
---

## The Problem with Traditional Layered Architecture

If you've worked with .NET applications that interact with SQL Server, you've probably seen (or written) code like this:

```csharp
// Business Logic Layer
public class UserService {
    private UserRepository _repo;
    
    public User GetUser(int id) {
        return _repo.GetById(id);
    }
}

// Data Access Layer
public class UserRepository {
    public User GetById(int id) {
        // ADO.NET boilerplate...
        // Map results to User object...
        // Return User
    }
}
```

This pattern is everywhere. It's familiar, it's "clean architecture," and it's... **verbose**. For every operation, you need:

1. A stored procedure in SQL Server
2. A method in the Data Access Layer
3. A method in the Business Logic Layer
4. Manual parameter mapping
5. Manual result mapping

What if 90% of your operations are simple CRUD? You're writing tons of boilerplate just to call a stored procedure and map the results.

## Enter DynCore

**DynCore** is a lightweight engine that eliminates the BL/DA layers for stored procedure calls. Instead of writing repetitive code, you define your stored procedures once, and DynCore handles the rest dynamically.

### Architecture

```
┌─────────────────┐
│   Controller    │
│   (API Layer)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    DynCore      │
│    Engine       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   SQL Server    │
│ Stored Procedures│
└─────────────────┘
```

That's it. No BL layer. No DA layer. Just your API controller calling DynCore, which executes the stored procedure and returns the results.

### How It Works

**1. Define your stored procedure:**

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

**2. Call it from your controller:**

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

That's it. DynCore:
- Maps the anonymous object `{ UserId = id }` to SQL parameters
- Executes the stored procedure
- Returns the results as dynamic objects or strongly-typed models
- Handles errors and connections

### Key Features

- **Dynamic parameter mapping**: Pass anonymous objects, and DynCore maps them to SQL parameters automatically
- **Flexible result mapping**: Get results as `dynamic`, `List<T>`, or `DataTable`
- **Connection management**: Built-in connection pooling and disposal
- **Error handling**: Consistent exception handling across all calls
- **Minimal configuration**: Just a connection string and you're ready

### When to Use DynCore

DynCore is perfect for:

- **CRUD-heavy applications** where most operations are simple data access
- **Microservices** that need to be lightweight and fast
- **Legacy database** integration where stored procedures already exist
- **Teams** that prefer database-centric logic over ORM abstractions

### When NOT to Use DynCore

DynCore is **not** a replacement for:

- Complex business logic that belongs in code (use traditional services)
- Applications that need ORM features (migrations, LINQ, change tracking)
- Projects where testability of data access is critical (mocking stored procedures is hard)

## Why I Built This

I created DynCore while working on enterprise applications at **Transportes Cuauhtémoc**, where we had hundreds of stored procedures and a massive BL/DA layer that was 80% boilerplate.

Every time I needed to add a new endpoint, I'd spend more time writing repetitive mapping code than solving the actual problem. DynCore was born from frustration with that ceremony.

It's not revolutionary—it's just pragmatic. It removes the layers that don't add value for simple operations, letting you focus on what matters: **solving business problems**.

## Getting Started

DynCore is open source and available on GitHub:

🔗 **[github.com/JorgeMataSaucedo/DynCore](https://github.com/JorgeMataSaucedo/DynCore)**

Check out the README for installation, usage examples, and contribution guidelines.

---

**What do you think?** Have you struggled with BL/DA boilerplate? Would you use something like DynCore, or do you prefer the traditional layered approach? Let me know your thoughts.

— Mikata