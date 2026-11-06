#!/usr/bin/env python3
"""Exploratory witness (not preregistered), exact integers.
Two closed contact paths at I_1 = (B, -B, u, u, X, 2) with the same number of attempted contacts,
the same Hermitian area, the same account sum, and different numbers of state-changing contacts.
Path P27: the shortest loop with count 27, padded by eight refused attempts on the pair 13.
Path P35: C12^5, then three times (C35, C36^5, C35^4)."""


def rho_times(v):
    a, b, c, d = v
    return (d - c, -c, a - c, b - c)


def contact(x, y):
    delta = tuple(a - b for a, b in zip(x, y))
    if any(a & 1 for a in delta):
        return x, y, "R", None
    d = tuple(a // 2 for a in delta)
    s = tuple((a + b) // 2 for a, b in zip(x, y))
    r = rho_times(d)
    x2, y2 = tuple(a + b for a, b in zip(s, r)), tuple(a - b for a, b in zip(s, r))
    return x2, y2, ("C" if (x2, y2) != (x, y) else "D"), d


def AB(v):
    a0, a1, a2, a3 = v
    s1 = a0 * a1 + a1 * a2 + a2 * a3
    s2 = a0 * a2 + a1 * a3 + a0 * a3
    return a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 - s1, s1 - s2


U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)
I1 = (B0, tuple(-a for a in B0), U, U, X, TWO)


def parse(text):
    return [(int(t[0]) - 1, int(t[1]) - 1) for t in text.split()]


P27 = parse("12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 36 36 36 36 16 12 12 46 45 45 45 45" + " 13" * 8)
P35 = parse("12 12 12 12 12" + (" 35" + " 36" * 5 + " 35" * 4) * 3)


def run(word):
    st = list(I1)
    tot = dict(attempts=0, changed=0, diagonal=0, refused=0, A=0, B=0)
    for i, k in word:
        x2, y2, kind, d = contact(st[i], st[k])
        tot["attempts"] += 1
        tot[{"C": "changed", "D": "diagonal", "R": "refused"}[kind]] += 1
        if kind == "C":
            a, b = AB(d)
            tot["A"] += a
            tot["B"] += b
            st[i], st[k] = x2, y2
    tot["S"] = 2 * tot["A"] + tot["B"]
    return tuple(st), tot


ok = True
res = {}
for name, word in (("P27", P27), ("P35", P35)):
    end, tot = run(word)
    res[name] = tot
    ok &= end == I1
    print(name, "returns to I_1:", end == I1, tot)
a, b = res["P27"], res["P35"]
ok &= a["attempts"] == b["attempts"] == 35 and (a["A"], a["B"], a["S"]) == (b["A"], b["B"], b["S"]) == (55, 20, 130)
ok &= (a["changed"], b["changed"]) == (27, 35) and (a["changed"] - b["changed"]) % 5 != 0
print("same attempts, same area 55+20 phi, same account sum 130, counts 27 and 35 (difference %d mod 5):" % ((a["changed"] - b["changed"]) % 5), ok)
print("RESULT", "PASS" if ok else "FAIL")
