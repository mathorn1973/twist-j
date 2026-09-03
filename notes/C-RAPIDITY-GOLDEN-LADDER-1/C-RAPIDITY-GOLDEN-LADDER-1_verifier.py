"""C-RAPIDITY-GOLDEN-LADDER-1 draft verifier.

STATUS NON-CANONICAL. Draft-grade note verifier per POLICY.md; it is not
a formal probe pin, creates no public status, and changes no canon file.

Exact integer and exact Z[phi] arithmetic only (phi^2 = phi + 1, elements
stored as integer pairs a + b phi). Standard library only. No floats.
Every gate is an exact equality of integers, integer pairs, or exact
Fraction linear algebra.

Gates
  V01 golden unit facts: phi-power route equals the Lucas recurrence
      L_{2(k+1)} = 3 L_{2k} - L_{2k-2}, L_0=2, L_2=3, for k<=6;
      N(phi) = -1; Pell enumeration m^2-5b^2=4, m<=322, yields exactly
      the even-index Lucas values {2,3,7,18,47,123,322}
  V02 local tables: exact Z[phi] series division of
      (1 - tau T + T^2)/(1-T) gives 1, (1-tau), (2-tau), (2-tau), ...
      for tau = +-L_{2k}, k<=4; non-split local stays 1 - T
  V03 anchor mu: the full-lift diagonal evaluation at tau = 2 equals
      the Mobius function for every n <= 100000
  V04 negative anchor: at tau = -2, on squarefree n the value is
      (-1)^(#nonsplit) 3^(#split), the signed ternary l1 census shape
  V05 shell anchor: the shell ladder at tau = 3 equals the merged
      squarefree core s_5 = mu * a_F * 1_{(n,5)=1} for every n <= 100000
  V06 layer identity: sum_{n<=x} mu^2(n) m_tau(n)
      = sum_a (1-tau)^a B_a(x) at the frozen checkpoints for
      tau in {2, 3, 7, 18, -2, -3}
  V07 Vandermonde inversion: the ladder values at tau = 2,3,7,18
      recover the layers B_a(20000), a = 0..3, exactly
  V08 connecting units: m_tau = sigma_tau * w_tau coefficientwise to
      100000 for tau = 2 and tau = 3; the split deviation of w_3 starts
      exactly at T^2 with coefficients 2-L and L(2-L); w_2 is trivial
      at split primes
  V09 exact readouts of ladder partial sums and layers (frozen)
  V10 breakers: five frozen mutations fire at their witnesses
"""

import math
import sys
from fractions import Fraction

N_MAIN = 100000
E_MAX = 8
K_MAX = 6
VAND_X = 20000
CHECKPOINTS = (1000, 10000, 100000)
LUCAS_EVEN = (2, 3, 7, 18, 47, 123, 322)
POS_TAUS = (2, 3, 7, 18)
NEG_TAUS = (-2, -3)

FROZEN_READOUTS = (
    ('Mflat', 2, 1000, 2), ('Mflat', 3, 1000, 24),
    ('Mflat', 7, 1000, 252), ('Mflat', 18, 1000, 2034),
    ('Mflat', 2, 10000, -23), ('Mflat', 3, 10000, 75),
    ('Mflat', 7, 10000, 647), ('Mflat', 18, 10000, -6855),
    ('Mflat', 2, 100000, -48), ('Mflat', 3, 100000, 483),
    ('Mflat', 7, 100000, -4473), ('Mflat', 18, 100000, -279792),
    ('Sigma', 2, 1000, -64), ('Sigma', 3, 1000, -103),
    ('Sigma', 2, 10000, -395), ('Sigma', 3, 10000, -381),
    ('Sigma', 2, 100000, -2432), ('Sigma', 3, 100000, -925),
    ('Layer', 0, 100000, -363), ('Layer', 1, 100000, -53),
    ('Layer', 2, 100000, 339), ('Layer', 3, 100000, 77),
)

# ---- exact Z[phi] arithmetic: (a, b) means a + b phi, phi^2 = phi + 1

ONE = (1, 0)
PHI = (0, 1)
PHI_INV = (-1, 1)


def zmul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zneg(x):
    return (-x[0], -x[1])


def zpow(x, n):
    r = ONE
    for _ in range(n):
        r = zmul(r, x)
    return r


def zconj(x):
    a, b = x
    return (a + b, -b)


# ---- exact series division over Z[phi]

