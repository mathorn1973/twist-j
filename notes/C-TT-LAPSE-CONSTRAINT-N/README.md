# C-TT-LAPSE-CONSTRAINT-N: lapse and Hamiltonian constraint on the planar TT carrier

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-D (construction and its declared choices)
                        candidate-T (the exact consequences proved and verified below)
ACTION LAYER:           L1 rational arrays; declared L2 role (lapse, spatial metric); no gate
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        PREREG.md, frozen before execution,
                        sha256 e0bb69848b442974ac6b69d32f1794547bdd982696bbb947e06077714e8f0af8
BASIS:                  Public Canon v81, main c6d90f148f6ea7295cb42c629b6cf735060ebfd4
OWNER ROWS (unchanged): TT-VECTOR-STATE-NORMALIZATION [O], FRW-INHOM [O], TT-SOURCE [O]
CANON / REGISTRY CHANGE: NONE
PROMOTION:              NONE
```

This note supplies one constrained geometric construction and decides the
owner's six falsifiers for it at an explicitly bounded scope. It does not
supply a cosmological scalar power, a numerical `r_T(k)`, a physical
amplitude, or a Regge-Wheeler coefficient. A fired falsifier below is
archived as a result, not repaired.

## 1. Why this candidate exists

The predecessor `C-K1-DYNAMIC-METRIC-N` used the positive-definite pairing
`B_+(H,K) = tr(HK) + tr H tr K` as the common kinetic form of all six spatial
metric components. Its independent break-check found two structural facts:
the homogeneous trace mode then carries a positive kinetic sign, opposite to
`FRW-CANONICAL-FORM [T]`, and the trace is a radiative mode locked pointwise
to the TT component by `h_+ = -12 s`, so it cannot serve as a scalar
denominator. The owner recorded the predecessor as F for the `r_T` route and
took two program decisions: (A) `h = v^2` remains the registered TT decoder,
the square is not moved to the source side; (B) the scalar sector is a
constrained sector fixed by a lapse and a Hamiltonian constraint, not the
dynamical trace of the same radiative field.

The five conditions C1 to C5 and the six falsifiers F1 to F6 are frozen in
`PREREG.md`. This note builds the smallest construction that can be judged
against them.

## 2. The construction

Fields on the planar carrier `Z/5` (the K1 slot axis) at each counter `n`:
a lapse `nu = 1 + n` and a symmetric spatial metric `gamma = I + H`, shift
zero. Discrete time difference `Delta f_n = f_(n+1) - f_n`. Spatial operator:
the exact planar reduction of the public D3 stencil,

```text
(L f)_r = [188 f_r - 29 (f_(r-1) + f_(r+1)) - 65 (f_(r-2) + f_(r+2))] / 324,
```

with the planar rule fixed once: every product of two first differences along
the axis is the stencil form `<f, L g>`, every second difference is `-L`.

The gravitational action is the discrete linearized ADM action with the
standard indefinite DeWitt kinetic form and the prefactor `1/(2 lambda)`,
`lambda = 216 pi` from `FRW-CANONICAL-FORM [T]`:

```text
S_g = sum_n sum_r (1/(2 lambda)) [ (1/4)( tr (Delta H)^2 - (tr Delta H)^2 )
                                   + G_2(H) + n R_1(H) ],
G_2 = (1/2) d_i h_ij d_k h_kj - (1/2) d_i h_ij d_j h + (1/4) (d h)^2 - (1/4) d_k h_ij d_k h_ij,
R_1 = d_i d_j h_ij - d^2 h,           h = tr H,
```

`G_2` being the quadratic part of `sqrt(gamma) R(gamma)` (verified in the
standard way by the conformally flat check, `h_ij = 2 psi delta_ij` gives
`2 |grad psi|^2`), and `R_1` its linear part. The nonlinear homogeneous
sector is declared to be `FRW-CANONICAL-FORM` itself; only the linearized
coefficients are checked here (C1 at linearized scope).

Two readings of the fixed K1 are frozen:

```text
Source reading   e = (a b_r(t), 0, 0) is a prescribed stress source with
                 S_m = - sum (1 + n) sqrt(det gamma) eps_gamma(e),
                 eps_gamma(e) = (1/2) e^T gamma^-1 e, covector fixed under
                 variation. Linear terms: -(n/2)|e|^2 + (1/2) tr(H S(e)),
                 S(e) = e e^T - (|e|^2/2) I. This is the predecessor's coupling
                 with the lapse added. The owner already confined this reading
                 to TT-SOURCE; it is kept only to decide whether constrained
                 dynamics admits it at all.
