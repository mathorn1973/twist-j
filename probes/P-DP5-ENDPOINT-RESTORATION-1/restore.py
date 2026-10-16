#!/usr/bin/env python3
"""Independent endpoint-restoration candidate, Apache-2.0, NON-CANONICAL.

No execution on import. No old numerical module is imported. Execution requires
the complete accepted public source/data pin and a clean exact Git checkout.
All scientific functions, including controls, are subject to preregistration.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isfinite, isqrt
from pathlib import Path
import multiprocessing
import platform
import queue
import signal
import struct
import subprocess
import sys
import time

P = 192
Q = 1 << P
N = 256
L = 8
DIM = 6435
COLS = 120
PAIRS = ((0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5))
LABELS = ((4, 3), (4, 4), (1, 1))
TAIL = F(680046581, 794280046581)
RETAINED = 1 - TAIL
THRESHOLD = F(1, 1000)
ZERO = (0, 0)
ONE = (Q, Q)
CZ = (0, 0, 0, 0)
CO = (Q, Q, 0, 0)
SCOPE = 'FULL_WORD_SIX_CASES_K3_CONDITIONAL'
CAMPAIGN_PIN = 'bca348445715c03f4cdc3af6079207024dd40332'
PAYLOADS = {
    'basis.json': (103064, 'ec66eca09652f6d5d5ee80f7beb592e72bfd31cd71d5a92ba52093d6d7970f61'),
    'components.bin': (69120, '581e371bce1fd72b1abab5f837b4e33786bada00a6e2de14d750542877928c41'),
    'endpoints.bin': (74131200, '7d67034f594bdc923794b61e019c3566b860d6bfe942143ff5c6a06d2b66066f'),
    'metadata.json': (6773, '7c2edd7701efad8a2db8af997d97c704a6460b1aeb3487d5503ac0083800fff2'),
    'result.json': (312313, '49940669a1954abaa52a230d1e40d76bc9bc7cef0b6eb395b1c57f10176f3e31'),
}
CUSTODY = {
    'artifact-inventory.json': (2424474, 'b540e5135c5d0b81f7c4e7b5ee8bf0a0ac9f08bf6812b1931b113666a40700c8'),
    'final-custody.json': (1575, 'ae81c8e940ae2beead4eca379c78b8d07380a573c4a04350e0316f366eed56a6'),
    'summary.json': (17670, 'ac9348f39112dfb00de47988f79f483b492600f4bfbbc4d8871babec4ded1def'),
}
# Content matches the preserved final-campaign receipt, four earlier saved
# inputs, and independent serialization of the immutable pinned JSON.
INPUT_CONTENT = (3918, '720f167680bbb51549165a10ba04ce9688de43cc67bb4087cd4ce5be20ebb471')
# Now independently read back against the actual preserved final-custody input.
SERIALIZED_INPUT = INPUT_CONTENT
BINDING_SHA256 = 'd01109396b54296d15535bf8625c800153071f666350fa1e4287ba1e436b15fc'
SOURCE_NAMES = {'README.md', 'PREREG.md', 'DERIVATION.md', 'SECURITY.md',
                'REVIEW.md', 'verify.py', 'restore.py', 'INPUT_BINDING.json'}
SECONDS = 600
WORKERS = 6
PARENT_MIB = 256
WORKER_MIB = 256
INTEGER_TEXT_DIGITS = 32768


class Rejected(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise Rejected(reason)


def failure_description(exc):
    # OS errors may include private absolute transport paths; public evidence
    # keeps their type, while declared Rejected reasons are fixed source text.
    return type(exc).__name__+(': '+str(exc) if isinstance(exc, Rejected) else '')


def ceildiv(a, b):
    require(type(a) is int and type(b) is int and b > 0, 'integer division domain')
    return -((-a) // b)


def rational(x):
    """JSON numeric operands have binary64 semantics, not decimal semantics."""
    require(type(x) in (int, float), 'numeric operand type')
    require(type(x) is int or isfinite(x), 'nonfinite numeric operand')
    return F(x)


def grid(lo, hi=None):
    lo = F(lo)
    hi = lo if hi is None else F(hi)
    require(lo <= hi, 'interval order')
    return ((lo.numerator * Q) // lo.denominator,
            ceildiv(hi.numerator * Q, hi.denominator))


def bounds(a):
    return F(a[0], Q), F(a[1], Q)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products)//Q, -((-max(products))//Q)


def div_int(a, n):
    require(type(n) is int and n > 0, 'positive integer divisor')
    return a[0]//n, -((-a[1])//n)


def scale(a, x):
    """Multiply by an exact rational, without first rounding the weight."""
    x = F(x)
    low, high = (a[0]*x.numerator, a[1]*x.numerator)
    if low > high:
        low, high = high, low
    return low//x.denominator, -((-high)//x.denominator)


def square(a):
    low = 0 if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    high = max(a[0]*a[0], a[1]*a[1])
    return low//Q, -((-high)//Q)


def sqrt_fraction(x):
    x = F(x)
    require(x >= 0, 'nonnegative square root')
    numerator = x.numerator*Q*Q
    q = isqrt(numerator//x.denominator)
    return q, q if q*q*x.denominator == numerator else q+1


def sqrt_interval(a):
    require(a[0] >= 0, 'nonnegative square root interval')
    return sqrt_fraction(F(a[0], Q))[0], sqrt_fraction(F(a[1], Q))[1]


def join(real, imag):
    return real[0], real[1], imag[0], imag[1]


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3]


def cneg(a):
    return -a[1], -a[0], -a[3], -a[2]


def csub(a, b):
    return cadd(a, cneg(b))


def conj(a):
    return a[0], a[1], -a[3], -a[2]


def cmul(a, b):
    arbr = mul(a[:2], b[:2])
    aibi = mul(a[2:], b[2:])
    arbi = mul(a[:2], b[2:])
    aibr = mul(a[2:], b[:2])
    return join(sub(arbr, aibi), add(arbi, aibr))


def cscale(a, x):
    return join(scale(a[:2], x), scale(a[2:], x))


def cdiv_int(a, n):
    return join(div_int(a[:2], n), div_int(a[2:], n))


def abs2(a):
    return add(square(a[:2]), square(a[2:]))


def clipped(a, low, high):
    out = max(a[0], low*Q), min(a[1], high*Q)
    require(out[0] <= out[1], 'empty analytic intersection')
    return out


def configure_integer_text():
    # Guarded scalar midpoint denominator <=2^193, numerator <=2^199.
    # A degree-257 remainder numerator/denominator needs <15504 decimal
    # digits; the explicit finite cap also covers radius plus remainder.
    require(hasattr(sys, 'set_int_max_str_digits'), 'PYTHON_3_11_OR_LATER_REQUIRED')
    sys.set_int_max_str_digits(INTEGER_TEXT_DIGITS)


def scalar_certificate(argument, phase):
    lo, hi = bounds(argument)
    c, radius = (lo+hi)/2, (hi-lo)/2
    require(max(abs(lo), abs(hi)) <= 64 if phase else 0 <= lo <= hi <= 64,
            'SCALAR_DOMAIN')
    error = radius + abs(c)**(N+1)/factorial(N+1)
    if phase:
        real, imag, tr, ti = F(1), F(0), F(1), F(0)
        for k in range(1, N+1):
            tr, ti = -ti*c/k, tr*c/k
            real, imag = real+tr, imag+ti
        value = join(clipped(grid(real-error, real+error), -1, 1),
                     clipped(grid(imag-error, imag+error), -1, 1))
    else:
        value = term = F(1)
        for k in range(1, N+1):
            term *= -c/k
            value += term
        value = clipped(grid(value-error, value+error), 0, 1)
    return value, {'midpoint': str(c), 'radius': str(radius),
                   'degree': N, 'remainder': str(error-radius),
                   'coordinate_error': str(error)}


def validate_scalar_bound(argument, phase, record):
    lo, hi = bounds(argument)
    c, r = (lo+hi)/2, (hi-lo)/2
    require(max(abs(lo), abs(hi)) <= 64 if phase else 0 <= lo <= hi <= 64,
            'SCALAR_DOMAIN')
    require(record['degree'] == N and F(record['midpoint']) == c and F(record['radius']) == r,
            'scalar certificate context')
    require(F(record['remainder']) >= abs(c)**257/factorial(257)
            and F(record['coordinate_error']) >= r+F(record['remainder']),
            'understated elementary remainder')


def graded_basis(modes=7, cutoff=L):
    def grade(total, count):
        if count == 1:
            yield (total,)
        else:
            for first in range(total+1):
                for rest in grade(total-first, count-1):
                    yield (first,)+rest
    return tuple(nu for total in range(cutoff+1) for nu in grade(total, modes))


def ladder_edges(basis, cutoff=L):
    index = {nu: i for i, nu in enumerate(basis)}
    lower, upper = [], []
    for source, nu in enumerate(basis):
        for mode, n in enumerate(nu):
            if n:
                dest = list(nu)
                dest[mode] -= 1
                lower.append((source, index[tuple(dest)], mode, n))
            if sum(nu) < cutoff:
                dest = list(nu)
                dest[mode] += 1
                upper.append((source, index[tuple(dest)], mode, n+1))
    return tuple(lower), tuple(upper)


def coefficients(delta, cutoff=L):
    roots = [sqrt_fraction(n) for n in range(cutoff+1)]
    up = tuple(tuple(join(mul(z[:2], root), mul(z[2:], root))
                     for root in roots) for z in delta)
    down = tuple(tuple(cneg(conj(z)) for z in row) for row in up)
    return down, up


def ladder(vector, edges, coeff):
    out = [CZ]*len(vector)
    for source, dest, mode, n in edges:
        # Only mathematical zero is skipped; all nonzero components survive.
        if vector[source] != CZ:
            out[dest] = cadd(out[dest], cmul(coeff[mode][n], vector[source]))
    return out


def polynomial(vector, edges, coeff, cutoff=L):
    term, total = list(vector), list(vector)
    for degree in range(1, cutoff+1):
        term = [cdiv_int(z, degree) for z in ladder(term, edges, coeff)]
        total = [cadd(a, b) for a, b in zip(total, term)]
    return total


def normal_ordered(vector, edges, coeff, cutoff=L):
    lowered = polynomial(vector, edges[0], coeff[0], cutoff)
    return polynomial(lowered, edges[1], coeff[1], cutoff)


def inner(bra, ket):
    require(len(bra) == len(ket), 'inner product dimensions')
    out = CZ
    for b, a in zip(bra, ket):
        out = cadd(out, cmul(conj(b), a))
    return out


def binary64_rational(bits):
    require(type(bits) is int and 0 <= bits < (1 << 64), 'binary64 bits')
    exponent, significand = (bits >> 52) & 2047, bits & ((1 << 52)-1)
    require(exponent != 2047, 'NONFINITE_PAYLOAD')
    if exponent:
        significand += 1 << 52
        shift = exponent-1023-52
    else:
        shift = -1074
    if bits >> 63:
        significand = -significand
    return F(significand << shift) if shift >= 0 else F(significand, 1 << -shift)


def decode_vector(raw, dimension=DIM):
    require(len(raw) == dimension*16, 'TRUNCATED_OR_TRAILING_VECTOR')
    return [join(grid(binary64_rational(a)), grid(binary64_rational(b)))
            for a, b in struct.iter_unpack('<QQ', raw)]


def strict_pairs(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def load_json(path):
    def invalid(value):
        raise Rejected('nonfinite JSON token '+value)
    obj = json.loads(path.read_bytes(), object_pairs_hook=strict_pairs,
                     parse_constant=invalid)
    def finite(x):
        if type(x) is float:
            require(isfinite(x), 'nonfinite JSON numeric overflow')
        elif type(x) is dict:
            for v in x.values():
                finite(v)
        elif type(x) is list:
            for v in x:
                finite(v)
    finite(obj)
    return obj


def number_interval(value):
    require(type(value) is list and len(value) == 2, 'real interval shape')
    lo, hi = map(rational, value)
    require(lo <= hi, 'real interval order')
    return grid(lo, hi)


def complex_interval(value):
    require(type(value) is list and len(value) == 2, 'complex interval shape')
    return join(number_interval(value[0]), number_interval(value[1]))


def compare(new, old):
    # The old box must not be widened before a whole-box containment claim.
    require(type(old) is list and len(old) == 2 and
            all(type(a) is list and len(a) == 2 for a in old), 'old rectangle shape')
    old = tuple(rational(x) for a in old for x in a)
    require(old[0] <= old[1] and old[2] <= old[3], 'old rectangle order')
    new = tuple(F(x, Q) for x in new)
    if new[1] < old[0] or old[1] < new[0] or new[3] < old[2] or old[3] < new[2]:
        return 'CONFLICT'
    if old[0] <= new[0] <= new[1] <= old[1] and old[2] <= new[2] <= new[3] <= old[3]:
        return 'COVERED'
    return 'NOT_DECIDED'


def witness(retained, linear, numerical, thermal):
    numerical, thermal = F(numerical), F(thermal)
    require(numerical >= 0 and thermal >= TAIL/2, 'inherited radius domain')
    center = scale(sqrt_interval(abs2(csub(retained, linear))), F(1, 2))
    lo, hi = bounds(center)
    halfwidth = (hi-lo)/2
    total = numerical+thermal+halfwidth
    lower, upper = max(F(0), lo-numerical-thermal), min(F(1), hi+numerical+thermal)
    require(lower <= upper, 'inconsistent physical inherited account')
    return {'center': [str(lo), str(hi)], 'center_midpoint': str((lo+hi)/2),
            'arithmetic_halfwidth': str(halfwidth), 'numerical_radius': str(numerical),
            'thermal_radius': str(thermal), 'total_radius': str(total),
            'distance': [str(lower), str(upper)], 'precision_goal_pass': total <= THRESHOLD,
            'discrepancy': 'EXCEEDS_TARGET' if lower > THRESHOLD else
                           'WITHIN_TARGET' if upper <= THRESHOLD else 'UNRESOLVED'}


def pair_parameters(branch_a, branch_b):
    alpha_a = [complex_interval(z) for z in branch_a['linear_alpha']]
    alpha_b = [complex_interval(z) for z in branch_b['linear_alpha']]
    require(len(alpha_a) == len(alpha_b) == 7, 'parameter mode count')
    delta = [csub(a, b) for a, b in zip(alpha_a, alpha_b)]
    theta = sub(number_interval(branch_a['linear_phase']), number_interval(branch_b['linear_phase']))
    norm = ZERO
    for a, b, d in zip(alpha_a, alpha_b, delta):
        theta = add(theta, cmul(conj(b), a)[2:])
        norm = add(norm, abs2(d))
    gaussian, gaussian_bound = scalar_certificate(scale(norm, F(1, 2)), False)
    thermal, thermal_bound = scalar_certificate(scale(norm, F(11, 20)), False)
    phase, phase_bound = scalar_certificate(theta, True)
    return delta, gaussian, phase, cmul(phase, join(thermal, ZERO)), {
        'gaussian': gaussian_bound, 'thermal': thermal_bound, 'phase': phase_bound}


def artifact(path, expected):
    require(path.is_file() and not path.is_symlink(), 'regular input file required')
    size, checksum = expected
    require(path.stat().st_size == size, 'input byte count: '+path.name)
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            digest.update(block)
    require(digest.hexdigest() == checksum, 'input SHA-256: '+path.name)
    return {'bytes': size, 'sha256': checksum}


def exact_type_match(actual, expected):
    """Python's True == 1 is not an admitted schema equality."""
    if type(actual) is not type(expected):
        return False
    if type(expected) is list:
        return len(actual) == len(expected) and all(exact_type_match(a, b) for a, b in zip(actual, expected))
    if type(expected) is dict:
        return actual.keys() == expected.keys() and all(exact_type_match(actual[k], v) for k, v in expected.items())
    return actual == expected


