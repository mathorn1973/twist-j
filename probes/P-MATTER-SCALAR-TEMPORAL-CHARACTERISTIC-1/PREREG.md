# P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST

Owner: A. M. Thorn  
Public claim: [issue #743](https://github.com/mathorn1973/twist-j/issues/743)  
Branch: `probe/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1`  
Directory: `probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1/`  
Date: 2026-09-01

This document freezes one exact proof-audit after Public Canon v74 and the
sealed photon Herm2 probe `P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1`.
The result is exposed before the formal pin. The written proof owns the
universal statements; `verify.py` audits the exact algebra, constants and
negative controls.

The proposed scientific ceiling is candidate-`T` for mathematical scalar
kinematics only. No Canon status moves without a later separate Canon fold.
The parameter `mu` is inserted. It is not a derived particle mass.

## 0. Authority and inherited boundary

```text
STATE:                 ACTIVE
CANON:                 Public Canon v74
AUTHORITY:             mathorn1973/twist-j main
MAIN AT CLAIM:         f1281773e132eb180b330473b08ef3733ee43006
TAG:                   canon-v74
CONTENT_COMMIT:        2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:          2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:           389246
CLAIM DATE:            2026-09-01
```

Inherited exact inputs:

```text
FCC-WEIGHTED-SHELL-SYMBOL [T]
FCC-WEIGHTED-SHELL-REMAINDER [T]
PHOTON-TEMPORAL-CHARACTERISTIC [T]
P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1
  PASS / candidate-T / non-canonical
```

The predecessor is consumed and is not resumed or modified. It already proves
the conditional massive quadratic germ. This successor freezes the complete
scalar temporal branch classification, the zero-momentum gap, the exact
mass-scaling law and the global regions that follow from the public bound.

No massless-phase, pole-identification, polarization, interaction, species,
occurrence, stability, apparatus, SI or physical-mass statement is in scope.

## Field 1: equation, carrier and theorem

### 1.1 Spatial input

Use the Public Canon v74 momentum carrier

```text
T_D3 = R^3 / Gamma_D3
```

and its exact nonnegative symbol `s:T_D3->R` with

```text
s(k)>=0,
s(k)=0 iff k=0 in T_D3,
s(k)<=16/9.
```

The probe does not alter or rederive the selected shell weights.

### 1.2 Massive scalar recurrence

For one inserted real parameter `mu>=0`, freeze

```text
psi_(m+2)-2 psi_(m+1)+psi_m
  +(s(k)+mu^2) psi_(m+1)=0.                         (R)
```

Put

```text
q_mu(k)=s(k)+mu^2.
```

For the ansatz `psi_m=zeta^m`, (R) has characteristic polynomial

```text
P_q(zeta)=zeta^2+(q-2)zeta+1.                       (P)
```

Equivalently, for a two-slice state `(psi_(m+1),psi_m)`, the transfer matrix is

```text
T_q=[[2-q,-1],
     [1,   0]],

det T_q=1,
tr T_q=2-q.                                         (T)
```

Its discriminant is

```text
Delta_q=(q-2)^2-4=q(q-4).                           (D)
```

### 1.3 Exact pointwise branch classification

For the allowed range `q>=0`:

```text
q=0       P_q=(zeta-1)^2
          non-identity parabolic transfer at zeta=+1

0<q<4     two distinct conjugate roots on the unit circle
          zeta=e^(+-i omega), 4 sin^2(omega/2)=q
          elliptic transfer

q=4       P_q=(zeta+1)^2
          non-identity parabolic transfer at zeta=-1

q>4       two distinct negative real reciprocal roots
          one has modulus below one and one above one
          hyperbolic transfer; no real unit-circle frequency
```

In this probe, `FORBIDDEN` means only that no real `omega` solves the frozen
unit-circle frequency equation. It is not a claim that a configuration or a
physical state is forbidden by an occurrence law.

Define exact momentum regions

```text
E_mu={k:0<q_mu(k)<4},
P_mu^+={k:q_mu(k)=0},
P_mu^-={k:q_mu(k)=4},
F_mu={k:q_mu(k)>4}.
```

These four sets are disjoint and exhaust `T_D3` for every `mu>=0`.

### 1.4 Zero-momentum spectral gap

At the unique spatial zero,

```text
q_mu(0)=mu^2.
```

For `0<=mu<=2`, define the principal nonnegative angular gap

```text
omega_0(mu)=2 asin(mu/2) in [0,pi].                 (G)
```

Equivalently, without choosing an inverse-trigonometric representation,

```text
cos omega_0=1-mu^2/2.
```

Therefore:

```text
mu=0       zero gap and the +1 parabolic double root
0<mu<2     positive gap and two elliptic roots e^(+-i omega_0)
mu=2       the -1 parabolic double root
mu>2       no real zero-momentum frequency; hyperbolic roots
```

This is an exact dimensionless spectral gap. It is not a selected physical
mass or energy in SI units.

### 1.5 Global momentum disposition from the public bound

The public estimate `0<=s<=16/9` yields:

```text
mu^2=0:
  P_mu^+={0}; every k!=0 is elliptic.

0<mu^2<20/9:
  every momentum is elliptic.

mu^2=20/9:
  every momentum is elliptic or belongs to P_mu^-;
  no forbidden momentum exists.
  This probe does not assert that s=16/9 is attained.

20/9<mu^2<4:
  k=0 is elliptic;
  the exact sets P_mu^- and F_mu are decided pointwise by
  s(k)=4-mu^2 and s(k)>4-mu^2.
  The public upper bound alone does not decide whether either set is nonempty.

mu^2=4:
  k=0 is the -1 parabolic point and every k!=0 is forbidden/hyperbolic.

mu^2>4:
  every momentum is forbidden/hyperbolic.
```

In particular,

```text
mu^2<=20/9                                             (SAFE)
```

is a sufficient all-momentum real-branch range. It is deliberately not
asserted to be the sharp largest range.

### 1.6 Hermitian mass shell

Freeze the independent standard Hermitian carrier

```text
H(Omega,k)
 =[[Omega+k3,k1-i k2],
   [k1+i k2,Omega-k3]],

det H=Omega^2-|k|^2.
```

The scalar massive tangent shell is the determinant level set

```text
det H=M^2,
```

or equivalently

```text
Omega^2-|k|^2-M^2=0.                                 (H_M)
```

It is not obtained by calling `H+M^2 I` a Dirac or spinor mass operator. No
spin representation or first-order equation is asserted.

### 1.7 Exact scaling law and remainder

For `epsilon>0`, put

```text
mu_epsilon=epsilon M
```

and define

```text
q_(epsilon,M)(Omega,k)
 =4 sin^2(epsilon Omega/2)/epsilon^2
  -s(epsilon k)/epsilon^2-M^2.
```

The v74 remainder gives, for all real `Omega,k,M` and `epsilon>0`,

```text
-(epsilon^2/12) Omega^4
 <=q_(epsilon,M)(Omega,k)
   -(Omega^2-|k|^2-M^2)
 <=(11/27) epsilon^2 |k|^4.                         (REM)
```

Thus the massive Hermitian level polynomial is the uniform bounded-set germ
with an effective modulus.

More generally, if

```text
mu_epsilon=epsilon^alpha M,  M!=0,
```

then the rescaled mass contribution is

```text
epsilon^(2 alpha-2) M^2.
```

Hence:

```text
alpha=1   unique finite nonzero massive limit
alpha>1   mass term vanishes and the limit is massless
alpha<1   mass term diverges and no finite germ survives
```

Keeping a nonzero lattice `mu` fixed is `alpha=0`, not a finite continuum
mass scaling.

## Field 2: accepted code

```text
file:         probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1/verify.py
sha256:       36cce062e985cbd685ab87052c2bbf237261f30aeac3039b115f3778f83b16aa
bytes:        6632
dependencies: Python standard library only
arithmetic:   integers and fractions.Fraction; no floating point
input:        none
command:      python3 probes/P-MATTER-SCALAR-TEMPORAL-CHARACTERISTIC-1/verify.py
```

The accepted verifier audits:

1. the characteristic polynomial and transfer determinant;
2. the exact discriminant factorization and both parabolic endpoints;
3. `16/9+20/9=4` and the declared safe range;
4. the Hermitian determinant and massive level polynomial;
5. the unique scaling exponent for a finite nonzero mass term;
6. the inherited remainder constants;
7. independent wrong-mass-sign, wrong-temporal-sign, fixed-`mu` and
   wrong-scaling controls.

The written proof owns the inequalities, the unit-circle branch theorem and
the global statements using the inherited `s` bounds.

## Field 3: equality, scope and systematics

```text
spatial equality       equality in T_D3
frequency equality     equality in R/2pi Z
state equality         literal scalar recurrence values
mass parameter         inserted mu>=0
continuum parameter    M with mu_epsilon=epsilon M
Hermitian equality     literal 2x2 matrix equality
mass shell equality    det H=M^2
```

Systematic boundaries:

1. `mu` is not derived.
2. The safe bound `20/9` is not declared sharp.
3. A real frequency is not by itself a stable interacting particle.
4. The scalar second-order recurrence does not supply spin.
5. The Hermitian determinant comparison is a quadratic carrier comparison,
   not a first-order matter equation.
6. No coupling to the measured L4 photon phase is supplied.
7. No species, multiplicity, charge, interaction, self-energy, decay,
   occurrence or apparatus law is supplied.
8. No physical unit or SI conversion is supplied.
9. No Canon, Registry, Gate or Frontier file changes in this probe.

## Field 4: frozen falsifiers and outcomes

The formal gate returns `PASS` only if every item holds exactly:

```text
F01 P_q differs from zeta^2+(q-2)zeta+1
F02 det T_q differs from 1 or Delta_q differs from q(q-4)
F03 either endpoint fails to be the declared non-identity double root
F04 the branch classification contradicts the sign of q(q-4)
F05 q_mu(0) differs from mu^2 or the gap identity has the wrong sign
F06 16/9+20/9 differs from 4
F07 det H-M^2 differs from Omega^2-|k|^2-M^2
F08 alpha=1 is not the unique finite nonzero scaling exponent
F09 either exact remainder constant differs from 1/12 or 11/27
F10 a frozen negative control is accepted
F11 execution exits nonzero, writes stderr, changes accepted verifier bytes,
    differs from EXPECTED.txt or differs across required architectures
```

Outcome grammar:

```text
PASS   every exact certificate and integrity gate passes
BREAK  one of F01-F10 fires with a reproducible witness
STOP   authority, pin, bytes, environment or execution integrity fails
```

A `PASS` proposes exactly:

```text
MATTER-SCALAR-TEMPORAL-CHARACTERISTIC candidate-T
MATTER-SCALAR-BRANCH-CLASSIFICATION   candidate-T
MATTER-SCALAR-MASSIVE-GERM            candidate-T
```

It does not propose a physical matter or mass claim.