Decoder reading  h_+(r,t) = v^2 = iota_t(r) = a^2 b_r(t)^2 is the TT strain
                 itself (TT-SQUARING-DECODER [D], POL-READ [D]); no matter
                 source; the scalar sector is sourced at second order by the
                 TT field through the Hamiltonian constraint.
```

Declared choices of this candidate, all visible:

| Choice | Position |
|---|---|
| Planar carrier `Z/5` with the planar rule | The three-dimensional carrier needs a discrete gradient to write `d_i d_j h_ij`; none is introduced. |
| Indefinite DeWitt form, prefactor `1/(2 lambda)`, `lambda = 216 pi` | Forced by C1: the same prefactor multiplies the homogeneous FRW action. No relative coefficient is left free. |
| Nonlinear homogeneous sector = `FRW-CANONICAL-FORM` | Declared; discrete-time exactness of `e^(3 Phi)` against `Delta` is not claimed. |
| Second-order lattice density for `R_2(h)` in the decoder reading | Two transcriptions are declared and compared: (i) the stencil energy density, (ii) the literal `(3/2) h'^2 + 2 h h''`. They have the same zero mode and different nonzero modes. (i) is the working choice. |
| `k != 0` equations are the flat static linearization | FRW-background corrections to them are not derived. |

## 3. Sector decomposition [candidate-T]

Write `h_+ = (h_11 - h_22)/2`, `h_x = h_12` (TT), `tau = (h_11 + h_22)/2`
(transverse trace), `ell = h_33` (longitudinal), `h_13, h_23` (vector).
With only the axis-3 difference nonzero, exact polynomial identities give

```text
kinetic   (1/4)[ tr (Delta H)^2 - (tr Delta H)^2 ]
        = (1/2)[ (Delta h_+)^2 + (Delta h_x)^2 + (Delta h_13)^2 + (Delta h_23)^2 - (Delta tau)^2 ]
          - Delta tau Delta ell,
gradient  G_2 = (1/2) <tau, L tau> - (1/2) <h_+, L h_+> - (1/2) <h_x, L h_x>,
lapse     R_1 = 2 L tau.
```

`ell` and the vector components have no gradient energy (they are the
gauge directions `x_3 -> x_3 + xi_3`, `x_a -> x_a + xi_a(x_3)`); the lapse
multiplies only `tau`; the TT pair carries the wave form with the sign of a
physical field; `tau` carries the opposite gradient sign and a kinetic term
only through its coupling to `ell`. This is the conformal-factor structure of
the Einstein action, now on the lattice, and it is what the positive-definite
predecessor erased.

## 4. Equations [candidate-T]

Exact variation of the explicit discrete action (checked by the verifier at
a random rational configuration and two values of `lambda`; the identities
are linear in `1/lambda`, so two values decide them):

```text
(a) lapse        (1/lambda) L tau = iota/2                        [source reading]
(b) longitudinal (1/(2 lambda)) Delta^2 tau = iota/4
(c) trace        Delta^2 tau + Delta^2 ell + L tau + 2 L n = 0
(d) TT           Delta^2 h_+ + L h_+ = lambda iota,   Delta^2 h_x + L h_x = 0
(e) vector       Delta^2 h_13 = Delta^2 h_23 = 0
```

The lapse enters the action linearly: it has no `n^2` and no `Delta n`
term, and (a) is algebraic in the fields. F2 does not fire.

With `ell` gauge-fixed to zero, (a) fixes `tau` instantaneously from the
source, (c) fixes `n` (on nonzero modes, whenever (a) and (b) both hold,
`n = -tau`, the weak-field relation between lapse and spatial conformal
factor), and (b) is the consistency condition. No free scalar mode
survives: F3 does not fire. The TT pair is the only radiative sector: C3
holds.

The coefficient census: every coefficient of (a) to (e) is a rational
multiple of `lambda^0` or `lambda^(-1)` with `lambda = 216 pi` public, plus
K1's own amplitude `a`. The relative source-to-geometry coefficient that the
predecessor had to set by hand (`rho = 1`) is here `lambda`, fixed by C1.
F5 does not fire.

## 5. Homogeneous limit [candidate-T at linearized scope]

For `H = 2 Phi I` constant in space (`tau = ell = 2 Phi`, TT zero, source
zero) the action equals, per site,

```text
-(3/lambda) (Delta Phi)^2,
```

exactly the kinetic term of `FRW-CANONICAL-FORM`,
`S = V_0 sum nu e^(3 Phi) [ -(3/lambda)(Delta Phi / nu)^2 - rho(Phi) ]`, at
`nu = 1`, `e^(3 Phi) -> 1`, with the negative sign and the same `lambda`.
The lapse coupling at zero wave number is `-n rho` with `rho = |e|^2/2`,
matching the FRW matter term; the `(3/lambda) n (Delta Phi)^2` term of FRW
is cubic and outside the quadratic action. The covector matter has
`rho(Phi) = rho_0 e^(-2 Phi)` in the homogeneous limit, an FRW-form matter
term. F1 does not fire at this scope. The predecessor's pairing gives
`+24 (Delta Phi)^2` per site at the same place: opposite sign, as recorded.

