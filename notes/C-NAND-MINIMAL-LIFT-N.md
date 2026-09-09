# C-NAND-MINIMAL-LIFT-N

**Status:** NON-CANONICAL incubation. No authority. No Canon status change.

**Date:** 2026-08-29

**Purpose:** Record the exact results of the NAND / lifted-Sheffer exercise while preserving the failed route that led to the stronger invariant.

This note contains four separate outcomes:

1. a complete minimal coefficient-height classification of literal integer lifts of the NAND ANF polynomial;
2. an exact seed-target obstruction for the lifted Sheffer operation `s(x,y)=1-xy` from the seed `zeta_5`, obtained from the ramified residue class modulo `lambda=1-zeta_5`;
3. a falsified exploratory claim that `zeta_5` is the only unit in the Sheffer closure, with an explicit constructive counterexample;
4. a finite characteristic-two control showing that the ramified-place obstruction is absent in `F_16`.

No physical, decoder, measure, apparatus, or L2-L6 claim is made.

## 1. Literal minimal integer lifts of the NAND polynomial

Write the Boolean NAND polynomial in algebraic normal form as

\[
N(x,y)=1+xy \in \mathbf F_2[x,y].
\]

This section studies **literal coefficientwise polynomial lifts**

\[
P(x,y)\in\mathbf Z[x,y],\qquad P\bmod 2=N
\]

as an equality in `F_2[x,y]`.

This scope is load-bearing. It is not the larger class of arbitrary integer polynomials that merely induce the same Boolean function on `{0,1}^2`.

For

\[
P=\sum_{a,b\ge 0} c_{ab}x^ay^b,
\]

define coefficient height

\[
H(P):=\max_{a,b}|c_{ab}|.
\]

Two lifts are identified up to global sign when `P ~ -P`.

### Candidate theorem: minimal lift classification

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

This gives four height-one lifts. Quotienting by global sign leaves exactly two classes.

Thus the result is a classification, not a search witness.

## 2. The two minimal classes have the same binary shadow

Modulo two,

\[
R_+(x,y)\equiv R_-(x,y)\equiv1+xy.
\]

Therefore the reduction map from the two global-sign classes of minimal lifts to the NAND polynomial shadow is non-injective.

The binary shadow alone does not determine which of the two minimal coefficientwise lift classes was present before reduction. An additional choice can select a lift, but that choice is not contained in the one-bit polynomial shadow.

This is a narrow one-bit no-go only. It does not say that finer `2^k` information can never distinguish the two classes.

Indeed, at `x=y=1`,

\[
1+xy=2,\qquad 1-xy=0,
\]

so the two values are distinct modulo four.

## 3. Chosen cyclotomic diagonal read

Make the additional, explicitly chosen read

\[
x=y=j,\qquad j=\zeta_5.
\]

For the positive lift,

\[
R_+(j,j)=1+j^2=J,
\]

with

\[
N_{\mathbf Q(j)/\mathbf Q}(J)=\Phi_5(-1)=1.
\]

For the negative lift,

\[
R_-(j,j)=1-j^2=(1-j)(1+j).
\]

Since

\[
N(1+j)=\Phi_5(-1)=1,
\]

`1+j` is a unit, so `1-j^2` is associated to `1-j`, and

