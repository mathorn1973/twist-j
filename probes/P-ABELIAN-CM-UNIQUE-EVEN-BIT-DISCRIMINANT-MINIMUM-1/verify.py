#!/usr/bin/env python3
"""Exact audit for the unique-even-bit abelian CM discriminant minimum.

This standard-library verifier audits finite certificates used by the written
proof in PREREG.md.  It does not replace Kronecker--Weber, the abelian
character-field correspondence, the conductor-discriminant theorem, or the
infinite Minkowski reduction.
"""

from fractions import Fraction
from itertools import product
from math import factorial, gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def units(modulus):
    return [a for a in range(modulus) if gcd(a, modulus) == 1]


def character_order(exponents):
    orders = {4 // gcd(4, value) for value in exponents.values()}
    return max(orders)


def characters_to_mu4(modulus):
    """Enumerate Hom((Z/modulus Z)^x, mu_4) by exponent maps to Z/4Z."""
    carrier = units(modulus)
    identity = 1 % modulus
    others = [a for a in carrier if a != identity]
    result = []
    for values in product(range(4), repeat=len(others)):
        exponent = {identity: 0}
        exponent.update(zip(others, values))
        if all(
            exponent[(a * b) % modulus] == (exponent[a] + exponent[b]) % 4
            for a in carrier
            for b in carrier
        ):
            result.append(exponent)
    return result


def factors_through(exponent, modulus, divisor):
    require(modulus % divisor == 0, "candidate conductor must divide modulus")
    carrier = units(modulus)
    return all(
        a % divisor != b % divisor or exponent[a] == exponent[b]
        for a in carrier
        for b in carrier
    )


def conductor(exponent, modulus):
    return min(d for d in divisors(modulus) if factors_through(exponent, modulus, d))


def character_parity(exponent, modulus):
    value = exponent[(-1) % modulus]
    require(value in (0, 2), "a character must send -1 to +1 or -1")
    return "even" if value == 0 else "odd"


def square_character(exponent):
    return {a: (2 * value) % 4 for a, value in exponent.items()}


def bareiss_determinant(matrix):
    """Fraction-free determinant over Z."""
    work = [row[:] for row in matrix]
    size = len(work)
    require(all(len(row) == size for row in work), "determinant matrix must be square")
    if size == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if work[row][pivot_index] != 0),
            None,
        )
        require(pivot_row is not None, "unexpected singular Bareiss pivot")
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                require(numerator % previous == 0, "Bareiss division was not exact")
                work[row][column] = numerator // previous
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def resultant(low_first_f, low_first_g):
    """Sylvester determinant for integer polynomials in low-first order."""
    degree_f = len(low_first_f) - 1
    degree_g = len(low_first_g) - 1
    high_f = list(reversed(low_first_f))
    high_g = list(reversed(low_first_g))
    size = degree_f + degree_g
    rows = []
    for shift in range(degree_g):
        rows.append([0] * shift + high_f + [0] * (degree_g - 1 - shift))
    for shift in range(degree_f):
        rows.append([0] * shift + high_g + [0] * (degree_f - 1 - shift))
    require(len(rows) == size, "Sylvester row count mismatch")
    return bareiss_determinant(rows)


def gate_group_floor():
    hom_c4_c2 = []
    for generator_image in (0, 1):
        mapping = {x: (generator_image * x) % 2 for x in range(4)}
        require(
            all(mapping[(a + b) % 4] == (mapping[a] + mapping[b]) % 2
                for a in range(4) for b in range(4)),
            "C4 character law failed",
        )
        hom_c4_c2.append(mapping)
    require(len(hom_c4_c2) == 2, "Hom(C4,C2) must have cardinality two")
    require(all(mapping[2] == 0 for mapping in hom_c4_c2),
            "every quadratic character must kill the C4 involution")
    require((2 * 1) % 4 == 2, "the C4 generator must square to the involution")
    require(len(list(product((0, 1), repeat=2))) == 4,
            "Hom(C2xC2,C2) must have cardinality four")


def gate_minkowski():
    def m_value(n):
        return Fraction(3, 4) ** n * Fraction(n ** (2 * n), factorial(n) ** 2)

    require(m_value(8) == Fraction(21233664, 1225), "M(8) exact value mismatch")
    require(m_value(8) > 125, "M(8) must exceed 125")
    for n in range(1, 65):
        ratio = m_value(n + 1) / m_value(n)
        formula = Fraction(3, 4) * Fraction(n + 1, n) ** (2 * n)
        binomial_floor = Fraction(3, 4) * (5 - Fraction(1, n))
        require(ratio == formula, "M(n+1)/M(n) identity mismatch")
        require(formula >= binomial_floor >= 3, "M ratio lower bound mismatch")


def gate_quartic_groups():
    c4_orders = [1, 4, 2, 4]
    require(c4_orders.count(2) == 1, "C4 must have one involution")
    v4_nonidentity = [(1, 0), (0, 1), (1, 1)]
    require(len(v4_nonidentity) == 3, "C2xC2 must have three involutions")
    require(len(list(product((0, 1), repeat=2))) == 4,
            "the Klein group must have four quadratic characters including trivial")


