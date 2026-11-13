#!/usr/bin/env python3
"""Exact design-exposed audit of the thermal-launch capacity candidate.
Standard library only. The theorem is analytical; no full apparatus simulation.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import subprocess
import sys

COUNT = 0


def check(test: bool, message: str) -> None:
    global COUNT
    COUNT += 1
    if not test:
        raise AssertionError(message)


PAIRS = (
    ('0101', '0000'), ('0010', '0001'), ('1000', '0100'),
    ('0011', '0101'), ('0111', '0010'), ('1101', '1000'),
    ('1010', '0011'), ('1011', '0111'), ('1110', '1101'),
    ('1111', '1010'),
)
FORWARD = dict(PAIRS)
REVERSE = {v: u for u, v in PAIRS}


def energy(word: str, hot_gap: int = 3) -> int:
    return sum((hot_gap if i % 2 == 0 else 1) * int(b)
               for i, b in enumerate(word))


def weight(word: str) -> int:
    answer = 1
    for i in range(0, len(word), 2):
        answer *= {'00': 8, '01': 2, '10': 4, '11': 1}[word[i:i+2]]
    return answer


def grouped_capacity(n: int) -> F:
    groups: dict[int, list[tuple[int, int]]] = defaultdict(list)
    dims: dict[int, int] = defaultdict(int)
    for a in range(n + 1):
        for b in range(n + 1):
            e = 3*a + b
            multiplicity = comb(n, a) * comb(n, b)
            numerator = 2 ** (3*n - a - 2*b)
            dims[e] += multiplicity
            groups[e].append((numerator, multiplicity))
    check(sum(dims.values()) == 4**n, f'dimension N={n}')
    check(sum(w*m for rows in groups.values() for w, m in rows) == 15**n,
          f'normalization N={n}')
    total = 0
    for e, rows in groups.items():
        remaining = min(dims[e], dims.get(e-2, 0))
        for w, m in sorted(rows, reverse=True):
            used = min(m, remaining)
            total += used*w
            remaining -= used
        check(remaining == 0, f'sector capacity N={n},E={e}')
    return F(total, 15**n)


def exhaustive_capacity(n: int) -> F:
    shells: dict[int, list[int]] = defaultdict(list)
    for bits in product('01', repeat=2*n):
        word = ''.join(bits)
        shells[energy(word)].append(weight(word))
    return F(sum(sum(sorted(ws, reverse=True)[:len(shells.get(e-2, []))])
                 for e, ws in shells.items()), 15**n)


def audit_capacities() -> dict[int, F]:
    values = {n: grouped_capacity(n) for n in range(1, 33)}
    check(values[1] == F(4, 15), 'one-pair optimum')
    check(values[2] == F(7, 15), 'two-pair optimum')
    for n in range(1, 7):
        check(values[n] == exhaustive_capacity(n), f'exhaustive N={n}')
    for n, q in values.items():
        ground_low = F(2**(3*n) + n*2**(3*n-2), 15**n)
        check(0 < q <= 1-ground_low < 1, f'finite obstruction N={n}')
        if n > 1:
            check(q >= values[n-1], f'monotone capacity N={n}')
    return values


def audit_raw_reaction() -> None:
    check(len(FORWARD) == len(REVERSE) == 10, 'injection cardinality')
    check(sum(weight(u) for u in FORWARD) == 105, 'selected weight')
    check(all(energy(u)-energy(v) == 2 for u, v in PAIRS), 'all resonances')
    states = [''.join(bits) for bits in product('01', repeat=7)]
    permutation = {}
    for word in states:
        bath, s, t, ell = word[:4], int(word[4]), int(word[5]), int(word[6])
        if ell == 0 and s == t == 0 and bath in FORWARD:
            out = FORWARD[bath] + '110'
        elif ell == 0 and s == t == 1 and bath in REVERSE:
            out = REVERSE[bath] + '000'
        else:
            out = word
        permutation[word] = out
    check(len(set(permutation.values())) == 128, 'all-raw bijection')
    broken_gap = False
    for word, out in permutation.items():
        check(permutation[out] == word, 'all-raw involution')
        e = energy(word[:4]) + sum(map(int, word[4:]))
        ep = energy(out[:4]) + sum(map(int, out[4:]))
        check(e == ep, 'all-raw bare energy')
        # K = I-P, so K*=K and K^2=2K for this involutive permutation.
        def k_apply(vector: dict[str, int]) -> dict[str, int]:
            result: dict[str, int] = defaultdict(int)
            for key, amp in vector.items():
                result[key] += amp
                result[permutation[key]] -= amp
            return {key: amp for key, amp in result.items() if amp}
        k = k_apply({word: 1})
        check(k_apply(k) == {key: 2*amp for key, amp in k.items()},
              'positive-block polynomial')
        for key, amp in k.items():
            check(k_apply({key: 1}).get(word, 0) == amp, 'Hermitian block')
        if word[-1] == '1':
            check(out == word, 'occupied endpoint disables reaction')
        wrong_e = energy(word[:4], 2) + sum(map(int, word[4:]))
        wrong_ep = energy(out[:4], 2) + sum(map(int, out[4:]))
        broken_gap = broken_gap or wrong_e != wrong_ep
    check(broken_gap, 'negative control wrong hot gap')


# State = bath word, source bit, loader occupancy mask, main occupancy mask.
State = tuple[str, int, int, int]


def move(mask: int, src: int, dst: int) -> int | None:
    if (mask >> src) & 1 and not ((mask >> dst) & 1):
        return mask ^ (1 << src) ^ (1 << dst)
    return None


def edge(i: int, st: State, length: int, backwards: bool = False,
         guard: bool = True) -> State | None:
    bath, s, tm, cm = st
    last = (tm >> (length-1)) & 1
    if i == 0:
        if guard and last:
            return None
        if not backwards and s == 0 and not (tm & 1) and bath in FORWARD:
            return FORWARD[bath], 1, tm | 1, cm
        if backwards and s == 1 and (tm & 1) and bath in REVERSE:
            return REVERSE[bath], 0, tm ^ 1, cm
        return None
    if i < length:
        if i == length-1 and not s:
            return None
        src, dst = (i, i-1) if backwards else (i-1, i)
        out = move(tm, src, dst)
        return None if out is None else (bath, s, out, cm)
    if i == length:
        if not last:
            return None
        if not backwards and s == 1 and not (cm & 1):
            return bath, 0, tm, cm | 1
        if backwards and s == 0 and (cm & 1):
            return bath, 1, tm, cm ^ 1
        return None
    r = i-length
    src, dst = (r, r-1) if backwards else (r-1, r)
    out = move(cm, src, dst)
    return None if out is None else (bath, s, tm, out)


def vertex_q(j: int, st: State, length: int) -> int:
    bath, s, tm, cm = st
    last = (tm >> (length-1)) & 1
    if j == 0:
        return int(not last and bath in FORWARD and s == 0 and not (tm & 1))
    if j < length:
        return (tm >> (j-1)) & 1
    if j == length:
        return s*last
    return (cm >> (j-length-1)) & 1


def edge_d(i: int, st: State, length: int) -> int:
    bath, s, tm, cm = st
    last = (tm >> (length-1)) & 1
    if i == 0:
        return int(not last) * (int(bath in FORWARD and s == 0 and not (tm & 1))
              + int(bath in REVERSE and s == 1 and (tm & 1)))
    if i < length:
        return (s if i == length-1 else 1) * (((tm >> (i-1)) & 1) + ((tm >> i) & 1))
    if i == length:
        return last*(s+(cm & 1))
    r = i-length
    return ((cm >> (r-1)) & 1) + ((cm >> r) & 1)


def audit_paths() -> None:
    words = [''.join(bits) for bits in product('01', repeat=4)]
    for length in (2, 3, 5):
        k = 4*length
        all_active = set()
        for u, v in PAIRS:
            path: list[State] = [(u, 0, 0, 0)]
            path += [(v, 1, 1 << (j-1), 0) for j in range(1, length+1)]
            path += [(v, 0, 1 << (length-1), 1 << (r-1))
                     for r in range(1, 3*length+1)]
            check(len(path) == k+1, 'path length')
            for j, st in enumerate(path):
                check(st not in all_active, 'orthogonal bath/path states')
                all_active.add(st)
                total_e = energy(st[0])+st[1]+st[2].bit_count()+st[3].bit_count()
                check(total_e == energy(u), 'constant reached bare energy')
                for i in range(k):
                    check(edge(i, st, length) == (path[j+1] if i == j else None),
                          'exact forward adjacency')
                    check(edge(i, st, length, True) == (path[j-1] if i == j-1 else None),
                          'exact backward adjacency')
                    check(edge_d(i, st, length) == int(j in (i, i+1)),
                          'edge diagonal is path incidence')
                for vtx in range(k+1):
                    check(vertex_q(vtx, st, length) == int(vtx == j),
                          'one vertex potential per history')
        for bath in words:
            if bath in FORWARD:
                continue
            st = (bath, 0, 0, 0)
            for i in range(k):
                check(edge(i, st, length) is None and edge(i, st, length, True) is None,
                      'inactive initialized bath stays inactive')
                check(edge_d(i, st, length) == 0, 'inactive edge diagonal')
            for j in range(k+1):
                check(vertex_q(j, st, length) == 0, 'inactive vertex potential')
        # Reached first-main state from bath 0011: spent bath 0101 is launchable.
        witness = ('0101', 0, 1 << (length-1), 1)
        check(edge(0, witness, length, guard=False) ==
              ('0000', 1, (1 << (length-1)) | 1, 1), 'unguarded relaunch witness')
        check(edge(0, witness, length) is None, 'guard repairs relaunch')


def audit_energy_and_channel() -> None:
    words = [''.join(bits) for bits in product('01', repeat=4)]
    mean = sum(F(weight(w), 225)*energy(w) for w in words)
    second = sum(F(weight(w), 225)*energy(w)**2 for w in words)
    q = sum(F(weight(w), 225) for w in FORWARD)
    joint = sum(F(weight(w), 225)*energy(w) for w in FORWARD)
    check(mean == F(12, 5), 'bath mean')
    check(second-mean*mean == F(108, 25), 'bath variance')
    check(q == F(7, 15), 'launch weight')
    check(joint == F(412, 225), 'energy active covariance input')
    check(joint-mean*q == F(32, 45), 'covariance coefficient')
    check(q*(1-q) == F(56, 225), 'propagation mixing variance')
    end_mean = sum(F(weight(w), 225)*energy(FORWARD.get(w, w)) for w in words)
    check(end_mean == F(22, 15), 'endpoint bath mean')
    check(mean-end_mean == 2*q == F(14, 15), 'inclusive bare transfer')
    # All environment matrix units: tracing distinct successful bath outputs
    # kills u!=v; failed words are rejected. Logical/reference factors are untouched.
    for u in words:
        for v in words:
            reduced = int(u in FORWARD and v in FORWARD and FORWARD[u] == FORWARD[v])
            check(reduced == int(u == v and u in FORWARD), 'accepted environment matrix unit')
            for a in range(3):
                for b in range(3):
                    actual = {(a, b): reduced} if reduced else {}
                    expected = {(a, b): 1} if u == v and u in FORWARD else {}
                    check(actual == expected, 'data matrix unit tensor spectator')
    p0 = F(2, 5)*F(1024, 15625)*F(99, 50000)
    check(F(99, 100)*p0 > F(1, 20000), 'inherited rational slack')
    check(q*F(99, 100)*p0 > F(7, 300000), 'two-pair read lower bound')
    check(q/F(4, 15) == F(7, 4), 'throughput factor')
    check(2*F(5, 6)**1024 < F(1, 10**60), 'inherited loading norm margin')
    check(F(3, 4)**2048 < F(1, 10**30), 'inherited read tail margin')


def audit_sources() -> None:
    root = Path(__file__).resolve().parents[2]
    path = root/'notes/C-THERMAL-LAUNCH-CAPACITY-N/SOURCES.json'
    manifest = json.loads(path.read_text(encoding='utf-8'))
    for row in manifest['sources']:
        raw = subprocess.run(['git', 'cat-file', 'blob', f"{row['commit']}:{row['path']}"],
                             cwd=root, check=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE).stdout
        check(len(raw) == row['bytes'], 'source byte count')
        check(hashlib.sha256(raw).hexdigest() == row['sha256'], 'source sha256')


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError('optimized Python execution is not admitted')
    audit_sources()
    capacities = audit_capacities()
    audit_raw_reaction()
    audit_paths()
    audit_energy_and_channel()
    print('C-THERMAL-LAUNCH-CAPACITY-N exact audit')
    print('NON-CANONICAL L1 candidate-T; parent assembly conditional; independent review pending')
    print(f'checks {COUNT}')
    print('one_pair_optimum 4/15; two_pair_optimum 7/15')
    print('seven_qubit_full_space_energy_involution_positive_blocks PASS')
    print('guarded_loader_all_reached_edges_and_inactive_states PASS')
    print('unguarded_relaunch_negative_control DETECTED')
    print('bath_mean 12/5; bath_variance 108/25; active_energy_moment 412/225')
    print('bare_energy_transferred 14/15; covariance_coefficient 32/45')
    print('accepted_environment_and_toy_data_matrix_units PASS')
    print('conditional_read_weight > 7/300000; original_thresholds UNCHANGED')
    print('finite_capacity_table_N_1_to_32 EXACT (not a local implementation)')
    for n, value in capacities.items():
        print(f'N {n} q_max {value.numerator}/{value.denominator}')
    print('full_H_preparation occurrence renewed_engine reset UNRESOLVED')
    print('PASS')


if __name__ == '__main__':
    main()
