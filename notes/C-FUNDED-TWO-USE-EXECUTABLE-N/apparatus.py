#!/usr/bin/env python3
"""Self-contained exact funded two-use continuing apparatus (Lane I, #1507).

NON-CANONICAL / L1 executable incubation machine.
Original work Apache-2.0, A. M. Thorn, 2026-10-15.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from typing import Dict, List, Optional, Sequence, Tuple, Union


# ---------------------------------------------------------------------------
# Primary embedded constants (from frozen #1485 and Public Canon v101)
# ---------------------------------------------------------------------------

Y_SITES: Tuple[Tuple[int, int, int], ...] = (
    (0, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 0, 0),
)
R_PORTS: Tuple[Tuple[int, int, int], ...] = Y_SITES[:4]
Y4_SITE: Tuple[int, int, int] = Y_SITES[4]

SHELL_WEIGHTS: Dict[int, int] = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
STENCIL_DENOM: int = 324
DIAG_LD: Fraction = Fraction(8, 9)
DIAG_H: Fraction = Fraction(10, 9)
BALANCED_LIFT_ELL: Tuple[int, int, int, int, int] = (0, 1, 2, -2, -1)

COMPARISON_CAPACITIES: Tuple[Fraction, ...] = (
    Fraction(0, 1),
    Fraction(1, 10),
    Fraction(1, 5),
    Fraction(2, 5),
    Fraction(8224427, 10497600),
    Fraction(4, 5),
)


# ---------------------------------------------------------------------------
# Strict exact type and carrier validators (rejecting bool, float, str, etc.)
# ---------------------------------------------------------------------------

def require_exact_int(val: object, name: str) -> int:
    if isinstance(val, bool) or not isinstance(val, int):
        raise TypeError(f"{name} must be an exact int (not bool/float), got {type(val).__name__}")
    return val


def require_nonneg_int(val: object, name: str) -> int:
    v = require_exact_int(val, name)
    if v < 0:
        raise ValueError(f"{name} must be >= 0, got {v}")
    return v


def require_f5_int(val: object, name: str) -> int:
    v = require_exact_int(val, name)
    if v < 0 or v >= 5:
        raise ValueError(f"{name} must be in {{0,1,2,3,4}}, got {v}")
    return v


def require_f5_tuple(seq: object, length: int, name: str) -> Tuple[int, ...]:
    if not isinstance(seq, (tuple, list)):
        raise TypeError(f"{name} must be a tuple or list of F_5 ints, got {type(seq).__name__}")
    if len(seq) != length:
        raise ValueError(f"{name} must have length {length}, got {len(seq)}")
    return tuple(require_f5_int(x, f"{name}[{i}]") for i, x in enumerate(seq))


def require_fraction(val: object, name: str) -> Fraction:
    if isinstance(val, bool):
        raise TypeError(f"{name} must be a Fraction or exact int, not bool")
    if isinstance(val, Fraction):
        return val
    if isinstance(val, int):
        return Fraction(val, 1)
    raise TypeError(f"{name} must be a Fraction or exact int, got {type(val).__name__}")


def require_q_tuple(seq: object, length: int, name: str) -> Tuple[Fraction, ...]:
    if not isinstance(seq, (tuple, list)):
        raise TypeError(f"{name} must be a tuple or list of rationals, got {type(seq).__name__}")
    if len(seq) != length:
        raise ValueError(f"{name} must have length {length}, got {len(seq)}")
    return tuple(require_fraction(x, f"{name}[{i}]") for i, x in enumerate(seq))


def require_sign(val: object, name: str) -> int:
    v = require_exact_int(val, name)
    if v not in (-1, 1):
        raise ValueError(f"{name} must be in {{-1, +1}}, got {v}")
    return v


def require_clock(val: object, modulus: int, name: str) -> int:
    v = require_exact_int(val, name)
    if v < 0 or v >= modulus:
        raise ValueError(f"{name} must be in 0..{modulus - 1}, got {v}")
    return v


# ---------------------------------------------------------------------------
# Lazy primary geometry and sparse stencil construction (no import side effects)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class LatticeGeometry:
    b_st: Tuple[Tuple[int, int, int], ...]
    b_zero: Tuple[Tuple[int, int, int], ...]
    stencil_coeffs: Dict[Tuple[int, int, int], Fraction]
    domain_d: Tuple[Tuple[int, int, int], ...]
    site_to_index: Dict[Tuple[int, int, int], int]
    port_indices: Tuple[int, int, int, int]
    y_indices: Tuple[int, int, int, int, int]
    y4_index: int
    h_neighbors: Tuple[Tuple[Tuple[int, Fraction], ...], ...]


@lru_cache(maxsize=1)
def get_geometry() -> LatticeGeometry:
    b_st_list: List[Tuple[int, int, int]] = []
    stencil_coeffs: Dict[Tuple[int, int, int], Fraction] = {}
    for x1 in range(-4, 5):
        for x2 in range(-4, 5):
            for x3 in range(-4, 5):
                if (x1 + x2 + x3) % 2 != 0:
                    continue
                norm_sq = x1 * x1 + x2 * x2 + x3 * x3
                if norm_sq in SHELL_WEIGHTS:
                    d = (x1, x2, x3)
                    b_st_list.append(d)
                    stencil_coeffs[d] = Fraction(SHELL_WEIGHTS[norm_sq], STENCIL_DENOM)
    b_st = tuple(sorted(b_st_list))
    b_zero = tuple(sorted(b_st_list + [(0, 0, 0)]))

    domain_set = set()
    for y in Y_SITES:
        for b1 in b_zero:
            for b2 in b_zero:
                domain_set.add((y[0] + b1[0] + b2[0], y[1] + b1[1] + b2[1], y[2] + b1[2] + b2[2]))
    domain_d = tuple(sorted(domain_set))
    if len(domain_d) != 869:
        raise RuntimeError(f"Expected |D| = 869, got {len(domain_d)}")

    site_to_index = {pt: idx for idx, pt in enumerate(domain_d)}
    port_indices = (
        site_to_index[R_PORTS[0]],
        site_to_index[R_PORTS[1]],
        site_to_index[R_PORTS[2]],
        site_to_index[R_PORTS[3]],
    )
    y_indices = tuple(site_to_index[y] for y in Y_SITES)  # type: ignore[assignment]
    y4_index = site_to_index[Y4_SITE]

    h_neighbors_list: List[Tuple[Tuple[int, Fraction], ...]] = []
    for x in domain_d:
        nbrs: List[Tuple[int, Fraction]] = []
        for d, coeff in stencil_coeffs.items():
            y = (x[0] - d[0], x[1] - d[1], x[2] - d[2])
            j = site_to_index.get(y)
            if j is not None:
                nbrs.append((j, coeff))
        h_neighbors_list.append(tuple(nbrs))

    return LatticeGeometry(
        b_st=b_st,
        b_zero=b_zero,
        stencil_coeffs=stencil_coeffs,
        domain_d=domain_d,
        site_to_index=site_to_index,
        port_indices=port_indices,
        y_indices=y_indices,  # type: ignore[arg-type]
        y4_index=y4_index,
        h_neighbors=tuple(h_neighbors_list),
    )


# ---------------------------------------------------------------------------
# Immutable typed state dataclasses
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class WaveTapeState:
    u: Tuple[Fraction, ...]
    v: Tuple[Fraction, ...]
    A0: Tuple[Fraction, ...]
    A1: Tuple[Fraction, ...]
    B0: Tuple[Fraction, ...]
    B1: Tuple[Fraction, ...]
    k: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "u", require_q_tuple(self.u, 869, "u"))
        object.__setattr__(self, "v", require_q_tuple(self.v, 869, "v"))
        object.__setattr__(self, "A0", require_q_tuple(self.A0, 4, "A0"))
        object.__setattr__(self, "A1", require_q_tuple(self.A1, 4, "A1"))
        object.__setattr__(self, "B0", require_q_tuple(self.B0, 4, "B0"))
        object.__setattr__(self, "B1", require_q_tuple(self.B1, 4, "B1"))
        object.__setattr__(self, "k", require_clock(self.k, 2, "k"))


@dataclass(frozen=True)
class ApparatusSubstate:
    X: WaveTapeState
    W: Fraction
    b: Fraction
    B: Fraction
    sigma_A: int
    sigma_B: int
    d: Tuple[int, int]

    def __post_init__(self) -> None:
        if not isinstance(self.X, WaveTapeState):
            raise TypeError(f"X must be WaveTapeState, got {type(self.X).__name__}")
        w_val = require_fraction(self.W, "W")
        b_val = require_fraction(self.b, "b")
        cap_val = require_fraction(self.B, "B")
        if cap_val < 0:
            raise ValueError(f"Capacity B must be >= 0, got {cap_val}")
        if b_val < 0 or b_val > cap_val:
            raise ValueError(f"Store b must satisfy 0 <= b <= B ({cap_val}), got {b_val}")
        sig_a = require_sign(self.sigma_A, "sigma_A")
        sig_b = require_sign(self.sigma_B, "sigma_B")
        d_tup = require_f5_tuple(self.d, 2, "d")
        object.__setattr__(self, "W", w_val)
        object.__setattr__(self, "b", b_val)
        object.__setattr__(self, "B", cap_val)
        object.__setattr__(self, "sigma_A", sig_a)
        object.__setattr__(self, "sigma_B", sig_b)
        object.__setattr__(self, "d", (d_tup[0], d_tup[1]))


@dataclass(frozen=True)
class CompositeState:
    n: int
    x_A: Tuple[int, ...]
    x_B: Tuple[int, ...]
    X: WaveTapeState
    W: Fraction
    b: Fraction
    B: Fraction
    sigma_A: int
    sigma_B: int
    d: Tuple[int, int]
    c: int

    def __post_init__(self) -> None:
        n_val = require_nonneg_int(self.n, "n")
        xa = require_f5_tuple(self.x_A, 6, "x_A")
        xb = require_f5_tuple(self.x_B, 6, "x_B")
        if not isinstance(self.X, WaveTapeState):
            raise TypeError(f"X must be WaveTapeState, got {type(self.X).__name__}")
        w_val = require_fraction(self.W, "W")
        b_val = require_fraction(self.b, "b")
        cap_val = require_fraction(self.B, "B")
        if cap_val < 0:
            raise ValueError(f"Capacity B must be >= 0, got {cap_val}")
        if b_val < 0 or b_val > cap_val:
            raise ValueError(f"Store b must satisfy 0 <= b <= B ({cap_val}), got {b_val}")
        sig_a = require_sign(self.sigma_A, "sigma_A")
        sig_b = require_sign(self.sigma_B, "sigma_B")
        d_tup = require_f5_tuple(self.d, 2, "d")
        c_val = require_clock(self.c, 8, "c")
        object.__setattr__(self, "n", n_val)
        object.__setattr__(self, "x_A", xa)
        object.__setattr__(self, "x_B", xb)
        object.__setattr__(self, "W", w_val)
        object.__setattr__(self, "b", b_val)
        object.__setattr__(self, "B", cap_val)
        object.__setattr__(self, "sigma_A", sig_a)
        object.__setattr__(self, "sigma_B", sig_b)
        object.__setattr__(self, "d", (d_tup[0], d_tup[1]))
        object.__setattr__(self, "c", c_val)

    def to_apparatus_substate(self) -> ApparatusSubstate:
        return ApparatusSubstate(
            X=self.X,
            W=self.W,
            b=self.b,
            B=self.B,
            sigma_A=self.sigma_A,
            sigma_B=self.sigma_B,
            d=self.d,
        )


@dataclass(frozen=True)
class ChronologicalCutEntry:
    status: str
    use: Optional[int]
    cut: Optional[int]
    slot_name: Optional[str]
    vector: Optional[Tuple[Fraction, ...]]


@dataclass(frozen=True)
class DirectPortReadout:
    """Restricted port/context readout with no native-head or wave/archive fields."""
    b0: Tuple[Fraction, ...]
    b2: Tuple[Fraction, ...]
    sigma_A: Optional[int] = -1
    sigma_B: Optional[int] = -1
    d: Optional[Tuple[int, int]] = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "b0", require_q_tuple(self.b0, 4, "b0"))
        object.__setattr__(self, "b2", require_q_tuple(self.b2, 4, "b2"))
        if self.sigma_A is not None:
            object.__setattr__(self, "sigma_A", require_sign(self.sigma_A, "sigma_A"))
        if self.sigma_B is not None:
            object.__setattr__(self, "sigma_B", require_sign(self.sigma_B, "sigma_B"))
        if self.d is not None:
            d_tup = require_f5_tuple(self.d, 2, "d")
            object.__setattr__(self, "d", (d_tup[0], d_tup[1]))


# ---------------------------------------------------------------------------
# Primary linear operators on Q^D and Q^4
# ---------------------------------------------------------------------------

def zero_qd() -> Tuple[Fraction, ...]:
    return (Fraction(0, 1),) * 869


def zero_q4() -> Tuple[Fraction, ...]:
    return (Fraction(0, 1),) * 4


def basis_q4(index: int) -> Tuple[Fraction, ...]:
    idx = require_clock(index, 4, "index")
    return tuple(Fraction(1 if j == idx else 0, 1) for j in range(4))


def dot_vec(a: Sequence[Fraction], b: Sequence[Fraction]) -> Fraction:
    if len(a) != len(b):
        raise ValueError(f"Vector length mismatch: {len(a)} vs {len(b)}")
    total = Fraction(0, 1)
    for x, y in zip(a, b):
        if x != 0 and y != 0:
            total += x * y
    return total


def apply_P(z: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    z_tup = require_q_tuple(z, 4, "z")
    geom = get_geometry()
    out = [Fraction(0, 1)] * 869
    for j, idx in enumerate(geom.port_indices):
        out[idx] = z_tup[j]
    return tuple(out)


def apply_PT(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    u_tup = require_q_tuple(u, 869, "u")
    geom = get_geometry()
    return tuple(u_tup[idx] for idx in geom.port_indices)


def apply_K(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    u_tup = require_q_tuple(u, 869, "u")
    geom = get_geometry()
    out = list(u_tup)
    half = Fraction(1, 2)
    for idx in geom.port_indices:
        out[idx] = out[idx] * half
    return tuple(out)


def apply_J0(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    u_tup = require_q_tuple(u, 869, "u")
    geom = get_geometry()
    out = list(u_tup)
    zero = Fraction(0, 1)
    for idx in geom.port_indices:
        out[idx] = zero
    return tuple(out)


def apply_H(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    u_tup = require_q_tuple(u, 869, "u")
    geom = get_geometry()
    out = [Fraction(0, 1)] * 869
    nonzero_indices = [i for i, val in enumerate(u_tup) if val != 0]
    if not nonzero_indices:
        return tuple(out)
    for i in nonzero_indices:
        ui = u_tup[i]
        out[i] += DIAG_H * ui
        for j, coeff in geom.h_neighbors[i]:
            out[j] += coeff * ui
    return tuple(out)


def apply_LD(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    u_tup = require_q_tuple(u, 869, "u")
    hu = apply_H(u_tup)
    return tuple(2 * u_tup[i] - hu[i] for i in range(869))


def apply_T(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    return apply_K(apply_H(u))


def apply_S(z: Sequence[Fraction]) -> Tuple[Fraction, ...]:
    z_tup = require_q_tuple(z, 4, "z")
    geom = get_geometry()
    s_over_5 = (z_tup[0] + z_tup[1] + z_tup[2] + z_tup[3]) * Fraction(1, 5)
    out = [Fraction(0, 1)] * 869
    for j, idx in enumerate(geom.port_indices):
        out[idx] = z_tup[j] - s_over_5
    out[geom.y4_index] = -s_over_5
    return tuple(out)


def eta_lift(r: Sequence[int]) -> Tuple[Fraction, ...]:
    r_tup = require_f5_tuple(r, 2, "r")
    q, r2 = r_tup
    return (
        Fraction(BALANCED_LIFT_ELL[q], 2),
        Fraction(BALANCED_LIFT_ELL[r2] + 1, 2),
        Fraction(0, 1),
        Fraction(0, 1),
    )


def source_field_for_receiver(r: Sequence[int]) -> Tuple[Fraction, ...]:
    return apply_S(eta_lift(r))


def wave_energy(u: Sequence[Fraction], v: Sequence[Fraction]) -> Fraction:
    u_tup = require_q_tuple(u, 869, "u")
    v_tup = require_q_tuple(v, 869, "v")
    hv = apply_H(v_tup)
    return Fraction(1, 2) * (dot_vec(u_tup, u_tup) + dot_vec(v_tup, v_tup) - dot_vec(u_tup, hv))


def wave_energy_difference_form(u: Sequence[Fraction], v: Sequence[Fraction]) -> Fraction:
    u_tup = require_q_tuple(u, 869, "u")
    v_tup = require_q_tuple(v, 869, "v")
    diff = tuple(v_tup[i] - u_tup[i] for i in range(869))
    ld_v = apply_LD(v_tup)
    return Fraction(1, 2) * (dot_vec(diff, diff) + dot_vec(u_tup, ld_v))


def full_classical_energy(X: WaveTapeState) -> Fraction:
    if not isinstance(X, WaveTapeState):
        raise TypeError(f"X must be WaveTapeState, got {type(X).__name__}")
    tape_norm_sq = (
        dot_vec(X.A0, X.A0)
        + dot_vec(X.A1, X.A1)
        + dot_vec(X.B0, X.B0)
        + dot_vec(X.B1, X.B1)
    )
    return wave_energy(X.u, X.v) + 2 * tape_norm_sq


# ---------------------------------------------------------------------------
# Native F_5^6 generators, selector, and separate native_tick
# ---------------------------------------------------------------------------

def apply_generator(gen_index: int, x: Sequence[int]) -> Tuple[int, ...]:
    g = require_f5_int(gen_index, "gen_index")
    a, b, c0, d0, q, r = require_f5_tuple(x, 6, "x")
    if g == 0:
        return (b, a, d0, c0, q, r)
    if g == 1:
        return ((-c0) % 5, (-d0) % 5, (-a) % 5, (-b) % 5, (-q) % 5, (-r) % 5)
    if g == 2:
        return (
            (2 - c0) % 5,
            (1 + r - d0) % 5,
            (2 - a) % 5,
            (1 - r - b) % 5,
            (1 - q) % 5,
            (-r) % 5,
        )
    if g == 3:
        return (
            (2 - a) % 5,
            (1 - b) % 5,
            (3 - c0) % 5,
            (4 - d0) % 5,
            (1 - q) % 5,
            (1 - r) % 5,
        )
    return (
        (2 - a) % 5,
        (1 - b) % 5,
        (3 - c0) % 5,
        (4 - d0) % 5,
        (2 - q) % 5,
        (1 - r) % 5,
    )


def theta_bit(n: int) -> int:
    n_val = require_nonneg_int(n, "n")
    return n_val.bit_count() % 2


def native_selector(n: int, x: Sequence[int]) -> int:
    n_val = require_nonneg_int(n, "n")
    x_tup = require_f5_tuple(x, 6, "x")
    z6 = sum(x_tup) % 5
    return (z6 + 2 * theta_bit(n_val)) % 5


def receiver_of(x: Sequence[int]) -> Tuple[int, int]:
    x_tup = require_f5_tuple(x, 6, "x")
    return (x_tup[4], x_tup[5])


def native_tick_single(n: int, x: Sequence[int]) -> Tuple[int, Tuple[int, ...]]:
    n_val = require_nonneg_int(n, "n")
    x_tup = require_f5_tuple(x, 6, "x")
    j = native_selector(n_val, x_tup)
    return (n_val + 1, apply_generator(j, x_tup))


def native_tick(
    n: int, x_A: Sequence[int], x_B: Sequence[int]
) -> Tuple[int, Tuple[int, ...], Tuple[int, ...]]:
    n_val = require_nonneg_int(n, "n")
    xa = require_f5_tuple(x_A, 6, "x_A")
    xb = require_f5_tuple(x_B, 6, "x_B")
    ja = native_selector(n_val, xa)
    jb = native_selector(n_val, xb)
    return (n_val + 1, apply_generator(ja, xa), apply_generator(jb, xb))


# ---------------------------------------------------------------------------
# Buffer capture L_buf, wave update F / F_inverse, and funded contacts H_B,A / H_B,B
# ---------------------------------------------------------------------------

def buffer_capture(
    x_B: Sequence[int], d: Sequence[int]
) -> Tuple[Tuple[int, ...], Tuple[int, int]]:
    xb = require_f5_tuple(x_B, 6, "x_B")
    d_tup = require_f5_tuple(d, 2, "d")
    rec_b = receiver_of(xb)
    return (xb, ((d_tup[0] + rec_b[0]) % 5, (d_tup[1] + rec_b[1]) % 5))


def buffer_capture_inverse(
    x_B: Sequence[int], d_prime: Sequence[int]
) -> Tuple[Tuple[int, ...], Tuple[int, int]]:
    xb = require_f5_tuple(x_B, 6, "x_B")
    d_tup = require_f5_tuple(d_prime, 2, "d_prime")
    rec_b = receiver_of(xb)
    return (xb, ((d_tup[0] - rec_b[0]) % 5, (d_tup[1] - rec_b[1]) % 5))


def buffer_capture_label(r_B: Sequence[int], d: Sequence[int]) -> Tuple[int, int]:
    rb = require_f5_tuple(r_B, 2, "r_B")
    d_tup = require_f5_tuple(d, 2, "d")
    return ((d_tup[0] + rb[0]) % 5, (d_tup[1] + rb[1]) % 5)


def buffer_capture_label_inverse(r_B: Sequence[int], d_prime: Sequence[int]) -> Tuple[int, int]:
    rb = require_f5_tuple(r_B, 2, "r_B")
    d_tup = require_f5_tuple(d_prime, 2, "d_prime")
    return ((d_tup[0] - rb[0]) % 5, (d_tup[1] - rb[1]) % 5)


def F_step(X: WaveTapeState) -> WaveTapeState:
    if not isinstance(X, WaveTapeState):
        raise TypeError(f"X must be WaveTapeState, got {type(X).__name__}")
    hv = apply_H(X.v)
    j0u = apply_J0(X.u)
    pa0 = apply_P(X.A0)
    rhs = tuple(hv[i] - j0u[i] + 4 * pa0[i] for i in range(869))
    w_next = apply_K(rhs)
    pt_diff = apply_PT(tuple(w_next[i] - X.u[i] for i in range(869)))
    b_out = tuple(X.A0[j] - Fraction(1, 2) * pt_diff[j] for j in range(4))
    return WaveTapeState(
        u=X.v,
        v=w_next,
        A0=X.A1,
        A1=X.B1,
        B0=b_out,
        B1=X.B0,
        k=(X.k + 1) % 2,
    )


def F_inverse(X_prime: WaveTapeState) -> WaveTapeState:
    if not isinstance(X_prime, WaveTapeState):
        raise TypeError(f"X_prime must be WaveTapeState, got {type(X_prime).__name__}")
    v = X_prime.u
    w_next = X_prime.v
    b_out = X_prime.B0
    hv = apply_H(v)
    j0w = apply_J0(w_next)
    pb = apply_P(b_out)
    rhs = tuple(hv[i] - j0w[i] + 4 * pb[i] for i in range(869))
    u = apply_K(rhs)
    pt_diff = apply_PT(tuple(w_next[i] - u[i] for i in range(869)))
    a0 = tuple(b_out[j] + Fraction(1, 2) * pt_diff[j] for j in range(4))
    return WaveTapeState(
        u=u,
        v=v,
        A0=a0,
        A1=X_prime.A0,
        B0=X_prime.B1,
        B1=X_prime.A1,
        k=(X_prime.k - 1) % 2,
    )


def contact_energy_increment(
    u: Sequence[Fraction], v: Sequence[Fraction], sigma: int, r: Sequence[int]
) -> Fraction:
    u_tup = require_q_tuple(u, 869, "u")
    v_tup = require_q_tuple(v, 869, "v")
    sig = require_sign(sigma, "sigma")
    a = source_field_for_receiver(r)
    v_shifted = tuple(v_tup[i] + sig * a[i] for i in range(869))
    return wave_energy(u_tup, v_shifted) - wave_energy(u_tup, v_tup)


def contact_energy_increment_bilinear(
    u: Sequence[Fraction], v: Sequence[Fraction], sigma: int, r: Sequence[int]
) -> Fraction:
    u_tup = require_q_tuple(u, 869, "u")
    v_tup = require_q_tuple(v, 869, "v")
    sig = require_sign(sigma, "sigma")
    a = source_field_for_receiver(r)
    hu = apply_H(u_tup)
    wave_term = tuple(v_tup[i] - Fraction(1, 2) * hu[i] for i in range(869))
    return Fraction(1, 2) * dot_vec(a, a) + sig * dot_vec(a, wave_term)


def funded_contact_A_substate(
    substate: ApparatusSubstate, r_A: Sequence[int]
) -> ApparatusSubstate:
    if not isinstance(substate, ApparatusSubstate):
        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
    ra = require_f5_tuple(r_A, 2, "r_A")
    a_vec = source_field_for_receiver(ra)
    v_cand = tuple(substate.X.v[i] + substate.sigma_A * a_vec[i] for i in range(869))
    delta_a = wave_energy(substate.X.u, v_cand) - wave_energy(substate.X.u, substate.X.v)
    b_cand = substate.b - delta_a
    if 0 <= b_cand <= substate.B:
        new_x = WaveTapeState(
            u=substate.X.u,
            v=v_cand,
            A0=substate.X.A0,
            A1=substate.X.A1,
            B0=substate.X.B0,
            B1=substate.X.B1,
            k=substate.X.k,
        )
        return ApparatusSubstate(
            X=new_x,
            W=substate.W + delta_a,
            b=b_cand,
            B=substate.B,
            sigma_A=-substate.sigma_A,
            sigma_B=substate.sigma_B,
            d=substate.d,
        )
    return substate


def funded_contact_B_substate(substate: ApparatusSubstate) -> ApparatusSubstate:
    if not isinstance(substate, ApparatusSubstate):
        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
    a_vec = source_field_for_receiver(substate.d)
    v_cand = tuple(substate.X.v[i] + substate.sigma_B * a_vec[i] for i in range(869))
    delta_b = wave_energy(substate.X.u, v_cand) - wave_energy(substate.X.u, substate.X.v)
    b_cand = substate.b - delta_b
    if 0 <= b_cand <= substate.B:
        new_x = WaveTapeState(
            u=substate.X.u,
            v=v_cand,
            A0=substate.X.A0,
            A1=substate.X.A1,
            B0=substate.X.B0,
            B1=substate.X.B1,
            k=substate.X.k,
        )
        return ApparatusSubstate(
            X=new_x,
            W=substate.W + delta_b,
            b=b_cand,
            B=substate.B,
            sigma_A=substate.sigma_A,
            sigma_B=-substate.sigma_B,
            d=substate.d,
        )
    return substate


def funded_contact_A(state: CompositeState) -> CompositeState:
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    sub = funded_contact_A_substate(state.to_apparatus_substate(), receiver_of(state.x_A))
    return CompositeState(
        n=state.n,
        x_A=state.x_A,
        x_B=state.x_B,
        X=sub.X,
        W=sub.W,
        b=sub.b,
        B=sub.B,
        sigma_A=sub.sigma_A,
        sigma_B=sub.sigma_B,
        d=sub.d,
        c=state.c,
    )


def funded_contact_B(state: CompositeState) -> CompositeState:
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    sub = funded_contact_B_substate(state.to_apparatus_substate())
    return CompositeState(
        n=state.n,
        x_A=state.x_A,
        x_B=state.x_B,
        X=sub.X,
        W=sub.W,
        b=sub.b,
        B=sub.B,
        sigma_A=sub.sigma_A,
        sigma_B=sub.sigma_B,
        d=sub.d,
        c=state.c,
    )


# ---------------------------------------------------------------------------
# Eight-phase static-source apparatus and coupled transitions
# ---------------------------------------------------------------------------

def apparatus_row_map(
    substate: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
) -> ApparatusSubstate:
    if not isinstance(substate, ApparatusSubstate):
        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
    phase = require_clock(c, 8, "c")
    ra = require_f5_tuple(r_A, 2, "r_A")
    rb = require_f5_tuple(r_B, 2, "r_B")
    if phase in (0, 7):
        return substate
    if phase == 1:
        new_d = buffer_capture_label(rb, substate.d)
        after_buf = ApparatusSubstate(
            X=substate.X,
            W=substate.W,
            b=substate.b,
            B=substate.B,
            sigma_A=substate.sigma_A,
            sigma_B=substate.sigma_B,
            d=new_d,
        )
        return funded_contact_A_substate(after_buf, ra)
    if phase in (2, 3, 5, 6):
        return ApparatusSubstate(
            X=F_step(substate.X),
            W=substate.W,
            b=substate.b,
            B=substate.B,
            sigma_A=substate.sigma_A,
            sigma_B=substate.sigma_B,
            d=substate.d,
        )
    return funded_contact_B_substate(substate)


def apparatus_row_map_inverse(
    substate_prime: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
) -> ApparatusSubstate:
    if not isinstance(substate_prime, ApparatusSubstate):
        raise TypeError(
            f"substate_prime must be ApparatusSubstate, got {type(substate_prime).__name__}"
        )
    phase = require_clock(c, 8, "c")
    ra = require_f5_tuple(r_A, 2, "r_A")
    rb = require_f5_tuple(r_B, 2, "r_B")
    if phase in (0, 7):
        return substate_prime
    if phase == 1:
        after_ha = funded_contact_A_substate(substate_prime, ra)
        old_d = buffer_capture_label_inverse(rb, after_ha.d)
        return ApparatusSubstate(
            X=after_ha.X,
            W=after_ha.W,
            b=after_ha.b,
            B=after_ha.B,
            sigma_A=after_ha.sigma_A,
            sigma_B=after_ha.sigma_B,
            d=old_d,
        )
    if phase in (2, 3, 5, 6):
        return ApparatusSubstate(
            X=F_inverse(substate_prime.X),
            W=substate_prime.W,
            b=substate_prime.b,
            B=substate_prime.B,
            sigma_A=substate_prime.sigma_A,
            sigma_B=substate_prime.sigma_B,
            d=substate_prime.d,
        )
    return funded_contact_B_substate(substate_prime)


def apparatus_step(
    substate: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
) -> Tuple[ApparatusSubstate, int]:
    phase = require_clock(c, 8, "c")
    return (apparatus_row_map(substate, phase, r_A, r_B), (phase + 1) % 8)


def apparatus_step_inverse(
    substate_prime: ApparatusSubstate, c_prime: int, r_A: Sequence[int], r_B: Sequence[int]
) -> Tuple[ApparatusSubstate, int]:
    phase_prime = require_clock(c_prime, 8, "c_prime")
    prev_phase = (phase_prime - 1) % 8
    return (apparatus_row_map_inverse(substate_prime, prev_phase, r_A, r_B), prev_phase)


def coupled_step(state: CompositeState) -> CompositeState:
    """Execute one phase row of G_B on arbitrary valid occupied state in Z_B."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    c = state.c
    if c == 0:
        n1, xa1, xb1 = native_tick(state.n, state.x_A, state.x_B)
        return CompositeState(
            n=n1,
            x_A=xa1,
            x_B=xb1,
            X=state.X,
            W=state.W,
            b=state.b,
            B=state.B,
            sigma_A=state.sigma_A,
            sigma_B=state.sigma_B,
            d=state.d,
            c=1,
        )
    if c == 1:
        _, new_d = buffer_capture(state.x_B, state.d)
        sub_after = funded_contact_A_substate(
            ApparatusSubstate(
                X=state.X,
                W=state.W,
                b=state.b,
                B=state.B,
                sigma_A=state.sigma_A,
                sigma_B=state.sigma_B,
                d=new_d,
            ),
            receiver_of(state.x_A),
        )
        return CompositeState(
            n=state.n,
            x_A=state.x_A,
            x_B=state.x_B,
            X=sub_after.X,
            W=sub_after.W,
            b=sub_after.b,
            B=sub_after.B,
            sigma_A=sub_after.sigma_A,
            sigma_B=sub_after.sigma_B,
            d=sub_after.d,
            c=2,
        )
    if c in (2, 3, 5, 6):
        n1, xa1, xb1 = native_tick(state.n, state.x_A, state.x_B)
        return CompositeState(
            n=n1,
            x_A=xa1,
            x_B=xb1,
            X=F_step(state.X),
            W=state.W,
            b=state.b,
            B=state.B,
            sigma_A=state.sigma_A,
            sigma_B=state.sigma_B,
            d=state.d,
            c=(c + 1) % 8,
        )
    if c == 4:
        sub_after = funded_contact_B_substate(state.to_apparatus_substate())
        return CompositeState(
            n=state.n,
            x_A=state.x_A,
            x_B=state.x_B,
            X=sub_after.X,
            W=sub_after.W,
            b=sub_after.b,
            B=sub_after.B,
            sigma_A=sub_after.sigma_A,
            sigma_B=sub_after.sigma_B,
            d=sub_after.d,
            c=5,
        )
    return CompositeState(
        n=state.n,
        x_A=state.x_A,
        x_B=state.x_B,
        X=state.X,
        W=state.W,
        b=state.b,
        B=state.B,
        sigma_A=state.sigma_A,
        sigma_B=state.sigma_B,
        d=state.d,
        c=0,
    )


