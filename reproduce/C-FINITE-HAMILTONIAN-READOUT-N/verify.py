#!/usr/bin/env python3
"""Exact small audit of the analytical Hamiltonian/readout construction.

Standard library only. No floating-point amplitudes, numerical evolution,
physical-source simulation or claim of independent proof acceptance.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb
import sys

CHECKS = 0


def require(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def zero(n: int, m: int | None = None) -> list[list[F]]:
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def identity(n: int) -> list[list[F]]:
    a = zero(n)
    for j in range(n):
        a[j][j] = F(1)
    return a


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(r) for r in zip(*a)]


def mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    out = zero(len(a), len(b[0]))
    for r, row in enumerate(a):
        for k, av in enumerate(row):
            if av:
                for c, bv in enumerate(b[k]):
                    if bv:
                        out[r][c] += av * bv
    return out


def add_scaled(a: list[list[F]], b: list[list[F]], factor: F) -> list[list[F]]:
    return [[x + factor * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a: list[list[F]], q: F) -> list[list[F]]:
    return [[q * x for x in row] for row in a]


def clock_raw(m: int) -> list[list[F]]:
    a = zero(m + 1)
    for j in range(m):
        a[j + 1][j] = F(j + 1)
        a[j][j + 1] = F(m - j)
    return a


def clock_audit() -> None:
    for m in range(1, 7):
        n = m + 1
        a = clock_raw(m)
        gram = [F(comb(m, j)) for j in range(n)]
        for r in range(n):
            for c in range(n):
                require(gram[r] * a[r][c] == gram[c] * a[c][r], 'weighted Hermiticity')
        eig = [m - 2 * r for r in range(n)]
        ann = identity(n)
        for lam in eig:
            ann = mul(ann, add_scaled(a, identity(n), F(-lam)))
        require(ann == zero(n), 'exact integer spectral polynomial')
        # At time pi/2 the phase is (-i)^m times (-1)^r on eigenvalue m-2r.
        mirror_poly = zero(n)
        for r, lam in enumerate(eig):
            term = identity(n)
            denominator = 1
            for k, other in enumerate(eig):
                if k != r:
                    term = mul(term, add_scaled(a, identity(n), F(-other)))
                    denominator *= lam - other
            mirror_poly = add_scaled(mirror_poly, term, F((-1) ** r, denominator))
        mirror = zero(n)
        for j in range(n):
            mirror[m - j][j] = F(1)
        require(mirror_poly == mirror, 'exact endpoint and mirror polynomial')
        require(mul(mirror_poly, mirror_poly) == identity(n), 'mirror is involutive')
        require(a[0][0] == 0 and mul(a, a)[0][0] == m, 'localized clock generator variance is m')
        for s, c in [(F(0), F(1)), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(1), F(0))]:
            total = sum(F(comb(m, j)) * s ** (2 * j) * c ** (2 * (m - j)) for j in range(n))
            require(total == 1, 'binomial history normalization')
        require(a[1][0] != 0 and a[0][1] != 0, 'both Hermitian edge orientations present')
        require(gram[1] * a[1][0] != 0, 'forward-only edge fails weighted Hermiticity')


def toy_word() -> tuple[list[list[list[F]]], list[tuple[int, int, int]], list[int]]:
    # Data = physical qubit p, retained intermediate h, and final flag f.
    basis = [(p, h, f) for p in range(2) for h in range(2) for f in range(2)]
    index = {st: j for j, st in enumerate(basis)}
    rot = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    prep = zero(8)
    controlled = zero(8)
    mark = zero(8)
    for p, h, f in basis:
        c = index[p, h, f]
        for hp in range(2):
            prep[index[p, hp, f]][c] = rot[hp][h]
        for pp in range(2):
            controlled[index[pp, h, f]][c] = rot[pp][p] if h else F(pp == p)
        mark[index[p, h, f ^ h]][c] = F(1)
    gates = [mul(controlled, prep), mark, identity(8), identity(8)]
    energies = [h + f for p, h, f in basis]
    for g in gates:
        require(mul(transpose(g), g) == identity(8), 'whole toy gate unitary')
        for r in range(8):
            for c in range(8):
                if g[r][c]:
                    require(abs(energies[r] - energies[c]) <= 1, 'named gate energy change <=1')
    return gates, basis, energies


def inner_sparse(a: dict[int, F], b: dict[int, F]) -> F:
    return sum((v * b.get(k, F(0)) for k, v in a.items()), F(0))


def energy_and_channel_audit() -> None:
    gates, basis, energies = toy_word()
    d, m, l = len(basis), len(gates), 2
    q = m + max(energies)
    prefixes = [identity(d)]
    for g in gates:
        prefixes.append(mul(g, prefixes[-1]))
    for j, g in enumerate(gates):
        require(mul(prefixes[j + 1], transpose(prefixes[j])) == g, 'labelled clock gauge identity')
    for j in range(l, m + 1):
        require(prefixes[j] == prefixes[l], 'identity tail has one completed data word')
    input_indices = [basis.index((p, 0, 0)) for p in range(2)]
    for j in range(l):
        require(all(prefixes[j][r][c] == 0 for r, st in enumerate(basis) if st[2] for c in input_indices),
                'final flag is zero at every incomplete ready prefix')

    def bi(a: int, n: int) -> int:
        return a * (q + 1) + n

    # Each finite E_j is the compression of an explicit unitary on a larger
    # cyclic battery. The extra two levels prevent wrap into the kept range.
    extended_size = q + 3
    finite_edges = []
    for g in gates:
        ext_columns: list[dict[int, F]] = []
        for a in range(d):
            for n in range(extended_size):
                col = {}
                for b in range(d):
                    if g[b][a]:
                        shift = 1 + energies[b] - energies[a]
                        col[b * extended_size + ((n - shift) % extended_size)] = g[b][a]
                ext_columns.append(col)
        for a in range(len(ext_columns)):
            for b in range(a + 1):
                require(inner_sparse(ext_columns[a], ext_columns[b]) == F(a == b),
                        'unitary cyclic extension of battery edge')
        finite = {}
        for a in range(d):
            for n in range(q + 1):
                col = ext_columns[a * extended_size + n]
                for b in range(d):
                    if g[b][a]:
                        shift = 1 + energies[b] - energies[a]
                        np = n - shift
                        require(0 <= shift <= 2, 'battery edge shift range')
                        if 0 <= np <= q:
                            finite[bi(b, np), bi(a, n)] = g[b][a]
                compressed = {bi(r // extended_size, r % extended_size): v for r, v in col.items()
                              if r % extended_size <= q}
                direct = {r: v for (r, c), v in finite.items() if c == bi(a, n)}
                require(compressed == direct, 'finite edge equals unitary compression')
        finite_edges.append(finite)

    per_clock = d * (q + 1)
    full_dim = (m + 1) * per_clock
    kf = {}
    for j, e in enumerate(finite_edges):
        for (r, c), v in e.items():
            kf[(j + 1) * per_clock + r, j * per_clock + c] = F(j + 1) * v
            kf[j * per_clock + c, (j + 1) * per_clock + r] = F(m - j) * v

    def decode(k: int) -> tuple[int, int, int]:
        j, rest = divmod(k, per_clock)
        a, n = divmod(rest, q + 1)
        return j, a, n

    for (r, c), v in kf.items():
        jr, ar, nr = decode(r)
        jc, ac, nc = decode(c)
        require(jr + energies[ar] + nr == jc + energies[ac] + nc,
                'all-sector additive energy conservation including boundaries')
        require(F(comb(m, jr)) * v == F(comb(m, jc)) * kf.get((c, r), F(0)),
                'complete weighted Hermiticity of finite funded generator')

    kl = zero((m + 1) * d)
    for j, g in enumerate(gates):
        for r in range(d):
            for c in range(d):
                kl[(j + 1) * d + r][j * d + c] = F(j + 1) * g[r][c]
                kl[j * d + c][(j + 1) * d + r] = F(m - j) * g[r][c]
    sector = {j * d + a: j * per_clock + bi(a, q - j - energies[a])
              for j in range(m + 1) for a in range(d)}
    for c in range((m + 1) * d):
        expected = {sector[r]: kl[r][c] for r in range((m + 1) * d) if kl[r][c]}
        actual = {r: v for (r, k), v in kf.items() if k == sector[c]}
        require(actual == expected, 'K_f J_Q = J_Q K on every sector matrix column')
    require(len(sector) == (m + 1) * d and full_dim > len(sector), 'full edge sectors retained')

    # Compare linear maps on ALL physical input matrix units. Reference
    # extension follows mathematically; these tests do not sample pure states only.
    for sin_theta, cos_theta in [(F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(1), F(0))]:
        weights = [F(comb(m, j)) * sin_theta ** (2 * j) * cos_theta ** (2 * (m - j))
                   for j in range(m + 1)]
        completed = sum(weights[l:])
        for ia in input_indices:
            for ib in input_indices:
                actual = zero(2)
                target = zero(2)
                for ra, sa in enumerate(basis):
                    for rb, sb in enumerate(basis):
                        if not sa[2] or not sb[2] or sa[1:] != sb[1:]:
                            continue
                        target[sa[0]][sb[0]] += prefixes[l][ra][ia] * prefixes[l][rb][ib]
                        for j in range(m + 1):
                            na, nb = q - j - energies[ra], q - j - energies[rb]
                            if na == nb:
                                actual[sa[0]][sb[0]] += weights[j] * prefixes[j][ra][ia] * prefixes[j][rb][ib]
                require(actual == scale(target, completed), 'exact accepted reduced matrix-unit channel')
        require(completed > 0, 'declared toy read has nonzero completed weight')

    # Negative control: counting physical output energy creates distinguishable
    # battery states and destroys a physical off-diagonal term on a sharp input.
    src = input_indices[0]
    ideal = zero(2)
    dephased = zero(2)
    for ra, sa in enumerate(basis):
        for rb, sb in enumerate(basis):
            if sa[2] and sb[2] and sa[1:] == sb[1:]:
                v = prefixes[l][ra][src] * prefixes[l][rb][src]
                ideal[sa[0]][sb[0]] += v
                if energies[ra] + sa[0] == energies[rb] + sb[0]:
                    dephased[sa[0]][sb[0]] += v
    require(ideal[0][1] != 0 and dephased[0][1] == 0, 'physical-energy degeneracy is a necessary stated premise here')
    require(ideal != dephased, 'no generic sharp-battery product/coherence claim')


def bounds_audit() -> None:
    d = 8 * (32768 + 8192)
    pentits, bits = d + 1, 2 * d + 3
    length = 5 + 2 + 3 * d + bits
    m = 2 * length
    r = 1 + pentits + bits
    q = m + r
    require((d, pentits, bits, length) == (327680, 327681, 655363, 1638410), 'word counts')
    require((m + 1, r, q, q + 1) == (3276821, 983045, 4259865, 4259866), 'clock and sharp-battery dimensions')
    require(99 + 2 + d + 3 == 327784, 'finite spatial box bound')
    p0 = F(2, 5) * F(1024, 15625) * F(99, 50000)
    require(F(99, 100) * p0 > F(1, 20000), 'inherited acceptance threshold has read-window margin')
    require(F(50000, 99 * 2 ** 29) < F(1, 10 ** 6), 'inherited selected-band bound')
    require(length >= 400, 'integer clock exponent lower bound')
    require(F(3, 4) ** 4 < F(1, 2), 'four padding powers reduce below half')
    require(F(1, 2 ** 100) < F(1, 10 ** 30), 'rational clock-tail certificate')
    for l in range(1, 9):
        n = 2 * l
        read_bad = sum(F(comb(n, j)) * F(3, 4) ** j * F(1, 4) ** (n - j) for j in range(l))
        future_bad = sum(F(comb(n, j)) * F(1, 4) ** j * F(3, 4) ** (n - j) for j in range(l + 1, n + 1))
        require(read_bad <= F(3, 4) ** l, 'small complete read-tail polynomial')
        require(future_bad <= F(3, 4) ** l, 'small post-read reverse-tail polynomial')
    for m in range(1, 13):
        for j in range(m):
            require(4 * (j + 1) * (m - j) <= (m + 1) ** 2, 'bounded clock-edge strength scaling')


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError('Optimized execution is not admitted')
    clock_audit()
    energy_and_channel_audit()
    bounds_audit()
    print('C-FINITE-HAMILTONIAN-READOUT-N exact audit')
    print('NON-CANONICAL L1 conditional candidate-T; independent acceptance pending')
    print(f'checks {CHECKS}')
    print('integer_clock_Gram_spectrum_and_exact_mirror PASS')
    print('finite_battery_all_sector_energy_and_full_sector_intertwiner PASS')
    print('accepted_reduced_channel_all_toy_input_matrix_units PASS')
    print('negative_controls_reverse_edge_and_physical_energy_coherence PASS')
    print('clock_states 3276821; sharp_battery_levels 4259866')
    print('read_and_postread_bad_clock_weight < 1/1000000000000000000000000000000')
    print('inherited_acceptance > 1/20000 and outside_band < 1/1000000 CONDITIONAL_ON_1746')
    print('spatial_locality native_realization energy_identification occurrence reset OPEN')
    print('PASS')


if __name__ == '__main__':
    main()
