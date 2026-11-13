#!/usr/bin/env python3
"""How much of the native counter does the fixed residue reader need?

NON-CANONICAL / L1 exact exploration for notes/STAVBA-STROJE-2026-11-08. It
creates no claim. U-NATIVE-RAW-RESIDUE-READOUT [T] (canon/CANON.md, section
of that name) gives one fixed reader R(n, q_n, r_n) = PRESENT(kappa(P)) for
every four-piston source P and every n >= 3, prepared at the common receiver
(q, r) = (0, 1), and says that for decoding the counter can be summarized by
T_n^read = (sigma_n, z_n, N_n mod 5) with at most 20 values, "with no
minimality claim".

This script asks the finite question behind that remark. For every counter
n >= 3 the receiver map kappa -> (q_n, r_n) is a signature. Two counters
conflict when some kappa != kappa' produce the same receiver pair at the two
counters: a counter summary f with f(n) = f(n') could not decode both. The
least number of classes of any sufficient summary on a counter range is the
chromatic number of this conflict graph on the distinct signatures. The script
computes the distinct signatures and that chromatic number exactly on
3 <= n < 2^16 and reports whether the 20-valued summary is minimal there.

Why the finite answer holds for every n >= 3. The Canon's inverse formula
(qhat, rhat) = (1 + sigma_n (q_n - z_n) + N_n, sigma_n r_n - N_n) mod 5
equals (q_3, r_3) for every admitted source and every n >= 3; for fixed n
it is an affine bijection of F_5^2 because sigma_n = +-1 is invertible
modulo 5, so (q_n, r_n) is a function of T_n^read and (q_3, r_3); and
(q_3, r_3) depends on the source P only through kappa (table C3 of the
proof, U-NATIVE-APPARATUS-HISTORY-FACTOR). Hence the receiver signature at
counter n is a function of T_n^read, the conflict relation between two
counters depends only on their T values, and since all 20 values occur
before n = 64 the conflict graph below is the conflict graph for all n.
As the Canon says of T_n^read, neither it nor the five-class table defines
an autonomous clock; both are functions of the counter.

Validation against registered facts before the question is asked: the full
six-coordinate update reproduces the (z, q, r) quotient table of the Canon
proof; the common-receiver table C1, C2, C3 of the proof is reproduced; all
15625 heads lie on z in {1, 4} from tick 3; the ready (0, 1) map P -> x_3 is
injective (625 image states); and the Canon's inverse formula (qhat, rhat)
recovers (q_3, r_3) for all n up to the range bound.

Python standard library only, exact integers, no randomness, deterministic
output.
"""

from __future__ import annotations

from itertools import product

RANGE = 1 << 16


def theta(n: int) -> int:
    return bin(n).count("1") % 2


def gen(i: int, x: tuple[int, ...]) -> tuple[int, ...]:
    p1, p4, p1p, p4p, q, r = x
    if i == 0:  # a
        y = (p4, p1, p4p, p1p, q, r)
    elif i == 1:  # b
        y = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif i == 2:  # c
        y = (-p1p + 2, -p4p + 1 + r, -p1 + 2, -p4 + 1 - r, 1 - q, -r)
    elif i == 3:  # d
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    else:  # e
        y = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    return tuple(v % 5 for v in y)


def step(n: int, x: tuple[int, ...]) -> tuple[int, ...]:
    z6 = sum(x) % 5
    return gen((z6 + 2 * theta(n)) % 5, x)


def quotient_step(n: int, zqr: tuple[int, int, int]) -> tuple[int, int, int]:
    z, q, r = zqr
    i = (z + 2 * theta(n)) % 5
    if i == 0:
        y = (z, q, r)
    elif i == 1:
        y = (-z, -q, -r)
    elif i == 2:
        y = (2 - z, 1 - q, -r)
    elif i == 3:
        y = (2 - z, 1 - q, 1 - r)
    else:
        y = (3 - z, 2 - q, 1 - r)
    return tuple(v % 5 for v in y)  # type: ignore[return-value]


