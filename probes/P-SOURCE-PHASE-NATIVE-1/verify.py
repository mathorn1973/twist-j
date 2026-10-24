#!/usr/bin/env python3
"""Exact finite audit of the declared source, phase and native bridge.

Fresh self-contained transcription of the displayed equations. Mathematical
inputs were available during preparation; this is not a blind experiment or
an independent external proof. No project imports, files, network or floats.
General all-time claims require the accompanying algebraic proofs.
"""

from fractions import Fraction
from itertools import product
import sys


def require(condition, label):
    if not condition:
        raise AssertionError(label)


# O = Z[t]/(t^8-t^6+t^4-t^2+1), in the ordered power basis 1,...,t^7.
ZERO = (0,) * 8
ONE = (1,) + (0,) * 7


def integer(n):
    return (n,) + (0,) * 7


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def times_integer(a, n):
    return tuple(n * x for x in a)


def multiply(a, b):
    work = [0] * 15
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            work[j + k] += x * y
    for k in range(14, 7, -1):
        x = work[k]
        work[k - 2] += x
        work[k - 4] -= x
        work[k - 6] += x
        work[k - 8] -= x
    return tuple(work[:8])


T_ROOT = (0, 1, 0, 0, 0, 0, 0, 0)
POWERS = [ONE]
for _ in range(20):
    POWERS.append(multiply(POWERS[-1], T_ROOT))
I = POWERS[5]
ZETA = POWERS[4]
CONTACT = POWERS[16]
P = plus(ONE, times_integer(I, 2))
P2 = multiply(P, P)


def star(a):
    result = ZERO
    for k, coefficient in enumerate(a):
        result = plus(result, times_integer(POWERS[(-k) % 20], coefficient))
    return result


def rho(a, place):
    return sum(coefficient * pow(place, k, 5)
               for k, coefficient in enumerate(a)) % 5


def ring_sum(values):
    result = ZERO
    for value in values:
        result = plus(result, value)
    return result


