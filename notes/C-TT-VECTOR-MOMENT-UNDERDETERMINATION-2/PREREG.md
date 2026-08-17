# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 preregistration

Incubation candidate. No authority. This document promotes nothing.

Candidate id: `C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2`
Line targeted on promotion: `mathorn1973/twist-j`, `main`, same single registry
row `TT-VECTOR-MOMENT-UNDERDETERMINATION` as candidate -1, per the owner
ruling of 2026-08-17 that there is one row, not three.
Parent: `TT-VECTOR-STATE-NORMALIZATION` [O]. Untouched. It remains O / STOP.

Purpose. This candidate exists to resolve two open owner decisions by
computation instead of by taste. D2: the six-member family form of the
underdetermination, proved after the freeze of candidate -1 and therefore
inadmissible there, is frozen properly here. D3: the diagonal
site-and-Galois variant of the four-fold action, excluded from -1 by its
systematic S2, is given its own frozen statement here. Candidate -1 is not
modified in any way; its directory and pins stay byte-exact.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v50
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v50
CONTENT_COMMIT: b68c60c57cfd0b1e655b6fc4d5496a333a249fdf
CANON_SHA256:   f99f5eeb42db3e9d40bc6a46f716aa98d7af1925b66989406e0b3671ab43a9fe
CANON_BYTES:    240724
BASE_COMMIT:    4020c5373453ef4b8466a8738337be187fc238b6
LINEAGE:        notes branch of candidate -1 at commit
                05cf23f4118c86e60b876c7665d07016c14db549, parent 4020c537
CLAIM_ISSUE:    the incubation lock issue of this lane, number 407. Incubation
                only. No public probe, no fold.
```

Currency gate run before this freeze, fresh shallow clone: `main` equals the
base commit; `canon/SHA256SUMS` 5 of 5 OK; STATUS fields as above; the only
branch in this lane is the candidate -1 branch; no directory or identifier
matching `-2`, `FAMILY` or `DIAGONAL` exists under `notes/` at `main`.

Frozen input pins from candidate -1, read only, never edited:

```text
PREREG.md    sha256 091ef70b0b0f65247afab229c1d4a8a9ade7ccdaa9a0009de6f26a052a7d519d
verify.py    sha256 68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c
EXPECTED.txt sha256 d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6
RESULT.md    sha256 1d5001b7b0a12542fdb8d9615fd7cf4ba6a3580061ea0de776e87dfcc7079dc4
```

## Field 1. Equation

Carrier `X = Z/5`, `z = zeta_5`, scale frozen at `a = 1`. Coefficient field
`Q(zeta_5)` on the basis `{1, z, z^2, z^3}` with
`z^4 = -(1 + z + z^2 + z^3)`. A monomial is
`M = prod_x v_x^{p_x} conj(v_x)^{q_x}` with net exponents `n_x = p_x - q_x`,
total degree `d = sum_x (p_x + q_x)`, weight sum `S = sum_x n_x`, and site
moment `W = sum_x x n_x`.

The six extremal laws and the mixture:

```text
A     : v_x = z^{t_x},              (t_x) iid uniform on Z/5
B_m   : v_x = z^{t_0 + m x} eps_x,  m in Z/5, t_0 uniform on Z/5,
                                    independent of (eps_x) iid uniform {+1,-1}
