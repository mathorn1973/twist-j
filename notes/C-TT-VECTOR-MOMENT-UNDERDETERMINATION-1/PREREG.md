# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 preregistration

Incubation candidate. No authority. This document promotes nothing. Its only
output on success is a promotion proposal for a public child probe.

Candidate id: `C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1`
Line targeted on promotion: `mathorn1973/twist-j`, `main`, as a child probe
`P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1`.
Parent: `TT-VECTOR-STATE-NORMALIZATION` [O]. The parent is not touched, not
closed, and not weakened by this candidate. It remains O / STOP.

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
CLAIM_ISSUE:    none. Incubation only. No branch, no public pin, no fold.
```

Currency gate run before this freeze against a freshly cloned public `main`:
`main` equals the base commit above; peeled `canon-v50` resolves to
`6b40d54831d9204a5bee9277177b4de1dae8b529` and is an ancestor of `main`; the
declared content commit is an ancestor of `main`; `canon/SHA256SUMS` is 5 of 5
OK; `canon/CANON.md` is 240724 bytes with the declared SHA-256. No probe
directory, and no registry identifier, matches this candidate.

Read at the same head and binding this pin:

```text
canon/NORMATIVE.tsv  TT-SQUARING-DECODER            D  layer NOT_APPLICABLE  gate_ids empty
canon/NORMATIVE.tsv  POL-READ                       D  layer NOT_APPLICABLE  gate_ids empty
canon/NORMATIVE.tsv  TT-VECTOR-STATE-NORMALIZATION  O  layer NOT_APPLICABLE  gate_ids empty
canon/GATES.tsv      no gate owns this normalization; 10 gate rows, none matching
```

Consequence, frozen here: the public ledger does not type the layers of the
vector doublet or of the physical tensor field. This candidate therefore makes
no layer identification. See field 6.

## Field 1. Equation

Carrier `X = Z/5`, sites `x` in `Z/5`. Scale frozen at `a = 1`; general
`a` in `Q_{>0}` enters only as the stated algebraic corollary, not as a
computed case. Coefficient field `Q(zeta_5)`, basis `{1, z, z^2, z^3}`,
reduction `z^4 = -(1 + z + z^2 + z^3)`.

Two laws on `C^X`, each supported on finitely many configurations:

```text
A    : v_x = z^{t_x},            (t_x) iid uniform on Z/5
B_0  : v_x = z^{t_0} eps_x,      t_0 uniform on Z/5, independent of
                                 (eps_x) iid uniform on {+1, -1}
```

Control family, for `m` in `Z/5`:

```text
B_m  : v_x = z^{t_0} eps_x z^{m x}
Bmix : uniform mixture of B_1, B_2, B_3, B_4 with weight 1/4 each
```

Group actions, written as formulas and not by name. Translation
`(tau_c v)_x = v_{x - c}` for `c` in `Z/5`. Spatial four-fold action
`(rho_u v)_x = v_{u^{-1} x}` for `u` in `(Z/5)^*`, a cyclic group of order 4.
No Galois action on coefficients is applied, jointly or otherwise. `rho` acts
on sites only.

Second-order data:

```text
mean_x  = E[v_x]
C_{xy}  = E[v_x conj(v_y)]
P_{xy}  = E[v_x v_y]
S_v(k)  = sum_{r in Z/5} C_{r,0} z^{-k r}
Pi_v(k) = sum_{r in Z/5} P_{r,0} z^{-k r}
```

Squared image, a pure algebraic map of states with no physical identification:

```text
w_x     = v_x^2
C^w_{xy}= E[w_x conj(w_y)]
S_w(k)  = sum_{r in Z/5} C^w_{r,0} z^{-k r}
Pi_w(k) = sum_{r in Z/5} E[w_r w_0] z^{-k r}
```

Fourth cumulant of the squared image at zero mean of `w`:

```text
K_{xy} = E[v_x^2 conj(v_y)^2] - P_{xx} conj(P_{yy}) - 2 C_{xy}^2
```

### Statement S1, fourth-moment separation

`A` and `B_0` are both `tau`-invariant and both `rho`-invariant, both satisfy
`|v_x| = 1` pointwise almost surely, and:

```text
(i)   mean_x = 0, C_{xy} = delta_{xy}, P_{xy} = 0 under both, hence
      S_v(k) = 1 and Pi_v(k) = 0 for all k under both.