def field_contract(obj, fixed):
    require(type(obj) is dict, 'object required')
    for key, value in fixed.items():
        require(key in obj and exact_type_match(obj[key], value), 'metadata field: '+key)


def validate_weights(saved, weights):
    require(type(saved) is list and len(saved) == len(weights), 'thermal weight inventory')
    for weight, enclosure in zip(weights, saved):
        require(type(enclosure) is list and len(enclosure) == 2, 'thermal enclosure shape')
        lo, hi = map(rational, enclosure)
        require(0 <= lo <= weight <= hi, 'wrong thermal weight')


def source_binding():
    path = Path(__file__).resolve().with_name('INPUT_BINDING.json')
    require(hashlib.sha256(path.read_bytes()).hexdigest() == BINDING_SHA256, 'input binding changed')
    binding = load_json(path)
    field_contract(binding, {'campaign_source_pin': CAMPAIGN_PIN,
                            'final_time_seconds_rational': [1, 2000], 'scope': SCOPE})
    require(binding['serialized_input'] == {'bytes': SERIALIZED_INPUT[0], 'sha256': SERIALIZED_INPUT[1]},
            'serialized binding changed')
    return binding


def source_receipts():
    source = Path(__file__).resolve().parent
    raw = (source/'SOURCE_SHA256SUMS').read_bytes()
    records = {}
    for line in raw.decode('ascii').splitlines():
        checksum, name = line.split('  ')
        require(name in SOURCE_NAMES and name not in records and len(checksum) == 64,
                'source manifest inventory')
        payload = (source/name).read_bytes()
        require(hashlib.sha256(payload).hexdigest() == checksum, 'source changed: '+name)
        records[name] = {'bytes': len(payload), 'sha256': checksum}
    require(set(records) == SOURCE_NAMES, 'incomplete accepted source inventory')
    records['SOURCE_SHA256SUMS'] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    return records


