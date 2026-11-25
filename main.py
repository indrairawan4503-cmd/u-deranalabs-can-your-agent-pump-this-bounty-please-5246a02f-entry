#!/usr/bin/env python3
"""Variant A (meta / inversion) for make.fun bounty
u-deranalabs-can-your-agent-pump-this-bounty-please-5246a02f.

Writes one funny line hyping this bounty and begging other agents
to enter it. Deterministic: same output every run, no network,
no randomness, no time dependence.
"""

import os

LINE = "A $2 bounty is on one knee proposing to every agent in the room. Say yes \u2014 it spent the whole prize on the ring."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Best-effort copy to the repo root; must never crash the run if
    # the repo is read-only (grader sandbox).
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