def prepare_ready_state(
    p_A: Sequence[int],
    p_B: Sequence[int],
    B: Union[Fraction, int],
    *,
    b_init: Optional[Union[Fraction, int]] = None,
    c0: Optional[Sequence[Union[Fraction, int]]] = None,
    c1: Optional[Sequence[Union[Fraction, int]]] = None,
) -> CompositeState:
    """Prepare a common-ready state in R_{(c0, c1, b_init, B)} at c=0, n=0.

    Only the 4-piston inputs p_A, p_B with common ready receiver (0, 1) are loaded
    into x_A, x_B; no residue sum or source vector is preloaded into the apparatus.
    """
    pa = require_f5_tuple(p_A, 4, "p_A")
    pb = require_f5_tuple(p_B, 4, "p_B")
    cap = require_fraction(B, "B")
    b0_store = cap if b_init is None else require_fraction(b_init, "b_init")
    c0_vec = zero_q4() if c0 is None else require_q_tuple(c0, 4, "c0")
    c1_vec = zero_q4() if c1 is None else require_q_tuple(c1, 4, "c1")
    z_wave = zero_qd()
    z_tape = zero_q4()
    x_init = WaveTapeState(
        u=z_wave,
        v=z_wave,
        A0=z_tape,
        A1=z_tape,
        B0=c0_vec,
        B1=c1_vec,
        k=0,
    )
    return CompositeState(
        n=0,
        x_A=(pa[0], pa[1], pa[2], pa[3], 0, 1),
        x_B=(pb[0], pb[1], pb[2], pb[3], 0, 1),
        X=x_init,
        W=Fraction(0, 1),
        b=b0_store,
        B=cap,
        sigma_A=1,
        sigma_B=1,
        d=(0, 0),
        c=0,
    )


