#!/usr/bin/env python3
"""P-SPIN-LIFT-FORCED-1 exact verifier.

Implements the pinned owner ruling: public main merge
5d20a194201bec46b0a6d11c028a02f3fa5cf447, file
notes/canon/P-SPIN-LIFT-FORCED-RULING-1.md, SHA-256
0a0712dd8c2b87c31263269b0de04414489204a6b2b89a5fce04478daed62520,
14579 bytes, 409 lines.

Exact integer arithmetic modulo 5 only. Python standard library only;
the single import is sys. Matrices are row-major 4-tuples (a, b, c, d)
for ((a, b), (c, d)). Every printed sequence is sorted; no set or dict
iteration order reaches any print path. The verifier exits 0 iff every
audit gate passes; the scientific decision POSITIVE or NEGATIVE does
not affect the exit code.
"""

import sys

P = 5
I2 = (1, 0, 0, 1)
ZM = (4, 0, 0, 4)

GATES = []


def gate(name, ok, detail=""):
    GATES.append((name, ok))
    tail = f" {detail}" if detail else ""
    print(f"GATE {name}{tail} {'PASS' if ok else 'FAIL'}")


def mmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return ((a * e + b * g) % P, (a * f + b * h) % P,
            (c * e + d * g) % P, (c * f + d * h) % P)


def minv(x):
    a, b, c, d = x
    return (d % P, (-b) % P, (-c) % P, a % P)


def mpow(x, k):
    r = I2
    for _ in range(k):
        r = mmul(r, x)
    return r


def morder(x):
    k = 1
    y = x
    while y != I2:
        y = mmul(y, x)
        k += 1
    return k


def coset(g):
    return min(g, mmul(ZM, g))


def cmul(x, y):
    return coset(mmul(x, y))


def cinv(x):
    return coset(minv(x))


def cpow(x, k):
    r = coset(I2)
    for _ in range(k):
        r = cmul(r, x)
    return r


D5_ELEMS = sorted([('rot', a) for a in range(5)] + [('ref', a) for a in range(5)])
D5_E = ('rot', 0)
D5_R = ('rot', 1)
D5_S = ('ref', 0)


def kmul(k1, k2):
    t1, a = k1
    t2, b = k2
    if t1 == 'rot' and t2 == 'rot':
        return ('rot', (a + b) % 5)
    if t1 == 'rot' and t2 == 'ref':
        return ('ref', (a + b) % 5)
    if t1 == 'ref' and t2 == 'rot':
        return ('ref', (a - b) % 5)
    return ('rot', (a - b) % 5)


def derive_map(X, Y):
    xp = [cpow(X, a) for a in range(5)]
    m = {}
    for a in range(5):
        m['rot', a] = xp[a]
        m['ref', a] = cmul(xp[a], Y)
    return m


def is_mono(m):
    if len({m[k] for k in D5_ELEMS}) != 10:
        return False
    for k1 in D5_ELEMS:
        for k2 in D5_ELEMS:
            if m[kmul(k1, k2)] != cmul(m[k1], m[k2]):
                return False
    return True


def canon_map(m):
    return tuple(m[k] for k in D5_ELEMS)


def closure(R, S):
    h = {I2}
    frontier = [I2]
    while frontier:
        g = frontier.pop()
        for x in (R, S):
            ng = mmul(x, g)
            if ng not in h:
                h.add(ng)
                frontier.append(ng)
    return h


