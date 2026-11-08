#!/usr/bin/env python3
"""First-engine exact audit of the all-N compiler; run only after freezing."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import factorial
from pathlib import Path
import argparse
import json
import compiler as c

EXHAUSTIVE_LENGTHS = tuple(range(1, 8))
LONG_LENGTHS = (8, 9, 12, 16, 32, 64, 128)


def row_hash_update(h, *words):
    h.update(('>'.join(''.join(map(str, w)) for w in words)+'\n').encode('ascii'))


def verify_analytic_constants():
    c.require(c.multiply(c.J, c.J_INV) == c.ONE, 'J inverse identity')
    c.require(1791**2 > 5*800**2, 'exact lower bound on all embedding moduli')
    c.require(Fraction(153600, 49) < 3135, 'integer Q ceiling')
    for a, b in product(range(5), repeat=2):
        for u in (c.J, c.J_INV):
            forcing = c.add(c.scale(b, u), (-a, 0, 0, 0))
            c.require(c.trace_norm(forcing) <= 96, 'forcing norm bound')
    # Formal polynomial identity H(t)K(t)=1-t^6, no complex-series claim.
    h, k = (1, -2, 2, -1), (1, 2, 2, 1)
    coefficients = [0]*7
    for i, a in enumerate(h):
        for j, b in enumerate(k):
            coefficients[i+j] += a*b
    c.require(coefficients == [1, 0, 0, 0, 0, 0, -1], 'periodic carry polynomial identity')


def verify_duality(tables):
    forward, backward = tables['J'], tables['J_inverse']
    index = {tuple(s): i for i, s in enumerate(backward['states'])}
    correspondence = []
    for state in forward['states']:
        dual = c.scale(-1, c.multiply(c.J_INV, state))
        c.require(dual in index, 'inverse carry correspondence contains state')
        correspondence.append(index[dual])
    c.require(len(set(correspondence)) == len(index) == len(forward['states']), 'bijection of carry closures')
    for src, row in enumerate(forward['transitions']):
        for b, (a, nxt) in enumerate(row):
            c.require(tuple(backward['transitions'][correspondence[src]][a]) == (b, correspondence[nxt]),
                      'duality swaps input/output labels of every edge')
    return 5*len(forward['states'])


def equality_turns(value, k, x, y):
    state = [x, y]
    phase = Fraction(0)
    gates = list(c.equality_pulses(0, value, 1, k))
    c.require(sum(g[0] == 'PAIR' for g in gates) == 7, 'equality seven-pulse inventory')
    c.require(sum(g[0] != 'PAIR' for g in gates) <= 11, 'equality local-gate inventory')
    for gate in gates:
        if gate[0] == 'SHIFT':
            _, i, shift = gate
            state[i] = (state[i]+shift) % 5
        elif gate[0] == 'PERM':
            _, i, permutation = gate
            state[i] = permutation[state[i]]
        elif gate[0] == 'PAIR':
            _, i, j, turns = gate
            c.require(turns > 0, 'positive pair-pulse duration')
            phase += turns*state[i]*state[j]
        else:
            c.require(gate[0] == 'F' and gate[1] == 1, 'only target Fourier boundaries')
    c.require(state == [x, y], 'diagonal equality phase restores control')
    return phase


def cubic_phase(x, y, z, sign):
    state = [x, y, z]
    total, additions = 0, 0
    for subset, coefficient in c.CUBIC_TERMS:
        pivot = subset[-1]
        for control in subset[:-1]:
            state[pivot] = (state[pivot]+state[control]) % 5
            additions += 1
        total += sign*coefficient*state[pivot]**3
        for control in reversed(subset[:-1]):
            state[pivot] = (state[pivot]-state[control]) % 5
            additions += 1
    c.require(state == [x, y, z] and additions == 10, 'cubic construction restores inputs')
    return total % 5


def verify_gates():
    phase_count = 0
    actual = {}
    for value, k, x, t in product(range(5), range(1, 5), range(5), range(5)):
        turns = equality_turns(value, k, x, t)
        expected = Fraction(k*int(x == value)*t, 5)
        c.require((turns-expected).denominator == 1, 'exact equality phase modulo a full turn')
        actual[value, k, x, t] = int(5*turns)
        phase_count += 1
    matrix_count = 0
    for value, k, x, incoming, outgoing in product(range(5), range(1, 5), range(5), range(5), range(5)):
        numerator = c.ZERO
        for t in range(5):
            exponent = ((incoming-outgoing)*t+actual[value, k, x, t]) % 5
            numerator = c.add(numerator, c.ROOTS[exponent])
        wanted = (incoming+k*int(x == value)) % 5
        c.require(numerator == (c.scale(5, c.ONE) if outgoing == wanted else c.ZERO),
                  'exact phase-free equality-add matrix')
        matrix_count += 1

    multiply_phase_count = 0
    phases = {}
    for sign, x, y, z in product((-1, 1), range(5), range(5), range(5)):
        phase = cubic_phase(x, y, z, sign)
        c.require(phase == sign*x*y*z % 5, 'cubic polarization in F5')
        phases[sign, x, y, z] = phase
        multiply_phase_count += 1
    for sign in (-1, 1):
        generated = list(c.product_pulses(0, 1, 2, sign))
        c.require(sum(g[0] == 'PAIR' for g in generated) == 10, 'multiply-add pair inventory')
        c.require(sum(g[0] != 'PAIR' for g in generated) == 29, 'multiply-add local inventory')
    multiply_matrix_count = 0
    for sign, x, y, incoming, outgoing in product((-1, 1), range(5), range(5), range(5), range(5)):
        numerator = c.ZERO
        for t in range(5):
            numerator = c.add(numerator, c.ROOTS[((incoming-outgoing)*t+phases[sign, x, y, t]) % 5])
        wanted = (incoming+sign*x*y) % 5
        c.require(numerator == (c.scale(5, c.ONE) if outgoing == wanted else c.ZERO),
                  'exact phase-free multiply-add matrix')
        multiply_matrix_count += 1
    return {'equality_phase_cases': phase_count, 'equality_matrix_cases': matrix_count,
            'multiply_phase_cases': multiply_phase_count, 'multiply_matrix_cases': multiply_matrix_count}


def verify_lookup_rows():
    cases = 0
    for r in (1, 2, 3, 4):
        values = tuple((i+1) % 5 for i in range(r))
        controls, targets = list(range(r)), [r, r+1]
        scratch = list(range(r+2, r+2+2*r-1))
        gates = list(c.lookup_row_pulses(controls, values, targets, (1, 4), scratch))
        c.require(sum(g[0] == 'PAIR' for g in gates) <= 34*r-20+2, 'row pair bound')
        c.require(sum(g[0] != 'PAIR' for g in gates) <= 80*r-58+4, 'row local bound')
        for source in product(range(5), repeat=r):
            for previous in ((0, 0), (2, 3)):
                flags = [int(x == a) for x, a in zip(source, values)]
                links = [0]*(r-1)
                for i in range(1, r):
                    left = flags[0] if i == 1 else links[i-2]
                    links[i-1] = (links[i-1]+left*flags[i]) % 5
                indicator = flags[0] if r == 1 else links[-1]
                result = ((previous[0]+indicator) % 5, (previous[1]+4*indicator) % 5)
                for i in range(r-1, 0, -1):
                    left = flags[0] if i == 1 else links[i-2]
                    links[i-1] = (links[i-1]-left*flags[i]) % 5
                for i in range(r):
                    flags[i] = (flags[i]-int(source[i] == values[i])) % 5
                hit = int(tuple(source) == values)
                c.require(result == ((previous[0]+hit) % 5, (previous[1]+4*hit) % 5), 'row lookup output')
                c.require(not any(flags+links), 'all row flags cleaned')
                cases += 1
    return cases


def verify_word(word, tables, q, run_program=False, dirty=False):
    j, end_j = c.stream(word, tables['J'])
    inverse, end_i = c.stream(word, tables['J_inverse'])
    n = len(word)
    value = c.encode(word)
    c.require(j == c.ring_digits(c.multiply(c.J, value), n), 'J agrees with exact quotient arithmetic')
    c.require(inverse == c.ring_digits(c.multiply(c.J_INV, value), n), 'inverse agrees with quotient arithmetic')
    lam_n = c.ONE
    for _ in range(n):
        lam_n = c.multiply(lam_n, c.LAM)
    for u, output, end, name in ((c.J, j, end_j, 'J'), (c.J_INV, inverse, end_i, 'J_inverse')):
        residual = c.multiply(lam_n, tables[name]['states'][end])
        c.require(c.multiply(u, value) == c.add(c.encode(output), residual), 'full telescoping identity in O')
    c.require(c.inplace(word, tables, q) == j, 'clean compiled multiplication')
    c.require(c.stream(j, tables['J_inverse'])[0] == tuple(word), 'inverse after forward')
    c.require(c.stream(inverse, tables['J'])[0] == tuple(word), 'forward after inverse')
    if dirty:
        target = tuple((i+2) % 5 for i in range(n))
        for name, expected in (('J', j), ('J_inverse', inverse)):
            got = c.oracle(word, target, tables[name], q)
            c.require(got == tuple((x+y) % 5 for x, y in zip(target, expected)), 'dirty target is digit addition')
    if run_program:
        c.require(c.simulate_blocks(word, tables, q) == j, 'generated block wiring agrees')
    return j, inverse


def verify_finite_words(tables, q):
    exhaustive, longer = [], []
    for n in EXHAUSTIVE_LENGTHS:
        h = sha256()
        for word in product(range(5), repeat=n):
            j, inverse = verify_word(word, tables, q, run_program=(n <= 3), dirty=(n <= 4))
            row_hash_update(h, word, j, inverse)
        exhaustive.append({'N': n, 'words': 5**n, 'map_sha256': h.hexdigest()})
    for n in LONG_LENGTHS:
        h = sha256()
        words = c.patterns(n)
        for word in words:
            j, inverse = verify_word(word, tables, q, run_program=True, dirty=True)
            row_hash_update(h, word, j, inverse)
        longer.append({'N': n, 'words': len(words), 'map_sha256': h.hexdigest()})
    return exhaustive, longer


def verify_readout(tables, q):
    rows = []
    for n in range(1, 6):
        h, zeros, images = sha256(), 0, set()
        for source in product(range(5), repeat=n):
            state, record = source, []
            for clock in range(n):
                record.append(state[clock])
                state = c.inplace(state, tables, q)
            out = tuple(record)
            images.add(out)
            row_hash_update(h, source, out)
            value = c.ZERO
            for a in out:
                value = c.add(value, c.ROOTS[a])
            zeros += value == c.ZERO
        c.require(len(images) == 5**n, 'whole archived word is a bijection')
        expected_zeros = factorial(n)//factorial(n//5)**5 if n % 5 == 0 else 0
        c.require(zeros == expected_zeros, 'exact O return count')
        rows.append({'N': n, 'words': 5**n, 'map_sha256': h.hexdigest(), 'zero_count': zeros})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', required=True)
    parser.add_argument('--program', required=True)
    args = parser.parse_args()
    verify_analytic_constants()
    tables, summaries = {}, []
    for name in ('J', 'J_inverse'):
        table, summary = c.enumerate_carry(name)
        tables[name] = table
        summaries.append(summary)
    c.require(summaries[0]['q'] == summaries[1]['q'], 'same carry coding width')
    q = summaries[0]['q']
    dual_edges = verify_duality(tables)
    gates = verify_gates()
    row_cases = verify_lookup_rows()
    exhaustive, longer = verify_finite_words(tables, q)
    readout = verify_readout(tables, q)
    negative_input = (0, 3, 0, 0, 0, 0)
    correct, _ = c.stream(negative_input, tables['J'])
    wrong = (0, 1, 4, 3, 0, 0)
    c.require(correct == (0, 1, 4, 3, 0, 4) and correct != wrong, 'A5 carry is insufficient for A6')
    facts = {'carry': summaries, 'dual_edges': dual_edges, 'gates': gates,
             'exhaustive': exhaustive, 'long': longer, 'word_readout': readout,
             'resources': c.resource_bound(tables, q),
             'negative_A6': {'input': list(negative_input), 'correct': list(correct), 'old_shortcut': list(wrong)}}
    certificate = {'q': q, 'tables': tables, 'zero_id': 0,
                   'encoding': 'little-endian base-five identifiers; zero first, then lexicographic zeta coefficients',
                   'scope': 'complete reachable closures, independent of N'}
    program = {'layout': c.layout(8, q), 'blocks': list(c.multiplier_blocks(8, q)),
               'bound': facts['resources'], 'clock_and_routing': 'not included in data/work layout'}
    for name, value in ((args.certificate, certificate), (args.program, program)):
        path = Path(name)
        with path.open('x') as f:
            json.dump(value, f, sort_keys=True, separators=(',', ':'))
            f.write('\n')
    print(json.dumps({'facts': facts, 'checks': {
        'engine': 'zeta-basis integer ring, independently discovered closures, reversible work-code simulation',
        'row_lookup_cases': row_cases,
        'expanded_all_physical_pulses_of_large_tables': False,
        'primitive_pulse_matrices_exact': True,
        'scientific_floats': False,
        'canonical_mutations': False,
        'native_U_compilation': False}}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
