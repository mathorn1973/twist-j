#!/usr/bin/env python3
"""Mutation harness for verify_record_quotient.py (NON-CANONICAL note).

Why this file exists. Three successive revisions of this note's verifier
shipped gates that could not fail: a hardcoded True, a comparison of a
quantity with itself, and a cardinality standing in for a structure claim.
A source scan for literal constants cannot see any of those, because they
are construction-true rather than literal. The only mechanical test of
"this gate actually tests something" is to break the thing the gate claims
to test and require the gate to notice.

Contract enforced here:
  1. Every mutation must KILL at least one gate. A mutation that leaves the
     verifier fully green is a proven tautology in the gates it targets.
  2. Every mutation must kill the gates it TARGETS, not merely some gate.
  3. Every gate of the verifier must be killed by at least one mutation.
     An uncovered gate is where the next tautology hides, so uncovered
     gates fail this harness.
  4. A deliberately tautological gate injected into a scratch copy must be
     reported as uncovered, which is the harness's own self-test.

Exit 0 only when all four hold. Standard library only, no file writes.

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
        python3 mutation_test.py
"""

import io
import os
import subprocess
import sys

TARGET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "verify_record_quotient.py")

# (id, what is broken, exact old snippet, replacement, gates that must fail)
MUTATIONS = [
    ("M01", "cyclotomic reduction doubles the carried term",
     "                c[j] -= t", "                c[j] -= 2 * t",
     ["W1"]),
    ("M02", "hand expansion of (1+z)(1+z^2) is falsified",
     "== (1, 1, 1, 1),", "== (1, 1, 1, 0),",
     ["W2"]),
    ("M03", "coset reduction becomes a no-op",
     "def ired(v, H):\n    v = list(v)",
     "def ired(v, H):\n    return tuple(v)\n    v = list(v)",
     ["W3"]),
    ("M04", "the HNF box is enlarged by one cell per coordinate",
     "range(H[i][i]) for i in range(4)", "range(H[i][i] + 1) for i in range(4)",
     ["W3"]),
    ("M05", "the lattice determinant drops a diagonal factor",
     "return H[0][0] * H[1][1] * H[2][2] * H[3][3]",
     "return H[0][0] * H[1][1] * H[2][2]",
     ["W4"]),
    ("M06", "prime factors are counted with multiplicity again (the p = 5 "
            "defect this file was fixed for)",
     "return sorted(set(facs))", "return sorted(facs)",
     ["F1", "R1b"]),
    ("M07", "ramification: lambda^4 is compared against the wrong power",
     "and ipow(P5[0].ideal, 4) == ideal([(5, 0, 0, 0)])",
     "and ipow(P5[0].ideal, 3) == ideal([(5, 0, 0, 0)])",
     ["F1"]),
    ("M08", "the inertia route uses the wrong congruence",
     "if pow(p, k, 5) == 1) == 4", "if pow(p, k, 5) == 4) == 4",
     ["F2"]),
    ("M09", "the fifth-root search is replaced by a fourth-power search",
     "if pow(r, 5, 11) == 1)", "if pow(r, 4, 11) == 1)",
     ["F3"]),
    ("M10", "residue reduction skips the polynomial remainder",
     "    def reduce(self, a):\n        num = [x % self.p for x in a]",
     "    def reduce(self, a):\n        return tuple(x % self.p for x in a)"
     "\n        num = [x % self.p for x in a]",
     ["F4", "F5"]),
    ("M11", "multiplication in kappa(P) becomes addition",
     "cc[i + j] = (cc[i + j] + x * y) % P.p",
     "cc[i + j] = (cc[i + j] + x + y) % P.p",
     ["F5"]),
    ("M12", "the support label inverts: e is recorded where it is 0",
     "if P.reduce(e) == P.reduce(ONE)) for e in idm})",
     "if P.reduce(e) != P.reduce(ONE)) for e in idm})",
     # not R1a: complementing every label is still a bijection onto the power
     # set, so R1a cannot see this; R1c and R1d can.
     ["R1c", "R1d"]),
    ("M13", "idempotence is tested before reduction into the quotient",
     "return [e for e in cells(I) if ired(rmul(e, e), I) == e]",
     "return [e for e in cells(I) if rmul(e, e) == e]",
     ["R1b"]),
    ("M14", "support containment is tested in the wrong direction",
     "return [P for P in CAND_PRIMES if isub(I, P.ideal)]",
     "return [P for P in CAND_PRIMES if isub(P.ideal, I)]",
     ["R1a", "R1b"]),
    ("M15", "the Boolean join drops its correction term",
     "sig[ired(rsub(radd(a, b), rmul(a, b)), I)]", "sig[ired(radd(a, b), I)]",
     ["R1c"]),
    ("M16", "atoms are selected by the wrong support size",
     "at = [e for e in idm if len(sig[e]) == 1]",
     "at = [e for e in idm if len(sig[e]) <= 1]",
     ["R1d"]),
    ("M17", "the split prime 11 is dropped from the candidate primes",
     "for p in (2, 3, 5, 11) for P in primes_above(p)]",
     "for p in (2, 3, 5) for P in primes_above(p)]",
     ["R1e"]),
    ("M18", "the radical keeps only the first prime of the support",
     "    for P in sup:\n        r = imul(r, P.ideal)",
     "    for P in sup[:1]:\n        r = imul(r, P.ideal)",
     ["L5"]),
    ("M19", "(4) is built as (2), so thickness becomes invisible to the "
            "ideal too",
     '("(4)", ipow(P2[0].ideal, 2))', '("(4)", ipow(P2[0].ideal, 1))',
     ["R2b"]),
    ("M20", "R/(5) is replaced by R/lambda, which IS a field",
     '("(5)", ideal([(5, 0, 0, 0)]))', '("(5)", ideal([LAM]))',
     ["R2c"]),
    ("M21", "the Loewy chain starts at n^1 (the wrong convention)",
     "        Lk = isum(ipow(rad, k), I)", "        Lk = isum(ipow(rad, k + 1), I)",
     ["L1", "L4", "L5", "N3"]),
    ("M22", "one residue-field norm is off by one in the product formula",
     "                pr *= P.norm", "                pr *= P.norm + 1",
     ["L1", "L3"]),
    ("M23", "the valuation is truncated at 1",
     "        if k > 12:", "        if k > 1:",
     ["L2"]),
    ("M24", "well-definedness is tested on 1 instead of on the ideal",
     "if any(ired(rmul(g, t), I2) != ZERO for g in I1):",
     "if any(ired(rmul(g, t), I2) != ZERO for g in [ONE]):",
     ["H1"]),
    ("M25", "unitality is imposed INSIDE the enumeration (the exact defect "
            "that survived the previous revision)",
     "            if ired(rmul(t, t), I2) == t:",
     "            if ired(rmul(t, t), I2) == t and t == ired(ONE, I2):",
     ["H2"]),
    ("M26", "unitality is never applied, so the map need not be reduction",
     "hom_un[(l1, l2)] = [t for t in cand if t == ired(ONE, I2)]",
     "hom_un[(l1, l2)] = list(cand)",
     ["H2", "H3"]),
    ("M27", "strictness is inverted, so identity pairs enter the section test",
     "if isub(DATA[a][0], DATA[b][0]) and DATA[a][0] != DATA[b][0]]",
     "if isub(DATA[a][0], DATA[b][0]) and DATA[a][0] == DATA[b][0]]",
     ["H5"]),
    ("M28", "the idempotent characterisation of Hom is weakened to 'some "
            "generator kills t'",
     "                if all(ired(rmul(g, t), DATA[b][0]) == ZERO",
     "                if any(ired(rmul(g, t), DATA[b][0]) == ZERO",
     ["H6"]),
    ("M29", "every I_L collapses to I_1, so the family stops growing",
     "    I = imul(ipow(ideal([LAM]), L), P2[0].ideal)",
     "    I = imul(ipow(ideal([LAM]), 1), P2[0].ideal)",
     ["N2", "N3", "N4"]),
    ("M30", "the second prime is dropped from I_L, changing the support",
     "    I = imul(ipow(ideal([LAM]), L), P2[0].ideal)",
     "    I = imul(ipow(ideal([LAM]), L), ideal([(3, 0, 0, 0)]))",
     ["N1", "N2"]),
    ("M31", "the multiplicativity filter is removed from the Hom enumeration",
     "            if ired(rmul(t, t), I2) == t:", "            if True:",
     # H2 only bounds the counts from above and below; H6 is the gate that
     # pins the multiplicative maps to the idempotents.
     ["H6"]),
]


