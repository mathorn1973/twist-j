# C-NAND-MINIMAL-LIFT-N

**Status:** NON-CANONICAL incubation. candidate-T / L1 only. No authority. No Canon status change.

**Date:** 2026-08-29

**Purpose:** Record the exact negative result from the NAND exercise: the binary NAND polynomial shadow does not determine its minimal integer lift. Under the chosen cyclotomic diagonal read at `j = zeta_5`, the two minimal lift classes become respectively a unit of norm `1` and a ramified element of norm `5`.

No computation is used in this note. The result is a self-contained exact proof.

## 1. Scope and convention

Write the Boolean NAND polynomial in algebraic normal form as

\[
N(x,y)=1+xy \in \mathbf F_2[x,y].
\]

This note studies **literal coefficientwise polynomial lifts**

\[
P(x,y)\in\mathbf Z[x,y],\qquad P\bmod 2=N
\]

as an equality in `F_2[x,y]`.

This scope is load-bearing. It is **not** the larger class of arbitrary integer polynomials that merely induce the same Boolean function on `{0,1}^2`; Boolean-function identities such as `x^2=x` are not quotiented here.

For

\[
P=\sum_{a,b\ge 0} c_{ab}x^ay^b,
\]

define coefficient height

\[
H(P):=\max_{a,b}|c_{ab}|.
\]

Two lifts are identified up to global sign when `P ~ -P`.

## 2. Minimal integer lift classification

### Proposition

Among integer polynomial lifts of `N(x,y)=1+xy` of minimal coefficient height, the complete list is

\[
P(x,y)=\pm 1\pm xy.
\]

Modulo global sign there are exactly two classes:

\[
\boxed{R_+(x,y)=1+xy},
\qquad
\boxed{R_-(x,y)=1-xy}.
\]

### Proof

If

\[
P\bmod 2=1+xy,
\]

then the constant coefficient and the coefficient of `xy` are odd, while every other coefficient is even.

Therefore every lift has `H(P) >= 1`. At height one, the two odd coefficients can only be `+1` or `-1`, while every even coefficient must be zero. Hence

\[
P=\pm1\pm xy.
\]

This gives four height-one lifts. Quotienting by global sign pairs them as

\[
\{1+xy,-1-xy\},
\qquad
\{1-xy,-1+xy\},
\]

so exactly two classes remain. `square`

Thus the result is a classification, not a search witness.

## 3. The two classes have the same binary shadow

Modulo two,

\[
R_+(x,y)\equiv R_-(x,y)\equiv1+xy.
\]

Therefore the reduction map from the two global-sign classes of minimal lifts to the NAND polynomial shadow is non-injective:

\[
\{[R_+],[R_-]\}\longrightarrow\{N\}.
\]

There is no reconstruction map from the NAND shadow that recovers both original lift classes. A section can of course be imposed by an additional choice, but that choice is not contained in the binary shadow.

This is the exact no-go.

## 4. Chosen cyclotomic diagonal read

Now make an additional, explicitly chosen read:

\[
x=y=j,\qquad j=\zeta_5.
\]

For the positive lift,

\[
R_+(j,j)=1+j^2=J.
\]

Its norm is

\[
N_{\mathbf Q(j)/\mathbf Q}(J)
=\prod_{a=1}^{4}(1+j^{2a})
=\Phi_5(-1)
=1.
\]

So the positive class gives the TWIST-J unit.

For the negative lift,

\[
R_-(j,j)=1-j^2=(1-j)(1+j).
\]

Since

\[
N(1+j)=\Phi_5(-1)=1,
\]

`1+j` is a unit, so `1-j^2` is associated to the standard ramified element `1-j`. Equivalently,

\[
N(1-j^2)
=\prod_{a=1}^{4}(1-j^{2a})
=\Phi_5(1)
=5.
\]

Hence

\[
\boxed{
R_+\equiv R_-\pmod 2,
\qquad
N(R_+(j,j))=1,
\qquad
N(R_-(j,j))=5.
}
\]

The two minimal integer lift classes that are identical in the NAND shadow become arithmetically distinct under this chosen cyclotomic diagonal read:

\[
\begin{array}{ccl}
1+xy &\mapsto& J=1+j^2,\quad N=1,\quad \text{unit branch},\\[1mm]
1-xy &\mapsto& 1-j^2,\quad N=5,\quad \text{ramified branch}.
\end{array}
\]

## 5. No-go statement

**candidate-T / L1 / NON-CANONICAL.**

> Reduction modulo two identifies the two global-sign classes of coefficient-height-one integer polynomial lifts of the NAND algebraic-normal-form polynomial `1+xy`. Under the additional diagonal read `x=y=zeta_5`, one class maps to the unit `J=1+zeta_5^2` of norm `1`, while the other maps to `1-zeta_5^2`, an associate of the ramified element `1-zeta_5`, of norm `5`. Therefore the binary NAND polynomial shadow does not contain the information required to reconstruct which of these two minimal integer lift classes was present before reduction.

Equivalently:

\[
\boxed{\text{NAND is a shadow, not a sufficient lift.}}
\]

A compact reading is:

> NAND knows the relation, but the binary shadow does not determine the sign of its minimal integer lift. Under the chosen cyclotomic diagonal read, that lost sign separates a unit branch from a ramified branch.

## 6. What this does not prove

This note does **not** claim any of the following:

- that characteristic two generally identifies the TWIST-J axiom with ramification;
- that `J` or `Q(zeta_5)` is derived from NAND;
- that no richer NAND circuit, typed carrier, external orientation, or additional datum can select `R_+`;
- that NAND alone produces the five-point carry pentad;
- that NAND selects an oriented `C_5`, a primitive generator `j`, or the exponent `2` in `J=1+j^2`;
- that Thue-Morse is derived from NAND; functional completeness only means that a NAND circuit can implement its Boolean operations;
- that the chosen diagonal read `x=y=zeta_5` is forced;
- any decoder, physical, measure, apparatus, or L2-L6 statement.

The no-go is narrower and exact: **within the frozen minimal-lift class, the binary shadow is non-injective. Additional structure is required to select a lift.**

## 7. Relation to Public Canon v69

At the time of writing, Public Canon v69 is the active public authority. This note changes none of its claims.

Relevant existing public rows are contextual only:

- `CARRY-QUADRATIC-SYMMETRY [T]` classifies the permutation-invariant pure quadratic Boolean form and explicitly states that five is an output cardinality, not a selected rational prime.
- `CARRY-PENTAD [T]` gives the five-point singular set and its `O^-(4,2) ~= S_5` symmetry, while explicitly selecting no cycle, orientation, exponent, `J`, or physical reading.
- `J-BINARY-NORM-DESCENT [T]` gives the exact binary norm descent at the prime `2` and explicitly does not select `J`, `2`, `5`, or order five.
- `RAMIFIED-TM-LIFT [T]` gives the separate ramified `F_5` phase lift and the universal carry identity, with no claim that the binary quotient alone selects the lift.

The present note does not strengthen, merge, or reinterpret those rows. It records a separate exact L1 obstruction discovered by the NAND exercise.

## 8. Falsifier

The classification fails if any integer polynomial `P` exists such that

\[
H(P)=1,
\qquad
P\bmod2=1+xy
\]

as a literal equality in `F_2[x,y]`, but `P` is not one of `+-1 +- xy`.

The cyclotomic corollary fails if

\[
N(1+j^2)\ne1
\]

or

\[
N(1-j^2)\ne5
\]

for `j=zeta_5`.

A different lift class obtained only after enlarging the declared scope, or a selector using additional typed data, does not falsify this note.
