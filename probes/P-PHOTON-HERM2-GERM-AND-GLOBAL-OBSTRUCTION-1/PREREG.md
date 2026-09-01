# P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1 preregistration

Status: FORMAL PREREGISTRATION / RESULT-EXPOSED / PROOF-FIRST

Owner: A. M. Thorn  
Public claim: [issue #738](https://github.com/mathorn1973/twist-j/issues/738)  
Branch: `probe/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1`  
Directory: `probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/`  
Date: 2026-09-01

This document freezes one exact proof-audit after Public Canon v74. The
mathematical result, its constants, the complete reciprocal two-torsion
obstruction, and the accepted verifier were derived before this pin. That
exposure is explicit: this is proof checking, not a blind prediction.

The written proof below owns the universal statements. The verifier audits
the complete finite shell, lattice, torsion, determinant, normalization and
negative-control certificates. The proposed scientific ceiling is
candidate-`T`; no public status moves without a later separate Canon fold.

## 0. Authority and inherited boundary

The read-back authority is:

```text
STATE:                 ACTIVE
CANON:                 Public Canon v74
AUTHORITY:             mathorn1973/twist-j main
MAIN AT CLAIM:         05a74b21df4b7d8c5c53cfa75255684929c1b76c
TAG:                   canon-v74
CONTENT_COMMIT:        2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:          2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:           389246
CLAIM DATE:            2026-09-01
```

The only inherited scientific inputs are:

```text
FCC-WEIGHTED-SHELL-SYMBOL [T], L2
FCC-WEIGHTED-SHELL-REMAINDER [T], L2
PHOTON-SPATIAL-TEMPORAL-TRANSFER [D], MULTI
PHOTON-TEMPORAL-CHARACTERISTIC [T], L5
```

The sealed predecessor probes are consumed inputs only. They are not resumed,
renamed, modified, or reinterpreted.

The current public gate

```text
GATE-L4-L5-PHOTON-CONE-IDENTIFICATION
```

remains open under every outcome of this probe. The gate presently asks for a
total typed global map and exact equality of null sets. This probe proves two
strictly narrower and logically distinct facts:

1. the rescaled v74 characteristic has the standard Hermitian Minkowski
   determinant as its exact quadratic germ, with an effective global
   remainder bound;
2. the natural *global separated inversion-equivariant vector-square-root
   class* is empty.

It does not classify arbitrary nonlinear, frequency-mixing, multichart,
bundle-valued, higher-rank, or symmetry-breaking maps. A non-covariant
set-theoretic square root is not accepted as a physical cone dictionary.

`PHOTON-MASSLESS-PHASE [O]` is untouched. No action, Gibbs state,
thermodynamic phase, propagator, polarization, apparatus, SI scale, physical
photon, or physical mass is asserted.

## Field 1: exact equation and theorem

### 1.1 The v74 characteristic

Use

```text
D3 = {x in Z^3 : x1+x2+x3 is even},
Gamma_D3 = 2 pi Z^3 union (pi(1,1,1)+2 pi Z^3),
T_D3 = R^3 / Gamma_D3.
```

For

```text
N = {2,4,8,10,16},
S_n = {v in Z^3 : |v|^2=n},
(w2,w4,w8,w10,w16)=(6,1,15,1,1),
```

put

```text
s(k) = (1/324) sum_(n in N) w_n sum_(v in S_n)
                    (1-cos(<k,v>)).
```

The inherited exact temporal characteristic is

```text
K_op = {([omega],[k]) :
        4 sin^2(omega/2)-s(k)=0}
```

on `(R/2pi Z) x T_D3`.

For `epsilon>0`, define its lifted rescaling

```text
q_epsilon(Omega,k)
  = 4 sin^2(epsilon Omega/2)/epsilon^2
    - s(epsilon k)/epsilon^2.
```

Public Canon v74 proves

```text
-(epsilon^2/12) Omega^4
 <= q_epsilon(Omega,k)-(Omega^2-|k|^2)
 <= (11/27) epsilon^2 |k|^4.                       (Q)
```

### 1.2 Standard Hermitian quadratic carrier

Freeze the independent mathematical carrier

```text
V_H = Herm_2(C)
```

with literal matrix equality. For real `(Omega,x,y,z)`, put

```text
H(Omega,x,y,z)
  = [[Omega+z, x-i y],
     [x+i y, Omega-z]].
```

Direct multiplication gives

```text
det H = Omega^2-x^2-y^2-z^2.                        (H)
```

The positive semidefinite cone is

```text
C_H = {H in Herm_2(C) : H >= 0},
```

and its boundary is the future null cone

```text
partial C_H
  = {H(Omega,k) : Omega>=0,
                    Omega^2-|k|^2=0}.
```

No spinor, Lorentz group, physical time orientation, or occurrence rule is
imported from this definition.

### 1.3 Candidate theorem A: exact tangent-germ agreement

Equations (Q) and (H) imply, for all real `Omega,k` and every
`epsilon>0`,

```text
-(epsilon^2/12) Omega^4
 <= q_epsilon(Omega,k)-det H(Omega,k)
 <= (11/27) epsilon^2 |k|^4.                        (TG)
```

Hence `q_epsilon` converges uniformly on every bounded subset of `R^4` to
`det H`. The v74 characteristic and the standard Hermitian cone therefore
agree as an exact quadratic germ, with a displayed effective modulus.

This is function convergence and equality of the limiting quadratic germ.
It is not exact equality of the finite-lattice global null sets.

### 1.4 Frozen global separated equivariant class

A standard separated global Hermitian lift would have the form

```text
H_global(omega,k)
  = tau(omega) I_2 + p(k).sigma,
tau(omega)=2 sin(omega/2),
```

where `sigma` denotes the three Pauli coordinate matrices and

```text
p : T_D3 -> R^3
```

is total. Freeze the natural spatial class `A_sep` by the exact conditions

```text
A1  p is a well-defined function on T_D3;
A2  p(-[k])=-p([k]) for every [k] in T_D3;
A3  |p([k])|^2=s(k) for every [k] in T_D3.
```

A2 is the action of the inversion element of the registered 48-element
signed-coordinate point group in its ordinary vector representation. No
continuity assumption is needed for the obstruction. Full point-group
covariance would imply A2, so the frozen class is weaker than the full
physical symmetry requirement.

A map such as `p(k)=(sqrt(s(k)),0,0)` is outside `A_sep`: it breaks inversion
covariance and chooses a direction. It cannot close a physical cone gate
merely because its norm is correct.

### 1.5 Candidate theorem B: the global class is empty

Let `B` be the `D3` basis matrix

```text
B = [[1,1,0],
     [1,0,1],
     [0,1,1]],
det B=-2,
```

and

```text
D=B^(-T)
 = (1/2)[[ 1, 1,-1],
          [ 1,-1, 1],
          [-1, 1, 1]].
```

The eight reciprocal two-torsion classes are represented by

```text
k_m = pi D m,  m in {0,1}^3.
```

They are distinct because `B^T(k_m/pi)=m` modulo `2`.

Complete exact shell evaluation gives the following table. Entries in the
middle column are the unweighted shell sums

```text
sum_(v in S_n)(1-cos(<k_m,v>))
```

in the shell order `(2,4,8,10,16)`.

```text
class type             multiplicity   shell sums          s(k_m)
m=0                    1              (0,0,0,0,0)         0
integer nonzero        3              (16,0,0,32,0)       32/81
half-integer           4              (12,12,0,24,0)      1/3
```

At any two-torsion class, `-[k_m]=[k_m]`. A2 therefore gives

```text
p([k_m])=-p([k_m]),
```

so `p([k_m])=0`. A3 would then force `s(k_m)=0`. The seven positive values
in the table contradict this. Therefore

```text
A_sep = empty.                                             (NO-GLOBAL)
```

This is not a no-go for all conceivable maps. It proves that a global,
single-chart, separated, ordinary-vector, inversion-equivariant square root
of the exact periodic symbol does not exist. A multichart or twisted vector
bundle, a frequency-dependent map, a higher-rank Clifford carrier, or a
deliberate symmetry-breaking dictionary is outside the frozen class.

### 1.6 Candidate theorem C: scalar massive kinematic extension

For a dimensionless nonnegative parameter `mu^2`, add `mu^2 I` to the
selected v74 spatial operator in the middle time slice. On a spatial
character the exact recurrence becomes

```text
psi_(m+2)-2psi_(m+1)+psi_m+(s(k)+mu^2)psi_(m+1)=0,
```

with characteristic

```text
4 sin^2(omega/2)=s(k)+mu^2.                             (M)
```

This is a mathematical scalar spectral-gap extension of the frozen temporal
class, not a derivation or physical selection of mass.

If `mu=epsilon M`, then

```text
q_(epsilon,M)(Omega,k)
  = 4 sin^2(epsilon Omega/2)/epsilon^2
    -s(epsilon k)/epsilon^2-M^2
```

satisfies

```text
-(epsilon^2/12) Omega^4
 <= q_(epsilon,M)
    -(Omega^2-|k|^2-M^2)
 <= (11/27) epsilon^2 |k|^4.                           (MG)
```

Thus the same exact modulus gives the scalar massive Minkowski germ.

The inherited bound `s<=16/9` supplies the sufficient global real-branch
condition

```text
0<=mu^2<=20/9  =>  0<=s(k)+mu^2<=4
```

for every momentum. The value `20/9` is a sufficient bound from the public
global estimate, not a claim of the sharp largest admissible mass parameter.

## Field 2: accepted code

```text
file:         probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/verify.py
sha256:       37cd038c1a9e6ff8bf5ba485d2a69ea0c7b735e9e224c117797b7740b12eb239
bytes:        9533
dependencies: Python standard library only
arithmetic:   integer and fractions.Fraction; no floating point
input:        none
command:      python3 probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/verify.py
```

The accepted verifier was read before this pin. It:

1. enumerates all five shells and verifies their complete sizes;
2. proves the support lies in `D3`, checks `det B=-2`, and checks
   `B^T D=I`;
3. recomputes the exact quadratic and quartic moments and normalizations;
4. enumerates all eight reciprocal two-torsion classes without sampling;
5. computes their exact symbol-value multiset;
6. verifies the Hermitian and massive determinant polynomials over Gaussian
   rationals;
7. checks the inherited remainder constants and the sufficient massive
   branch bound;
8. executes independent bad-weight, bad-scale, bad-reciprocal and bad-sign
   negative controls.

The written argument, not the program, owns the logical implication from
two-torsion plus oddness to emptiness, the universal real inequalities, and
bounded-set uniform convergence.

## Field 3: carrier and data

There is no external data.

```text
spatial carrier          D3
momentum carrier         T_D3=R^3/Gamma_D3
momentum equality        difference lies in Gamma_D3
frequency carrier        R/2pi Z
v74 characteristic       exact displayed scalar equation
quadratic carrier        Herm_2(C), literal matrix equality
quadratic cone            positive semidefinite cone
global comparison class  exactly A_sep, clauses A1-A3
mass parameter            conditional real mu^2>=0
```

The reciprocal two-torsion census is complete because it is the full
`Gamma_D3/2Gamma_D3`, represented by `m in F_2^3`.

## Field 4: systematics and exclusions

1. **Germ is not global equality.** The tangent theorem closes only the
   quadratic local/scaling question.
2. **The no-go class is declared.** It excludes no twisted bundle or broader
   map.
3. **No square-root gaming.** Norm equality without covariance and typing is
   insufficient.
4. **No massless phase.** A dispersion relation does not supply a measure or
   prove a thermodynamic photon phase.
5. **No pole identification.** Even a future L4 massless phase theorem would
   still need a named map from its long-distance observable and residue to
   this L5 characteristic.
6. **No physical mass.** `mu` is an inserted spectral parameter. A matter
   carrier, occurrence law, coupling, calibration, and measurement remain
   separate.
7. **No Lorentz overclaim.** The standard Hermitian determinant is a
   mathematical carrier; physical Lorentz covariance is not adopted here.
8. **No continuum state.** Only the characteristic function has an effective
   scaling limit.
9. **No status by computation.** Candidate-`T` rests on the written proof.
10. **No Canon edit.** This probe PR changes one probe directory only.

## Field 5: frozen falsifiers and outcomes

The formal gate returns `PASS` only if every item below holds exactly:

```text
F01 shell sizes differ from (12,6,12,24,6)
F02 D3 index, dual basis, or eight-class completeness fails
F03 the two-torsion value multiset differs from
    {0 once, 1/3 four times, 32/81 three times}
F04 any nonzero reciprocal two-torsion class has s=0
F05 det H differs from Omega^2-x^2-y^2-z^2
F06 the massive determinant or inserted-gap characteristic has a sign error
F07 the exact constants 11/27, 1/12, 16/9, or 20/9 fail their frozen identities
F08 any independent negative control is accepted
F09 execution exits nonzero, writes stderr, differs from EXPECTED.txt,
    changes verifier bytes, or differs across required architectures
```

Outcome grammar:

```text
PASS   every frozen theorem certificate and integrity gate passes
BREAK  a mathematical falsifier F01-F08 fires with a reproducible witness
STOP   authority, pin, bytes, environment, or execution integrity fails
```

A `PASS` proposes exactly:

```text
PHOTON-HERM2-TANGENT-GERM                 candidate-T
PHOTON-HERM2-SEPARATED-GLOBAL-OBSTRUCTION candidate-T
PHOTON-MASSIVE-SCALAR-GERM                candidate-T, conditional kinematics
```

No gate or Canon row moves in this probe PR.

## Field 6: action layer and gate boundary

The proof compares an independently frozen L4 mathematical Hermitian carrier
with the registered L5 characteristic. Its interface is `MULTI`, with the
cross-layer boundary `L4 -> L5`.

This probe does not satisfy the current positive decision condition of
`GATE-L4-L5-PHOTON-CONE-IDENTIFICATION`, because it does not supply a total
global map with exact finite-lattice null-set equality. Instead it proves:

```text
local/scaling quadratic germ: AGREE
natural global separated equivariant class: EMPTY
arbitrary total typed map class: UNCLASSIFIED
```

A later governance fold must decide whether to:

1. retarget the cone obligation to the exact tangent/scaling theorem;
2. open a distinct multichart or twisted-bundle global lane; or
3. freeze a broader global admissible class and classify it.

Silently accepting an untyped non-covariant square root is forbidden.

## Formal execution rule

Before the first formal run, this `PREREG.md` and the accepted `verify.py`
must be committed, pushed, and publicly read back at one immutable pin. After
that pin, execute exactly:

```text
python3 probes/P-PHOTON-HERM2-GERM-AND-GLOBAL-OBSTRUCTION-1/verify.py
```

A completed run adds `EXPECTED.txt`, `RUN.md`, and `RESULT.md`. The probe is
not reused or amended after sealing. A later Canon fold is separate.