## 6. The zero mode: the flat static carrier cannot host K1 [candidate-T]

On the compact carrier `L` annihilates constants, so the `k = 0` component
of the lapse equation (a) reads `0 = iota_hat_0 / 2`. For every K1 word and
both cuts, `sum_r iota_t(r) = a^2 > 0`. Hence the Hamiltonian constraint has
no solution on a static flat carrier for any K1 word in the source reading.
In the decoder reading the same happens with the second-order source
`sigma`: its zero mode is strictly positive for every word,

```text
sum_r sigma = 53/864  (u_0 = u_1),   161/864  (|u_0 - u_1| = 1),   269/864  (|u_0 - u_1| = 2),
```

at unit `a^2`, identical for the two lattice transcriptions (i) and (ii),
which differ only on nonzero modes.

The `k = 0` component of the Hamiltonian constraint is the Friedmann
equation `3 H^2 = lambda rho` linearized at zero expansion; the obstruction
says exactly that the K1 energy must be carried by a dynamical homogeneous
sector. C1 is therefore not a limit to be checked afterwards; it is forced
by C2 on a compact carrier. This is the precise sense in which the scalar
denominator of the TT program is bounded by `FRW-INHOM`: the zero mode of any
constrained scalar sector on this carrier is the homogeneous FRW sector. The
nonzero modes below are stated on the flat static background conditionally.

## 7. Source reading: conservation, and F6 fires

Equations (a) and (b) together imply, on every nonzero mode,

```text
Delta^2 iota = L iota,
```

the linearized conservation law of the prescribed stress (energy density
`iota/2`, longitudinal stress `-iota/2`; `partial_t^2 T_00 = partial_3^2 T_33`).
A prescribed source that is not conserved is refused by any dynamics with a
Bianchi identity; that is what (b) enforces. The fixed K1 word law supplies
two cuts. The continuation the law demands at either cut,

```text
iota_(-1) = 2 iota_0 - iota_1 + L iota_0,      iota_2 = 2 iota_1 - iota_0 + L iota_1,
```

is not a K1 intensity (two cyclically adjacent sites at `a^2/2`) for any of
the ten words, twenty of twenty cases; for word `0010`,
`iota_(-1) = (-209/324, 161/216, 269/216, -47/324, -65/324)`. The four
words with `iota_0 = iota_1` fail as well, because a static axis-dependent
longitudinal stress has `partial_3 T_33 != 0`. Together with the zero mode of
section 6, the fixed K1 cannot be the prescribed stress source of this
constrained dynamics without being changed: **F6 fires for the source
reading.** This closes, at candidate level, the route the owner had already
confined to `TT-SOURCE`: as a child of `TT-SOURCE` the dynamic map remains a
conditional emission map, but it cannot be promoted to a constrained gravity
source without a conservation law for K1, which is the predecessor's own
backreaction debt.

## 8. Decoder reading: the constrained scalar [candidate-T for the exact arrays]

With `h_+ = iota_t(r)` the TT strain and no matter, the Hamiltonian
constraint at second order reads `2 L tau = (K_ij K^ij - K^2)_2 - R_2(h_+)`.
With `K = (1/2) Delta h` and the transcription (i), `R_2 -> -(1/2) g(h)`,
where `g(h)(r) = (1/2) sum_k m_k (h(r) - h(r+k))^2` is the site density of the
stencil form (`sum_r g = <h, L h>`), this is

```text
L tau = sigma,     sigma = (1/4) [ (Delta h_+)^2 + g(h_+) ]  =  lambda eps_GW,
```

`lambda` cancels. The scalar sector is sourced by the discrete energy density
of the TT field; the same energy form the predecessor proved nonnegative. The
zero mode of `sigma` goes to the homogeneous sector (section 6); on the
nonzero modes

```text
tau = L^+ (sigma - mean sigma),
```

with `L^+` the pseudo-inverse of `L` on the mean-zero subspace, a rational
symmetric circulant (`L L^+ = I - J/5`, verified exactly in `Q(sqrt5)` and
found rational). At cut 0, unit `a^2`, indices `r = 0..4`, by class
`(u_0, u_1)` (the two words `0101, 1010` share `(0,0)`):

