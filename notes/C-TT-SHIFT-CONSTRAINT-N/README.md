# C-TT-SHIFT-CONSTRAINT-N: lapse, shift, exact gauge invariance and constraint propagation on the planar TT carrier

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-D (construction and declared choices)
                        candidate-T (the identities certified below, as operator or
                        polynomial identities)
ACTION LAYER:           L1 rational arrays; declared L2 role (lapse, shift, spatial metric); no gate
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        PREREG.md, frozen before execution,
                        sha256 d38e9fb3a272e0d8ed93cf83c744c920e91a7ca017cb8a471b760c5f1e013026
BASIS:                  Public Canon v81, main 4fe37d3539ce4513d51e71e90f78e3ae0a607ad1 (after #908)
PREDECESSORS:           C-K1-DYNAMIC-METRIC-N (owner F for r_T), C-TT-LAPSE-CONSTRAINT-N (#909)
OWNER ROWS (unchanged): TT-VECTOR-STATE-NORMALIZATION [O], FRW-INHOM [O], TT-SOURCE [O]
CANON / REGISTRY CHANGE: NONE
PROMOTION:              NONE
```

This note delivers the linear-order part of the owner's acceptance object
from the review of #909: one common variational system with lapse and shift,
exactly gauge invariant on the lattice, whose Noether identities are the
discrete Bianchi identities and give preservation of the Hamiltonian and
momentum constraints by the evolution equations. It states exactly what it
does not deliver: the second-order TT self-source, the FRW background for the
zero mode, the three-dimensional carrier, the Regge-Wheeler coefficient. No
owner condition C1 to C5 is claimed complete. No original O/H closes.

## 1. The construction

Planar carrier `Z/5` (the K1 slot axis). Fields: spatial metric perturbation
`h_ij` (six components) and lapse perturbation `n` on integer slices; shift
`N_i` (three components) on half-integer slices. `Delta f(n) = f(n+1) - f(n)`.
One antisymmetric first-difference operator `D` on `Z/5` (`D^T = -D`) and
the Laplacian `L := -D^2 = D^T D`. With only the axis-3 difference present,

```text
K_11 = Delta h_11/2,  K_22 = Delta h_22/2,  K_12 = Delta h_12/2,
K_13 = (Delta h_13 - D N_1)/2,  K_23 = (Delta h_23 - D N_2)/2,  K_33 = (Delta h_33 - 2 D N_3)/2,
K = K_11 + K_22 + K_33,   all on half-integer slices,

S = sum_n sum_r (1/(2 lambda)) [ K_ij K_ij - K^2 + G_2(h) + n R_1(h) ]
    + sum_n sum_r [ - n rho + N_i J_i + (1/2) h_ij S_ij ],                 (prescribed source, optional)

G_2 = (1/2)<D h_3j, D h_3j> - (1/2)<D h_33, D h> + (1/4)<D h, D h> - (1/4)<D h_ij, D h_ij>,
R_1 = D D h_33 - D D h = 2 L tau,      tau = (h_11 + h_22)/2,     lambda = 216 pi.
```

Gauge transformation, parameters `xi_0` on half-integer slices and
`xi_1, xi_2, xi_3` on integer slices:

```text
delta h_13 = D xi_1,  delta h_23 = D xi_2,  delta h_33 = 2 D xi_3,  other h_ij unchanged,
delta N_i  = Delta xi_i + delta_(i,3) D xi_0,
delta n    = -( xi_0(n + 1/2) - xi_0(n - 1/2) ).
```

The time placement is not a convention chosen afterwards: with `K` and `N` on
half-integer slices and `n` on integer slices this is the unique staggering
under which the variation of `K_ij K_ij - K^2` cancels against the variation of
`n R_1` exactly (section 2). This answers the time-placement question of the
#909 review at linear order.

Two representations are used and cross-checked. (P1) A commutative symbol
algebra `Q[L, D, E, E^-1]/(D^2 + L)`, `E` the unit time shift, with transpose
`D -> -D`, `E -> E^-1`; every identity proved there holds for every
antisymmetric circulant `D` with `L = -D^2`, including irrational ones. (P3)
An explicit polynomial action on `Z/5 x Z/4` (time periodic) with the rational
centered difference `D_c f(r) = (f(r+1) - f(r-1))/2`, `L_c = -D_c^2`, in which
the same statements are polynomial identities in all 200 field and 80 gauge
variables; its Euler-Lagrange polynomials agree with the P1 expressions
instantiated with `D_c` for all fields, slices and sites.

Declared choices:

| Choice | Position |
|---|---|
| Planar carrier, one axis difference `D` | Three-dimensional carrier not addressed. |
| `D` abstract in P1, `D_c` in P3 | The public stencil has no rational antisymmetric square root (section 7); which `D` the program adopts is an owner fork. |
| Linear order | No TT self-source; the second-order constraint of #909 is outside this candidate. |
| Flat static background | The `k = 0` sector is analysed exactly and not solved (section 6). |
| Prefactor `1/(2 lambda)` | As in #909; every identity below is homogeneous in it and does not depend on its value. |

## 2. Exact gauge invariance [candidate-T]

For a quadratic action `S(phi + G xi) - S(phi) = <grad S(phi), G xi> + S(G xi)`.
Both parts vanish identically:

- Linear part: the four Noether combinations `sum_f G_f,mu^T EL_f` are the
  zero operator on every field (P1, every `D`).
- Quadratic part: `S(G xi) = 0`, i.e. `C_(mu nu) + C_(nu mu)^T = 0` for all
  parameter pairs (P2, every `D`).
- Explicit model: `S(phi + G xi) - S(phi) = 0` as a polynomial identity in
  all 280 variables (P3, `D_c`).

So the discrete action is invariant under the four-parameter linearized
diffeomorphism family, exactly, on the lattice, with no total-derivative
remainder.

## 3. Euler-Lagrange equations and the constraints [candidate-T]

With the gravitational factor `1/(2 lambda)` written as `1/lambda` on the
constraint expressions (the verifier prints them with the factor stripped):

```text
Hamiltonian   EL_n   = (1/lambda) L tau - rho
momentum 1,2  EL_N1  = (1/lambda) D K_13 + J_1,       EL_N2 = (1/lambda) D K_23 + J_2
momentum 3    EL_N3  = -(1/lambda) D Delta tau + J_3
evolution     EL_h11 = (1/lambda) [ -(1/2) nabla D N_3 + (1/4)(Delta^2 + L) h_22 + (1/4) Delta^2 h_33 + (1/2) L n ] + (1/2) S_11
              EL_h22 = the same with h_11 and h_22 exchanged, + (1/2) S_22
              EL_h33 = (1/(2 lambda)) Delta^2 tau + (1/2) S_33
              EL_h12 = -(1/(2 lambda)) (Delta^2 + L) h_12 + S_12
              EL_h13 = -(1/lambda) nabla K_13 + S_13,        EL_h23 = -(1/lambda) nabla K_23 + S_23
```

`Delta^2 = E^-1 - 2 + E` (centered second difference), `nabla = 1 - E^-1`;
the verifier prints the same expressions with the factor `1/(2 lambda)`
stripped. The diagonal kinetic terms cancel in `EL_h11`, the DeWitt
structure; the lapse enters linearly and its equation is the Hamiltonian
constraint; the three shift equations are the momentum constraints; the
longitudinal momentum constraint contains no shift, as in the continuum
(`d_3 tau_dot = -lambda J_3`).

## 4. Noether identities are the discrete Bianchi identities: constraint propagation [candidate-T]

The four identities, each the zero operator (P1):

```text
xi_0:  (E - 1) EL_n = D EL_N3
xi_1:  (E^-1 - 1) EL_N1 = D EL_h13
xi_2:  (E^-1 - 1) EL_N2 = D EL_h23
xi_3:  (E^-1 - 1) EL_N3 = 2 D EL_h33
```

Read as propagation: if the longitudinal momentum constraint holds on every
half slice, the Hamiltonian constraint expression is constant in time, so
initial data satisfying it satisfy it forever; if the evolution equations
for `h_13, h_23, h_33` hold, each momentum constraint expression is constant
in time. Constraints imposed on initial data are preserved by the evolution.
This is the exact discrete statement the #909 review asked for, at linear
order, with no continuum limit.

## 5. Conservation laws a prescribed source must satisfy [candidate-T]

With the source coupling of section 1 the Noether combinations no longer
vanish on the source fields; gauge invariance holds if and only if

```text
(1 - E) rho    = D J_3                    (continuity)
(E^-1 - 1) J_i = D S_i3,   i = 1, 2, 3    (momentum balance)
```

exactly, on the lattice. Consequences for the fixed K1:

- The covector stress model of the predecessors (`rho = iota/2`, `J = 0`,
  `S_33 = -iota/2`) violates the momentum law for every word and both cuts
  (`D iota != 0`, `D` invertible on nonzero modes, rank 4) and the continuity
  law for the six words with `iota_0 != iota_1`. This is the structural form
  of the #909 F6 finding for the source reading: it no longer depends on the
  tested fixed-shape continuation.
- The K1 intensities themselves admit a conserved completion: `J_3 =
  D^-1 (rho_0 - rho_1)` exists and is mean-zero (`sum iota` is constant), and
  `S_33` follows from the momentum law; for word `0010` and `D_c`,
  `J_3 = (1/10, -2/5, 1/10, 1/10, 1/10)`. The transverse stress
  `S_11, S_22, S_12`, the part that sources `h_+` and `h_x`, does not appear
  in any planar law and is unconstrained. FE does not fire: what must change
  is the longitudinal stress and the momentum density of the covector model,
  not the K1 words or windows.

## 6. Sector reduction, the witness, and the zero mode [candidate-T]

Witness of the #909 review, `h_13(n, r) = n f(r)`, `f` nonconstant, all
other perturbations zero, `N = 0`: every equation holds except the momentum
constraint `EL_N1 = (1/lambda) D K_13`, which fails (P7). With
`N_1 = D^-1 f` all equations hold: the witness is the pure-gauge configuration
generated by `xi_1 = n D^-1 f`. In the zero-shift gauge it is excluded. FC
does not fire.

In the gauge `N = 0`, `ell = 0`, vacuum, the constraints read `L tau = 0`,
`D Delta h_13 = 0`, `D Delta h_23 = 0`, `D Delta tau = 0`. Since `D` and `L`
have rank 4 on `Z/5` (kernel exactly the constants), on nonzero modes `tau =
0`, `Delta h_13 = Delta h_23 = 0`; the time-constant `h_13, h_23` are removed
by time-independent `xi_1, xi_2`. What remains is the TT pair with
`(Delta^2 + L) h = 0`, and TT-only data with `n = N = tau = ell = vector = 0`
satisfy every constraint and evolution equation exactly (P7). No non-TT
radiative sector survives on nonzero modes: FD does not fire at linear order.

Zero mode. `D` and `L` annihilate constants, so at `k = 0` the Hamiltonian
constraint reads `-rho_hat_0 = 0` and the momentum constraints are empty. For
every K1 word `sum_r iota = a^2 > 0`; there is no static flat solution with
the K1 energy. This candidate does not solve the homogeneous component; it
records exactly why the flat static background cannot carry it. The FRW
background construction, on which the `k = 0` constraint becomes the
Friedmann equation and the `k != 0` equations acquire background terms, is
the next candidate; the propagation structure of section 4 is what that
construction must reproduce.

## 7. The operator `D` and the public stencil [candidate-T, exact fact]

Everything above holds for any antisymmetric circulant `D` with `L = -D^2`.
Whether the public planar stencil `L` is such an `L` is decided exactly: for
`D = x (S - S^-1) + y (S^2 - S^-2)`,

```text
-D^2 = 2(x^2 + y^2) - (x^2 + 2xy)(S^2 + S^-2) - (y^2 - 2xy)(S + S^-1),
```

so `-D^2 = L_public` requires `x^2 + 2xy = 65/324`, `y^2 - 2xy = 29/324`,
i.e. `t = y/x` a root of `65 t^2 - 188 t - 29 = 0`, discriminant
`42884 = 4 . 71 . 151`, not a square. No rational antisymmetric first
difference on `Z/5` squares to the public stencil; the required `D` lives in
`Q(sqrt(10721))`, `10721 = 71 . 151 = 53605/5`, the primes already in the
denominators of the #909 arrays. The rational centered difference gives a
different Laplacian, `L_c = -D_c^2` with entries `1/2` at `0` and `-1/4` at
shifts `+-2`.

This is an owner fork, not decided here: (alpha) keep the public `L` for the
metric and TT sectors and accept an algebraic `D` in the shift and gauge
sector, where it never enters a physical readout; or (beta) adopt a rational
`D` and its `L_D` for the whole constrained system, which changes the
propagation operator of the TT sector away from the registered stencil.
The identities of sections 2 to 6 are the same in both.

## 8. What this candidate does not deliver

- Second order. The TT self-source of the decoder reading (the `sigma` of
  #909) needs the cubic lattice action with a lattice curvature. The linear
  structure fixes its time placement in advance: `K` lives on half slices,
  so the second-order Hamiltonian constraint at slice `n` will carry
  `K(n - 1/2) K(n + 1/2)`-type terms, not the same-slice `(Delta h)^2` of the
  transcriptions (i)/(ii). Those transcriptions remain undecided here.
- FRW background: the `k = 0` sector is obstructed, not solved (section 6).
- Three-dimensional carrier and the Regge-Wheeler coefficient `1 - s^2`.
- The physical meaning of `tau` and any scalar power: unchanged, open.

## 9. Scoped record

```text
FA  gauge invariance fails ........... no fire (P1, P2 every D; P3 polynomial identity)
FB  no constraint propagation ........ no fire (four Noether identities, section 4)
FC  witness not excluded / not gauge . no fire (P7)
FD  non-TT radiative sector survives . no fire at linear order, nonzero modes (P7, rank 4)
FE  K1 intensities admit no conserved completion ... no fire (P5); the covector stress does

Owner conditions:
C1  homogeneous limit ................ unchanged from #909 (quadratic coefficient only)
C2  lapse as constraint variable ..... met at linear order, now with the momentum constraints
C3  TT separation .................... met at linear order on nonzero modes, vacuum
C4  spin dependence .................. flat level only; RW coefficient open
C5  K1 unchanged ..................... windows unchanged; the covector stress is what fails

Closed original O/H: 0.   Status moves: 0.
```

## 10. Reproducibility

`PREREG.md` frozen 2026-09-08T17:04:48Z. `verify.py` frozen after a static
read and `py_compile` only, before any execution; 18 of 18 exact checks on
the first run, stderr empty, on x86_64 (Ubuntu 24.04, Python 3.11.15) and
rerun from the same bytes on arm64 (macOS 26.5, Python 3.13.13) with
byte-identical stdout. Hashes and environments in `RESULT.md`. One author,
one code path; a local two-architecture record, not the public gate.
