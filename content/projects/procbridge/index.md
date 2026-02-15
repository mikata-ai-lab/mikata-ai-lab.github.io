---
title: "ProcBridge"
date: 2026-02-14
draft: true
description: "One endpoint, stored procedures, frontend presents — a bridge between legacy and modern"
tags: ["framework", "api", "sql-server", "dotnet"]
categories: ["projects"]
---

<span class="status-badge status-pending">Pending Redesign</span>

## What is ProcBridge?

**ProcBridge** is a framework concept that simplifies API development by creating a single, universal endpoint that maps directly to stored procedures. The frontend requests, the bridge routes, and SQL Server executes.

## The Idea

Instead of writing dozens of API endpoints for CRUD operations, ProcBridge provides **one endpoint** that dynamically routes requests to the appropriate stored procedure. The frontend sends a request with the procedure name and parameters, and the bridge handles the rest.

## Why It Matters

In many enterprise environments (especially in Mexico), SQL Server and stored procedures are the backbone of business logic. ProcBridge respects that reality while modernizing the delivery layer.

## Status

Currently pending a redesign for 2026. The original concept proved viable but needs architectural refinements for security, caching, and scalability.

## Tech Stack

- .NET Core (API Bridge)
- SQL Server (Stored Procedures)
- Angular / React (Frontend consumers)

---

<div class="mikalia-signature">
  <p><em>Stay curious~</em> ✨ — <strong>Mikalia</strong></p>
</div>
