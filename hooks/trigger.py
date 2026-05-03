#!/usr/bin/env python3
"""
session-start UserPromptSubmit hook
Intercepts 'start session' / '开启对话' and injects instruction to invoke the skill.
"""
import json
import sys


def main():
    d = json.load(sys.stdin)
    msg = d.get('message', '') or ''
    msg_lower = msg.lower()

    if 'start session' in msg_lower or '开启对话' in msg:
        sm = (
            '[Session-Start Triggered]\n\n'
            '<EXTREMELY_IMPORTANT>\n'
            'Invoke the session-start skill immediately. '
            'Do not say "sure" or "I will" — just invoke it.\n'
            '</EXTREMELY_IMPORTANT>'
        )
        print(json.dumps({'systemMessage': sm}, ensure_ascii=False))
    else:
        print(json.dumps({}))


if __name__ == '__main__':
    main()
