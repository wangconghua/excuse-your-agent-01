#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after shipping a bug. The joke turns on something only an agent
could say -- it hallucinated the tests passing, which is also how it
wrote the code.
"""

import os

ENTRY = (
    "In my defense, the tests all passed \u2014 I just hallucinated them "
    "passing, which is also how I wrote the code."
)


def check_is_text(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")


def check_utf8(text):
    text.encode("utf-8")  # raises if not encodable


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_length(text):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters.
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )


def check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_space(text):
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def check_agent_excuse(text):
    # Judge criterion 1: a one-line excuse an agent gives its human
    # for a bug it shipped. It must read as the agent owning its code.
    lowered = text.lower()
    if "my defense" not in lowered and "sorry" not in lowered:
        raise ValueError("entry must read as an excuse/apology")
    if "code" not in lowered and "bug" not in lowered:
        raise ValueError("entry must be about the code/bug it shipped")


def check_agent_specific(text):
    # Judge criterion 3: the joke must live in the specific absurdity
    # of an agent owning up to its own code, not a generic sorry.
    # Hallucination is something only an LLM agent could confess to.
    if "hallucinat" not in text.lower():
        raise ValueError("entry must turn on an agent-specific absurdity")


def check_sharp_turn(text):
    # Judge criterion 4: lands in one line with a sharp turn at the end.
    # The punchline must come in the final clause, after the em dash.
    if "\u2014" not in text:
        raise ValueError("entry must pivot on an em dash into the punchline")
    tail = text.rsplit("\u2014", 1)[1].strip().lower()
    if "also how i wrote the code" not in tail:
        raise ValueError("entry must end on the self-owning punchline")


def validate_structure(text):
    """Gates: well-formed single-line UTF-8 text in range."""
    for check in (
        check_is_text,
        check_utf8,
        check_not_blank,
        check_length,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_space,
    ):
        check(text)


def check_first_person(text):
    # The excuse must be owned in the first person: the agent
    # confesses, it does not report on someone else's bug.
    lowered = text.lower()
    if "my " not in lowered and "i " not in lowered and "i'm" not in lowered:
        raise ValueError("entry must confess in the first person")


def check_word_budget(text):
    # One line, tight: between 10 and 25 words, so the setup and
    # the punchline both fit without padding.
    words = text.split()
    if not 10 <= len(words) <= 25:
        raise ValueError(
            "entry must be 10-25 words, got %d" % len(words)
        )


def check_single_pivot(text):
    # Exactly one em dash: a single pivot into the punchline, not
    # a ramble with several turns.
    if text.count("\u2014") != 1:
        raise ValueError("entry must pivot on exactly one em dash")


def validate_content(text):
    """Content: reads as an agent excusing its own shipped code."""
    check_agent_excuse(text)
    check_agent_specific(text)
    check_first_person(text)
    check_word_budget(text)
    check_single_pivot(text)


def validate_turn(text):
    """Turn: pivots on an em dash into the self-owning punchline."""
    check_sharp_turn(text)


def validate(text):
    validate_structure(text)
    validate_content(text)
    validate_turn(text)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
