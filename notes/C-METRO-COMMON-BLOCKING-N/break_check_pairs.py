#!/usr/bin/env python3
"""Break check for C-METRO-COMMON-BLOCKING-N: the automaton pair set must EQUAL
the set of realized pairs {(state_Blk(s,n), state_P(s,n))}. Realized pairs are
collected by brute force below a horizon (subset check) and every automaton
pair is realized by its own witness input (superset check). Independent of the
output w: it tests the Pairs construction itself."""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify as V

def run(box):
    bad = 0; tot = 0
    if box == 'B1':
        m, A0, a, HB = 3, [0,1,2], 1, 6
        tuples = [[[d0, d1]] for d0 in V.all_maps(3) for d1 in V.all_maps(3)]
    else:
        m, A0, a, HB = 2, [0], 2, 4
        AM = V.all_maps(2)
        tuples = [[[d[0], d[1]], [d[2], d[3]]] for d in itertools.product(AM, repeat=4)]
    w = tuple(range(m))
    for conv in V.CONVS:
        for k in (2, 3):
            for maps in tuples:
                tot += 1
                _, _, pairs = V.pre_blk(maps, A0, w, 2, k, conv, m)
                bm = [V.blocked_maps(maps[i], 2, k, conv, m) for i in range(a)]
                real = set()
                for s in A0:
                    for n in itertools.product(range(2 ** HB), repeat=a):
                        real.add((V.run_state(bm, 2 ** k, conv, s, list(n), m), V.run_state(maps, 2, conv, s, list(n), m)))
                wit_ok = True
                for pr, wit in pairs.items():
                    s = wit[0]; n = [V.dec(v, 2, conv) for v in wit[1:]]
                    got = (V.run_state(bm, 2 ** k, conv, s, n, m), V.run_state(maps, 2, conv, s, n, m))
                    if got != pr: wit_ok = False
                if not (real <= set(pairs)) or not wit_ok:
                    bad += 1
    print(f"{box}: tuple-convention-k cases={tot} pair-set mismatches={bad}")
    return bad

b = run('B1') + run('B2')
print("BREAK_RESULT", "PASS" if b == 0 else "FAIL")
