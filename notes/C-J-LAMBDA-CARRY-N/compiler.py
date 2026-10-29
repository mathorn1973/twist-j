#!/usr/bin/env python3
"""Exact all-length carry compiler. NON-CANONICAL, supplied control model.

Arithmetic is in Z[zeta_5]; work-register additions are coordinatewise F5.
Pulse lowering uses a fixed finite gate alphabet. It does not claim a native
U controller or spatial routing. No floating-point scientific arithmetic.
"""
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
LAM = (1, -1, 0, 0)
J = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)
UNITS = {'J': J, 'J_inverse': J_INV}
ROOTS = (ONE, (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, -1, -1, -1))
MAX_CARRY_STATES = 1_000_000


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k*x for x in a)


def multiply(a, b):
    c = [0]*7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i+k] += x*y
    for i in range(6, 3, -1):
        for k in range(4):
            c[i-4+k] -= c[i]
    return tuple(c[:4])


def divide_lambda(x):
    require(sum(x) % 5 == 0, 'exact divisibility by lambda')
    t = sum(x)//5
    return (x[0]-t, x[0]+x[1]-2*t, x[0]+x[1]+x[2]-3*t, t)


def ring_digits(x, n):
    out = []
    for _ in range(n):
        a = sum(x) % 5
        out.append(a)
        x = divide_lambda(add(x, (-a, 0, 0, 0)))
    return tuple(out)


def encode(word):
    x = ZERO
    for b in reversed(word):
        x = add(multiply(LAM, x), (b, 0, 0, 0))
    return x


def trace_norm(c):
    return 5*sum(x*x for x in c)-sum(c)**2


def carry_step(c, b, u):
    t = add(c, scale(b, u))
    a = sum(t) % 5
    nxt = divide_lambda(add(t, (-a, 0, 0, 0)))
    return a, nxt


def id_digits(i, q):
    out = []
    for _ in range(q):
        out.append(i % 5)
        i //= 5
    require(i == 0, 'state identifier fits its code')
    return tuple(out)


def digits_id(word):
    value = 0
    for d in reversed(word):
        value = 5*value+d
    return value


@lru_cache(maxsize=None)
def codebook(count, q):
    return tuple(id_digits(i, q) for i in range(count))


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')


def enumerate_carry(name):
    u = UNITS[name]
    distance = {ZERO: 0}
    pending = deque([ZERO])
    while pending:
        c = pending.popleft()
        for b in range(5):
            a, nxt = carry_step(c, b, u)
            require(add(multiply(LAM, nxt), (a, 0, 0, 0)) == add(c, scale(b, u)),
                    'exact carry edge in O')
            require(trace_norm(nxt) <= 3134 and max(map(abs, nxt)) <= 35,
                    'proved carry bound')
            if nxt not in distance:
                if len(distance) >= MAX_CARRY_STATES:
                    raise RuntimeError('INCOMPLETE ENUMERATION: resource ceiling; not a mathematical falsifier')
                distance[nxt] = distance[c]+1
                pending.append(nxt)
    states = [ZERO] + sorted(c for c in distance if c != ZERO)
    index = {c: i for i, c in enumerate(states)}
    transitions = []
    for c in states:
        row = []
        for b in range(5):
            a, nxt = carry_step(c, b, u)
            row.append((a, index[nxt]))
        require(sorted(a for a, _ in row) == list(range(5)), 'digit permutation for fixed carry')
        transitions.append(row)
    table = {'states': states, 'transitions': transitions}
    q, power = 0, 1
    while power < len(states):
        q += 1
        power *= 5
    summary = {'unit': name, 'states': len(states), 'edges': 5*len(states),
               'max_depth': max(distance.values()), 'max_Q': max(map(trace_norm, states)),
               'max_abs': max(max(map(abs, c)) for c in states), 'q': q,
               'table_sha256': sha256(canonical_bytes(table)).hexdigest()}
    return table, summary


def stream(word, table):
    state = 0
    out = []
    for b in word:
        a, state = table['transitions'][state][b]
        out.append(a)
    return tuple(out), state


def oracle(word, target, table, q, sign=1):
    """Simulate the compiled lookup blocks, including actual work-code cleanup.

Each lookup block is lowered separately by lookup_pulses. This simulator
does not pretend to enumerate every physical pulse of an enormous table.
"""
    n = len(word)
    require(len(target) == n and sign in (-1, 1), 'oracle dimensions and sign')
    codes = codebook(len(table['states']), q)
    work = [(0,)*q for _ in range(n+1)]
    result = list(target)
    for i, b in enumerate(word):
        c = digits_id(work[i])
        a, nxt = table['transitions'][c][b]
        result[i] = (result[i]+sign*a) % 5
        work[i+1] = tuple((x+y) % 5 for x, y in zip(work[i+1], codes[nxt]))
    for i in range(n-1, -1, -1):
        c = digits_id(work[i])
        _, nxt = table['transitions'][c][word[i]]
        work[i+1] = tuple((x-y) % 5 for x, y in zip(work[i+1], codes[nxt]))
    require(all(code == (0,)*q for code in work), 'every carry work cell returned to zero')
    return tuple(result)


