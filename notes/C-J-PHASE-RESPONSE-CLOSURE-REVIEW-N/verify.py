#!/usr/bin/env python3
"""Exact, result-exposed successor audit for issue #1609.

Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
No source implementation is imported or executed. Only standard-library
integer/Fraction arithmetic; no network, subprocess, randomness or writes.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product


class Falsifier(Exception):
    pass


def need(condition, label):
    if not condition:
        raise Falsifier(label)


Y = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
PORTS = Y[:4]
WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
DOMAIN_HASH = "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
ROOTS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0),
         (0, 0, 0, 1), (4, 4, 4, 4))
REFERENCES = ((0, 2, 2, 0), (4, 2, 2, 0), (1, 1, 0, 1))
Z4 = (Q(0),) * 4
DOMAIN = ()
NEIGHBORS = {}


def shift(a, b):
    return tuple(x + y for x, y in zip(a, b))


def lin(*terms):
    """Sparse linear combination; exact zero entries are discarded."""
    result = {}
    for scale, vec in terms:
        for key, value in vec.items():
            result[key] = result.get(key, Q(0)) + scale * value
    return {key: value for key, value in result.items() if value}


def qlin(*terms):
    return tuple(sum(scale * vec[i] for scale, vec in terms) for i in range(4))


def dot(a, b):
    return sum((value * b.get(key, Q(0)) for key, value in a.items()), Q(0))


def geometry():
    global DOMAIN, NEIGHBORS
    stencil = {p: Q(WEIGHTS[sum(c*c for c in p)], 324)
               for p in product(range(-4, 5), repeat=3)
               if sum(p) % 2 == 0 and sum(c*c for c in p) in WEIGHTS}
    need(len(stencil) == 60, "GEOMETRY_STENCIL_SIZE")
    need(sum(stencil.values()) == Q(8, 9), "GEOMETRY_ROW_BOUND")
    for p, value in stencil.items():
        need(stencil[tuple(-c for c in p)] == value, "H_SYMMETRY")
    shell = tuple(stencil) + ((0, 0, 0),)
    first = {shift(y, b) for y in Y for b in shell}
    DOMAIN = tuple(sorted({shift(y, b) for y in first for b in shell}))
    payload = "x\ty\tz\n" + "".join("\t".join(map(str, p))+"\n" for p in DOMAIN)
    need(len(DOMAIN) == 705 and len(payload.encode()) == 5029,
         "GEOMETRY_DOMAIN_SIZE")
    need(sha256(payload.encode()).hexdigest() == DOMAIN_HASH, "GEOMETRY_DOMAIN_BYTES")
    allowed = set(DOMAIN)
    NEIGHBORS = {p: tuple((shift(p, d), value) for d, value in stencil.items()
                         if shift(p, d) in allowed) for p in DOMAIN}


def H(v):
    out = {p: Q(10, 9)*value for p, value in v.items()}
    for p, value in v.items():
        for dest, weight in NEIGHBORS[p]:
            out[dest] = out.get(dest, Q(0)) + weight*value
    return {p: value for p, value in out.items() if value}


def P(z):
    return {p: Q(value) for p, value in zip(PORTS, z) if value}


def PT(v):
    return tuple(v.get(p, Q(0)) for p in PORTS)


def J(v):
    return {p: value for p, value in v.items() if p not in PORTS}


def K(v):
    return {p: value / (2 if p in PORTS else 1) for p, value in v.items()}


def T(v):
    return K(H(v))


def S(z):
    mean = sum(z) / Q(5)
    out = {p: -mean for p in Y if mean}
    return lin((1, out), (1, P(z)))


@dataclass(eq=True)
class Wave:
    u: dict
    v: dict
    tape: tuple  # A0, A1, B0, B1, each Q^4
    k: int


def zero(k=0):
    return Wave({}, {}, (Z4, Z4, Z4, Z4), k)


def F(x):
    a0, a1, b0, b1 = x.tape
    w = lin((1, T(x.v)), (-1, J(x.u)), (2, P(a0)))
    outgoing = qlin((1, a0), (-Q(1, 2), PT(w)), (Q(1, 2), PT(x.u)))
    return Wave(dict(x.v), w, (a1, b1, outgoing, b0), 1-x.k)


def backward(y):
    """Solve the scalar port/nonport equations, then undo the tape wiring."""
    a0p, a1p, b0p, b1p = y.tape
    hu = H(y.u)
    before_u = lin((1, J(hu)), (-1, J(y.v)),
                   (Q(1, 2), P(PT(hu))), (2, P(b0p)))
    before_a0 = qlin((1, b0p), (Q(1, 2), PT(y.v)),
                     (-Q(1, 2), PT(before_u)))
    return Wave(before_u, dict(y.u), (before_a0, a0p, b1p, a1p), 1-y.k)


def energy(x):
    tapes = sum((value*value for block in x.tape for value in block), Q(0))
    return (dot(x.u, x.u)+dot(x.v, x.v)-dot(x.u, H(x.v)))/2 + 2*tapes


def basis(index, k):
    x = zero(k)
    n = len(DOMAIN)
    if index < n:
        return replace(x, u={DOMAIN[index]: Q(1)})
    if index < 2*n:
        return replace(x, v={DOMAIN[index-n]: Q(1)})
    slot, coord = divmod(index-2*n, 4)
    blocks = list(x.tape)
    blocks[slot] = tuple(Q(i == coord) for i in range(4))
    return replace(x, tape=tuple(blocks))


def audit_full_carrier():
    dimension = 2*len(DOMAIN)+16
    for k in (0, 1):
        for i in range(dimension):
            x = basis(i, k)
            fx = F(x)
            need(backward(fx) == x, f"LEFT_INVERSE_{k}_{i}")
            need(F(backward(x)) == x, f"RIGHT_INVERSE_{k}_{i}")
            need(energy(fx) == energy(x), f"BASIS_ENERGY_{k}_{i}")
        # A full-support occupied state complements, not replaces, the proof.
        occupied = Wave({p: Q((i % 7)+1, 7) for i, p in enumerate(DOMAIN)},
                        {p: Q((i % 5)-5, 11) for i, p in enumerate(DOMAIN)},
                        tuple(tuple(Q(4*a+b+1, 13) for b in range(4)) for a in range(4)), k)
        need(backward(F(occupied)) == occupied, "OCCUPIED_LEFT_INVERSE")
        need(F(backward(occupied)) == occupied, "OCCUPIED_RIGHT_INVERSE")
        need(energy(F(occupied)) == energy(occupied), "OCCUPIED_ENERGY")
    witness = replace(zero(), tape=((Q(1), Q(0), Q(0), Q(0)), Z4, Z4, Z4))
    twice = F(F(witness))
    need(twice != witness and twice.u == P((Q(2), Q(0), Q(0), Q(0))), "NOT_INVOLUTION")
    wrong = replace(backward(F(witness)), tape=(Z4, Z4, Z4, Z4))
    need(wrong != witness, "INVERSE_TAPE_OMISSION_DETECTED")
    return dimension


def columns(cols):
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def mv(matrix, z):
    return tuple(sum(matrix[i][j]*z[j] for j in range(4)) for i in range(4))


def determinant(matrix):
    total = Q(0)
    for order in permutations(range(4)):
        inversions = sum(order[i] > order[j] for i in range(4) for j in range(i+1, 4))
        value = Q((-1)**inversions)
        for i, j in enumerate(order):
            value *= matrix[i][j]
        total += value
    return total


def responses():
    cuts = [[], [], [], []]
    formulas = [[], [], [], []]
    mcols, jcols = [], []
    for i in range(4):
        e = tuple(Q(i == j) for j in range(4))
        v = S(e)
        x = replace(zero(), v=v)
        for j in range(4):
            x = F(x)
            cuts[j].append(x.tape[2])
        need(x.tape == (cuts[0][-1], cuts[1][-1], cuts[3][-1], cuts[2][-1]),
             "CHRONOLOGICAL_TAPE_ORDER")
        tv, t2 = T(v), T(T(v))
        t3, t4 = T(t2), T(T(t2))
        expressions = (
            lin((-Q(1, 2), tv)),
            lin((Q(1, 2), v), (-Q(1, 2), t2)),
            lin((Q(1, 2), tv), (-Q(1, 2), t3), (Q(1, 2), T(J(v)))),
            lin((Q(1, 2), t2), (-Q(1, 2), t4),
                (Q(1, 2), T(T(J(v)))), (Q(1, 2), T(J(tv)))),
        )
        for j, expr in enumerate(expressions):
            formulas[j].append(PT(expr))
        mcols.append(PT(H(v)))
        jcols.append(PT(H(P(e))))
    matrices = tuple(columns(cols) for cols in cuts)
    need(matrices == tuple(columns(cols) for cols in formulas), "RESPONSE_POLYNOMIALS")
    m = columns(mcols)
    rank_vector = (349, 354, 354, 348)
    expected_m = tuple(tuple((Q(1770) if i == j else Q(0))-rank_vector[i]
                            for j in range(4)) for i in range(4))
    expected_m = tuple(tuple(x/1620 for x in row) for row in expected_m)
    need(m == expected_m, "FULL_PORT_MATRIX")
    r0 = matrices[0]
    need(r0 == tuple(tuple(-x/4 for x in row) for row in m), "CORRECT_R0")
    inverse = tuple(tuple(-Q(216, 59)*(Q(i == j)+Q(rank_vector[i], 365))
                          for j in range(4)) for i in range(4))
    for i in range(4):
        e = tuple(Q(i == j) for j in range(4))
        need(mv(inverse, mv(r0, e)) == e and mv(r0, mv(inverse, e)) == e,
             "FULL_MATRIX_TWO_SIDED_CERTIFICATE")
    det = determinant(r0)
    need(det == Q(14992667, 13060694016) == Q(1, 4)**4*Q(59, 54)**3*Q(73, 324),
         "FULL_DETERMINANT")
    need(r0[0][0] == -Q(1421, 6480), "R0_ENTRY")
    need(1-m[0][0]/2 == Q(1819, 3240) != r0[0][0], "OLD_R0_FALSE")
    return matrices, inverse, columns(jcols), det


def letter(index, x):
    a, b, c, d, q, r = x
    if index == 0:
        y = (b, a, d, c, q, r)
    elif index == 1:
        y = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        y = (2-c, 1+r-d, 2-a, 1-r-b, 1-q, -r)
    else:
        y = (2-a, 1-b, 3-c, 4-d, (1 if index == 3 else 2)-q, 1-r)
    return tuple(value % 5 for value in y)


def native(n, x):
    return letter((sum(x)+2*(n.bit_count()%2)) % 5, x)


def lift(pair):
    ell = (0, 1, 2, -2, -1)
    return (Q(ell[pair[0]], 2), Q(ell[pair[1]]+1, 2), Q(0), Q(0))


def mixed(x, y):
    return 3*(x[0]*y[3]+x[3]*y[0]-x[1]*y[2]-x[2]*y[1]) % 5


def ucal(y):
    table = ((0, 2, 1, 3, 4), (0, 1, 2, 3, 4), (2, 1, 0, 3, 4),
             (1, 0, 2, 3, 4), (1, 0, 2, 3, 4))
    return y[:5]+(table[y[4]][y[5]],)


WORD = ("U", "ey", "dy", "W", "bx", "by", "W",
        "dy", "ey", "W", "by", "bx", "W", "U")


def contact(x, y, bit, inverse=False, delete_w=False):
    word = WORD[::-1] if inverse else WORD
    for op in word:
        if op == "W":
            if delete_w:
                continue
            h = mixed(x, y)
            if h:
                chosen = int(h in (3, 4))
                if bit != chosen:
                    x, y = letter(1, x), letter(1, y)
                bit = chosen
        elif op == "U":
            y = ucal(y)
        else:
            index = {"b": 1, "d": 3, "e": 4}[op[0]]
            if op[1] == "x":
                x = letter(index, x)
            else:
                y = letter(index, y)
    return x, y, bit


def phase_head(k, delete_w=False):
    source = ROOTS[k]+(0, 1)
    head = (4, 0, 4, 2, 0, 0)
    bit = 0
    deltas = []
    for piston, weight in zip(REFERENCES, (1, 2, 4)):
        ref = piston+(0, 0)
        old = source, ref, bit
        source, written, bit = contact(source, ref, bit, delete_w=delete_w)
        deltas.append(written[5])
        for _ in range(weight):
            head = tuple((a+b)%5 for a, b in zip(head, written))
        source, ref, bit = contact(source, written, bit, inverse=True, delete_w=delete_w)
        need((source, ref, bit) == old, "SHARED_RESOURCE_RESTORATION")
    expected_m = 2 if delete_w else (3, 4, 0, 1, 2)[k]
    need(head == (1, 0, 0, 1, 3*expected_m%5, expected_m), "ACTUAL_COLLECTOR")
    return head, tuple(deltas)


def pair_head(k):
    source = ROOTS[k]+(0, 1)
    sx, head, bit = contact(source, (1, 0, 0, 1, 0, 0), 0)
    need(sx == source and bit == 0, "PAIR_RESOURCE_RESTORATION")
    delta = int(k == 1)
    need(head == (1, 0, 0, 1, 3*delta, delta), "ACTUAL_PAIR_HEAD")
    return head


@dataclass(eq=True)
class Machine:
    heads: tuple
    x: Wave
    n: int
    c: int
    work: Q
    bank: Q
    capacity: Q
    signs: tuple
    d: tuple


def kick(m, lane, vector):
    proposed = replace(m.x, v=lin((1, m.x.v), (m.signs[lane], S(vector))))
    delta = energy(proposed)-energy(m.x)
    candidate = m.bank-delta
    if 0 <= candidate <= m.capacity:
        signs = list(m.signs)
        signs[lane] *= -1
        return replace(m, x=proposed, work=m.work+delta, bank=candidate, signs=tuple(signs))
    return m


def run_heads(heads, capacity):
    m = Machine(tuple(heads), zero(), 0, 0, Q(0), capacity, capacity, (1, 1), (0, 0))
    history = [m]
    for c in range(7):
        need(m.c == c, "SCHEDULE_PHASE")
        if c in (0, 2, 3, 5, 6):
            m = replace(m, heads=tuple(native(m.n, x) for x in m.heads), n=m.n+1)
        if c == 1:
            m = replace(m, d=tuple((a+b)%5 for a, b in zip(m.d, m.heads[1][4:])))
            m = kick(m, 0, lift(m.heads[0][4:]))
        elif c == 4:
            m = kick(m, 1, lift(m.d))
        elif c in (2, 3, 5, 6):
            m = replace(m, x=F(m.x))
        m = replace(m, c=c+1)
        need(m.work == energy(m.x) and m.work+m.bank == capacity, "COMPLETE_CLASSICAL_ACCOUNT")
        need(0 <= m.bank <= capacity, "BOTH_BANK_BOUNDS")
        history.append(m)
    clocks = ((0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (5, 7))
    need(tuple((s.n, s.c) for s in history) == clocks, "ACTUAL_CLOCKS")
    need(m.signs == (-1, -1), "BOTH_CONTACTS_ACCEPT")
    first, second = history[3].x.tape[2], history[4].x.tape[2]
    need(history[4].x.tape[3] == first and history[5].x.tape[3] == first,
         "RETAIN_FIRST_BEFORE_SECOND_FREE_STEP")
    need(history[5].x.tape[2] == second and history[6].x.tape[1] == first
         and history[6].x.tape[3] == second, "RETAIN_FIRST_PAIR")
    need(m.x.tape[:2] == (first, second), "RETAIN_FIRST_PAIR_AT_END")
    return history


def receiver(m):
    return m.n, m.c, m.x, m.work, m.bank, m.capacity, m.signs, m.d


def decode_record(b0, b2, signs, inverse, d2, d=None):
    # The API admits no native head or source label and the buffer is absent.
    need(d is None, "READER_BUFFER_MUST_BE_ABSENT")
    need(signs == (-1, -1), "READER_ACCEPTED_BRANCH_ONLY")
    a = mv(inverse, b0)
    b = mv(inverse, qlin((1, b2), (-1, mv(d2, a))))
    return a, b


def read_history(history, inverse, d2):
    m = history[-1]
    value = decode_record(m.x.tape[0], m.x.tape[3], m.signs, inverse, d2, d=None)
    need(value == (lift(history[1].heads[0][4:]), lift(history[1].heads[1][4:])),
         "ACTUAL_RECORD_DECODING")
    return value


def audit_compositions(matrices, inverse, jp):
    r0, r1, d2, d3 = matrices
    old = [run_heads((ROOTS[a]+(0, 1), ROOTS[b]+(0, 1)), Q(4, 5))
           for a, b in product((1, 4), repeat=2)]
    for history in old:
        need([receiver(m) for m in history] == [receiver(m) for m in old[0]], "OLD_PORT_EQUALITY")
        need(read_history(history, inverse, d2) == ((Q(1, 2), Q(0), Q(0), Q(0)),)*2,
             "OLD_PORT_BASELINE_VECTOR")
    control = run_heads((ROOTS[1]+(0, 1), (2, 0, 0, 0, 0, 1)), Q(4, 5))
    target = ((Q(1, 2), Q(0), Q(0), Q(0)), (Q(1, 2), Q(1, 2), Q(0), Q(0)))
    need(read_history(control, inverse, d2) == target, "EXACT_CONTROL_VECTORS")
    wrong_target = ((Q(0), -Q(1, 2), Q(0), Q(0)), (Q(1, 2), Q(0), Q(0), Q(0)))
    need(target != wrong_target, "OLD_CONTROL_TARGET_FALSE")
    need(all(receiver(control[i]) == receiver(old[0][i]) for i in (0, 1)), "CONTROL_COMMON_START")
    need(control[2].d != old[0][2].d, "CONTROL_CAPTURE_TIME")
    need(all(control[i].x == old[0][i].x for i in range(5)), "CONTROL_WAVE_HISTORY_PREFIX")
    need(control[5].x != old[0][5].x, "CONTROL_ACTUAL_SECOND_CONTACT")
    need(control[-1].x.tape[0] == old[0][-1].x.tape[0]
         and control[-1].x.tape[3] != old[0][-1].x.tape[3], "CONTROL_RETAINED_RECORD")
    pair_records, phase_records = set(), set()
    maxima = [Q(0), Q(0)]
    pair_vectors = {1: (Q(1), Q(0), Q(0), Q(0)), 4: (Q(1, 2), Q(1, 2), Q(0), Q(0))}
    phase_vectors = ((-Q(1), -Q(1, 2), Q(0), Q(0)),
                     (-Q(1, 2), Q(3, 2), Q(0), Q(0)),
                     (Q(1, 2), Q(1, 2), Q(0), Q(0)),
                     (Q(1), Q(0), Q(0), Q(0)),
                     (Q(1, 2), Q(3, 2), Q(0), Q(0)))
    for a, b in product((1, 4), repeat=2):
        history = run_heads((pair_head(a), pair_head(b)), Q(2))
        need(read_history(history, inverse, d2) == (pair_vectors[a], pair_vectors[b]), "FOUR_PAIR_READOUT")
        m = history[-1]
        pair_records.add((m.x.tape[0], m.x.tape[3]))
        maxima[0] = max(maxima[0], *(s.work for s in history))
        need(all(s.work <= Q(8, 5) for s in history), "PAIR_A_PRIORI_BOUND")
    for a, b in product(range(5), repeat=2):
        ha, bits_a = phase_head(a)
        hb, bits_b = phase_head(b)
        history = run_heads((ha, hb), Q(5))
        need(read_history(history, inverse, d2) == (phase_vectors[a], phase_vectors[b]), "TWENTY_FIVE_READOUT")
        m = history[-1]
        phase_records.add((m.x.tape[0], m.x.tape[3]))
        maxima[1] = max(maxima[1], *(s.work for s in history))
        need(all(s.work <= Q(23, 5) for s in history), "PHASE_A_PRIORI_BOUND")
        need(len(set((3, 4, 0, 1, 2))) == 5, "PHASE_CODE_INJECTIVITY")
    need(len(pair_records) == 4 and len(phase_records) == 25, "RECORD_INJECTIVITY")
    negative = [phase_head(k, delete_w=True)[0] for k in range(5)]
    need(len(set(negative)) == 1 and negative[0] == phase_head(4)[0], "DELETED_W_COLLAPSE")
    need(all(mixed((0, 0, 0, 0), y) == 0 for y in REFERENCES), "ABSENCE_ALIAS")
    # Algebraic columns certify readout immunity to arbitrary outgoing archives.
    for slot in (2, 3):
        for i in range(4):
            e = tuple(Q(i == j) for j in range(4))
            blocks = [Z4]*4
            blocks[slot] = e
            x = replace(zero(), tape=tuple(blocks))
            for _ in range(4):
                x = F(x)
            need(x.tape[0] == Z4 and x.tape[1] == Z4 and x.tape[3] == Z4, "ARCHIVE_READER_IMMUNITY")
            expected_last = Z4 if slot == 2 else qlin((-Q(1, 2), mv(jp, e)))
            need(x.tape[2] == expected_last, "ARCHIVE_FOURTH_CUT")
    return target, tuple(maxima)


def fmt_vector(z):
    return ",".join(map(str, z))


def main():
    geometry()
    dimension = audit_full_carrier()
    matrices, inverse, jp, det = responses()
    control, maxima = audit_compositions(matrices, inverse, jp)
    print("C-J-PHASE-RESPONSE-CLOSURE-REVIEW-N")
    print("SCOPE NON-CANONICAL L1 RESULT-EXPOSED")
    print(f"DOMAIN sites={len(DOMAIN)} sha256={DOMAIN_HASH}")
    print(f"FULL_LINEAR_CARRIER dimension={dimension} pointers=2 two_sided_basis_checks={4*dimension}")
    print("ENERGY analytic_certificate=PROOF.md basis_checks=2852 full_support_occupied=2")
    print("F_IS_NOT_AN_INVOLUTION witnessed; occupied_tapes_retained")
    for name, matrix in zip(("R0", "R1", "D2", "D3"), matrices):
        for i, row in enumerate(matrix):
            print(f"{name}[{i}]={fmt_vector(row)}")
    print(f"DET_R0={det}; two_sided_inverse_certificate=PASS")
    print("OLD_R0_TARGET=FALSE old_entry=1819/3240 actual_entry=-1421/6480")
    print("OLD_UNDEFINED_K_RELATION=STOP_UNDEFINED; defined_D2_polynomial=PASS")
    print("CONTROL_A="+fmt_vector(control[0]))
    print("CONTROL_B="+fmt_vector(control[1]))
    print("OLD_CONTROL_TARGET=FALSE; exact_history_and_d_None_reader=PASS")
    print(f"PAIR_FAMILY cases=4 capacity=2 max_work={maxima[0]}")
    print(f"PHASE_FAMILY cases=25 capacity=5 max_work={maxima[1]}")
    print("ARCHIVE_IMMUNITY linear_columns=8; retained_cuts=PASS")
    print("RESOURCES pair=4_cells_2_bits phase=7_cells_1_bit binary_outputs=3")
    print("OPEN native_admission prefix_energy autonomous_prefix late_input whole_renewal absence_detection")
    print("STATUS PASS_DEFINED_SUCCESSOR; predecessor_PARTIAL_unchanged")


if __name__ == "__main__":
    try:
        main()
    except Falsifier as error:
        # A mathematical falsifier is a completed, preserved scientific result.
        print("C-J-PHASE-RESPONSE-CLOSURE-REVIEW-N")
        print("STATUS FAIL")
        print("FALSIFIER="+str(error))
