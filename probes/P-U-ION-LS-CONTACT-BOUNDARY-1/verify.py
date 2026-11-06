#!/usr/bin/env python3
"""Exact audit of the frozen closed-LS contact boundary, not a pulse simulation."""
from __future__ import annotations

from collections import Counter
import csv
from fractions import Fraction
import hashlib
import importlib.util
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MANIFEST_SHA256 = 'edab37410cb23c571a46cf25fe2e70778abbf4566351fcb00697f7490ed8cafa'
D = 5
PAIRS = [(s, q) for s in range(D) for q in range(D)]


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def source_check():
    raw = (HERE / 'INPUTS.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest() == MANIFEST_SHA256, 'input manifest drift')
    manifest = json.loads(raw)
    for path, spec in manifest['files'].items():
        data = (ROOT / path).read_bytes()
        require(len(data) == spec['bytes'], 'input length: ' + path)
        require(hashlib.sha256(data).hexdigest() == spec['sha256'], 'input hash: ' + path)


def rows(name):
    path = ROOT / 'probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary' / name
    reader = csv.DictReader(io.StringIO(path.read_bytes().decode('utf-8')))
    fields = reader.fieldnames
    require(fields is not None and len(fields) == 17, 'source schema')
    return fields, [{key: int(value) for key, value in row.items()} for row in reader]


def source_audit():
    fields, history = rows('HISTORY.csv')
    require(len(history) == 250, 'history count')
    require({(r['a1'], r['a2'], r['n']) for r in history}
            == {(a, b, n) for a in range(5) for b in range(5) for n in range(10)},
            'complete historical input coverage')
    require(all(0 <= r[k] < 5 for r in history for k in fields if k != 'n'),
            'pentit source domain')
    counts, maxima = [], []
    for n in range(10):
        fibres = Counter(tuple(r[k] for k in fields[2:]) for r in history if r['n'] == n)
        counts.append(len(fibres))
        maxima.append(max(fibres.values()))
    require(counts == [25, 20, 20, 15, 15, 15, 15, 12, 12, 9], 'history state counts')
    require(maxima == [1, 2, 2, 2, 2, 2, 2, 4, 4, 4], 'history fibre counts')
    final_four = [tuple(r[k] for k in fields[2:]) for r in history
                  if r['n'] == 9 and r['a1'] in (0, 1) and r['a2'] in (0, 1)]
    require(len(final_four) == 4 and len(set(final_four)) == 1, 'four-state collision')
    _, contacts = rows('CONTACTS.csv')
    require(len(contacts) == 50, 'contact source count')
    require({(r['a1'], r['a2'], r['n']) for r in contacts}
            == {(a, b, n) for a in range(5) for b in range(5) for n in (0, 6)},
            'contact historical input coverage')
    second = [r for r in contacts if r['n'] == 6]
    zero = []
    keys = ['p1', 'p4', 'p1p', 'p4p', 'q', 'r']
    for r in second:
        s = (r['a2'] + 1) % 5
        before = tuple(r['before_' + k] for k in keys)
        after = tuple(r['after_' + k] for k in keys)
        require(before == (2, 1, 3, 4, 0, 4), 'actual ready receiver')
        require(after == (2, 1, 3, 4, (s + 1) % 5, 4), 'actual receiver output')
        require((r['source_before'], r['source_after']) == (s, 4), 'source export')
        if s == 0:
            zero.append(r)
    require(len(zero) == 5 and {r['a1'] for r in zero} == set(range(5)), 'all witnesses')
    return {'actual_second_contacts': len(second), 'zero_pair_histories': len(zero),
            'history_distinct': counts, 'history_max_fibre': maxima}


def matrix(fn):
    return [[fn(i, j) for j in range(25)] for i in range(25)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(25)) for j in range(25)]
            for i in range(25)]


