#!/usr/bin/env python3
"""NON-CANONICAL exact audit of an exposed all-real counterexample.

Python 3.12, standard library only. No floats, randomness, external data,
network access, or file I/O. Do not execute before the public freeze and
the coordinator's explicit replay authorization.

The counterexample and every target below were known before this script.
This is not a blind test. The principal embedding is t = exp(i*pi/20).
Arithmetic is in Q[t]/(t^16-t^12+t^8-t^4+1), the cyclotomic field Q(zeta_40).

EXPOSED ANALYTIC SIGN CERTIFICATE, FROZEN BEFORE EXECUTION:
  cos(pi/10) > 0 and cos(3*pi/10) > 0, since both angles are strictly
  between 0 and pi/2. The computed zero-momentum row is required to be
  (a,-a,b,0,-b), with a=cos(pi/10)/5, b=cos(3*pi/10)/5.
  The other nonzero entries are the positive rational 1/10.
  sqrt(5)=1+2*zeta_5+2*zeta_5^-1 is the positive root in this embedding.
Signs are justified by these analytic facts, not by a floating-point or
general algebraic-number sign algorithm. All supporting identities are
checked exactly. The script does not audit or alter the 624-source census.
"""

from dataclasses import dataclass
from fractions import Fraction
import sys


DEGREE = 16


@dataclass(frozen=True)
class Q40:
    """Reduced coefficients in the ordered basis 1,t,...,t^15."""

    coefficients: tuple[Fraction, ...]

    @staticmethod
    def scalar(value: int | Fraction) -> "Q40":
        return Q40((Fraction(value),) + (Fraction(0),) * (DEGREE - 1))

    @staticmethod
    def coerce(value: "Q40 | int | Fraction") -> "Q40":
        if isinstance(value, Q40):
            return value
        if isinstance(value, (int, Fraction)):
            return Q40.scalar(value)
        raise TypeError("Q40 arithmetic accepts only Q40, int, or Fraction")

    def __add__(self, other: "Q40 | int | Fraction") -> "Q40":
        rhs = self.coerce(other)
        return Q40(tuple(a + b for a, b in zip(self.coefficients,
                                               rhs.coefficients)))

    __radd__ = __add__

    def __neg__(self) -> "Q40":
        return Q40(tuple(-a for a in self.coefficients))

    def __sub__(self, other: "Q40 | int | Fraction") -> "Q40":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "Q40 | int | Fraction") -> "Q40":
        return self.coerce(other) + (-self)

    def __mul__(self, other: "Q40 | int | Fraction") -> "Q40":
        rhs = self.coerce(other)
        product = [Fraction(0)] * (2 * DEGREE - 1)
        for i, a in enumerate(self.coefficients):
            if a:
                for j, b in enumerate(rhs.coefficients):
                    if b:
                        product[i + j] += a * b
        # t^16 = t^12 - t^8 + t^4 - 1.
        for k in range(2 * DEGREE - 2, DEGREE - 1, -1):
            a = product[k]
            if a:
                product[k] = Fraction(0)
                product[k - 4] += a
                product[k - 8] -= a
                product[k - 12] += a
                product[k - 16] -= a
        return Q40(tuple(product[:DEGREE]))

    __rmul__ = __mul__

    def __truediv__(self, divisor: int | Fraction) -> "Q40":
        if not isinstance(divisor, (int, Fraction)):
            raise TypeError("Only exact rational division is needed here")
        divisor = Fraction(divisor)
        if not divisor:
            raise ZeroDivisionError("Q40 rational divisor is zero")
        return Q40(tuple(a / divisor for a in self.coefficients))

    def conjugate(self) -> "Q40":
        return sum((a * t_power(-k) for k, a in enumerate(self.coefficients)
                    if a), ZERO)


ZERO = Q40.scalar(0)
ONE = Q40.scalar(1)
T = Q40((Fraction(0), Fraction(1)) + (Fraction(0),) * (DEGREE - 2))
_powers = []
_current = ONE
for _exponent in range(40):
    _powers.append(_current)
    _current = _current * T
T_POWERS = tuple(_powers)
T_TO_40 = _current


def t_power(exponent: int) -> Q40:
    return T_POWERS[exponent % 40]


def cosine(exponent: int) -> Q40:
    """cos(exponent*pi/20) in the fixed principal embedding."""
    return (t_power(exponent) + t_power(-exponent)) / 2


Matrix = tuple[tuple[Q40, ...], ...]
IDENTITY = tuple(tuple(ONE if i == j else ZERO for j in range(5))
                 for i in range(5))


def adjoint(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i].conjugate() for j in range(5))
                 for i in range(5))


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum((left[i][k] * right[k][j] for k in range(5)),
                           ZERO) for j in range(5)) for i in range(5))


def trace(matrix: Matrix) -> Q40:
    return sum((matrix[i][i] for i in range(5)), ZERO)


def phase_operator(q: int, r: int) -> Matrix:
    """A(q,r)|j> = zeta_5^(2*r*(q-j)) |2*q-j>; zeta_5=t^8."""
    matrix = [[ZERO for _ in range(5)] for _ in range(5)]
    for j in range(5):
        matrix[(2 * q - j) % 5][j] = t_power(16 * r * (q - j))
    return tuple(tuple(row) for row in matrix)


