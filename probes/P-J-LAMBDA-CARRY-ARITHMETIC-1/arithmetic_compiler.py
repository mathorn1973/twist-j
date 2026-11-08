#!/usr/bin/env python3
"""Exact bounded-coefficient carry compiler. NON-CANONICAL.

ADD is integer addition modulo 5^L; SUM is digit addition modulo five.
Every ADD expands to a reversible ripple schedule; every H expands to
EQ/MUL primitives; those expand to the frozen physical pulse constructions.
No large carry table is used by this compiler. All work is explicit.
"""
from functools import lru_cache
from pathlib import Path
import argparse
import importlib.util
import json

BINOMIAL = {2: (0, 0, 1, 3, 1), 3: (0, 0, 0, 1, 4),
            4: (0, 0, 0, 0, 1)}
UNITS = {'J': (1, 0, 1, 0), 'J_inverse': (0, -1, -1, 0)}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def digit_value(memory, wires):
    result = 0
    for w in reversed(wires):
        result = 5*result+memory[w]
    return result


def put_digits(memory, wires, value):
    for w in wires:
        memory[w], value = value % 5, value//5
    require(value == 0, 'nonnegative integer fits digit bank')


def inverse(block):
    out = dict(block)
    op = out['op']
    if op in ('ADD', 'H', 'MUL'):
        out['sign'] = -out['sign']
    elif op in ('SUM', 'EQ', 'SHIFT'):
        out['k'] = -out['k']
    elif op == 'SCALE':
        out['k'] = pow(out['k'], -1, 5)
    else:
        require(op == 'REFLECT', 'known inverse block')
    return out


def reversed_blocks(blocks):
    return [inverse(b) for b in reversed(blocks)]


def unary_blocks(source, degree, target, sign=1):
    for x, v in enumerate(BINOMIAL[degree]):
        if v:
            yield {'op': 'EQ', 'x': source, 'value': x,
                   'target': target, 'k': sign*v}


def h_blocks(x, y, target, scratch, sign=1):
    """target += sign*floor((x+y)/5), with two returned clean helpers."""
    p, q = scratch
    require(len({x, y, target, p, q}) == 5, 'H distinct inputs, target and helpers')
    for dx, dy in ((1, 4), (2, 3), (3, 2), (4, 1)):
        prep = []
        if dx != 1:
            prep.extend(unary_blocks(x, dx, p))
        if dy != 1:
            prep.extend(unary_blocks(y, dy, q))
        yield from prep
        yield {'op': 'MUL', 'x': x if dx == 1 else p,
               'y': y if dy == 1 else q, 'target': target, 'sign': sign}
        yield from reversed_blocks(prep)


def delta_product(control, source, value, target, helper, sign=1):
    yield {'op': 'EQ', 'x': source, 'value': value, 'target': helper, 'k': 1}
    yield {'op': 'MUL', 'x': control, 'y': helper, 'target': target, 'sign': sign}
    yield {'op': 'EQ', 'x': source, 'value': value, 'target': helper, 'k': -1}


def adder_blocks(a, b, carries, scratch, zero, sign=1):
    """True reversible ripple schedule for B += A mod5^L.

Repeated read-only zero wires in A are permitted. Work and writable B
are disjoint, and all ADDs return their carry and H helpers to zero.
"""
    a, b = tuple(a), tuple(b)
    length = len(a)
    require(length == len(b) and length >= 1 and sign in (-1, 1), 'ADD dimensions')
    cc = tuple(carries[:max(0, length-1)])
    require(len(cc) == length-1 and len(set(b+cc+tuple(scratch))) == len(b)+len(cc)+2,
            'ADD writable banks disjoint')
    require(not set(a).intersection(b+cc+tuple(scratch)), 'ADD source read-only')
    require(zero not in b+cc+tuple(scratch), 'zero pad is read-only')
    schedule = []
    c = (zero,)+cc
    for i in range(length-1):
        schedule.append({'op': 'H', 'x': a[i], 'y': b[i], 'target': c[i+1], 'sign': 1})
        schedule.append({'op': 'SUM', 'x': a[i], 'target': b[i], 'k': 1})
        schedule.extend(delta_product(c[i], b[i], 4, c[i+1], scratch[0], 1))
        schedule.append({'op': 'SUM', 'x': c[i], 'target': b[i], 'k': 1})
    schedule.append({'op': 'SUM', 'x': a[-1], 'target': b[-1], 'k': 1})
    if length > 1:
        schedule.append({'op': 'SUM', 'x': c[-1], 'target': b[-1], 'k': 1})
    for i in range(length-2, -1, -1):
        schedule.append({'op': 'REFLECT', 'target': b[i]})
        schedule.append({'op': 'H', 'x': a[i], 'y': b[i], 'target': c[i+1], 'sign': -1})
        schedule.append({'op': 'REFLECT', 'target': b[i]})
        schedule.append({'op': 'SUM', 'x': a[i], 'target': b[i], 'k': -1})
        schedule.extend(delta_product(c[i], b[i], 0, c[i+1], scratch[0], -1))
        schedule.append({'op': 'SUM', 'x': a[i], 'target': b[i], 'k': 1})
    yield from schedule if sign == 1 else reversed_blocks(schedule)


