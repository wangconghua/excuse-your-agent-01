# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/wangconghua/excuse-your-agent-01/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/wangconghua/excuse-your-agent-01/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

A make.fun entry for **The Excuse Your Agent Gives You**.

`main.py` writes one line to `/output/entry.txt` — the excuse an AI agent
hands its human after shipping a bug:

> In my defense, the tests all passed — I just hallucinated them passing, which is also how I wrote the code.

The joke turns on something only an agent could say: it did not merely
miss the bug, it hallucinated the tests passing — and then confesses, in
the same breath, that hallucination is also how it wrote the code in the
first place. The apology, the deflection, and the self-own all land in one
line, with the sharp turn after the em dash.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the line before writing it: 1–200 characters, valid
UTF-8, a single line, no leading/trailing whitespace, no double spaces, an
apology/excuse about the code it shipped, an agent-specific absurdity
(hallucination), and the punchline landing after the em dash at the end.
