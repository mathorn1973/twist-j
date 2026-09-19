#!/usr/bin/env python3
"""NON-CANONICAL DRAFT: proposed P-QDD-NATIVE-POINT-PORT-CAPACITY-1 audit.
Adapted from A. M. Thorn's Apache-2.0 issue #1036 audit.py, Git blob
3e48205d4649118006377f559b9423950a6d97d7. This preparation has not run it.
Pin and review under current POLICY.md before any formal execution.
Frozen census, bound and constructive-certificate checks added for intake.
This program audits finite identities; it does not establish physical events
or prove universal history statements by extrapolating finite trajectories.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import factorial

ELL = (0, 1, 2, -2, -1)
ZERO = (0, 0, 0, 0)
EXPECTED_CENSUS = {
    F(0): 84, F(1, 256): 24, F(1, 176): 48, F(1, 136): 32,
    F(1, 96): 24, F(1, 56): 48, F(1, 46): 36, F(1, 26): 48,
    F(9, 224): 24, F(1, 16): 56, F(9, 104): 24, F(2, 17): 24,
    F(9, 64): 24, F(5, 32): 8, F(1, 6): 24, F(2, 7): 24,
    F(5, 16): 24, F(3, 8): 16, F(5, 8): 8, F(9, 14): 12,
    F(49, 64): 8, F(1): 4,
}
FREE_CERTIFICATE = (
    (F(0), F(1, 46), F(1, 92)),
    (F(1, 26), F(1, 6), F(4, 39)),
    (F(2, 7), F(3, 8), F(37, 112)),
    (F(5, 8), F(49, 64), F(89, 128)),
    (F(1), F(1), F(1)),
)


def multinomial_census():
    # Independent carrier enumeration: 69 supported multiplicity patterns.
    census = Counter()
    patterns = 0
    for ns in product(range(5), repeat=5):
        if sum(ns) != 4 or ns[2] == 4:
            continue
        patterns += 1
        s = sum(a*n for a, n in zip(range(-2, 3), ns))
        norm = sum(a*a*n for a, n in zip(range(-2, 3), ns))
        denominator = 1
        for n in ns:
            denominator *= factorial(n)
        census[F(s*s, 4*(5*norm-s*s))] += factorial(4)//denominator
    assert patterns == 69
    return census


def generators(x):
    a, b, c, d, q, r = x
    rows = ((b, a, d, c, q, r), (-c, -d, -a, -b, -q, -r),
            (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
            (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
            (2-a, 1-b, 3-c, 4-d, 2-q, 1-r))
    return tuple(tuple(y % 5 for y in row) for row in rows)


def quotient(x):
    return (sum(x) % 5, x[4], x[5])


def qgenerators(y):
    z, q, r = y
    rows = ((z, q, r), (-z, -q, -r), (2-z, 1-q, -r),
            (2-z, 1-q, 1-r), (3-z, 2-q, 1-r))
    return tuple(tuple(a % 5 for a in row) for row in rows)


def step(x, t):
    return generators(x)[(sum(x)+2*t) % 5]


def beta(p):
    v = tuple(ELL[a] for a in p)
    s, norm = sum(v), sum(a*a for a in v)
    if not norm:
        return None  # ZERO_SUPPORT, never a probability zero.
    return F(s*s, 4*(5*norm-s*s))


def evaluate_matrix(v, m):
    return sum(v[i]*m[i][j]*v[j] for i in range(4) for j in range(4))


def groups_from_cuts(values, cuts):
    endpoints = (0,)+tuple(cuts)+(len(values),)
    return [values[a:b] for a, b in zip(endpoints, endpoints[1:])]


def group_row(values):
    return {'count': len(values), 'lo': values[0], 'hi': values[-1],
            'center': (values[0]+values[-1])/2}


def exhaustive_cover(values, k):
    best = None
    for cuts in combinations(range(1, len(values)), k-1):
        groups = groups_from_cuts(values, cuts)
        radius = max((g[-1]-g[0])/2 for g in groups)
        trial = (radius, cuts)
        if best is None or trial < best:
            best = trial
    assert best is not None
    return best


def dynamic_cover(values, k):
    # Independent interval recurrence, optimizing diameters rather than centers.
    m = len(values)
    dp = [[None]*(m+1) for _ in range(k+1)]
    dp[0][0] = F(0)
    for t in range(1, k+1):
        for j in range(t, m+1):
            options = [max(dp[t-1][i], values[j-1]-values[i])
                       for i in range(t-1, j) if dp[t-1][i] is not None]
            dp[t][j] = min(options)
    return dp[k][m]/2


def packing_certificate(values, k):
    best_gap, best_indices = F(-1), None
    for inds in combinations(range(len(values)), k):
        gap = min(values[b]-values[a] for a, b in zip(inds, inds[1:]))
        if gap > best_gap:
            best_gap, best_indices = gap, inds
    assert best_indices is not None
    return best_gap, best_indices


def json_fraction(o):
    if isinstance(o, F):
        return str(o)
    raise TypeError(type(o).__name__)


def main():
    ps = list(product(range(5), repeat=4))
    bs = {p: beta(p) for p in ps}
    g = [[F(i == j)-F(1, 5) for j in range(4)] for i in range(4)]
    low = [[F(1, 20) for j in range(4)] for i in range(4)]
    for p in ps:
        v = tuple(ELL[a] for a in p)
        mass, low_mass = evaluate_matrix(v, g), evaluate_matrix(v, low)
        if p == ZERO:
            assert mass == low_mass == 0 and bs[p] is None
        else:
            assert mass > 0 and 0 <= low_mass <= mass
            assert bs[p] == low_mass/mass
    native_edges = selected_edges = 0
    for x in product(range(5), repeat=6):
        ys, qs = generators(x), qgenerators(quotient(x))
        for y, qy in zip(ys, qs):
            assert quotient(y) == qy
            native_edges += 1
        for t in (0, 1):
            idx = (sum(x)+2*t) % 5
            assert quotient(step(x, t)) == qs[idx]
            selected_edges += 1
    # Regressions of inherited common-ready observability, not a new all-time proof.
    ready_classes = []
    time_edges = 0
    for ready in product(range(5), repeat=2):
        by_sum = {}
        for p in ps:
            x = p+ready
            hist = [ready]
            for n in range(8):
                x = step(x, n.bit_count() % 2)
                hist.append(x[4:])
                time_edges += 1
            key = sum(p) % 5
            hist = tuple(hist)
            if key in by_sum:
                assert by_sum[key] == hist
            by_sum[key] = hist
        full_count = len(set(by_sum.values()))
        prefix_count = len({h[:3] for h in by_sum.values()})
        assert full_count == prefix_count == (4 if ready == (3, 0) else 5)
        ready_classes.append((ready, prefix_count))
    fixed_v = ((1, -1, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0),
               (1, 1, 1, 0), (2, 1, 1, 2), (1, 1, 1, 1))
    fixed_b = (F(0), F(1, 16), F(1, 6), F(3, 8), F(9, 14), F(1))
    fixed = []
    for v, value in zip(fixed_v, fixed_b):
        p = tuple(a % 5 for a in v)
        assert bs[p] == value
        fixed.append({'p': p, 'v': v, 'beta': value})
    assert min(b-a for a, b in zip(fixed_b, fixed_b[1:])) == F(1, 16)
    fibres = defaultdict(list)
    for p in ps:
        if p != ZERO:
            fibres[bs[p]].append(p)
    values = sorted(fibres)
    census = {value: len(fibres[value]) for value in values}
    assert sum(census.values()) == 624 and len(values) == 22
    assert census == EXPECTED_CENSUS == multinomial_census()
    assert sum(count for value, count in census.items() if value > F(5, 32)) == 120
    for value in values:
        matches = [(lo, hi, center) for lo, hi, center in FREE_CERTIFICATE
                   if lo <= value <= hi]
        assert len(matches) == 1
        lo, hi, center = matches[0]
        assert center == (lo+hi)/2 and abs(value-center) <= F(9, 128)
    packing_sources = ((0, 0, 1, 4), (0, 0, 1, 2), (0, 1, 1, 2),
                       (1, 1, 1, 2), (1, 2, 2, 2), (1, 1, 1, 1))
    packing_values = (F(0), F(9, 64), F(2, 7), F(5, 8), F(49, 64), F(1))
    assert tuple(bs[p] for p in packing_sources) == packing_values
    assert min(b-a for a, b in zip(packing_values, packing_values[1:])) == F(9, 64)
    eps, cuts = exhaustive_cover(values, 5)
    assert dynamic_cover(values, 5) == eps == F(9, 128)
    cover = groups_from_cuts(values, cuts)
    gap, inds = packing_certificate(values, 6)
    assert gap == 2*eps
    cover_rows = []
    free_signal = {}
    for signal, vals in enumerate(cover):
        row = group_row(vals)
        row['values'] = vals
        row['source_count'] = sum(len(fibres[a]) for a in vals)
        cover_rows.append(row)
        for value in vals:
            for p in fibres[value]:
                free_signal[p] = signal
                assert abs(bs[p]-row['center']) <= eps
    assert max(abs(bs[p]-cover_rows[free_signal[p]]['center'])
               for p in ps if p != ZERO) == eps
    ordered = sorted((p for p in ps if p != ZERO), key=lambda p: (bs[p], p))
    ordered_values = [bs[p] for p in ordered]
    faithful_cases = []
    for short_block in range(5):
        sizes = [124 if i == short_block else 125 for i in range(5)]
        end, block_values = 0, []
        for size in sizes:
            block_values.append(ordered_values[end:end+size])
            end += size
        assert end == 624
        rows = [group_row(a) for a in block_values]
        error = max((row['hi']-row['lo'])/2 for row in rows)
        faithful_cases.append({'short_block': short_block, 'error': error, 'groups': rows})
    faithful_best = min(faithful_cases, key=lambda a: (a['error'], a['short_block']))
    assert all(case['error'] == F(27, 64) for case in faithful_cases)
    assert faithful_best['short_block'] == 0
    assert [(row['lo'], row['hi'], row['center']) for row in faithful_best['groups']] == [
        (F(0), F(1, 176), F(1, 352)),
        (F(1, 176), F(1, 56), F(29, 2464)),
        (F(1, 56), F(1, 16), F(9, 224)),
        (F(1, 16), F(5, 32), F(7, 64)),
        (F(5, 32), F(1), F(37, 64)),
    ]
    native_fibres = {s: [p for p in ps if sum(p) % 5 == s] for s in range(5)}
    assert all(len(gp) == 125 for gp in native_fibres.values())
    permutation, faithful_signal = {}, {}
    end = 0
    for signal, row in enumerate(faithful_best['groups']):
        block = ordered[end:end+row['count']]
        end += row['count']
        for j, p in enumerate(block):
            permutation[p] = native_fibres[signal][j]
            faithful_signal[p] = signal
    short = faithful_best['short_block']
    permutation[ZERO] = native_fibres[short][-1]
    assert len(permutation) == 625 and set(permutation.values()) == set(ps)
    assert Counter(sum(y) % 5 for y in permutation.values()) == Counter({i: 125 for i in range(5)})
    observed_sum = {}
    for signal in range(5):
        x = native_fibres[signal][0]+(0, 1)
        a1 = step(x, 0)[4:]
        assert a1 not in observed_sum
        observed_sum[a1] = signal
    assert [step(native_fibres[s][0]+(0, 1), 0)[4:] for s in range(5)] == [
        (0, 4), (1, 4), (1, 0), (2, 0), (0, 1)]
    for p in ordered:
        a1 = step(permutation[p]+(0, 1), 0)[4:]
        signal = observed_sum[a1]
        assert signal == faithful_signal[p]
        assert abs(bs[p]-faithful_best['groups'][signal]['center']) <= faithful_best['error']
    assert max(abs(bs[p]-faithful_best['groups'][faithful_signal[p]]['center'])
               for p in ordered) == faithful_best['error']
    zero_signal = sum(permutation[ZERO]) % 5
    assert sum(faithful_signal[p] == zero_signal for p in ordered) == 124
    # Source-dependent loading counter-control. It is an input law, not a native derivation.
    assert all((1-bs[p])*0+bs[p]*1 == bs[p] for p in ordered)
    source_index = {p: i for i, p in enumerate(ps)}
    out = {
        'proposed_probe': 'P-QDD-NATIVE-POINT-PORT-CAPACITY-1',
        'status': 'finite exact audit only; proof acceptance and public status assessed separately',
        'checks': {'native_generator_edges': native_edges, 'selected_edges': selected_edges,
                   'ready_history_edges': time_edges, 'quadratic_inputs': len(ps)},
        'inherited_ready_classes': ready_classes,
        'target': {'supported_sources': 624, 'null': 'ZERO_SUPPORT; beta undefined',
                   'distinct_values': len(values),
                   'values': [{'beta': a, 'count': len(fibres[a]), 'first_p': fibres[a][0]}
                              for a in values]},
        'fixed_six': fixed,
        'free_five_message': {'error': eps, 'groups': cover_rows, 'packing_gap': gap,
                              'packing': [{'beta': values[i], 'p': fibres[values[i]][0]}
                                          for i in inds]},
        'faithful': {'cases': faithful_cases, 'best_error': faithful_best['error'],
                     'best_short_block': short, 'zero_shares_with_supported': 124,
                     'permutation_lex_source_to_lex_native_index': [source_index[permutation[p]] for p in ps]},
        'boundaries': ['One deterministic point per source; source-independent ready/noise.',
                       'No native feedback or source-sensitive extra observation.',
                       'Target-aware optima are comparison witnesses, not physical loaders.',
                       'Coherent codes and source-dependent stochastic loading are outside scope.',
                       'No physical QDD closure or two-architecture gate.'],
    }
    print(json.dumps(out, default=json_fraction, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
