#!/usr/bin/env python3
"""Independent, finite exact audit for C-HODGE-OPEN-CHANNEL-N.

Standard library only; no verifier or scientific source is imported.  The
matrix and step order below are transcribed from homogeneous_source.md at
twistj-handoff/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8.  All arithmetic is
over Gaussian rationals, polynomial rings over them, or the formal phase
ring Q(i)[z]/(z**5 - 1), evaluated physically at z = exp(-2*pi*i/5).

Scope: finite algebraic identities, specified finitely supported source
states, and return amplitudes through four source steps.  The F samples are inputs to
an algebraic identity, not computed boundary values of the source spectral
function.  This audit does not establish boundary values at every energy,
prove a whole-window scattering representation, or discard dark current.
"""

from fractions import Fraction


def q(real=0, imag=0):
    return (Fraction(real), Fraction(imag))


ZERO, ONE, I = q(), q(1), q(0, 1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def abs2(x):
    return x[0] * x[0] + x[1] * x[1]


def div(x, y):
    den = abs2(y)
    assert den != 0
    num = mul(x, conj(y))
    return (num[0] / den, num[1] / den)


def qsum(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


# Polynomials in two real variables.  Conjugation acts on coefficients.
def clean(p):
    return {key: value for key, value in p.items() if value != ZERO}


def pc(value):
    return clean({(0, 0): value})


def pa(p, r):
    result = dict(p)
    for key, value in r.items():
        result[key] = add(result.get(key, ZERO), value)
    return clean(result)


def ps(p, value):
    return clean({key: mul(value, coeff) for key, coeff in p.items()})


def pm(p, r):
    result = {}
    for (i, j), a in p.items():
        for (k, ell), b in r.items():
            key = (i + k, j + ell)
            result[key] = add(result.get(key, ZERO), mul(a, b))
    return clean(result)


def pstar(p):
    return {key: conj(value) for key, value in p.items()}


def pabs2(p):
    return pm(pstar(p), p)


def polynomial_schur_defect():
    a, b = {(1, 0): ONE}, {(0, 1): ONE}
    f = pa(a, ps(b, I))
    den = pa(pc(q(4)), f)
    num = pa(pc(q(4)), ps(f, q(-1)))
    defect = pa(pabs2(den), ps(pabs2(num), q(-1)))
    assert defect == ps(a, q(16))


def polynomial_unitary_completion():
    # a=t**2 permits polynomial checking without numerical square roots.
    t, b = {(1, 0): ONE}, {(0, 1): ONE}
    f = pa(pm(t, t), ps(b, I))
    den = pa(pc(q(4)), f)
    n = [
        [pa(pc(q(4)), ps(f, q(-1))), ps(t, q(4))],
        [ps(t, q(-4)), pa(pc(q(4)), ps(pstar(f), q(-1)))],
    ]
    den_norm = pabs2(den)
    for j in range(2):
        for k in range(2):
            gram = pa(pm(pstar(n[0][j]), n[0][k]),
                      pm(pstar(n[1][j]), n[1][k]))
            row_gram = pa(pm(n[j][0], pstar(n[k][0])),
                          pm(n[j][1], pstar(n[k][1])))
            expected = den_norm if j == k else {}
            assert gram == expected
            assert row_gram == expected


def finite_schur_samples():
    # The order is (pulse q, object eta), as in PROOF_PORT.md.
    for f, root_a in ((q(1), 1), (q(1, 1), 1),
                      (q(4, -3), 2), (q(9, 2), 3), (q(0, 2), 0)):
        assert root_a * root_a == f[0]
        den = add(q(4), f)
        s = div(sub(q(4), f), den)
        matrix = [
            [s, div(q(4 * root_a), den)],
            [div(q(-4 * root_a), den), div(sub(q(4), conj(f)), den)],
        ]
        for j in range(2):
            for k in range(2):
                gram = qsum(mul(conj(matrix[i][j]), matrix[i][k])
                            for i in range(2))
                assert gram == (ONE if j == k else ZERO)
        assert 1 - abs2(s) == 16 * f[0] / abs2(den)
        if f == q(1):
            assert matrix == [[q(Fraction(3, 5)), q(Fraction(4, 5))],
                              [q(Fraction(-4, 5)), q(Fraction(3, 5))]]
        if f[0] == 0:
            assert matrix[0][1] == matrix[1][0] == ZERO
            assert abs2(s) == 1
    # Outside Re F >= 0 the scalar expression need not be a contraction.
    assert abs2(div(q(5), q(3))) == Fraction(25, 9) > 1


# Source M2; coin indices 0..3 have physical velocities listed below.
M2 = [[div(entry, q(5)) for entry in row] for row in (
    (q(1), q(0, 2), q(0, 2), q(-4)),
    (q(0, 2), q(1), q(-4), q(0, 2)),
    (q(0, 2), q(-4), q(1), q(0, 2)),
    (q(-4), q(0, 2), q(0, 2), q(1)),
)]
VELOCITIES = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def source_step(state, token_phase=2):
    """U_T=exp(-i beta) Gamma S M2, beta=4pi/5, g=2pi/5.

    A state key is (x_A,x_B,coin,z_power).  The default token phase is
    z**2; Gamma contributes z precisely AFTER the shift at x_A=x_B.
    The fixed token and receiver coordinates are spectators of U_T.
    """
    output = {}
    for (x_a, x_b, old_coin, power), amp in state.items():
        assert (x_a - x_b) % 2 == 0
        for new_coin, (v_a, v_b) in enumerate(VELOCITIES):
            y_a, y_b = x_a + v_a, x_b + v_b
            phase = (power + token_phase + int(y_a == y_b)) % 5
            key = (y_a, y_b, new_coin, phase)
            value = mul(M2[new_coin][old_coin], amp)
            output[key] = add(output.get(key, ZERO), value)
    return clean(output)


def state_scale(state, factor):
    return clean({key: mul(factor, value) for key, value in state.items()})


def state_add(left, right):
    output = dict(left)
    for key, value in right.items():
        output[key] = add(output.get(key, ZERO), value)
    return clean(output)


def form(left, right, weight=lambda x_a, x_b: 1):
    """Exact mixed form as five coefficients of the formal phase ring."""
    result = [ZERO] * 5
    for (x_a, x_b, coin, power_l), amp_l in left.items():
        for (y_a, y_b, other_coin, power_r), amp_r in right.items():
            if (x_a, x_b, coin) == (y_a, y_b, other_coin):
                power = (power_r - power_l) % 5
                term = mul(q(weight(x_a, x_b)), mul(conj(amp_l), amp_r))
                result[power] = add(result[power], term)
    return tuple(result)


def constant(value):
    return (q(value), ZERO, ZERO, ZERO, ZERO)


def real_constant(value):
    assert value[1:] == (ZERO,) * 4 and value[0][1] == 0
    return value[0][0]


def n_right(x_a, x_b, carrier, receiver=100):
    # The physical cut is 99.5; true identity ancillas are fixed to zero.
    return (2 * int(x_a > 99) + 2 * int(x_b > 99)
            + 4 * int(carrier > 99) + 2 * int(receiver > 99))


def source_current_negative_control():
    for j in range(4):
        for k in range(4):
            assert qsum(mul(conj(M2[i][j]), M2[i][k]) for i in range(4)) == (
                ONE if j == k else ZERO)
    # R=102,r=-3; token y=0, receiver z=100; p_0=0.  Contact is inactive.
    initial = {(99, 105, 0, 0): ONE}
    after = source_step(initial)
    assert all(x_a != x_b for x_a, x_b, coin, power in after)
    assert form(initial, initial) == form(after, after) == constant(1)
    charge = lambda x_a, x_b: n_right(x_a, x_b, carrier=0)
    before_q = real_constant(form(initial, initial, charge))
    after_q = real_constant(form(after, after, charge))
    assert before_q == 4 and after_q == Fraction(28, 5)
    assert after_q - before_q == Fraction(8, 5)
    # There is no pulse, and the standing token does not cross the cut.
    carrier_only = lambda x_a, x_b: 4 * int(0 > 99)
    assert form(after, after, carrier_only) == constant(0)
    assert form(initial, initial, carrier_only) == constant(0)


def alpha0(n):
    # sqrt(2) times the normalized source alpha_n=i(e2-e3)/sqrt(2).
    return {(n, n, 1, 0): I, (n, n, 2, 0): neg(I)}


def damp_alpha0(state, n):
    """I-(2/5)|alpha_n><alpha_n|, with the normalized alpha_n."""
    output = dict(state)
    for power in range(5):
        overlap = add(mul(neg(I), state.get((n, n, 1, power), ZERO)),
                      mul(I, state.get((n, n, 2, power), ZERO)))
        # alpha0 has squared norm 2; (2/5)/2=1/5.
        for coin, alpha_amp in ((1, I), (2, neg(I))):
            key = (n, n, coin, power)
            correction = mul(q(Fraction(1, 5)), mul(alpha_amp, overlap))
            output[key] = sub(output.get(key, ZERO), correction)
    return clean(output)


def source_two_returns():
    initial = alpha0(0)
    after_one = source_step(initial)
    after_two = source_step(after_one)
    assert form(initial, initial) == constant(2)
    assert form(initial, after_one) == constant(0)
    assert form(initial, after_two) == constant(Fraction(8, 5))
    mu_two = real_constant(form(initial, after_two)) / 2
    assert mu_two == Fraction(4, 5)
    # The contact projection after one step is zero, so g_1=mu_2.
    assert -Fraction(4, 5) ** 2 * mu_two == Fraction(-64, 125)
    after_four = source_step(source_step(after_two))
    expected_four = [ZERO] * 5
    expected_four[0] = q(Fraction(160, 125))
    expected_four[4] = q(Fraction(-56, 125))
    assert form(initial, after_four) == tuple(expected_four)
    # The next damped return is evaluated by the actual three A factors,
    # not by inserting its expected scalar recurrence into the stepper.
    damped = after_one
    for _ in range(3):
        damped = source_step(damp_alpha0(damped, 0))
    expected_g3 = list(expected_four)
    expected_g3[0] = q(Fraction(96, 125))
    assert form(initial, damped) == tuple(expected_g3)
    correction = 2 * Fraction(2, 5) * mu_two ** 2
    assert sub(expected_four[0], expected_g3[0]) == q(correction)
    assert expected_four[1:] == expected_g3[1:]
    conjugated_four = tuple(conj(expected_four[(-power) % 5]) for power in range(5))
    assert tuple(expected_four) != conjugated_four
    # At the physical primitive fifth root z, z**4 != z: its order 5
    # cannot divide 4-1=3.  Thus the displayed nonzero z**4 coefficient
    # gives a nonreal return, not only a formal coefficient difference.
    assert (4 - 1) % 5 != 0 and expected_four[4] != ZERO
    # The cancellation is z**(2+2+1)=1.  Deleting the two token phases
    # instead gives (4/5)z, not 4/5 at the physical primitive fifth root.
    wrong = source_step(source_step(initial, token_phase=0), token_phase=0)
    expected_wrong = [ZERO] * 5
    expected_wrong[1] = q(Fraction(8, 5))
    assert form(initial, wrong) == tuple(expected_wrong)
    assert form(initial, wrong) != form(initial, after_two)


def source_memory_cross_term():
    # Initial (alpha_99 +/- beta_99)/sqrt(2), same carrier/receiver labels.
    # beta is the pulse-a source vector (e1-e4)/sqrt(2).  The contact token
    # output is (3 alpha -/+ 4 alpha)/(5 sqrt(2)), then the actual U_T.
    # Unnormalized alpha0 has norm^2=2, so the total initial norm^2 is 4.
    free_alpha = source_step(alpha0(99))
    charge = lambda x_a, x_b: n_right(x_a, x_b, carrier=99)
    assert form(free_alpha, free_alpha) == constant(2)
    assert form(free_alpha, free_alpha, charge) == constant(8)
    initial_term = state_scale(free_alpha, q(Fraction(3, 5)))
    history_term = state_scale(free_alpha, q(Fraction(-4, 5)))
    plus = state_add(initial_term, history_term)
    minus = state_add(initial_term, state_scale(history_term, q(-1)))
    coherent = real_constant(form(plus, plus, charge)) / 4
    reversed_phase = real_constant(form(minus, minus, charge)) / 4
    diagonal_only = (real_constant(form(initial_term, initial_term, charge))
                     + real_constant(form(history_term, history_term, charge))) / 4
    cross = 2 * real_constant(form(initial_term, history_term, charge)) / 4
    assert coherent == Fraction(2, 25)
    assert reversed_phase == Fraction(98, 25)
    assert diagonal_only == 2
    assert cross == Fraction(-48, 25)
    assert coherent == diagonal_only + cross
    assert coherent != diagonal_only


def main():
    checks = (
        (polynomial_schur_defect, "symbolic Schur defect: 16 Re F"),
        (polynomial_unitary_completion, "symbolic S_F: both unitary Gram identities"),
        (finite_schur_samples, "four interior F samples; Re F=0 boundary; negative-Re control"),
        (source_current_negative_control, "source W cut99.5: object current 8/5, pulse current 0"),
        (source_two_returns, "source W: mu1=0, mu2=4/5, mu4=(80-28*z^4)/125, g3=(48-28*z^4)/125"),
        (source_memory_cross_term, "source memory: charge 2/25 versus diagonal-only 2; cross=-48/25"),
    )
    for check, description in checks:
        check()
        print("PASS " + description)
    print("PASS 6 finite exact audit groups; no whole-window spectral claim")


if __name__ == "__main__":
    main()