def series_div(num, den, kmax):
    assert den[0] == ONE
    num = list(num) + [(0, 0)] * (kmax + 1 - len(num))
    out = []
    for k in range(kmax + 1):
        c = num[k]
        for j in range(k):
            if k - j < len(den):
                c = zadd(c, zneg(zmul(out[j], den[k - j])))
        out.append(c)
    return out


# ---- integer sequences

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


def lift_value(n, tau, spf):
    """Full-lift diagonal evaluation m_tau(n): split e=1 -> 1-tau,
    split e>=2 -> 2-tau, non-split e=1 -> -1, non-split e>=2 -> 0."""
    value = 1
    for p, e in factorization(n, spf):
        if chi5(p) == 1:
            value *= (1 - tau) if e == 1 else (2 - tau)
        else:
            if e >= 2:
                return 0
            value *= -1
    return value


def shell_value(n, tau, spf):
    """Shell ladder sigma_tau(n): squarefree pure-split support only."""
    value = 1
    for p, e in factorization(n, spf):
        if chi5(p) != 1 or e >= 2:
            return 0
        value *= (1 - tau)
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


def dirichlet_convolution(a, b, limit):
    c = [0] * (limit + 1)
    for i in range(1, limit + 1):
        ai = a[i]
        if ai:
            for j in range(1, limit // i + 1):
                if b[j]:
                    c[i * j] += ai * b[j]
    return c


def require(condition, label):
    if not condition:
        raise RuntimeError("FAIL " + label)


def main():
    lines = []
    lines.append("C-RAPIDITY-GOLDEN-LADDER-1 DRAFT VERIFIER")
    lines.append("STATUS NON-CANONICAL DRAFT")

    # V01 golden unit facts
    lucas = [2, 3]
    for _ in range(2, K_MAX + 1):
        lucas.append(3 * lucas[-1] - lucas[-2])
    require(tuple(lucas) == LUCAS_EVEN, "V01-lucas-recurrence")
    for k in range(K_MAX + 1):
        t = zpow(PHI, 2 * k)
        tinv = zpow(PHI_INV, 2 * k)
        require(zmul(t, tinv) == ONE, "V01-unit-inverse")
        tau = zadd(t, tinv)
        require(tau == (lucas[k], 0), "V01-phi-power-lucas")
    require(zmul(PHI, zconj(PHI)) == (-1, 0), "V01-norm-phi")
    pell = tuple(m for m in range(0, LUCAS_EVEN[-1] + 1)
                 if (m * m - 4) % 5 == 0
                 and math.isqrt((m * m - 4) // 5) ** 2 == (m * m - 4) // 5)
    require(pell == LUCAS_EVEN, "V01-pell-enumeration")
    lines.append("V01 golden unit facts k<=6, Pell m<=322 PASS")

    # V02 local tables by exact Z[phi] division
    for k in range(0, 5):
        for sign in (1, -1):
            tau_int = sign * lucas[k]
            tau = (tau_int, 0)
            num = [ONE, zneg(tau), ONE]
            den = [ONE, zneg(ONE)]
            series = series_div(num, den, E_MAX)
            expected = [ONE, (1 - tau_int, 0)] + [(2 - tau_int, 0)] * (E_MAX - 1)
            require(series == expected, "V02-split-local")
    nonsplit = series_div([ONE, (0, 0), zneg(ONE)], [ONE, ONE], E_MAX)
    require(nonsplit == [ONE, zneg(ONE)] + [(0, 0)] * (E_MAX - 1),
            "V02-nonsplit-local")
    lines.append("V02 local tables tau=+-L_2k k<=4 e<=" + str(E_MAX) + " PASS")

    # sequences
    spf = smallest_prime_factor_table(N_MAIN)
    mu = mobius_table(N_MAIN, spf)

    # V03 anchor mu
    for n in range(1, N_MAIN + 1):
        require(lift_value(n, 2, spf) == mu[n], "V03-mu-anchor")
    lines.append("V03 full-lift ladder at tau=2 equals mu n<=" +
                 str(N_MAIN) + " PASS")

    # V04 negative anchor: signed ternary census shape on squarefree n
    for n in range(1, N_MAIN + 1):
        factors = factorization(n, spf) if n > 1 else []
        if any(e > 1 for _, e in factors):
            continue
        a = sum(1 for p, _ in factors if chi5(p) == 1)
        b = len(factors) - a
        expected = (3 ** a) * (-1 if b % 2 else 1)
        require(lift_value(n, -2, spf) == expected, "V04-ternary-anchor")
    lines.append("V04 full-lift ladder at tau=-2 is (-1)^b 3^a on"
                 " squarefree n<=" + str(N_MAIN) + " PASS")

    # V05 shell anchor: sigma at tau=3 equals the merged squarefree core
    one = [0] + [1] * N_MAIN
    chi = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        chi[n] = chi5(n)
    ideal_count = dirichlet_convolution(one, chi, N_MAIN)
    for n in range(1, N_MAIN + 1):
        core = mu[n] * ideal_count[n] * (1 if n % 5 else 0)
        require(shell_value(n, 3, spf) == core, "V05-shell-core")
    lines.append("V05 shell ladder at tau=3 equals s_5 = mu a_F"
                 " 1_(5!|n) n<=" + str(N_MAIN) + " PASS")

    # layers B_a(x) over squarefree n
    max_a = 0
    layer_rows = {}
    layers = [0] * 12
    vand_layers = None
    max_a_vand = 0
    for n in range(1, N_MAIN + 1):
        factors = factorization(n, spf) if n > 1 else []
        if not any(e > 1 for _, e in factors):
            a = sum(1 for p, _ in factors if chi5(p) == 1)
            b = len(factors) - a
            layers[a] += -1 if b % 2 else 1
            if a > max_a:
                max_a = a
        if n == VAND_X:
            vand_layers = layers[:]
            max_a_vand = max_a
        if n in CHECKPOINTS:
            layer_rows[n] = layers[:]

    # V06 layer identity for the squarefree-restricted full-lift ladder
    taus = POS_TAUS + NEG_TAUS
    ladder_rows = {x: {} for x in CHECKPOINTS}
    for tau in taus:
        partial = 0
        for n in range(1, N_MAIN + 1):
            if mu[n] != 0:
                partial += lift_value(n, tau, spf)
            if n in CHECKPOINTS:
                ladder_rows[n][tau] = partial
    for x in CHECKPOINTS:
        for tau in taus:
            z = 1 - tau
            rhs = sum((z ** a) * layer_rows[x][a] for a in range(max_a + 1))
            require(ladder_rows[x][tau] == rhs, "V06-layer-identity")
    lines.append("V06 layer identity taus " +
                 ",".join(str(t) for t in taus) + " PASS")

    # V07 Vandermonde inversion at x = VAND_X with nodes from tau=2,3,7,18
    require(max_a_vand == 3, "V07-layer-depth")
    nodes = [1 - tau for tau in POS_TAUS]
    values = []
    for tau in POS_TAUS:
        partial = 0
        for n in range(1, VAND_X + 1):
            if mu[n] != 0:
                partial += lift_value(n, tau, spf)
        values.append(partial)
    size = len(nodes)
    matrix = [[Fraction(nodes[i] ** a) for a in range(size)]
              for i in range(size)]
    rhs_vec = [Fraction(v) for v in values]
    for col in range(size):
        pivot = next(r for r in range(col, size) if matrix[r][col] != 0)
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        rhs_vec[col], rhs_vec[pivot] = rhs_vec[pivot], rhs_vec[col]
        inv = 1 / matrix[col][col]
        matrix[col] = [v * inv for v in matrix[col]]
        rhs_vec[col] = rhs_vec[col] * inv
        for r in range(size):
            if r != col and matrix[r][col] != 0:
                factor = matrix[r][col]
                matrix[r] = [matrix[r][j] - factor * matrix[col][j]
                             for j in range(size)]
                rhs_vec[r] = rhs_vec[r] - factor * rhs_vec[col]
    recovered = [rhs_vec[a] for a in range(size)]
    for a in range(size):
        require(recovered[a] == Fraction(vand_layers[a]),
                "V07-vandermonde-inversion")
    lines.append("V07 Vandermonde recovers B_0..B_3 at x=" +
                 str(VAND_X) + " PASS")

    # V08 connecting units m_tau = sigma_tau * w_tau
    def w_split_series(tau_int, kmax):
        m_series = series_div([(1, 0), (-tau_int, 0), (1, 0)],
                              [(1, 0), (-1, 0)], kmax)
        return series_div(m_series, [(1, 0), (1 - tau_int, 0)], kmax)

    for tau in (2, 3):
        wsplit = w_split_series(tau, E_MAX)
        require(wsplit[0] == (1, 0), "V08-w-degree")
        require(all(wsplit[e] == (1 - (tau - 1) ** (e - 1), 0)
                    for e in range(1, E_MAX + 1)), "V08-closed-form")
        if tau == 2:
            require(all(c == (0, 0) for c in wsplit[1:]), "V08-w2-trivial")
        wcoef = [c[0] for c in wsplit]

        def w_value(n):
            value = 1
            for p, e in factorization(n, spf):
                if chi5(p) == 1:
                    if e > E_MAX:
                        raise RuntimeError("FAIL V08-exponent-range")
                    value *= wcoef[e]
                else:
                    if e >= 2:
                        return 0
                    value *= -1
            return value

        w_table = [0] * (N_MAIN + 1)
        sigma_table = [0] * (N_MAIN + 1)
        m_table = [0] * (N_MAIN + 1)
        for n in range(1, N_MAIN + 1):
            w_table[n] = w_value(n)
            sigma_table[n] = shell_value(n, tau, spf)
            m_table[n] = lift_value(n, tau, spf)
        require(dirichlet_convolution(sigma_table, w_table, N_MAIN)
                == m_table, "V08-connecting-unit")
    lines.append("V08 m_tau = sigma_tau * w_tau tau=2,3 n<=" +
                 str(N_MAIN) + " PASS")

    # V09 readouts
    readouts = []
    for x in CHECKPOINTS:
        for tau in POS_TAUS:
            readouts.append(("Mflat", tau, x, ladder_rows[x][tau]))
    sigma_partial = {2: 0, 3: 0}
    for n in range(1, N_MAIN + 1):
        for tau in (2, 3):
            sigma_partial[tau] += shell_value(n, tau, spf)
        if n in CHECKPOINTS:
            for tau in (2, 3):
                readouts.append(("Sigma", tau, n, sigma_partial[tau]))
    for a in range(max_a + 1):
        readouts.append(("Layer", a, N_MAIN, layer_rows[N_MAIN][a]))
    require(tuple(readouts) == FROZEN_READOUTS, "V09-frozen-readouts")
    for kind, idx, x, value in readouts:
        lines.append("V09 readout " + kind + " " + str(idx) + " x=" +
                     str(x) + " value=" + str(value))
    lines.append("V09 exact readouts, no estimate claimed PASS")

    # V10 breakers
    fires = []
    diff = 0
    for n in range(1, N_MAIN + 1):
        core = mu[n] * ideal_count[n] * (1 if n % 5 else 0)
        if shell_value(n, 4, spf) != core:
            diff = n
            break
    fires.append(diff)          # B1 wrong Lucas value tau=4
    diff = 0
    for n in range(1, N_MAIN + 1):
        value = 1
        for p, e in factorization(n, spf):
            if chi5(p) == 1:
                value *= (1 - 2) if e == 1 else 0
            else:
                if e >= 2:
                    value = 0
                else:
                    value *= 1  # B2 inert sign dropped: -1 replaced by +1
        if n > 1 and value != mu[n]:
            diff = n
            break
    fires.append(diff)          # B2
    tau_phi = zadd(PHI, PHI_INV)
    tau_phi3 = zadd(zpow(PHI, 3), zpow(PHI_INV, 3))
    fires.append(1 if (tau_phi[1] != 0 and tau_phi3[1] != 0) else 0)  # B3
    near = [m for m in (4, 8) if (m * m - 4) % 5 == 0
            and math.isqrt((m * m - 4) // 5) ** 2 == (m * m - 4) // 5]
    fires.append(1 if near == [] else 0)                              # B4
    bad_nodes = [-1, -2, -6, -1]
    bad_matrix = [[Fraction(bad_nodes[i] ** a) for a in range(4)]
                  for i in range(4)]
    singular = 0
    for col in range(4):
        pivot = next((r for r in range(col, 4)
                      if bad_matrix[r][col] != 0), None)
        if pivot is None:
            singular = 1
            break
        bad_matrix[col], bad_matrix[pivot] = (bad_matrix[pivot],
                                              bad_matrix[col])
        inv = 1 / bad_matrix[col][col]
        bad_matrix[col] = [v * inv for v in bad_matrix[col]]
        for r in range(4):
            if r != col and bad_matrix[r][col] != 0:
                factor = bad_matrix[r][col]
                bad_matrix[r] = [bad_matrix[r][j]
                                 - factor * bad_matrix[col][j]
                                 for j in range(4)]
    fires.append(singular)                                            # B5
    require(tuple(fires) == (11, 2, 1, 1, 1), "V10-breakers")
    lines.append("V10 breakers 5/5 FIRE 11,2,phi-odd,near-miss,singular"
                 " PASS")

    lines.append("VERIFY RESULT 10/10 ALL PASS")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
