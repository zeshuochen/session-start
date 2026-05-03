# session-start — Contributor Guidelines

## Overview

`session-start` is a single-skill plugin providing a structured opening ritual for AI coding sessions. It reads memory, surfaces the previous session's todo list, and gives a status summary — before responding to anything else.

## Contribution Principles

- **Keep it agent-agnostic.** Steps must work on any AI agent with a persistent memory system.
- **No opinion on memory format.** The skill references `MEMORY.md` as an example; users may use any memory structure.
- **No new dependencies.** Hooks use stdlib Python only (`json`, `os`, `sys`).
- **One skill, one job.** This plugin handles session opening. Closing belongs in `session-end`.

## File structure

```
.claude-plugin/plugin.json         ← Claude Code manifest
.cursor-plugin/plugin.json         ← Cursor manifest
skills/session-start/SKILL.md      ← The skill content
hooks/hooks.json                   ← SessionStart + UserPromptSubmit config
hooks/on-session-start.py          ← SessionStart event handler
hooks/trigger.py                   ← UserPromptSubmit keyword trigger
gemini-extension.json              ← Gemini CLI support
GEMINI.md                          ← Gemini context include
```
