#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Independent PREREG-only exact audit; cyclic five-coordinate quotient ring."""
import json
import sys

CONTEXT = {"case": "fixtures", "cut": "initial"}


class AuditFailure(Exception):
    pass


def require(condition, name, observed=None, expected=None):
    if not condition:
        raise AuditFailure(json.dumps({"context": CONTEXT.copy(), "check": name,
                                       "observed": observed, "expected": expected},
                                      sort_keys=True, separators=(",", ":")))


# Quotient by the common-shift vector (1,1,1,1,1); choose minimum zero.
def norm(a):
    m = min(a)
    return tuple(x - m for x in a)


def add(a, b):
    return norm(tuple(x + y for x, y in zip(a, b)))


def neg(a):
    return norm(tuple(-x for x in a))


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return norm(tuple(n * x for x in a))


def mul(a, b):
    out = [0] * 5
    for i in range(5):
        for k in range(5):
            out[(i + k) % 5] += a[i] * b[k]
    return norm(out)


def conj(a):
    return norm(tuple(a[(-k) % 5] for k in range(5)))


def div_exact(a, n):
    # A quotient exists precisely when every cyclic coefficient has one residue.
    shift = a[4]
    lifted = tuple(x - shift for x in a)
    if any(x % n for x in lifted):
        return None
    return norm(tuple(x // n for x in lifted))


def ring_sum(values):
    out = ZERO
    for a in values:
        out = add(out, a)
    return out


def four(a):
    return [a[k] - a[4] for k in range(4)]


def from_four(a):
    return norm(tuple(a) + (0,))


def trace(a):
    return 5 * a[0] - sum(a)


def h(a):
    return mul(a, conj(a))


def q(a):
    tr = trace(h(a))
    require(tr % 2 == 0, "integral half trace", tr)
    # Independently verify the preregistered four-coordinate quadratic form.
    coeff = four(a)
    numerator = 5 * sum(x * x for x in coeff) - sum(coeff) ** 2
    require(numerator == tr, "Q formula", numerator, tr)
    return tr // 2


def residue(a):
    return sum(a) % 5


ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)
ROOT = (0, 1, 0, 0, 0)
ROOTS = [tuple(int(i == k) for i in range(5)) for k in range(5)]
RHO = ROOTS[2]
J = add(ONE, RHO)
JINV = neg(add(ROOT, RHO))
PHI = neg(add(ROOTS[2], ROOTS[3]))
RHOM1 = sub(RHO, ONE)


def scalar_phi(a, b):
    return add(scale(ONE, a), scale(PHI, b))


def ordinary_shadow_pair(a, b):
    halfdiff = div_exact(sub(a, b), 2)
    if halfdiff is None:
        return a, b, False
    center = div_exact(add(a, b), 2)
    require(center is not None, "shadow center integrality")
    rotated = mul(RHO, halfdiff)
    return add(center, rotated), sub(center, rotated), True


def empty_counts():
    return {"attempts": 0, "admissions": 0, "diagonal": 0,
            "changes": 0, "field_changes": 0}


TOTAL = empty_counts()
TOTAL_CUTS = 0
CATEGORY_TOTALS = {}


class Carrier:
    def __init__(self, actual, case):
        self.case = case
        self.v = list(actual)
        self.f = neg(actual[0])
        self.e = [ZERO for unused in actual[1:]]
        self.shadow = list(actual)
        self.shadow_f = self.f
        self.initial = self.snapshot()
        self.initial_residues = [residue(a) for a in actual] + [residue(self.f)]
        self.H, self.E = self.account()
        self.cut = 0
        self.counts = {}
        self.areas = {}
        self.audit("initial")

    def snapshot(self):
        return (tuple(self.v), self.f)

    def account(self):
        # Include every fixed, uncharged reference and difference explicitly.
        terms = [self.v[0], self.f]
        for a, ref in zip(self.v[1:], self.e):
            terms.extend((a, ref, sub(a, ref)))
        return ring_sum(h(a) for a in terms), sum(q(a) for a in terms)

    def audit(self, label):
        global TOTAL_CUTS
        CONTEXT.update(case=self.case, cut=self.cut, boundary=label)
        require(all(type(z) is int for a in self.v + [self.f] + self.e for z in a),
                "integral coefficients")
        require(all(len(a) == 5 and min(a) == 0 for a in self.v + [self.f] + self.e),
                "cyclic quotient normalization")
        require(all(ref == ZERO for ref in self.e), "fixed references")
        require(ring_sum(self.v) == ZERO, "exact total charge")
        require(add(self.v[0], self.f) == ZERO, "Gauss vertex A")
        require(sub(ring_sum(self.v[1:]), self.f) == ZERO, "Gauss vertex B")
        H, E = self.account()
        require(H == self.H, "full H account", four(H), four(self.H))
        require(E == self.E, "full E account", E, self.E)
        require(E == 2 * sum(q(a) for a in self.v), "loaded-account identity")
        require(trace(H) == 2 * E, "account trace")
        residues = [residue(a) for a in self.v] + [residue(self.f)]
        require(residues == self.initial_residues, "slot and field residues",
                residues, self.initial_residues)
        require(self.v == self.shadow and self.f == self.shadow_f,
                "ordinary shadow with current field")
        TOTAL_CUTS += 1

    def step(self, pair, category):
        i, k = pair
        require(i != k and 0 <= i < len(self.v) and 0 <= k < len(self.v),
                "valid physical pair", pair)
        before = self.snapshot()
        old_x = self.v[0]
        a, b = self.v[i], self.v[k]
        t = div_exact(sub(a, b), 2)
        if i == 0 or k == 0:
            other = k if i == 0 else i
            x, v, e = self.v[0], self.v[other], self.e[other - 1]
            numerator = add(sub(sub(scale(v, 2), x), e), self.f)
            d = div_exact(numerator, 4)
            admitted = d is not None
            if admitted:
                current = mul(RHOM1, d)
                self.v[0] = sub(x, current)
                self.v[other] = add(v, current)
                self.f = add(self.f, current)
        else:
            admitted = t is not None
            if admitted:
                transfer = mul(RHOM1, t)
                self.v[i] = add(a, transfer)
                self.v[k] = sub(b, transfer)
        require(admitted == (t is not None), "loaded admission equals ordinary")
        sa, sb, shadow_admitted = ordinary_shadow_pair(self.shadow[i], self.shadow[k])
        shadow_x_before = self.shadow[0]
        self.shadow[i], self.shadow[k] = sa, sb
        self.shadow_f = add(self.shadow_f, sub(shadow_x_before, self.shadow[0]))
        require(admitted == shadow_admitted, "shadow admission")
        require(self.f == add(before[1], sub(old_x, self.v[0])), "actual current update")
        record = {"attempts": 1, "admissions": int(admitted),
                  "diagonal": int(admitted and t == ZERO),
                  "changes": int(self.snapshot() != before),
                  "field_changes": int(self.f != before[1])}
        counts = self.counts.setdefault(category, empty_counts())
        totals = CATEGORY_TOTALS.setdefault(category, empty_counts())
        for key, value in record.items():
            counts[key] += value
            totals[key] += value
            TOTAL[key] += value
        contribution = h(t) if admitted else ZERO
        self.areas[category] = add(self.areas.get(category, ZERO), contribution)
        self.cut += 1
        self.audit(category)
        return admitted


def invert(carrier, word, snapshots, category):
    require(len(snapshots) == len(word) + 1, "inverse snapshot lengths")
    for pos in range(len(word) - 1, -1, -1):
        for repeat in range(4):
            carrier.step(word[pos], category)
        require(carrier.snapshot() == snapshots[pos], "literal inverse primitive block",
                {"forward_position": pos})
    require(carrier.snapshot() == carrier.initial, "complete inverse resource return")


def p_word(i, k):
    A = [(2 * i, 2 * i + 1)]
    K = [(2 * i, 2 * k + 1), (2 * i + 1, 2 * k)]
    out = list(A)
    for exponent in range(1, 5):
        out.extend(K * exponent)
        out.extend(A)
    require(len(out) == 25, "P length", len(out), 25)
    return out


def phase_pair(a, b):
    require(b == neg(a), "phase pair opposition", [four(a), four(b)])
    require(a in ROOTS, "root phase", four(a))
    return ROOTS.index(a)


def experiment_a():
    writer = p_word(0, 1) * 2 + p_word(0, 2) * 2 + p_word(1, 2) * 2
    reader = [(2, 6), (2, 3)] * 5
    require(len(writer) == 150 and len(reader) == 10, "A word lengths")
    stock = from_four((3, 4, 2, 0))
    expected_stock = [(3, 4, 2, 0), (2, 3, 3, 1), (1, 1, 1, 1),
                      (1, 0, -1, -1), (3, 2, 0, -1)]
    expected_Q = [32, 17, 2, 7, 27]
    expected_memory_Q = [4, 19, 34, 29, 9]
    rows = []
    positive = 0
    positive_blank = 0
    preparations = {}
    for r in range(5):
        for s in range(5):
            for t in range(5):
                v = [ROOTS[r], neg(ROOTS[r]), ROOTS[s], neg(ROOTS[s]),
                     ROOTS[t], neg(ROOTS[t]), stock, neg(stock)]
                trial = Carrier(v, "A:%d,%d,%d" % (r, s, t))
                require(trial.E == 152, "A initial E", trial.E, 152)
                require(trial.H == scalar_phi(48, 56), "A initial H", four(trial.H))
                snapshots = [trial.snapshot()]
                for contact in writer:
                    trial.step(contact, "A_writer")
                    snapshots.append(trial.snapshot())
                phases = [phase_pair(trial.v[2 * n], trial.v[2 * n + 1]) for n in range(3)]
                predicted = [(r + 3 * s + 2 * t) % 5,
                             (r + 4 * s + t) % 5, (2 * s + 4 * t) % 5]
                require(phases == predicted, "A writer phase matrix", phases, predicted)
                writer_state = trial.snapshot()
                writer_field_return = trial.f == trial.initial[1]
                if t == s:
                    positive += 1
                    require(trial.v[:2] == v[:2] and trial.v[4:6] == v[4:6],
                            "positive source and reference writer return")
                    require(writer_field_return, "positive writer field return")
                    prepared = tuple(v[2:])
                    if s in preparations:
                        require(preparations[s] == prepared, "common positive preparation")
                    else:
                        preparations[s] = prepared
                    positive_blank += int(trial.v[2:4] == v[2:4])
                for contact in reader:
                    trial.step(contact, "A_reader")
                    snapshots.append(trial.snapshot())
                    require(trial.v[:2] == list(writer_state[0][:2]) and
                            trial.v[4:6] == list(writer_state[0][4:6]),
                            "reader leaves source and reference unchanged")
                    require(trial.f == writer_state[1], "reader field unchanged")
                b = phases[1]
                require(four(trial.v[6]) == list(expected_stock[b]), "A stock state",
                        four(trial.v[6]), expected_stock[b])
                stock_q = q(trial.v[6])
                memory_q = q(trial.v[2]) + q(trial.v[3])
                require(stock_q == expected_Q[b], "A stock Q", stock_q, expected_Q[b])
                require(memory_q == expected_memory_Q[b], "A memory Q", memory_q,
                        expected_memory_Q[b])
                admissions = trial.counts["A_reader"]["admissions"]
                require(admissions == (6 if b == 0 else 5), "A reader admissions",
                        admissions, 6 if b == 0 else 5)
                require(trial.counts["A_reader"]["diagonal"] == 0, "A reader diagonals")
                require(trial.counts["A_reader"]["field_changes"] == 0, "A reader field count")
                if t == s:
                    require(trial.v[2:4] != v[2:4], "positive final memory disturbed")
                rows.append({"input": [r, s, t], "writer_phases": phases,
                             "stock_out": four(trial.v[6]), "stock_Q": stock_q,
                             "memory_Q": memory_q, "reader_admissions": admissions,
                             "field_return": trial.f == trial.initial[1],
                             "writer_field_return": writer_field_return})
                invert(trial, writer + reader, snapshots, "A_inverse")
                require(trial.cut == 800, "A all attempt count", trial.cut, 800)
    require(positive == 25 and positive_blank == 5, "positive family counts",
            [positive, positive_blank], [25, 5])
    return rows, {"triples": len(rows), "positive_triples": positive,
                  "positive_unchanged_blank_before_reading": positive_blank,
                  "attempts_per_triple": 800}


def source_words():
    tokens27 = "12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 36 36 36 36 16 12 12 46 45 45 45 45".split()
    tokens27 += ["13"] * 8
    tokens35 = ["12"] * 5 + (["35"] + ["36"] * 5 + ["35"] * 4) * 3
    convert = lambda tokens: [(int(token[0]) - 1, int(token[1]) - 1) for token in tokens]
    return {"P27": convert(tokens27), "P35": convert(tokens35)}


def source_only_prefixes(initial, word):
    values = list(initial[:6])
    prefixes = [tuple(values)]
    for i, k in word:
        values[i], values[k], unused = ordinary_shadow_pair(values[i], values[k])
        prefixes.append(tuple(values))
    return prefixes


def experiment_b():
    B = sub(ONE, RHO)
    u = sub(ONE, ROOT)
    X = sub(add(ONE, ROOT), scale(ROOTS[3], 2))
    I1 = [B, neg(B), u, u, X, scale(ONE, 2)]
    S = ring_sum(I1)
    require(S == from_four((5, -1, 0, -2)), "B source sum fixture", four(S))
    selectors = []
    for a in [B, mul(B, ROOTS[3])]:  # rho^4 = j^3
        c = mul(a, JINV)
        helper = add(a, scale(c, 2))
        delta = mul(sub(ONE, RHO), c)
        selectors.append((a, c, helper, delta))
    a0, c0, helper0, delta0 = selectors[0]
    require(four(c0) == [-1, -2, -2, 0], "c0 fixture", four(c0))
    require(four(helper0) == [-1, -4, -5, 0], "h0 fixture", four(helper0))
    require(h(c0) == scalar_phi(3, 4), "h(c0) fixture")
    require(h(helper0) == scalar_phi(18, 19) and q(helper0) == 55, "helper metric fixture")
    require(h(delta0) == scalar_phi(10, 15) and q(delta0) == 35, "delta metric fixture")
    require(selectors[1][3] == mul(ROOTS[3], delta0), "delta1 fixture")
    initial = I1 + [neg(S)]
    for unused_a, unused_c, helper, unused_d in selectors:
        initial.extend((helper, ZERO, neg(helper)))
    port = [(0, 7), (0, 8), (0, 10), (0, 11)]
    rows = []
    for path, word in source_words().items():
        require(len(word) == 35, "source word length")
        prefixes = source_only_prefixes(initial, word)
        require(prefixes[-1] == tuple(I1), "source-only endpoint")
        expected_x_at_five = selectors[1 if path == "P27" else 0][0]
        require(prefixes[5][0] == expected_x_at_five, "source port-prefix x fixture")
        for timing in ["immediate", "omitted", "delayed"]:
            trial = Carrier(initial, "B:%s:%s" % (path, timing))
            require(trial.E == 672, "B complete E", trial.E, 672)
            forward = []
            snapshots = [trial.snapshot()]
            retained_archive = None
            def run_port():
                nonlocal retained_archive
                before_source = tuple(trial.v[:6])
                before_field = trial.f
                before_count = trial.counts.get("B_port", empty_counts())["admissions"]
                for pair in port:
                    trial.step(pair, "B_port")
                    forward.append(pair)
                    snapshots.append(trial.snapshot())
                require(tuple(trial.v[:6]) == before_source and trial.f == before_field,
                        "port complete source and field nondisturbance")
                require(trial.counts["B_port"]["admissions"] - before_count == 2,
                        "exactly one selector admitted twice")
                retained_archive = tuple(trial.v[7:])
            for index, pair in enumerate(word, 1):
                admitted = trial.step(pair, "B_source")
                if path == "P27" and index > 27:
                    require(not admitted, "P27 padding refusal")
                forward.append(pair)
                snapshots.append(trial.snapshot())
                require(tuple(trial.v[:6]) == prefixes[index], "source prefix nondisturbance",
                        {"source_counter": index})
                if retained_archive is not None:
                    require(tuple(trial.v[7:]) == retained_archive, "retained archive at source cut",
                            {"source_counter": index})
                if timing == "immediate" and index == 5:
                    require(trial.v[0] == expected_x_at_five, "actual source at port")
                    run_port()
                    require(tuple(trial.v[:6]) == prefixes[index], "post-port source prefix")
            if timing == "delayed":
                run_port()
                require(tuple(trial.v[:6]) == prefixes[35], "delayed post-port source prefix")
            require(trial.v[:7] == initial[:7], "B original source and neutral return")
            require(trial.f == trial.initial[1], "B field return")
            selected = None if timing == "omitted" else (1 if timing == "immediate" and path == "P27" else 0)
            predicted_archive = list(initial[7:])
            if selected is not None:
                a, unused_c, helper, delta = selectors[selected]
                predicted_archive[3 * selected:3 * selected + 3] = [scale(a, 2), delta, neg(helper)]
            require(trial.v[7:] == predicted_archive, "B complete current archive states",
                    [four(a) for a in trial.v[7:]], [four(a) for a in predicted_archive])
            record_qs = [q(trial.v[8]), q(trial.v[11])]
            expected_qs = [0, 0] if selected is None else ([35, 0] if selected == 0 else [0, 35])
            require(record_qs == expected_qs, "B current norm records", record_qs, expected_qs)
            source_area = trial.areas["B_source"]
            port_area = trial.areas.get("B_port", ZERO)
            full_area = add(source_area, port_area)
            require(source_area == scalar_phi(55, 20), "B source area", four(source_area))
            require(port_area == (ZERO if selected is None else scalar_phi(6, 8)),
                    "B port area", four(port_area))
            require(full_area == (scalar_phi(55, 20) if selected is None else scalar_phi(61, 28)),
                    "B full path area", four(full_area))
            if selected is not None:
                require(trace(full_area) == 150, "B total area trace", trace(full_area), 150)
                require(scale(full_area, 2) == scalar_phi(122, 56), "B doubled area")
            source_counts = trial.counts["B_source"].copy()
            port_counts = trial.counts.get("B_port", empty_counts()).copy()
            expected_source_admissions = 27 if path == "P27" else 35
            require(source_counts["admissions"] == expected_source_admissions, "B source admissions")
            require(source_counts["diagonal"] == 0 and port_counts["diagonal"] == 0,
                    "B forward no diagonal admissions")
            forward_admissions = source_counts["admissions"] + port_counts["admissions"]
            require(forward_admissions == expected_source_admissions + (0 if selected is None else 2),
                    "B combined admissions")
            source_det_exp = 2 * source_counts["admissions"] % 5
            combined_det_exp = 2 * forward_admissions % 5
            require(source_det_exp == (4 if path == "P27" else 0), "B source determinant")
            expected_combined = source_det_exp if selected is None else (3 if path == "P27" else 4)
            require(combined_det_exp == expected_combined, "B combined determinant")
            row = {"path": path, "timing": timing,
                   "source_final": [four(a) for a in trial.v[:7]],
                   "archive_final": [four(a) for a in trial.v[7:]],
                   "field_final": four(trial.f), "record_Q": record_qs,
                   "E": trial.E, "H_account": four(trial.H),
                   "H_source": four(source_area), "H_port": four(port_area),
                   "H_path": four(full_area), "two_H_path": four(scale(full_area, 2)),
                   "source_det_j_exponent": source_det_exp,
                   "combined_det_j_exponent": combined_det_exp,
                   "source_counts": source_counts, "port_counts": port_counts}
            forward_length = len(forward)
            require(forward_length == (35 if timing == "omitted" else 39), "B forward length")
            invert(trial, forward, snapshots, "B_inverse")
            require(trial.counts["B_inverse"]["diagonal"] == 0, "B inverse no diagonals")
            require(trial.cut == 5 * forward_length, "B all attempt count")
            row["inverse_counts"] = trial.counts["B_inverse"].copy()
            rows.append(row)
    require(len(rows) == 6, "B control count")
    return rows


def main():
    require(mul(J, JINV) == ONE, "ring J inverse")
    require(mul(J, PHI) == ROOT, "ring anchor")
    A, a_summary = experiment_a()
    B = experiment_b()
    require(TOTAL["attempts"] == 101130, "combined attempt total", TOTAL["attempts"], 101130)
    require(TOTAL_CUTS == 101261, "combined audited cuts", TOTAL_CUTS, 101261)
    output = {"status": "PASS", "evidence_status": "candidate-C", "layer": "L1",
              "authority": "NON-CANONICAL", "arithmetic": "exact cyclic Z5 coefficients modulo common shift",
              "architecture_scope": "one local architecture", "A": A, "B": B,
              "summary": {"A": a_summary, "B_runs": len(B), "counts": TOTAL,
                          "cuts_checked": TOTAL_CUTS, "category_counts": CATEGORY_TOTALS}}
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except AuditFailure as error:
        print(json.dumps({"status": "FAIL", "first_failure": json.loads(str(error))},
                         sort_keys=True, separators=(",", ":")))
        print("Independent frozen checker stopped at first failure.", file=sys.stderr)
        sys.exit(1)