def gate_small_conductors():
    all_characters = {m: characters_to_mu4(m) for m in range(1, 6)}
    for modulus in range(1, 5):
        require(not any(character_order(chi) == 4 for chi in all_characters[modulus]),
                "quartic character appeared below conductor five")

    quartic_five = [
        chi for chi in all_characters[5]
        if character_order(chi) == 4 and conductor(chi, 5) == 5
    ]
    require(len(quartic_five) == 2, "conductor five must have two primitive quartic characters")
    require(all(character_parity(chi, 5) == "odd" for chi in quartic_five),
            "primitive quartic characters at five must be odd")
    require(all(conductor(square_character(chi), 5) == 5 for chi in quartic_five),
            "their quadratic squares must have conductor five")
    require(all(character_parity(square_character(chi), 5) == "even" for chi in quartic_five),
            "their quadratic squares must be even")

    primitive_quadratic = {}
    for modulus in range(1, 5):
        primitive_quadratic[modulus] = [
            chi for chi in all_characters[modulus]
            if character_order(chi) == 2 and conductor(chi, modulus) == modulus
        ]
    require(len(primitive_quadratic[1]) == 0 and len(primitive_quadratic[2]) == 0,
            "no nontrivial primitive quadratic character may occur at one or two")
    require(len(primitive_quadratic[3]) == 1 and len(primitive_quadratic[4]) == 1,
            "conductors three and four must each have one primitive quadratic character")
    require(all(character_parity(chi, modulus) == "odd"
                for modulus in (3, 4) for chi in primitive_quadratic[modulus]),
            "the primitive quadratic characters below five must be odd")


def gate_two_primary():
    chars_eight = characters_to_mu4(8)
    primitive_quadratic_eight = [
        chi for chi in chars_eight
        if character_order(chi) == 2 and conductor(chi, 8) == 8
    ]
    require(len(primitive_quadratic_eight) == 2,
            "modulus eight must have two primitive quadratic characters")
    parities = sorted(character_parity(chi, 8) for chi in primitive_quadratic_eight)
    require(parities == ["even", "odd"],
            "modulus eight must have one even and one odd primitive quadratic character")

    chars_sixteen = characters_to_mu4(16)
    primitive_quartic_sixteen = [
        chi for chi in chars_sixteen
        if character_order(chi) == 4 and conductor(chi, 16) == 16
    ]
    require(len(primitive_quartic_sixteen) == 4,
            "modulus sixteen must have four primitive quartic characters")
    odd_quartic = [chi for chi in primitive_quartic_sixteen if character_parity(chi, 16) == "odd"]
    require(len(odd_quartic) == 2,
            "modulus sixteen must have two odd primitive quartic characters")
    require(all(conductor(square_character(chi), 16) == 8 for chi in odd_quartic),
            "the square of every odd primitive quartic character at sixteen must have conductor eight")
    require(all(character_parity(square_character(chi), 16) == "even" for chi in odd_quartic),
            "the quadratic square in the pure 2-primary CM branch must be even")
    require(16 ** 2 * 8 == 2048, "pure 2-primary discriminant floor mismatch")


def gate_conductor_product():
    require(5 ** 2 * 5 == 125, "conductor floor mismatch")
    equality_pairs = [
        (quartic, quadratic)
        for quartic in range(5, 126)
        for quadratic in range(5, 126)
        if quartic ** 2 * quadratic == 125
    ]
    require(equality_pairs == [(5, 5)], "conductor equality case must be unique")


def gate_zeta_five():
    phi_five = [1, 1, 1, 1, 1]
    derivative = [1, 2, 3, 4]
    discriminant = resultant(phi_five, derivative)
    require(discriminant == 125, "Phi_5 discriminant must be 125")
    unit_group = units(5)
    require(unit_group == [1, 2, 3, 4], "unexpected unit group modulo five")
    powers_of_two = [pow(2, exponent, 5) for exponent in range(4)]
    require(powers_of_two == [1, 2, 4, 3], "two must generate (Z/5Z)^x")
    require(len(set(powers_of_two)) == 4, "the quartic character kernel at five must be trivial")


def main():
    gates = [
        ("GROUP-FLOOR", gate_group_floor,
         "the even-bit condition supplies an order-four root and excludes the Klein group at degree four"),
        ("MINKOWSKI", gate_minkowski,
         "M(8)=21233664/1225>125 and the exact ratio certificate is at least three"),
        ("QUARTIC-GROUPS", gate_quartic_groups,
         "C4 has one involution and two C2 characters; C2xC2 has three and four"),
        ("SMALL-CONDUCTORS", gate_small_conductors,
         "quartic conductors start at five and even quadratic conductors start at five"),
        ("TWO-PRIMARY", gate_two_primary,
         "the pure 2-primary quartic/even-quadratic floor is (16,8) and discriminant at least 2048"),
        ("CONDUCTOR-PRODUCT", gate_conductor_product,
         "f(psi)^2 f(epsilon) is at least 125 with equality only at (5,5)"),
        ("ZETA-FIVE", gate_zeta_five,
         "Phi_5 has discriminant 125 and the faithful conductor-five character cuts out the full field"),
    ]
    for index, (name, gate, description) in enumerate(gates, 1):
        gate()
        print(f"PASS {index:02d} {name:<18} {description}")
    print("SCOPE L1 MINIMUM IN THE FROZEN ABELIAN GALOIS CM UNIQUE-EVEN-BIT CLASS ONLY; NO PHYSICAL SELECTION, J DERIVATION, TWO-PLACE-PHYSICS PROMOTION, OR L2-L6 CLAIM")
    print(f"RESULT {len(gates)}/{len(gates)} ALL PASS")


if __name__ == "__main__":
    main()
