# P-PHOTON-TEMPORAL-CHARACTERISTIC-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST

Owner: A. M. Thorn
Public claim: [issue #734](https://github.com/mathorn1973/twist-j/issues/734)
Branch: `probe/P-PHOTON-TEMPORAL-CHARACTERISTIC-1`
Directory: `probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/`
Date: 2026-09-01

This document freezes a selected spatial-to-temporal transfer dictionary and
the complete exact theorem derived from it. The owner selection and theorem
are separate claims. The selection has status ceiling `D`; the theorem is
proposed as `T` by the written proof below. The verifier audits finite exact
certificates and is not a numerical substitute for the universal proof.

All equations, constants, branches, bounds, outcomes and exclusions were
publicly exposed before the pin. This is disclosed result-exposed proof
checking, not a blind prediction. No formal gate execution is permitted until
this file and the accepted `verify.py` are committed, pushed, and publicly
read back byte for byte.

## 0. Authority, identity and inherited boundary

The read-back public authority is:

```text
STATE:                 ACTIVE
CANON:                 Public Canon v73
MAIN AT CLAIM:         92724e6a92ede39e11061ffe53fca672a96d0f0e
TAG:                   canon-v73
TAG OBJECT:            5f7efa1578e3f2ed182fe141ee30e9acd27cb926
TAG TARGET:            92724e6a92ede39e11061ffe53fca672a96d0f0e
CONTENT_COMMIT:        0bd22b047719a12b869db77bde9512f9e89ed751
CANON_SHA256:          c37e9cb2c4b2081d020ae2cb4b5d58789a32537e833dbba5846992a8d17022bf
CANON_BYTES:           384662
CLAIM DATE:            2026-09-01
```

The inherited public inputs are only:

- `FCC-WEIGHTED-SHELL-SYMBOL [T]`, including the five complete shells,
  `W*=(6,1,15,1,1)`, `M_2=648|k|^2`, `M_4=3168|k|^4`, and
  signed-permutation invariance;
- `FCC-WEIGHTED-SHELL-REMAINDER [T]`, including `0<=s<=16/9`, the complete
  zero lattice, and the explicit rescaled spatial remainder;
- the binding contract of
  `GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC` in Public Canon v73.

The sealed probe directories for both FCC theorems are consumed inputs only.
They are not resumed, renamed, amended or reinterpreted. The old note-grade
name `P-FCC-TIME-CHARACTERISTIC-1` was never a public formal probe and is not
reused. Related closed issues #691, #700 and #710 are disclosed historical
fuzzy matches; issue #734 is the fresh reservation for this exact identity.

`PHOTON-CONE-CONVERGENCE [O]` is `ROOT / STOP / FORMAL`. This probe targets
only its L2-to-L5 gate. It neither supplies nor compares a Herm2 carrier or
cone. The L4-to-L5 gate remains open under every outcome here.

The two candidate rows frozen by this probe are:

```text
PHOTON-SPATIAL-TEMPORAL-TRANSFER [D]
  item type: DICTIONARY
  layer: MULTI (selected L2 datum and selected L5 transfer rule)
  status ceiling: D

PHOTON-TEMPORAL-CHARACTERISTIC [T]
  item type: THEOREM
  layer: L5
  proposed status: T by the independent written proof
```

The probe PR changes no Canon, Registry, Normative, Evidence, Dependency,
Gate, Frontier, Status, release or workflow file. A later separate sealed
Canon fold alone may register these rows and close the gate positively as a
dictionary lift supported by the theorem.

## Field 1: equation

### 1.1 Spatial carrier, equality and selected datum

Use the standard integer embedding in `R^3` and put

```text
D3 = {x=(x1,x2,x3) in Z^3 : x1+x2+x3 is even},
N  = {2,4,8,10,16},
S_n = {v in Z^3 : v1^2+v2^2+v3^2=n},
(w2,w4,w8,w10,w16) = (6,1,15,1,1).
```

Real-space points have literal equality in `D3`. The 48 signed coordinate
permutations act as symmetries but are not quotiented: symmetry-related
characters remain distinct carrier points.

The reciprocal period lattice is

```text
Gamma_D3
  = {q in R^3 : <q,x> is in 2pi Z for every x in D3}
  = 2pi Z^3 union (pi(1,1,1)+2pi Z^3).
```

Momentum equality is exactly `k~k'` iff `k-k' in Gamma_D3`. The momentum
carrier is the character torus `T_D3=R^3/Gamma_D3`.

The spatial coordinate unit is one in the displayed integer embedding. The
selected fixed trivial flux representative is the edge function

```text
F0(x,v)=1 in U(1) for x in D3 and v in union_n S_n,
F0(x+v,-v)=conjugate(F0(x,v))=1.
```

Path transport is the ordered product of edge values. Every path transport
is one, hence every closed-path and triangle holonomy is one. Flux equality
is literal edgewise equality in this fixed gauge. No gauge representative is
selected after inspecting a result.

Let `V=Map(D3,C)`, all complex-valued functions on `D3`. Define the finite
sum first in flux-covariant form, consuming the selected `F0` explicitly,
and then simplify by its frozen value. It is total on `V`:

```text
(A_F0 f)(x)
  = (1/324) sum_(n in N) w_n sum_(v in S_n)
      [f(x)-F0(x,v)f(x+v)]
  = (1/324) sum_(n in N) w_n sum_(v in S_n) [f(x)-f(x+v)].
```

For the Fourier character `chi_k(x)=exp(i<k,x>)`, shell reversal cancels the
imaginary part and gives

```text
A_F0 chi_k = s(k) chi_k,
s(k) = (1/324) sum_(n in N) w_n sum_(v in S_n)
                         (1-cos(<k,v>)).
```

The factor `1/324` is the selected dimensionless operator normalization. It
is fixed from the inherited identity `M_2=648|k|^2`, so the quadratic Taylor
coefficient of `s` is one. It is not a physical distance, duration, speed or
SI conversion.

### 1.2 Time carrier, normalization and selected transfer class

Time is the public forward counter with unit update `m->m+1`. For every
`m>=0`, the total state is the two-slice value

```text
X_m=(psi_(m+1),psi_m) in H=V x V,
```

with arbitrary initial `X_0=(psi_1,psi_0)`. One update is one dimensionless
time unit. The
time/space scale relation is frozen by requiring the tangent characteristic
to have unit coefficients `omega^2-|k|^2`; no independent coefficient or
physical velocity is left in this selected dictionary.

The selected temporal reading family is exactly the following declared
class, and no larger class:

```text
psi_(m+2)+psi_m+(a+b s(k))psi_(m+1)=0,  m>=0,
```

on each spatial character, where `a,b` are real constants independent of
`m,k`; leading and trailing coefficients are normalized to one; the rule is
scalar, translation-invariant, nearest-neighbor and time-reversal symmetric;
there is no mass or other term; and the spatial dependence is affine and
only through the already selected scalar `s`.

The zero mode `(lambda,s)=(1,0)` forces `a=-2`. Under the convention
`lambda=exp(-i omega)`, the small-variable equation is

```text
-omega^2+b s+higher order=0.
```

The frozen unit tangent normalization forces `b=1`. Thus this selected class
contains exactly the rule

```text
psi_(m+2)-2psi_(m+1)+psi_m+A_F0 psi_(m+1)=0,
X_(m+1)=T_op X_m,
T_op = [[2I-A_F0,-I],[I,0]].
```

This is a `D` selection and a uniqueness theorem only inside the displayed
class. No completeness or uniqueness is claimed among longer-range,
matrix-valued, nonlinear, nonlocal, massive, non-reversible, differently
normalized or non-flat-flux rules.

### 1.3 Exact characteristic

On a spatial character, the transfer matrix is

```text
T(k) = [[2-s(k),-1],
        [1,       0]],
det T(k)=1.
```

Time-frequency equality is `omega~omega+2pi r`, `r in Z`, with the fixed
multiplier convention `lambda=exp(-i omega)`. This is a characteristic
parameter of the forward two-slice transfer, not a second physical clock and
not an adoption of a bilateral time architecture.

Define the total matrix

```text
C(omega,k) = exp(-i omega) I_2-T(k)
            = [[exp(-i omega)-2+s(k), 1],
               [-1,                    exp(-i omega)]].
```

Its domain is `(R/2pi Z) x T_D3`, its codomain is `Mat_2(C)`, and equality is
entrywise complex equality after the stated quotient equalities. Direct
expansion gives

```text
det C(omega,k)
  = exp(-2i omega)-(2-s(k))exp(-i omega)+1
  = exp(-i omega)[s(k)-4sin^2(omega/2)].
```

The L5 characteristic null set is

```text
K_op
  = {([omega],[k]) in (R/2pi Z) x T_D3 : det C(omega,k)=0}
  = {([omega],[k]) : 4sin^2(omega/2)=s(k)}.
```

`K_op` is a set. Algebraic root multiplicity is recorded separately.

### 1.4 Exact branches and small-scale function bound

Public Canon v73 gives `0<=s(k)<=16/9<4` and says `s(k)=0` exactly on
`Gamma_D3`. Therefore every nonzero `[k] in T_D3` has two distinct real
frequency classes

```text
omega_+(k)=+2asin(sqrt(s(k))/2),
omega_-(k)=-2asin(sqrt(s(k))/2)        modulo 2pi,
```

and reciprocal conjugate multipliers

```text
lambda(omega_+) = 1-s/2-i sqrt(s-s^2/4),
lambda(omega_-) = 1-s/2+i sqrt(s-s^2/4),
lambda(omega_+)lambda(omega_-)=1,
|lambda(omega_+)|=|lambda(omega_-)|=1.
```

The transfer is elliptic for `s>0`. At the unique zero character, both roots
are `lambda=1`; `T(0)` is non-identity unipotent with `(T(0)-I)^2=0`, hence
parabolic. The branches meet only there and the algebraic multiplicity is two.

For every real `epsilon>0`, `Omega in R`, and `k in R^3`, define the lifted
universal-cover comparison function

```text
q_epsilon(Omega,k)
  = 4sin^2(epsilon Omega/2)/epsilon^2
    - s(epsilon k)/epsilon^2.
```

The exact two-sided bound is

```text
-(epsilon^2/12) Omega^4
  <= q_epsilon(Omega,k)-(Omega^2-|k|^2)
  <= (11/27) epsilon^2 |k|^4.                 (Q)
```

Hence `q_epsilon` converges uniformly on every bounded `(Omega,k)` set to
`Omega^2-|k|^2`. This is convergence of characteristic functions only. It is
not equality, Hausdorff convergence, or physical convergence of null sets,
states, measures, propagators or spacetime theories.

## Field 2: code

`verify.py` is the accepted exact certificate audit. It uses only the Python
standard library, exact integers and `Fraction`. It uses no floating point,
randomness, network, subprocess, clock, environment-dependent input or file
writes. It accepts no arguments. Successful stdout is buffered until all
gates pass; any exception emits only a generic `STOP` line to stderr and exits
nonzero.

The verifier audits finite certificates for:

- complete shells, weights, moments, normalization and signed-permutation
  invariance;
- the support lattice `D3` and reciprocal two-coset lattice;
- the fixed trivial flux typing and reversal law;
- uniqueness inside the frozen two-parameter temporal class;
- exact transfer and characteristic determinant polynomials;
- reciprocal unit-circle roots, stability interval and parabolic apex;
- exact temporal cosine and inherited spatial remainder constants in (Q);
- independent negative controls for the datum, dual lattice, flux, stencil,
  transfer sign and normalization.

The universal cosine inequalities, zero-locus implication, branch argument
and bounded-set limit are proved below. The verifier checks their finite
algebraic certificates; it does not sample real `omega`, `k` or `epsilon` as
a substitute for proof.

## Field 3: carrier and data

There is no external dataset. Every consumed mathematical object is literal
in Field 1. The carrier/equality ledger is:

```text
real space       D3 with literal point equality
state carrier    V=Map(D3,C), H=V x V, literal function/pair equality
spatial steps    all vectors of S_2,S_4,S_8,S_10,S_16
weights          W*=(6,1,15,1,1), shell-constant and positive
spatial unit     standard integer-coordinate unit one
operator scale   1/324
flux             fixed edgewise F0=1, exact equality in the fixed gauge
momentum          R^3/Gamma_D3
momentum equality k-k' in Gamma_D3
counter           m in N0, forward unit update; arbitrary two-slice X_0
time unit         one counter update
frequency         R/2pi Z, lambda=exp(-i omega)
transfer          X_(m+1)=T_op X_m
characteristic    C:(R/2pi Z)xT_D3 -> Mat_2(C), total
null equality     equality of subsets of the declared product quotient
```

The 48 signed permutations are exact symmetries, not carrier equality. Each
`chi_k` is a simultaneous eigenfunction of spatial translations and satisfies
`A_F0 chi_k=s(k)chi_k`; no Fourier completeness or diagonalization of all
`V=Map(D3,C)` is claimed. Translation-related functions are not identified
unless literally equal.

## Field 4: systematics and boundary ledger

1. **Selection is not derivation.** `D3`, `W*`, `1/324`, `F0`, the unit
   counter relation and the temporal class are owner-adopted dictionary data.
   The exact theorem is conditional on that tuple. The computation cannot
   prove an owner choice.
2. **Ambient `Z^3` is not the selected carrier.** All steps preserve the two
   parity cosets in `Z^3`. On the selected `D3` carrier the two ambient zero
   representatives are one momentum character. They are not two photons,
   polarizations, visible/invisible sectors or Born halves.
3. **No hidden scale `alpha`.** A family with `alpha s(k)` exists, but this
   probe freezes exactly `alpha=1` through the displayed dimensionless
   tangent normalization. Another scale is a different dictionary, not an
   alternative result inside this probe.
4. **Flat flux only.** A non-flat `Z5` or other magnetic flux may make the
   symbol matrix-valued. It is outside this selected datum and cannot be
   inferred or refuted here.
5. **Forward time only.** Algebraic invertibility and the reciprocal roots do
   not add negative counter values to the public architecture. The
   time-reversal phrase describes the frozen recurrence coefficients.
6. **Apex multiplicity.** `K_op` is a set; the double root at the apex and
   the nontrivial Jordan block are stated separately. No diagonalizability or
   uniform boundedness is claimed at the apex.
7. **Theorem replacement.** A later derived carrier, weight, flux, scale or
   clock rule may supersede the `D` row. That is a recorded dictionary
   replacement or `STOP`, not by itself a counterexample to the conditional
   algebra proved here.
8. **No cone comparison.** Herm2, Born positivity and any map `iota` are
   absent. The local quadratic function limit does not close the L4-to-L5
   gate and is not a physical continuum claim.
9. **No branch ontology.** The reciprocal pair consists of unit-modulus
   phases for `s>0`; it is not mathematically a contraction/expansion pair.
   Any matter/light, visible/invisible or cosmological reading stays outside
   the earned scope.

## Field 5: failure threshold and outcomes

### `CHARACTERISTIC-PROVED`

This outcome requires the complete selected tuple to be internally typed,
the written proof to establish every displayed equality and universal bound,
all exact certificate gates to pass, exit code zero, empty stderr, exact
stdout capture, pin integrity, and required public architecture checks.

It earns only the proposed `D` dictionary and conditional `T` theorem. It
does not itself edit or close the public gate. A separate Canon fold may close
the L2-to-L5 gate positively only if it registers the complete tuple, theorem,
dependencies, evidence and lift ownership without changing this scope.

### `CHARACTERISTIC-REFUTED`

An independently checked exact counterexample to the selected operator
symbol, determinant identity, root classification, zero quotient, scaling
bound, or another displayed theorem clause refutes the conditional `T` claim.
This outcome does **not** negatively close the parent gate. Public Canon v73
allows negative closure only when a complete frozen admissible temporal-
transfer class for a selected datum is proved empty. This probe deliberately
selects one class and proves one member; it does not classify all admissible
rules. Failure of one provisional rule leaves the gate `OPEN_LIFT / STOP`.

### `STOP`

Any missing or ambiguous carrier field, equality, scale, flux, normalization,
rule, endpoint, proof step, pin, transcript, security check, clean checkout,
public readback or architecture requirement is `STOP`. An internally
ill-typed proposed `D` tuple is exclusively `STOP`, never
`CHARACTERISTIC-REFUTED`. Runtime and integrity defects are not scientific
falsifiers. Thresholds and exclusions never move after this pin.

## Field 6: action layer and gate

```text
source layer:    L2 selected spatial transfer datum
target layer:    L5 exact two-slice transfer characteristic
dictionary row: PHOTON-SPATIAL-TEMPORAL-TRANSFER [D], MULTI
theorem row:    PHOTON-TEMPORAL-CHARACTERISTIC [T], L5
gate:           GATE-L2-L5-PHOTON-TEMPORAL-CHARACTERISTIC
gate result:    candidate positive dictionary lift only after separate fold
```

The dictionary owns the cross-layer selection. The theorem supports it but
does not turn the owner choice into a mathematical necessity. The parent
`PHOTON-CONE-CONVERGENCE [O]` remains open because its independent
`GATE-L4-L5-PHOTON-CONE-IDENTIFICATION` is untouched.

## 7. Self-contained written proof

### 7.1 Support and reciprocal lattice

Every `v in S_n` has even coordinate sum modulo two because
`v_i^2=v_i (mod 2)` and every selected `n` is even. Thus the support lies in
`D3`. The three vectors

```text
b1=(1,1,0), b2=(1,0,1), b3=(0,1,1)
```

belong to `S_2` and have determinant `-2`. Their span is an index-two
sublattice of `Z^3` contained in the index-two lattice `D3`, so it equals
`D3`.

A vector `q` is reciprocal exactly when `<q,b_j>` lies in `2pi Z` for all
three basis vectors. In units of `2pi`, the inverse-transpose basis has
half-integral columns all congruent modulo `Z^3` to `(1/2,1/2,1/2)`. Hence
the reciprocal lattice has exactly the two residue classes

```text
Z^3 and (1/2,1/2,1/2)+Z^3,
```

which gives the displayed `Gamma_D3`. Consequently the two zero cosets of
the ambient `Z^3` Fourier display are a single zero character on `T_D3`.

### 7.2 Fourier symbol and flat flux

For `chi_k(x)=exp(i<k,x>)`,

```text
(A_F0 chi_k)(x)/chi_k(x)
  = (1/324) sum_(n,v) w_n [1-F0(x,v)exp(i<k,v>)]
  = (1/324) sum_(n,v) w_n [1-exp(i<k,v>)].
```

Each complete shell is closed under `v->-v` with the same weight and `F0=1`.
Pairing reversed vectors cancels the sine terms and changes the last display
to the real function `s(k)`. It is invariant under `Gamma_D3` because every
support vector lies in `D3`. The flux reversal and every closed holonomy are
one directly from the constant edge function.

All summands of `s` are nonnegative. Therefore `s(k)=0` exactly when every
support phase is one, equivalently when `k` is reciprocal to the lattice
generated by the support, namely `Gamma_D3`. This also reproves the required
zero statement at the selected quotient scope.

The quadratic coefficient is `M_2/(2*324)=648/(648)=1`. The crude universal
bound `1-cos x<=2` and weighted count

```text
sum_n w_n |S_n| = 288
```

give `s<=2*288/324=16/9`. No sharpness is claimed.

### 7.3 Uniqueness inside the selected temporal class

Substituting `psi_m=lambda^m` into the frozen two-parameter class gives

```text
lambda+lambda^-1+a+b s=0.
```

The required zero mode `lambda=1,s=0` gives `2+a=0`, so `a=-2`. With
`lambda=exp(-i omega)`, `lambda+lambda^-1=2cos omega`, whose quadratic term
at zero is `-omega^2`. The required unit tangent equation is
`omega^2-s=0`; therefore `b=1`. These two independent linear conditions have
the unique solution `(-2,1)` inside the declared class.

Solving forward gives the displayed `T_op`. It is total on `H` because
`A_F0` is a finite sum total on `V`.

### 7.4 Characteristic determinant and branches

Direct `2x2` expansion gives

```text
det T=1,
det(lambda I-T)=lambda^2-(2-s)lambda+1.
```

For nonzero `lambda=exp(-i omega)`, division by `lambda` gives

```text
lambda+lambda^-1-2+s
  = 2cos omega-2+s
  = s-4sin^2(omega/2).
```

This proves the determinant formula and `K_op` equality.

The polynomial discriminant is `s(s-4)`. For `0<s<=16/9<4` it is negative,
so the roots are distinct conjugates. Their product is one, hence each has
modulus one. Explicitly their real part is `1-s/2` and their squared
imaginary part is `s-s^2/4`; the principal frequencies are the displayed
`+-2asin(sqrt(s)/2)`. At `s=0` the polynomial is `(lambda-1)^2` and direct
matrix multiplication gives `(T(0)-I)^2=0` while `T(0)!=I`. This proves the
elliptic/parabolic and meeting statements.

### 7.5 Exact characteristic-function remainder

For real `x`, put

```text
P2(x)=x^2/2-1+cos x,
P4(x)=1-cos x-x^2/2+x^4/24.
```

Then `P2(0)=P2'(0)=0` and `P2''(x)=1-cos x>=0`, so double integration gives
`P2>=0`. Also `P4(0)=P4'(0)=0` and `P4''=P2>=0`, so `P4>=0`. Since
`P2+P4=x^4/24`, this proves `P2<=x^4/24` without a local Taylor truncation.
Therefore

```text
0 <= x^2-4sin^2(x/2) <= x^4/12.             (TREM)
```

The inherited spatial theorem, or its repeated proof from the same scalar
certificate and exact fourth moment, gives for every `epsilon>0`

```text
0 <= |k|^2-s(epsilon k)/epsilon^2
  <= (11/27)epsilon^2|k|^4.                 (SREM)
```

Write the temporal deficit in (TREM) as `A_t` and the spatial deficit in
(SREM) as `A_s`. Then

```text
q_epsilon-(Omega^2-|k|^2)=-A_t+A_s,
0<=A_t<=(epsilon^2/12)Omega^4,
0<=A_s<=(11/27)epsilon^2|k|^4,
```

which is exactly (Q). On a bounded set the two displayed endpoint bounds are
uniform and tend to zero, proving compact-uniform convergence of the
functions.

## 8. Exact audit gates and controls

The accepted verifier freezes twenty gates. Positive gates audit the shell
and moment inputs, `D3` and its reciprocal, `F0`, the selected scale and
temporal-class solution, transfer determinant, characteristic polynomial,
root norm, stability constants, apex and both remainder constants.

Independent constructed controls are rejected by the same predicates:

```text
N1  change W* or remove one shell vector;
N2  replace 1/324 by 1/323;
N3  replace the reciprocal basis by an index-three proper sublattice whose
    first basis column is tripled; it has the same two coarse residue classes
    modulo Z^3 but fails primitive dual equality;
N4  replace F0=1 by an orientation assignment whose triangle holonomy is -1;
N5  change a=-2 or b=1 in the frozen temporal class;
N6  reverse the lower-left transfer sign, changing det T;
N7  alter a characteristic-polynomial coefficient;
N8  alter either 1/12 or 11/27 in the scaling certificate.
```

Controls do not change the datum used by positive gates and are not searches
over an unstated family.

## 9. Output and execution lock

On success, the verifier emits one ASCII header, exactly twenty `PASS` lines,
one exact total line, and two boundary lines. It emits nothing scientific
until all gates have passed. On failure it emits no partial successful
transcript.

The only authorized command after the public pin and readback is:

```text
python3 probes/P-PHOTON-TEMPORAL-CHARACTERISTIC-1/verify.py
```

under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
```

from a clean Linux-compatible checkout at the exact pin. Capture stdout and
stderr separately. The first completed formal run fixes `EXPECTED.txt`.
`RUN.md` and `RESULT.md` may then be added without changing the pinned files.
The PR must touch this probe directory only and pass the required x86_64,
aarch64, aggregate and security checks. No amend, rebase, force-push, squash,
threshold change or post-result rule change is permitted.

## 10. Non-claims

No Herm2 carrier, positive cone, Born rule, causal ontology, `iota`, global
cone equality, Lorentz invariance, physical continuum, massless Gibbs phase,
propagator, polarization, apparatus, readout, SI value or physical photon is
proved. The two temporal phases are not labeled contraction/expansion,
matter/light or visible/invisible. The user's cosmological reading is
motivation only and is not consumed as a mathematical premise.
