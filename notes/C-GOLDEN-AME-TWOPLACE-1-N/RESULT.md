# C-GOLDEN-AME-TWOPLACE-1-N — result

Status: **NON-CANONICAL, exact scoped negative**

Decision: **hard falsifier G4 fired**

Canon change: **none**

`PROMO.md`: **not created**

## Verdict

The coefficient-level two-place connection is exact, but the preregistered
six-line structural bridge is false.

The golden AME matrix has minimal entry field

```text
Q(all entries of U) = Q(zeta_40) = Q(zeta_5,zeta_8).
```

Separately, the six frozen golden lines carry the expected ambient rotational
action

```text
Gamma_line = A5 = 2I/{+I,-I}.
```

These two positive L1 facts do not combine into the required tensor bridge.
The exact support of the pinned AME tensor forbids the order-five local
permutations that every faithful six-point `A5` action must contain.
Therefore no allowed faithfully embedded diagonal `A5` exists in the
preregistered local monomial class.

This is the null outcome frozen in `PREREG.md`: common `phi`, dimension
six, and the two-place coefficient field do not select a canonical
intertwiner.

## Gate ledger

| Gate | Result | Exact scope |
|---|---|---|
| G0 source integrity | **PASS** | Pinned source, support, values, and exact left/right unitarity of `U`, `U^R`, and `U^Gamma_2` |
| G1 two-place field | **PASS** | Minimal entry field is exactly `Q(zeta_40)=Q(zeta_5,zeta_8)`; coefficient bridge only |
| G2 six-line audit | **PASS** | Rank six, tight frame, centered rank-five simplex, `1+5` moment split, `Gamma_Gram=S6`, ambient `Gamma_line=A5`, and marked comparison with `2I/{±I}` |
| G3 intrinsic symmetries | **DECISIVE SUBCLASS COMPLETE** | Strict simultaneous stabilizer, all 24 leg permutations, and the complete degree-preserving independent support class needed by G4 |
| G4 common-action breaker | **FALSIFIER FIRED** | No faithful local six-point `A5` in the frozen monomial class |
| G5 intertwiner/canonicity | **NOT EXECUTED** | Its required common action is empty after G4 |
| G6 gauge robustness | **NEGATIVE OBSTRUCTION INVARIANT** | Per-leg support-degree multisets are unchanged by every allowed local monomial gauge |
| G7 output | **COMPLETE** | Exact scoped negative; no promotion package |

The unneeded remainder of the full G3 stabilizer classification was not
computed after the preregistered hard falsifier fired.

## G0 — exact source reproduction

The sole input is the pinned 8515-byte `AME46_ORIGINAL.m` named in
`SOURCE.md`. Its parser found

```text
112 nonzero entries = 40 a + 40 b + 32 c,
active zeta_20 exponents 0 through 19.
```

All arithmetic was performed in

```text
Q[x]/(Phi_40(x)),
Phi_40(x) = x^16 - x^12 + x^8 - x^4 + 1.
```

The six exact Gram products for the rows and columns of `U`, `U^R`, and
`U^Gamma_2` each had zero residual entries. This reproduces the published
2-unitarity / AME(4,6) construction; it is not a new TWIST-J theorem.

## G1 — the positive coefficient theorem

Write `w=zeta_20`. Two actual entries of the pinned matrix are

```text
U[1,2] = c,
U[2,3] = c w^17
```

in one-based mathematical indexing. Since `17*13 = 1 mod 20`,

```text
w = (U[2,3]/U[1,2])^13.
```

The same entry field then contains

```text
zeta_40 = c (1+w^5) w^-2.
```

Conversely,

```text
w = zeta_40^2,
c = (zeta_40^5 + zeta_40^-5)/2,
a = c/(w+w^-1),
b = (w^2+w^-2)a,
```

so every matrix entry belongs to `Q(zeta_40)`. These inclusions prove
minimality, not merely containment. The degree is 16.

The two Canon places generate the same field by the explicit identities

```text
zeta_5 = zeta_40^8,
zeta_8 = zeta_40^5,
zeta_40 = zeta_5^2 zeta_8^-3,
```

