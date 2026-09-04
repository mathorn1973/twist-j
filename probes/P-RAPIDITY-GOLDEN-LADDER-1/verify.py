#!/usr/bin/env python3
"""P-RAPIDITY-GOLDEN-LADDER-1 exact audit.

Frozen scope:
  * golden unit facts: the even-index Lucas recurrence, unit inverses in
    Z[phi], N(phi) = -1, and the Pell enumeration m^2 - 5 b^2 = 4 through
    m = 322;
  * exact Z[phi] local tables of the diagonal evaluations tau = +-L_2k;
  * the anchors: tau = 2 is mu, tau = -2 is the signed ternary census on
    squarefree n, and the shell rung tau = 3 is the squarefree core s_5;
  * the layer identity and its finite Vandermonde inversion;
  * the connecting units m_tau = sigma_tau * w_tau with closed form;
  * frozen exact integer readouts;
  * a standard-library-only exact-arithmetic source firewall;
  * five production-path negative controls at frozen witnesses.

Exact integers, exact Z[phi] pairs (a, b) meaning a + b phi with
phi^2 = phi + 1, and exact Fractions only.  No analytic continuation,
zeta zero, RH/GRH, summatory estimate, floating point, or external data.
"""

from __future__ import annotations

import ast
import math
import sys
from fractions import Fraction
from pathlib import Path


N_MAIN = 100_000
E_MAX = 8
K_MAX = 6
VAND_X = 20_000
CHECKPOINTS = (1_000, 10_000, 100_000)
LUCAS_EVEN = (2, 3, 7, 18, 47, 123, 322)
POS_TAUS = (2, 3, 7, 18)
NEG_TAUS = (-2, -3)
PELL_NEAR_MISSES = (4, 8)
BAD_NODES = (-1, -2, -6, -1)
BREAKER_WITNESSES = (11, 2, 1, 1, 1)
ALLOWED_IMPORTS = {"__future__", "ast", "fractions", "math", "pathlib", "sys"}
FORBIDDEN_CALLS = {
    "__import__", "compile", "complex", "eval", "exec", "float", "open",
}

FROZEN_READOUTS = (
    ("Mflat", 2, 1_000, 2), ("Mflat", 3, 1_000, 24),
    ("Mflat", 7, 1_000, 252), ("Mflat", 18, 1_000, 2034),
    ("Mflat", 2, 10_000, -23), ("Mflat", 3, 10_000, 75),
    ("Mflat", 7, 10_000, 647), ("Mflat", 18, 10_000, -6855),
    ("Mflat", 2, 100_000, -48), ("Mflat", 3, 100_000, 483),
    ("Mflat", 7, 100_000, -4473), ("Mflat", 18, 100_000, -279792),
    ("Sigma", 2, 1_000, -64), ("Sigma", 3, 1_000, -103),
    ("Sigma", 2, 10_000, -395), ("Sigma", 3, 10_000, -381),
    ("Sigma", 2, 100_000, -2432), ("Sigma", 3, 100_000, -925),
    ("Layer", 0, 100_000, -363), ("Layer", 1, 100_000, -53),
    ("Layer", 2, 100_000, 339), ("Layer", 3, 100_000, 77),
)


# ---- exact Z[phi] arithmetic: (a, b) means a + b phi, phi^2 = phi + 1

ONE = (1, 0)
ZERO = (0, 0)
PHI = (0, 1)
PHI_INV = (-1, 1)


