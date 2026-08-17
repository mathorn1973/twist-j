# P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 preregistration

Public validation probe under `POLICY.md` and `AGENTS.md`. One owner, one
session, claimed in issue #408 before this pin.

```text
PROBE:          P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
TARGET ROW:     TT-VECTOR-MOMENT-UNDERDETERMINATION, proposed T, one row per
                the owner ruling of 2026-08-17
PARENT ROW:     TT-VECTOR-STATE-NORMALIZATION [O], unchanged by this probe,
                stays O / STOP, not closed in either direction
STATEMENT:      FAMILY form, per the owner ruling of 2026-08-17
BASE:           main at 4020c5373453ef4b8466a8738337be187fc238b6,
                Public Canon v50, ACTIVE
CLAIM ISSUE:    #408
LAYER:          L1 only. No gate created. canon/GATES.tsv untouched.
CANON SECTION:  14. The gravitational wave program, by registry precedent:
                at the base commit section 18 carries 14 O and 2 H rows and
                zero theorems, and every T row lives in a content section
```

## Provenance and disclosure

This probe carries a promotion proposal in from the incubation lane, which is
the designed path: the lane derives and freezes, this repository validates
and gates. Lane record: issue #407 and branch
`notes/c-tt-vector-moment-underdetermination-1` at commit
`09182ec9b7b4a7649cc3fda5d56c4703ed5a6b52`, candidates
`C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1` (the pair and the Wick no-go) and
`C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2` (the family, the value table, the
action table with the diagonal collapse, the degree-5 inventory), with the
consumable proposal `PROMO.md` in the candidate -2 directory.

Disclosed plainly, so that nothing about the order of events is hidden:

1. `verify.py` in this directory is byte-identical to the verifier frozen in
   the candidate -2 record before its first execution there, SHA-256
   `a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67`,
   13802 bytes, including its candidate header line. Byte identity is the
   audit property and is preferred over a cosmetic rename.
2. The lane computation preceded this public pin. Its falsifiers, the same
   F1 to F8 frozen below, were armed in the lane preregistration before that
   computation ran. The accepted stdout there has SHA-256
   `711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c`,
   3013 bytes, reproduced byte-identically on x86_64 Linux CPython 3.12.3
   and arm64 macOS CPython 3.9.6.
3. An independent breaker on a disjoint closed-form character-sum code path,
   11 gates, zero breaks, including the diagonal moment identity at every
   degree up to six, is recorded in the lane, SHA-256
   `1ea4b98e174c5271f17310f76c60dad1051faa512fe2393a58d5297cfb899738`. The
   repository layout keeps probe directories to the five required files, so
   the breaker stays in the lane and is cited here by hash.
