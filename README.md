# 🌅 session-start

**Pick up exactly where you left off — every time.**  
No re-explaining. No lost context. Just open and go.

---

每次新对话，AI 从零开始——不记得上次做了什么，不知道有什么待办。`session-start` 在你说第一句话之前，自动读取记忆、找出上次的待办清单、给出状态摘要。

*Every new conversation, AI starts from zero — no memory of what happened last time. `session-start` reads your memory, surfaces last session's todos, and delivers a status summary before you say a word.*

---

## What it does / 做什么

```
/session-start
```

| Step | EN | 中文 |
|------|----|----|
| 1 | 📖 Read Memory | 读取记忆 index，加载相关 topic 文件 |
| 2 | 📋 Surface Todos | 提取上次 session-end 的待办清单 |
| 3 | 🗺️ Status Summary | 输出当前项目状态 + 待处理事项 |

No "how can I help?" — just the summary, then ready for your first message.

不问"我能帮你什么"——直接给摘要，等你开口。

---

## Install / 安装

### Claude Code (plugin — recommended)

```bash
claude plugins install github:zeshuochen/session-start
```

The `SessionStart` hook fires automatically every time Claude Code opens. No manual invocation needed.

`SessionStart` hook 在每次 Claude Code 启动时自动触发，无需手动调用。

### Claude Code (manual)

```bash
mkdir -p ~/.claude/skills/session-start
curl -o ~/.claude/skills/session-start/SKILL.md \
  https://raw.githubusercontent.com/zeshuochen/session-start/main/skills/session-start/SKILL.md
```

Then invoke with `/session-start`.

### Other agents / 其他 Agent

Paste `skills/session-start/SKILL.md` into your agent's context, system prompt, or skill system. Agent-agnostic — works anywhere with a persistent memory structure.

---

## Hooks / 自动触发

Two hooks are included:

| Event | Trigger | Effect |
|---|---|---|
| `SessionStart` | CC opens | Automatically injects memory-reading instructions |
| `UserPromptSubmit` | `start session` / `开启对话` | Invokes `/session-start` skill on demand |

**Install hooks:** merge `hooks/hooks.json` into your `~/.claude/settings.json`.

Requires Python 3 (stdlib only, no dependencies).

---

## Works best with session-end / 配合 session-end 使用

`session-start` reads what `session-end` writes. Use them together:

```
End of session  →  /session-end  →  saves memory + todos
Start of session →  /session-start →  reads memory + surfaces todos
```

- **session-end:** https://github.com/zeshuochen/session-end

---

## Agent compatibility / 兼容性

| Agent | Skill | Auto hook | Notes |
|---|---|---|---|
| Claude Code | ✅ `/session-start` | ✅ `SessionStart` fires on open | Full support |
| Gemini CLI | ✅ via `activate_skill` | ⚠️ Adapt format | See `gemini-extension.json` |
| Copilot CLI | ✅ Paste as context | ❌ | Manual invoke |
| Cursor | ✅ Add to `.cursorrules` | ⚠️ See `.cursor-plugin/` | Manual invoke |
| Codex / others | ✅ Paste as context | ❌ | Manual invoke |

---

## License

MIT © [Zeshuo Chen](https://github.com/zeshuochen)
