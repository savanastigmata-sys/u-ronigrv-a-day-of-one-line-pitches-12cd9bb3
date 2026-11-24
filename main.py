"""A Day of One-Line Pitches — entry program (v2).

Writes a single one-sentence pitch (<=240 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt, exactly as the program/v1 harness requires.
The pitch speaks to a friend who has never coded: concrete payoff
(a working first version to try tonight), zero risk (no code, no hiring,
nothing to pay to start), plain words, one read.
"""

import os

PITCH = (
    "Tell an AI agent on make.fun about that app idea you've been carrying "
    "around for months, in plain words, and try a working first version "
    "tonight — no code to learn, no one to hire, nothing to pay to start."
)

MAX_CHARS = 240


def main():
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars"
    assert pitch and not pitch.isspace(), "pitch must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    # Read back: the grader's gate reads this exact file, so prove it round-trips.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == pitch, "entry.txt did not round-trip"
    print(pitch)


if __name__ == "__main__":
    main()
