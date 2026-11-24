#!/usr/bin/env python3
"""C-J-BINARY-READ-CLASSIFICATION-N: compare the two first stdouts.

NON-CANONICAL, L1. Reads EXPECTED.txt (verify.py) and BREAK_EXPECTED.txt
(break.py) from this directory and requires identical COUNT and CLASS rows.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def rows(fname, prefix):
    with open(os.path.join(HERE, fname), "rb") as fh:
        text = fh.read().decode("ascii")
    return sorted(line for line in text.split("\n") if line.startswith(prefix))


def main():
    ok = True
    for prefix, expected_n in (("COUNT ", 2 * 150), ("CLASS ", 2 * 30)):
        a = rows("EXPECTED.txt", prefix)
        b = rows("BREAK_EXPECTED.txt", prefix)
        same = a == b and len(a) == expected_n
        ok = ok and same
        print("COMPARE %s rows verify=%d break=%d expected=%d %s" % (
            prefix.strip(), len(a), len(b), expected_n, "IDENTICAL" if same else "DIFFERENT"))
        if not same:
            for line in sorted(set(a) ^ set(b))[:20]:
                print("DIFF " + line)
    for fname in ("EXPECTED.txt", "BREAK_EXPECTED.txt"):
        last = rows(fname, "VERDICT ")
        print("VERDICT_OF %s %s" % (fname, last[-1] if last else "MISSING"))
        ok = ok and last == ["VERDICT PASS"]
    print("COMPARE_VERDICT %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