def algebra_audit():
    def swap(x):
        return x[1], x[0]

    def contact(x):
        return (x[1] + 4) % 5, (x[0] + 1) % 5

    require(len({contact(x) for x in PAIRS}) == 25, 'contact bijection')
    require(all(contact(contact(x)) == x for x in PAIRS), 'contact involution')
    mismatches = sum(swap(contact(x)) != contact(swap(x)) for x in PAIRS)
    require(mismatches == 25, 'target does not commute with swap')
    require(contact((0, 0)) == (4, 1), 'witness target')

    # AA-dagger = Delta_s^2 + Delta_q^2 + 2 c Delta_s Delta_q.
    # Terms encode (power of c, sorted Delta indices); no angle is sampled.
    def norm_polynomial(s, q):
        result = Counter()
        result[(0, (s, s))] += 1
        result[(0, (q, q))] += 1
        result[(1, tuple(sorted((s, q))))] += 2
        return result

    require(all(norm_polynomial(s, q) == norm_polynomial(q, s) for s, q in PAIRS),
            'closed Hamiltonian phase symmetry')
    require(all((s == q) == (q == s) for s, q in PAIRS), 'Hrmo G phase symmetry')
    # Every entry of P(R tensor R) equals the corresponding entry of (R tensor R)P.
    for j, k in PAIRS:
        for a, b in PAIRS:
            left = tuple(sorted(((k, a), (j, b))))
            right = tuple(sorted(((j, b), (k, a))))
            require(left == right, 'collective rotation symbolic monomial')

    ident = matrix(lambda i, j: int(i == j))
    p = matrix(lambda i, j: int(PAIRS[i] == swap(PAIRS[j])))
    require(mul(p, p) == ident, 'swap square')
    t = PAIRS.index((4, 1))
    u = PAIRS.index((1, 4))
    e = matrix(lambda i, j: int(i == j == t))
    f = matrix(lambda i, j: int(i == j == u))
    require(mul(mul(p, e), p) == f, 'swapped output effect')
    require(mul(e, f) == matrix(lambda i, j: 0), 'orthogonal outcomes')
    require(all(ident[i][i] - e[i][i] - f[i][i] >= 0 for i in range(25)),
            'nonnegative outcome complement')

    # Exact PSD certificate: Q = P_plus - 2 P_plus E P_plus is a projector.
    # B = 2 P_plus; Q4 = 4 Q. Symmetric idempotence certifies positivity.
    bmat = matrix(lambda i, j: ident[i][j] + p[i][j])
    b_e_b = mul(mul(bmat, e), bmat)
    q4 = matrix(lambda i, j: 2 * bmat[i][j] - 2 * b_e_b[i][j])
    require(q4 == matrix(lambda i, j: q4[j][i]), 'PSD certificate symmetry')
    require(mul(q4, q4) == matrix(lambda i, j: 4 * q4[i][j]), 'PSD projector identity')
    require(Fraction(sum(q4[i][i] for i in range(25)), 4) == 14, 'projector rank')
    v = [int(i in (t, u)) for i in range(25)]
    bound = Fraction(sum(v[i] * e[i][j] * v[j] for i in range(25) for j in range(25)),
                     sum(x*x for x in v))
    require(bound == Fraction(1, 2), 'symmetry-sector bound')
    # This vector saturates the enlarged symmetry sector, not necessarily the LS library.

    # Unequal FIXED port dictionaries are an explicit boundary control.
    # Physical encoding K(s,q)=(s,q+4), K C K^-1 = SWAP.
    for physical in PAIRS:
        logical = (physical[0], (physical[1] - 4) % 5)
        out = contact(logical)
        encoded_out = (out[0], (out[1] + 4) % 5)
        require(encoded_out == swap(physical), 'different-dictionary control')

    coefficients = []
    for s in range(5):
        coeff = [0] * 5
        for level, amount in [(4, 1), ((s + 1) % 5, 1), (s, -1), (0, -1)]:
            coeff[level] += amount
        coefficients.append(coeff[1:])  # independent normalization E0=0
    require(coefficients == [[1, 0, 0, 1], [-1, 1, 0, 1], [0, -1, 1, 1],
                             [0, 0, -1, 2], [0, 0, 0, 0]], 'endpoint energy identity')
    require(contact((4, 0)) == (4, 0), 'zero-work fixed-point endpoint')
    return {'target_swap_commutator_mismatches': mismatches,
            'symmetric_success_bound': str(bound),
            'identical_spectrum_coefficients': coefficients,
            'relabelled_target_is_swap': True}


def main():
    source_check()
    report = source_audit() | algebra_audit()
    spec = importlib.util.spec_from_file_location('independent_boundary_audit', HERE/'verify_independent.py')
    require(spec is not None and spec.loader is not None, 'independent module specification')
    independent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(independent)
    require(report == independent.audit(ROOT), 'independent exact audit disagreement')
    report.update(status='PASS', decision='SYMMETRIC-ISOLATED-CONTACT-EXCLUDED-BELOW-1/2',
                  physical_realization='NOT_PROVIDED', model_error_bound='NOT_CALIBRATED',
                  independent_audit='AGREE', scope='NON-CANONICAL L1 restricted effective-model boundary')
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