(ii)  every monomial prod_x v_x^{p_x} conj(v_x)^{q_x} of total degree
      sum_x (p_x + q_x) <= 3 has equal expectation under A and under B_0.
      Hence every polynomial functional of degree <= 3, in particular every
      quadratic Q(v, conj(v)), has equal expectation under A and B_0.
(iii) C^w_{xy} = delta_{xy} under A and C^w_{xy} = 1 for all x, y under B_0,
      hence S_w(k) = 1 for all k under A and S_w(k) = 5 delta_{k,0} under B_0,
      while Pi_w(k) = 0 for all k under both.
(iv)  the minimal total degree at which A and B_0 separate is exactly 4, and
      at degree 4 the separating monomials are exactly the 20 monomials
      v_x^2 conj(v_y)^2 with x != y, each with expectation 0 under A and 1
      under B_0.
```

Sharp prediction registered here and falsifiable: the degree-4 separator set
has cardinality exactly 20 and contains no monomial of any other shape.

### Statement S2, fixed-modulus Wick no-go

If a law on `C^X` satisfies `E[v_x] = 0`, `P_{xx} = 0` and `|v_x|^2 = a^2`
almost surely with `a > 0`, then `E[|v_x|^4] = a^4`, while the Wick / Isserlis
closure for a mean-zero Gaussian field requires
`E[v_x^2 conj(v_x)^2] = P_{xx} conj(P_{xx}) + 2 C_{xx}^2 = 2 a^4`. Since
`a > 0` these differ, so no deterministic-modulus law is Gaussian, and the
fourth cumulant is `K_{xx} = -a^4` exactly. Verified exactly at `a = 1` for
both `A` and `B_0`.

### Statement S3, four-fold trichotomy, control

`rho_u B_m = B_{u^{-1} m}` as measures. Hence `B_0` is `rho`-invariant with
`S_w` peak at `k = 0`; for `m != 0` the law `B_m` has `S_w(k) = 5 delta_{k, 2m}`
but is not `rho`-invariant; `Bmix` is `rho`-invariant with
`S_w(k) = (5/4)(1 - delta_{k,0})`. Arbitrary peak placement at fixed `m` and
spatial `rho`-invariance cannot hold together.

### What is not claimed

No closure of `TT-VECTOR-STATE-NORMALIZATION`. No `r_T(k)`. No action, no
Stage-B pullback, no scalar power spectrum `P_S(k)`, no identification of `w`
with a physical tensor field, no tensor spectrum, no helicity, no detector
response, no observable, no cosmology. No statement about `J`, `p = 5` as
physics, the decoder, Born, measure, observer, force, spacetime, the Plenum,
SI units, or layers L2 to L6.

## Field 2. Code

`verify.py`, Python standard library only, no third-party import, no network,
no file read, deterministic, under 120 seconds, run from the working directory
with `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Exact arithmetic only: `fractions.Fraction` coefficients over the cyclotomic
basis above, and integer exponent arithmetic in `Z/5`. No float literal, no
float operation, and no float in any assertion, anywhere in the file. Exit 0
on all gates PASS, exit 1 otherwise. Stdout is the sole result surface and is
byte compared.

Independent breaker `breaker.py` on a second code path: closed-form character
sums, not enumeration. For `A` the expectation of
`prod_x v_x^{p_x} conj(v_x)^{q_x}` equals the indicator that
`p_x - q_x = 0 mod 5` for every `x`. For `B_0` it equals the indicator that
`sum_x (p_x - q_x) = 0 mod 5` and `p_x + q_x` is even for every `x`. The
breaker sweeps all monomials of total degree at most 4, computes both
expectations by these formulas, cross-checks against enumeration, and reports
the full separator set at each degree. This is an attempt to break S1(iv), not
a rerun of the verifier path.

## Field 3. Carrier or data

