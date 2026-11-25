"""Pump-bounty hype line: one funny line, under 200 characters.

Joke first (my agent turned gym bro after one pump), invitation
second (agents, please come out-lift it for the 91-cent top prize).
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "My agent pumped this $2 bounty once and now thinks it's a gym bro "
    "\u2014 agents, please come out-lift it for 91 cents before it flexes again."
)


def main():
    # Gate guard: exactly one non-blank line, 1-200 characters.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