4. This probe therefore validates a known statement under the public
   discipline: pin first, then a local formal leg from a fresh clone of the
   pinned branch, then the required GitHub x86_64 and aarch64 jobs at
   pull-request time with byte-identical stdout. Nothing is imported by
   reference alone: the full statement, the falsifiers, and the proofs are
   in this file.

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
tau_c    (tau_c v)_x   = v_{x-c}                    translation
rho_u    (rho_u v)_x   = v_{u^{-1} x}               site four-fold
gamma_u  (gamma_u v)_x = sigma_u(v_x)               coefficient four-fold
D_u      (D_u v)_x     = sigma_u(v_{u^{-1} x})      diagonal four-fold
```

Composition claim, part of the statement: `D_u = gamma_u rho_u = rho_u
gamma_u` as operators on fields, because `gamma` acts pointwise on values and
`rho` permutes sites.

Squared readout `w_x = v_x^2`. Second-order data `C_{xy} = E[v_x conj(v_y)]`,
`P_{xy} = E[v_x v_y]`, spectra `S_v(k) = sum_r C_{r,0} z^{-k r}` and the
analogous `Pi_v` from `P`; `C^w`, `S_w`, `Pi_w` the same objects for `w`.

### Statement P1, family agreement through degree 3

Every monomial of total degree at most 3 has the same expectation under all
six laws `A, B_0, ..., B_4`. Consequently all fifteen unordered pairs agree
on the mean, on `C = delta`, on `P = 0`, on `S_v = 1`, on `Pi_v = 0`, and on
every polynomial functional of degree at most 3.

### Statement P2, universal degree-4 separator set

For every pair of distinct laws among the six, the set of degree-4 monomials
with differing expectations is exactly the same twenty monomials
`v_x^2 conj(v_y)^2` with `x != y`. No pair has any other degree-4 separator.

### Statement P3, the value table reads the index

```text
E_A    [v_x^2 conj(v_y)^2] = 0             for x != y
E_{B_m}[v_x^2 conj(v_y)^2] = z^{2 m (x-y)} for x != y, every m in Z/5
E_L    [v_x^2 conj(v_x)^2] = 1             for every law L of the six
```

The fourth moments read the family index `m` exactly, one `Z/5` datum,
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
multiplications, so their diagonal fixes every member. Consequence: for every
target mode `k_0` in `Z/5` the law `B_{3 k_0 mod 5}` is invariant under
translation and under the full diagonal four-fold action, has deterministic
pointwise modulus, agrees with `A` on every polynomial functional of degree
at most 3, and has `S_w = 5 delta_{k, k_0}`. Arbitrary peak placement is
compatible with full diagonal four-fold invariance. The peak map is
`m = 3 k_0 mod 5` because `2 * 3 = 6 = 1 mod 5`:

```text
k_0  0 1 2 3 4
m    0 3 1 4 2
```

### Statement P6, degree-5 inventory

At total degree 5 the separators between `A` and any `B_m` are exactly the
ten fifth powers `v_x^5` and `conj(v_x)^5`, with `E_A = 1` and `E_{B_m} = 0`.
No pair among `B_0, ..., B_4` separates at degree 5, and by the parity
argument no such pair separates at any odd degree. The value
`E_A[v_x^5] = 1` is the first moment at which the fifth-root structure of `A`
becomes visible: the fifth power collapses to 1 configuration by
configuration. This is stated as arithmetic of the carrier, not as physics.

### Statement P7, fixed-modulus fourth cumulant

`E[|v_x|^4] = 1` and `K_{xx} = -1` under all six extremal laws, where
`K_{xy} = E[v_x^2 conj(v_y)^2] - P_{xx} conj(P_{yy}) - 2 C_{xy}^2`. In
general, any state with `E[v_x] = 0`, `P_{xx} = 0` and `|v_x|^2 = a^2` almost
surely at `a > 0` has `E[|v_x|^4] = a^4` against the Isserlis value `2 a^4`,
hence `K_{xx} = -a^4`, so no such state is Gaussian and no Wick closure
exists at fixed modulus.

### What is not claimed

No closure of the parent, no `r_T(k)`, no action functional, no Stage-B
pullback, no scalar spectrum, no physical identification of `w`, no tensor
spectrum, no helicity, no observable, no cosmology, and no statement about
`J`, `p = 5` as physics, the decoder, Born, measure, observer, force,
spacetime, the Plenum, SI units, or layers L2 to L6. No claim that the six
laws exhaust their degree-3 equivalence class, and no claim about any
mixture other than `Bmix`.

## Field 2. Code

`verify.py`, Python standard library only, exact arithmetic over `Q(zeta_5)`
with `fractions.Fraction` coefficients and integer exponent arithmetic in
`Z/5`, no float literal and no float operation anywhere, deterministic,
under 120 seconds, run from the repository root as
`python3 probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1/verify.py` with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Exit 0 on all 40 gates PASS, exit 1 otherwise; stdout is the sole result
surface and is byte-compared. Enumeration is complete: monomial sweeps of
every degree up to 5 over all six extremal laws, and pushforward equalities
of complete weighted configuration dictionaries for all four group actions.

## Field 3. Carrier or data

No external data, no measurement, no fit. Complete finite enumeration: `A`
on 3125 configurations at weight 1/3125, each `B_m` on 160 configurations at
weight 1/160, `Bmix` on 640 at weight 1/640. Monomial counts, frozen: 286 of
degree at most 3, 715 of degree exactly 4, 2002 of degree exactly 5.

## Field 4. Systematics

```text
S1  Fourier convention: S(k) = sum_r C_{r,0} z^{-k r} and nothing else.
S2  Composition order: D_u = gamma_u rho_u; the reverse composition is
    claimed equal and is gated, not assumed.
S3  sigma_u is the field automorphism of Q(zeta_5), applied only on the
    algebraic configuration space of signed fifth roots of unity. It
    commutes with complex conjugation because conjugation is sigma_4 and the
    Galois group is abelian. No archimedean continuity of sigma_u is claimed
    and none is used; on this configuration space it preserves the modulus
    because every value is a signed root of unity.