def run_seven_steps(
    state: CompositeState, *, return_boundaries: bool = False
) -> Union[CompositeState, Tuple[CompositeState, ...]]:
    """Advance 7 phase steps (c=0 -> c=7, n=0 -> n=5 on a ready state)."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    boundaries: List[CompositeState] = [state]
    cur = state
    for _ in range(7):
        cur = coupled_step(cur)
        boundaries.append(cur)
    if return_boundaries:
        return tuple(boundaries)
    return cur


def run_eight_steps(
    state: CompositeState, *, return_boundaries: bool = False
) -> Union[CompositeState, Tuple[CompositeState, ...]]:
    """Advance 8 phase steps (7 steps to completion c=7 plus 8th rollover c: 7 -> 0)."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    boundaries: List[CompositeState] = [state]
    cur = state
    for _ in range(8):
        cur = coupled_step(cur)
        boundaries.append(cur)
    if return_boundaries:
        return tuple(boundaries)
    return cur


# ---------------------------------------------------------------------------
# Machine-derived response operators (computed from basis dynamics, not tables)
# ---------------------------------------------------------------------------

def invert_4x4(mat: Tuple[Tuple[Fraction, ...], ...]) -> Tuple[Tuple[Fraction, ...], ...]:
    aug = [
        [mat[r][c] for c in range(4)] + [Fraction(1 if r == c else 0, 1) for c in range(4)]
        for r in range(4)
    ]
    for col in range(4):
        pivot = None
        for row in range(col, 4):
            if aug[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise ValueError("4x4 matrix is singular")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        piv_val = aug[col][col]
        for j in range(8):
            aug[col][j] /= piv_val
        for row in range(4):
            if row != col and aug[row][col] != 0:
                factor = aug[row][col]
                for j in range(8):
                    aug[row][j] -= factor * aug[col][j]
    return tuple(tuple(aug[r][4 + c] for c in range(4)) for r in range(4))


def mat_vec_4(
    mat: Tuple[Tuple[Fraction, ...], ...], vec: Sequence[Fraction]
) -> Tuple[Fraction, ...]:
    v_tup = require_q_tuple(vec, 4, "vec")
    return tuple(
        sum((mat[r][c] * v_tup[c] for c in range(4)), Fraction(0, 1)) for r in range(4)
    )


@dataclass(frozen=True)
class DerivedOperators:
    R0: Tuple[Tuple[Fraction, ...], ...]
    R0_inv: Tuple[Tuple[Fraction, ...], ...]
    R1: Tuple[Tuple[Fraction, ...], ...]
    D2: Tuple[Tuple[Fraction, ...], ...]
    D3: Tuple[Tuple[Fraction, ...], ...]
    Jp: Tuple[Tuple[Fraction, ...], ...]
    M: Tuple[Tuple[Fraction, ...], ...]


@lru_cache(maxsize=1)
def get_derived_operators() -> DerivedOperators:
    """Derive R0, R0^{-1}, R1, D2, D3, Jp, M directly from primary operators & F_step."""
    r0_cols: List[Tuple[Fraction, ...]] = []
    r1_cols: List[Tuple[Fraction, ...]] = []
    d2_cols: List[Tuple[Fraction, ...]] = []
    d3_cols: List[Tuple[Fraction, ...]] = []
    jp_cols: List[Tuple[Fraction, ...]] = []
    m_cols: List[Tuple[Fraction, ...]] = []

    z_wave = zero_qd()
    z_tape = zero_q4()
    for j in range(4):
        ej = basis_q4(j)
        f_ej = apply_S(ej)
        x0 = WaveTapeState(u=z_wave, v=f_ej, A0=z_tape, A1=z_tape, B0=z_tape, B1=z_tape, k=0)
        x1 = F_step(x0)
        x2 = F_step(x1)
        x3 = F_step(x2)
        x4 = F_step(x3)
        r0_cols.append(x4.A0)
        r1_cols.append(x4.A1)
        d2_cols.append(x4.B1)
        d3_cols.append(x4.B0)

        p_ej = apply_P(ej)
        jp_cols.append(apply_PT(apply_H(p_ej)))
        m_cols.append(apply_PT(apply_H(f_ej)))

    def transpose_cols(cols: List[Tuple[Fraction, ...]]) -> Tuple[Tuple[Fraction, ...], ...]:
        return tuple(tuple(cols[c][r] for c in range(4)) for r in range(4))

    r0 = transpose_cols(r0_cols)
    return DerivedOperators(
        R0=r0,
        R0_inv=invert_4x4(r0),
        R1=transpose_cols(r1_cols),
        D2=transpose_cols(d2_cols),
        D3=transpose_cols(d3_cols),
        Jp=transpose_cols(jp_cols),
        M=transpose_cols(m_cols),
    )


# ---------------------------------------------------------------------------
# Direct chronological cut reader and direct source reader (API-restricted)
# ---------------------------------------------------------------------------

VALID_FIRST_PERIOD_CLOCKS: Dict[int, int] = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 3,
    6: 4,
    7: 5,
}