def s_alt(m: int) -> int:
    total, sign, d = 0, 1, 1
    while d <= m:
        total += sign * (m // d)
        sign = -sign
        d *= 2
    return total


def t_read(n: int) -> tuple[int, int, int]:
    sigma = 1 if (n - 3) % 2 == 0 else -1
    z = (4 + 2 * theta(n - 1)) % 5
    big_n = s_alt((n - 1) // 2) - 1
    return sigma, z, big_n % 5


def inverse(n: int, q: int, r: int) -> tuple[int, int]:
    sigma, z, _ = t_read(n)
    big_n = s_alt((n - 1) // 2) - 1
    qhat = (1 + sigma * (q - z) + big_n) % 5
    rhat = (sigma * r - big_n) % 5
    return qhat, rhat


def chromatic_number(nodes: list, edges: set) -> int:
    """Exact chromatic number by backtracking; graphs here have <= 20 nodes."""
    order = sorted(nodes, key=lambda v: -sum((v, w) in edges for w in nodes))
    adj = {v: {w for w in nodes if (v, w) in edges or (w, v) in edges} for v in nodes}

    def colourable(k: int) -> bool:
        colour: dict = {}

        def rec(i: int) -> bool:
            if i == len(order):
                return True
            v = order[i]
            used = {colour[w] for w in adj[v] if w in colour}
            for c in range(k):
                if c not in used:
                    colour[v] = c
                    if rec(i + 1):
                        return True
                    del colour[v]
            return False

        return rec(0)

    k = 1
    while not colourable(k):
        k += 1
    return k


def main() -> None:
    # 1. Full six-coordinate dynamics versus the quotient table.
    heads = [tuple(v) for v in product(range(5), repeat=6)]
    for x in heads:
        for n in range(0, 8):
            y = step(n, x)
            zqr = (sum(x) % 5, x[4], x[5])
            assert (sum(y) % 5, y[4], y[5]) == quotient_step(n, zqr), (n, x)
    print("quotient table (z,q,r) agrees with the six-coordinate generators: all 15625 heads, ticks 0..7")

    # 2. Sheet synchronization and ready-(0,1) injectivity at tick three.
    on_sheet = 0
    image3 = set()
    for x in heads:
        y = x
        for n in range(0, 64):
            y = step(n, y)
            if n + 1 >= 3:
                assert sum(y) % 5 in (1, 4), (x, n + 1, y)
        on_sheet += 1
    for p in product(range(5), repeat=4):
        y = (*p, 0, 1)
        for n in range(0, 3):
            y = step(n, y)
        image3.add(y)
    print(f"all {on_sheet} heads lie on z in {{1,4}} at every tick 3..64; "
          f"ready (0,1) image at tick 3 has {len(image3)} states")

    # 3. The proof table C1..C3 and the reader inverse on the whole range.
    rows = {}
    for p in product(range(5), repeat=4):
        kappa = sum(p) % 5
        y = (*p, 0, 1)
        hist = []
        for n in range(0, 3):
            y = step(n, y)
            hist.append((y[4], y[5]))
        rows.setdefault(kappa, set()).add(tuple(hist))
    for kappa in range(5):
        assert len(rows[kappa]) == 1, kappa
    table = {k: next(iter(rows[k])) for k in range(5)}
    expected = {0: ((0, 4), (0, 1), (1, 0)), 1: ((1, 4), (0, 1), (2, 0)),
                2: ((1, 0), (4, 0), (2, 1)), 3: ((2, 0), (3, 0), (3, 1)),
                4: ((0, 1), (1, 4), (1, 2))}
    assert table == expected, table
    print("common-receiver table C1,C2,C3 of the Canon proof reproduced for kappa = 0..4")

    # Quotient trajectories per kappa (the receiver depends on P only via kappa).
    traj = {}
    for kappa in range(5):
        zqr = ((kappa + 1) % 5, 0, 1)
        seq = []
        for n in range(0, RANGE):
            zqr = quotient_step(n, zqr)
            seq.append((zqr[1], zqr[2]))
        traj[kappa] = seq  # seq[n-1] is the receiver at counter n
    for n in range(3, RANGE):
        for kappa in range(5):
            q, r = traj[kappa][n - 1]
            assert inverse(n, q, r) == traj[kappa][2], (n, kappa)
    print(f"reader inverse (qhat,rhat) = (q_3,r_3) verified for all kappa and all 3 <= n < {RANGE}")

    # 4. Signatures and the conflict graph.
    sig_of_n = {}
    sig_to_t = {}
    for n in range(3, RANGE):
        sig = tuple(traj[k][n - 1] for k in range(5))
        assert len(set(sig)) == 5, n
        sig_of_n[n] = sig
        sig_to_t.setdefault(sig, set()).add(t_read(n))
    sigs = sorted(sig_to_t)
    t_values = sorted({t_read(n) for n in range(3, RANGE)})
    print(f"distinct counter summaries T_n^read on the range: {len(t_values)}")
    print(f"distinct receiver signatures kappa -> (q_n, r_n) on the range: {len(sigs)}")
    for sig in sigs:
        assert len(sig_to_t[sig]) == 1, sig
    print("each signature corresponds to exactly one summary value: the summary determines the signature and conversely")

    edges = set()
    for i, s in enumerate(sigs):
        for j, t in enumerate(sigs):
            if i < j:
                for ka in range(5):
                    for kb in range(5):
                        if ka != kb and s[ka] == t[kb]:
                            edges.add((s, t))
    print(f"conflict edges between signatures: {len(edges)}")
    chi = chromatic_number(sigs, edges)
    print(f"chromatic number of the conflict graph: {chi}")
    complete = len(edges) == len(sigs) * (len(sigs) - 1) // 2
    print(f"conflict graph complete: {'yes' if complete else 'no'}")
    if chi == len(sigs):
        print(f"consequence: on 3 <= n < {RANGE} every counter summary sufficient for the fixed reader "
              f"needs at least {chi} classes, and the {len(t_values)}-valued T_n^read attains it; "
              "the Canon's summary is minimal on this range")
    else:
        print(f"consequence: on 3 <= n < {RANGE} a summary with {chi} classes suffices, fewer than the "
              f"{len(t_values)} values of T_n^read; an explicit coarser summary exists on this range")
    # Which summary values actually occur in the first 64 ticks.
    first = sorted({t_read(n) for n in range(3, 64)})
    print(f"summary values occurring for 3 <= n < 64: {len(first)}")

    # 5. Coarser projections of T_n^read and one explicit minimal colouring.
    t_of_sig = {sig: next(iter(sig_to_t[sig])) for sig in sigs}

    def conflict_free(cls) -> bool:
        return all(not ((s, t) in edges) for s in sigs for t in sigs if cls[s] == cls[t] and s < t)

    projections = {
        "N_n mod 5 alone": lambda t: (t[2],),
        "(sigma_n, N_n mod 5)": lambda t: (t[0], t[2]),
        "(z_n, N_n mod 5)": lambda t: (t[1], t[2]),
        "(sigma_n, z_n)": lambda t: (t[0], t[1]),
    }
    for name, proj in projections.items():
        cls = {sig: proj(t_of_sig[sig]) for sig in sigs}
        print(f"projection {name}: {len(set(cls.values()))} values, "
              f"{'sufficient' if conflict_free(cls) else 'NOT sufficient'}")
    affine = None
    for alpha in range(1, 5):
        for beta in range(5):
            for gamma in range(5):
                for delta in range(5):
                    cls = {}
                    for sig in sigs:
                        s0, z0, n0 = t_of_sig[sig]
                        sb = 1 if s0 == -1 else 0
                        zb = 1 if z0 == 4 else 0
                        cls[sig] = (alpha * n0 + beta * sb + gamma * zb + delta * sb * zb) % 5
                    if conflict_free(cls) and affine is None:
                        affine = (alpha, beta, gamma, delta)
    print("affine five-class formula (alpha*N + beta*[sigma=-1] + gamma*[z=4] + delta*[both]) mod 5: "
          + (f"found {affine}" if affine else "none in the 500-member family"))

    order = sorted(sigs, key=lambda v: -sum(((v, w) in edges) or ((w, v) in edges) for w in sigs))
    adj = {v: {w for w in sigs if (v, w) in edges or (w, v) in edges} for v in sigs}
    colour: dict = {}

    def rec(i: int) -> bool:
        if i == len(order):
            return True
        v = order[i]
        used = {colour[w] for w in adj[v] if w in colour}
        for c in range(chi):
            if c not in used:
                colour[v] = c
                if rec(i + 1):
                    return True
                del colour[v]
        return False

    assert rec(0)
    print(f"one explicit {chi}-class summary as a table T_n^read = (sigma, z, N mod 5) -> class:")
    for t in t_values:
        sig = next(s for s in sigs if t_of_sig[s] == t)
        print(f"  {t} -> {colour[sig]}")
    print("all-n reading: by U-NATIVE-RAW-RESIDUE-READOUT the receiver map at counter n is a function "
          "of T_n^read for every n >= 3, and all 20 values occur before n = 64, so the conflict graph "
          "above is the conflict graph for all n >= 3; the table is sufficient for all n >= 3 and "
          f"no sufficient summary has fewer than {chi} classes")
    print("NATIVE COUNTER STATISTIC AUDIT PASS")


if __name__ == "__main__":
    main()
