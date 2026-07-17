# P-J-LI-S2-RELATIVE-DETERMINANT-1. Preregistration predefinition

```text
STATUS:      PREDEFINITION. DRAFT. BLOCKED-ON-CONCRETE-A_J.
AUTHORITY:   none. NON-CANONICAL.
SOURCE:      notes/C-LI-S2-RELATIVE-DETERMINANT-1/
WARNING:     this is not probes/P-J-LI-S2-RELATIVE-DETERMINANT-1/PREREG.md.
             No formal gate has been pinned or executed.
```

A formal probe is premature until a concrete operator `A_J`, its Hilbert
space, and its J-only dependency graph exist.  If that construction is
supplied, the owner must open a fresh `probe/P-J-LI-S2-RELATIVE-DETERMINANT-1`
branch and pin fresh `PREREG.md` and `verify.py` files before the first formal
execution.  This draft cannot be retroactively promoted into that pin.

## 1. Equation

The target is a complex Hilbert space `H_J` and a positive operator

```text
A_J=A_J* >= 0,       A_J in S1,       rank(A_J)=infinity,
sqrt(A_J) not in S1,
```

constructed solely from declared J-data.  With the ordinary Fredholm
determinant,

```text
D_J(t)=det_1(I-t^2 A_J),       D_J(0)=1.
```

The proof-only terminal equality is

```text
D_J(t)=Xi_J(t)/Xi_J(0)
```

as an identity of entire functions, where `Xi_J(t)=xi_J(1/2+i t)` and the
root-filter-normalized `xi_J` uses `Z_J=P_0/f_5=zeta`, not raw `P_0`.

The polarized Cayley map is frozen as

```text
Z_A=(I+(i/2)sqrt(A_J))(I-(i/2)sqrt(A_J))^(-1),
O_J=realification(Z_A),
```

with one complex positive-frequency copy in the determinant.  The direct
rotation singular value at an eigenvalue `a` is

```text
s(I-O_J)=sqrt(a/(1+a/4)).
```

Local Fredholm moments are

```text
-d/dx log det_1(I-x A_J)
  = sum_(n>=0) q_n x^n,
q_n=Tr(A_J^(n+1)).
```

Both shifted Hankel families `(q_(i+j))` and `(q_(i+j+1))` must be positive
semidefinite at every order.  Finite prefixes are calibration and kill tests,
not substitutes for the terminal identity.

## 2. Code

The prep dictionary verifier is
`verify_s2_relative_determinant.py`.  A formal probe must copy or rewrite it
as a freshly reviewed `probes/P-J-LI-S2-RELATIVE-DETERMINANT-1/verify.py` and
pin the exact bytes before any formal execution.

The current verifier uses only the Python standard library and exact
`Fraction` arithmetic.  It audits finite instances of:

```text
S1  Cayley rotation and S2 factors;
S2  the block Li formula and cocycle telescope;
S3  spectral moments and Li second differences;
S4  A-to-O, B_A, and the Chebyshev trace formula;
S5  complex polarization versus real determinant squaring;
S6  Fredholm log-derivative moments;
S7  shifted Hankel positivity;
S8  restricted direct-carrier obstruction skeletons.
```

Classical infinite theorems are proof-first imports and are not machine
assertions.

## 3. Carrier or data

No external dataset is allowed.  No zero list, prime table, zeta evaluation,
Li coefficient table, or standard Weil form may enter the construction.

Before a formal pin the proposal must freeze:

1. the complex Hilbert space and dense/common domains, if unbounded parent
   operators occur;
2. the C4 action and the projector onto the trivial sector;
3. the parent operator pair if `relative determinant` is meant literally;
4. the perturbation or resolvent difference that is trace class;
5. the positive-frequency polarization and multiplicity convention;
6. the local block at 5 and the archimedean block.

If no parent pair and determinant quotient are defined, the object is an
ordinary positive Fredholm construction and must be named as such.

## 4. Systematics

The gates are ordered and frozen as follows.

```text
G0  J-only dependency graph for A_J.
G1  Hilbert space, adjunction, domains, C4 projector, multiplicities,
    polarization.
G2  A_J>=0, A_J in S1, infinite rank, sqrt(A_J) not in S1.
G3  det_1, D_J(0)=1, Z_J=P_0/f_5, local block at 5.
G4  only local/coefficient accounting on a named test domain: declared
    Taylor/log-derivative coefficients, Gamma, von Mangoldt, filter
    subtraction.  No global meromorphic identity.
G5  lambda_1..lambda_3, K_2, K_3, and declared q/Hankel data emerge as
    outputs rather than inputs.
G6  explicit polarized A-to-O map, I-O_J in S2, I-O_J not in S1, no
    determinant doubling.
G7  dependency audit: no zeta, Xi, zeros, primes, Li table, or Weil form as
    hidden input.
G8  proof-only entire identity D_J=Xi_J/Xi_J(0).
```

If G4 is formulated as equality of complete logarithmic derivatives on an
open connected region, normalization already integrates it to G8.  Such a G4
is forbidden because it hides the terminal wall in an earlier gate.

The real S2 form and the complex determinant form use different multiplicity
bookkeeping: realification doubles each positive-frequency eigenvalue.  Any
formal candidate must demonstrate the polarization explicitly.

## 5. Failure threshold

The construction fails on the first occurrence of any of the following:

```text
A_J is not positive or not trace class;
rank(A_J) is finite;
sqrt(A_J) is trace class while exact Li Schatten behavior is claimed;
the real determinant is asserted without the required square/polarization;
the trivial sector uses raw P_0 or omits the local block at 5;
any exact local coefficient differs;
any exactly derived Hankel matrix has a negative direction;
an input dependency reaches zeta, Xi, zeros, primes, Li data, or Weil;
an undeclared pole, zero, kernel, multiplicity, or normalization occurs.
```

A failure before G8 falsifies the proposed J-construction.  It is not a
counterexample to RH.  G8 cannot be certified by a finite numerical sweep.

## 6. Action layer

```text
L6: measure / operator ideal.
```

Every lift from the finite pentagon, toral, ideal, kernel, or stream layers
into this global positive operator requires a separately named bridge.  No
such lift is created by this draft.

## Promotion posture

```text
current       notes-only predefinition
next          concrete A_J candidate with G0-G3 proofs and a frozen
              dependency graph
then          owner claim, fresh probe branch, fresh prereg/verifier pin
never         retroactive promotion of this notes run
```