Bmix  : uniform mixture of B_1, B_2, B_3, B_4, weight 1/4 each
```

Four group actions, written as formulas. `sigma_u` is the field automorphism
of `Q(zeta_5)` with `sigma_u(z) = z^u`, `u` in `(Z/5)^*`.

```text
tau_c    (tau_c v)_x  = v_{x-c}                     translation
rho_u    (rho_u v)_x  = v_{u^{-1} x}                site four-fold
gamma_u  (gamma_u v)_x = sigma_u(v_x)               coefficient four-fold
D_u      (D_u v)_x    = sigma_u(v_{u^{-1} x})       diagonal four-fold
```

Composition claim, part of the statement: `D_u = gamma_u rho_u = rho_u
gamma_u` as operators on fields, because `gamma` acts pointwise on values and
`rho` permutes sites.

Squared readout `w_x = v_x^2`, spectra `S_w`, `Pi_w` and second-order data
`C`, `P`, `S_v`, `Pi_v` exactly as in the -1 preregistration, same Fourier
sign convention `S(k) = sum_r C_{r,0} z^{-k r}`.

### Statement P1, family agreement through degree 3

Every monomial of total degree at most 3 has the same expectation under all
six laws `A, B_0, ..., B_4`. Consequently all fifteen unordered pairs agree on
the mean, on `C = delta`, on `P = 0`, on `S_v = 1`, on `Pi_v = 0`, and on
every polynomial functional of degree at most 3.

### Statement P2, universal degree-4 separator set

For every ordered pair of distinct laws among the six, the set of degree-4
monomials with differing expectations is exactly the same twenty monomials
`v_x^2 conj(v_y)^2` with `x != y`. No pair has any other degree-4 separator.

### Statement P3, the value table reads the index

```text
E_A    [v_x^2 conj(v_y)^2] = 0             for x != y
E_{B_m}[v_x^2 conj(v_y)^2] = z^{2 m (x-y)} for x != y, every m in Z/5
E_L    [v_x^2 conj(v_x)^2] = 1             for every law L of the six
```

So the fourth moments read the family index `m` exactly, one `Z/5` datum,
consistent with the peak position `2m`.

### Statement P4, spectra

`S_w(k) = 1` for all `k` under `A`; `S_w(k) = 5 delta_{k, 2m mod 5}` under
`B_m` for every `m`; `S_w(0) = 0` and `S_w(k) = 5/4` for `k != 0` under
`Bmix`; `Pi_w = 0` under all seven laws.

### Statement P5, the action table and the diagonal collapse

As equalities of measures:

```text
tau_c  L     = L                 all seven laws, all c
rho_u  A     = A,   rho_u  Bmix = Bmix,   rho_u  B_m = B_{u^{-1} m mod 5}
gamma_u A    = A,   gamma_u Bmix = Bmix,  gamma_u B_m = B_{u m mod 5}
D_u    L     = L                 all seven laws, all u
```

The site action and the coefficient action move the family index by inverse
multiplications, so their diagonal fixes every member. Consequence, the
corrected form of the withdrawn claim E1 of the earlier lane comment: for
every target mode `k_0` in `Z/5` the law `B_{3 k_0 mod 5}` is invariant under
translation and under the full diagonal four-fold action, has deterministic
pointwise modulus, agrees with `A` on every polynomial functional of degree at
most 3, and has `S_w = 5 delta_{k, k_0}`. Arbitrary peak placement is
compatible with full diagonal four-fold invariance. The peak map is
`m = 3 k_0 mod 5` because `2 * 3 = 6 = 1 mod 5`:

```text
k_0  0 1 2 3 4
m    0 3 1 4 2
```

### Statement P6, degree-5 inventory, the p = 5 signature

At total degree 5 the separators between `A` and any `B_m` are exactly the ten
fifth powers `v_x^5` and `conj(v_x)^5`, with `E_A = 1` and `E_{B_m} = 0`. No
pair among `B_0, ..., B_4` separates at degree 5, and by the parity argument
no such pair separates at any odd degree. The value `E_A[v_x^5] = 1` is the
first moment at which the fifth-root structure of `A` becomes visible: `v^5`
collapses to `1` configuration by configuration.

### Statement P7, fixed-modulus fourth cumulant, family-wide

`E[|v_x|^4] = 1` and `K_{xx} = -1` under all six extremal laws, extending the
-1 statement S2 from the pair to the family at `a = 1`.

### What is not claimed

Everything the -1 preregistration excluded stays excluded: no closure of the
parent, no `r_T(k)`, no action functional, no scalar spectrum, no physical
identification of `w`, no tensor spectrum, no helicity, no observable, no
cosmology, and no statement about `J`, `p = 5` as physics, the decoder, Born,
measure, observer, force, spacetime, the Plenum, SI units, or layers L2 to
L6. Additionally: no claim that the six laws exhaust the degree-3-equivalent
class, and no claim about any mixture other than `Bmix`.

## Field 2. Code

`verify.py`, Python standard library only, exact arithmetic, no float
anywhere, deterministic, under 120 seconds, environment
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`. The
exact-arithmetic engine is the same design as the -1 verifier by the same
author; that is disclosed, and independence is supplied by the breaker, not by
the verifier pair. Enumeration is complete: monomial sweeps of every degree up
to 5 over all six extremal laws, action checks as pushforward equalities of
complete weighted configuration dictionaries.

