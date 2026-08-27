#!/usr/bin/env python3
"""Exact audit for P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1."""

import ast
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path


IDEAL_LIMIT = 2000
INVERSION_LIMIT = 3000
ROTA_LIMIT = 5000
MERTENS_LIMIT = 5000
DESCENT_LIMIT = 30000
CHARACTER_LIMIT = 20000
CHARACTER_PRIME_LIMIT = 997
S5_LIMIT = 10000
PRIME_CENSUS_LIMIT = 300


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def multiply(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def conjugate(x):
    a, b = x
    return (a + b, -b)


def norm(x):
    a, b = x
    return a * a + a * b - b * b


def multiply_phi(x):
    a, b = x
    return (b, a + b)


def multiply_phi_inverse(x):
    a, b = x
    return (b - a, a)


def unit_shift(x, exponent):
    y = x
    if exponent >= 0:
        for _ in range(exponent):
            y = multiply_phi(y)
    else:
        for _ in range(-exponent):
            y = multiply_phi_inverse(y)
    return y


def sign_normalized(x):
    a, b = x
    return a > 0 or (a == 0 and b > 0)


def in_fundamental_domain(x):
    a, b = x
    require(x != (0, 0), "zero has no unit fundamental representative")
    return b * (2 * a + b) >= 0 and a * (2 * b - a) < 0


def canonical_associate(x):
    require(x != (0, 0), "zero has no canonical associate")
    a, b = x
    while b * (2 * a + b) < 0:
        a, b = b, a + b
    while a * (2 * b - a) >= 0:
        a, b = b - a, a
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    require(in_fundamental_domain((a, b)), "canonical reduction missed domain")
    require(sign_normalized((a, b)), "canonical sign normalization failed")
    return (a, b)


def principal_basis(x):
    return (x, multiply_phi(x))


def lattice_contains(generator, vector):
    c, d = generator
    x, y = vector
    determinant = norm(generator)
    require(determinant != 0, "singular principal lattice")
    first = (c + d) * x - d * y
    second = -d * x + c * y
    return first % determinant == 0 and second % determinant == 0


def same_principal_ideal(x, y):
    if abs(norm(x)) != abs(norm(y)):
        return False
    return (
        all(lattice_contains(y, v) for v in principal_basis(x))
        and all(lattice_contains(x, v) for v in principal_basis(y))
    )


def associated(x, y):
    return canonical_associate(x) == canonical_associate(y)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    bound = isqrt(n)
    candidate = 3
    while candidate <= bound:
        if n % candidate == 0:
            return False
        candidate += 2
    return True


@lru_cache(maxsize=None)
def factorization(n):
    require(n >= 1, "factorization domain")
    factors = []
    remaining = n
    candidate = 2
    while candidate <= isqrt(remaining):
        if remaining % candidate == 0:
            exponent = 0
            while remaining % candidate == 0:
                remaining //= candidate
                exponent += 1
            factors.append((candidate, exponent))
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


@lru_cache(maxsize=None)
def divisors(n):
    values = [1]
    for prime, exponent in factorization(n):
        old = tuple(values)
        power = 1
        for _ in range(exponent):
            power *= prime
            values.extend(value * power for value in old)
    return tuple(sorted(values))


@lru_cache(maxsize=None)
def roots_mod_prime(prime):
    require(is_prime(prime), "root modulus must be prime")
    return tuple(
        value
        for value in range(prime)
        if (value * value - value - 1) % prime == 0
    )


def projective_fixed_count(prime):
    points = [(1, slope) for slope in range(prime)]
    points.append((0, 1))
    count = 0
    for x, y in points:
        ax, ay = y, x + y
        if (x * ay - y * ax) % prime == 0:
            count += 1
    return count


def chi_residue(n):
    residue = n % 5
    if residue == 0:
        return 0
    if residue in (1, 4):
        return 1
    return -1


@lru_cache(maxsize=None)
def chi_dynamic_prime(prime):
    require(is_prime(prime), "dynamic character prime input")
    return projective_fixed_count(prime) - 1


@lru_cache(maxsize=None)
def chi_dynamic(n):
    value = 1
    for prime, exponent in factorization(n):
        value *= chi_dynamic_prime(prime) ** exponent
    return value


def principal_character_mod_five(n):
    return 0 if n % 5 == 0 else 1


def prime_kind(prime, inert_two_as_split=False):
    if prime == 5:
        return "ramified"
    if inert_two_as_split and prime == 2:
        return "split"
    root_count = len(roots_mod_prime(prime))
    require(root_count in (0, 2), "unexpected unramified root count")
    return "split" if root_count == 2 else "inert"


@lru_cache(maxsize=None)
def ideal_state_count(n):
    result = 1
    for prime, exponent in factorization(n):
        kind = prime_kind(prime)
        if kind == "split":
            result *= exponent + 1
        elif kind == "inert":
            if exponent % 2:
                return 0
        else:
            result *= 1
    return result


def ideal_state_count_mutated(n, omit_ramified=False):
    result = 1
    for prime, exponent in factorization(n):
        kind = prime_kind(prime)
        if kind == "split":
            result *= exponent + 1
        elif kind == "inert":
            if exponent % 2:
                return 0
        elif omit_ramified and exponent:
            return 0
    return result


def local_valuation_states(prime, exponent, inert_two_as_split=False):
    kind = prime_kind(prime, inert_two_as_split=inert_two_as_split)
    if kind == "split":
        return tuple((left, exponent - left) for left in range(exponent + 1))
    if kind == "inert":
        if exponent % 2:
            return tuple()
        return ((exponent // 2,),)
    return ((exponent,),)


def ideal_mobius_from_valuations(valuations):
    if any(value >= 2 for value in valuations):
        return 0
    return -1 if sum(valuations) % 2 else 1


@lru_cache(maxsize=None)
def b_state(n):
    states = [tuple()]
    for prime, exponent in factorization(n):
        local = local_valuation_states(prime, exponent)
        states = [left + right for left in states for right in local]
    return sum(ideal_mobius_from_valuations(state) for state in states)


def b_state_mutated(n, inert_two_as_split=False):
    states = [tuple()]
    for prime, exponent in factorization(n):
        local = local_valuation_states(
            prime,
            exponent,
            inert_two_as_split=inert_two_as_split,
        )
        states = [left + right for left in states for right in local]
    return sum(ideal_mobius_from_valuations(state) for state in states)


@lru_cache(maxsize=None)
def b_local(n):
    result = 1
    for prime, exponent in factorization(n):
        kind = prime_kind(prime)
        if kind == "split":
            coefficient = (1, -2, 1)[exponent] if exponent <= 2 else 0
        elif kind == "inert":
            coefficient = -1 if exponent == 2 else 0
        else:
            coefficient = -1 if exponent == 1 else 0
        result *= coefficient
        if result == 0:
            break
    return result


def a_convolution(n):
    return sum(chi_residue(divisor) for divisor in divisors(n))


@lru_cache(maxsize=None)
def enumerated_ideals():
    bound = isqrt(IDEAL_LIMIT)
    require(bound == 44, "frozen complete box changed")
    buckets = [[] for _ in range(IDEAL_LIMIT + 1)]
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            x = (a, b)
            if x == (0, 0):
                continue
            absolute_norm = abs(norm(x))
            if (
                1 <= absolute_norm <= IDEAL_LIMIT
                and in_fundamental_domain(x)
                and sign_normalized(x)
            ):
                buckets[absolute_norm].append(x)
    return tuple(tuple(sorted(bucket)) for bucket in buckets)


def reduced_generators_of_norm(n, narrow_bound=False):
    bound = max(0, isqrt(n) - 1) if narrow_bound else isqrt(n)
    values = []
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            x = (a, b)
            if (
                x != (0, 0)
                and abs(norm(x)) == n
                and in_fundamental_domain(x)
                and sign_normalized(x)
            ):
                values.append(x)
    return tuple(sorted(values))


def common_prime_valuation(a, b, prime):
    exponent = 0
    left, right = a, b
    while left % prime == 0 and right % prime == 0:
        left //= prime
        right //= prime
        exponent += 1
    return exponent, left, right


def ideal_valuations(x):
    absolute_norm = abs(norm(x))
    require(absolute_norm >= 1, "ideal valuation on zero")
    values = []
    a, b = x
    for prime, exponent in factorization(absolute_norm):
        if prime == 5:
            values.append(exponent)
            continue
        common, a0, b0 = common_prime_valuation(a, b, prime)
        roots = roots_mod_prime(prime)
        if len(roots) == 2:
            residual = exponent - 2 * common
            require(residual >= 0, "negative split residual valuation")
            hits = tuple(
                root for root in roots if (a0 + b0 * root) % prime == 0
            )
            if residual:
                require(len(hits) == 1, "split side not uniquely selected")
                for root in roots:
                    values.append(common + residual if root == hits[0] else common)
            else:
                require(len(hits) == 0, "unexpected primitive split hit")
                values.extend((common, common))
        else:
            require(len(roots) == 0, "inert root census")
            require(exponent == 2 * common, "inert valuation/norm mismatch")
            values.append(common)
    return tuple(values)


def ideal_mu_from_generator(x):
    return ideal_mobius_from_valuations(ideal_valuations(x))


@lru_cache(maxsize=None)
def b_enumerated(n):
    return sum(ideal_mu_from_generator(x) for x in enumerated_ideals()[n])


def mu_trial(n):
    sign = 1
    remaining = n
    candidate = 2
    while candidate <= isqrt(remaining):
        if remaining % candidate == 0:
            remaining //= candidate
            if remaining % candidate == 0:
                return 0
            sign = -sign
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        sign = -sign
    return sign


def mu_rota_values(limit):
    values = [0] * (limit + 1)
    values[1] = 1
    for n in range(2, limit + 1):
        values[n] = -sum(values[d] for d in divisors(n) if d < n)
    return tuple(values)


def convolution_value(n, left, right):
    return sum(left(divisor) * right(n // divisor) for divisor in divisors(n))


def descent_value(n):
    return convolution_value(n, b_state, chi_dynamic)


def dirichlet_inverse_of_ideal_count(limit):
    ideal_counts = [0] * (limit + 1)
    inverse = [0] * (limit + 1)
    ideal_counts[1] = 1
    inverse[1] = 1
    for n in range(2, limit + 1):
        ideal_counts[n] = a_convolution(n)
        inverse[n] = -sum(
            ideal_counts[d] * inverse[n // d]
            for d in divisors(n)
            if d > 1
        )
    return tuple(inverse)


def s5_direct(m):
    return sum(chi_residue(value) for value in range(1, m + 1))


def s5_law(m):
    return (0, 1, 0, -1, 0)[m % 5]


def mertens_twosum(n):
    return sum(b_state(a) * s5_law(n // a) for a in range(1, n + 1))


def mertens_residue_twosum(n):
    positive = sum(
        b_state(a)
        for a in range(1, n + 1)
        if (n // a) % 5 == 1
    )
    negative = sum(
        b_state(a)
        for a in range(1, n + 1)
        if (n // a) % 5 == 3
    )
    return positive - negative


def gate_g01():
    coefficients = range(-6, 7)
    for a in coefficients:
        for b in coefficients:
            x = (a, b)
            require(conjugate(conjugate(x)) == x, "conjugation involution")
            require(norm(x) == multiply(x, conjugate(x))[0], "norm product scalar")
            require(multiply(x, conjugate(x))[1] == 0, "norm product phi part")
            for c in coefficients:
                for d in coefficients:
                    y = (c, d)
                    product = multiply(x, y)
                    require(norm(product) == norm(x) * norm(y), "norm multiplicativity")
                    require(
                        conjugate(product) == multiply(conjugate(x), conjugate(y)),
                        "conjugation multiplicativity",
                    )
    for prime in range(2, CHARACTER_PRIME_LIMIT + 1):
        if not is_prime(prime):
            continue
        fixed = projective_fixed_count(prime)
        require(fixed == len(roots_mod_prime(prime)), "projective/root census")
        require(fixed == 1 + chi_residue(prime), "fixed-point deficit")
    for n in range(1, CHARACTER_LIMIT + 1):
        require(chi_dynamic(n) == chi_residue(n), "multiplicative character")
    print(
        "G01 golden ring [-6,6]^4; fixed-line character "
        "p<=997 n<=20000 PASS"
    )


def gate_g02():
    buckets = enumerated_ideals()
    for n in range(1, IDEAL_LIMIT + 1):
        representatives = buckets[n]
        require(len(representatives) == a_convolution(n), "enumerated ideal count")
        require(len(representatives) == ideal_state_count(n), "ideal state count")
        require(b_enumerated(n) == b_state(n), "valuation/state b mismatch")
        require(b_enumerated(n) == b_local(n), "valuation/local b mismatch")
        for x in representatives:
            require(canonical_associate(x) == x, "canonical idempotence")
            for exponent in range(-8, 9):
                shifted = unit_shift(x, exponent)
                require(canonical_associate(shifted) == x, "unit invariance")
                require(same_principal_ideal(x, shifted), "unit lattice equality")
        for left_index, left in enumerate(representatives):
            for right in representatives[left_index + 1 :]:
                require(not associated(left, right), "distinct canonical associates")
                require(
                    not same_principal_ideal(left, right),
                    "distinct principal lattices",
                )
    print(
        "G02 canonical ideals and valuation Mobius "
        "n<=2000 Bmax=isqrt(2000) PASS"
    )


def gate_g03():
    rota = mu_rota_values(ROTA_LIMIT)
    for n in range(1, DESCENT_LIMIT + 1):
        require(b_state(n) == b_local(n), "state/local b full range")
        require(descent_value(n) == mu_trial(n), "descent/trial Mobius")
        if n <= ROTA_LIMIT:
            require(descent_value(n) == rota[n], "descent/Rota Mobius")
    print(
        "G03 mu=b*chi_A n<=30000; trial<=30000 Rota<=5000 PASS"
    )


def gate_g04():
    inverse = dirichlet_inverse_of_ideal_count(INVERSION_LIMIT)
    for n in range(1, INVERSION_LIMIT + 1):
        require(inverse[n] == b_local(n), "inverse/local b")
        if n <= IDEAL_LIMIT:
            require(inverse[n] == b_enumerated(n), "inverse/enumerated b")
    print(
        "G04 Dirichlet inversion n<=3000; enum overlap n<=2000 PASS"
    )


def gate_g05():
    running = 0
    for m in range(0, S5_LIMIT + 1):
        if m:
            running += chi_residue(m)
        require(running == s5_law(m), "S5 residue law")
    rota = mu_rota_values(MERTENS_LIMIT)
    mertens = 0
    for n in range(1, MERTENS_LIMIT + 1):
        mertens += rota[n]
        require(mertens_twosum(n) == mertens, "Mertens S5 two-sum")
        require(mertens_residue_twosum(n) == mertens, "Mertens residue two-sum")
    print(
        "G05 S5 m<=10000; both Mertens two-sums N<=5000 PASS"
    )


def gate_g06():
    for prime in range(2, PRIME_CENSUS_LIMIT + 1):
        if not is_prime(prime):
            continue
        roots = roots_mod_prime(prime)
        representatives = reduced_generators_of_norm(prime)
        kind = prime_kind(prime)
        expected = 2 if kind == "split" else (1 if kind == "ramified" else 0)
        require(len(representatives) == expected, "prime norm census")
        require(len(representatives) == ideal_state_count(prime), "prime ideal census")
        if kind == "split":
            for root in roots:
                vector = (-root, 1)
                image = (1, 1 - root)
                eigenvalue = (1 - root) % prime
                expected_image = (
                    eigenvalue * vector[0] % prime,
                    eigenvalue * vector[1] % prime,
                )
                require(
                    (image[0] % prime, image[1] % prime) == expected_image,
                    "cross-labelled eigenline",
                )
    roots_eleven = roots_mod_prime(11)
    require(roots_eleven == (4, 8), "p=11 roots")
    for root in roots_eleven:
        vector = (-root, 1)
        image = (1, 1 - root)
        same_root_image = (root * vector[0] % 11, root * vector[1] % 11)
        require(
            (image[0] % 11, image[1] % 11) != same_root_image,
            "same-root breaker did not fire",
        )
    print(
        "G06 prime norm census p<=300 and cross-label p=11 PASS"
    )


def sign_only_count(n):
    bound = isqrt(n)
    count = 0
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            if (a, b) != (0, 0) and abs(norm((a, b))) == n and sign_normalized((a, b)):
                count += 1
    return count


def first_mismatch(limit, left, right):
    for n in range(1, limit + 1):
        if left(n) != right(n):
            return n
    return 0


def gate_g07():
    principal_witness = first_mismatch(
        20,
        lambda n: convolution_value(n, b_state, principal_character_mod_five),
        mu_trial,
    )
    require(principal_witness == 2, "principal-character mutation witness")

    inert_witness = first_mismatch(
        20,
        lambda n: b_state_mutated(n, inert_two_as_split=True),
        b_enumerated,
    )
    require(inert_witness == 2, "inert-as-split mutation witness")

    ramified_witness = first_mismatch(
        20,
        lambda n: ideal_state_count_mutated(n, omit_ramified=True),
        lambda n: len(enumerated_ideals()[n]),
    )
    require(ramified_witness == 5, "omitted-ramification mutation witness")

    sign_witness = first_mismatch(
        20,
        sign_only_count,
        lambda n: len(enumerated_ideals()[n]),
    )
    require(sign_witness == 1, "sign-only mutation witness")

    u = (3, 1)
    v = (1, -3)
    require(abs(norm(u)) == abs(norm(v)) == 11, "B4 equal norm")
    require(not associated(u, v), "B4 false associate")
    require(not same_principal_ideal(u, v), "B4 lattice breaker")
    raw_numerator = multiply(u, conjugate(v))
    require(raw_numerator == (-3, 10), "B4 raw conjugate numerator")
    positive_denominator = -norm(v)
    positive_numerator = (-raw_numerator[0], -raw_numerator[1])
    require(positive_denominator == 11, "B4 positive denominator")
    require(positive_numerator == (3, -10), "B4 positive numerator")
    require(
        positive_numerator[0] % positive_denominator != 0
        or positive_numerator[1] % positive_denominator != 0,
        "B4 nonintegral quotient breaker",
    )

    bound_witness = 0
    for n in range(2, 61):
        narrow_count = len(reduced_generators_of_norm(n, narrow_bound=True))
        full_count = len(enumerated_ideals()[n])
        if narrow_count != full_count:
            bound_witness = n
            break
    require(bound_witness == 4, "open-boundary mutation witness")
    require((2, 0) in enumerated_ideals()[4], "n=4 boundary generator")
    require(
        (2, 0) not in reduced_generators_of_norm(4, narrow_bound=True),
        "open bound unexpectedly contains witness",
    )

    print(
        "G07 mutations fired principal=2 inert=2 ramified=5 "
        "sign=1 B4=11 bound=4 PASS"
    )


def called_name(function):
    if isinstance(function, ast.Name):
        return function.id
    if isinstance(function, ast.Attribute):
        return function.attr
    return ""


def gate_g08():
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    allowed_imports = {"ast", "functools", "math", "pathlib"}
    banned_calls = {
        "__import__",
        "complex",
        "eval",
        "exec",
        "exp",
        "float",
        "getenv",
        "log",
        "popen",
        "round",
        "sqrt",
        "system",
    }
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    direct_calls = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            require(
                not isinstance(node.value, (float, complex)),
                "nonintegral numeric constant",
            )
        if isinstance(node, ast.BinOp):
            require(not isinstance(node.op, ast.Div), "true division forbidden")
            if isinstance(node.op, ast.Pow):
                exponent = node.right
                require(
                    not (
                        isinstance(exponent, ast.UnaryOp)
                        and isinstance(exponent.op, ast.USub)
                        and isinstance(exponent.operand, ast.Constant)
                        and isinstance(exponent.operand.value, int)
                    ),
                    "negative integer exponent forbidden",
                )
        if isinstance(node, ast.Call):
            require(called_name(node.func) not in banned_calls, "banned call")
        if isinstance(node, ast.Import):
            require(
                all(alias.name.split(".")[0] in allowed_imports for alias in node.names),
                "non-whitelisted import",
            )
        if isinstance(node, ast.ImportFrom):
            require(
                node.module is not None
                and node.module.split(".")[0] in allowed_imports,
                "non-whitelisted from-import",
            )
    for name, function in functions.items():
        direct_calls[name] = {
            called_name(node.func)
            for node in ast.walk(function)
            if isinstance(node, ast.Call)
        }
    starts = {
        "enumerated_ideals",
        "ideal_valuations",
        "ideal_mu_from_generator",
        "b_enumerated",
    }
    banned_construction = {
        "a_convolution",
        "b_local",
        "b_state",
        "chi_dynamic",
        "chi_residue",
        "mu_rota_values",
        "mu_trial",
    }
    reachable = set()
    pending = list(starts)
    while pending:
        name = pending.pop()
        if name in reachable:
            continue
        reachable.add(name)
        pending.extend(
            called
            for called in direct_calls.get(name, set())
            if called in functions
        )
    require(
        not reachable.intersection(banned_construction),
        "ideal construction firewall",
    )
    print("G08 exact-source AST and construction firewalls PASS")


def main():
    gate_g01()
    gate_g02()
    gate_g03()
    gate_g04()
    gate_g05()
    gate_g06()
    gate_g07()
    gate_g08()
    print("VERIFY RESULT 8/8 ALL PASS")


if __name__ == "__main__":
    main()