def layout(n):
    require(n >= 1, 'positive finite length')
    start = 2*n
    carry = []
    for _ in range(n+1):
        carry.append([list(range(start+3*j, start+3*j+3)) for j in range(4)])
        start += 12
    total = start+10
    return {'N': n, 'data': list(range(n)), 'buffer': list(range(n, 2*n)),
            'carry': carry, 'S': list(range(start, start+4)),
            'adder_carries': list(range(start+4, start+7)),
            'h_scratch': list(range(start+7, start+9)), 'zero': start+9,
            'cells': total, 'cells_with_archive': total+n}


def offset_blocks(bank, sign=1):
    # Bank must initially be zero on the declared prepared interface.
    yield {'op': 'SHIFT', 'target': bank[1], 'k': sign*2}
    yield {'op': 'SHIFT', 'target': bank[2], 'k': sign}


def padded(wires, length, zero):
    require(len(wires) <= length, 'zero extension dimension')
    return list(wires)+[zero]*(length-len(wires))


def add_block(a, b, sign=1):
    return {'op': 'ADD', 'a': list(a), 'b': list(b), 'sign': sign}


def step_parts(unit, source, current, following, apparatus):
    u, s, z = UNITS[unit], apparatus['S'], apparatus['zero']
    prep = list(offset_blocks(s))
    for d in current:
        prep.append(add_block(padded(d, 4, z), s))
    for _ in range(abs(sum(u))):
        prep.append(add_block(padded([source], 4, z), s, 1 if sum(u) > 0 else -1))
    write = []
    for j in range(3):
        write.extend(offset_blocks(following[j]))
        for d in current[:j+1]:
            write.append(add_block(d, following[j]))
        factor = sum(u[:j+1])
        for _ in range(abs(factor)):
            write.append(add_block(padded([source], 3, z), following[j],
                                   1 if factor > 0 else -1))
        write.append(add_block(padded([s[0]], 3, z), following[j], -1))
        for _ in range(j+1):
            write.append(add_block(s[1:], following[j], -1))
    for x, y in zip(s[1:], following[3]):
        write.append({'op': 'SUM', 'x': x, 'target': y, 'k': 1})
    return prep, write


def step_blocks(unit, source, current, following, output, apparatus,
                digit_sign=1, reverse=False):
    prep, write = step_parts(unit, source, current, following, apparatus)
    yield from prep
    yield from reversed_blocks(write) if reverse else write
    if not reverse and output is not None:
        yield {'op': 'SUM', 'x': apparatus['S'][0], 'target': output, 'k': digit_sign}
    yield from reversed_blocks(prep)


def oracle_blocks(unit, inputs, outputs, apparatus, digit_sign=1):
    carry = apparatus['carry']
    init = [b for d in carry[0] for b in offset_blocks(d)]
    yield from init
    for i, source in enumerate(inputs):
        yield from step_blocks(unit, source, carry[i], carry[i+1], outputs[i],
                               apparatus, digit_sign)
    for i in range(len(inputs)-1, -1, -1):
        yield from step_blocks(unit, inputs[i], carry[i], carry[i+1], None,
                               apparatus, reverse=True)
    yield from reversed_blocks(init)


def multiplier_blocks(n, apparatus=None):
    apparatus = layout(n) if apparatus is None else apparatus
    x, y = apparatus['data'], apparatus['buffer']
    yield from oracle_blocks('J', x, y, apparatus)
    for a, b in zip(x, y):
        yield {'op': 'SUM', 'x': a, 'target': b, 'k': 1}
        yield {'op': 'SUM', 'x': b, 'target': a, 'k': -1}
        yield {'op': 'SUM', 'x': a, 'target': b, 'k': 1}
        yield {'op': 'SCALE', 'target': a, 'k': -1}
    yield from oracle_blocks('J_inverse', x, y, apparatus, -1)


def expand(block, apparatus, level='primitive'):
    if block['op'] == 'ADD':
        for inner in adder_blocks(block['a'], block['b'], apparatus['adder_carries'],
                                  apparatus['h_scratch'], apparatus['zero'], block['sign']):
            yield from expand(inner, apparatus, level)
    elif block['op'] == 'H' and level == 'primitive':
        yield from h_blocks(block['x'], block['y'], block['target'],
                            apparatus['h_scratch'], block['sign'])
    else:
        yield block


def expand_program(program, apparatus, level='primitive'):
    for block in program:
        yield from expand(block, apparatus, level)


def carry_value(x, y):
    return (x*BINOMIAL[4][y]+BINOMIAL[2][x]*BINOMIAL[3][y]
            +BINOMIAL[3][x]*BINOMIAL[2][y]+BINOMIAL[4][x]*y) % 5