def inplace(word, tables, q):
    buffer = oracle(word, (0,)*len(word), tables['J'], q)
    data, buffer = buffer, tuple(word)
    buffer = oracle(data, buffer, tables['J_inverse'], q, sign=-1)
    require(buffer == (0,)*len(word), 'inverse multiplication erased the old data buffer')
    return data


def patterns(n):
    result = {tuple([d]*n) for d in range(5)}
    result.add(tuple(i % 5 for i in range(n)))
    result.add(tuple((4-i) % 5 for i in range(n)))
    result.add(tuple(i.bit_count() % 2 for i in range(n)))
    for offset in range(5):
        result.add(tuple((i*i+3*i+offset) % 5 for i in range(n)))
    for position in (0, n//2, n-1):
        for d in range(1, 5):
            w = [0]*n
            w[position] = d
            result.add(tuple(w))
    return sorted(result)


def sum_pulses(control, target, k=1):
    k %= 5
    if not k:
        return
    yield ('F', target, 1)
    yield ('PAIR', control, target, Fraction(k, 5))
    yield ('F', target, -1)


def equality_pulses(control, value, target, k=1):
    """Target += k[control=value]; exact seven positive pair pulses."""
    k %= 5
    if not k:
        return
    yield ('SHIFT', control, (4-value) % 5)
    yield ('F', target, 1)
    s = (3, 2, 1, 0, 4)
    yield ('PERM', control, s)
    yield ('PAIR', control, target, Fraction(k, 25))
    yield ('PERM', control, s)
    yield ('PAIR', control, target, Fraction(k, 25))
    beta = Fraction(25-3*k, 250)
    for _ in range(5):
        yield ('PAIR', control, target, beta)
        yield ('SHIFT', control, 1)
    yield ('F', target, -1)
    yield ('SHIFT', control, (value-4) % 5)


CUBIC_TERMS = (((0, 1, 2), 1), ((0, 1), -1), ((0, 2), -1),
               ((1, 2), -1), ((0,), 1), ((1,), 1), ((2,), 1))


def product_pulses(x, y, target, sign=1):
    """Target += sign*x*y over F5; ten pair pulses, no extra cell."""
    require(len({x, y, target}) == 3 and sign in (-1, 1), 'distinct multiplier wires')
    wires = (x, y, target)
    yield ('F', target, 1)
    for subset, coefficient in CUBIC_TERMS:
        pivot = wires[subset[-1]]
        controls = [wires[i] for i in subset[:-1]]
        for control in controls:
            yield from sum_pulses(control, pivot, 1)
        yield ('CUBIC', pivot, sign*coefficient)
        for control in reversed(controls):
            yield from sum_pulses(control, pivot, -1)
    yield ('F', target, -1)


def lookup_row_pulses(controls, values, targets, additions, scratch):
    """One equality row with a clean 2r-1-cell reversible flag tree."""
    r = len(controls)
    require(len(values) == r and len(scratch) == 2*r-1 and len(targets) == len(additions),
            'lookup row dimensions')
    if not any(v % 5 for v in additions):
        return
    flags, links = scratch[:r], scratch[r:]
    for c, v, f in zip(controls, values, flags):
        yield from equality_pulses(c, v, f, 1)
    for i in range(1, r):
        left = flags[0] if i == 1 else links[i-2]
        yield from product_pulses(left, flags[i], links[i-1], 1)
    final = flags[0] if r == 1 else links[-1]
    for target, value in zip(targets, additions):
        yield from sum_pulses(final, target, value)
    for i in range(r-1, 0, -1):
        left = flags[0] if i == 1 else links[i-2]
        yield from product_pulses(left, flags[i], links[i-1], -1)
    for c, v, f in reversed(list(zip(controls, values, flags))):
        yield from equality_pulses(c, v, f, -1)


def layout(n, q):
    require(n >= 1 and q >= 1, 'nonempty finite apparatus')
    data = list(range(n))
    buffer = list(range(n, 2*n))
    carry = [list(range(2*n+i*q, 2*n+(i+1)*q)) for i in range(n+1)]
    start = 2*n+q*(n+1)
    scratch = list(range(start, start+2*q+1))
    return {'N': n, 'q': q, 'data': data, 'buffer': buffer, 'carry': carry,
            'scratch': scratch, 'cells': start+2*q+1}


def oracle_blocks(unit, inputs, outputs, apparatus, sign=1):
    carry = apparatus['carry']
    for i, b in enumerate(inputs):
        yield {'kind': 'LOOKUP', 'unit': unit, 'controls': carry[i]+[b],
               'targets': carry[i+1]+[outputs[i]], 'mode': 'carry_and_digit',
               'digit_sign': sign, 'carry_sign': 1}
    for i in range(len(inputs)-1, -1, -1):
        yield {'kind': 'LOOKUP', 'unit': unit, 'controls': carry[i]+[inputs[i]],
               'targets': carry[i+1], 'mode': 'carry_only', 'carry_sign': -1}


def multiplier_blocks(n, q):
    apparatus = layout(n, q)
    x, y = apparatus['data'], apparatus['buffer']
    yield from oracle_blocks('J', x, y, apparatus, 1)
    for a, b in zip(x, y):
        yield {'kind': 'SUM', 'control': a, 'target': b, 'coefficient': 1}
        yield {'kind': 'SUM', 'control': b, 'target': a, 'coefficient': 4}
        yield {'kind': 'SUM', 'control': a, 'target': b, 'coefficient': 1}
        yield {'kind': 'SCALE', 'target': a, 'coefficient': 4}
    yield from oracle_blocks('J_inverse', x, y, apparatus, -1)


def lower_block(block, tables, apparatus):
    kind = block['kind']
    if kind == 'SUM':
        yield from sum_pulses(block['control'], block['target'], block['coefficient'])
    elif kind == 'SCALE':
        yield ('SCALE', block['target'], block['coefficient'])
    elif kind == 'LOOKUP':
        q = apparatus['q']
        for c, row in enumerate(tables[block['unit']]['transitions']):
            for b, (a, nxt) in enumerate(row):
                values = id_digits(c, q)+(b,)
                additions = tuple(block['carry_sign']*d for d in id_digits(nxt, q))
                if block['mode'] == 'carry_and_digit':
                    additions += (block['digit_sign']*a,)
                yield from lookup_row_pulses(block['controls'], values, block['targets'],
                                            additions, apparatus['scratch'])
    else:
        raise ValueError('unknown compiled block')


def resource_bound(tables, q):
    rows_j, rows_i = (5*len(tables[u]['states']) for u in ('J', 'J_inverse'))
    return {'q': q, 'rows_J': rows_j, 'rows_inverse': rows_i,
            'pair_upper_per_digit': (70*q+29)*(rows_j+rows_i)+3,
            'memory_linear': q+2, 'memory_constant': 3*q+1}


def simulate_blocks(word, tables, q):
    """Execute the generated program at the proved lookup-block level."""
    apparatus = layout(len(word), q)
    memory = [0]*apparatus['cells']
    memory[:len(word)] = word
    for block in multiplier_blocks(len(word), q):
        if block['kind'] == 'SUM':
            c, t = block['control'], block['target']
            memory[t] = (memory[t]+block['coefficient']*memory[c]) % 5
        elif block['kind'] == 'SCALE':
            t = block['target']
            memory[t] = block['coefficient']*memory[t] % 5
        else:
            control_values = tuple(memory[i] for i in block['controls'])
            c, b = digits_id(control_values[:-1]), control_values[-1]
            table = tables[block['unit']]
            if c < len(table['states']):
                a, nxt = table['transitions'][c][b]
                delta = tuple(block['carry_sign']*d for d in id_digits(nxt, q))
                if block['mode'] == 'carry_and_digit':
                    delta += (block['digit_sign']*a,)
                for t, d in zip(block['targets'], delta):
                    memory[t] = (memory[t]+d) % 5
    require(all(v == 0 for v in memory[len(word):]), 'generated block program clean workspace')
    return tuple(memory[:len(word)])


if __name__ == '__main__':
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tables', required=True, help='verified CARRY_TABLES.json')
    parser.add_argument('--length', required=True, type=int)
    parser.add_argument('--pulses', action='store_true', help='expand every pulse; potentially very large')
    args = parser.parse_args()
    saved = json.loads(Path(args.tables).read_text())
    tables = saved['tables']
    q = saved['q']
    apparatus = layout(args.length, q)
    if not args.pulses:
        print(json.dumps({'layout': apparatus, 'bounds': resource_bound(tables, q),
                          'blocks': list(multiplier_blocks(args.length, q)),
                          'scope': 'NON-CANONICAL supplied addressed controls; clock excluded'}, indent=2))
    else:
        for block in multiplier_blocks(args.length, q):
            for gate in lower_block(block, tables, apparatus):
                print(json.dumps(gate, default=str))