def validate_payloads(campaign):
    """Read-only binding to the frozen serialized-input and custody receipts."""
    require(SERIALIZED_INPUT is not None, 'UNBOUND_SERIALIZED_INPUT')
    state = campaign/'full-state'
    receipts = {name: artifact(state/name, value) for name, value in PAYLOADS.items()}
    for name, value in CUSTODY.items():
        artifact(campaign/name, value)
    input_receipt = artifact(campaign/'exact_input.txt', SERIALIZED_INPUT)
    binding = source_binding()
    custody = load_json(campaign/'final-custody.json')
    require(custody.get('status') == 'PASS' and custody.get('input') == input_receipt,
            'serialized input/final-custody association')
    require(custody.get('pins') == binding['source_pins'], 'source manifest/custody association')
    inventory = load_json(campaign/'artifact-inventory.json')
    require(inventory.get('complete') is True and inventory.get('errors') == [], 'closed inventory')
    require(all(inventory['files'].get(name) == rec for name, rec in receipts.items()),
            'endpoint inventory association')
    require((state/'result.json').read_bytes() == (campaign/'full.stdout').read_bytes(),
            'final result/stdout association')
    require((campaign/'full.stderr').read_bytes() == b'', 'original stderr')
    summary = load_json(campaign/'summary.json')
    require(summary.get('status') in ('COMPLETE_PRECISION_GOAL_MET', 'COMPLETE_PRECISION_UNRESOLVED')
            and summary.get('custody_verified') is True and summary.get('first_outcome_preserved') is True
            and summary.get('retry_or_resume_performed') is False, 'closed campaign summary')
    basis = graded_basis()
    saved_basis = load_json(state/'basis.json')
    field_contract(saved_basis, {'scope': SCOPE, 'cutoff': 8, 'guard': 10, 'thermal_cutoff': 3,
                                'occupations': [list(nu) for nu in basis]})
    require(len(basis) == DIM and sum(sum(nu) <= 3 for nu in basis) == COLS, 'independent basis size')
    weights = [F(20, 21)**7 * F(1, 21)**sum(nu) for nu in basis[:COLS]]
    require(sum(weights) == RETAINED, 'exact retained thermal mass')
    meta, result = load_json(state/'metadata.json'), load_json(state/'result.json')
    fixed = {'scope': SCOPE, 'cutoff': 8, 'dimension': DIM, 'thermal_columns': COLS,
             'thermal_cutoff': 3, 'cases': 6, 'final_time_seconds_rational': [1, 2000],
             'reset_between_checkpoints': False, 'normalization_applied': False, 'phase_fit_applied': False}
    field_contract(meta, fixed)
    field_contract(result, fixed)
    field_contract(result, {'status': 'COMPLETED', 'full_trajectory_certificate': True,
                            'final_coherences_computed': True})
    validate_weights(meta['thermal_weights'], weights)
    require(len(result['branches']) == len(result['pair_coherences']) == 6, 'six branches and pairs')
    for case, branch in enumerate(result['branches']):
        field_contract(branch, {'case': case, 'labels': list(LABELS[case % 3])})
        require(len(branch['columns']) == COLS and len(branch['linear_alpha']) == 7, 'branch inventory')
    for pair, identity in zip(result['pair_coherences'], PAIRS):
        field_contract(pair, {'cases': list(identity)})
    return basis, weights, result, receipts


