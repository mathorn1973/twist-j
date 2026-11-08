"""Independent exact affine audit in the integral basis 1,u,u^2,u^3.

Here u=1-j and u^4=5u^3-10u^2+10u-5. A state pair (A,D) denotes
A+nD, with six four-coefficient tuples in each state and integer n.
Edges are zero-based unordered slot pairs. No search, input files, imports
from another probe, or scientific work at module import is performed.
"""

from fractions import Fraction


ZERO = (0, 0, 0, 0)
U = (0, 1, 0, 0)
B = (0, 2, -1, 0)
X = (0, 5, -6, 2)
TWO = (2, 0, 0, 0)
P = (1, -2, 1, 0)

# H_ab = Tr(u^a * conjugate(u)^b), a,b=0,...,3.
# Write s=u+conjugate(u)=u*conjugate(u). Then s^2-5s+5=0,
# Tr(1)=4, Tr(u^m)=5 for m=1,2,3, and
# Tr(s),Tr(s^2),Tr(s^3)=10,30,100. Expanding with u+ubar=s,
# and Tr(z)=Tr(conjugate(z)), gives this symmetric trace Gram matrix.
# Q(v)=v^T H v/2. This route does not use power-basis Q coefficients.
TRACE_GRAM = ((4, 5, 5, 5),
              (5, 10, 15, 20),
              (5, 15, 30, 50),
              (5, 20, 50, 100))


def _add(x, y):
    return tuple(x[i] + y[i] for i in range(4))


def _subtract(x, y):
    return tuple(x[i] - y[i] for i in range(4))


def _scale(v, factor):
    return tuple(factor * a for a in v)


def _multiply(x, y):
    """Generic polynomial convolution and monic degree-four reduction."""
    product = [0] * 7
    for i in range(4):
        for j in range(4):
            product[i + j] += x[i] * y[j]
    for degree in range(6, 3, -1):
        value = product[degree]
        product[degree] = 0
        shift = degree - 4
        product[shift] -= 5 * value
        product[shift + 1] += 10 * value
        product[shift + 2] -= 10 * value
        product[shift + 3] += 5 * value
    return tuple(product[:4])


def _half(v):
    if any(a % 2 for a in v):
        raise ArithmeticError("nonintegral affine contact coefficient")
    return tuple(a // 2 for a in v)


def _linear_contact(x, y):
    total = _add(x, y)
    rotated = _multiply(P, _subtract(x, y))
    return _half(_add(total, rotated)), _half(_subtract(total, rotated))


def _power_scalar(v):
    a, b, c, d = v
    return (a + b + c + d, -b - 2 * c - 3 * d, c + 3 * d, -d)


def to_power(A):
    """Convert a six-slot u-basis state to the basis 1,j,j^2,j^3."""
    return tuple(_power_scalar(v) for v in A)


def preparation(r, stride):
    """Return I_(r+stride*n) as two six-slot coefficient states."""
    charged = _scale(B, r)
    tangent = _scale(B, stride)
    return ((charged, _scale(charged, -1), U, U, X, TWO),
            (tangent, _scale(tangent, -1), ZERO, ZERO, ZERO, ZERO))


def target(r, stride):
    """Return G_(r+stride*n) as two six-slot coefficient states."""
    charged = _scale(B, r)
    tangent = _scale(B, stride)
    return ((_add(U, charged), _subtract(U, charged), ZERO, ZERO, X, TWO),
            (tangent, _scale(tangent, -1), ZERO, ZERO, ZERO, ZERO))


def admissions(A, D, edge):
    """Return admission for even n and odd n, respectively."""
    i, j = edge
    constant = _subtract(A[i], A[j])
    slope = _subtract(D[i], D[j])
    return (all(a % 2 == 0 for a in constant),
            all((constant[c] + slope[c]) % 2 == 0 for c in range(4)))


def refine(A, D, epsilon):
    """Substitute n=2*m+epsilon, with epsilon in {0,1}."""
    if epsilon not in (0, 1):
        raise ValueError("refinement parity must be zero or one")
    constant = tuple(_add(a, _scale(d, epsilon)) for a, d in zip(A, D))
    slope = tuple(_scale(d, 2) for d in D)
    return constant, slope


def step(A, D, edge, admitted):
    """Apply one contact after a uniform branch has been selected.

    Reject a nonuniform or incorrectly selected branch. Audit every division
    on both affine coefficient states, including the complete slope.
    """
    if type(admitted) is not bool:
        raise ValueError("admitted must be a Boolean branch decision")
    if admissions(A, D, edge) != (admitted, admitted):
        raise ArithmeticError("affine contact branch is not uniformly selected")
    if not admitted:
        return A, D
    i, j = edge
    left_a, right_a = _linear_contact(A[i], A[j])
    left_d, right_d = _linear_contact(D[i], D[j])
    constant, slope = list(A), list(D)
    constant[i], constant[j] = left_a, right_a
    slope[i], slope[j] = left_d, right_d
    return tuple(constant), tuple(slope)


def _trace_pair(x, y):
    """Tr(x*conjugate(y)) from the independent u-basis Gram form."""
    return sum(x[i] * TRACE_GRAM[i][j] * y[j]
               for i in range(4) for j in range(4))


def _q(v):
    trace = _trace_pair(v, v)
    if trace % 2:
        raise ArithmeticError("half-trace account is not integral")
    return trace // 2


def polynomial_invariants(A, D):
    """Return complete affine invariants in the primary comparison format.

    Result: ((sum_A_in_j_basis,sum_D_in_j_basis),(Q0,Q1,Q2),residues),
    where each of the six residues is (constant,slope) modulo 5.
    The linear account coefficient is Tr(A*conjugate(D)), because trace
    conjugation makes the two cross terms equal before division by two.
    """
    sum_a = tuple(sum(v[c] for v in A) for c in range(4))
    sum_d = tuple(sum(v[c] for v in D) for c in range(4))
    account = (sum(_q(v) for v in A),
               sum(_trace_pair(a, d) for a, d in zip(A, D)),
               sum(_q(v) for v in D))
    # Evaluation at u=0 lands in Z/5 by the constant term 5 of Phi_5(1-u).
    residues = tuple((a[0] % 5, d[0] % 5) for a, d in zip(A, D))
    return ((_power_scalar(sum_a), _power_scalar(sum_d)), account, residues)


def classify(A, D, r, k):
    """Classify full six-slot equality on t=r+2^k*n, n in Z.

    Return ('full',None), ('empty',None), or ('singleton',actual_t).
    This is rational equation elimination in the u basis, independent of
    any primary integer-divisibility implementation of terminal equality.
    """
    if type(k) is not int or k < 0:
        raise ValueError("cylinder exponent must be a nonnegative integer")
    stride = 1 << k
    expected_a, expected_d = target(r, stride)
    candidate = None
    for slot in range(6):
        for coefficient in range(4):
            intercept = A[slot][coefficient] - expected_a[slot][coefficient]
            gradient = D[slot][coefficient] - expected_d[slot][coefficient]
            if gradient == 0:
                if intercept != 0:
                    return "empty", None
                continue
            value = Fraction(-intercept, gradient)
            if candidate is None:
                candidate = value
            elif candidate != value:
                return "empty", None
    if candidate is None:
        return "full", None
    if candidate.denominator != 1:
        return "empty", None
    return "singleton", r + stride * candidate.numerator
