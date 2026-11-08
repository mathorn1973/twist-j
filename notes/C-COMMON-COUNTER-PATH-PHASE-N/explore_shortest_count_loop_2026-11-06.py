#!/usr/bin/env python3
"""Exploratory (not preregistered): shortest closed walk of single contacts from I_1 whose number of
state-changing contacts is not a multiple of 5. Exact integers. BFS on (state, count mod 5).
Refused and diagonal contacts are skipped (they change neither the state nor the count)."""
from collections import deque


def rho_times(v):
    a, b, c, d = v
    return (d - c, -c, a - c, b - c)


def contact(x, y):
    delta = tuple(a - b for a, b in zip(x, y))
    if any(a & 1 for a in delta):
        return None
    d = tuple(a // 2 for a in delta)
    if not any(d):
        return None
    s = tuple((a + b) // 2 for a, b in zip(x, y))
    r = rho_times(d)
    return tuple(a + b for a, b in zip(s, r)), tuple(a - b for a, b in zip(s, r)), d


def AB(v):
    a0, a1, a2, a3 = v
    s1 = a0 * a1 + a1 * a2 + a2 * a3
    s2 = a0 * a2 + a1 * a3 + a0 * a3
    return a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3 - s1, s1 - s2


def fmt(v):
    names = {(0, 0, 0, 0): "0", (1, -1, 0, 0): "u", (1, 0, -1, 0): "B", (-1, 0, 1, 0): "-B", (1, 1, 0, -2): "X", (2, 0, 0, 0): "2"}
    return names.get(v, str(v).replace(" ", ""))


U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)
for label, start in (("I_1", (B0, tuple(-a for a in B0), U, U, X, TWO)),):
    root = (start, 0)
    prev = {root: None}
    queue = deque([root])
    found = None
    while queue and found is None:
        node = queue.popleft()
        st, ph = node
        for i in range(6):
            for k in range(i + 1, 6):
                res = contact(st[i], st[k])
                if res is None:
                    continue
                nl = list(st)
                nl[i], nl[k] = res[0], res[1]
                nxt = (tuple(nl), (ph + 1) % 5)
                if nxt not in prev:
                    prev[nxt] = (node, (i, k))
                    if nxt[0] == start and nxt[1] != 0:
                        found = nxt
                        break
                    queue.append(nxt)
            if found:
                break
    word, node = [], found
    while prev[node] is not None:
        node, edge = prev[node]
        word.append(edge)
    word.reverse()
    print("%s: shortest closed walk with count not divisible by 5: %d state-changing contacts (count mod 5 = %d)"
          % (label, len(word), found[1]))
    print("   word:", " ".join("%d%d" % (i + 1, k + 1) for i, k in word))
    st = list(start)
    totA = totB = 0
    print("   start  ", [fmt(v) for v in st])
    for step, (i, k) in enumerate(word, 1):
        x2, y2, d = contact(st[i], st[k])
        a, b = AB(d)
        totA += a
        totB += b
        st[i], st[k] = x2, y2
        print("   %2d  C%d%d  d dbar = %d%+d phi   state %s" % (step, i + 1, k + 1, a, b, [fmt(v) for v in st]))
    print("   closed:", tuple(st) == start, " area sum = %d%+d phi  (both divisible by 5: %s)" % (totA, totB, totA % 5 == 0 and totB % 5 == 0))
    st = list(start)

    def refused(state):
        out = []
        for i in range(6):
            for k in range(i + 1, 6):
                delta = tuple(a - b for a, b in zip(state[i], state[k]))
                if any(a & 1 for a in delta):
                    out.append("%d%d" % (i + 1, k + 1))
        return out
    print("   refused pairs at the start:", refused(st))