def restore_pair(state, pair_index, basis, weights, result, check_budget=lambda: None,
                 completed=lambda column: None):
    """All 120 columns; no column subset or precision knob is accepted."""
    a, b = PAIRS[pair_index]
    delta, gaussian, phase, linear, scalar_bounds = pair_parameters(result['branches'][a], result['branches'][b])
    edges = ladder_edges(basis)
    coeff = coefficients(delta)
    total = CZ
    width = DIM*16
    with (state/'endpoints.bin').open('rb') as stream_a, (state/'endpoints.bin').open('rb') as stream_b:
        stream_a.seek(a*COLS*width)
        stream_b.seek(b*COLS*width)
        for r in range(COLS):
            check_budget()
            ket = decode_vector(stream_a.read(width))
            bra = decode_vector(stream_b.read(width))
            value = inner(bra, normal_ordered(ket, edges, coeff))
            total = cadd(total, cscale(value, weights[r]))
            completed(r)
    retained = cmul(phase, cmul(join(gaussian, ZERO), total))
    old = result['pair_coherences'][pair_index]
    account = witness(retained, linear, rational(old['numerical_radius']), rational(old['thermal_radius']))
    return {'cases': [a, b], 'overlaps': COLS, 'retained_grid': list(retained),
            'linear_grid': list(linear), 'grid_denominator': str(Q), 'scalar_bounds': scalar_bounds,
            'old_retained_comparison': compare(retained, old['sine_retained_interval']),
            'old_linear_comparison': compare(linear, old['linear_full_interval']), 'account': account}