where `2*8-3*5=1`. The preregistered coefficient relations also pass:

```text
w   = (T_pl/2)^7,
a^2 = (3-phi)/10 = s_J^2/10,
b^2 = (2+phi)/10,
b/a = phi,
c^2 = 1/2.
```

**[candidate-T, NON-CANONICAL, L1 only]** The pinned golden AME
representative has exactly the TWIST-J two-place compositum as its entry
field. This statement supplies no carrier, action, decoder, Born rule, or
physical lift.

## G2 — the six-line side

For the six frozen projectors `P_i`,

```text
rank{P_i} = 6,
sum_i P_i = 2 I_3,
Tr(P_i P_j) = 1       if i=j,
              1/5     if i!=j.
```

For `Q_i=P_i-I_3/3`,

```text
sum_i Q_i = 0,
Tr(Q_i^2) = 2/3,
Tr(Q_i Q_j) = -2/15  for i!=j.
```

Thus the centered projectors form a regular simplex of rank five and the
moment operator has exact spectrum

```text
(1/3)^1, (2/15)^5.
```

The abstract Gram symmetry is all of `S6`, order 720. It must not be
confused with the ambient geometry. Complete exact enumeration of the
ambient `SO(3,Q(phi))` realizations gives 60 rotations with cycle counts

```text
1 identity,
15 of type (2,2,1,1),
20 of type (3,3),
24 of type (5,1).
```

This group is faithfully conjugate to the Möbius action of
`PSL_2(F_5)=2I/{±I}` on `P^1(F_5)`. There are 120 unmarked group
comparisons. The public marked `T` trace splits them into 60 correct and 60
outer-twisted comparisons; the remaining 60 differ by inner conjugation.

## G3/G4 — exact killer

Let `S` be the support of the four-index tensor and define

```text
d_q(r) = number of x in S with x_q=r.
```

The pinned support gives

```text
leg 0: (20,18,16,24,16,18)
leg 1: (14,14,22,20,20,22)
leg 2: (20,20,18,18,18,18)
leg 3: (18,18,18,18,20,20).
```

The largest equal-degree classes therefore have sizes

```text
(2,2,4,4).
```

Any local monomial tensor symmetry permutes support without cancellation.
When its tensor-leg permutation is the identity, its local permutation
`p_q` must preserve `d_q`.

Now choose any order-five element of the required six-point `A5`. On every
local six-point carrier it has cycle type `(5,1)`. Its image on the four
tensor legs is the identity because `S4` has no element of order five
(equivalently every homomorphism `A5 -> S4` is trivial). Hence its local
five-cycle would require five symbols with equal `d_q` on every leg. No leg
has such a degree class. Contradiction.

This proof fires before phases are considered. Diagonal `mu_40` phases
cannot alter support. It is also stable under the allowed local monomial
gauge, which only permutes each degree vector and leaves its multiplicities
unchanged.

Two finite checks strengthen the certificate:

1. all `720*24` simultaneous `S6` permutations and tensor-leg
   permutations have only the identity projective stabilizer;
2. among all `4*8*48*48=73728` independent degree-preserving local tuples,
   only the identity and
   `(id,id,(01)(23)(45),(01)(23)(45))` preserve support and amplitude
   labels. The latter has no `mu_40` phase lift: modulo five its phase
   system has coefficient rank 21 and augmented rank 22. A four-row left-null
   certificate is printed in `EXPECTED_G3_G4.txt`.

**[exact F, NON-CANONICAL, scoped]** The pinned golden AME tensor and every
representative in its allowed local monomial gauge class admit no common
faithful six-line `A5` action of the preregistered type.

## Boundary of the negative result

This result does not refute:

- the published AME(4,6) construction or its 2-unitarity;
- the Ball-Simoens entanglement-necessity theorem;
- the exact two-place coefficient identity;
- the separate golden-line `A5` theorem; or
- every conceivable relation between AME(4,6) and TWIST-J.

It refutes exactly the finite monomial bridge class frozen before execution.
Arbitrary local unitaries, a different spinor carrier, or a new bridge class
would be a new incubation with a new preregistration, not a repair of this
result.
