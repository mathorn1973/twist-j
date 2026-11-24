"""Exact audit of the publicly pinned 64-block native-step program.

Primary arithmetic and affine counting adapt the disclosed #1369 primary.
The program compiler, complete exchange audit and primitive adjoint audit
are specific to this candidate. No predecessor program is imported.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
NAME = "P-U-ION-NATIVE-COMPRESSION-1"
MANIFEST_SHA256 = "3163b277d88b641328f74783b10e820504f17cf65a01c3a8c4948fc145b3b8e8"
ZERO = (F(0),) * 8
ONE = (F(1),) + ZERO[1:]


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


@lru_cache(maxsize=None)
def mul(a, b):
    out = [F(0)] * 8
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i+j) % 8] += x*y*(1 if i+j < 8 else -1)
    return tuple(out)


def root_power(n):
    n %= 16
    out = list(ZERO)
    out[n % 8] = F(1 if n < 8 else -1)
    return tuple(out)


@lru_cache(maxsize=None)
def trig(units):
    # theta=units*pi/4; zeta16=exp(i*pi/8).
    half = (F(1, 2),) + ZERO[1:]
    p, m = root_power(units), root_power(-units)
    return mul(half, add(p, m)), mul(half, mul(root_power(-4), add(p, neg(m))))


def put(state, key, value):
    if value != ZERO:
        value = add(state.get(key, ZERO), value)
        if value == ZERO:
            state.pop(key, None)
        else:
            state[key] = value


def canonical_stars(p):
    """Exact chronological canonical cycle compiler; never optimized."""
    assert sorted(p) == list(range(5))
    seen, word = set(), []
    for start in range(5):
        if start in seen:
            continue
        cycle, x = [], start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x]
        assert x == start
        if len(cycle) > 1:
            word.extend(cycle[1:] if start == 0 else cycle + cycle[:1])
    return word


def carrier(ion, k, axis, units):
    assert 1 <= k <= 4 and axis in ('x', 'y') and isinstance(units, int)
    return ('R', ion, k, axis, units)


def adjoint(word):
    # Algebraic adjoint: this does NOT assert a physical inverse LS primitive.
    return [op[:-1] + (-op[-1],) for op in reversed(word)]


def frame(ion, permutation):
    return [carrier(ion, k, 'x', 4) for k in canonical_stars(permutation)]


def mask_permutation(labels, k):
    labels = sorted(labels)
    assert len(labels) == 2 and labels[0] != labels[1]
    p = [None] * 5
    p[labels[0]], p[labels[1]] = 0, k
    for x, y in zip([x for x in range(5) if x not in labels],
                    [y for y in range(5) if y not in (0, k)]):
        p[x] = y
    return p


def mask_word(c, t, k, labels, beta):
    pre = frame(c, mask_permutation(labels, k))
    g = ('G', c, t, 1)
    return pre + [g, g, carrier(t, k, 'y', -beta), g, g,
                  carrier(t, k, 'y', beta)] + adjoint(pre)


def single_word(c, t, k, j):
    b, d = [x for x in range(5) if x != j][:2]
    return (mask_word(c, t, k, [j, b], 1)
            + mask_word(c, t, k, [j, d], 1)
            + mask_word(c, t, k, [b, d], -1))


def exchange_word(c, t, k):
    g = ('G', c, t, 1)
    word = [g]
    for axis in ('y', 'x'):
        word += [carrier(c, k, axis, -2), carrier(t, k, axis, -2), g,
                 carrier(c, k, axis, 2), carrier(t, k, axis, 2)]
    return word


def compile_operation(op):
    kind, *args = op
    if kind == 'carrier':
        return [carrier(*args)]
    if kind == 'mask':
        return mask_word(*args)
    if kind == 'single':
        return single_word(*args)
    assert kind == 'exchange'
    return exchange_word(*args)


def apply(state, op, sign=1, omitted=False):
    out = {}
    if op[0] == 'G':
        _, c, t, exponent = op
        phase = root_power(-4*sign*exponent)
        for basis, amp in state.items():
            factor = ONE if omitted or basis[c] != basis[t] else phase
            put(out, basis, mul(amp, factor))
        return out
    _, ion, k, axis, units = op
    co, si = trig(units)
    for basis, amp in state.items():
        x = basis[ion]
        if x not in (0, k):
            put(out, basis, amp)
            continue
        put(out, basis, mul(amp, co))
        dest = list(basis)
        dest[ion] = k if x == 0 else 0
        off = mul(root_power(-4), si) if axis == 'x' else (si if x == 0 else neg(si))
        put(out, tuple(dest), mul(amp, off))
    return out


def evolve(state, word, sign=1, omitted=False):
    for op in word:
        state = apply(state, op, sign, omitted)
    return state


def audit_echo():
    """Symbolic coefficient multiplicities, never substituted physical data."""
    vectors = list(product(range(5), repeat=3))
    directions = [v for v in vectors if any(v) and next(x for x in v if x) == 1]
    assert len(directions) == 31
    active = (1, 0, 0)
    pool = [v for v in directions if v != active]
    affine = {(a, b): tuple((a*x+b) % 5 for x in range(5))
              for a in range(1, 5) for b in range(5)}
    lengths = {}
    for key, p in affine.items():
        word = frame(0, p)
        assert len(word) <= 6
        for x in range(5):
            got = evolve({(x,): ONE}, word)
            assert set(got) == {(p[x],)}
            assert evolve(got, adjoint(word)) == {(x,): ONE}
        lengths[key] = len(word)
    assert sum(lengths.values()) == 72

    def dot(v, u):
        return sum(x*y for x, y in zip(v, u)) % 5

    for target in range(2, 8):
        layout, cursor = [], 0
        for ion in range(17):
            if ion in (target, 14):
                layout.append(active)
            else:
                layout.append(pool[cursor])
                cursor += 1
        assert cursor == 15
        count = 0
        for i, v in enumerate(layout):
            occurrence = Counter((a, dot(v, u)) for a in range(1, 5) for u in vectors)
            assert occurrence == Counter({key: 25 for key in affine})
            count += 2*sum(n*lengths[key] for key, n in occurrence.items())
            for j in range(i+1, 17):
                w = layout[j]
                if (i, j) == (target, 14):
                    assert v == w
                else:
                    assert any((v[r]*w[s]-v[s]*w[r]) % 5
                               for r in range(3) for s in range(r+1, 3))
                    assert Counter((dot(v, u), dot(w, u)) for u in vectors) == Counter(
                        {(x, y): 5 for x in range(5) for y in range(5)})
        assert count == 61200
        for x, y in product(range(5), repeat=2):
            actual = Counter(((a*x+dot(active, u)) % 5, (a*y+dot(active, u)) % 5)
                             for a in range(1, 5) for u in vectors)
            expected = ({(z, z): 100 for z in range(5)} if x == y else
                        {(z, w): 25 for z, w in product(range(5), repeat=2) if z != w})
            assert actual == Counter(expected)
    return count


def helper_signatures(operations):
    masks, singles = set(), set()
    for op in operations:
        if op[0] == 'mask':
            _, c, t, k, labels, beta = op
            masks.add((k, tuple(sorted(labels)), beta))
        elif op[0] == 'single':
            _, c, t, k, j = op
            singles.add((k, j))
            b, d = [x for x in range(5) if x != j][:2]
            for labels, beta in (([j, b], 1), ([j, d], 1), ([b, d], -1)):
                masks.add((k, tuple(sorted(labels)), beta))
    return sorted(masks), sorted(singles)


def audit_helpers(operations):
    masks, singles = helper_signatures(operations)
    for k in range(1, 5):
        word = exchange_word(0, 1, k)
        for sign in (-1, 1):
            for x, y in product(range(5), repeat=2):
                dest, factor = (x, y), ONE
                if x in (0, k) and y in (0, k):
                    dest, factor = (y, x), neg(ONE)
                elif x == y and x not in (0, k):
                    factor = root_power(4*sign)  # i*sign, NOT identity.
                initial = {(x, y): ONE}
                got = evolve(initial, word, sign)
                assert got == {dest: factor}
                assert evolve(got, adjoint(word), sign) == initial
                assert evolve(initial, word, sign, True) == initial
    for k, labels, beta in masks:
        word = mask_word(0, 1, k, labels, beta)
        for sign in (-1, 1):
            for x, y in product(range(5), repeat=2):
                initial = {(x, y): ONE}
                expected = (apply(initial, carrier(1, k, 'y', 2*beta))
                            if x in labels else initial)
                got = evolve(initial, word, sign)
                assert got == expected
                assert evolve(got, adjoint(word), sign) == initial
                assert evolve(initial, word, sign, True) == initial
    for k, j in singles:
        word = single_word(0, 1, k, j)
        for sign in (-1, 1):
            for x, y in product(range(5), repeat=2):
                initial = {(x, y): ONE}
                expected = apply(initial, carrier(1, k, 'y', 4)) if x == j else initial
                got = evolve(initial, word, sign)
                assert got == expected
                assert evolve(got, adjoint(word), sign) == initial
                assert evolve(initial, word, sign, True) == initial
    assert len(masks) == 12 and len(singles) == 2
    return dict(exchange_columns=200, mask_columns=50*len(masks), single_columns=50*len(singles))


OUTPUTS = [(0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 4, 0), (2, 1, 2, 1, 4, 0),
           (2, 1, 3, 4, 3, 1), (2, 1, 3, 4, 3, 1)]


def native_step(cell, offset):
    # Canon v97 original generators, physical R2 chart y=q-1, theta_0=0.
    a, b, c, d, v, r = cell
    q = (v+offset) % 5
    j = (a+b+c+d+q+r) % 5
    branches = [(b, a, d, c, q, r), (-c, -d, -a, -b, -q, -r),
                (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
                (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
                (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)]
    result = list(branches[j])
    result[4] -= offset
    return tuple(x % 5 for x in result), j


def audit_program(spec, echo_carriers):
    assert spec['schema'] == 'ion-native-compression-v1'
    assert spec['ions'] == 17 and spec['chronological'] is True
    assert spec['angle_unit'] == 'pi/4'
    operations = spec['operations']
    assert Counter(op[0] for op in operations) == Counter(
        exchange=4, mask=7, single=2, carrier=9)
    word = [primitive for op in operations for primitive in compile_operation(op)]
    g = [op for op in word if op[0] == 'G']
    rotation = [op for op in word if op[0] == 'R']
    exponents = Counter(tuple(sorted(op[1:3])) for op in g)
    expected_edges = {(k, 14): n for k, n in zip(range(2, 8), (4, 4, 16, 16, 20, 4))}
    assert exponents == expected_edges
    assert {(min(a, b), max(a, b)): n for a, b, n in spec['gamma_edges']} == expected_edges
    assert len(g) == 64 and all(op[-1] == 1 for op in g)
    carriers = 64*echo_carriers+len(rotation)
    area = F(64*echo_carriers)+sum((F(abs(op[-1]), 4) for op in rotation), F(0))
    switching = carriers+32000+1
    assert carriers <= spec['bounds']['carrier_pulses'] == 3917023
    assert area <= spec['bounds']['carrier_angle_pi'] == 3916995
    assert switching <= spec['bounds']['switching_boundaries'] == 3949024
    assert spec['bounds']['g_blocks'] == 64 and spec['bounds']['ls_loops'] == 32000
    assert spec['bounds']['omitted_ls_success'] == 0
    finals, control_success = [], 0
    for s, t in product(range(5), repeat=2):
        initial = [0]*17
        initial[0], initial[1], initial[6] = 1, t, s
        initial = tuple(initial)
        first, j1 = native_step(initial[2:8], 0)
        second, j2 = native_step(initial[8:14], 1)
        assert first == OUTPUTS[s] and second == (0, 0, 0, 0, 3, 0)
        assert (j1, j2) == (s, 1)
        expected = list(initial)
        expected[2:8], expected[8:14] = first, second
        expected[14], expected[15], expected[16] = j1, j2, 1
        expected = tuple(expected)
        for sign in (-1, 1):
            result = evolve({initial: ONE}, word, sign)
            assert result == {expected: ONE}
            assert evolve(result, adjoint(word), sign) == {initial: ONE}
        control = evolve({initial: ONE}, word, omitted=True)
        control_success += int(control == {expected: ONE})
        assert set(control) == {tuple([1, t, 2, 1, 0, 0, s, 0,
                                      0, 0, 0, 0, 3, 0, 0, 1, 1])}
        finals.append(expected)
    assert control_success == 0 and len(set(finals)) == 25
    for t in range(5):
        left, right = finals[15+t], finals[20+t]
        assert left[:14] == right[:14] and left[14:] == (3, 1, 1) and right[14:] == (4, 1, 1)
    return dict(actual_inputs=25, echo_rows=500, g_blocks=64, ls_loops=32000,
                carrier_pulses=carriers, carrier_angle_pi=str(area),
                switching_boundaries=switching, omitted_ls_success=control_success,
                gamma_exponents=[exponents[(k, 14)] for k in range(2, 8)])


def custody():
    raw = (ROOT/'INPUTS.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == MANIFEST_SHA256
    manifest = json.loads(raw)
    for entry in manifest['files']:
        data = (ROOT/entry['path']).read_bytes()
        assert len(data) == entry['bytes'], entry['path']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']


def main():
    custody()
    spec = json.loads((ROOT/'PROGRAM.json').read_text(encoding='utf-8'))
    echo_carriers = audit_echo()
    helpers = audit_helpers(spec['operations'])
    result = audit_program(spec, echo_carriers)
    result.update(helpers)
    child = subprocess.run([sys.executable, str(ROOT/'verify_independent.py')],
                           cwd=ROOT, capture_output=True, timeout=300, check=True)
    assert not child.stderr
    independent = json.loads(child.stdout)
    assert independent['status'] == 'PASS'
    for key in result:
        assert independent[key] == result[key], (key, independent.get(key), result[key])
    print(NAME)
    print('STATUS NON-CANONICAL CONDITIONAL IDEAL 64-BLOCK CANDIDATE')
    print('MODEL 17 Ca40 ions; unchanged six edges and 500-loop equality blocks')
    print('HELPERS full exchange sectors and controlled columns; both geometric signs')
    print('TARGET 25 full outputs with amplitude +1; retained memory and finite counter')
    print('COUNTS '+json.dumps(result, sort_keys=True, separators=(',', ':')))
    print('INVERSE algebraic primitive adjoints only; physical reverse program NOT CLAIMED')
    print('OMITTED_LS same carrier schedule and prescribed waits: 0/25')
    print('DEVICE ERROR / PRACTICAL FIDELITY / FULL HISTORY NOT CERTIFIED')
    print('INDEPENDENT_SHA256 '+hashlib.sha256(child.stdout).hexdigest())
    print('NATIVE COMPRESSION AUDIT PASS')


if __name__ == '__main__':
    main()