def coefficient_controls():
    """Exact B1/B2 comparison in f_n=sqrt(n!)|n>, no numerical square roots."""
    def zmul(a, b):
        return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
    def zadd(a, b):
        return a[0]+b[0], a[1]+b[1]
    def zscale(a, x):
        return a[0]*x, a[1]*x
    def zpow(a, n):
        out = (F(1), F(0))
        for _ in range(n):
            out = zmul(out, a)
        return out
    d, lower = (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5))
    count = 0
    for initial in range(9):
        v = [(F(0), F(0))]*9
        v[initial] = (F(1), F(0))
        for raising in (False, True):
            term, accum = list(v), list(v)
            for k in range(1, 9):
                fresh = [(F(0), F(0))]*9
                for n in range(9):
                    dest = n+1 if raising else n-1
                    if 0 <= dest <= 8:
                        fresh[dest] = zscale(zmul(d if raising else lower, term[n]), F(1 if raising else n, k))
                term = fresh
                accum = [zadd(a, b) for a, b in zip(accum, term)]
            v = accum
        for final in range(9):
            expected = (F(0), F(0))
            for ell in range(min(final, initial)+1):
                scalar = F(factorial(initial), factorial(ell)*factorial(final-ell)*factorial(initial-ell))
                expected = zadd(expected, zscale(zmul(zpow(d, final-ell), zpow(lower, initial-ell)), scalar))
            require(v[final] == expected, 'B1/B2 factorial-basis coefficient mismatch')
            count += 1
    return count