`breaker.py`, an independent second code path: closed-form character sums,
`E_A[M] = prod_x [n_x = 0 mod 5]` and
`E_{B_m}[M] = [all p_x + q_x even][S = 0 mod 5] z^{m W}`, cross-bound to
enumeration on every monomial of degree at most 5 on all six laws, plus a
character-algebra proof of the diagonal collapse at every degree up to 6: for
every monomial, every `u`, every law, the identity
`sigma_u( cf(p compose u, q compose u) ) = cf(p, q)` where
`(p compose u)_y = p_{u y mod 5}`. The orbit statements are also checked at
the moment level: `cf_{B_m}(p compose u, q compose u) = cf_{B_{u^{-1} m}}(p,
q)` and `sigma_u(cf_{B_m}(p, q)) = cf_{B_{u m}}(p, q)` for every monomial of
degree at most 4.

## Field 3. Carrier or data

No external data. Complete finite enumeration: `A` on 3125 configurations at
weight 1/3125, each `B_m` on 160 configurations at weight 1/160, `Bmix` on 640
at weight 1/640. Monomial counts, frozen: 286 of degree at most 3, 715 of
degree exactly 4, 2002 of degree exactly 5, 8008 of degree at most 6.

## Field 4. Systematics

```text
S1  Fourier convention as in -1: S(k) = sum_r C_{r,0} z^{-k r}.
S2  Composition order: D_u = gamma_u rho_u; the reverse composition is claimed
    equal and is gated, not assumed.
S3  sigma_u is the field automorphism of Q(zeta_5), applied only on the
    algebraic configuration space of signed fifth roots of unity. It commutes
    with complex conjugation because conjugation is sigma_4 and the Galois
    group is abelian. No archimedean continuity of sigma_u is claimed and none
    is used; on this configuration space it preserves the modulus because
    every value is a signed root of unity.
S4  Index arithmetic in Z/5. Peak of B_m at k = 2m; inverse map m = 3 k_0.
S5  Scale frozen at a = 1. Mixtures: only Bmix is gated; no other mixture.
S6  Monomial sweeps run over the six extremal laws only; Bmix enters only the
    spectrum and action gates, since its moments follow by linearity.
S7  Existence and equality statements are carried by written proofs; the
    verifier audits them at complete finite scope and is not the source of a
    computed status. Candidate -1 is an input by hash only and is not rerun.
```

## Field 5. Failure threshold

Exact and binary. Any one fires, the candidate is recorded F and archived:

```text
F1  any monomial of degree at most 3 separating any pair of the six laws.
F2  any pair whose degree-4 separator set differs from the twenty, or any
    entry of the P3 value table wrong, in either direction.
F3  any P5 action-table entry failing as an equality of measures, including
    any D_u L != L, or the composition claim failing on any configuration.
F4  any spectrum in P4 wrong.
F5  the degree-5 inventory differing from P6 in membership or in values, or
    any degree-5 separator between two B laws.
F6  E[|v_x|^4] != 1 or K_{xx} != -1 under any of the six laws.
F7  verifier and breaker disagreeing on any shared quantity: integrity STOP.
F8  any float in the verifier or in any assertion: integrity STOP.
```

## Field 6. Action layer

`L1`, state, and only `L1`. Everything declared in field 6 of the -1
preregistration carries over verbatim: `v -> w = v^2` is a pure `L1` algebraic
map, `S_w` is the power spectrum of the squared readout, no gate is created,
`canon/GATES.tsv` is not touched. The new ingredient, `gamma_u`, is an
algebraic operation on state values inside `L1`; it identifies nothing
physical and lifts nothing. The moment any of this is identified with a
physical tensor field, that is a layer lift needing its own named gate, which
this document does not supply.

## Freeze

Nothing was computed, enumerated or executed for this candidate before this
file was written. `verify.py` is written next and hashed together with this
file before its first execution; the first execution is the one reported. No
amendment, no second freeze, no renaming. The derivations behind P1 to P7 are
paper derivations recorded as proofs in the result document; deriving a
prediction on paper before freezing is what a preregistration is for.

Commit identity for the public carry: `A. M. Thorn <thorn@twistj.com>`.