M = ((ONE, times_integer(I, 2)), (times_integer(I, 2), ONE))
COIN = tuple(tuple(multiply(M[a // 2][b // 2], M[a % 2][b % 2])
                   for b in range(4)) for a in range(4))
H = (1, -1, -1, 1)
DISPLACEMENTS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def check_ring_and_grams():
    require(POWERS[20] == ONE, "t^20")
    require(multiply(I, I) == integer(-1), "i^2")
    require(multiply(P, star(P)) == integer(5), "p norm")
    require(multiply(CONTACT, star(CONTACT)) == ONE, "contact norm")
    for a in POWERS[:8]:
        require(star(star(a)) == a, "star involution")
        for b in POWERS[:8]:
            require(star(multiply(a, b)) == multiply(star(b), star(a)),
                    "star product on basis")
            for place in (2, 3):
                require(rho(multiply(a, b), place)
                        == rho(a, place) * rho(b, place) % 5,
                        "residue product on basis")
    for place in (2, 3):
        require((place ** 8 - place ** 6 + place ** 4 - place ** 2 + 1) % 5 == 0,
                "Phi20 residue place")
        require(rho(I, place) == place and rho(ZETA, place) == 1,
                "residue i and zeta")
    require(rho(P, 2) == 0 and rho(P2, 3) == 4, "phase residue places")
    for a, b in product(range(4), repeat=2):
        require(rho(COIN[a][b], 2) == H[a] * H[b] % 5, "rank one rho2")
        require(rho(COIN[a][b], 3) == 1, "rank one rho3")
    for retained_phase, gain in ((False, 25), (True, 625)):
        matrix = tuple(tuple(multiply(P2, x) if retained_phase else x for x in row)
                       for row in COIN)
        for a, b in product(range(4), repeat=2):
            target = integer(gain if a == b else 0)
            require(ring_sum(multiply(star(matrix[k][a]), matrix[k][b])
                             for k in range(4)) == target, "column Gram")
            require(ring_sum(multiply(matrix[a][k], star(matrix[b][k]))
                             for k in range(4)) == target, "row Gram")


def clean_ring(field):
    return {key: value for key, value in field.items() if value != ZERO}


def raw_step(field, retained_phase=False):
    output = {}
    for (r, s, b), value in field.items():
        for a, (dr, ds) in enumerate(DISPLACEMENTS):
            target = (r + dr, s + ds, a)
            contribution = multiply(COIN[a][b], value)
            if target[1] == 0:
                contribution = multiply(CONTACT, contribution)
            if retained_phase:
                contribution = multiply(P2, contribution)
            output[target] = plus(output.get(target, ZERO), contribution)
    return clean_ring(output)


def ring_norm(field):
    return ring_sum(multiply(star(value), value) for value in field.values())


def clean_five(field):
    return {key: value % 5 for key, value in field.items() if value % 5}


def residues(field, retained_phase=False):
    q, z = {}, {}
    for (r, s, c), amplitude in field.items():
        site = (r, s)
        value = rho(amplitude, 3 if retained_phase else 2)
        q[site] = q.get(site, 0) + (1 if retained_phase else H[c]) * value
        z[site] = z.get(site, 0) + (H[c] if retained_phase else 1) * value
    return clean_five(q), clean_five(z)


def adjacency(field, weight=4):
    result = {}
    for (r, s), value in field.items():
        for dr, ds in DISPLACEMENTS:
            target = (r + dr, s + ds)
            result[target] = result.get(target, 0) + weight * value
    return clean_five(result)


def check_residue_preparation():
    for retained_phase in (False, True):
        for q, z in product(range(5), repeat=2):
            alpha = 3 * (q + z) % 5
            beta = 3 * ((q - z) if retained_phase else (z - q)) % 5
            field = {(0, 0, 0): integer(alpha), (0, 0, 1): integer(beta)}
            read_q, read_z = residues(field, retained_phase)
            require(read_q.get((0, 0), 0) == q and read_z.get((0, 0), 0) == z,
                    "two-channel residue preparation")


SAMPLE_FIELDS = (
    {(0, 0, 0): ONE},
    {(0, 0, 2): ONE},
    {(0, -1, 2): T_ROOT, (0, 1, 1): plus(ONE, POWERS[3])},
    {(1, 0, 3): I, (-1, 1, 0): plus(integer(2), times_integer(T_ROOT, -1))},
    {(0, 0, c): POWERS[c] for c in range(4)},
    {(0, 2, 1): integer(-2), (0, 0, 0): P},
    {},
    {(0, 0, 0): integer(5)},
)


def check_local_raw():
    require(raw_step(SAMPLE_FIELDS[1])[(0, 1, 2)] == ONE,
            "contact is not applied before departure")
    require(raw_step(SAMPLE_FIELDS[2])[(0, 0, 2)] == multiply(CONTACT, T_ROOT),
            "contact is applied on arrival")
    for initial in SAMPLE_FIELDS:
        for retained_phase in (False, True):
            field = initial
            gain = 625 if retained_phase else 25
            for _ in range(4):
                q, _ = residues(field, retained_phase)
                expected = {}
                for (r, s), value in q.items():
                    for c, (dr, ds) in enumerate(DISPLACEMENTS):
                        expected[(r + dr, s + ds, c)] = (
                            4 if retained_phase else H[c]) * value
                result = raw_step(field, retained_phase)
                actual = {site: rho(value, 3 if retained_phase else 2)
                          for site, value in result.items()}
                require(clean_five(actual) == clean_five(expected), "local port reduction")
                require(residues(result, retained_phase)[0]
                        == adjacency(q, 4 if retained_phase else 1), "local q reduction")
                require(ring_norm(result) == times_integer(ring_norm(field), gain),
                        "full local raw norm gain")
                require(raw_step(field, True)
                        == {key: multiply(P2, value)
                            for key, value in raw_step(field).items()}, "retained phase")
                field = result


def theta(n):
    return n.bit_count() % 2


def generator(index, x):
    a, b, c, d, q, r = x
    choices = ((b, a, d, c, q, r),
               (-c, -d, -a, -b, -q, -r),
               (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
               (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
               (2-a, 1-b, 3-c, 4-d, 2-q, 1-r))
    return tuple(value % 5 for value in choices[index])


def native_step(n, head):
    return generator((sum(head) + 2 * theta(n)) % 5, head)


def prefix(n, head):
    for tick in range(n):
        head = native_step(tick, head)
    return head


def summatory(m):
    return 0 if m == 0 else m - summatory(m // 2)


def chart(n, labels):
    alpha, beta, gamma, delta, epsilon = labels
    t = (-1) ** (n - 3)
    h = (-1) ** (n + theta(n - 1))
    offset = summatory((n - 1) // 2) - 1
    a, b = t * alpha, t * beta
    c, d = 2 + h * gamma, 1 + h * delta
    r = t * (epsilon + offset)
    q = 4 - 3 * theta(n - 1) - a - b - r
    return tuple(value % 5 for value in
                 (3*(a+c), 3*(b+d), 3*(a-c), 3*(b-d), q, r))


def read_chart(n, head):
    a, b, c, d, _, r = head
    t = (-1) ** (n - 3)
    h = (-1) ** (n + theta(n - 1))
    offset = summatory((n - 1) // 2) - 1
    return tuple(value % 5 for value in
                 (t*(a+c), t*(b+d), h*(a-c-2), h*(b-d-1), t*r-offset))


ANTECEDENT_WORDS = ((0, 2, 4), (3,), (4,), (3, 1, 3), (4, 1, 3))


def antecedent(z, target):
    for index in reversed(ANTECEDENT_WORDS[z]):
        target = generator(index, target)
    return target


CHART_TIMES = tuple(range(3, 16)) + (31, 32, 63, 64, 255, 256, 1023)


def check_native_exhaustive():
    heads = set()
    for labels in product(range(5), repeat=5):
        target = chart(3, labels)
        for z in range(5):
            head = antecedent(z, target)
            require(sum(head) % 5 == z, "antecedent initial sheet")
            require(prefix(3, head) == target, "antecedent F3")
            heads.add(head)
        for n in CHART_TIMES:
            head = chart(n, labels)
            require(read_chart(n, head) == labels, "chart inverse")
            require(native_step(n, head) == chart(n + 1, labels), "chart transport")
    require(len(heads) == 15625, "antecedents must exhaust all heads")


STATIC_LABELS = {(0, 0): (1, 2, 3, 4), (1, -1): (4, 0, 2, 1)}
ZERO_LABELS = (0,) * 5


def vacuum(n):
    if n < 3:
        return prefix(n, antecedent(0, chart(3, ZERO_LABELS)))
    return chart(n, ZERO_LABELS)


def projected_network(n, field, retained_phase, static_labels):
    q, z = residues(field, retained_phase)
    network = {}
    for site in set(q) | set(z) | set(static_labels):
        labels = static_labels.get(site, (0,) * 4)
        if n < 3:
            head = prefix(n, antecedent(z.get(site, 0), chart(3, labels + (q.get(site, 0),))))
        else:
            compensation = 1 if retained_phase else pow(4, n // 3, 5)
            head = chart(n, labels + (compensation * q.get(site, 0) % 5,))
        if head != vacuum(n):
            network[site] = head
    return network


def network_step(n, network):
    advanced = {site: native_step(n, head) for site, head in network.items()}
    require(native_step(n, vacuum(n)) == vacuum(n + 1), "vacuum transport")
    if (n + 1) % 3:
        return {site: head for site, head in advanced.items() if head != vacuum(n + 1)}
    labels = {site: read_chart(n + 1, head) for site, head in advanced.items()}
    eps = clean_five({site: values[4] for site, values in labels.items()})
    eps_next = adjacency(eps)
    result = {}
    for site in set(labels) | set(eps_next):
        lam = labels.get(site, ZERO_LABELS)[:4]
        head = chart(n + 1, lam + (eps_next.get(site, 0),))
        if head != vacuum(n + 1):
            result[site] = head
    return result


def check_all_tick_seams():
    for index, initial in enumerate(SAMPLE_FIELDS):
        static_labels = STATIC_LABELS if index < 6 else {}
        for retained_phase in (False, True):
            field = initial
            network = projected_network(0, field, retained_phase, static_labels)
            for n in range(15):
                network = network_step(n, network)
                if (n + 1) % 3 == 0:
                    field = raw_step(field, retained_phase)
                require(network == projected_network(n + 1, field, retained_phase, static_labels),
                        "all-tick local native diagram")


def laurent_multiply(a, b, modulus=5):
    result = {}
    for (x, y), c in a.items():
        for (r, s), d in b.items():
            site = (x+r, y+s)
            result[site] = result.get(site, 0) + c*d
    if modulus:
        result = {key: value % modulus for key, value in result.items()}
    return {key: value for key, value in result.items() if value}


def laurent_power(a, exponent, modulus=5):
    result = {(0, 0): 1}
    while exponent:
        if exponent % 2:
            result = laurent_multiply(result, a, modulus)
        a = laurent_multiply(a, a, modulus)
        exponent //= 2
    return result


def four_fronts(distance, coefficient=4):
    return {(distance*r, distance*s): coefficient for r, s in DISPLACEMENTS}


def check_frobenius_and_inverse():
    b = four_fronts(1)
    field = {(0, 0): 1}
    for k in range(1, 126):
        field = adjacency(field)
        require(all(field.get(site) == value
                    for site, value in four_fronts(k, pow(4, k, 5)).items()),
                "residual extreme fronts")
        if k in (1, 5, 25, 125):
            require(field == four_fronts(k), "complete Frobenius profile")
    polynomial = b
    for m in range(9):
        require(polynomial == four_fronts(5 ** m), "Laurent Frobenius")
        if m < 8:
            polynomial = laurent_power(polynomial, 5)
    factors = laurent_multiply({(-1, -1): 4}, {(1, 0): 1, (0, 1): 1})
    require(laurent_multiply(factors, {(1, 1): 1, (0, 0): 1}) == b,
            "Laurent factor")
    evaluate = lambda f: sum(c * pow(4, y % 4, 5) for (_, y), c in f.items()) % 5
    require(evaluate(b) == 0 and evaluate({(0, 0): 1}) == 1, "nonimage witness")
    # Prefix of b^-1 = 4v/((1+uv)(1+u^-1 v)): powers v^1,...,v^32.
    inverse = {}
    for n in range(32):
        for a in range(n + 1):
            inverse[(2*a-n, n+1)] = (4 * (-1) ** n) % 5
    residual = laurent_multiply(b, inverse)
    require({key: value for key, value in residual.items() if key[1] < 32}
            == {(0, 0): 1}, "formal inverse through product v order 31")
    require(any(y >= 32 for _, y in residual), "truncated inverse is not a finite inverse")
    char_zero = laurent_power(b, 5, modulus=None)
    require(char_zero.get((3, 0)) == 25600, "characteristic-zero coefficient")
    require(laurent_power(b, 5).get((3, 0), 0) == 0, "Frobenius is characteristic five")
    # Evaluate the displayed infinite field, never truncate it at the box edge.
    kernel = lambda r, s: 1 if r % 2 == 0 else 4
    for r, s in product(range(-4, 5), repeat=2):
        require(4 * sum(kernel(r + dr, s + ds) for dr, ds in DISPLACEMENTS) % 5 == 0,
                "bilateral kernel pointwise identity")
        require(kernel(r, s) != 0, "bilateral kernel is nonzero")


def check_normalization():
    t = ((1, 2), (-2, 1))
    a = tuple(tuple(t[r//2][c//2] * t[r%2][c%2] for c in range(4)) for r in range(4))
    apply = lambda matrix, vector: tuple(sum(x*y for x, y in zip(row, vector)) for row in matrix)
    norm = lambda vector: sum(x*x for x in vector)
    initial = (1, 2, -1, 3)
    n0 = norm(initial)
    raw, rational = initial, tuple(Fraction(x) for x in initial)
    for k in range(13):
        require(tuple(Fraction(x, 5**k) for x in raw) == rational, "linear amplitude reading")
        require(norm(raw) == 25**k * n0 and norm(rational) == n0, "fixed preparation norm")
        require(sum(Fraction(x*x, 25**k*n0) for x in raw) == 1, "unit Hilbert reading")
        raw = apply(a, raw)
        rational = tuple(Fraction(x, 5) for x in apply(a, rational))
    base, scaled = (1, 0, 0, 0), (5, 0, 0, 0)
    require(norm(scaled) == 25*norm(base) and all(y == 5*x for x, y in zip(base, scaled)),
            "same positive normalized ray")
    require(sum(x*y for x, y in zip(H, base)) % 5 == 1
            and sum(x*y for x, y in zip(H, scaled)) % 5 == 0, "raw residue separation")
    ports = (1, 2)
    original_weights = tuple(Fraction(x*x, norm(ports)) for x in ports)
    portwise_normalized = tuple(Fraction(x, abs(x)) for x in ports)
    altered_weights = tuple(Fraction(x*x, norm(portwise_normalized))
                            for x in portwise_normalized)
    require(original_weights == (Fraction(1, 5), Fraction(4, 5))
            and altered_weights == (Fraction(1, 2), Fraction(1, 2))
            and original_weights != altered_weights, "portwise normalization counterexample")
    inverse = tuple(tuple(Fraction(a[c][r], 5) for c in range(4)) for r in range(4))
    require(apply(inverse, tuple(Fraction(x, 5) for x in apply(a, initial))) == initial,
            "localized amplitude inverse")


def main():
    check_ring_and_grams()
    check_residue_preparation()
    check_local_raw()
    check_native_exhaustive()
    check_all_tick_seams()
    check_frobenius_and_inverse()
    check_normalization()
    lines = (
        "PASS source_ring basis=8 residue_places=2,3",
        "PASS coin_grams squared_gains=25,625",
        "PASS residue_preparation pairs=25 places=2",
        "PASS local_raw_reduction fields=8 macrosteps=4 branches=2",
        "PASS native_antecedents exhaustive_heads=15625",
        "PASS native_chart labels=3125 times=20",
        "PASS native_local_factor fields=8 microscopic_ticks=15 branches=2",
        "PASS residual_fronts times=1..125 frobenius_profiles=1,5,25,125",
        "PASS laurent_frobenius m=0..8 factor_and_nonimage",
        "PASS formal_inverse prefix_v=1..32 product_through_v=31",
        "PASS characteristic_zero coefficient_b5_u3_v0=25600",
        "PASS bilateral_kernel pointwise_box=-4..4 nonzero_values=81",
        "PASS normalization fixed_initial_norm_steps=0..12 raw_residue_separation",
        "PASS localized_amplitude_inverse rational_example",
        "PASS P-SOURCE-PHASE-NATIVE-1 exact_finite_audit",
    )
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