def controls():
    """Invoke only under the complete accepted public source pin."""
    configure_integer_text()
    require(coefficient_controls() == 81, 'coefficient coverage')
    small_basis = graded_basis(1, 1)
    edges = ladder_edges(small_basis, 1)
    zero_coeff = coefficients([CZ], 1)
    nonunit = [cscale(CO, 2), CZ]
    require(normal_ordered(nonunit, edges, zero_coeff, 1) == nonunit, 'zero displacement/nonunit preservation')
    require(inner(nonunit, nonunit) == cscale(CO, 4), 'nonunit Gram value')
    d = join(grid(F(3, 8)), grid(F(4, 8)))
    transformed = [normal_ordered(v, edges, coefficients([d], 1), 1) for v in ([CO, CZ], [CZ, CO])]
    # All these ladder coefficients and targets are exactly dyadic.
    targets = ((CO, d), (cneg(conj(d)), csub(CO, join(abs2(d), ZERO))))
    for column, target in zip(transformed, targets):
        for actual, expected in zip(column, target):
            require(actual[0] <= expected[0] <= expected[1] <= actual[1]
                    and actual[2] <= expected[2] <= expected[3] <= actual[3], 'vacuum/one-excitation coefficient')
    reverse = [normal_ordered(v, edges, coefficients([cneg(d)], 1), 1)
               for v in ([CO, CZ], [CZ, CO])]
    for col in range(2):
        for row in range(2):
            require(transformed[col][row] == conj(reverse[row][col]), 'adjoint convention')
    va, vb = [CO, cscale(CO, 2)], [d, CO]
    forward = inner(vb, normal_ordered(va, edges, coefficients([d], 1), 1))
    backward = inner(va, normal_ordered(vb, edges, coefficients([cneg(d)], 1), 1))
    require(forward == conj(backward), 'swapped branches and conjugated bra')
    plus, _ = scalar_certificate(grid(1), True)
    minus, _ = scalar_certificate(grid(-1), True)
    require(plus == conj(minus) and plus[2] > minus[3], 'phase/intentional wrong Weyl sign')
    zero_alpha = [[0, 0], [0, 0]]
    branch_a = {'linear_alpha': [[[1, 1], [1, 1]]]+[zero_alpha]*6, 'linear_phase': [0, 0]}
    branch_b = {'linear_alpha': [[[1, 1], [0, 0]]]+[zero_alpha]*6, 'linear_phase': [0, 0]}
    # Im(conj(1)*(1+i))=+1; reversing branches gives -1.
    da, ga, pa, la, sa = pair_parameters(branch_a, branch_b)
    db, gb, pb, lb, sb = pair_parameters(branch_b, branch_a)
    require(pa == plus and pb == minus and pa == conj(pb) and ga == gb
            and la == conj(lb) and da == [cneg(z) for z in db], 'actual Weyl sign and pair swap')
    ep0, record = scalar_certificate(ZERO, False)
    require(ep0 == ONE and F(record['coordinate_error']) == 0, 'zero scalar')
    _, record = scalar_certificate(grid(1), True)
    needed = F(1, factorial(257))
    validate_scalar_bound(grid(1), True, record)
    bad = dict(record, remainder=str(needed/2))
    try:
        validate_scalar_bound(grid(1), True, bad)
    except Rejected:
        pass
    else:
        raise Rejected('understated remainder negative control did not fail')
    _, long_record = scalar_certificate((Q-1, Q-1), True)
    validate_scalar_bound((Q-1, Q-1), True, long_record)
    require(sum(F(20, 21)**7*F(1, 21)**sum(nu) for nu in graded_basis()[:120]) == RETAINED,
            'unequal unnormalized thermal weights')
    require(RETAINED != 1 and not exact_type_match(True, 1), 'weight normalization/type trap')
    fixture_weights = [F(1, 2), F(1, 4)]
    validate_weights([[0.5, 0.5], [0.25, 0.25]], fixture_weights)
    for wrong in ([[0.5, 0.5], [0.5, 0.5]], [[1, 1], [0, 0]], [[True, True], [0.25, 0.25]]):
        try:
            validate_weights(wrong, fixture_weights)
        except Rejected:
            pass
        else:
            raise Rejected('wrong/normalized thermal weights negative control did not fail')
    small_saved = {'occupations': [list(nu) for nu in small_basis]}
    try:
        field_contract(small_saved, {'occupations': [list(nu) for nu in reversed(small_basis)]})
    except Rejected:
        pass
    else:
        raise Rejected('reordered basis negative control did not fail')
    for bits in (0x7ff0000000000000, 0x7ff8000000000000, 0xfff0000000000000):
        try:
            binary64_rational(bits)
        except Rejected:
            pass
        else:
            raise Rejected('nonfinite negative control did not fail')
    require(binary64_rational(1) == F(1, 1 << 1074), 'subnormal exact decoding')
    for raw in (b'\0'*15, b'\0'*17):
        try:
            decode_vector(raw, 1)
        except Rejected:
            pass
        else:
            raise Rejected('truncated/trailing negative control did not fail')
    for operation in (lambda: number_interval([False, 1]),
                      lambda: strict_pairs([('a', 1), ('a', 2)])):
        try:
            operation()
        except Rejected:
            pass
        else:
            raise Rejected('type/duplicate-key negative control did not fail')
    test = witness(join(grid(F(1, 4), F(1, 2)), ZERO), CZ, F(1, 100), TAIL/2)
    center_lo, center_hi = map(F, test['center'])
    require(F(test['distance'][1]) == center_hi+F(1, 100)+TAIL/2
            and F(test['total_radius']) == F(1, 100)+TAIL/2+(center_hi-center_lo)/2,
            'center uncertainty counted once')
    return {'coefficient_equalities': 81, 'status': 'CONTROLS_PASSED'}