def main() -> None:
    if sys.version_info[:2] != (3, 12):
        raise SystemExit("AUDIT_ERROR: this frozen replay requires Python 3.12")

    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    check(T_TO_40 == ONE, "t^40=1 by unreduced recurrence")
    check(t_power(20) == -ONE, "t^20=-1")
    check(t_power(16) - t_power(12) + t_power(8) - t_power(4) + ONE
          == ZERO, "Phi_40(t)=0")

    c = tuple(cosine(8 * j + 1) for j in range(5))
    check(all(x.conjugate() == x for x in c), "source is real")
    check(sum(c, ZERO) == ZERO, "source has zero sum")
    norm_squared = sum((x.conjugate() * x for x in c), ZERO)
    check(norm_squared == Q40.scalar(Fraction(5, 2)), "source norm squared")

    rho = tuple(tuple(c[i] * c[j].conjugate() / Fraction(5, 2)
                      for j in range(5)) for i in range(5))
    check(adjoint(rho) == rho, "density is Hermitian")
    check(trace(rho) == ONE, "density is normalized")
    check(multiply(rho, rho) == rho, "density is a projector")
    check(trace(multiply(rho, rho)) == ONE, "density is pure")
    # Positivity is an exact certificate: a Hermitian projector satisfies
    # <z,rho z>=||rho z||^2>=0. Independently rho=c c^*/(5/2) has a
    # positive rational denominator and <z,rho z>=|c^* z|^2/(5/2)>=0.

    direct = {}
    analytic = {}
    for q in range(5):
        for r in range(5):
            operator = phase_operator(q, r)
            check(adjoint(operator) == operator, f"A({q},{r}) Hermitian")
            check(multiply(operator, operator) == IDENTITY,
                  f"A({q},{r}) involution")
            check(trace(operator) == ONE, f"A({q},{r}) trace")
            # This route uses the complete independently built density and
            # phase matrix; it does not use the analytic Wigner table.
            direct[q, r] = trace(multiply(rho, operator)) / 5
            if r == 0:
                analytic[q, r] = cosine(16 * q + 2) / 5
            elif r in (1, 4):
                analytic[q, r] = Q40.scalar(Fraction(1, 10))
            else:
                analytic[q, r] = ZERO
            check(direct[q, r] == analytic[q, r], f"W({q},{r}) table")
            check(direct[q, r].conjugate() == direct[q, r],
                  f"W({q},{r}) real")

    check(sum(direct.values(), ZERO) == ONE, "Wigner normalization")
    check(sum((value * value for value in direct.values()), ZERO)
          == Q40.scalar(Fraction(1, 5)), "pure-state Wigner squared norm")
    check(sum((direct[q, 0] for q in range(5)), ZERO) == ZERO,
          "zero-momentum row sums to zero")

    a = cosine(2) / 5       # Exposed analytic sign: cos(pi/10)>0.
    b = cosine(6) / 5       # Exposed analytic sign: cos(3*pi/10)>0.
    check(tuple(direct[q, 0] for q in range(5)) == (a, -a, b, ZERO, -b),
          "analytic sign-certificate row")
    negative = {(1, 0), (4, 0)}
    positive = {(q, r) for q in range(5) for r in (1, 4)} | {(0, 0), (2, 0)}
    zero = {(q, r) for q in range(5) for r in range(5)} - negative - positive
    check((len(zero), len(positive), len(negative)) == (11, 12, 2),
          "sign-certificate support counts")
    check({u for u, value in direct.items() if value == ZERO} == zero,
          "exact zero support")
    check(all(direct[u] == Q40.scalar(Fraction(1, 10))
              for u in positive if u[1] in (1, 4)), "positive rational bands")

    negativity = -sum((direct[u] for u in sorted(negative)), ZERO)
    check(negativity == a + b, "negativity from the direct trace values")
    sqrt5 = ONE + 2 * (t_power(8) + t_power(-8))
    check(sqrt5.conjugate() == sqrt5, "sqrt(5) is real")
    check(sqrt5 * sqrt5 == Q40.scalar(5), "sqrt(5) square")
    check(negativity * negativity == (5 + 2 * sqrt5) / 100,
          "counterexample negativity squared")
    old_bound = (ONE + sqrt5) / 10
    check(old_bound * old_bound == (6 + 2 * sqrt5) / 100,
          "old conjectured bound squared")
    gap = old_bound * old_bound - negativity * negativity
    check(gap == Q40.scalar(Fraction(1, 100)), "strict squared gap")
    # Both quantities are positive under the frozen analytic certificate,
    # so the positive rational squared gap proves negativity < old_bound.

    print("C-REAL-SUMZERO-SHARP-COUNTEREXAMPLE")
    print(f"exact_checks={checks} status=PASS")
    print("density=POSITIVE_HERMITIAN_RANK1_PROJECTOR")
    print("wigner_support=zero:11 positive:12 negative:2")
    print("negative_points=(1,0),(4,0)")
    print("sign_basis=EXPOSED_ANALYTIC_FIRST_QUADRANT")
    print("negativity=sqrt(5+2*sqrt(5))/10")
    print("negativity_squared=(5+2*sqrt(5))/100")
    print("old_bound_squared_gap=1/100")
    print("scope=ALL_REAL_SUMZERO_CONJECTURE_ONLY")


if __name__ == "__main__":
    main()