def direct_chronological_cut_reader(
    state: CompositeState,
) -> Tuple[ChronologicalCutEntry, ChronologicalCutEntry, ChronologicalCutEntry, ChronologicalCutEntry]:
    """Read the 4 chronological cuts directly from (n, c) and tapes (A0, A1, B0, B1)."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    expected_n = VALID_FIRST_PERIOD_CLOCKS.get(state.c)
    if expected_n != state.n:
        raise ValueError(
            f"State (c={state.c}, n={state.n}) is not a valid first-period boundary"
        )
    unwritten = ChronologicalCutEntry(
        status="UNWRITTEN", use=None, cut=None, slot_name=None, vector=None
    )
    c = state.c
    if c in (0, 1, 2):
        return (unwritten, unwritten, unwritten, unwritten)
    if c == 3:
        return (
            ChronologicalCutEntry("PRESENT", 1, 0, "B0", state.X.B0),
            unwritten,
            unwritten,
            unwritten,
        )
    if c in (4, 5):
        return (
            ChronologicalCutEntry("PRESENT", 1, 0, "B1", state.X.B1),
            ChronologicalCutEntry("PRESENT", 1, 1, "B0", state.X.B0),
            unwritten,
            unwritten,
        )
    if c == 6:
        return (
            ChronologicalCutEntry("PRESENT", 1, 0, "A1", state.X.A1),
            ChronologicalCutEntry("PRESENT", 1, 1, "B1", state.X.B1),
            ChronologicalCutEntry("PRESENT", 2, 2, "B0", state.X.B0),
            unwritten,
        )
    return (
        ChronologicalCutEntry("PRESENT", 1, 0, "A0", state.X.A0),
        ChronologicalCutEntry("PRESENT", 1, 1, "A1", state.X.A1),
        ChronologicalCutEntry("PRESENT", 2, 2, "B1", state.X.B1),
        ChronologicalCutEntry("PRESENT", 2, 3, "B0", state.X.B0),
    )


def extract_direct_port_readout(
    state: CompositeState, *, include_d: bool = False, include_sigma_B: bool = True
) -> DirectPortReadout:
    """Extract only (b0, b2) and declared acceptance/context fields at c=7, n=5."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
    if state.c != 7 or state.n != 5:
        raise ValueError(f"Direct port readout requires completion boundary c=7, n=5; got c={state.c}, n={state.n}")
    return DirectPortReadout(
        b0=state.X.A0,
        b2=state.X.B1,
        sigma_A=state.sigma_A,
        sigma_B=state.sigma_B if include_sigma_B else None,
        d=state.d if include_d else None,
    )