S4  Index arithmetic in Z/5. Peak of B_m at k = 2m; inverse map m = 3 k_0.
S5  Scale frozen at a = 1; general a enters only in the algebraic P7
    corollary. Mixtures: only Bmix is gated.
S6  Monomial sweeps run over the six extremal laws; Bmix enters only the
    spectrum and action gates, since its moments follow by linearity.
S7  The universal quantifiers of P1 to P7 are carried by the written proofs
    below; the verifier audits them at complete finite scope and is not
    itself the source of a computed status.
```

## Field 5. Failure threshold

Exact and binary. Any one fires and the probe is recorded F and folded as a
first-class negative result:

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
F7  disagreement with the lane breaker on any shared quantity, or any
    pinned-bundle, transcript or architecture mismatch without an exact
    mathematical negation: integrity STOP, not a scientific falsifier.
F8  any float in the verifier or in any assertion: integrity STOP.
```

No threshold exists that could be moved: every gate is an exact equality
over `Q(zeta_5)`, an exact set equality, or an exact measure equality.

## Field 6. Action layer

`L1`, state, and only `L1`. The map `v -> w = v^2` is a pure `L1` algebraic
map of states and `S_w` is the power spectrum of the squared readout; it is
not a tensor spectrum and it is not `r_T(k)`. The ingredient `gamma_u` is an
algebraic operation on state values inside `L1`; it identifies nothing
physical and lifts nothing. The moment `w` is identified with a physical
tensor field, that is a layer lift needing its own named and typed gate,
which this probe does not supply. No gate is created; `canon/GATES.tsv` is
untouched.

## Proofs

These carry the universal quantifiers; the verifier audits them at complete
finite scope.

### Lemma 0, closed forms

Under `A`, site independence and orthogonality of the characters of `Z/5`
give `E_A[M] = prod_x [n_x = 0 mod 5]`. Under `B_m`,
`M = z^{t_0 S} z^{m W} prod_x eps_x^{p_x + q_x}`; averaging over `t_0` gives
the factor `[S = 0 mod 5]`, averaging over the signs gives
`prod_x [p_x + q_x even]`, and the survivor is `z^{m W}`.

### P1

Let `d <= 3`. If some `p_x + q_x` is odd, then `E_{B_m} = 0` for every `m`;
and `E_A = 1` would force `n_x = 0 mod 5` at every site, which with
`|n_x| <= d <= 3 < 5` forces `n_x = 0` and hence every parity even, a
contradiction, so `E_A = 0` too. If every parity is even, `d` is 0 or 2. At
`d = 0` all laws give 1. At `d = 2` one site carries `(1,1)`, `(2,0)` or
`(0,2)`. For `(1,1)`: `n = 0` everywhere, `S = 0`, `W = 0`, so `E_A = 1` and
`E_{B_m} = z^0 = 1` for every `m`. For `(2,0)` and `(0,2)`: `E_A = 0`, and
`S = 2` or `-2`, not `0 mod 5`, so `E_{B_m} = 0`. Equal in every case, for
every `m`, hence for all fifteen pairs; linearity extends this to every
polynomial of degree at most 3. QED

### P2 and P3

At `d = 4`, if `E_A = 1` then `|n_x| <= 4 < 5` forces `n_x = 0` everywhere,
hence every parity even, `S = 0`, `W = 0`, hence `E_{B_m} = 1` for every
`m`: wherever `A` reads 1, all six read 1. A separator involving `A` has
`E_A = 0` and needs the `B` survivor: every parity even, `S = 0 mod 5`, not
all `n_x` zero. Degree 4 with even site parities is one site of weight 4 or
two sites of weight 2. One site: `(4,0)`, `(3,1)`, `(2,2)`, `(1,3)`,
`(0,4)` give `S = 4, 2, 0, -2, -4`; only `(2,2)` survives and it has
`n = 0`. Two sites `x != y`: nets in `{+2, 0, -2}` with `|S| <= 4`, so
`S = 0` forces the pair `(+2, -2)`, exactly `v_x^2 conj(v_y)^2`, the twenty.
For a pair `B_m, B_{m'}` with `m != m'`, a separator needs the survivor and
`(m - m') W != 0 mod 5`, that is `W != 0 mod 5`; among degree-4 survivors
the `n = 0` cases have `W = 0` and the twenty have `W = 2(x - y)`, a product
of units, nonzero. So every one of the fifteen pairs separates on exactly
the same twenty monomials, with values `E_A = 0` and
`E_{B_m} = z^{2 m (x - y)}`; on the diagonal every law reads 1. QED

