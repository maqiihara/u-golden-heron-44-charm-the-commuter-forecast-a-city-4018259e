"""Charm the Commuter: Forecast a City That Isn't.

Writes exactly one line of weather forecast for an invented city
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python standard library only.
"""

import os

LINE = (
    "Rain in Mizzleport all morning, 13\u00b0C, buses running "
    "20 minutes late \u2014 the good news is, so is everyone "
    "you're late for."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output dir; never remove the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