TIMEOUT = 60


def run_source(src):
    """Run a verifier source in a child interpreter.

    Returns (outcome, failing_gate_ids, all_gate_ids) where outcome is
    "clean" (the program ran and reported gates), "exception", or "timeout".
    A mutation detected only as an exception or a timeout still counts as
    detected, but it attributes coverage to no particular gate, so the
    coverage requirement below is not satisfied by it.
    """
    try:
        proc = subprocess.run(
            [sys.executable, "-"], input=src.encode("utf-8"),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "timeout", [], []
    out = proc.stdout.decode("utf-8", "replace")
    failing, all_ids = [], []
    for line in out.split("\n"):
        parts = line.split()
        if len(parts) >= 2 and parts[0][:1] in "WFRLHNX" and len(parts[0]) <= 4:
            if line.rstrip().endswith("OK") or " OK " in line:
                all_ids.append(parts[0])
            elif line.rstrip().endswith("FAIL") or " FAIL " in line:
                all_ids.append(parts[0])
                failing.append(parts[0])
    if "GATE COUNT:" not in out or proc.returncode not in (0, 1):
        # the verifier prints GATE COUNT unconditionally, so its absence means
        # the mutant died before finishing: detected, but attributing to no gate
        return "exception", failing, all_ids
    return "clean", failing, all_ids


with io.open(TARGET, encoding="utf-8") as fh:
    BASE = fh.read()

print("Mutation harness for verify_record_quotient.py")
print("contract: every mutation kills its targets; every gate is covered")
print("")

base_out, base_fail, base_gates = run_source(BASE)
print("baseline: %s, %d gates, %d failing"
      % (base_out, len(base_gates), len(base_fail)))
if base_out != "clean" or base_fail:
    print("RESULT: FAIL -- the unmutated verifier is not green")
    raise SystemExit(1)
print("")

problems = []
covered = set()
for mid, what, old, new, targets in MUTATIONS:
    if BASE.count(old) < 1:
        print("%-4s SNIPPET-NOT-FOUND   %s" % (mid, what))
        problems.append("%s: snippet not found in the verifier" % mid)
        continue
    outcome, failing, _ = run_source(BASE.replace(old, new, 1))
    killed = set(failing)
    if outcome == "clean":
        covered |= killed
    missed = [t for t in targets if t not in killed]
    if outcome == "timeout":
        tag, extra = "diverged", "no gate attribution"
    elif outcome == "exception":
        tag, extra = "crashed", "no gate attribution"
    elif not killed:
        tag, extra = "SURVIVED", "nothing failed -- the targets are untested"
        problems.append("%s SURVIVED: %s" % (mid, what))
    elif missed:
        tag, extra = "MISTARGETED", ("killed %s but MISSED %s"
                                     % (",".join(sorted(killed)),
                                        ",".join(missed)))
        problems.append("%s missed its targets %s" % (mid, missed))
    else:
        tag, extra = "killed", ",".join(sorted(killed))
    print("%-4s %-12s %s" % (mid, tag, what))
    print("     -> %s" % extra)

print("")
uncovered = [g for g in base_gates if g not in covered]
print("coverage: %d of %d gates are killed by at least one mutation with a "
      "clean gate attribution" % (len(base_gates) - len(uncovered),
                                  len(base_gates)))
if uncovered:
    print("UNCOVERED: %s" % ", ".join(uncovered))
    problems.append("uncovered gates: %s" % ", ".join(uncovered))

# self-test: a deliberately tautological gate must show up as uncovered
print("")
INJECT = ('gate("X1  deliberate tautology (harness self-test)", 1 == 1,\n'
          '     "must be reported UNCOVERED")\n'
          'print("")\n_bad = [g for g, ok in GATES if not ok]')
scratch = BASE.replace('print("")\n_bad = [g for g, ok in GATES if not ok]',
                       INJECT, 1)
s_out, s_fail, s_gates = run_source(scratch)
s_cov = set()
for mid, what, old, new, targets in MUTATIONS:
    if scratch.count(old) < 1:
        continue
    _c, f, _a = run_source(scratch.replace(old, new, 1))
    s_cov |= set(f)
selftest_ok = ("X1" in s_gates) and ("X1" not in s_cov)
print("self-test: injected tautological gate X1 present=%s, killed by any "
      "mutation=%s" % ("X1" in s_gates, "X1" in s_cov))
if not selftest_ok:
    problems.append("self-test failed: the harness did not flag a "
                    "deliberately tautological gate")
else:
    print("self-test PASS: the harness reports X1 as uncovered, so an "
          "untestable gate cannot pass unnoticed")

print("")
if problems:
    print("RESULT: FAIL (%d)" % len(problems))
    for p in problems:
        print("  %s" % p)
    raise SystemExit(1)
print("RESULT: %d mutations, all killed their targets; %d of %d gates "
      "covered; self-test passed"
      % (len(MUTATIONS), len(base_gates), len(base_gates)))
raise SystemExit(0)