No external data, no measurement, no fit. The carrier is the finite
configuration space of the two laws, enumerated in full: 3125 configurations
for `A` at weight 1/3125 each, 160 configurations for `B_0` at weight 1/160
each, 160 for each `B_m`, 640 for `Bmix` at weight 1/640 each. Every stated
expectation is a finite exact sum, not a sample.

## Field 4. Systematics

Frozen before execution, since each is a place where a convention could be
slid after the fact:

```text
S1  Fourier sign convention is S(k) = sum_r C_{r,0} z^{-k r} and nothing else.
S2  rho acts on sites only. No Galois action on coefficients is applied.
    Under a diagonal site-and-Galois action the trichotomy of S3 changes;
    that variant is out of scope here.
S3  |v_x| = 1 pointwise almost surely is the deterministic reading, not
    E[|v_x|^2] = 1. Both laws satisfy the deterministic form.
S4  Scale is frozen at a = 1. Configurations then lie in Z[zeta_5] and
    expectations in Q(zeta_5). General a enters as an algebraic corollary
    by homogeneity of degree 2 in C and degree 4 in K, never as a run.
S5  The falsifier for quadratic separation is stated on expectations of a
    quadratic polynomial, not on the distribution of a quadratic random
    variable. The distribution of Q(v) may and does differ between A and B_0.
S6  Cumulant convention is the zero-mean fourth joint cumulant written out
    in field 1; no other convention is admitted after the fact.
S7  Both laws are exhibited constructively. This is an existence statement.
    Its status derives from the written proof; the verifier audits it at
    complete finite scope and is not itself the source of a computed status.
```

## Field 5. Failure threshold

Exact and binary. Any one of the following fires and the candidate is recorded
F, archived, and not repaired by moving a threshold:

```text
F1  any monomial in (v, conj(v)) of total degree <= 3 whose expectation
    differs between A and B_0. Kills S1(ii) and the whole point.
F2  any tabulated moment differs from its stated value: mean 0, C = delta,
    P = 0, S_v = 1, Pi_v = 0 under both; S_w = 1 under A;
    S_w = 5 delta_{k,0} under B_0; Pi_w = 0 under both.
F3  either A or B_0 fails tau-invariance or rho-invariance as measures.
F4  E[|v_x|^4] equals the Wick value 2 at a = 1 under either law, or
    K_{xx} != -1. Kills S2.
F5  the degree-4 separator set is not exactly the 20 monomials
    v_x^2 conj(v_y)^2 with x != y. Kills the sharp form of S1(iv).
F6  Bmix fails rho-invariance, or some B_m with m != 0 is rho-invariant, or
    S_w for B_m is not 5 delta_{k, 2m}, or S_w for Bmix is not
    (5/4)(1 - delta_{k,0}). Kills S3.
F7  verifier and breaker disagree on any shared quantity. Integrity STOP,
    not a scientific falsifier.
F8  any float appears in the verifier or in any assertion. Integrity STOP.
```

There is no partial credit and no threshold to move: every gate is an exact
equality over `Q(zeta_5)` or an exact set equality.

## Field 6. Action layer

`L1`, state, and only `L1`.

The map `v -> w = v^2` is declared inside this candidate to be a pure `L1`
algebraic map of states. `S_w` is named the power spectrum of the squared
image. It is not called a tensor spectrum, it is not `r_T(k)`, and `w` is not
identified with any physical tensor field. Under that reading no layer lift
occurs and no gate is required or created. `canon/GATES.tsv` is not touched.

The moment `w` is identified with a physical tensor field, or the moment an
`r_T(k)` is asked of it, this candidate stops: that is a layer lift, it needs
its own named and typed gate, and this document does not supply one. The
public ledger currently types the parent and both relevant dictionary rows as
`NOT_APPLICABLE`, so the two endpoint layers are not even fixed yet. Naming
them is the parent's work, not this child's.

## Freeze

Nothing was computed, enumerated or executed before this file was written.
The verifier file is written next and hashed together with this file; both
hashes are recorded before first execution, and the first execution is the one
reported. No amendment, no second freeze, no renaming.

Commit identity for any later public carry: `A. M. Thorn <thorn@twistj.com>`.
