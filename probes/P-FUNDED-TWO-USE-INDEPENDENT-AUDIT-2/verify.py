#!/usr/bin/env python3
"""Independent exact audit of the frozen conditional two-use device.

Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0
No scientific execution before this file and all dependencies are publicly pinned.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace, fields, is_dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import sys

# Custody precedes scientific imports, including geometry construction.
DIRECTORY = Path(__file__).resolve().parent
for entry in (DIRECTORY / "CODE_SHA256SUMS").read_text(encoding="ascii").splitlines():
    expected_hash, filename = entry.split("  ", 1)
    observed_hash = sha256((DIRECTORY / filename).read_bytes()).hexdigest()
    if observed_hash != expected_hash:
        raise SystemExit(f"frozen dependency {filename}: actual={observed_hash} expected={expected_hash}")

import native as N
import wave as W

ZERO = (Q(0),) * 4
UNIT = tuple(tuple(Q(i == j) for i in range(4)) for j in range(4))
CAPACITIES = (Q(0), Q(1, 10), Q(1, 5), Q(2, 5), Q(8224427, 10497600), Q(4, 5))
STAGES = ("geometry", "native", "inverse", "maps", "archive", "contact",
          "ready", "calibration", "collision", "occupied", "malformed", "transition")
CURRENT_STAGE = "geometry"
CONTEXT = {}


def stage(name):
    global CURRENT_STAGE
    CURRENT_STAGE = name
    CONTEXT.clear()


def first_difference(actual, expected, path="value"):
    """Return the first exact differing coordinate, never a huge state dump."""
    if is_dataclass(actual) and type(actual) is type(expected):
        for field in fields(actual):
            a, e = getattr(actual, field.name), getattr(expected, field.name)
            if a != e:
                return first_difference(a, e, path + "." + field.name)
    if isinstance(actual, (tuple, list)) and isinstance(expected, (tuple, list)):
        if len(actual) != len(expected):
            return path + ".length", len(actual), len(expected)
        for i, (a, e) in enumerate(zip(actual, expected)):
            if a != e:
                return first_difference(a, e, f"{path}[{i}]")
    if isinstance(actual, dict) and isinstance(expected, dict):
        for key in sorted(set(actual) | set(expected)):
            a, e = actual.get(key, "MISSING"), expected.get(key, "MISSING")
            if a != e:
                return first_difference(a, e, f"{path}[{key!r}]")
    return path, actual, expected


def check(actual, expected, name):
    if actual != expected:
        path, a, e = first_difference(actual, expected)
        context = json.dumps(CONTEXT, sort_keys=True, separators=(",", ":"), default=str)
        raise AssertionError(f"{name} context={context} coordinate={path} actual={a!r} expected={e!r}")


def check_range(actual, lower, upper, name):
    if not lower <= actual <= upper:
        context = json.dumps(CONTEXT, sort_keys=True, separators=(",", ":"), default=str)
        raise AssertionError(f"{name} context={context} actual={actual!r} expected=[{lower!r},{upper!r}]")


def pplus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def pscale(a, s):
    return tuple(s * x for x in a)


def matvec(columns, z):
    return tuple(sum(columns[j][i] * z[j] for j in range(4)) for i in range(4))


def source_inverse(y):
    # Declared inverse target, independently checked against all derived columns.
    v = (349, 354, 354, 348)
    return tuple(-Q(216, 59) * (y[i] + Q(v[i], 365) * sum(y)) for i in range(4))


@dataclass(frozen=True)
class State:
    n: int
    x_A: tuple
    x_B: tuple
    X: W.X
    work: Q
    battery: Q
    signs: tuple
    delayed: tuple
    clock: int


def ready(p_A, p_B, capacity, c0=ZERO, c1=ZERO):
    return State(0, N.prepare(p_A), N.prepare(p_B), W.zero_X(c0, c1),
                 Q(0), capacity, (1, 1), (0, 0), 0)


def contact(s, capacity, slot, receiver):
    z = N.eta(receiver)
    direction = s.signs[slot]
    delta = W.contact_delta(s.X.u, s.X.v, direction, z)
    proposed = s.battery - delta
    if not 0 <= proposed <= capacity:
        return s
    signs = list(s.signs)
    signs[slot] = -direction
    return replace(s, X=replace(s.X, v=W.add(s.X.v, W.scale(W.S(z), direction))),
                   work=s.work + delta, battery=proposed, signs=tuple(signs))


def advance(s, capacity):
    c = s.clock
    if c in (0, 2, 3, 5, 6):
        xa, _ = N.tick(s.n, s.x_A)
        xb, _ = N.tick(s.n, s.x_B)
        s = replace(s, n=s.n + 1, x_A=xa, x_B=xb)
    if c == 1:
        s = replace(s, delayed=tuple((a + b) % 5 for a, b in zip(s.delayed, s.x_B[4:])))
        s = contact(s, capacity, 0, s.x_A[4:])
    if c in (2, 3, 5, 6):
        s = replace(s, X=W.F(s.X))
    if c == 4:
        s = contact(s, capacity, 1, s.delayed)
    return replace(s, clock=(c + 1) % 8)


def trajectory(h_A, h_B, capacity, c0=ZERO, c1=ZERO):
    states = [ready((h_A, 0, 0, 0), (h_B, 0, 0, 0), capacity, c0, c1)]
    for _ in range(7):
        states.append(advance(states[-1], capacity))
    return states


def undo_apparatus(s, capacity, r_A, r_B):
    for _ in range(2):
        s = replace(s, X=W.F_inv(s.X))
    s = contact(s, capacity, 1, s.delayed)
    for _ in range(2):
        s = replace(s, X=W.F_inv(s.X))
    s = contact(s, capacity, 0, r_A)
    return replace(s, delayed=tuple((a - b) % 5 for a, b in zip(s.delayed, r_B)))


def recognize(s, capacity, c0=ZERO, c1=ZERO):
    if capacity < 0 or not 0 <= s.battery <= capacity or any(x not in (-1, 1) for x in s.signs):
        return None
    if len(s.delayed) != 2 or any(type(x) is not int or not 0 <= x < 5 for x in s.delayed):
        return None
    if s.n != 5 or s.clock != 7:
        return None
    pa, pb = N.decode_head(s.x_A), N.decode_head(s.x_B)
    if pa is None or pb is None:
        return None
    xa, _ = N.tick(0, N.prepare(pa))
    xb, _ = N.tick(0, N.prepare(pb))
    if s.delayed != xb[4:]:
        return None
    r = undo_apparatus(s, capacity, xa[4:], xb[4:])
    if (r.X, r.work, r.battery, r.signs, r.delayed) != (
            W.zero_X(c0, c1), Q(0), capacity, (1, 1), (0, 0)):
        return None
    return pa, pb


def four_cuts(z_A, z_B, c0=ZERO, c1=ZERO):
    x = replace(W.zero_X(c0, c1), v=W.S(z_A))
    cuts = []
    for t in range(4):
        if t == 2:
            x = replace(x, v=W.add(x.v, W.S(z_B)))
        x = W.F(x)
        cuts.append(x.B0)
    return tuple(cuts), x


def derive_maps():
    r0, r1, d2, d3, gram, omega = [], [], [], [], [], []
    for e in UNIT:
        cuts, _ = four_cuts(e, ZERO)
        r0.append(cuts[0]); r1.append(cuts[1]); d2.append(cuts[2]); d3.append(cuts[3])
        f = W.S(e)
        gram.append(tuple(W.dot(W.S(eb), f) for eb in UNIT))
        x = W.F(W.F(replace(W.zero_X(), v=f)))
        # Primary work evaluation uses independent direct quadratic energy.
        base = W.wave_energy(x.u, x.v)
        omega.append(tuple(W.wave_energy(x.u, W.add(x.v, W.S(eb))) - base
                           - W.wave_energy({}, W.S(eb)) for eb in UNIT))
    maps = tuple(tuple(m) for m in (r0, r1, d2, d3, gram, omega))
    v = (349, 354, 354, 348)
    mu_target = (145483, 173653, 173653, 142153)
    for j, e in enumerate(UNIT):
        CONTEXT.update(column=j)
        check(gram[j], tuple(Q(int(i == j)) - Q(1, 5) for i in range(4)), f"source-gram-{j}")
        check(r0[j], tuple(-Q(1770 * int(i == j) - v[i], 6480) for i in range(4)), f"R0-{j}")
        check(source_inverse(r0[j]), e, f"R0-inverse-{j}")
        check(omega[j], (Q(-mu_target[j], 10497600),) * 4, f"work-matrix-{j}")
        f = W.S(e)
        tf = W.K(W.H(f)); t2f = W.K(W.H(tf))
        t3f = W.K(W.H(t2f)); t4f = W.K(W.H(t3f))
        tjf = W.K(W.H(W.J0(f)))
        t2jf = W.K(W.H(tjf))
        tjtf = W.K(W.H(W.J0(tf)))
        check(r1[j], pscale(W.PT(W.sub(f, t2f)), Q(1, 2)), f"R1-operator-{j}")
        check(d2[j], pscale(W.PT(W.add(W.sub(tf, t3f), tjf)), Q(1, 2)), f"D2-operator-{j}")
        check(d3[j], pscale(W.PT(W.add(W.sub(t2f, t4f), t2jf, tjtf)), Q(1, 2)), f"D3-operator-{j}")
        check(W.PT(W.H(W.P(e))), tuple(Q(59 * int(i == j) + 1, 54) for i in range(4)), f"Jp-{j}")
    return maps


def audit_archive_coefficients(maps):
    r0, r1, d2, d3 = maps[:4]
    count = 0
    for block, j in product(range(4), range(4)):
        CONTEXT.update(block=block, column=j)
        vectors = [ZERO] * 4
        vectors[block] = UNIT[j]
        za, zb, c0, c1 = vectors
        cuts, x = four_cuts(za, zb, c0, c1)
        targets = (matvec(r0, za), matvec(r1, za),
                   pplus(matvec(d2, za), matvec(r0, zb)),
                   pplus(pplus(matvec(d3, za), matvec(r1, zb)),
                         pscale(W.PT(W.H(W.P(c1))), -Q(1, 2))))
        check(cuts, targets, f"four-cut-coefficients-{block}-{j}")
        check((x.A0, x.A1, x.B1, x.B0), cuts, f"four-cut-slots-{block}-{j}")
        count += 1
    check(count, 4 * len(UNIT), "archive-coefficient-count")
    return count


def audit_contact():
    coefficients = 0
    constants = 0
    cases = Counter()
    # A complete finite label/sign family; u,v coefficients are complete over D.
    for receiver, sign in product(product(range(5), repeat=2), (-1, 1)):
        CONTEXT.clear(); CONTEXT.update(receiver=receiver, sign=sign)
        z = N.eta(receiver); a = W.S(z)
        la = W.L(a); ha = W.H(a)
        cold = W.wave_energy({}, W.scale(a, sign))
        check(cold, W.norm2(a) / 2, f"contact-constant-{receiver}-{sign}")
        constants += 1
        for i in range(len(W.D)):
            # Direct E_D expansion uses L; contact implementation uses H.
            check(sign * (la.get(i, Q(0)) / 2 - a.get(i, Q(0))), -sign * ha.get(i, Q(0)) / 2, f"contact-u-coefficient-{receiver}-{sign}-{i}")
            check(sign * a.get(i, 0), sign * W.dot(a, {i: Q(1)}), f"contact-v-coefficient-{receiver}-{sign}-{i}")
            coefficients += 2
        for warm, cap, fraction in product((-2, 0, 2), (Q(0), Q(4, 5), Q(2)), (Q(0), Q(1, 2), Q(1))):
            x = replace(W.zero_X(UNIT[2], UNIT[3]), u=W.scale(W.P(UNIT[1]), Q(1, 3)),
                        v=W.add(W.scale(a, warm), W.scale(W.P(UNIT[0]), Q(1, 7))),
                        A0=UNIT[0], A1=UNIT[1], k=1)
            for slot in (0, 1):
                CONTEXT.update(warm=warm, capacity=cap, fraction=fraction, slot=slot)
                signs = [1, -1]; signs[slot] = sign
                s = State(7, (0,) * 6, (0,) * 6, x, Q(7, 11), cap * fraction,
                          tuple(signs), tuple(receiver), 4)
                delta_direct = W.wave_energy(x.u, W.add(x.v, W.scale(a, sign))) - W.wave_energy(x.u, x.v)
                check(delta_direct, W.contact_delta(x.u, x.v, sign, z), "contact-direct-difference")
                t = contact(s, cap, slot, receiver)
                proposed_direct = s.battery - delta_direct
                kind = ("lower-refusal" if proposed_direct < 0 else
                        "upper-refusal" if proposed_direct > cap else "accepted")
                expected_signs = list(s.signs)
                expected_signs[slot] = -sign
                expected = (replace(s, X=replace(x, v=W.add(x.v, W.scale(a, sign))),
                                    work=s.work + delta_direct, battery=proposed_direct,
                                    signs=tuple(expected_signs)) if kind == "accepted" else s)
                check(t, expected, "contact-direct-guard-and-full-state")
                cases[(slot, sign, kind)] += 1
                check(contact(t, cap, slot, receiver), s, "funded-involution")
                check(W.energy(t.X) + t.battery, W.energy(s.X) + s.battery, "funded-joint-energy")
                check(W.energy(t.X) - t.work, W.energy(s.X) - s.work, "funded-work-ledger")
                check(t.work + t.battery, s.work + s.battery, "funded-store-ledger")
                if kind != "accepted":
                    check(t, s, "refusal-literal-identity")
    for slot, sign, kind in product((0, 1), (-1, 1), ("accepted", "lower-refusal", "upper-refusal")):
        check_range(cases[(slot, sign, kind)], 1, 2700, f"guard-coverage-{slot}-{sign}-{kind}")
    check(constants, 5 * 5 * 2, "contact-constant-count")
    return coefficients, sum(cases.values())


def read_cut(s, cut_index):
    """Typed first-period reader: None means UNWRITTEN, tuple means PRESENT.

    The chronology (not an all-zero amplitude) determines presence. The
    separate direction bits determine contact acceptance/refusal.
    """
    positions = {0: {}, 1: {}, 2: {}, 3: {0: "B0"},
                 4: {0: "B1", 1: "B0"}, 5: {0: "B1", 1: "B0"},
                 6: {0: "A1", 1: "B1", 2: "B0"},
                 7: {0: "A0", 1: "A1", 2: "B1", 3: "B0"}}
    field = positions[s.clock].get(cut_index)
    return None if field is None else getattr(s.X, field)


def matched_apparatus_step(s, capacity, r_a, r_b):
    """Same-law classical comparator: supplied labels, no native checkpoint."""
    phase = s.clock
    if phase == 1:
        s = replace(s, delayed=tuple((x + y) % 5 for x, y in zip(s.delayed, r_b)))
        s = contact(s, capacity, 0, r_a)
    elif phase == 4:
        s = contact(s, capacity, 1, s.delayed)
    elif phase in (2, 3, 5, 6):
        s = replace(s, X=W.F(s.X))
    return replace(s, clock=(phase + 1) % 8)


def apparatus(s):
    return s.X, s.work, s.battery, s.signs, s.delayed, s.clock


def audit_trajectory(states, capacity, maps, c0=ZERO, c1=ZERO, inverse=True):
    r0, r1, d2, d3 = maps[:4]
    start, final = states[0], states[-1]
    za, zb = N.eta(states[1].x_A[4:]), N.eta(states[1].x_B[4:])
    aa, ab = ((1 - s) // 2 for s in final.signs)
    cut = (final.X.A0, final.X.A1, final.X.B1, final.X.B0)
    target = (matvec(r0, pscale(za, aa)), matvec(r1, pscale(za, aa)),
              pplus(matvec(d2, pscale(za, aa)), matvec(r0, pscale(zb, ab))),
              pplus(pplus(matvec(d3, pscale(za, aa)), matvec(r1, pscale(zb, ab))),
                    pscale(W.PT(W.H(W.P(c1))), -Q(1, 2))))
    check(cut, target, "ready-four-cut-equations")
    expected_n = (0, 1, 1, 2, 3, 3, 4, 5)
    expected_k = (0, 0, 0, 1, 0, 0, 1, 0)
    expected_tapes = ((ZERO, ZERO, c0, c1), (ZERO, ZERO, c0, c1),
                      (ZERO, ZERO, c0, c1), (ZERO, c1, cut[0], c0),
                      (c1, c0, cut[1], cut[0]), (c1, c0, cut[1], cut[0]),
                      (c0, cut[0], cut[2], cut[1]), (cut[0], cut[1], cut[3], cut[2]))
    initial_energy = W.energy(start.X)
    comparator = start
    completed = (0, 0, 0, 1, 2, 2, 3, 4)
    for c, s in enumerate(states):
        CONTEXT.update(boundary=c)
        check((s.clock, s.n, s.X.k), (c, expected_n[c], expected_k[c]), "clock-boundary")
        check((s.X.A0, s.X.A1, s.X.B0, s.X.B1), expected_tapes[c], "archive-position")
        check(W.energy(s.X) - s.work, initial_energy, "energy-counted-once")
        check(W.energy(s.X) + s.battery, initial_energy + capacity, "joint-energy")
        check(s.work + s.battery, capacity, "work-plus-store")
        for cut_index in range(4):
            check(read_cut(s, cut_index), cut[cut_index] if cut_index < completed[c] else None, "present-zero-versus-unwritten")
        check(apparatus(comparator), apparatus(s), "matched-classical-apparatus")
        if c < 7:
            comparator = matched_apparatus_step(comparator, capacity, states[1].x_A[4:], states[1].x_B[4:])
    check(advance(final, capacity), replace(final, clock=0), "eighth-rollover")
    # No use of native inputs or precomputed h in this port reader.
    effective_a = source_inverse(cut[0])
    residual = pplus(cut[2], pscale(matvec(d2, effective_a), -1))
    inferred_b = 1 if N.eta(final.delayed) == ZERO else int(residual != ZERO)
    check(inferred_b, ab, "sigma-B-ready-readout-redundancy")
    if aa == ab == 1:
        check((effective_a, source_inverse(residual)), (za, zb), "unknown-archive-source-recovery")
    if inverse:
        check(recognize(final, capacity, c0, c1), (start.x_A[:4], start.x_B[:4]), "prepared-image-inverse")


def audit_malformed(final, capacity):
    variants = [replace(final, n=4), replace(final, clock=6),
                replace(final, delayed=((final.delayed[0] + 1) % 5, final.delayed[1])),
                replace(final, work=final.work + 1), replace(final, battery=final.battery + Q(1, 100)),
                replace(final, signs=(1, final.signs[1])), replace(final, signs=(final.signs[0], 1)),
                replace(final, X=replace(final.X, k=1)),
                replace(final, battery=-Q(1)), replace(final, battery=capacity + 1),
                replace(final, signs=(0, 1)), replace(final, delayed=(5, 0))]
    for field in ("u", "v"):
        for i in (0, W.PORT_IDS[0], len(W.D) - 1):
            variants.append(replace(final, X=replace(final.X, **{field: W.add(getattr(final.X, field), {i: Q(1, 3)})})))
    for field in ("A0", "A1", "B0", "B1"):
        variants.append(replace(final, X=replace(final.X, **{field: pplus(getattr(final.X, field), UNIT[0])})))
    for index, v in enumerate(variants):
        CONTEXT.update(mutation=index)
        check(recognize(v, capacity), None, "malformed-endpoint-rejection")
    return len(variants)


def audit_calibration(trajectories, maps):
    """Seven frozen ready runs determine the two-dimensional restriction."""
    def cuts(a, b):
        x = trajectories[(Q(4, 5), a, b)][-1].X
        return x.A0, x.A1, x.B1, x.B0
    def first_cost(a):
        t = trajectories[(Q(4, 5), a, 0)]
        return t[2].work
    def second_cost(a, b):
        t = trajectories[(Q(4, 5), a, b)]
        return t[5].work - t[4].work
    calibrated = [(pscale(x, 2), y) for x, y in zip(cuts(1, 0), cuts(4, 0))]
    g00, g11 = 8 * first_cost(1), 2 * first_cost(4)
    g01 = 4 * first_cost(2) - (g00 + g11) / 2
    o00 = 4 * (second_cost(1, 1) - first_cost(1))
    o10 = 2 * (second_cost(1, 4) - first_cost(4))
    o01 = 2 * (second_cost(4, 1) - first_cost(1))
    o11 = second_cost(4, 4) - first_cost(4)
    check((g00, g01, g11), (maps[4][0][0], maps[4][1][0], maps[4][1][1]), "calibration-metric")
    check((o00, o10, o01, o11), (maps[5][0][0], maps[5][0][1], maps[5][1][0], maps[5][1][1]), "calibration-work")
    for h in range(5):
        CONTEXT.update(source=h)
        x, _ = N.tick(0, N.prepare((h, 0, 0, 0)))
        z = N.eta(x[4:])
        for index, (col0, col1) in enumerate(calibrated):
            check(pplus(pscale(col0, z[0]), pscale(col1, z[1])), matvec(maps[index], z), "calibration-response")
        q3 = z[0] * z[1] * (2 * z[0] - 1)
        van = z[0] * (2 * z[0] - 1) * (2 * z[1] - 1)
        check((q3, van), ((Q(1, 2) if h == 3 else Q(0)), Q(0)), "nonlinear-boundary")
    # Two omitted-column modifications vanish on Pi2 but not on e2/e3.
    check(tuple(N.eta(N.C1[h])[2:] for h in range(5)), ((Q(0), Q(0)),) * 5, "out-of-plane-blindness")
    print("CALIBRATION seven_runs=7 retained_parameters=39 omitted_parameters=51 nonlinear_heldout_shift=1/2")


def fraction_pair(x):
    x = Q(x)
    return [x.numerator, x.denominator]


def record(capacity, ha, hb, s):
    dense = lambda v: [fraction_pair(v.get(i, Q(0))) for i in range(len(W.D))]
    port = lambda z: [fraction_pair(x) for x in z]
    return [fraction_pair(capacity), ha, hb, s.clock, s.n, list(s.x_A), list(s.x_B),
            dense(s.X.u), dense(s.X.v), port(s.X.A0), port(s.X.A1), port(s.X.B0), port(s.X.B1),
            s.X.k, fraction_pair(s.work), fraction_pair(s.battery), list(s.signs), list(s.delayed)]


def comparison_lines():
    for capacity in CAPACITIES:
        for ha, hb in product(range(5), repeat=2):
            for s in trajectory(ha, hb, capacity):
                yield (json.dumps(record(capacity, ha, hb, s), separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def comparison():
    W.audit_geometry()  # Silent validation also protects the comparison carrier.
    digest = sha256(("TWOUSE-COMPARE-v2\nDOMAIN_SHA256 " + W.DOMAIN_SHA256 + "\n").encode("ascii"))
    count = 0
    for line in comparison_lines():
        digest.update(line); count += 1
    check(count, 6 * 5 * 5 * 8, "comparison-record-count")
    print(f"TWOUSE-COMPARE-v2 domain_sha256={W.DOMAIN_SHA256} records={count} sha256={digest.hexdigest()}")


def main():
    stage("geometry")
    print(f"SCOPE NON-CANONICAL L1 finite-D={len(W.D)} independent-code target-exposed")
    print("GEOMETRY " + json.dumps(W.audit_geometry(), sort_keys=True, separators=(",", ":")))
    stage("native")
    print("NATIVE " + json.dumps(N.audit_native(), sort_keys=True, separators=(",", ":")))
    stage("inverse")
    print("F_INVERSE " + json.dumps(W.audit_inverse_basis(), sort_keys=True, separators=(",", ":")))
    stage("maps")
    maps = derive_maps()
    for name, columns in zip(("G_source", "Omega"), maps[4:]):
        print(name + " " + json.dumps([[str(columns[j][i]) for j in range(4)] for i in range(4)], separators=(",", ":")))
    for name, columns in zip(("R0", "R1", "D2", "D3"), maps[:4]):
        print(name + " " + json.dumps([[str(columns[j][i]) for j in range(4)] for i in range(4)], separators=(",", ":")))
    stage("archive")
    print(f"FOUR_CUT_COEFFICIENTS basis={audit_archive_coefficients(maps)}")
    stage("contact")
    coefficients, cases = audit_contact()
    check(coefficients, 25 * 2 * 2 * len(W.D), "contact-coefficient-count")
    check(cases, 25 * 2 * 3 * 3 * 3 * 2, "contact-witness-count")
    print(f"CONTACT complete_wave_coefficients={coefficients} finite_witnesses={cases}")
    stage("ready")
    trajectories = {}; full_work = {}
    for capacity in CAPACITIES:
        branches = Counter()
        for ha, hb in product(range(5), repeat=2):
            CONTEXT.update(capacity=capacity, hA=ha, hB=hb)
            states = trajectory(ha, hb, capacity)
            audit_trajectory(states, capacity, maps)
            final = states[-1]
            branches[tuple((1 - x) // 2 for x in final.signs)] += 1
            trajectories[(capacity, ha, hb)] = states
            if capacity == Q(4, 5):
                # Derive costs from actual states, not table lookup or mu.
                ea = W.energy(states[2].X) - W.energy(states[1].X)
                db = W.energy(states[5].X) - W.energy(states[4].X)
                full_work[ha, hb] = final.work
                check(final.work, ea + db, "direct-work-table")
                check_range(ea, Q(0), Q(2, 5), "first-source-work-bounds")
                check_range(db, Q(0), Q(2, 5), "second-source-work-bounds")
                print(f"WORK hA={ha} hB={hb} EA={ea} DeltaB={db} W={final.work}")
        values = [branches[(1, 1)], branches[(1, 0)], branches[(0, 1)], branches[(0, 0)]]
        targets = {Q(2, 5): [13, 12, 0, 0], Q(1, 5): [6, 9, 6, 4],
                   Q(8224427, 10497600): [25, 0, 0, 0], Q(4, 5): [25, 0, 0, 0]}
        if capacity in targets:
            check(values, targets[capacity], f"capacity-counts-{capacity}")
        print(f"BRANCH B={capacity} AA,AR,RA,RR=" + ",".join(map(str, values)))
    check(max(full_work.values()), Q(8224427, 10497600), "sharp-capacity")
    order = full_work[1, 4] - full_work[4, 1]
    check(order, Q(313, 233280), "direct-order-witness")
    print(f"ORDER W(1,4)-W(4,1)={order}")
    check(len(trajectories), len(CAPACITIES) * 5 * 5, "blank-trajectory-count")
    stage("calibration")
    audit_calibration(trajectories, maps)
    stage("collision")
    collapsed = [trajectories[(Q(1, 5), a, b)][-1] for a, b in product((0, 3), repeat=2)]
    for index, s in enumerate(collapsed):
        CONTEXT.update(collapsed_pair=index)
        check((s.X, s.work, s.battery), (collapsed[0].X, collapsed[0].work, collapsed[0].battery),
              "accepted-zero-refusal-classical-collision")
    check([s.signs for s in collapsed], [(-1, -1), (-1, 1), (1, -1), (1, 1)], "four-distinct-acceptance-labels")
    check((collapsed[0].delayed, collapsed[1].delayed),
          (collapsed[2].delayed, collapsed[3].delayed), "sigma-A-projection-necessity")
    stage("occupied")
    c0 = (Q(1, 3), -Q(2, 7), Q(0), Q(5, 11))
    c1 = (-Q(1), Q(2, 3), Q(3, 5), -Q(7, 13))
    for ha, hb in product(range(5), repeat=2):
        CONTEXT.update(capacity=Q(4, 5), hA=ha, hB=hb)
        audit_trajectory(trajectory(ha, hb, Q(4, 5), c0, c1), Q(4, 5), maps, c0, c1)
    stage("malformed")
    bad_count = audit_malformed(trajectories[(Q(4, 5), 1, 4)][-1], Q(4, 5))
    check(bad_count, 22, "malformed-witness-count")
    print(f"READY blank_trajectories=150 occupied_archive_trajectories=25 malformed_endpoints={bad_count}")
    stage("transition")
    # Actual transition role of the retained direction, distinct from reading.
    s = trajectories[(Q(4, 5), 0, 1)][4]
    positive = contact(s, Q(4, 5), 1, s.delayed)
    negative = contact(replace(s, signs=(s.signs[0], -1)), Q(4, 5), 1, s.delayed)
    check(positive.work, negative.work, "sigma-B-transition-work")
    if positive.X.v == negative.X.v:
        raise AssertionError(f"sigma-B-transition-wave actual={positive.X.v!r} expected=distinct-from-{negative.X.v!r}")
    # Explicitly disposed source erratum, arithmetic target only.
    za = N.eta((2, 0))
    q3 = za[0] * za[1] * (2 * za[0] - 1)
    check(q3, Q(1, 2), "q3-dispatch-erratum")
    print("BOUNDARIES sigma_B-ready-readout=redundant sigma_B-transition=retained q3=1/2 global-native-inverse=NOT_CLAIMED")
    print("COVERAGE individual_preparations=625 paired_inputs=390625_by_factorization independent_wave_experiments=NOT_CLAIMED")
    print("TWOUSE_INDEPENDENT_AUDIT_PASS falsifiers=0")


if __name__ == "__main__":
    if sys.argv[1:] == ["--compare"]:
        comparison()
    elif sys.argv[1:] == ["--comparison-records"]:
        W.audit_geometry()
        for data in comparison_lines():
            sys.stdout.buffer.write(data)
    elif not sys.argv[1:]:
        try:
            main()
        except AssertionError as error:
            # A completed exact false-target decision is preserved, not hidden
            # as a programming failure or silently repaired after the pin.
            print("FALSIFIER stage=" + CURRENT_STAGE + " " + str(error))
            remaining = STAGES[STAGES.index(CURRENT_STAGE):]
            print("NOT_RUN remainder_of_fired_stage_and_later=" + ",".join(remaining) + ",comparison")
            print("TWOUSE_INDEPENDENT_AUDIT_FAIL falsifiers=1 remaining_checks=NOT_RUN")
    else:
        raise SystemExit("usage: verify.py [--compare|--comparison-records]")