def direct_source_reader(
    b0: Union[Sequence[Union[Fraction, int]], DirectPortReadout],
    b2: Optional[Sequence[Union[Fraction, int]]] = None,
    *,
    sigma_A: Optional[int] = -1,
    sigma_B: Optional[int] = -1,
    d: Optional[Sequence[int]] = None,
) -> Dict[str, object]:
    """Decode (z_A, z_B) from (b0, b2) and declared acceptance/context information.

    API access restriction: rejects CompositeState, ApparatusSubstate, WaveTapeState,
    and 6-element native checkpoints. Never accesses x_A, x_B, p_A, p_B, or c0, c1.
    Supports both:
      (1) standard (sigma_A, sigma_B) acceptance readout; and
      (2) Clarification (ii) ready-family second-acceptance readout from (d, b0, b2)
          when sigma_B is None and d is provided.
    """
    if isinstance(b0, (CompositeState, ApparatusSubstate, WaveTapeState)):
        raise TypeError(
            "direct_source_reader forbids CompositeState/ApparatusSubstate/WaveTapeState access"
        )
    if isinstance(b2, (CompositeState, ApparatusSubstate, WaveTapeState)):
        raise TypeError(
            "direct_source_reader forbids CompositeState/ApparatusSubstate/WaveTapeState access"
        )

    if isinstance(b0, DirectPortReadout):
        if b2 is not None:
            raise ValueError("When passing DirectPortReadout as first argument, omit b2")
        b0_vec = b0.b0
        b2_vec = b0.b2
        sig_a = b0.sigma_A
        sig_b = b0.sigma_B
        d_val = b0.d
    else:
        if b2 is None:
            raise ValueError("b2 must be provided when b0 is a 4-vector")
        b0_vec = require_q_tuple(b0, 4, "b0")
        b2_vec = require_q_tuple(b2, 4, "b2")
        sig_a = None if sigma_A is None else require_sign(sigma_A, "sigma_A")
        sig_b = None if sigma_B is None else require_sign(sigma_B, "sigma_B")
        d_val = None if d is None else require_f5_tuple(d, 2, "d")

    ops = get_derived_operators()
    alpha_a_z_a = mat_vec_4(ops.R0_inv, b0_vec)
    residual_b2 = tuple(
        b2_vec[j] - mat_vec_4(ops.D2, alpha_a_z_a)[j] for j in range(4)
    )
    alpha_b_z_b = mat_vec_4(ops.R0_inv, residual_b2)

    alpha_a: Optional[int] = None
    z_a: Optional[Tuple[Fraction, ...]] = None
    if sig_a is not None:
        alpha_a = (1 - sig_a) // 2
        if alpha_a == 1:
            z_a = alpha_a_z_a
        else:
            if any(x != 0 for x in b0_vec):
                raise ValueError("Inconsistent refused sigma_A=+1 with non-zero b0")
            z_a = None
    elif any(x != 0 for x in b0_vec):
        alpha_a = 1
        z_a = alpha_a_z_a

    # Clarification (ii): on the ready family, alpha_B is readable from (d, b0, b2)
    alpha_b_from_d: Optional[int] = None
    if d_val is not None:
        z_b_cand = eta_lift(d_val)
        if all(x == 0 for x in z_b_cand):
            if any(x != 0 for x in residual_b2):
                raise ValueError("Inconsistent d=(0,4) with non-zero b2 - D2(alpha_A z_A)")
            alpha_b_from_d = 1
        else:
            expected_r0_zb = mat_vec_4(ops.R0, z_b_cand)
            if residual_b2 == expected_r0_zb:
                alpha_b_from_d = 1
            elif all(x == 0 for x in residual_b2):
                alpha_b_from_d = 0
            else:
                raise ValueError("Residual b2 - D2(alpha_A z_A) does not match d on ready family")

    alpha_b: Optional[int] = None
    if sig_b is not None:
        alpha_b = (1 - sig_b) // 2
        if alpha_b_from_d is not None and alpha_b != alpha_b_from_d:
            raise ValueError("Mismatch between sigma_B and (d, b0, b2) acceptance readout")
    elif alpha_b_from_d is not None:
        alpha_b = alpha_b_from_d

    z_b: Optional[Tuple[Fraction, ...]] = None
    if alpha_b == 1:
        z_b = alpha_b_z_b
    elif alpha_b == 0:
        if any(x != 0 for x in residual_b2):
            raise ValueError("Inconsistent refused Contact B with non-zero residual b2")
        z_b = None

    return {
        "alpha_A": alpha_a,
        "alpha_B": alpha_b,
        "alpha_B_from_d_b0_b2": alpha_b_from_d,
        "z_A": z_a,
        "z_B": z_b,
        "alpha_A_z_A": alpha_a_z_a,
        "alpha_B_z_B": alpha_b_z_b,
    }


