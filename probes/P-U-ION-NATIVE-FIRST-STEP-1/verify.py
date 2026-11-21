"""Exact audit of a frozen global-force first-native-step construction."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST_SHA256 = "831106e859554394d3595745f83713cdeb8fbce265b0b1d3a8c42817f7a9a6f6"
NAME = "P-U-ION-NATIVE-FIRST-STEP-1"
ZERO = (F(0),) * 8


def scalar(x):
    return (F(x),) + ZERO[1:]


ONE = scalar(1)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    out = [F(0)] * 8
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % 8] += x * y * (1 if i + j < 8 else -1)
    return tuple(out)


def root_power(n):
    n %= 16
    out = list(ZERO)
    out[n % 8] = F(1 if n < 8 else -1)
    return tuple(out)


def conjugate(a):
    out = ZERO
    for k, x in enumerate(a):
        if x:
            out = add(out, mul(scalar(x), root_power(-k)))
    return out


def trig(units):
    # Rotation angle is units*pi/4, hence its half angle is units*pi/8.
    pos, minus = root_power(units), root_power(-units)
    return mul(scalar(F(1, 2)), add(pos, minus)), mul(
        scalar(F(1, 2)), mul(root_power(-4), add(pos, neg(minus)))
    )


def put(state, key, value):
    if value != ZERO:
        state[key] = add(state.get(key, ZERO), value)
        if state[key] == ZERO:
            del state[key]


def canonical_stars(p):
    """Chronological Rx(0,j,pi) monomial with the specified permutation."""
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
        if len(cycle) < 2:
            continue
        if cycle[0] == 0:
            word.extend(cycle[1:])
        else:
            word.extend(cycle + cycle[:1])
    return word


def monomial(word, x, inverse=False):
    phase = ONE
    for j in reversed(word) if inverse else word:
        if x in (0, j):
            x = j if x == 0 else 0
            phase = mul(phase, root_power(4 if inverse else -4))
    return x, phase


def control_permutation(state, word, inverse=False):
    out = {}
    for (x, y), amp in state.items():
        xx, phase = monomial(word, x, inverse)
        put(out, (xx, y), mul(phase, amp))
    return out


def rotate_pair_target(state, k, units):
    c, s = trig(units)
    out = {}
    for (x, y), amp in state.items():
        if y == 0:
            put(out, (x, 0), mul(c, amp))
            put(out, (x, k), mul(s, amp))
        elif y == k:
            put(out, (x, 0), neg(mul(s, amp)))
            put(out, (x, k), mul(c, amp))
        else:
            put(out, (x, y), amp)
    return out


def equality_echo(state, sign, omitted=False):
    # The physical global scalar is accounted analytically in MODEL/PROOF.
    out = {}
    for (x, y), amp in state.items():
        phase = ONE if omitted or x != y else root_power(-4 * sign)
        put(out, (x, y), mul(phase, amp))
    return out


def mask_permutation(pair, k):
    a, b = sorted(pair)
    p = [None] * 5
    p[a], p[b] = 0, k
    for x, y in zip([j for j in range(5) if j not in pair],
                    [j for j in range(5) if j not in (0, k)]):
        p[x] = y
    return tuple(p)


def masks(j):
    b, c = [x for x in range(5) if x != j][:2]
    return [((j, b), 1), ((j, c), 1), ((b, c), -1)]


def controlled_word(j, k, state, sign=1, omitted=False):
    for pair, beta in masks(j):
        word = canonical_stars(mask_permutation(pair, k))
        state = control_permutation(state, word)
        for unused in range(2):
            state = equality_echo(state, sign, omitted)
        state = rotate_pair_target(state, k, -beta)
        for unused in range(2):
            state = equality_echo(state, sign, omitted)
        state = rotate_pair_target(state, k, beta)
        state = control_permutation(state, word, inverse=True)
    return state


def determinant2(v, w):
    return any((v[i] * w[j] - v[j] * w[i]) % 5
               for i in range(3) for j in range(i + 1, 3))


def dot(v, u):
    return sum(x * y for x, y in zip(v, u)) % 5


def audit_echo():
    directions = [v for v in product(range(5), repeat=3)
                  if any(v) and next(x for x in v if x) == 1]
    assert len(directions) == 31
    active = (1, 0, 0)
    pool = [v for v in directions if v != active]
    affine = {(a, b): tuple((a * x + b) % 5 for x in range(5))
              for a in range(1, 5) for b in range(5)}
    lengths = {}
    for key, p in affine.items():
        word = canonical_stars(p)
        assert len(word) <= 6
        for x in range(5):
            y, phase = monomial(word, x)
            back, phase_back = monomial(word, y, True)
            assert y == p[x] and back == x and mul(phase, phase_back) == ONE
        lengths[key] = len(word)
    assert sum(lengths.values()) == 72
    vectors = list(product(range(5), repeat=3))
    for target in range(2, 8):
        pair = (target, 14)
        layout, cursor = [], 0
        for ion in range(17):
            if ion in pair:
                layout.append(active)
            else:
                layout.append(pool[cursor])
                cursor += 1
        assert cursor == 15
        gate_carriers = 0
        for i, v in enumerate(layout):
            occurrence = Counter((a, dot(v, u)) for a in range(1, 5) for u in vectors)
            assert occurrence == Counter({key: 25 for key in affine})
            gate_carriers += 2 * sum(n * lengths[key] for key, n in occurrence.items())
            for j in range(i + 1, 17):
                w = layout[j]
                if (i, j) == pair:
                    assert v == w
                else:
                    assert determinant2(v, w)
                    hist = Counter((dot(v, u), dot(w, u)) for u in vectors)
                    assert hist == Counter({(x, y): 5 for x in range(5) for y in range(5)})
        assert gate_carriers == 61200
        for x in range(5):
            for y in range(5):
                hist = Counter(((a*x+dot(active,u)) % 5, (a*y+dot(active,u)) % 5)
                               for a in range(1,5) for u in vectors)
                expected = ({(j,j):100 for j in range(5)} if x == y else
                            {(j,k):25 for j in range(5) for k in range(5) if j != k})
                assert hist == Counter(expected)
    # These coefficient identities imply 25*B for the active pair and scalar
    # cross/self/local terms for all others, independently of d and c_i.
    return gate_carriers


def audit_crot():
    tables, omitted_tables = {}, {}
    for units in (-8, -4, -1, 0, 1, 4, 8):
        c, s = trig(units)
        assert add(mul(c,c),mul(s,s)) == ONE
    for j in range(5):
        for k in range(1,5):
            cols, omitted_cols = {}, {}
            for x in range(5):
                for y in range(5):
                    expected_y, phase = y, ONE
                    if x == j and y in (0,k):
                        expected_y = k if y == 0 else 0
                        phase = ONE if y == 0 else neg(ONE)
                    expected = {(x,expected_y):phase}
                    for sign in (-1,1):
                        got = controlled_word(j,k,{(x,y):ONE},sign)
                        assert got == expected
                    omitted = controlled_word(j,k,{(x,y):ONE},omitted=True)
                    assert omitted == {(x,y):ONE}
                    cols[(x,y)] = got
                    omitted_cols[(x,y)] = omitted
            tables[j,k] = cols
            omitted_tables[j,k] = omitted_cols
    return tables, omitted_tables


OUTPUTS = [(0,0,0,0,0,0), (0,0,0,0,4,0), (2,1,2,1,4,0),
           (2,1,3,4,3,1), (2,1,3,4,3,1)]


def native_zero_cell(cell, offset):
    # Independently compare the pulse-design table with the original native
    # selector and generators at theta_0=0 in the fixed physical dictionary.
    a,b,c,d,v,r = cell
    q = (v + offset) % 5
    j = (a+b+c+d+q+r) % 5
    branches = [(b,a,d,c,q,r), (-c,-d,-a,-b,-q,-r),
                (2-c,1-d+r,2-a,1-b-r,1-q,-r),
                (2-a,1-b,3-c,4-d,1-q,1-r),
                (2-a,1-b,3-c,4-d,2-q,1-r)]
    result = list(branches[j])
    result[4] -= offset
    return tuple(x % 5 for x in result),j


def program():
    word = []
    for k in range(1,5):
        word.extend([('C',6,k,14,k), ('C',14,k,6,k)])
    for j in range(1,5):
        for offset,k in enumerate(OUTPUTS[j]):
            if k:
                word.append(('C',14,j,2+offset,k))
    for k in range(1,5):
        word.append(('X2',14,k))
    word.extend([('Y',12,3),('Y',15,1),('Y',16,1)])
    return word


def apply_full(state, operation, tables, inverse=False):
    out = {}
    if operation[0] == 'C':
        _, c, j, t, k = operation
        cols = tables[j,k]
        if inverse:
            cols_inverse = {}
            for source, entries in cols.items():
                for dest, phase in entries.items():
                    cols_inverse.setdefault(dest,{})[source] = conjugate(phase)
            cols = cols_inverse
        for basis, amp in state.items():
            for (x,y), phase in cols[basis[c],basis[t]].items():
                target = list(basis)
                target[c],target[t] = x,y
                put(out,tuple(target),mul(amp,phase))
    elif operation[0] == 'X2':
        _, ion, k = operation
        for basis, amp in state.items():
            put(out,basis,neg(amp) if basis[ion] in (0,k) else amp)
    else:
        _, ion, k = operation
        for basis,amp in state.items():
            local = rotate_pair_target({(0,basis[ion]):amp},k,-4 if inverse else 4)
            for (_,y), value in local.items():
                target = list(basis)
                target[ion] = y
                put(out,tuple(target),value)
    return out


def audit_program(tables, omitted_tables, echo_carriers):
    word = program()
    controls = [op for op in word if op[0] == 'C']
    assert len(controls) == 26
    extra_frames = sum(2*len(canonical_stars(mask_permutation(pair,op[4])))
                       for op in controls for pair,beta in masks(op[2]))
    echoes = 12*len(controls)
    ls_loops = 500*echoes
    carriers = echoes*echo_carriers + extra_frames + 6*len(controls) + 7
    angle_pi = echoes*echo_carriers + extra_frames + F(6*len(controls),4) + 8 + 3
    assert echoes == 312 and ls_loops == 156000
    assert carriers <= 19095499 and angle_pi <= 19095386
    initial_states, final_states, omitted_success = [], [], 0
    for s in range(5):
        for t in range(5):
            initial = [0]*17
            initial[0],initial[1],initial[6] = 1,t,s
            initial = tuple(initial)
            expected = list(initial)
            first,j1 = native_zero_cell(initial[2:8],0)
            second,j2 = native_zero_cell(initial[8:14],1)
            assert first == OUTPUTS[s] and second == (0,0,0,0,3,0)
            assert (j1,j2) == (s,1)
            expected[2:8],expected[8:14] = first,second
            expected[14],expected[15],expected[16] = j1,j2,1
            expected = tuple(expected)
            state,control = {initial:ONE},{initial:ONE}
            for op in word:
                state = apply_full(state,op,tables)
                control = apply_full(control,op,omitted_tables)
            assert state == {expected:ONE}
            omitted_success += int(control == {expected:ONE})
            for op in reversed(word):
                state = apply_full(state,op,tables,inverse=True)
            assert state == {initial:ONE}
            initial_states.append(initial)
            final_states.append(expected)
    assert len(set(initial_states)) == len(set(final_states)) == 25
    assert omitted_success == 5
    for t in range(5):
        left,right = final_states[3*5+t],final_states[4*5+t]
        assert left[:14] == right[:14] and left[14:] == (3,1,1) and right[14:] == (4,1,1)
    return dict(actual_inputs=25,crot_columns=500,echo_rows=500,ls_loops=ls_loops,
                echoes=echoes,carrier_pulses=carriers,carrier_angle_pi=str(angle_pi),
                omitted_ls_success=omitted_success,extra_frame_pulses=extra_frames,
                switching_boundaries=carriers+ls_loops+1)


def custody():
    raw = (ROOT/'INPUTS.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == MANIFEST_SHA256
    manifest = json.loads(raw)
    for entry in manifest['files']:
        data = (ROOT/entry['path']).read_bytes()
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'],entry['path']


def main():
    custody()
    echo_carriers = audit_echo()
    tables, omitted = audit_crot()
    result = audit_program(tables,omitted,echo_carriers)
    child = subprocess.run([sys.executable,str(ROOT/'verify_independent.py')],
                           cwd=ROOT,capture_output=True,timeout=300,check=True)
    assert not child.stderr
    independent = json.loads(child.stdout)
    assert independent['status'] == 'PASS'
    for key in ('actual_inputs','crot_columns','echo_rows','ls_loops','omitted_ls_success'):
        assert independent[key] == result[key],key
    print(NAME)
    print('STATUS NON-CANONICAL CONDITIONAL IDEAL FIRST NATIVE STEP')
    print('MODEL 17 Ca40 ions; global fixed-profile LS; individual star carriers')
    print('PAIR ISOLATION 500 finite affine loops; all spectators scalar')
    print('TARGET 25 coherent inputs; full data, retained M1/M2 and finite counter')
    print('COUNTS '+json.dumps(result,sort_keys=True,separators=(',',':')))
    print('MEMORY s=3,4 data merge; physical memory remains orthogonal')
    print('DEVICE ERROR / PRACTICAL FIDELITY / FULL HISTORY NOT CERTIFIED')
    print('INDEPENDENT_SHA256 '+hashlib.sha256(child.stdout).hexdigest())
    print('FIRST NATIVE STEP AUDIT PASS')


if __name__ == '__main__':
    main()
