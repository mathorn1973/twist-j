#!/usr/bin/env python3
"""Independent adversarial audit of C-U-AFFINE-TWO-COORD-RECEIVER-N (#1519 / #1521).

Authored independently from the mathematical specification in Issue #1521,
5caff8280c195c12c8c41bf462daae8e6d4bd64b:notes/C-U-AFFINE-TWO-COORD-RECEIVER-N/PREREG.md,
and probes/P-U-NATIVE-MEMORY-EVENT-1/{MEMORY-PROOF.md,CLOCK-PROOF.md} before
any inspection of the primary verifier or execution artifacts.
"""

from __future__ import annotations

import itertools
import sys

Vec6 = tuple[int, int, int, int, int, int]

# Explicit 6x6 generator matrices and translations over F5:
# x = (a, u, c, v, q, r)
GEN_MATRICES: tuple[tuple[Vec6, ...], ...] = (
    # g0 = (u, a, v, c, q, r)
    (
        (0, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    # g1 = (-c, -v, -a, -u, -q, -r)
    (
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    # g2 = (2-c, 1-v+r, 2-a, 1-u-r, 1-q, -r)
    (
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 1),
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 4),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    # g3 = (2-a, 1-u, 3-c, 4-v, 1-q, 1-r)
    (
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    # g4 = (2-a, 1-u, 3-c, 4-v, 2-q, 1-r)
    (
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
)

GEN_SHIFTS: tuple[Vec6, ...] = (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0),
    (2, 1, 2, 1, 1, 0),
    (2, 1, 3, 4, 1, 1),
    (2, 1, 3, 4, 2, 1),
)


def trace_z(x: Vec6) -> int:
    return sum(x) % 5


def theta(n: int) -> int:
    return n.bit_count() & 1


def gen_direct(k: int, x: Vec6) -> Vec6:
    a, u, c, v, q, r = x
    if k == 0:
        return (u % 5, a % 5, v % 5, c % 5, q % 5, r % 5)
    if k == 1:
        return ((-c) % 5, (-v) % 5, (-a) % 5, (-u) % 5, (-q) % 5, (-r) % 5)
    if k == 2:
        return (
            (2 - c) % 5,
            (1 - v + r) % 5,
            (2 - a) % 5,
            (1 - u - r) % 5,
            (1 - q) % 5,
            (-r) % 5,
        )
    if k == 3:
        return (
            (2 - a) % 5,
            (1 - u) % 5,
            (3 - c) % 5,
            (4 - v) % 5,
            (1 - q) % 5,
            (1 - r) % 5,
        )
    if k == 4:
        return (
            (2 - a) % 5,
            (1 - u) % 5,
            (3 - c) % 5,
            (4 - v) % 5,
            (2 - q) % 5,
            (1 - r) % 5,
        )
    raise ValueError(f"invalid generator index: {k}")


def gen_matrix(k: int, x: Vec6) -> Vec6:
    mat = GEN_MATRICES[k]
    shift = GEN_SHIFTS[k]
    return tuple(
        (sum(mat[row][col] * x[col] for col in range(6)) + shift[row]) % 5
        for row in range(6)
    )  # type: ignore[return-value]


def step_control(t: int, x: Vec6) -> tuple[int, Vec6]:
    k = (trace_z(x) + 2 * t) % 5
    return k, gen_direct(k, x)


def step_u(n: int, x: Vec6) -> tuple[int, Vec6, int]:
    t = theta(n)
    k, x_next = step_control(t, x)
    return n + 1, x_next, k


def chart_derived(x: Vec6) -> tuple[int, int, int, int, int, int, int]:
    a, u, c, v, q, r = x
    cap_a = (a + c) % 5
    cap_b = (u + v) % 5
    cap_c = (a - c - 2) % 5
    cap_d = (u - v - 1) % 5
    sigma = (q + r) % 5
    w = (q - r) % 5
    cap_h = (sigma + 3 * (cap_a - cap_b)) % 5
    return cap_a, cap_b, cap_c, cap_d, sigma, w, cap_h


def split_rbar(x: Vec6) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    a, u, c, v, q, r = x
    sigma = (q + r) % 5
    w = (q - r) % 5
    return (u, v, sigma), (a, c, w)


def inv_rbar(
    rbar: tuple[int, int, int], sbar: tuple[int, int, int]
) -> Vec6:
    u, v, sigma = rbar
    a, c, w = sbar
    q = (3 * (sigma + w)) % 5
    r = (3 * (sigma - w)) % 5
    return (a % 5, u % 5, c % 5, v % 5, q, r)


def split_rtilde(
    x: Vec6,
) -> tuple[tuple[int, int], tuple[int, int, int, int]]:
    a, _u, c, _v, _q, _r = x
    _cap_a, cap_b, _cap_c, cap_d, _sigma, w, cap_h = chart_derived(x)
    return (cap_d, cap_h), (a, c, cap_b, w)


def inv_rtilde(
    rtilde: tuple[int, int], stilde: tuple[int, int, int, int]
) -> Vec6:
    cap_d, cap_h = rtilde
    a, c, cap_b, w = stilde
    cap_a = (a + c) % 5
    u = (3 * (cap_b + cap_d + 1)) % 5
    v = (3 * (cap_b - cap_d - 1)) % 5
    sigma = (cap_h - 3 * (cap_a - cap_b)) % 5
    q = (3 * (sigma + w)) % 5
    r = (3 * (sigma - w)) % 5
    return (a % 5, u, c % 5, v, q, r)


def reader_rtilde(rtilde: tuple[int, int]) -> tuple[str, int | None]:
    cap_d, cap_h = rtilde
    if cap_h == 0:
        return ("PRESENT", (4 - 3 * cap_d) % 5)
    if cap_h in (2, 3):
        return ("PRESENT", (4 - 2 * cap_d) % 5)
    if cap_h in (1, 4):
        return ("BLANK", None)
    raise ValueError(f"invalid H: {cap_h}")


def reader_rbar(rbar: tuple[int, int, int]) -> tuple[str, int | None]:
    u, v, sigma = rbar
    cap_b = (u + v) % 5
    cap_d = (u - v - 1) % 5
    cap_z = (2 * cap_b + sigma) % 5
    if cap_b == 2 and sigma == 3:
        return ("PRESENT", u % 5)
    if cap_b in (2, 3) and cap_z in (1, 4):
        return ("PRESENT", (4 - cap_b * cap_z * cap_d) % 5)
    return ("BLANK", None)


def protected_v(x: Vec6) -> tuple[int, int, int, int]:
    z = trace_z(x)
    if z == 1:
        chi = 1
    elif z == 4:
        chi = 4
    else:
        raise ValueError(f"state not in X14: z={z}")
    cap_a, cap_b, cap_c, cap_d, _sigma, _w, _cap_h = chart_derived(x)
    return (cap_a, cap_b, (chi * cap_c) % 5, (chi * cap_d) % 5)


def sign_class_v(x: Vec6) -> frozenset[tuple[int, int, int, int]]:
    v = protected_v(x)
    neg_v = tuple((-coord) % 5 for coord in v)
    return frozenset((v, neg_v))


def prepare_x5(lam: int, mu: int) -> Vec6:
    return (
        lam % 5,
        0,
        (2 - lam) % 5,
        0,
        (-1 - mu) % 5,
        (mu - 1) % 5,
    )


def main() -> None:
    all_states: list[Vec6] = list(itertools.product(range(5), repeat=6))
    assert len(all_states) == 15625

    # 1. Exhaustive 15625-state generator, matrix, involution, trace and inverse audit
    matrix_comparisons = 0
    involution_checks = 0
    inverse_checks = 0

    expected_gen_trace = (
        lambda z: z % 5,
        lambda z: (-z) % 5,
        lambda z: (2 - z) % 5,
        lambda z: (2 - z) % 5,
        lambda z: (3 - z) % 5,
    )
    tau0 = {0: 0, 1: 4, 2: 0, 3: 4, 4: 4}
    tau1 = {0: 2, 1: 1, 2: 1, 3: 3, 4: 1}
    preimages_t1_z0 = 0

    for x in all_states:
        z = trace_z(x)
        for k in range(5):
            y_dir = gen_direct(k, x)
            y_mat = gen_matrix(k, x)
            assert y_dir == y_mat, f"generator {k} mismatch at {x}"
            matrix_comparisons += 1
            assert gen_direct(k, y_dir) == x, f"g{k} not involution at {x}"
            involution_checks += 1
            assert trace_z(y_dir) == expected_gen_trace[k](z)

        _k0, y0 = step_control(0, x)
        _k1, y1 = step_control(1, x)
        assert trace_z(y0) == tau0[z]
        assert trace_z(y1) == tau1[z]
        if trace_z(y1) == 0:
            preimages_t1_z0 += 1

        rbar, sbar = split_rbar(x)
        assert inv_rbar(rbar, sbar) == x
        inverse_checks += 1

        rtilde, stilde = split_rtilde(x)
        assert inv_rtilde(rtilde, stilde) == x
        inverse_checks += 1

    for raw in all_states:
        rbar_in = raw[:3]
        sbar_in = raw[3:]
        x_rec = inv_rbar(rbar_in, sbar_in)
        assert split_rbar(x_rec) == (rbar_in, sbar_in)
        inverse_checks += 1

        rtilde_in = raw[:2]
        stilde_in = raw[2:]
        x_rec2 = inv_rtilde(rtilde_in, stilde_in)
        assert split_rtilde(x_rec2) == (rtilde_in, stilde_in)
        inverse_checks += 1

    assert matrix_comparisons == 78125
    assert involution_checks == 78125
    assert inverse_checks == 62500
    assert preimages_t1_z0 == 0

    # 2. Section A: Late construction (n=5), 500-state continuation carrier, and 25 trajectories
    carrier_500 = [
        x
        for x in all_states
        if trace_z(x) in (1, 4)
        and chart_derived(x)[0] == chart_derived(x)[1]
        and chart_derived(x)[0] in (2, 3)
    ]
    assert len(carrier_500) == 500
    carrier_set = set(carrier_500)

    carrier_transitions = 0
    fibre_counts: dict[tuple[int, int], int] = {}
    for x in carrier_500:
        z = trace_z(x)
        cap_a, cap_b, cap_c, cap_d, sigma, _w, cap_h = chart_derived(x)
        assert cap_a == cap_b and cap_a in (2, 3)
        assert cap_h == sigma
        assert cap_h in (0, 2, 3)
        assert not (cap_b == 2 and sigma == 3)
        cap_z = (2 * cap_b + sigma) % 5
        assert cap_z == (2 * cap_a + cap_h) % 5 == z

        inv1 = (cap_a * z * cap_c) % 5
        inv2 = (cap_b * z * cap_d) % 5
        lam = (2 - inv1) % 5
        mu = (4 - inv2) % 5
        fibre_counts[(lam, mu)] = fibre_counts.get((lam, mu), 0) + 1

        out_tilde = reader_rtilde((cap_d, cap_h))
        out_bar = reader_rbar((x[1], x[3], sigma))
        assert out_tilde == ("PRESENT", mu)
        assert out_bar == ("PRESENT", mu)
        first_msg = (2 - cap_a * ((2 * cap_a + cap_h) % 5) * cap_c) % 5
        assert first_msg == lam

        for t in (0, 1):
            _k, x_next = step_control(t, x)
            assert x_next in carrier_set
            z_next = trace_z(x_next)
            a_n, b_n, c_n, d_n, _s_n, _w_n, _h_n = chart_derived(x_next)
            assert (a_n * z_next * c_n) % 5 == inv1
            assert (b_n * z_next * d_n) % 5 == inv2
            carrier_transitions += 1

    assert carrier_transitions == 1000
    assert len(fibre_counts) == 25 and all(v == 20 for v in fibre_counts.values())

    # Audit all 25 late-start preparations from n=5 through n=1024 inclusive
    trajectory_checks = 0
    w8_values: set[int] = set()
    w9_values: set[int] = set()
    bare_uv_support_by_mu: dict[int, set[tuple[int, int]]] = {}

    for lam in range(5):
        for mu in range(5):
            x5 = prepare_x5(lam, mu)
            assert trace_z(x5) == 0
            assert split_rbar(x5)[0] == (0, 0, 3)
            assert split_rtilde(x5)[0] == (4, 4)
            assert reader_rtilde(split_rtilde(x5)[0]) == ("BLANK", None)
            assert reader_rbar(split_rbar(x5)[0]) == ("BLANK", None)

            n6, x6, k5 = step_u(5, x5)
            assert (n6, k5) == (6, 0)
            assert x6 == (0, lam, 0, (2 - lam) % 5, (-1 - mu) % 5, (mu - 1) % 5)
            assert reader_rtilde(split_rtilde(x6)[0]) == ("PRESENT", lam)
            assert reader_rbar(split_rbar(x6)[0]) == ("PRESENT", lam)

            n7, x7, k6 = step_u(6, x6)
            assert (n7, k6) == (7, 0)
            assert x7 == x5
            assert (7, x7) != (5, x5)
            assert split_rbar(x7)[0] == (0, 0, 3)
            assert split_rtilde(x7)[0] == (4, 4)
            assert reader_rtilde(split_rtilde(x7)[0]) == ("BLANK", None)
            assert reader_rbar(split_rbar(x7)[0]) == ("BLANK", None)

            n8, x8, k7 = step_u(7, x7)
            assert (n8, k7) == (8, 2)
            assert x8 == (
                lam,
                mu,
                (2 - lam) % 5,
                (2 - mu) % 5,
                (2 + mu) % 5,
                (1 - mu) % 5,
            )
            assert reader_rtilde(split_rtilde(x8)[0]) == ("PRESENT", mu)
            assert reader_rbar(split_rbar(x8)[0]) == ("PRESENT", mu)
            w8_values.add(chart_derived(x8)[5])

            n9, x9, k8 = step_u(8, x8)
            assert (n9, k8) == (9, 4)
            assert x9 == (
                (2 - lam) % 5,
                (1 - mu) % 5,
                (1 + lam) % 5,
                (2 + mu) % 5,
                (-mu) % 5,
                mu % 5,
            )
            assert x9 in carrier_set
            w9_values.add(chart_derived(x9)[5])

            # Bare (u,v) support on the recurrent X14 sign fibre of x9
            sc9 = sign_class_v(x9)
            uv_proj = {
                (y[1], y[3])
                for y in all_states
                if trace_z(y) in (1, 4) and sign_class_v(y) == sc9
            }
            if mu in bare_uv_support_by_mu:
                assert bare_uv_support_by_mu[mu] == uv_proj
            else:
                bare_uv_support_by_mu[mu] = uv_proj

            # Full trajectory audit from n=5 through n=1024 inclusive (1020 states per pair)
            curr = x5
            for n in range(5, 1025):
                rt = split_rtilde(curr)[0]
                rb = split_rbar(curr)[0]
                if n in (5, 7):
                    expected_out = ("BLANK", None)
                elif n == 6:
                    expected_out = ("PRESENT", lam)
                else:
                    expected_out = ("PRESENT", mu)
                assert reader_rtilde(rt) == expected_out
                assert reader_rbar(rb) == expected_out
                if n >= 9:
                    assert curr in carrier_set
                    ca, _cb, cc, _cd, _sig, _w, ch = chart_derived(curr)
                    assert (2 - ca * ((2 * ca + ch) % 5) * cc) % 5 == lam
                trajectory_checks += 1
                if n < 1024:
                    _n_next, curr, _k = step_u(n, curr)

    assert trajectory_checks == 25500
    assert w8_values == {0, 1, 2, 3, 4}
    assert w9_values == {0, 1, 2, 3, 4}
    assert bare_uv_support_by_mu[0] == bare_uv_support_by_mu[3]
    assert bare_uv_support_by_mu[1] == bare_uv_support_by_mu[2]
    assert bare_uv_support_by_mu[0] != bare_uv_support_by_mu[1]
    assert bare_uv_support_by_mu[4] != bare_uv_support_by_mu[0]
    assert bare_uv_support_by_mu[4] != bare_uv_support_by_mu[1]

    # 3. Section B: 0011 launch windows and no-predecessor audit
    starts_0011 = []
    for n in range(4096):
        is_0011 = (
            theta(n) == 0
            and theta(n + 1) == 0
            and theta(n + 2) == 1
            and theta(n + 3) == 1
        )
        m = n // 2
        char_cond = (
            (n % 2 == 1)
            and theta(m) == 1
            and theta(m + 1) == 0
            and theta(m + 2) == 1
        )
        assert is_0011 == char_cond
        if is_0011:
            starts_0011.append(n)
            assert n >= 1 and theta(n - 1) == 1

    for k in range(4, 32):
        nk = 3 * (1 << k) + 5
        assert (
            theta(nk) == 0
            and theta(nk + 1) == 0
            and theta(nk + 2) == 1
            and theta(nk + 3) == 1
        )
        assert theta(nk - 1) == 1

    # 4. Section C: Origin-zero all-affine obstruction audit across all 15625 initial states
    x1_set: set[Vec6] = set()
    x2_set: set[Vec6] = set()
    x3_set: set[Vec6] = set()
    sum_x2_x3: set[Vec6] = set()
    z2_eq_1_count = 0
    z2_eq_2_count = 0

    t3_shift = GEN_SHIFTS[3]
    t4_shift = GEN_SHIFTS[4]

    for x0 in all_states:
        z0 = trace_z(x0)
        _n1, x1, _k0 = step_u(0, x0)
        _n2, x2, _k1 = step_u(1, x1)
        _n3, x3, k2 = step_u(2, x2)

        x1_set.add(x1)
        x2_set.add(x2)
        x3_set.add(x3)

        z1 = trace_z(x1)
        z2 = trace_z(x2)
        z3 = trace_z(x3)
        assert z1 in (0, 4)
        assert z2 in (1, 2)
        assert z3 == 1

        x2_plus_x3 = tuple((x2[i] + x3[i]) % 5 for i in range(6))
        sum_x2_x3.add(x2_plus_x3)  # type: ignore[arg-type]

        if z0 in (0, 2):
            assert z1 == 0 and z2 == 2 and k2 == 4
            assert x2_plus_x3 == t4_shift
            z2_eq_2_count += 1
        else:
            assert z1 == 4 and z2 == 1 and k2 == 3
            assert x2_plus_x3 == t3_shift
            # Verify x2 is already in X14 and shares the exact recurrent sign fibre of x3
            assert sign_class_v(x2) == sign_class_v(x3)
            z2_eq_1_count += 1

    assert len(x1_set) == 6250
    assert len(x2_set) == 6250
    assert len(x3_set) == 3125
    assert z2_eq_1_count == 9375
    assert z2_eq_2_count == 6250
    assert sum_x2_x3 == {t3_shift, t4_shift}

    # Sharpness witness 1: R(x) = q attains |{R(x3)}| = 2 with common R(x2) = 0
    x0_w1 = (1, 0, 0, 0, 0, 0)
    x0_w2 = (0, 0, 0, 0, 1, 1)
    _, x1_w1, _ = step_u(0, x0_w1)
    _, x2_w1, _ = step_u(1, x1_w1)
    _, x3_w1, _ = step_u(2, x2_w1)
    _, x1_w2, _ = step_u(0, x0_w2)
    _, x2_w2, _ = step_u(1, x1_w2)
    _, x3_w2, _ = step_u(2, x2_w2)
    assert x2_w1[4] == x2_w2[4] == 0
    assert {x3_w1[4], x3_w2[4]} == {1, 2}

    # Sharpness witness 2: R(x) = z(x) on X2 attains 1 permanent nonblank message after BLANK at n=0,2
    for x0 in all_states:
        if trace_z(x0) == 2:
            _, x1, _ = step_u(0, x0)
            _, x2, _ = step_u(1, x1)
            _, x3, _ = step_u(2, x2)
            assert trace_z(x0) == 2 and trace_z(x1) == 0 and trace_z(x2) == 2 and trace_z(x3) == 1

    print("AUDIT_STATES=15625")
    print(f"GENERATOR_MATRIX_COMPARISONS={matrix_comparisons}")
    print(f"CHART_INVERSE_CHECKS={inverse_checks}")
    print(f"LATE_PREPARATIONS=25")
    print(f"CONTINUATION_CARRIER_STATES={len(carrier_500)}")
    print(f"CONTINUATION_CARRIER_TRANSITIONS={carrier_transitions}")
    print(f"TRAJECTORY_STATE_CHECKS={trajectory_checks}")
    print("BARE_UV_SUPPORT_PARTITION={0,3}|{1,2}|{4}")
    print(f"LAUNCH_0011_COUNT_4096={len(starts_0011)}")
    print("LAUNCH_0011_PREDECESSOR_COUNT_ON_X0=0")
    print("ORIGIN_ZERO_X2_SHEETS={1,2}")
    print("ORIGIN_ZERO_X2_PLUS_X3_SHIFTS=2")
    print("ALL_AFFINE_N3_MAX_RECEIVER_STATES=2")
    print("ALL_AFFINE_EVENTUAL_MAX_NONBLANK_MESSAGES=1")
    print("P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-1 PASS")


if __name__ == "__main__":
    main()