def zmul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def zadd(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return (x[0] + y[0], x[1] + y[1])


def zneg(x: tuple[int, int]) -> tuple[int, int]:
    return (-x[0], -x[1])


def zpow(x: tuple[int, int], n: int) -> tuple[int, int]:
    r = ONE
    for _ in range(n):
        r = zmul(r, x)
    return r


def zconj(x: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    return (a + b, -b)


# ---- exact formal power-series division over Z[phi]

def series_div(num: list, den: list, kmax: int) -> list:
    require(den[0] == ONE, "series-div-unit-constant")
    num = list(num) + [ZERO] * (kmax + 1 - len(num))
    out: list = []
    for k in range(kmax + 1):
        c = num[k]
        for j in range(k):
            if k - j < len(den):
                c = zadd(c, zneg(zmul(out[j], den[k - j])))
        out.append(c)
    return out


# ---- integer sequences

CHI5 = (0, 1, -1, -1, 1)


def chi5(n: int) -> int:
    return CHI5[n % 5]


def is_split(p: int) -> bool:
    return chi5(p) == 1


def smallest_prime_factor_table(limit: int) -> list[int]:
    table = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if table[i] == i:
            for j in range(i * i, limit + 1, i):
                if table[j] == j:
                    table[j] = i
        i += 1
    return table


def factorization(n: int, spf: list[int]) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        factors.append((p, e))
    return factors


def lift_value(factors: list[tuple[int, int]], tau: int,
               nonsplit_sign: int = -1) -> int:
    """Full-lift diagonal evaluation m_tau(n) from its frozen local table:
    split e=1 -> 1-tau, split e>=2 -> 2-tau, non-split e=1 -> -1,
    non-split e>=2 -> 0.  The non-split sign is a parameter only so that
    breaker B2 can route its mutation through this production path."""
    value = 1
    for p, e in factors:
        if is_split(p):
            value *= (1 - tau) if e == 1 else (2 - tau)
        else:
            if e >= 2:
                return 0
            value *= nonsplit_sign
    return value


def shell_value(factors: list[tuple[int, int]], tau: int) -> int:
    """Shell ladder sigma_tau(n): squarefree pure-split support only."""
    value = 1
    for p, e in factors:
        if not is_split(p) or e >= 2:
            return 0
        value *= (1 - tau)
    return value


def mobius(factors: list[tuple[int, int]]) -> int:
    if any(e > 1 for _, e in factors):
        return 0
    return -1 if len(factors) % 2 else 1


def dirichlet_convolution(a: list[int], b: list[int], limit: int) -> list[int]:
    c = [0] * (limit + 1)
    for i in range(1, limit + 1):
        ai = a[i]
        if ai:
            for j in range(1, limit // i + 1):
                if b[j]:
                    c[i * j] += ai * b[j]
    return c


def pell_solvable(m: int) -> bool:
    """Exact test whether m^2 - 5 b^2 = 4 has an integer solution b."""
    rest = m * m - 4
    if rest < 0 or rest % 5:
        return False
    q = rest // 5
    return math.isqrt(q) ** 2 == q


def vandermonde_solve(nodes: list[int], values: list[int]):
    """Exact Gauss-Jordan solve of sum_a c_a node_i^a = value_i over Q.
    Returns the coefficient list, or None when the system is singular."""
    size = len(nodes)
    matrix = [[Fraction(nodes[i] ** a) for a in range(size)]
              for i in range(size)]
    rhs = [Fraction(v) for v in values]
    for col in range(size):
        pivot = next((r for r in range(col, size) if matrix[r][col] != 0),
                     None)
        if pivot is None:
            return None
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        rhs[col], rhs[pivot] = rhs[pivot], rhs[col]
        inv = 1 / matrix[col][col]
        matrix[col] = [v * inv for v in matrix[col]]
        rhs[col] = rhs[col] * inv
        for r in range(size):
            if r != col and matrix[r][col] != 0:
                factor = matrix[r][col]
                matrix[r] = [matrix[r][j] - factor * matrix[col][j]
                             for j in range(size)]
                rhs[r] = rhs[r] - factor * rhs[col]
    return rhs


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError("FAIL " + label)


def gate_source_firewall() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    require(source.isascii(), "G10-ascii")
    require("\r" not in source, "G10-lf-only")
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                require(alias.name.split(".")[0] in ALLOWED_IMPORTS,
                        "G10-import")
        elif isinstance(node, ast.ImportFrom):
            require((node.module or "").split(".")[0] in ALLOWED_IMPORTS,
                    "G10-import-from")
        elif isinstance(node, ast.Constant):
            require(not isinstance(node.value, (float, complex)),
                    "G10-inexact-constant")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in FORBIDDEN_CALLS, "G10-call")


def main() -> int:
    lines: list[str] = []

    # G01 golden unit facts.
    lucas = [2, 3]
    for _ in range(2, K_MAX + 1):
        lucas.append(3 * lucas[-1] - lucas[-2])
    require(tuple(lucas) == LUCAS_EVEN, "G01-lucas-recurrence")
    for k in range(K_MAX + 1):
        t = zpow(PHI, 2 * k)
        tinv = zpow(PHI_INV, 2 * k)
        require(zmul(t, tinv) == ONE, "G01-unit-inverse")
        require(zconj(t) == tinv, "G01-norm-one-conjugate")
        require(zadd(t, tinv) == (lucas[k], 0), "G01-phi-power-lucas")
        require(zadd(zneg(t), zneg(tinv)) == (-lucas[k], 0),
                "G01-negative-rung")
    require(zmul(PHI, zconj(PHI)) == (-1, 0), "G01-norm-phi")
    require(zmul(PHI, PHI_INV) == ONE, "G01-phi-inverse")
    pell = tuple(m for m in range(0, LUCAS_EVEN[-1] + 1) if pell_solvable(m))
    require(pell == LUCAS_EVEN, "G01-pell-enumeration")
    lines.append("G01 PASS golden unit facts k<=" + str(K_MAX) +
                 ", Pell m^2-5b^2=4 enumeration m<=" + str(LUCAS_EVEN[-1]))

    # G02 local tables by exact Z[phi] series division.
    for k in range(0, 5):
        for sign in (1, -1):
            tau_int = sign * lucas[k]
            t = zpow(PHI, 2 * k)
            if sign == -1:
                t = zneg(t)
            tinv = zconj(t)
            require(zmul(t, tinv) == ONE, "G02-evaluation-unit")
            require(zadd(t, tinv) == (tau_int, 0), "G02-tau-from-t")
            num = [ONE, zneg(zadd(t, tinv)), zmul(t, tinv)]
            den = [ONE, zneg(ONE)]
            series = series_div(num, den, E_MAX)
            expected = ([ONE, (1 - tau_int, 0)]
                        + [(2 - tau_int, 0)] * (E_MAX - 1))
            require(series == expected, "G02-split-local")
    nonsplit = series_div([ONE, ZERO, zneg(ONE)], [ONE, ONE], E_MAX)
    require(nonsplit == [ONE, zneg(ONE)] + [ZERO] * (E_MAX - 1),
            "G02-nonsplit-local")
    lines.append("G02 PASS local tables tau=+-L_2k k<=4 e<=" + str(E_MAX) +
                 " by exact Z[phi] division")

    # Exact arithmetic tables, built once.
    spf = smallest_prime_factor_table(N_MAIN)
    factors = [factorization(n, spf) if n else [] for n in range(N_MAIN + 1)]
    mu = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        mu[n] = mobius(factors[n])

    # G03 anchor: tau = 2 is mu.
    for n in range(1, N_MAIN + 1):
        require(lift_value(factors[n], 2) == mu[n], "G03-mu-anchor")
    lines.append("G03 PASS full-lift ladder at tau=2 equals mu through n=" +
                 str(N_MAIN))

    # G04 anchor: tau = -2 is (-1)^b 3^a on squarefree n.
    for n in range(1, N_MAIN + 1):
        if mu[n] == 0:
            continue
        a = sum(1 for p, _ in factors[n] if is_split(p))
        b = len(factors[n]) - a
        expected = (3 ** a) * (-1 if b % 2 else 1)
        require(lift_value(factors[n], -2) == expected, "G04-ternary-anchor")
    lines.append("G04 PASS full-lift ladder at tau=-2 is (-1)^b 3^a on"
                 " squarefree n through n=" + str(N_MAIN))

    # G05 shell anchor: sigma_3 equals s_5 = mu * a_F * 1_(5 nmid n).
    one = [0] + [1] * N_MAIN
    chi = [0] * (N_MAIN + 1)
    for n in range(1, N_MAIN + 1):
        chi[n] = chi5(n)
    ideal_count = dirichlet_convolution(one, chi, N_MAIN)
    for n in range(1, N_MAIN + 1):
        core = mu[n] * ideal_count[n] * (1 if n % 5 else 0)
        require(shell_value(factors[n], 3) == core, "G05-shell-core")
    lines.append("G05 PASS shell ladder at tau=3 equals s_5 = mu a_F"
                 " 1_(5nmid) through n=" + str(N_MAIN))

    # Layers B_a(x) over squarefree n, recorded at the frozen checkpoints.
    max_a = 0
    layers = [0] * 12
    layer_rows: dict[int, list[int]] = {}
    vand_layers: list[int] = []
    max_a_vand = 0
    for n in range(1, N_MAIN + 1):
        if mu[n] != 0:
            a = sum(1 for p, _ in factors[n] if is_split(p))
            b = len(factors[n]) - a
            layers[a] += -1 if b % 2 else 1
            if a > max_a:
                max_a = a
        if n == VAND_X:
            vand_layers = layers[:]
            max_a_vand = max_a
        if n in CHECKPOINTS:
            layer_rows[n] = layers[:]

    # G06 layer identity for the squarefree-restricted full-lift ladder.
    taus = POS_TAUS + NEG_TAUS
    ladder_rows: dict[int, dict[int, int]] = {x: {} for x in CHECKPOINTS}
    vand_values: dict[int, int] = {}
    for tau in taus:
        partial = 0
        for n in range(1, N_MAIN + 1):
            if mu[n] != 0:
                partial += lift_value(factors[n], tau)
            if n == VAND_X:
                vand_values[tau] = partial
            if n in CHECKPOINTS:
                ladder_rows[n][tau] = partial
    for x in CHECKPOINTS:
        for tau in taus:
            z = 1 - tau
            rhs = sum((z ** a) * layer_rows[x][a] for a in range(max_a + 1))
            require(ladder_rows[x][tau] == rhs, "G06-layer-identity")
    lines.append("G06 PASS layer identity taus " +
                 ",".join(str(t) for t in taus) + " at x=" +
                 ",".join(str(x) for x in CHECKPOINTS))

    # G07 Vandermonde inversion at x = VAND_X from the rungs tau = 2,3,7,18.
    require(max_a_vand == 3, "G07-layer-depth")
    nodes = [1 - tau for tau in POS_TAUS]
    require(len(set(nodes)) == len(nodes), "G07-distinct-nodes")
    recovered = vandermonde_solve(nodes, [vand_values[tau] for tau in POS_TAUS])
    require(recovered is not None, "G07-nonsingular")
    for a in range(len(nodes)):
        require(recovered[a] == Fraction(vand_layers[a]),
                "G07-vandermonde-inversion")
    lines.append("G07 PASS Vandermonde at nodes " +
                 ",".join(str(z) for z in nodes) + " recovers B_0..B_3 at x=" +
                 str(VAND_X))

    # G08 connecting units m_tau = sigma_tau * w_tau, with closed form.
    for tau in (2, 3):
        m_series = series_div([ONE, (-tau, 0), ONE], [ONE, (-1, 0)], E_MAX)
        wsplit = series_div(m_series, [ONE, (1 - tau, 0)], E_MAX)
        require(wsplit[0] == ONE, "G08-w-constant-term")
        require(all(wsplit[e] == (1 - (tau - 1) ** (e - 1), 0)
                    for e in range(1, E_MAX + 1)), "G08-closed-form")
        if tau == 2:
            require(all(c == ZERO for c in wsplit[1:]), "G08-w2-trivial")
        wcoef = [c[0] for c in wsplit]
        w_table = [0] * (N_MAIN + 1)
        sigma_table = [0] * (N_MAIN + 1)
        m_table = [0] * (N_MAIN + 1)
        for n in range(1, N_MAIN + 1):
            value = 1
            for p, e in factors[n]:
                if is_split(p):
                    require(e <= E_MAX, "G08-exponent-range")
                    value *= wcoef[e]
                else:
                    if e >= 2:
                        value = 0
                        break
                    value *= -1
            w_table[n] = value
            sigma_table[n] = shell_value(factors[n], tau)
            m_table[n] = lift_value(factors[n], tau)
        require(dirichlet_convolution(sigma_table, w_table, N_MAIN)
                == m_table, "G08-connecting-unit")
    lines.append("G08 PASS m_tau = sigma_tau * w_tau tau=2,3 through n=" +
                 str(N_MAIN) + ", split coefficients 1-(tau-1)^(e-1)")

    # G09 frozen exact readouts.
    readouts: list = []
    for x in CHECKPOINTS:
        for tau in POS_TAUS:
            readouts.append(("Mflat", tau, x, ladder_rows[x][tau]))
    sigma_partial = {2: 0, 3: 0}
    for n in range(1, N_MAIN + 1):
        for tau in (2, 3):
            sigma_partial[tau] += shell_value(factors[n], tau)
        if n in CHECKPOINTS:
            for tau in (2, 3):
                readouts.append(("Sigma", tau, n, sigma_partial[tau]))
    for a in range(max_a + 1):
        readouts.append(("Layer", a, N_MAIN, layer_rows[N_MAIN][a]))
    require(tuple(readouts) == FROZEN_READOUTS, "G09-frozen-readouts")
    for kind, idx, x, value in readouts:
        lines.append("G09 readout " + kind + " " + str(idx) + " x=" +
                     str(x) + " value=" + str(value))
    lines.append("G09 PASS exact readouts frozen, no estimate claimed")

    # G10 source firewall.
    gate_source_firewall()
    lines.append("G10 PASS stdlib-only exact-arithmetic source firewall")

    # G11 breakers, each routed through the production constructors.
    fires: list[int] = []
    witness = 0
    for n in range(1, N_MAIN + 1):
        core = mu[n] * ideal_count[n] * (1 if n % 5 else 0)
        if shell_value(factors[n], 4) != core:
            witness = n
            break
    fires.append(witness)                       # B1 wrong Lucas value
    witness = 0
    for n in range(1, N_MAIN + 1):
        if lift_value(factors[n], 2, nonsplit_sign=1) != mu[n]:
            witness = n
            break
    fires.append(witness)                       # B2 non-split sign +1
    tau_phi = zadd(PHI, PHI_INV)
    tau_phi3 = zadd(zpow(PHI, 3), zpow(PHI_INV, 3))
    require(tau_phi == (-1, 2), "G11-B3-phi-witness")
    require(tau_phi3 == (-2, 4), "G11-B3-phi3-witness")
    fires.append(1 if (tau_phi[1] != 0 and tau_phi3[1] != 0) else 0)  # B3
    fires.append(1 if not any(pell_solvable(m) for m in PELL_NEAR_MISSES)
                 else 0)                        # B4 Pell near-misses
    fires.append(1 if vandermonde_solve(list(BAD_NODES), [0, 0, 0, 0]) is None
                 else 0)                        # B5 repeated node
    require(tuple(fires) == BREAKER_WITNESSES, "G11-breakers")
    lines.append("G11 PASS breakers FIRE B1=11 B2=2 B3=phi-odd"
                 " B4=near-miss B5=singular")

    lines.append("VERIFY RESULT 11/11 ALL PASS")
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