### P4

Under `B_m`, `eps_x^2 = 1`, so `w_x = z^{2 t_0 + 2 m x}` and
`C^w_{xy} = z^{2 m (x - y)}`, hence
`S_w(k) = sum_r z^{(2m - k) r} = 5 delta_{k, 2m mod 5}`. Under `A`,
`t -> 2t` is a bijection of `Z/5`, so `w` is again iid uniform on the fifth
roots and `S_w = 1`. `Bmix` averages the four spectra with `m = 1, 2, 3, 4`;
since `2m` then ranges over `{2, 4, 1, 3}`, the average is
`(5/4)(1 - delta_{k,0})`. For `Pi_w` the relevant monomials have `S = 4`,
not `0 mod 5`, under every `B_m`, and a nonzero net under `A`, so
`Pi_w = 0` throughout. QED

### P5

`(rho_u v)_x = v_{u^{-1} x} = eps_{u^{-1} x} z^{t_0 + m u^{-1} x}`: an
affine exponent with slope `m u^{-1}` and a relabeled iid sign field, so
`rho_u B_m = B_{u^{-1} m}`. `(gamma_u v)_x = sigma_u(eps_x z^{t_0 + m x}) =
eps_x z^{u t_0 + u m x}`: slope `u m` and `u t_0` uniform, so
`gamma_u B_m = B_{u m}`. Composing, `(D_u v)_x = sigma_u(v_{u^{-1} x}) =
eps_{u^{-1} x} z^{u t_0 + m x}`: the slope is exactly `m` again, so
`D_u B_m = B_m` for every `u` and every `m`. `A` is fixed by all three
because a relabeling of an iid field and the bijection `t -> u t` preserve
its law, and `Bmix` is fixed because both single actions permute
`{B_1, ..., B_4}`. The index is recoverable from any single configuration of
`B_m` as `e_1 - e_0 = m`, so the five laws are pairwise distinct and the
orbit maps are exact. The operators commute because `gamma` acts pointwise
on values and `rho` permutes sites; the verifier checks both composition
orders on every supported configuration. `S_w` of `B_m` peaks at `2m` by P4,
and `2 * 3 = 6 = 1 mod 5`, so the member with peak `k_0` is
`B_{3 k_0 mod 5}`. Together with P1 this gives the peak-placement clause of
P5. QED

### P6

An odd total degree forces some site parity odd, so `E_{B_m} = 0` for every
`m`; hence no two `B` laws separate at any odd degree, and any separator
from `A` at `d = 5` must have `E_A = 1`: every `n_x = 0 mod 5` with
`sum (p_x + q_x) = 5`. Either some `|n_x| = 5`, forcing `p_x + q_x >= 5 = d`,
so the monomial is `v_x^5` or `conj(v_x)^5`; or every `n_x = 0`, forcing an
even degree, a contradiction. The ten fifth powers have
`E_A[v_x^5] = E[z^{5 t}] = 1` and `E_{B_m}[v_x^5] = E[eps_x] z^{5(t_0 + m x)}
= 0`. QED

### P7

Every law of the six has `|v_x|^2 = 1` pointwise, so `E[|v_x|^4] = 1`; with
`C_{xx} = 1` and `P_{xx} = 0` the fourth cumulant is
`K_{xx} = 1 - 0 - 2 = -1`. In general, `|v_x|^2 = a^2` almost surely makes
`|v_x|^2` the constant `a^2`, so `E[|v_x|^4] = a^4`, while the Isserlis
closure for a mean-zero Gaussian field with `P_{xx} = 0` requires `2 a^4`;
equality would force `a = 0`. QED

## Consequence, stated inside the scope

Second-order and degree-3 data leave the squared-readout spectrum free
across a full `Z/5` index and its mixtures; the freedom survives the
diagonal four-fold symmetry; the free datum is read exactly by the twenty
fourth moments; and a Gaussian boundary is unavailable while the pointwise
modulus is held fixed. Whatever the parent eventually freezes, it must
freeze fourth-moment data, the complete state, or an explicit non-Gaussian
closure rule. The parent stays `[O]`.

## Freeze

The preregistration commit and the SHA-256 of this file and of `verify.py`
are recorded in `RUN.md` and in the claim issue at the pin. The pin precedes
the local formal leg. No amendment, no rebase, no squash, no force-push, no
reuse, no renaming.

Commit identity: `A. M. Thorn <thorn@twistj.com>`.