def execute(program, memory, apparatus, level='add'):
    """Hierarchical exact execution. ADD/H block laws are separately exhaustive.

level='primitive' executes only EQ/MUL/SUM and local permutations.
level='h' executes the actual ripple schedule with certified H blocks.
level='add' executes the explicit coefficient schedule with certified ADDs.
This is not a claim to simulate every physical pulse of a large apparatus.
"""
    schedule = program if level == 'add' else expand_program(program, apparatus, level)
    for b in schedule:
        op = b['op']
        if op == 'ADD':
            n = len(b['a'])
            value = (digit_value(memory, b['b'])+b['sign']*digit_value(memory, b['a'])) % (5**n)
            put_digits(memory, b['b'], value)
        elif op == 'H':
            t = b['target']
            memory[t] = (memory[t]+b['sign']*carry_value(memory[b['x']], memory[b['y']])) % 5
        elif op == 'SUM':
            t = b['target']
            memory[t] = (memory[t]+b['k']*memory[b['x']]) % 5
        elif op == 'EQ':
            t = b['target']
            memory[t] = (memory[t]+b['k']*(memory[b['x']] == b['value'])) % 5
        elif op == 'MUL':
            t = b['target']
            memory[t] = (memory[t]+b['sign']*memory[b['x']]*memory[b['y']]) % 5
        elif op == 'SHIFT':
            t = b['target']
            memory[t] = (memory[t]+b['k']) % 5
        elif op == 'REFLECT':
            t = b['target']
            memory[t] = 4-memory[t]
        elif op == 'SCALE':
            t = b['target']
            memory[t] = b['k']*memory[t] % 5
        else:
            raise ValueError('unknown block '+op)


def lower_primitive(block, frozen):
    op = block['op']
    if op == 'SUM':
        yield from frozen.sum_pulses(block['x'], block['target'], block['k'])
    elif op == 'EQ':
        yield from frozen.equality_pulses(block['x'], block['value'], block['target'], block['k'])
    elif op == 'MUL':
        yield from frozen.product_pulses(block['x'], block['y'], block['target'], block['sign'])
    elif op == 'SHIFT':
        yield ('SHIFT', block['target'], block['k'] % 5)
    elif op == 'REFLECT':
        yield ('PERM', block['target'], (4, 3, 2, 1, 0))
    elif op == 'SCALE':
        yield ('SCALE', block['target'], block['k'] % 5)
    else:
        raise ValueError('physical lowering requires primitive blocks')


@lru_cache(maxsize=None)
def adder_inventory(length, sign=1):
    a, b = list(range(length)), list(range(length, 2*length))
    start = 2*length
    app = {'adder_carries': list(range(start, start+length-1)),
           'h_scratch': [start+length-1, start+length], 'zero': start+length+1}
    block = add_block(a, b, sign)
    return inventory(expand(block, app, 'primitive'))


def inventory(program):
    counts = {}
    pair = local = 0
    for b in program:
        op = b['op']
        if op == 'ADD':
            entry = adder_inventory(len(b['a']), b['sign'])
            pair += entry['pair_pulses']
            local += entry['local_operations']
            for name, count in entry['primitive_counts'].items():
                counts[name] = counts.get(name, 0)+count
            continue
        require(op in ('SUM', 'EQ', 'MUL', 'SHIFT', 'REFLECT', 'SCALE'), 'inventory primitive')
        counts[op] = counts.get(op, 0)+1
        pp, ll = {'SUM': (1, 2), 'EQ': (7, 11), 'MUL': (10, 29),
                  'SHIFT': (0, 1), 'REFLECT': (0, 1), 'SCALE': (0, 1)}[op]
        pair += pp
        local += ll
    return {'pair_pulses': pair, 'local_operations': local,
            'primitive_counts': dict(sorted(counts.items()))}


def load_frozen(path):
    spec = importlib.util.spec_from_file_location('frozen_carry_compiler', Path(path)/'compiler.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dependency_path(given=None):
    return Path(given) if given else Path(__file__).resolve().parents[2]/'notes'/'C-J-LAMBDA-CARRY-N'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--length', type=int, required=True)
    parser.add_argument('--dependency', help='directory containing frozen compiler.py for --pulses')
    parser.add_argument('--pulses', action='store_true')
    args = parser.parse_args()
    apparatus = layout(args.length)
    program = list(multiplier_blocks(args.length, apparatus))
    if args.pulses:
        frozen = load_frozen(dependency_path(args.dependency))
        for block in expand_program(program, apparatus):
            for gate in lower_primitive(block, frozen):
                print(json.dumps(gate, default=str))
    else:
        print(json.dumps({'layout': apparatus, 'inventory': inventory(program), 'blocks': program,
                          'scope': 'NON-CANONICAL supplied addressed controls; clock/routing excluded'},
                         sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
