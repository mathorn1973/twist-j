"""C-GRH-QSQRT5-SPLIT-ORIENTATION-1 verifier.

STATUS NON-CANONICAL. Candidate-grade note verifier per POLICY.md; it
creates no public status and changes no canon file.

Exact integer arithmetic only. Standard library only. No floats, no
division of coefficients, no analytic input. Every gate is an exact
equality of integer sequences. The analytic statements of the note
(continuation, half-plane divisor dictionary, GRH reading) are NOT
gated here; this verifier audits only the L1 Euler-factor algebra the
note stands on.

Gates
  V01 local expansion of (1-T)^2/(1+T^2) through T^12
  V02 channel coefficients: local law vs closed-identity convolution
  V03 mu = c_0 * o coefficientwise (1/zeta = C_0 O_5)
  V04 Dedekind regrouping: o * a_F * e_2 = r,
      the coefficient form of O_5(s) zeta_F(s) L(2s,chi_5)
        = zeta(4s)(1 + 5^-s + 25^-s + 125^-s)
  V05 support census: o(n) != 0 iff n is pure split-orientation
      (every prime factor split with odd exponent), there
      |o(n)| = 2^omega(n) and o(n) = (-1)^(omega(n)+J(n)) 2^omega(n)
  V06 exact summatory values T5(N) at frozen checkpoints, gated as
      integers (the values themselves prove no estimate and no
      cancellation; they gate only the arithmetic)
  V07 breakers: dropping the 5-block, the L(2s,chi_5) factor, or the
      zeta(4s) factor must break V04 at the frozen first differences
      5, 4, 16
"""

import math
import sys

N_MAIN = 100000
N_READ = 500000
CHECKPOINTS = (10, 100, 1000, 10000, 100000, 500000)
FROZEN_READOUTS = ((10, 1), (100, -19), (1000, -103), (10000, -377),
                   (100000, -947), (500000, -1869))
BREAKER_WITNESSES = (5, 4, 16)

CHI5 = (0, 1, -1, -1, 1)


def chi5(n):
    return CHI5[n % 5]


def smallest_prime_factor_table(limit):
    table = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if table[i] == i:
            for j in range(i * i, limit + 1, i):
                if table[j] == j:
                    table[j] = i
        i += 1
    return table


def factorization(n, spf):
    factors = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        factors.append((p, e))
    return factors