\[
N(1-j^2)=\Phi_5(1)=5.
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

This does not derive `J` from NAND, does not select `p=5`, and does not imply that characteristic two generally identifies the TWIST-J axiom with ramification.

For every odd prime `p`, the same elementary cyclotomic contrast `Phi_p(-1)=1`, `Phi_p(1)=p` is available, so this contrast is not a selector of five.

## 4. Lifted Sheffer operation

Now separate the previous coefficient-lift question from a different question.

Define the characteristic-zero lifted Sheffer operation

\[
s(x,y)=1-xy
\]

on

\[
\mathcal O_5=\mathbf Z[\zeta_5].
\]

Let `C_s(a)` denote the smallest subset of `O_5` containing a seed `a` and closed under `s`.

The operation is not associative and has no neutral element. Its Boolean functional completeness does not by itself give a semigroup, ring, or additive-multiplicative algebra structure upstairs.

The relevant question here is therefore not whether Sheffer is functionally complete on bits. It is whether a specified target is reachable from a specified seed under repeated use of the lifted operation.

## 5. General residue-closure lemma

Let `R` be a ring, `I` an ideal, and

\[
\rho:R\to R/I
\]

the quotient homomorphism. For

\[
s(x,y)=1-xy,
\]

one has

\[
\rho(s(x,y))=1-\rho(x)\rho(y)=s(\rho(x),\rho(y)).
\]

Therefore for every seed `a`,

\[
\boxed{\rho(C_s(a))\subseteq C_s(\rho(a)).}
\]

### Consequence

A target `t` is impossible from `a` whenever

\[
\rho(t)\notin C_s(\rho(a)).
\]

This is only a necessary obstruction. If the residue closure contains `rho(t)`, reachability of `t` upstairs remains undecided.

## 6. Complete `F_5` Sheffer-subalgebra classification

Work in `F_5` with

\[
s(a,b)=1-ab.
\]

The complete list of nonempty subsets closed under `s` is

\[
\boxed{\{2\},\qquad\{0,1\},\qquad\mathbf F_5.}
\]

This was independently checked by exhaustive enumeration of all `32` subsets of `F_5`. It also has a direct proof.

### Proof without enumeration

- If a closed set contains `0`, then `s(0,0)=1`, so it contains `{0,1}`.
- If such a set contains any additional element `2`, `3`, or `4`, repeated application of `s` generates all of `F_5`.
- If a nonempty closed set does not contain `0`, it cannot contain `1` because `s(1,1)=0`, and it cannot contain `4` because `s(4,4)=0`.
- If it contains `3`, then `s(3,3)=2` and `s(3,2)=0`, contradiction.
- The only remaining possibility is `{2}`, and indeed `s(2,2)=2`.

Hence exactly the three displayed closed subsets occur.

Equivalently, singleton seed closures are

\[
\begin{array}{c|c}
\text{seed}&C_s(\text{seed})\\
\hline
0&\{0,1\}\\
1&\{0,1\}\\
2&\{2\}\\
3&\mathbf F_5\\
4&\mathbf F_5.
\end{array}
\]

## 7. Ramified seed-target barrier for `zeta_5`

Let

\[
\lambda=1-\zeta_5.
\]

Then

\[
\mathcal O_5/(\lambda)\cong\mathbf F_5,
\qquad
\zeta_5\mapsto1.
\]

By the residue-closure lemma and the `F_5` classification,

\[
C_s(\zeta_5)\bmod\lambda\subseteq\{0,1\}.
\]

In fact both residues occur because the seed has residue `1` and

\[
s(\zeta_5,\zeta_5)=1-\zeta_5^2\equiv0\pmod\lambda.
\]

Therefore

\[
\boxed{C_s(\zeta_5)\bmod\lambda=\{0,1\}.}
\]

Now

\[
J=1+\zeta_5^2\equiv2\pmod\lambda,
\]

while

\[
\phi=-\zeta_5^2-\zeta_5^3\equiv-2\equiv3\pmod5.
\]

Since neither `2` nor `3` lies in `{0,1}`,

\[
\boxed{J\notin C_s(\zeta_5),\qquad \phi\notin C_s(\zeta_5).}
\]

This is an all-depth exact seed-target separation. No coefficient bound, search depth, norm census, or limiting argument enters the proof.

The first Sheffer step lands in the ramified ideal:

\[
s(\zeta_5,\zeta_5)=1-\zeta_5^2=(1-\zeta_5)(1+\zeta_5),
\]

so its residue is `0` modulo `lambda` and its norm is `5`.

The correct interpretation is narrow:

> From the seed `zeta_5`, the lifted Sheffer operation cannot reach `J` or `phi` because seed and targets lie in different `s`-invariant residue classes modulo `lambda`.

This is a theorem about the pair `seed + target`, not a theorem that the Sheffer operation is globally algebraically insufficient.

## 8. Uniform odd-prime form

For any odd prime `p`, set

\[
\zeta=\zeta_p,\qquad \lambda_p=1-\zeta.
\]

Then

\[
\mathbf Z[\zeta_p]/(\lambda_p)\cong\mathbf F_p,
\qquad \zeta\mapsto1.
\]

The set `{0,1}` is closed under `s(a,b)=1-ab` in every residue characteristic. Therefore the Sheffer closure of the seed `zeta` has residue contained in `{0,1}` modulo `lambda_p`, while

\[
1+\zeta^2\equiv2\pmod{\lambda_p}.
\]

For odd `p`, `2` is distinct from `0` and `1`, so

\[
1+\zeta_p^2\notin C_s(\zeta_p).
\]

Thus the residue obstruction is uniform over odd primes and does not select `p=5`.

## 9. Falsified exploratory route: unique unit in the closure

An earlier exploratory claim was:

> `zeta_5` is the only norm-one unit in `C_s(zeta_5)`.

This claim is **FALSIFIED** in this incubation. It is not silently repaired and is not a public Registry `F` row.

A constructive counterexample is

\[
\phi^{-4}=5+3\zeta_5^2+3\zeta_5^3,
\qquad
N(\phi^{-4})=1.
\]

Using `z=\zeta_5` and `s(x,y)=1-xy`, define

\[
u=s(z,z),
\]

\[
v=s(z,u),
\]

\[
b=s(z,v),
\]

\[
c=s(u,b),
\]

\[
a=s(z,c).
\]

In the basis `(1,z,z^2,z^3)` these are

```text
u = ( 1, 0,-1, 0)
v = ( 1,-1, 0, 1)
b = ( 2, 0, 2, 1) = 2 + 2 z^2 + z^3
c = (-2,-2,-2,-3)
a = (-2,-1,-1,-1) = -2 - z - z^2 - z^3
```

and the final step is

\[
\boxed{s(a,b)=5+3z^2+3z^3=\phi^{-4}.}
\]

Hence a second unit appears at the next closure level under the convention

\[
C_{d+1}=C_d\cup s(C_d,C_d).
\]

The unrestricted closure sizes through that stage are

```text
1, 2, 4, 11, 67, 2273
```

for `C_0` through `C_5`; the displayed final `s(a,b)` lies one application beyond the operands `a,b` and therefore supplies the explicit deeper witness.

The failed norm argument is therefore replaced, not patched, by the residue-subalgebra invariant. This replacement is structurally stronger because

\[
\phi^{-4}\equiv1\pmod\lambda
\]

is permitted by the barrier, whereas

\[
J\equiv2,\qquad\phi\equiv3
\]

are excluded regardless of how many further units the closure contains.

## 10. Characteristic-two control

At the prime `2`,

\[
\mathcal O_5/(2)\cong\mathbf F_{16}.
\]

In characteristic two,

\[
1-xy=1+xy.
\]

A finite exhaustive closure calculation starting from the residue class of `zeta_5` gives all `16` elements of `F_16`.

Within this finite control,

\[
J\bmod2=1+\zeta_5^2=s(\zeta_5,\zeta_5)
\]

is present immediately, and

\[
\phi\bmod2=\zeta_5^2+\zeta_5^3
\]

also lies in the closure.

This control is recorded at computation-grade incubation scope only. No public status is claimed here.

Its role is to delimit the ramified-place theorem: the `lambda` obstruction above is an odd-prime ramified residue obstruction. It is absent in the characteristic-two `F_16` control because the sign distinction collapses and the seed closure is the whole finite field.

This does not make the prime `2` a physical selector and does not strengthen any public two-place dictionary.

## 11. Relation to Public Canon v72

Public Canon v72 is the active public authority. This note changes none of its
claims. The note was written against v69; the four contextual rows below are
byte-identical in the v69 and v72 registries, so the relation is restated at
v72 with no change of content.

Relevant existing public rows are contextual only:

- `CARRY-QUADRATIC-SYMMETRY [T]` classifies the permutation-invariant pure quadratic Boolean form and explicitly states that five is an output cardinality, not a selected rational prime.
- `CARRY-PENTAD [T]` gives the five-point singular set and its `O^-(4,2) ~= S_5` symmetry, while explicitly selecting no cycle, orientation, exponent, `J`, or physical reading.
- `J-BINARY-NORM-DESCENT [T]` gives `O_5/(2) ~= F_16` and `O_(Q(phi))/(2) ~= F_4`, with no uniqueness of `J`, `2`, `5`, or order five.
- `RAMIFIED-TM-LIFT [T]` gives the separate ramified `F_5` lift and universal carry identity, without asserting the present Sheffer seed-target theorem.

The present note does not strengthen, merge, or reinterpret those rows.

## 12. Scientific ledger inside this incubation

The current local accounting is:

```text
candidate-T  literal minimal coefficient-height NAND lift classification
candidate-T  residue-closure lemma rho(C_s(a)) subseteq C_s(rho(a))
candidate-T  complete nonempty s-closed subset classification in F_5
candidate-T  C_s(zeta_5) mod lambda = {0,1}; hence J and phi are unreachable
FALSIFIED    "zeta_5 is the only unit in C_s(zeta_5)"
             witness phi^-4 = 5 + 3 zeta_5^2 + 3 zeta_5^3
candidate-C  F_16 closure control: seed zeta_5 generates all 16 elements under s
OPEN         reachability of J from lifted Sheffer seeds whose mod-lambda residue is 3 or 4
```

The word `FALSIFIED` above records the disposition of an exploratory candidate only. It is not a public Canon `F` status.

## 13. Falsifiers and boundaries

The minimal-lift classification fails if there exists a literal coefficientwise integer polynomial `P` with

\[
H(P)=1,
\qquad
P\bmod2=1+xy
\]

that is not one of `+-1 +- xy`.

The `F_5` classification fails if a nonempty proper `s`-closed subset exists other than `{2}` or `{0,1}`.

The seed-target theorem fails if an exact Sheffer expression in the single seed `zeta_5` evaluates in `Z[zeta_5]` to `J` or to `phi`, or if the quotient-homomorphism induction is wrong.

A seed whose residue is `3` or `4` modulo `lambda` does not falsify the theorem; it lies outside the frozen seed scope. Failure of the residue obstruction to decide such a seed is an acknowledged open reachability question.

The finite `F_16` control is falsified by an exact exhaustive closure different from all `16` field elements.

No statement here selects `p=5`, derives the TWIST-J axiom, derives `phi`, supplies a decoder, or moves any L2-L6 claim.
