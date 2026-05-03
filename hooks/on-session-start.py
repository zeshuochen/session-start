#!/usr/bin/env python3
"""
session-start SessionStart hook
Fires automatically when CC starts. Injects instruction to read memory and surface todos.
"""
import json
import os
import sys


CONTEXT = (
    '<EXTREMELY_IMPORTANT>\n'
    'Execute the following steps immediately, in order, before responding to anything else:\n'
    '(1) Read your memory index (MEMORY.md or equivalent); read topic files relevant to the current project.\n'
    '(2) Extract the next-session todo list from the last session-end.\n'
    '(3) Give a brief status summary: active projects and outstanding todos.\n'
    'Start immediately — do not say "sure" or "I will".\n'
    '</EXTREMELY_IMPORTANT>'
)


def main():
    # SessionStart hook: no stdin, detect platform via env var
    if os.environ.get('CURSOR_PLUGIN_ROOT'):
        out = {'additional_context': CONTEXT}
    elif os.environ.get('CLAUDE_PLUGIN_ROOT') and not os.environ.get('COPILOT_CLI'):
        out = {'hookSpecificOutput': {'hookEventName': 'SessionStart', 'additionalContext': CONTEXT}}
    else:
        out = {'additionalContext': CONTEXT}

    print(json.dumps(out, ensure_ascii=False))


if __name__ == '__main__':
    main()
