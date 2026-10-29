#!/usr/bin/env python3
"""Prospective exact audit of the arithmetic carry compiler.

Run only after the public source pin. Deterministic JSON on stdout;
no floating-point scientific arithmetic, no canonical mutations.
The frozen baseline is rerun, including its independent lambda-basis audit.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import arithmetic_compiler as a

ARITHMETIC_COMPILER_PIN = '0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027'
BASELINE_PINS = {
    'compiler.py': '6568abd79d31ae69ac34e163a55da4d34269da97ef1bdfeaf7a890df2fda23e3',
    'verify_general.py': '6543587aee0c561d7080a99ca191082658ae569ee994cc256e932fff43239245',
    'check_independent.py': '7d6bad0dc8ee8a5c534cbce4888ff8464e33009a9b74bdc6b78eb16a21d9482c',
    'THEOREMS.md': '19f05a4365ac131b9c2e4deaa6cb2e19cfcccc5ec2b5ec90fe07f42417fdf84f',
}
TABLE_PINS = {
    'J': '2119e4134c93dc740711fb124027f8cf3c752be2b5c502c2002980462d04322a',
    'J_inverse': '838b779a394c71d79cccef53ac13d8fd0562fb9db55ee2bcc4ee2a794b8640c4',
}
LONG_LENGTHS = (8, 9, 12, 16, 32, 64, 128)


class Budget:
    def __init__(self):
        self.stop = time.monotonic()+540

    def check(self):
        if time.monotonic() >= self.stop:
            raise RuntimeError('INCOMPLETE: predetermined 540-second execution budget')

    def timeout(self):
        self.check()
        return max(1, int(self.stop-time.monotonic()))


def baseline(directory, budget):
    for name, wanted in BASELINE_PINS.items():
        a.require(sha256((directory/name).read_bytes()).hexdigest() == wanted,
                  'frozen dependency bytes: '+name)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='twist-carry-prospective-') as tmp:
        certificate, program = Path(tmp)/'carry.json', Path(tmp)/'program.json'
        reports = []
        commands = [
            [sys.executable, '-B', str(directory/'verify_general.py'),
             '--certificate', str(certificate), '--program', str(program)],
            [sys.executable, '-B', str(directory/'check_independent.py')],
        ]
        for command in commands:
            name = Path(command[2]).name
            try:
                result = subprocess.run(command, capture_output=True, text=True, env=env,
                                        timeout=budget.timeout(), check=False)
            except subprocess.TimeoutExpired as exc:
                retain_child_output(name, exc.stdout, exc.stderr)
                raise RuntimeError('INCOMPLETE: frozen baseline execution timeout: '+name) from exc
            if result.returncode != 0 or result.stderr != '':
                retain_child_output(name, result.stdout, result.stderr)
                raise AssertionError('frozen baseline did not complete cleanly: '+name)
            reports.append(json.loads(result.stdout))
        a.require(reports[0]['facts'] == reports[1]['facts'], 'two baseline representations agree')
        tables = json.loads(certificate.read_text())['tables']
    return tables, reports[0]['facts']


def retain_child_output(name, stdout, stderr):
    """Keep failed/partial child evidence in the enclosing retained run log."""
    for channel, data in (('stdout', stdout), ('stderr', stderr)):
        if data:
            sys.stderr.write('\n--- captured '+name+' '+channel+' ---\n')
            sys.stderr.flush()
            if isinstance(data, bytes):
                sys.stderr.buffer.write(data)
                sys.stderr.buffer.flush()
            else:
                sys.stderr.write(data)
                sys.stderr.flush()
            sys.stderr.write('\n--- end captured '+name+' '+channel+' ---\n')
            sys.stderr.flush()


def word_hash(h, *words):
    h.update(('>'.join(''.join(map(str, w)) for w in words)+'\n').encode('ascii'))


def verify_h(frozen):
    cases = 0
    inventories = []
    for sign in (-1, 1):
        blocks = list(a.h_blocks(0, 1, 2, (3, 4), sign))
        inventory = a.inventory(blocks)
        a.require(inventory['pair_pulses'] == 208 and inventory['local_operations'] == 380,
                  'H exact generated resource count')
        gates = [g for b in blocks for g in a.lower_primitive(b, frozen)]
        a.require(sum(g[0] == 'PAIR' for g in gates) == 208,
                  'H physical pair expansion inventory')
        a.require(sum(g[0] != 'PAIR' for g in gates) == 380,
                  'H physical local expansion inventory')
        a.require(all(g[3] > 0 for g in gates if g[0] == 'PAIR'), 'positive pair durations')
        inventories.append(inventory)
        for x, y, target in product(range(5), repeat=3):
            memory = [x, y, target, 0, 0]
            a.execute(blocks, memory, {})
            a.require(memory == [x, y, (target+sign*((x+y)//5)) % 5, 0, 0],
                      'H compiled primitives and clean helpers, including dirty target')
            cases += 1
    return {'cases': cases, 'inventory': inventories[0],
            'physical_phase_dependency': 'fresh frozen exact EQ/MUL matrix audits'}


def adder_fixture(length):
    start = 2*length
    app = {'adder_carries': list(range(start, start+length-1)),
           'h_scratch': [start+length-1, start+length], 'zero': start+length+1}
    aa, bb = list(range(length)), list(range(length, 2*length))
    forward = list(a.adder_blocks(aa, bb, app['adder_carries'], app['h_scratch'], app['zero']))
    reverse = a.reversed_blocks(forward)
    return app, aa, bb, forward, reverse, start+length+2


def verify_adders(budget):
    rows, primitive_cases = [], 0
    for length in (1, 2, 3, 4):
        app, aa, bb, forward, reverse, cells = adder_fixture(length)
        modulus = 5**length
        inventory = a.adder_inventory(length)
        expected = (1, 2) if length == 1 else (468*(length-1)+2, 872*(length-1)+4)
        a.require((inventory['pair_pulses'], inventory['local_operations']) == expected,
                  'generated ripple inventory')
        for x in range(modulus):
            budget.check()
            for y in range(modulus):
                memory = [0]*cells
                a.put_digits(memory, aa, x)
                a.put_digits(memory, bb, y)
                original = tuple(memory)
                a.execute(forward, memory, app)
                a.require(a.digit_value(memory, aa) == x and
                          a.digit_value(memory, bb) == (x+y) % modulus and
                          not any(memory[2*length:]), 'ripple result, unchanged input, clean work')
                a.execute(reverse, memory, app)
                a.require(tuple(memory) == original, 'ripple exact inverse on every pair')
        primitive_forward = list(a.expand_program(forward, app))
        primitive_reverse = a.reversed_blocks(primitive_forward)
        examples = product(range(modulus), repeat=2) if length <= 2 else product((0, 1, modulus-1), repeat=2)
        for x, y in examples:
            memory = [0]*cells
            a.put_digits(memory, aa, x)
            a.put_digits(memory, bb, y)
            original = tuple(memory)
            a.execute(primitive_forward, memory, app)
            a.require(a.digit_value(memory, aa) == x and
                      a.digit_value(memory, bb) == (x+y) % modulus and
                      not any(memory[2*length:]), 'fully primitive small ripple')
            a.execute(primitive_reverse, memory, app)
            a.require(tuple(memory) == original, 'fully primitive ripple inverse')
            primitive_cases += 1
        rows.append({'length': length, 'pairs': modulus**2, 'forward_and_inverse': True,
                     'pair_pulses': inventory['pair_pulses'],
                     'local_operations': inventory['local_operations']})
    return {'exhaustive': rows, 'primitive_cases': primitive_cases}


def set_carry(memory, bank, state):
    for wires, coefficient in zip(bank, state):
        a.put_digits(memory, wires, coefficient+35)


def get_carry(memory, bank):
    return tuple(a.digit_value(memory, wires)-35 for wires in bank)


def verify_edges(tables, frozen, budget):
    app = a.layout(1)
    current, following = app['carry']
    rows, new_tables, primitive_cases = [], {}, 0
    for unit in ('J', 'J_inverse'):
        states = tables[unit]['states']
        state_ids = {tuple(s): i for i, s in enumerate(states)}
        forward = list(a.step_blocks(unit, 0, current, following, 1, app))
        reverse = list(a.step_blocks(unit, 0, current, following, None, app, reverse=True))
        primitive_forward = list(a.expand_program(forward, app))
        primitive_reverse = list(a.expand_program(reverse, app))
        prep, _ = a.step_parts(unit, 0, current, following, app)
        transitions, min_s, max_s = [], 625, 0
        for i, state in enumerate(states):
            if i % 64 == 0:
                budget.check()
            row = []
            for digit in range(5):
                memory = [0]*app['cells']
                memory[0], memory[1] = digit, 3
                set_carry(memory, current, state)
                original = tuple(memory)
                prepared = list(memory)
                a.execute(prep, prepared, app)
                ss = a.digit_value(prepared, app['S'])
                a.require(ss == 175+sum(state)+sum(a.UNITS[unit])*digit,
                          'S exact integer, no modulus wrap')
                a.require(27 <= ss <= 323, 'proved S range')
                min_s, max_s = min(min_s, ss), max(max_s, ss)
                a.execute(forward, memory, app)
                out = (memory[1]-3) % 5
                nxt = get_carry(memory, following)
                a.require(nxt in state_ids and out == ss % 5 and
                          all(-35 <= c <= 35 for c in nxt), 'valid next carry and residue')
                got = [out, state_ids[nxt]]
                a.require(got == tables[unit]['transitions'][i][digit], 'every compiled carry edge agrees')
                a.require(get_carry(memory, current) == tuple(state) and memory[0] == digit and
                          not any(memory[w] for w in app['S']+app['adder_carries']+
                                  app['h_scratch']+[app['zero']]), 'carry input and small work clean')
                after = tuple(memory)
                a.execute(reverse, memory, app)
                wanted = list(original)
                wanted[1] = after[1]
                a.require(memory == wanted, 'literal reverse carry schedule clears new bank')
                if i in (0, len(states)//2, len(states)-1):
                    expanded = list(original)
                    a.execute(primitive_forward, expanded, app)
                    a.require(tuple(expanded) == after, 'primitive-expanded full coefficient step')
                    a.execute(primitive_reverse, expanded, app)
                    a.require(expanded == wanted, 'primitive-expanded full step cleanup')
                    primitive_cases += 1
                row.append(got)
            transitions.append(row)
        new_table = {'states': states, 'transitions': transitions}
        digest = sha256(frozen.canonical_bytes(new_table)).hexdigest()
        a.require(digest == TABLE_PINS[unit], 'generated table equals prior pinned closure')
        new_tables[unit] = new_table
        rows.append({'unit': unit, 'states': len(states), 'edges': len(states)*5,
                     'min_S': min_s, 'max_S': max_s, 'table_sha256': digest})
    return new_tables, {'tables': rows, 'primitive_step_cases': primitive_cases}


def verify_maps(tables, frozen, prior, budget):
    exhaustive, longer = [], []
    groups = [(n, product(range(5), repeat=n), exhaustive) for n in range(1, 8)]
    groups += [(n, frozen.patterns(n), longer) for n in LONG_LENGTHS]
    for n, words, destination in groups:
        h, count = sha256(), 0
        lam_n = frozen.ONE
        for _ in range(n):
            lam_n = frozen.multiply(lam_n, frozen.LAM)
        for word in words:
            if count % 1024 == 0:
                budget.check()
            value = frozen.encode(word)
            outputs = []
            for unit, u in (('J', frozen.J), ('J_inverse', frozen.J_INV)):
                output, end = frozen.stream(word, tables[unit])
                lhs = frozen.multiply(u, value)
                a.require(output == frozen.ring_digits(lhs, n), 'compiled edge word vs direct ring digits')
                rhs = frozen.add(frozen.encode(output), frozen.multiply(lam_n, tables[unit]['states'][end]))
                a.require(lhs == rhs, 'whole O telescoping identity, terminal carry retained')
                outputs.append(output)
            a.require(frozen.stream(outputs[0], tables['J_inverse'])[0] == tuple(word), 'inverse unit on compiled words')
            word_hash(h, word, *outputs)
            count += 1
        destination.append({'N': n, 'words': count, 'map_sha256': h.hexdigest()})
    a.require(exhaustive == prior['exhaustive'] and longer == prior['long'], 'all prior multiplication hashes')
    return exhaustive, longer


def verify_programs(tables, frozen, budget):
    multiplier_cases = dirty_cases = 0
    groups = [(n, product(range(5), repeat=n)) for n in range(1, 4)]
    groups += [(n, frozen.patterns(n)) for n in LONG_LENGTHS]
    for n, words in groups:
        app = a.layout(n)
        program = list(a.multiplier_blocks(n, app))
        oracles = {(unit, sign): list(a.oracle_blocks(unit, app['data'], app['buffer'], app, sign))
                   for unit in ('J', 'J_inverse') for sign in (-1, 1)}
        for word in words:
            budget.check()
            memory = [0]*app['cells']
            memory[:n] = word
            a.execute(program, memory, app)
            wanted = frozen.stream(word, tables['J'])[0]
            a.require(tuple(memory[:n]) == wanted and not any(memory[n:]), 'whole generated multiplier clean')
            multiplier_cases += 1
            for (unit, sign), oracle in oracles.items():
                memory = [0]*app['cells']
                memory[:n] = word
                previous = tuple((i+2) % 5 for i in range(n))
                memory[n:2*n] = previous
                a.execute(oracle, memory, app)
                out = frozen.stream(word, tables[unit])[0]
                wanted = tuple((x+sign*y) % 5 for x, y in zip(previous, out))
                a.require(tuple(memory[:n]) == tuple(word) and tuple(memory[n:2*n]) == wanted
                          and not any(memory[2*n:]), 'dirty E target, both signs, clean entire work')
                dirty_cases += 1
    return {'multiplier_cases_at_ADD_level': multiplier_cases,
            'dirty_oracle_cases_at_ADD_level': dirty_cases}


def verify_archive(frozen, prior, budget):
    results = []
    for n in range(1, 6):
        app = a.layout(n)
        program = list(a.multiplier_blocks(n, app))
        h, zeros, images = sha256(), 0, set()
        for count, source in enumerate(product(range(5), repeat=n)):
            if count % 32 == 0:
                budget.check()
            memory = [0]*app['cells_with_archive']
            memory[:n] = source
            for clock in range(n):
                copy = {'op': 'SUM', 'x': app['data'][clock],
                        'target': app['cells']+clock, 'k': 1}
                a.execute([copy], memory, app)
                a.execute(program, memory, app)
                a.require(not any(memory[n:app['cells']]), 'work reused cleanly between archive writes')
            record = tuple(memory[app['cells']:])
            images.add(record)
            word_hash(h, source, record)
            value = frozen.ZERO
            for letter in record:
                value = frozen.add(value, frozen.ROOTS[letter])
            zeros += value == frozen.ZERO
        a.require(len(images) == 5**n, 'archived word bijection')
        results.append({'N': n, 'words': 5**n, 'map_sha256': h.hexdigest(), 'zero_count': zeros})
    a.require(results == prior['word_readout'], 'whole generated archive preserves prior hashes and zero count')
    return results


def verify_resources():
    rows = []
    for n in (1, 2, 3, 5, 8, 32, 128):
        app = a.layout(n)
        program = list(a.multiplier_blocks(n, app))
        count = a.inventory(program)
        a.require(count['pair_pulses'] == 136917*n, 'generated multiplier pair inventory')
        a.require(count['local_operations'] == 255187*n+32, 'generated multiplier local inventory')
        a.require(app['cells'] == 14*n+22 and app['cells_with_archive'] == 15*n+22,
                  'actual allocated memory count')
        pair_word = n*count['pair_pulses']+n
        local_word = n*count['local_operations']+3*n
        a.require(pair_word == 136917*n*n+n and pair_word+local_word == 392104*n*n+36*n,
                  'whole word and initial Fourier resource inventory')
        rows.append({'N': n, 'cells': app['cells'], 'cells_with_archive': app['cells_with_archive'],
                     'multiplier_pair_pulses': count['pair_pulses'],
                     'multiplier_local_operations': count['local_operations'],
                     'word_pair_pulses': pair_word, 'word_total_operations': pair_word+local_word})
    a.require(136917*45 < 6249713, 'more than 45-fold paired upper-bound reduction')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dependency', help='directory of immutable preceding general-carry sources')
    args = parser.parse_args()
    budget = Budget()
    a.require(sha256(Path(a.__file__).read_bytes()).hexdigest() == ARITHMETIC_COMPILER_PIN,
              'new arithmetic compiler exact pinned source bytes')
    directory = a.dependency_path(args.dependency).resolve()
    tables, prior = baseline(directory, budget)
    frozen = a.load_frozen(directory)
    h = verify_h(frozen)
    adders = verify_adders(budget)
    compiled_tables, edges = verify_edges(tables, frozen, budget)
    exhaustive, longer = verify_maps(compiled_tables, frozen, prior, budget)
    programs = verify_programs(compiled_tables, frozen, budget)
    archive = verify_archive(frozen, prior, budget)
    resources = verify_resources()
    budget.check()
    print(json.dumps({'facts': {
        'arithmetic_compiler_sha256': ARITHMETIC_COMPILER_PIN,
        'baseline_dependency_pins': BASELINE_PINS,
        'baseline_independent_facts_agree': True, 'baseline_carry': prior['carry'],
        'baseline_primitive_matrices': prior['gates'],
        'H': h, 'adders': adders, 'edges': edges,
        'exhaustive': exhaustive, 'long': longer, 'programs': programs,
        'word_readout': archive, 'resources': resources,
    }, 'scope': {
        'status': 'NON-CANONICAL', 'scientific_float_arithmetic': False,
        'new_arithmetic_engine_independent_of_old_carry_table': True,
        'all_small_adders_executed_as_ripple_schedules': True,
        'all_reachable_edges_executed_as_coefficient_schedules': True,
        'archive_uses_generated_program_with_certified_ADD_blocks': True,
        'all_large_physical_pulses_simulated': False,
        'native_U_derivation': False, 'clock_and_routing_in_data_memory': False,
        'actual_single_outcome_law': False,
    }}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