def limited_process(mebibytes):
    require(sys.platform == 'linux', 'LINUX_RESOURCE_LIMITS_REQUIRED')
    import resource
    amount = mebibytes*1024*1024
    resource.setrlimit(resource.RLIMIT_AS, (amount, amount))


def worker(state, index, basis, weights, result, deadline, messages):
    """Fixed pair worker. Exceptions become bounded records, not silent loss."""
    # The parent blocks these signals only during fork+registration. Children
    # restore ordinary termination before unblocking pending signals.
    for sig in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_UNBLOCK, {signal.SIGALRM, signal.SIGTERM, signal.SIGINT})
    try:
        limited_process(WORKER_MIB)
        def budget():
            require(time.monotonic() < deadline, 'TIME_LIMIT')
        def complete(column):
            budget()
            messages.put(('overlap', index, column))
        row = restore_pair(Path(state), index, basis, weights, result, budget, complete)
        budget()
        messages.put(('result', index, row))
    except BaseException as exc:
        messages.put(('failure', index, failure_description(exc)))


def bounded_invocation(campaign):
    """Accepted runner; one invocation, no retry, fixed six workers.

    The sum of address-space ceilings is 256 + 6*256 = 1792 MiB.
    The entry point requires the exact clean public candidate checkout.
    """
    started = time.monotonic()
    deadline = started+SECONDS
    limited_process(PARENT_MIB)
    configure_integer_text()
    processes, slots, pairs, failures = [], set(), {}, []
    report = {'status': 'NOT_CERTIFIED', 'new_restoration': 'INCOMPLETE',
              'old_rectangle_comparison': 'NOT_PERFORMED', 'action_layer': 'L1',
              'branch_parameter_intervals_valid': 'PREMISE', 'propagation_account': 'INHERITED_PREMISE',
              'precision_bits': P, 'scalar_degree': N, 'required_overlaps': 720,
              'required_pairs': 6, 'completed_overlaps': 0, 'complete_pairs': [],
              'attempts': 1, 'propagation_performed': False, 'normalization_applied': False,
              'phase_fit_applied': False, 'retry_or_resume_performed': False}
    def expired(signum, frame):
        raise Rejected('TIME_LIMIT')
    old_handlers = {sig: signal.signal(sig, expired)
                    for sig in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT)}
    signal.setitimer(signal.ITIMER_REAL, SECONDS)
    try:
        source_before = source_receipts()
        report['source_receipts'] = source_before
        basis, weights, result, receipts = validate_payloads(campaign)
        report['input_receipts'] = receipts
        report['controls'] = controls()
        require(time.monotonic() < deadline, 'TIME_LIMIT')
        # Linux fork creates no resource-tracker helper; only the parent and
        # exactly six limited worker processes contribute to the 2-GiB sum.
        ctx = multiprocessing.get_context('fork')
        messages = ctx.Queue()
        for index in range(WORKERS):
            process = ctx.Process(target=worker, args=(str(campaign/'full-state'), index,
                                 basis, weights, result, deadline, messages))
            # A deadline/interrupt cannot leave a just-forked worker outside
            # the cleanup inventory. Pending signals run after registration.
            mask = signal.pthread_sigmask(signal.SIG_BLOCK,
                                          {signal.SIGALRM, signal.SIGTERM, signal.SIGINT})
            try:
                process.start()
                processes.append(process)
            finally:
                signal.pthread_sigmask(signal.SIG_SETMASK, mask)
            require(time.monotonic() < deadline, 'TIME_LIMIT')
        while len(pairs) < 6:
            remaining = deadline-time.monotonic()
            require(remaining > 0, 'TIME_LIMIT')
            try:
                kind, index, value = messages.get(timeout=min(remaining, 1))
            except queue.Empty:
                require(all(p.exitcode in (None, 0) for p in processes), 'WORKER_EXIT')
                require(any(p.is_alive() for p in processes), 'MISSING_WORKER_OUTPUT')
                continue
            require(type(index) is int and 0 <= index < 6, 'worker identity')
            if kind == 'overlap':
                require(type(value) is int and 0 <= value < COLS and (index, value) not in slots,
                        'overlap identity or duplicate')
                slots.add((index, value))
            elif kind == 'result':
                require(index not in pairs and value['cases'] == list(PAIRS[index]) and value['overlaps'] == COLS,
                        'pair identity or coverage')
                pairs[index] = value
            else:
                raise Rejected('WORKER_FAILURE: '+str(value))
        require(slots == {(i, r) for i in range(6) for r in range(COLS)}, 'INCOMPLETE_720_COVERAGE')
        for process in processes:
            process.join(timeout=max(0, deadline-time.monotonic()))
            require(process.exitcode == 0, 'WORKER_EXIT')
        # Rehash original inputs after evaluation; no mutation is silently accepted.
        validate_payloads(campaign)
        require(source_receipts() == source_before, 'source changed during invocation')
        require(time.monotonic() < deadline, 'TIME_LIMIT')
        report['status'] = 'CONDITIONAL_RESTORATION_COMPLETE'
        report['new_restoration'] = 'ALL_720_OVERLAPS_ENCLOSED'
        report['old_rectangle_comparison'] = 'PER_PAIR_SEPARATE_DIAGNOSTICS'
    except BaseException as exc:
        report['status'] = 'NOT_CERTIFIED'
        report['new_restoration'] = 'INCOMPLETE'
        report['old_rectangle_comparison'] = 'INCOMPLETE_PER_PAIR_ONLY'
        failures.append(failure_description(exc))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        # Cleanup is non-scientific and must not be interrupted by a repeated
        # user signal. Kill remains available to an external supervisor.
        for sig in (signal.SIGALRM, signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, signal.SIG_IGN)
        # Cleanup adds no scientific work, and cannot convert a failure to success.
        for process in processes:
            if process.is_alive():
                process.terminate()
        for process in processes:
            process.join(timeout=1)
            if process.is_alive():
                process.kill()
                process.join(timeout=1)
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)
        report['completed_overlaps'] = len(slots)
        report['complete_pairs'] = [pairs[k] for k in sorted(pairs)]
        report['failures'] = failures
        report['wall_seconds'] = time.monotonic()-started
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--campaign', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--candidate', required=True)
    args = parser.parse_args()
    require(args.campaign.is_absolute() and args.output.is_absolute(), 'absolute paths required')
    campaign, output = args.campaign.resolve(), args.output.resolve()
    root = Path(__file__).resolve().parents[2]
    require(campaign.is_dir() and output != campaign and campaign not in output.parents,
            'output must be outside the original campaign')
    require(output != root and root not in output.parents, 'output must be outside the source checkout')
    require(len(args.candidate) == 40 and all(c in '0123456789abcdef' for c in args.candidate),
            'full lowercase candidate commit required')
    require(subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip() == args.candidate,
            'candidate checkout mismatch')
    require(not subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=all'], cwd=root).strip(),
            'clean accepted source checkout required')
    # Exclusive output creation is the attempt guard. Existing first evidence
    # is never overwritten. No output path is obtained from campaign metadata.
    output.mkdir(parents=True, exist_ok=False)
    start = datetime.now(timezone.utc).isoformat()
    (output/'attempt.json').write_text(json.dumps({'candidate': args.candidate, 'started_utc': start,
                        'attempts': 1, 'scope': SCOPE}, sort_keys=True)+'\n', encoding='ascii')
    try:
        report = bounded_invocation(campaign)
    except BaseException as exc:
        report = {'status': 'NOT_CERTIFIED', 'new_restoration': 'INCOMPLETE',
                  'old_rectangle_comparison': 'NOT_PERFORMED', 'completed_overlaps': 0,
                  'failures': [failure_description(exc)]}
    wall = report.pop('wall_seconds', None)
    payload = (json.dumps(report, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode('ascii')
    with (output/'result.json').open('xb') as stream:
        stream.write(payload)
    record = {'candidate': args.candidate, 'started_utc': start,
              'ended_utc': datetime.now(timezone.utc).isoformat(), 'wall_seconds': wall,
              'platform': platform.system(), 'architecture': platform.machine(),
              'python': platform.python_version(), 'result_bytes': len(payload),
              'result_sha256': hashlib.sha256(payload).hexdigest(), 'attempts': 1,
              'exit_code': 0 if report['status'] == 'CONDITIONAL_RESTORATION_COMPLETE' else 2,
              'inputs_written_by_this_program': False, 'propagation_performed': False}
    with (output/'run.json').open('x', encoding='ascii', newline='\n') as stream:
        json.dump(record, stream, sort_keys=True, indent=2)
        stream.write('\n')
    sys.stdout.write(payload.decode('ascii'))
    return record['exit_code']


if __name__ == '__main__':
    raise SystemExit(main())