def main():
    print("P-SPIN-LIFT-FORCED-1 exact verifier")
    print("RULING merge=5d20a194201bec46b0a6d11c028a02f3fa5cf447")
    print("RULING file_sha256="
          "0a0712dd8c2b87c31263269b0de04414489204a6b2b89a5fce04478daed62520"
          " bytes=14579 lines=409")

    sl2 = sorted((a, b, c, d)
                 for a in range(P) for b in range(P)
                 for c in range(P) for d in range(P)
                 if (a * d - b * c) % P == 1)
    gate("G-ORDER", len(sl2) == 120, f"|SL2(F5)|={len(sl2)}")

    invol = sorted(g for g in sl2 if g != I2 and mmul(g, g) == I2)
    gate("UNIQUE-INVOLUTION", invol == [ZM], f"count={len(invol)}")

    assoc_ok = all(kmul(kmul(k1, k2), k3) == kmul(k1, kmul(k2, k3))
                   for k1 in D5_ELEMS for k2 in D5_ELEMS for k3 in D5_ELEMS)
    gate("D5-ASSOCIATIVITY", assoc_ok)

    r5 = D5_E
    for _ in range(5):
        r5 = kmul(r5, D5_R)
    srs = kmul(kmul(D5_S, D5_R), D5_S)
    pres_ok = (len(D5_ELEMS) == 10 and r5 == D5_E
               and kmul(D5_S, D5_S) == D5_E and srs == ('rot', 4))
    gate("D5-PRESENTATION", pres_ok)

    kernel = sorted(g for g in sl2 if coset(g) == coset(I2))
    gate("PI-KERNEL", kernel == sorted([I2, ZM]))

    gbar = sorted({coset(g) for g in sl2})
    ebar = coset(I2)
    monos = []
    for x in gbar:
        if x == ebar or cpow(x, 5) != ebar:
            continue
        for y in gbar:
            if y == ebar or cmul(y, y) != ebar:
                continue
            if cmul(cmul(y, x), cinv(y)) != cinv(x):
                continue
            m = derive_map(x, y)
            if is_mono(m):
                monos.append(canon_map(m))
    monos = sorted(monos)
    mono_set = set(monos)
    print(f"MONOMORPHISMS count={len(monos)}")

    inv_cache = {g: minv(g) for g in sl2}
    r_cand = [g for g in sl2 if mpow(g, 5) == ZM]
    s_cand = [g for g in sl2 if mmul(g, g) == ZM]

    typing_excluded = 0
    entail_failures = 0
    adm = []
    adm_iota = {}
    for R in r_cand:
        r_inv = inv_cache[R]
        for S in s_cand:
            if mmul(mmul(S, R), inv_cache[S]) != r_inv:
                continue
            m = derive_map(coset(R), coset(S))
            if not is_mono(m):
                typing_excluded += 1
                continue
            image = {m[k] for k in D5_ELEMS}
            pre = {g for g in sl2 if coset(g) in image}
            h = closure(R, S)
            if h == pre and len(h) == 20:
                adm.append((R, S))
                adm_iota[R, S] = canon_map(m)
            else:
                entail_failures += 1
    adm = sorted(adm)
    adm_set = set(adm)
    print(f"TYPING excluded_pairs={typing_excluded}")
    print(f"ADMISSIBLE raw_triples={len(adm)}")
    gate("ENTAILMENT-A6-A7", entail_failures == 0,
         f"failures={entail_failures}")
    gate("MONO-MEMBERSHIP",
         all(adm_iota[p] in mono_set for p in adm))

    conj_closed = True
    seen = set()
    orbits = []
    for pair in adm:
        if pair in seen:
            continue
        pr, ps = pair
        orb = set()
        for g in sl2:
            gi = inv_cache[g]
            q = (mmul(mmul(g, pr), gi), mmul(mmul(g, ps), gi))
            orb.add(q)
            if q not in adm_set:
                conj_closed = False
        orb = sorted(orb)
        orbits.append(orb)
        seen.update(orb)
    gate("CONJUGATION-CLOSED", conj_closed)
    orbits.sort(key=lambda o: o[0])
    sizes = sorted(len(o) for o in orbits)
    n_classes = len(orbits)
    print(f"ORBIT sizes={sizes}")
    print(f"CLASSES N={n_classes}")

    orbit_index = {}
    for idx, orb in enumerate(orbits, 1):
        for q in orb:
            orbit_index[q] = idx

    stab_ok = True
    for idx, orb in enumerate(orbits, 1):
        rep_r, rep_s = orb[0]
        stab = 0
        for g in sl2:
            gi = inv_cache[g]
            if (mmul(mmul(g, rep_r), gi) == rep_r
                    and mmul(mmul(g, rep_s), gi) == rep_s):
                stab += 1
        if stab * len(orb) != 120:
            stab_ok = False
        a5_ok = mmul(mmul(rep_s, rep_r), inv_cache[rep_s]) == inv_cache[rep_r]
        print(f"CLASS {idx} R={rep_r} S={rep_s} orbit={len(orb)}"
              f" stabilizer={stab} A5={'PASS' if a5_ok else 'FAIL'}")
        GATES.append((f"A5-CLASS-{idx}", a5_ok))
    gate("ORBIT-STABILIZER-120", stab_ok)

    retwist_member = True
    retwist = {}
    for idx, orb in enumerate(orbits, 1):
        rep_r, rep_s = orb[0]
        partner = (rep_r, mmul(ZM, rep_s))
        if partner not in adm_set:
            retwist_member = False
            retwist[idx] = 0
        else:
            retwist[idx] = orbit_index[partner]
    for idx in range(1, n_classes + 1):
        print(f"RETWIST {idx} -> {retwist[idx]}")
    gate("RETWIST-MEMBERSHIP", retwist_member)
    invol_ok = retwist_member and all(
        retwist[retwist[idx]] == idx for idx in range(1, n_classes + 1))
    gate("RETWIST-INVOLUTION", invol_ok)

    r_w = None
    for g in sl2:
        if morder(g) == 10:
            r_w = g
            break
    s_w = None
    if r_w is not None:
        rw_inv = inv_cache[r_w]
        for g in sl2:
            if mmul(mmul(g, r_w), inv_cache[g]) == rw_inv:
                s_w = g
                break
    gate("WITNESS-EXISTS", r_w is not None and s_w is not None)
    witness_ok = (r_w is not None and s_w is not None
                  and (r_w, s_w) in adm_set)
    w_class = orbit_index.get((r_w, s_w), 0) if witness_ok else 0
    print(f"WITNESS R_w={r_w} S_w={s_w} class={w_class}")
    gate("WITNESS-ADMISSIBLE", witness_ok)

    passed = sum(1 for _, ok in GATES if ok)
    total = len(GATES)
    all_ok = passed == total

    if not all_ok:
        decision = "STOP"
    elif n_classes == 1:
        decision = "POSITIVE"
    else:
        decision = "NEGATIVE"

    print(f"DECISION {decision} N={n_classes}")
    print(f"RESULT {passed}/{total} AUDIT CHECKS {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
