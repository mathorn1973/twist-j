#!/usr/bin/env python3
"""NON-CANONICAL independent breaker for the frozen contact-table class.

This file is independent of the primary verifier and repository verifiers.
No counts or census digests are supplied as targets.  Only the preregistered
source identities and the two explicitly supplied regression tables are used.

Completeness reductions used here
---------------------------------
1. Enumerate all 4**10 raw control tables.  On h=0 the two beta values must
   differ.  On each nonzero pair, the four images of (u,eta) must differ.
   These conditions are necessary and sufficient on every complete I orbit.
   At h=0, beta is also the action on I-fixed states, so those are covered.
   Every h admits the specified piston witness with distinct I images;
   hence equality of the ten digits is equality of complete W maps.

2. A label permutation lifts to data by the parity of the change of u.
   This is the actual I action, including both q and both r coordinates.
   Its translation commutator is evaluated with symbolic affine q/r data,
   then on every pair of q values.  Consequently the reduction does not
   discard occupied eta, a second port, or an r sign.  The native leaves
   are independently replayed for every required full-coordinate witness.

3. Write x_q=P_q(0).  The ready contract is equivalent to
   P_q(1)=x_(q+2).  A table exists precisely when x_q != x_(q+2) at every q;
   then P_q(2)=3-x_q-x_(q+2).  Enumerating all 3**5 column assignments is
   therefore a bijective complete construction, independent of a product
   enumeration of five S3 factors.  S3 is used below only for relabelings.

4. Equal endpoint signatures imply P'_q=L P_q for one common L: propagate
   P'_(q+3) P_(q+3)^-1 = P'_q P_q^-1 around the q -> q+3 cycle.  This is
   checked against literal endpoint fibres and actual left relabelings.
   Translation, internal, and joint stabilizers are counted separately.

The finite checks are conditional L1 evidence only.  They do not admit the
interfaces physically or compare W prefixes, compiled words, or q lifts.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys


PREREG_SHA256 = "594b871504191af2b1f3d9ab70ca1398032bad6b767ab1c85e6e92a864790f6b"
CANON_SHA256 = "5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4"
CANON_BYTES = 980212
IDENTITY3 = (0, 1, 2)
OLD_READER = ((0, 2, 1), (0, 1, 2), (2, 1, 0), (1, 0, 2), (1, 0, 2))


class AuditFailure(Exception):
    """An exact failed obligation and its complete local witness."""


def require(condition, obligation, **witness):
    if not condition:
        raise AuditFailure({"status": "FAIL", "obligation": obligation,
                            "witness": witness})


def identify(values):
    return "".join(str(value) for value in values)


def pin_audit():
    here = Path(__file__).resolve().parent
    prereg = (here / "PREREG.md").read_bytes()
    canon = (here.parent.parent / "canon" / "CANON.md").read_bytes()
    require(sha256(prereg).hexdigest() == PREREG_SHA256,
            "frozen preregistration identity", actual=sha256(prereg).hexdigest())
    require(len(canon) == CANON_BYTES and sha256(canon).hexdigest() == CANON_SHA256,
            "pinned source Canon identity", bytes=len(canon),
            sha256=sha256(canon).hexdigest())


def b(cell):
    p, t, u, v, q, r = cell
    return ((-u) % 5, (-v) % 5, (-p) % 5, (-t) % 5, (-q) % 5, (-r) % 5)


def d(cell):
    p, t, u, v, q, r = cell
    return ((2-p) % 5, (1-t) % 5, (3-u) % 5, (4-v) % 5,
            (1-q) % 5, (1-r) % 5)


def e(cell):
    p, t, u, v, q, r = cell
    return ((2-p) % 5, (1-t) % 5, (3-u) % 5, (4-v) % 5,
            (2-q) % 5, (1-r) % 5)


def det(piston):
    return (piston[0]*piston[3] - piston[1]*piston[2]) % 5


def h_det(x, y):
    added = tuple((x[j]+y[j]) % 5 for j in range(4))
    return 3 * (det(added)-det(x)-det(y)) % 5


def h_native(state):
    # Audited against the displayed determinant definition on all 5**8 pairs.
    return 3 * (state[0]*state[9] + state[6]*state[3]
                - state[1]*state[8] - state[7]*state[2]) % 5


def source_audit():
    cells = tuple(product(range(5), repeat=6))
    tables = tuple({cell: fn(cell) for cell in cells} for fn in (b, d, e))
    bt, dt, et = tables
    for cell in cells:
        bc, dc, ec = bt[cell], dt[cell], et[cell]
        forward, reverse = et[dc], dt[ec]
        plus = cell[:4] + ((cell[4]+1) % 5, cell[5])
        minus = cell[:4] + ((cell[4]-1) % 5, cell[5])
        require(bt[bc] == dt[dc] == et[ec] == cell,
                "complete native involution identities", cell=cell)
        require(forward == plus and reverse == minus,
                "complete native tau and inverse", cell=cell,
                tau=forward, tau_inverse=reverse)
        require(dt[et[forward]] == et[dt[reverse]] == cell,
                "complete tau inverse compositions", cell=cell)
        require(bt[et[dt[bc]]] == reverse and bt[dt[et[bc]]] == forward,
                "complete I/tau inversion on each cell", cell=cell)
    for name, table in zip(("b", "d", "e"), tables):
        require(len(set(table.values())) == len(cells),
                "complete native bijection", generator=name)
    for pistons in product(range(5), repeat=8):
        x, y = pistons[:4], pistons[4:]
        ix = tuple((-x[j]) % 5 for j in (2, 3, 0, 1))
        iy = tuple((-y[j]) % 5 for j in (2, 3, 0, 1))
        mixed = h_det(x, y)
        state = x + (0, 0) + y + (0, 0, 0)
        require(h_det(ix, iy) == (-mixed) % 5,
                "h(I s)=-h(s) on all piston pairs", pistons=pistons)
        require(h_native(state) == mixed,
                "mixed bilinear expression agrees with source determinant",
                pistons=pistons)
    return tables


def piston_witness(h, eta, port=0, q=0):
    qx, qy = (q, 2) if port == 0 else (2, q)
    return (1, 0, 0, 0, qx, 1, 0, 0, 0, 2*h % 5, qy, 2, eta)


class Native:
    """Direct native leaf replay using exhaustively audited cell tables."""

    def __init__(self, tables):
        self.bt, self.dt, self.et = tables

    def involution(self, state):
        return self.bt[state[:6]] + self.bt[state[6:12]] + state[12:]

    def control(self, state, code):
        digit = code[2*h_native(state)+state[12]]
        if digit >= 2:
            state = self.involution(state)
        return state[:12] + (digit & 1,)

    def leaf(self, state, which, port, code, inverse):
        if which == "W":
            return self.control(state, code)
        if which == "V":
            return self.control(state, inverse)
        if which == "x":
            return self.bt[state[:6]] + state[6:]
        if which == "y":
            return state[:6] + self.bt[state[6:12]] + state[12:]
        table = self.dt if which == "d" else self.et
        if port == 0:
            return table[state[:6]] + state[6:]
        return state[:6] + table[state[6:12]] + state[12:]

    def word(self, state, letters, port, code, inverse):
        for letter in letters:
            state = self.leaf(state, letter, port, code, inverse)
        return state


# Execution order for E tau E^-1 tau^-1, with E=W I W^-1=E^-1.
# Unlike the supplied W_b, an arbitrary W need not be an involution.
FORWARD_WORD = ("e", "d", "V", "y", "x", "W",
                "d", "e", "V", "y", "x", "W")
INVERSE_WORD = tuple({"W": "V", "V": "W"}.get(a, a)
                     for a in reversed(FORWARD_WORD))


def faithful_control_audit(native):
    for h in range(5):
        for eta in range(2):
            state = piston_witness(h, eta)
            require(h_native(state) == h and native.involution(state) != state,
                    "faithful full-coordinate witness on every h sheet", h=h, eta=eta)
            outputs = set()
            for digit in range(4):
                code = [0]*10
                code[2*h+eta] = digit
                outputs.add(native.control(state, code))
            require(len(outputs) == 4, "literal table equality is faithful",
                    h=h, eta=eta)


def admissible(code):
    # This tests bijection only; no contact response is an admission filter.
    return ((code[0] & 1) != (code[1] & 1)
            and len({code[2], code[3], code[8] ^ 2, code[9] ^ 2}) == 4
            and len({code[4], code[5], code[6] ^ 2, code[7] ^ 2}) == 4)


def raw_controls():
    for code in product(range(4), repeat=10):
        if admissible(code):
            yield code


def inverse_control(code):
    inverse = [None]*10
    for h in range(5):
        for eta in range(2):
            digit = code[2*h+eta]
            a, beta = divmod(digit, 2)
            target = 2*((-h) % 5 if a else h)+beta
            require(inverse[target] is None, "raw control inverse uniqueness", code=code)
            inverse[target] = 2*a+eta
    require(None not in inverse and admissible(inverse),
            "inverse lies in the complete table class", code=code)
    inverse = tuple(inverse)
    for h in range(5):
        for eta in range(2):
            a, beta = divmod(code[2*h+eta], 2)
            hp = (-h) % 5 if a else h
            ai, back = divmod(inverse[2*hp+beta], 2)
            require(ai == a and back == eta,
                    "symbolic complete control inverse", code=code, h=h, eta=eta)
    return inverse


def label_permutations(code):
    return ((code[0], code[1], code[0] ^ 2, code[1] ^ 2),
            (code[2], code[3], code[8] ^ 2, code[9] ^ 2),
            (code[4], code[5], code[6] ^ 2, code[7] ^ 2))


def small_word(conjugate, start, port, backwards):
    """Return the exact lift (label, common sign, q_x shift, q_y shift).

    The common sign acts also on both r coordinates.  Translating either
    q fixes h, so each next E uses the current label without a saved input.
    """
    label, sign, tx, ty = start, 1, 0, 0
    operations = ("E", "-", "E", "+") if backwards else ("-", "E", "+", "E")
    for operation in operations:
        if operation == "E":
            next_label = conjugate[label]
            parity = -1 if (label ^ next_label) & 2 else 1
            label, sign = next_label, parity*sign
            tx, ty = parity*tx % 5, parity*ty % 5
        elif port == 0:
            tx = (tx + (1 if operation == "+" else -1)) % 5
        else:
            ty = (ty + (1 if operation == "+" else -1)) % 5
    return label, sign, tx, ty


def small_contact_audit(code, inverse):
    shifts = [None]*5
    small_involutive = True
    for k, perm in enumerate(label_permutations(code)):
        require(sorted(perm) == list(range(4)), "faithful orbit permutation", code=code, k=k)
        small_involutive = small_involutive and all(perm[perm[j]] == j for j in range(4))
        pi = tuple(perm.index(j) for j in range(4))
        conjugate = tuple(perm[pi[j] ^ 2] for j in range(4))
        require(all(conjugate[conjugate[j]] == j for j in range(4)),
                "conjugate I involution", code=code, k=k)
        for label in range(4):
            u, eta = divmod(label, 2)
            h = ((-k) % 5 if u else k) if k else 0
            for port in range(2):
                lift = small_word(conjugate, label, port, False)
                undo = small_word(conjugate, label, port, True)
                require(lift[:2] == undo[:2] == (label, 1),
                        "contact restores pistons, occupied eta and both r signs",
                        code=code, k=k, label=label, port=port, lift=lift, inverse=undo)
                delta = lift[2+port]
                require(delta in (0, 3) and lift[3-port] == 0,
                        "anticipated single-port binary translation",
                        code=code, h=h, eta=eta, port=port, lift=lift)
                require(undo[2+port] == (-delta) % 5 and undo[3-port] == 0,
                        "complete contact inverse lift", code=code, h=h, port=port)
                if shifts[h] is None:
                    shifts[h] = delta
                require(shifts[h] == delta, "contact independent of occupied eta and port",
                        code=code, h=h, eta=eta, port=port, shift=delta)
                for qx, qy in product(range(5), repeat=2):
                    forward = ((lift[1]*qx+lift[2]) % 5, (lift[1]*qy+lift[3]) % 5)
                    backward = ((undo[1]*qx+undo[2]) % 5, (undo[1]*qy+undo[3]) % 5)
                    wanted = ((qx+delta) % 5, qy) if port == 0 else (qx, (qy+delta) % 5)
                    wanted_back = ((qx-delta) % 5, qy) if port == 0 else (qx, (qy-delta) % 5)
                    require(forward == wanted and backward == wanted_back,
                            "complete two-q faithful action", code=code,
                            h=h, eta=eta, port=port, q=(qx, qy))
    require(small_involutive == (code == inverse),
            "involutive complete-map subclass", code=code)
    require(shifts[0] == 3 and shifts[1] == shifts[4] and shifts[2] == shifts[3],
            "anticipated even contact profile with chi(0)=1", code=code, shifts=shifts)
    return identify((2*shifts[1] % 5, 2*shifts[2] % 5)), tuple(shifts)


def native_control_witnesses(native, code, inverse, shifts):
    for h in range(5):
        for eta in range(2):
            for port in range(2):
                for q in range(5):
                    state = piston_witness(h, eta, port, q)
                    index = 4+6*port
                    for letters, direction in ((FORWARD_WORD, 1), (INVERSE_WORD, -1)):
                        expected = list(state)
                        expected[index] = (q+direction*shifts[h]) % 5
                        observed = native.word(state, letters, port, code, inverse)
                        require(observed == tuple(expected),
                                "direct complete native-coordinate contact word",
                                code=code, state=state, port=port, direction=direction,
                                expected=expected, observed=observed)


def fixed_I_audit(native, zero_tables):
    # These are every I-fixed pair: four independent piston coordinates,
    # p1p=-p1, p4p=-p4 in each cell, and all q,r equal zero.  On h=0 no
    # other control entries are reachable, so one representative per
    # zero-table proves the check for all their admitted extensions.
    for zero in sorted(zero_tables):
        code = zero + (0, 1)*4
        inverse = inverse_control(code)
        for p, t, u, v in product(range(5), repeat=4):
            for eta in range(2):
                state = (p, t, -p % 5, -t % 5, 0, 0,
                         u, v, -u % 5, -v % 5, 0, 0, eta)
                require(native.involution(state) == state and h_native(state) == 0,
                        "complete I-fixed-state parametrization", state=state)
                for port in range(2):
                    for letters, shift in ((FORWARD_WORD, 3), (INVERSE_WORD, 2)):
                        expected = list(state)
                        expected[4+6*port] = shift
                        observed = native.word(state, letters, port, code, inverse)
                        require(observed == tuple(expected), "contact across I-fixed states",
                                code=code, state=state, port=port, observed=observed)


def profile_witness(profile):
    # In the marked h coordinates use identity for an active nonzero pair,
    # and the source W_b pattern for an inactive pair.  All h=0 branches
    # here are identity.  These are witnesses, never admission filters.
    code = [0, 1]*5
    for k, bit in ((1, profile[0]), (2, profile[1])):
        if bit == "0":
            code[2*k:2*k+2] = (0, 2)
            code[2*(5-k):2*(5-k)+2] = (3, 1)
    return tuple(code)


def even_polynomial(shifts):
    # Search the entire degree<=4 even coefficient space.  Evaluation at
    # h=0,1,2 is nonsingular; the exact search also checks uniqueness.
    target = tuple(2*s % 5 for s in shifts)
    choices = [list(coefficients) for coefficients in product(range(5), repeat=3)
               if all((coefficients[0]+coefficients[1]*h*h+coefficients[2]*h**4) % 5
                      == target[h] for h in range(5))]
    require(len(choices) == 1, "unique even polynomial of degree at most four", shifts=shifts)
    return choices[0]


def controls_audit(native):
    records = {}
    law_counts, involutive_counts = Counter(), Counter()
    law_shifts, zero_tables = {}, set()
    total_involutive = 0
    for code in raw_controls():
        inverse = inverse_control(code)
        profile, shifts = small_contact_audit(code, inverse)
        native_control_witnesses(native, code, inverse, shifts)
        involutive = int(code == inverse)
        table_id = identify(code)
        require(table_id not in records, "raw control table enumeration is injective", code=code)
        records[table_id] = (profile, involutive)
        law_counts[profile] += 1
        involutive_counts[profile] += involutive
        total_involutive += involutive
        zero_tables.add(code[:2])
        if profile in law_shifts:
            require(law_shifts[profile] == shifts, "profile is complete contact-map equality", code=code)
        law_shifts[profile] = shifts
    fixed_I_audit(native, zero_tables)
    for profile, shifts in law_shifts.items():
        code = profile_witness(profile)
        require(admissible(code) and records.get(identify(code)) == (profile, 1),
                "explicit marked-coordinate involutive contact witness", profile=profile, code=code)
    for left, right in combinations(sorted(law_shifts), 2):
        differing = [h for h in range(5) if law_shifts[left][h] != law_shifts[right][h]]
        require(bool(differing), "different profiles are different complete contact maps",
                left=left, right=right)
        h = differing[0]
        state = piston_witness(h, 0)
        lc, rc = profile_witness(left), profile_witness(right)
        require(native.word(state, FORWARD_WORD, 0, lc, inverse_control(lc))
                != native.word(state, FORWARD_WORD, 0, rc, inverse_control(rc)),
                "explicit complete-map separation witness", left=left, right=right, state=state)
    old_w = (0, 1, 0, 2, 0, 2, 3, 1, 3, 1)
    require(records.get(identify(old_w)) == ("00", 1),
            "supplied v100 W_b class embedding", code=old_w)
    # Polynomial witnesses for every possible binary profile are checked
    # constructively as well as recording every profile actually enumerated.
    for bits in product("01", repeat=2):
        profile = "".join(bits)
        witness = profile_witness(profile)
        require(records.get(identify(witness)) == (profile, 1),
                "all binary contact profiles have explicit admitted witnesses", profile=profile)
    digest = sha256()
    for table_id, (profile, involutive) in sorted(records.items()):
        digest.update(f"{table_id}\t{profile}\t{involutive}\n".encode("ascii"))
    return ({"total": len(records), "involutive": total_involutive,
             "law_counts": dict(law_counts),
             "involutive_law_counts": dict(involutive_counts),
             "even_polynomials": {p: even_polynomial(s) for p, s in law_shifts.items()},
             "census_sha256": digest.hexdigest()}, law_shifts)


def table_id(table):
    return identify(value for row in table for value in row)


def reader_tables():
    # Exhaustive ready-column construction, not a Cartesian product of S3.
    for column in product(range(3), repeat=5):
        if all(column[q] != column[(q+2) % 5] for q in range(5)):
            yield tuple((column[q], column[(q+2) % 5],
                         3-column[q]-column[(q+2) % 5]) for q in range(5))


def inverse_reader(table):
    return tuple(tuple(row.index(r) for r in range(3)) for row in table)


def couple(table, q, r):
    return table[q][r] if r < 3 else r


def reader_step(table, inverse, q, r, shift):
    ready = couple(table, q, r)
    qp = (q+shift) % 5
    return qp, couple(inverse, qp, ready)


def endpoint_signature(table):
    inverse = inverse_reader(table)
    return identify(reader_step(table, inverse, q, r, 3)[1]
                    for q in range(5) for r in range(3))


def involutive_reader(table):
    return all(row[row[r]] == r for row in table for r in range(3))


def translate(table, t):
    return tuple(table[(q+t) % 5] for q in range(5))


def internal(table, relabel):
    return tuple(tuple(relabel[r] for r in row) for row in table)


def translate_signature(signature, t):
    return "".join(signature[3*((q+t) % 5):3*((q+t) % 5)+3] for q in range(5))


def reader_occupied_audit(table, laws):
    inverse = inverse_reader(table)
    require(all(sorted(row) == list(range(3)) for row in table),
            "constructed reference rows are permutations", table=table)
    for q in range(5):
        for r in range(5):
            require(couple(inverse, q, couple(table, q, r)) == r,
                    "identity experiment including occupied references", table=table, q=q, r=r)
            qp, rp = reader_step(table, inverse, q, r, 3)
            require(reader_step(table, inverse, qp, rp, -3) == (q, r),
                    "full endpoint-reader inverse", table=table, q=q, r=r)
            if r == 0:
                require(rp == 1, "marked ready one-query contract", table=table, q=q)
            if r >= 3:
                require(rp == r, "native inactive reference values fixed", table=table, q=q, r=r)
    for profile, shifts in laws.items():
        for h, shift in enumerate(shifts):
            for q in range(5):
                for r in range(5):
                    qp, rp = reader_step(table, inverse, q, r, shift)
                    # Direct expression and inverse use the CURRENT endpoint q.
                    expected = couple(inverse, (q+shift) % 5, couple(table, q, r))
                    require(rp == expected and qp == (q+shift) % 5,
                            "complete occupied reader paired with contact law",
                            table=table, profile=profile, h=h, q=q, r=r)
                    require(reader_step(table, inverse, qp, rp, -shift) == (q, r),
                            "paired complete reader inverse", table=table,
                            profile=profile, h=h, q=q, r=r)
                    qm, rm = reader_step(table, inverse, q, r, -shift)
                    require(reader_step(table, inverse, qm, rm, shift) == (q, r),
                            "paired complete reader inverse in reverse order",
                            table=table, profile=profile, h=h, q=q, r=r)
                    if r == 0:
                        require(rp == 2*shift % 5, "prepared output follows contact profile",
                                table=table, profile=profile, h=h, q=q)
                    advanced = (q, r)
                    for unused in range(5):
                        advanced = reader_step(table, inverse, *advanced, shift)
                    require(advanced == (q, r), "complete occupied reader fifth power",
                            table=table, profile=profile, h=h, q=q, r=r)


def readers_audit(laws):
    tables, signatures, flags = {}, {}, {}
    fibres = defaultdict(set)
    for table in reader_tables():
        tid = table_id(table)
        require(tid not in tables, "reference construction injectivity", table=table)
        reader_occupied_audit(table, laws)
        signature = endpoint_signature(table)
        tables[tid], signatures[tid], flags[tid] = table, signature, int(involutive_reader(table))
        fibres[signature].add(tid)
    require(table_id(OLD_READER) in tables and flags[table_id(OLD_READER)] == 1,
            "supplied v100 reference table class embedding", table=OLD_READER)
    relabelings = tuple(permutations(range(3)))
    q_reps, inv_q_reps, internal_reps, joint_reps = set(), set(), set(), set()
    endpoint_reps = set()
    for tid, table in tables.items():
        signature = signatures[tid]
        q_orbit = {table_id(translate(table, t)) for t in range(5)}
        q_stabilizer = {t for t in range(5) if translate(table, t) == table}
        require(q_orbit <= tables.keys() and len(q_orbit)*len(q_stabilizer) == 5,
                "table translation orbit and stabilizer", table=table)
        q_reps.add(min(q_orbit))
        if flags[tid]:
            require(all(flags[j] for j in q_orbit), "q translation preserves involutivity", table=table)
            inv_q_reps.add(min(q_orbit))
        internal_orbit = {table_id(internal(table, relabel)) for relabel in relabelings}
        internal_stabilizer = {relabel for relabel in relabelings if internal(table, relabel) == table}
        require(internal_orbit <= tables.keys() and internal_stabilizer == {IDENTITY3}
                and len(internal_orbit)*len(internal_stabilizer) == len(relabelings),
                "internal relabeling orbit and stabilizer", table=table)
        require(internal_orbit == fibres[signature],
                "literal complete endpoint equality iff common internal relabeling",
                table=table, signature=signature)
        internal_reps.add(min(internal_orbit))
        joint_orbit, joint_stabilizer = set(), set()
        for t in range(5):
            shifted = translate(table, t)
            shifted_signature = endpoint_signature(shifted)
            require(shifted_signature == translate_signature(signature, t),
                    "actual q-translation conjugacy of complete endpoint maps", table=table, t=t)
            for q, r in product(range(5), repeat=2):
                # T_-t R T_t, including r=3,4, verifies the conjugation direction.
                qp, rp = reader_step(table, inverse_reader(table), (q+t) % 5, r, 3)
                direct = reader_step(shifted, inverse_reader(shifted), q, r, 3)
                require(direct == ((qp-t) % 5, rp),
                        "full endpoint conjugacy including occupied native r", table=table, t=t, q=q, r=r)
            for relabel in relabelings:
                transformed = internal(shifted, relabel)
                transformed_id = table_id(transformed)
                joint_orbit.add(transformed_id)
                if transformed == table:
                    joint_stabilizer.add((t, relabel))
                require(transformed_id in tables
                        and signatures[transformed_id] == shifted_signature,
                        "joint algebraic relabeling complete-map action",
                        table=table, t=t, relabel=relabel)
        require(len(joint_orbit)*len(joint_stabilizer) == 5*len(relabelings),
                "joint orbit-stabilizer identity", table=table)
        joint_reps.add(min(joint_orbit))
        endpoint_orbit = {translate_signature(signature, t) for t in range(5)}
        endpoint_stabilizer = {t for t in range(5) if translate_signature(signature, t) == signature}
        require(endpoint_orbit <= fibres.keys() and len(endpoint_orbit)*len(endpoint_stabilizer) == 5,
                "endpoint translation orbit and stabilizer", signature=signature)
        require(len(endpoint_stabilizer) == len(joint_stabilizer),
                "unique internal compensation for an endpoint stabilizer", table=table)
        endpoint_reps.add(min(endpoint_orbit))
    require(len(internal_reps) == len(fibres) and len(joint_reps) == len(endpoint_reps),
            "complete endpoint quotients agree with algebraic orbit counts")
    digest = sha256()
    for tid in sorted(tables):
        digest.update(f"{tid}\t{signatures[tid]}\t{flags[tid]}\n".encode("ascii"))
    return {"total": len(tables), "involutive": sum(flags.values()),
            "table_q_orbits": len(q_reps), "endpoint_maps": len(fibres),
            "endpoint_q_orbits": len(endpoint_reps),
            "involutive_q_orbits": len(inv_q_reps),
            "internal_orbits": len(internal_reps), "joint_orbits": len(joint_reps),
            "census_sha256": digest.hexdigest()}


def main():
    pin_audit()
    native = Native(source_audit())
    faithful_control_audit(native)
    controls, laws = controls_audit(native)
    readers = readers_audit(laws)
    result = {"status": "PASS", "controls": controls, "readers": readers}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except AuditFailure as error:
        print(json.dumps(error.args[0], sort_keys=True, separators=(",", ":")))
        sys.exit(1)
