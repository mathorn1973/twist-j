# PREREG: C-TT-LAPSE-CONSTRAINT-N

```text
CANDIDATE:              C-TT-LAPSE-CONSTRAINT-N
STATUS:                 NON-CANONICAL INCUBATION, NO AUTHORITY
SCIENTIFIC STATUS:      candidate-D (construction), candidate-T (its consequences)
TARGET LINE:            public, mathorn1973/twist-j main
BASIS:                  Public Canon v81, main c6d90f148f6ea7295cb42c629b6cf735060ebfd4
OWNER ROWS (unchanged): TT-VECTOR-STATE-NORMALIZATION [O], FRW-INHOM [O], TT-SOURCE [O]
PREDECESSOR:            C-K1-DYNAMIC-METRIC-N (positive-definite pairing, owner verdict:
                        F as an r_T route, 2026-09-08)
ACTION LAYER:           L1 rational arrays with the declared L2 role of lapse and
                        spatial metric; no L1-to-L2 gate is registered or executed
FORMAL PUBLIC PROBE:    NONE
CANON / REGISTRY EDIT:  NONE
DATA OPENED BEFORE FREEZE: NONE (there are no data; the inputs are public
                        equations and the fixed K1 word law)
AUTHOR:                 A. M. Thorn, 2026-09-08
```

## 0. Owner conditions and falsifiers, frozen verbatim in meaning

The owner fixed five conditions and six falsifiers before any computation.
They are the decision rule of this candidate and are not modified below.

Conditions:

```text
C1  Homogeneous limit. With a spatially constant scalar sector and zero TT
    field the construction must return the public FRW-CANONICAL-FORM
    literally, including the negative kinetic sign of the trace. Not up to
    a convention, not after a sign change.
C2  Lapse is a constraint variable. The lapse nu receives no radiative
    kinetic term of its own; its variation gives a discrete Hamiltonian
    constraint H = 0.
C3  TT field genuinely separated. After the constraints are solved, a
    tracefree transverse sector survives, and no pure-trace radiative mode
    survives as an extra free copy (not six identical scalar oscillators).
C4  Spin dependence visible. The construction must not propagate every
    component by the same operator; it must respect the registered
    c = 1 - s^2, so c = -3 at s = 2, and this must arise before K1 is
    inserted, not be added because K1 needs -3.
C5  The square does not move. K1 enters the normalization branch as
    already frozen, h = v^2: no change of its words, amplitudes, joint law,
    local order of operations or fourth moments. If the construction needs
    a different K1, the construction failed; K1 is not repaired.
```

Falsifiers (the candidate is F if at least one fires):

```text
F1  the homogeneous limit does not give exactly FRW-CANONICAL-FORM;
F2  the lapse starts to propagate as a free mode;
F3  after the constraint an independent unphysical trace radiative mode survives;
F4  TT propagation is spin blind;
F5  closure requires a new free dimensionless coefficient;
F6  the fixed K1 must be changed according to the result.
```

## 1. The six preregistration fields

**Equation.** Discrete linearized ADM action with lapse and zero shift on the
planar carrier `Z/5` (the K1 slot axis, third coordinate of `D3/5D3`), with
the standard indefinite DeWitt kinetic form and the gravitational prefactor
`1/(2 lambda)`, `lambda = 216 pi` taken from FRW-CANONICAL-FORM [T]:

```text
S = sum_n sum_r { (1/(2 lambda)) [ (1/4)( tr(Delta H)^2 - (tr Delta H)^2 )
                                   + G_2(H) + n R_1(H) ]
                 - (1 + n) sqrt(det gamma) eps_gamma(e) }          (source reading)

S = sum_n sum_r { (1/(2 lambda)) [ (1/4)( tr(Delta H)^2 - (tr Delta H)^2 )
                                   + G_2(H) + n R_1(H) ] }         (decoder reading,
                                                                     second-order
                                                                     constraint below)
```

`gamma = I + H`, `nu = 1 + n`, `Delta f_n = f_(n+1) - f_n`. `G_2` is the
quadratic part of `sqrt(gamma) R(gamma)` (the Fierz-Pauli spatial form) and
`R_1` its linear part, both written with the planar rule: every product of two
first differences along the axis is the public stencil form `<f, L g>`, every
second difference is `-L`. `L` is the exact planar operator of the public
D3 stencil, `(L f)_r = [188 f_r - 29(f_(r-1)+f_(r+1)) - 65(f_(r-2)+f_(r+2))]/324`,
indices mod 5. No other spatial operator is introduced.