```text
(-1,-1)  ( 6951/1715360, -845/171536, 1499/857680, -845/171536, 6951/1715360)
(-1, 0)  (-77289/1715360, 47291/857680, -28957/857680, -34681/857680, 109983/1715360)
(-1, 1)  ( 25743/1715360, 5171/857680, 22559/857680, -65137/857680, 49071/1715360)
( 0,-1)  (-77289/1715360, 109983/1715360, -34681/857680, -28957/857680, 47291/857680)
( 0, 0)  ( 6951/1715360, 6951/1715360, -845/171536, 1499/857680, -845/171536)
( 0, 1)  ( 109983/1715360, -77289/1715360, 47291/857680, -28957/857680, -34681/857680)
( 1,-1)  ( 5171/857680, 25743/1715360, 49071/1715360, -65137/857680, 22559/857680)
( 1, 0)  ( 47291/857680, -77289/1715360, 109983/1715360, -34681/857680, -28957/857680)
( 1, 1)  (-845/171536, 6951/1715360, 6951/1715360, -845/171536, 1499/857680)
```

`1715360 = 32 . 53605 = 32 . 5 . 71 . 151`, the denominator of the nonzero-mode
inverse of `L`. The arrays are translation covariant under `u -> u + 1`, as
they must be. Under `a^2 -> c a^2` they scale by `c^2`: `tau = O(a^4)` while
`h_+ = O(a^2)`. `sigma` is quadratic in `h = v^2`, so the constrained scalar
consumes exactly the fourth-moment data of the doublet, the data that
`TT-VECTOR-MOMENT-UNDERDETERMINATION [T]` says a normalization must freeze
and that K1 supplies.

Under transcription (ii) the arrays differ for every word (same zero mode).
The fork is real and declared; it is the lattice residue of the missing
product rule (`sum_r [2 h L h - g(h)]` is not zero on the lattice).

**What this scalar is not.** `tau` is the transverse trace of the constrained
spatial metric on the flat static background, sourced by TT energy. It is
not a cosmological curvature perturbation, not a `P_S(k)`, and no ratio with
`h_+` is formed here. K1 is untouched: the strain beyond the two cuts, when
needed, is extended by the free TT equation (d) with zero source, which is
dynamics, not a change of K1. **F6 does not fire in the decoder reading.**

## 9. Spin structure (C4)

At the flat level the sectors are not propagated by one operator: TT pair
`Delta^2 + L` (hyperbolic), scalar `tau` by the elliptic constraint `L`,
lapse algebraic, longitudinal and vector without gradient energy (gauge).
F4 does not fire at this level. The registered coefficient `c = 1 - s^2`
(`-3` at `s = 2`) is a Regge-Wheeler coefficient on a mass background; it is
a cubic-order, background-dependent statement that a quadratic flat action
cannot exhibit. C4 is met only in the weak form (spin-dependent operators);
the strong form is not claimed and is listed open.

## 10. Verdicts and open items

```text
                      source reading (K1 as stress)   decoder reading (h = v^2)
F1 not FRW             no fire (linearized scope)      no fire (linearized scope)
F2 lapse propagates    no fire                         no fire
F3 trace mode left     no fire                         no fire
F4 spin blind          no fire (flat); RW open         no fire (flat); RW open
F5 new coefficient     no fire (lambda public)         no fire (lambda cancels)
F6 K1 must change      FIRES (zero mode, conservation) no fire
```

Open items, named so that the next step is narrow:

1. Discrete Bianchi identity at second order. In the decoder reading the
   longitudinal equation (b) at second order needs the cubic expansion of the
   ADM action in `H` and a lattice product rule. Not derived. It decides
   whether the lattice constrained theory is consistent at second order or
   whether `ell` must be frozen by a further declared choice.
2. Local density transcription (i) versus (ii). Same zero mode, different
   nonzero modes. A selection rule or a lattice curvature is needed.
3. The `k != 0` equations on the FRW background that section 6 forces.
   Not derived; the flat static forms are used conditionally.
4. Three-dimensional carrier: a discrete gradient compatible with `L`.
5. Regge-Wheeler coefficient `1 - s^2` on a mass background.

None of these is a hidden coefficient; each is a named construction.

## 11. Reproducibility

`verify.py` was frozen and run once; its first run failed one fixture, an
expected class count written as 8 where the joint law has 9 pairs
`(u_0, u_1)` (the check itself concerned the class structure, which held).
The failed output and the unchanged source are retained
(`RUN-verify-first.txt`). The successor `verify_fixture_corrected.py`
changes only that expected count, was frozen before execution, and passed
24 of 24 exact checks with empty stderr. Both verifiers were rerun from the
same frozen bytes on a second architecture (arm64, macOS, Python 3.13.13)
with byte-identical stdout. See `RESULT.md` for hashes and environments.
One author, one code path; a local two-architecture record, not the public
gate.