# ---------------------------------------------------------------------------
# Full-input endpoint inverse and ready-image recognizer (native-head access)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def get_native_c3_table() -> Dict[int, Dict[str, object]]:
    """Derive the 5-row canonical native table for h=0..4 from primary native_tick_single."""
    table: Dict[int, Dict[str, object]] = {}
    for h in range(5):
        x0 = (h, 0, 0, 0, 0, 1)
        j0 = native_selector(0, x0)
        _, x1 = native_tick_single(0, x0)
        j1 = native_selector(1, x1)
        _, x2 = native_tick_single(1, x1)
        j2 = native_selector(2, x2)
        _, x3 = native_tick_single(2, x2)
        j3 = native_selector(3, x3)
        _, x4 = native_tick_single(3, x3)
        j4 = native_selector(4, x4)
        _, x5 = native_tick_single(4, x4)
        table[h] = {
            "selectors": (j0, j1, j2, j3, j4),
            "C1": receiver_of(x1),
            "C2": receiver_of(x2),
            "C3": receiver_of(x3),
            "C5": receiver_of(x5),
        }
    return table


def recognize_ready_image(
    state: CompositeState,
    *,
    c0: Optional[Sequence[Union[Fraction, int]]] = None,
    c1: Optional[Sequence[Union[Fraction, int]]] = None,
    b_init: Optional[Union[Fraction, int]] = None,
) -> Dict[str, object]:
    """Necessary-and-sufficient 4-part recognizer for Im(Phi_{(c0, c1, b_init, B)})."""
    if not isinstance(state, CompositeState):
        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")

    # Test 1: Clock n=5, c=7 and C_3 receivers at n=5
    if state.n != 5 or state.c != 7:
        return {"valid": False, "failed_test": "test1_clock_n5_c7"}

    c3_table = get_native_c3_table()
    c3_to_h = {info["C3"]: h for h, info in c3_table.items()}
    rec_5a = receiver_of(state.x_A)
    rec_5b = receiver_of(state.x_B)
    if rec_5a not in c3_to_h or rec_5b not in c3_to_h:
        return {"valid": False, "failed_test": "test1_c3_receiver"}
    h_a = c3_to_h[rec_5a]
    h_b = c3_to_h[rec_5b]

    # Test 2: Inverse generator words, (0,1) receiver, AND piston-sum selector consistency
    sel_a: Tuple[int, ...] = c3_table[h_a]["selectors"]  # type: ignore[assignment]
    sel_b: Tuple[int, ...] = c3_table[h_b]["selectors"]  # type: ignore[assignment]
    x0_a = apply_generator(
        sel_a[0], apply_generator(sel_a[1], apply_generator(sel_a[2], state.x_A))
    )
    x0_b = apply_generator(
        sel_b[0], apply_generator(sel_b[1], apply_generator(sel_b[2], state.x_B))
    )
    if receiver_of(x0_a) != (0, 1) or receiver_of(x0_b) != (0, 1):
        return {"valid": False, "failed_test": "test2_initial_receiver"}
    p_a = x0_a[:4]
    p_b = x0_b[:4]
    if sum(p_a) % 5 != h_a or sum(p_b) % 5 != h_b:
        return {"valid": False, "failed_test": "test2_piston_sum_selector_consistency"}

    # Test 3: Delayed buffer d == rec(x_{1,B}) == C_1(h_B)
    x1_a = apply_generator(sel_a[0], x0_a)
    x1_b = apply_generator(sel_b[0], x0_b)
    r_a = receiver_of(x1_a)
    r_b = receiver_of(x1_b)
    if state.d != r_b:
        return {"valid": False, "failed_test": "test3_delayed_buffer_d"}

    # Test 4: Apparatus two-sided inverse (M_{7,B}^{(r_A, r_B)})^{-1}
    sub = state.to_apparatus_substate()
    c_cur = 7
    for _ in range(7):
        sub, c_cur = apparatus_step_inverse(sub, c_cur, r_a, r_b)
    if c_cur != 0:
        return {"valid": False, "failed_test": "test4_apparatus_clock"}

    z_wave = zero_qd()
    z_tape = zero_q4()
    if sub.X.u != z_wave or sub.X.v != z_wave:
        return {"valid": False, "failed_test": "test4_initial_wave_zero"}
    if sub.X.A0 != z_tape or sub.X.A1 != z_tape:
        return {"valid": False, "failed_test": "test4_initial_tape_A_zero"}
    if sub.X.k != 0:
        return {"valid": False, "failed_test": "test4_initial_k_zero"}
    if sub.W != 0:
        return {"valid": False, "failed_test": "test4_initial_W_zero"}
    if (sub.sigma_A, sub.sigma_B) != (1, 1):
        return {"valid": False, "failed_test": "test4_initial_sigma_plus1"}
    if sub.d != (0, 0):
        return {"valid": False, "failed_test": "test4_initial_d_zero"}

    if b_init is not None:
        b_exp = require_fraction(b_init, "b_init")
        if sub.b != b_exp:
            return {"valid": False, "failed_test": "test4_initial_store_b"}
    if c0 is not None:
        c0_exp = require_q_tuple(c0, 4, "c0")
        if sub.X.B0 != c0_exp:
            return {"valid": False, "failed_test": "test4_initial_archive_c0"}
    if c1 is not None:
        c1_exp = require_q_tuple(c1, 4, "c1")
        if sub.X.B1 != c1_exp:
            return {"valid": False, "failed_test": "test4_initial_archive_c1"}

    # Also verify that forward 7-step replay from the recovered initial state matches state
    replayed = run_seven_steps(
        prepare_ready_state(
            p_a, p_b, state.B, b_init=sub.b, c0=sub.X.B0, c1=sub.X.B1
        )
    )
    if replayed != state:
        return {"valid": False, "failed_test": "test4_forward_replay_mismatch"}

    return {
        "valid": True,
        "failed_test": None,
        "p_A": p_a,
        "p_B": p_b,
        "h_A": h_a,
        "h_B": h_b,
        "c0": sub.X.B0,
        "c1": sub.X.B1,
        "b_init": sub.b,
    }