def dirichlet_convolution(a, b, limit):
    c = [0] * (limit + 1)
    for i in range(1, limit + 1):
        ai = a[i]
        if ai:
            for j in range(1, limit // i + 1):
                if b[j]:
                    c[i * j] += ai * b[j]
    return c


def orientation_local_coefficients(kmax):
    """Power-series coefficients of (1-T)^2/(1+T^2), exactly.

    (1 - 2T + T^2) * sum_{j>=0} (-1)^j T^{2j}, collected per degree.
    """
    coefficients = [0] * (kmax + 1)
    for j in range(0, kmax // 2 + 1):
        sign = -1 if j % 2 else 1
        for shift, weight in ((0, 1), (1, -2), (2, 1)):
            degree = 2 * j + shift
            if degree <= kmax:
                coefficients[degree] += sign * weight
    return coefficients


def channel_coefficient(n, spf):
    """o(n) from the frozen local law."""
    value = 1
    for p, e in factorization(n, spf):
        if chi5(p) != 1 or e % 2 == 0:
            return 0
        j = (e - 1) // 2
        value *= -2 * (1 if j % 2 == 0 else -1)
    return value


def mobius_table(limit, spf):
    table = [0] * (limit + 1)
    table[1] = 1
    for n in range(2, limit + 1):
        factors = factorization(n, spf)
        if any(e > 1 for _, e in factors):
            table[n] = 0
        else:
            table[n] = -1 if len(factors) % 2 else 1
    return table


def c0_coefficient(n, spf):
    """c_0(n) from the frozen local law of the zero-rapidity channel."""
    value = 1
    for p, e in factorization(n, spf):
        if chi5(p) == 1:
            value *= 1 if e == 1 else 2
        else:
            if e >= 2:
                return 0
            value *= -1
    return value


def fourth_power_indicator(limit):
    table = [0] * (limit + 1)
    m = 1
    while m ** 4 <= limit:
        table[m ** 4] = 1
        m += 1
    return table


def five_block(limit):
    """Coefficients of 1 + 5^-s + 25^-s + 125^-s."""
    table = [0] * (limit + 1)
    for j in range(4):
        if 5 ** j <= limit:
            table[5 ** j] = 1
    return table


def five_powers(limit):
    """Coefficients of 1/(1-5^-s)."""
    table = [0] * (limit + 1)
    k = 1
    while k <= limit:
        table[k] = 1
        k *= 5
    return table


def square_supported(values, limit):
    table = [0] * (limit + 1)
    m = 1
    while m * m <= limit:
        table[m * m] = values[m]
        m += 1
    return table


def first_difference(a, b, limit):
    for n in range(1, limit + 1):
        if a[n] != b[n]:
            return n
    return 0


def require(condition, label):
    if not condition:
        raise RuntimeError("FAIL " + label)


def main():
    lines = []
    lines.append("C-GRH-QSQRT5-SPLIT-ORIENTATION-1 VERIFIER")
    lines.append("STATUS NON-CANONICAL")

    spf_main = smallest_prime_factor_table(N_MAIN)

    # V01 local expansion
    local = orientation_local_coefficients(12)
    frozen_local = [1, -2, 0, 2, 0, -2, 0, 2, 0, -2, 0, 2, 0]
    require(local == frozen_local, "V01-local-expansion")
    lines.append("V01 local (1-T)^2/(1+T^2) e<=12 " +
                 ",".join(str(c) for c in local) + " PASS")

    # channel coefficients from the local law
    o = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        o[n] = channel_coefficient(n, spf_main)

    # V02 closed identity
    # zeta(4s) (1-5^-4s) / ( zeta(s) L(s,chi5) L(2s,chi5) (1-5^-s) )
    mu = mobius_table(N_MAIN, spf_main)
    mu_chi = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        mu_chi[n] = mu[n] * chi5(n)
    inverse_l2 = square_supported(mu_chi, N_MAIN)
    a4 = fourth_power_indicator(N_MAIN)
    b625 = [0] * (N_MAIN + 1)
    b625[1] = 1
    if 625 <= N_MAIN:
        b625[625] = -1
    f5 = five_powers(N_MAIN)
    closed = dirichlet_convolution(a4, b625, N_MAIN)
    closed = dirichlet_convolution(closed, mu, N_MAIN)
    closed = dirichlet_convolution(closed, mu_chi, N_MAIN)
    closed = dirichlet_convolution(closed, inverse_l2, N_MAIN)
    closed = dirichlet_convolution(closed, f5, N_MAIN)
    require(closed == o, "V02-closed-identity")
    lines.append("V02 closed identity n<=" + str(N_MAIN) + " PASS")

    # V03 mu = c_0 * o
    c0 = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        c0[n] = c0_coefficient(n, spf_main)
    require(dirichlet_convolution(c0, o, N_MAIN) == mu, "V03-c0-o-mu")
    lines.append("V03 mu = c_0 * o n<=" + str(N_MAIN) + " PASS")

    # V04 Dedekind regrouping
    one = [0] + [1] * N_MAIN
    chi_table = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        chi_table[n] = chi5(n)
    ideal_count = dirichlet_convolution(one, chi_table, N_MAIN)
    require(all(v >= 0 for v in ideal_count[1:]), "V04-ideal-count-nonneg")
    chi_only = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        chi_only[n] = chi5(n)
    l2 = square_supported(chi_only, N_MAIN)
    block = five_block(N_MAIN)
    target = dirichlet_convolution(a4, block, N_MAIN)
    left = dirichlet_convolution(dirichlet_convolution(o, ideal_count, N_MAIN),
                                 l2, N_MAIN)
    require(left == target, "V04-dedekind-regroup")
    lines.append("V04 o * a_F * e_2 = zeta(4s)-times-5-block n<="
                 + str(N_MAIN) + " PASS")

    # V05 support census and sign law
    for n in range(1, N_MAIN + 1):
        factors = factorization(n, spf_main) if n > 1 else []
        pure = all(chi5(p) == 1 and e % 2 == 1 for p, e in factors)
        if pure:
            a = len(factors)
            j_sum = sum((e - 1) // 2 for _, e in factors)
            expected = (2 ** a) * (-1 if (a + j_sum) % 2 else 1)
            require(o[n] == expected, "V05-sign-law")
        else:
            require(o[n] == 0, "V05-support")
    lines.append("V05 support census and sign law n<=" + str(N_MAIN) + " PASS")

    # V06 exact summatory readouts
    spf_read = smallest_prime_factor_table(N_READ)
    partial = 0
    readouts = []
    for n in range(1, N_READ + 1):
        partial += channel_coefficient(n, spf_read)
        if n in CHECKPOINTS:
            readouts.append((n, partial))
    require(tuple(readouts) == FROZEN_READOUTS, "V06-frozen-readouts")
    for n, t5 in readouts:
        lines.append("V06 readout N=" + str(n) + " T5=" + str(t5) +
                     " isqrt(N)=" + str(math.isqrt(n)))
    lines.append("V06 frozen integer readouts, no estimate claimed PASS")

    # V07 breakers against V04
    delta = [0] * (N_MAIN + 1)
    delta[1] = 1
    without_block = dirichlet_convolution(a4, delta, N_MAIN)
    fire1 = first_difference(left, without_block, N_MAIN)
    without_l2 = dirichlet_convolution(o, ideal_count, N_MAIN)
    fire2 = first_difference(without_l2, target, N_MAIN)
    without_a4 = dirichlet_convolution(delta, block, N_MAIN)
    fire3 = first_difference(left, without_a4, N_MAIN)
    fires = (fire1, fire2, fire3)
    require(fires == BREAKER_WITNESSES, "V07-breakers")
    lines.append("V07 breakers 3/3 FIRE " +
                 ",".join(str(w) for w in fires) + " PASS")

    lines.append("VERIFY RESULT 7/7 ALL PASS")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