**Code.** `verify.py`, Python standard library, exact arithmetic (`Fraction`,
exact `Q(sqrt5)` pairs), `lambda` handled as an exact formal scale (the
identities are checked at two distinct rational values, which decides a
polynomial identity of degree one in `1/lambda`). No float in any assertion.

**Carrier or data.** The planar carrier `Z/5` with the public stencil; the ten
K1 words and weights, unchanged from `notes/V81-TT-K1-SOURCE-MAP-1.md`:

```text
0010,0011,0100,0101,1010,1011,1100,1101: 1/12 each;  0110,1001: 1/6 each,
u_t = b_(t+2) - b_t,  b_r(t) = (delta_(r,u_t) + delta_(r,u_t+1))/sqrt2,
iota_t(r) = a^2 b_r(t)^2,  a retained symbolically, a^2 = 1 for witnesses.
```

**Systematics.** (i) The planar restriction: the three-dimensional carrier
needs a discrete gradient to write `d_i d_j H_ij`; none is introduced, so the
candidate is stated on the planar sector only. (ii) Second order in the
decoder reading needs a local lattice density standing for `R_2(h)`; two
transcriptions are declared and compared, choice (i) the stencil energy
density, choice (ii) the literal `(3/2) h'^2 + 2 h h''`. (iii) Nonlinear
homogeneous sector: taken to be FRW-CANONICAL-FORM by declaration; only the
linearized coefficients are checked. (iv) The `k != 0` equations are the flat
static linearization; corrections from an FRW background are not derived.

**Failure threshold.** Each of F1 to F6 is decided by an exact identity or an
exact inequality printed by the verifier; no tolerance. A falsifier that fires
is recorded, not repaired.

**Action layer.** L1 (rational arrays); intended L2 role declared, no gate.

## 2. Two readings, both frozen

```text
Source reading   K1 covector e = (a b_r(t), 0, 0) is a prescribed stress source,
                 eps_gamma(e) = (1/2) e^T gamma^-1 e, covector components fixed
                 under variation, as in C-K1-DYNAMIC-METRIC-N. This reading is
                 the one the owner already confined to TT-SOURCE. It is kept
                 here only to decide whether the constrained dynamics admits it.
Decoder reading  h_+ = v^2 = iota_t(r) is the TT strain itself (registered
                 TT-SQUARING-DECODER [D], POL-READ [D]); no matter source; the
                 scalar sector is sourced at second order by the TT field
                 through the Hamiltonian constraint.
```

## 3. Checks the verifier will run, and what decides each falsifier

```text
K1  exact sector decomposition of the kinetic and gradient forms on the planar
    sector into h_+, h_x (TT), tau (transverse trace), ell (longitudinal),
    h_13, h_23 (vector); decides F3, F4 at the flat level
K2  homogeneous limit H = 2 Phi I: kinetic coefficient must be -(3/lambda)
    per site, matching FRW-CANONICAL-FORM; decides F1 (at linearized scope)
K3  Euler-Lagrange equations obtained by exact variation of the explicit
    discrete action at a random rational configuration, compared with the
    derived sector equations; lapse equation must be algebraic in n
    (no Delta^2 n term); decides F2
K4  zero mode of the Hamiltonian constraint on the compact carrier for all
    ten words, both readings
K5  source reading: conservation condition implied by the lapse and
    longitudinal equations, tested against the K1 word law for all ten words;
    decides F6 for that reading
K6  decoder reading: exact constrained scalar tau = L^+ (sigma - mean sigma)
    in Q(sqrt5) for all ten words at cut 0, under choice (i), and the
    difference against choice (ii); L L^+ = I - J/5 verified exactly
K7  coefficient census: every coefficient of the final equations is a
    rational multiple of 1, lambda or 1/lambda, with lambda public;
    decides F5
```

## 4. What this candidate does not claim

No numerical `r_T(k)`, no `P_S`, no cosmological identification of `tau`,
no physical amplitude, no Regge-Wheeler coefficient on a mass background,
no three-dimensional carrier statement, no discrete Bianchi identity at second
order, no change to any registered row, and no promotion. A fired falsifier
is a first-class outcome and is archived as such.