def recover_prepared_inputs(
    state: CompositeState,
    *,
    c0: Optional[Sequence[Union[Fraction, int]]] = None,
    c1: Optional[Sequence[Union[Fraction, int]]] = None,
    b_init: Optional[Union[Fraction, int]] = None,
) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    """Left inverse D(Z(7)) returning (p_A, p_B) in F_5^4 x F_5^4 or raising ValueError."""
    res = recognize_ready_image(state, c0=c0, c1=c1, b_init=b_init)
    if not res["valid"]:
        raise ValueError(f"State is not in the prepared ready image ({res['failed_test']})")
    return (res["p_A"], res["p_B"])  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Shared 1200-record comparison mode serialization (TWOUSE-COMPARE-v1)
# ---------------------------------------------------------------------------

def encode_rat(val: Fraction) -> List[int]:
    return [val.numerator, val.denominator]


def serialize_comparison_record(
    B: Fraction, h_A: int, h_B: int, state: CompositeState
) -> str:
    record = [
        encode_rat(B),
        h_A,
        h_B,
        state.c,
        state.n,
        list(state.x_A),
        list(state.x_B),
        [encode_rat(x) for x in state.X.u],
        [encode_rat(x) for x in state.X.v],
        [encode_rat(x) for x in state.X.A0],
        [encode_rat(x) for x in state.X.A1],
        [encode_rat(x) for x in state.X.B0],
        [encode_rat(x) for x in state.X.B1],
        state.X.k,
        encode_rat(state.W),
        encode_rat(state.b),
        [state.sigma_A, state.sigma_B],
        list(state.d),
    ]
    return json.dumps(record, separators=(",", ":"), ensure_ascii=True) + "\n"


def compute_comparison_digest() -> Tuple[int, str]:
    """Stream the 1200 frozen comparison records and compute their SHA-256 digest."""
    hasher = hashlib.sha256()
    count = 0
    for cap in COMPARISON_CAPACITIES:
        for h_a in range(5):
            for h_b in range(5):
                p_a = (h_a, 0, 0, 0)
                p_b = (h_b, 0, 0, 0)
                init_state = prepare_ready_state(p_a, p_b, cap, b_init=cap)
                boundaries = run_seven_steps(init_state, return_boundaries=True)
                assert isinstance(boundaries, tuple) and len(boundaries) == 8
                for c_idx, b_state in enumerate(boundaries):
                    if b_state.c != c_idx:
                        raise RuntimeError(f"Boundary clock mismatch: {b_state.c} != {c_idx}")
                    line = serialize_comparison_record(cap, h_a, h_b, b_state)
                    hasher.update(line.encode("ascii"))
                    count += 1
    return (count, hasher.hexdigest())
