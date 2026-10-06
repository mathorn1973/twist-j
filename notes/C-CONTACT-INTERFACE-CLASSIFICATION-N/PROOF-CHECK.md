# Independent analytical check: contact interface classification

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.

This is an independent analytical derivation from the complete frozen
`PREREG.md`, SHA-256
`594b871504191af2b1f3d9ab70ca1398032bad6b767ab1c85e6e92a864790f6b`,
at commit `b2ec1f81459829c2541ca38c59acd45c63e9f4fb`, and its pinned Canon
source. Neither `verify.py` nor `break.py` was read or executed for this
derivation. No finite census was executed. It does not yet certify a
separately authored `PROOF.md`; an exact proof-review pin belongs in a later
section after that file is supplied.

## 1. Full carrier and faithful control classification

Let `S=F5^12` and `X=S times {0,1}`. On the piston matrices, native `b`
is left multiplication by the negative row-exchange matrix, whose
determinant is -1. Applying it to both matrices therefore gives
`h(I s)=-h(s)`. Direct substitution in the complete native formulas gives
`b^2=d^2=e^2=id`, `e_i d_i=tau_i`, `d_i e_i=tau_i^-1`, and
`I tau_i I=tau_i^-1`: tau_i fixes every coordinate except q_i, which it
increments by one. These are complete-state identities.

Each I-orbit in S is preserved setwise by every W. On a nonzero pair
`h in {k,-k}`, use `h=(-1)^u k` and labels `2u+eta`. The control sends

    (u,eta) -> (u xor a(h,eta), beta(h,eta)).

There is one independently chosen output label for each of the four input
labels. Thus admissibility is exactly an arbitrary permutation `w_k in S4`.
The same permutation acts on every I-orbit having this h pair.

On a free I-orbit at h=0, the same formula holds, but a and beta depend
only on eta. It is bijective exactly when beta is a permutation of the
two bits; a(0,0) and a(0,1) are otherwise arbitrary. There are
`2*2^2=8` such controls. They form the centralizer of
`J=(02)(13)`, the operation that exchanges the actual I position.
In particular W is not required to be identity on this branch.

There are also I-fixed states: in each cell the second piston row is
the negative first row and q=r=0. There are `5^4=625` paired fixed states,
all with h=0. On these states W acts by the same bit permutation beta,
so it is bijective there as well. This covers the fixed states; they are
not deleted by a free-orbit quotient.

Conversely, free orbits exist on every h sheet. The preregistered piston
witness has `Xp=(1,0,0,0)` and `Yp=(0,0,0,2h)`, and I changes its
pistons even at h=0. It proves both necessity of the finite permutation
conditions and faithfulness of literal ten-digit table equality: a
different beta changes the bit, and a different a changes the data on
this witness. Therefore distinct admitted tables are distinct complete
W maps, even when their only difference is at h=0.

The complete class has size `8*24^2=4608`. W is involutive exactly when
both nonzero permutations are involutions and the zero-branch control
is involutive. S4 has `1+6+3=10` involutions. On the zero branch, beta=id
permits all four a choices; beta=bit-flip permits exactly the two choices
with a(0,0)=a(0,1). Hence the involutive class has `6*10^2=600` elements.

The inverse requires no extra state. At h=0 first set
`eta=beta^-1(eta')`, then `s=I^a(0,eta) s'`. At nonzero h', let
`(u,eta)=w_k^-1(u',eta')`, where `h'=(-1)^u' k`; then
`s=I^(u xor u') s'`. This gives a total inverse of the declared table
form on all X.

## 2. Conjugate involutions and complete contact laws

At h=0, the table dependence implies `W I=I W`, so `E_W=I` there,
including I-fixed states. On each nonzero pair, E is conjugate to J
in S4. Its only possibilities are

| E permutation | Complete action | Arbitrary w preimages | Involutive w preimages |
|---|---|---:|---:|
| `J=(02)(13)` | `(s,eta)->(I s,eta)` | 8 | 6 |
| `H=(01)(23)` | `(s,eta)->(s,eta xor 1)` | 8 | 2 |
| `D=(03)(12)` | `(s,eta)->(I s,eta xor 1)` | 8 | 2 |

The arbitrary counts follow from the centralizer size eight. For the
involutive counts, identity, the three double transpositions, and the
two transpositions (02),(13) centralize J. Of the four remaining
transpositions, (03),(12) send J to H, and (01),(23) send J to D.
Thus the displayed list is exhaustive without an enumeration program.

Consequently there are exactly nine complete E maps. Each has 512
arbitrary W preimages. The involutive W preimage count of a pair of
E types is six times the product of the two entries in the last column.
Globally every E can be written

    E(s,eta)=(I^chi(h) s, eta xor c(h)),

where chi and c are even binary functions, `(chi(0),c(0))=(1,0)`, and
at each nonzero h pair their values are `(1,0)`, `(0,1)`, or `(1,1)`.
These formulas hold at arbitrary occupied eta and arbitrary q,r.

Since h is tau-invariant and chi,c are even,

    E tau_i E = tau_i^((-1)^chi(h)),
    K_(W,i)   = tau_i^(3 chi(h)).

This is a full-carrier conjugation calculation, not a claim that tau_i
preserves any initial complete I-orbit. It proves that pistons, both r,
eta, and q_other are restored exactly. The only endpoint change is
`q_i -> q_i+3 chi(h)`, independently of the occupied bit. Its inverse is
`q_i -> q_i-3 chi(h)`, with every other coordinate fixed.
In particular a state initially fixed by I causes no exception: tau_i
can move it out of that fixed locus, but both I/tau conjugations are
still the same complete-state identities on h=0.

Write a=chi(1), b=chi(2). The unique even polynomial of degree at most
four representing the law is

    chi(h)=1+2(b-a)h^2+(3a-2b-1)h^4.

The three equations at h=0,1,2 uniquely determine these coefficients.
All four binary profiles occur, with the following complete fibres:

| Profile ab | Coefficients `[1,h2,h4]` | All W | Involutive W |
|---|---|---:|---:|
| 00 | `[1,0,4]` | 512 | 24 |
| 01 | `[1,2,2]` | 1024 | 96 |
| 10 | `[1,3,2]` | 1024 | 96 |
| 11 | `[1,0,0]` | 2048 | 384 |

For arbitrary W a nonzero zero-response pair has eight choices (H),
and a one-response pair has sixteen choices (J or D), multiplied by the
eight zero-branch choices. For involutive W the corresponding factors
are two and eight, multiplied by six. The fibres sum to 4608 and 600.
Different profiles are different full maps because every h occurs and
translation by three is nonidentity on F5.

Explicit involutive witnesses, in the preregistered ten-digit order, are

| Profile | W table |
|---|---|
| 00 | `0102023131` |
| 01 | `0102010131` |
| 10 | `0101023101` |
| 11 | `0101010101` |

These take W=id at h=0. At a nonzero pair with chi=1 they also take
W=id; at a pair with chi=0 they swap u and eta, equivalently
`a=u xor eta`, `beta=u`. This specification uses only the original
marked h,eta coordinates; u is the fixed sign label of the h pair.
The existing v100 W_b is exactly the 00 witness. Its embedding is a
regression fact about the supplied interface, not an independent
confirmation of the sealed theorem or selection of that law.

## 3. Reader tables, complete endpoints and the involutive subclass

Put `a_q=P_q(0)`. The ready contract is equivalent to
`P_q(1)=a_(q+2)`. Therefore a_q and a_(q+2) must be distinct, and
P_q(2) is the remaining active label. Admitted tables are in bijection
with proper three-colorings of the five-cycle whose edges advance q
by two. Each color appears at most twice, so the multiplicities are
exactly (2,2,1). Choose the singleton position (five choices), its
color (three choices), and the order of the other two colors on the
remaining path (two choices). This proves the total `5*3*2=30`.

A useful complete normal form is the pointwise-involutive table

    Q_0=(210,102,102,021,012),
    Q_j(q)=Q_0(q-j).

The five entries are in numerical q order; each three-digit entry
lists the images of r=0,1,2. Every admitted table is uniquely
`P_q=L Q_j(q)` for a global `L in S3` and a unique singleton position
`j in F5`. Relabeling the colors in a proper coloring proves existence;
its singleton position and all three attained colors prove uniqueness.
The supplied v100 table is Q_2.

Each Q_j consists of the identity and all three transpositions, with
(01) occurring twice. If every L Q_j(q) is involutive, the identity
entry first forces L to be an involution. Any nonidentity such L is a
transposition; multiplication by a different transposition appearing
in Q_j yields a three-cycle. Thus only L=id works. There are exactly
five pointwise-involutive tables, the five translates Q_j. This property
is not invariant under internal relabeling: for the supplied table,
`L=(01)` makes `L P_0=(01)(12)=(012)`.

Let `D_q=P_(q+3)^-1 P_q` on the active reference subset. Then D_q(0)=1,
so D_q is either `T=102=(01)` or `Z=120=(012)`. More precisely,

    D_q=T  iff a_(q+2)=a_(q+3)
           iff q=j-1 or q=j+1;
    D_q=Z  otherwise.

The second equivalence follows because each doubled color occupies an
adjacent pair in numerical q, and the two pairs left by singleton j
are `{j-2,j-1}` and `{j+1,j+2}`. The complete endpoint is

    R_j(q,r)=(q+3,D_q(r))  for r in {0,1,2},

with r=3,4 fixed, and every other native coordinate fixed. On occupied
r=1, T writes 0 whereas Z writes 2; on occupied r=2, T writes 2 whereas
Z writes 0. These occupied actions are part of the classification.
For Q_2 the frozen endpoint signature is `120102120102120`.

There are exactly five distinct complete endpoints, one per j. Each
has six literal-table preimages. One direct proof, independent of the
normal form, is that equal D_q imply

    P'_q P_q^-1=P'_(q+3) P_(q+3)^-1.

Since addition by three visits all five q values, this is one constant
L. Conversely a constant left L cancels from every D_q. Thus complete
endpoint equality is exactly global left-S3 table equivalence, including
all occupied native reference values; it is not literal table equality.

## 4. Frozen relabeling orbits and stabilizers

In the normal form (L,j), q translation t acts as `(L,j-t)` and internal
relabeling M acts as `(M L,j)`. At the actual endpoint level, with
`Q_t(q,r)=(q+t,r)`, the translated table satisfies
`R_(P translated by t)=Q_-t R_P Q_t`. No reversal or rescaling of q
has been used, and no external ready/output labels are exchanged.

| Object and acting group | Number of orbits | Orbit size | Stabilizer |
|---|---:|---:|---|
| All 30 tables; q translations C5 | 6 | 5 | identity |
| All 30 tables; internal S3 | 5 | 6 | identity |
| All 30 tables; C5 times S3 | 1 | 30 | identity |
| Five involutive tables; C5 | 1 | 5 | identity |
| Five endpoints; C5 | 1 | 5 | identity |
| Five endpoints; internal S3 | 5 | 1 | all S3 |
| Five endpoints; C5 times S3 | 1 | 5 | `{0} times S3` |

The normal form proves every entry and also shows that each endpoint
fibre contains exactly one pointwise-involutive table. The involutive
subset is not an S3-set under the frozen left action; no internal
relabeling orbit of that subset is asserted. The actions are algebraic
relations, with no physical-equivalence claim.

## 5. Every contact/reader pair, inverses and limits

For any admitted W and reader P, put `s=3 chi(h)`; h is unchanged by
the full contact and both couplings. Then on all X

    C_P^-1 K_(W,i) C_P:
        q_i' = q_i+s,
        r_i' = P_(q_i+s)^-1 P_(q_i)(r_i),

and every other coordinate is restored. The inverse is

    q_i = q_i'-s,
    r_i = P_(q_i'-s)^-1 P_(q_i')(r_i').

On chi=0 this is identity. On chi=1 it is the R_j endpoint above;
its inverse uses `D_(q_i'-3)^-1`, where `T^-1=T` and `Z^-1=201`.
Native r=3,4 remain fixed in either direction. This proves the occupied
reference continuation and inverse without using pointwise involutivity
of P or cleanliness of eta.

There are twenty different complete paired endpoints, indexed by
(profile,j). Their j values are distinguishable on the always-active
h=0 sheet with occupied r; their profiles are distinguishable by the
q shift on h=1 or h=2. For a fixed (profile,j), the number of literal
(W,P) pairs is six times that profile's W count. Restricting P to be
pointwise involutive replaces six by one; restricting W replaces its
count by the involutive-W count in Section 2.

On a separately prepared reference r_i=0, every P writes exactly
`r_i'=chi(h)`, independently of unknown q_i and occupied eta. Thus there
are four prepared output profiles, and all thirty reader tables give
the same prepared output for a fixed contact law. They cannot be
distinguished by the frozen ready-reference queries alone.

Exactly two fixed queries are necessary and sufficient to distinguish
all four laws in the preregistered query class. A query at h=1 reads a,
and a separate query at h=2 reads b. One query has at most two possible
marked reference outputs (at h=0 only one), so it cannot identify four
profiles. This counts only the declared independently ready references;
it supplies no apparatus, preparation or reset mechanism.

Every active full reader is conjugate to tau_i^3 and has order five;
the inactive branch is identity. Repetition therefore does not retain
a permanent archive. Indeed, after two active uses from ready zero,
`r_i''=P_(q_i+1)^-1 P_(q_i)(0)`, which is zero exactly when
`a_q=a_(q+1)`. Every admissible coloring has two such q values. Thus
every reader can erase its first ready record on its second use.
Inverse execution restores q as well as r, and a zero endpoint alone
does not distinguish a completed inactive experiment from no experiment.

All classifications above are conditional on the declared h, I, table
dependence, bijectivity, pointwise reference coupling and marked query
contract. They neither derive those premises from J nor classify the
complete native or physical apparatus family. Equality of contact or
reader endpoints says nothing about equality of W prefixes, a compiled
T_alg word, its q lift, autonomous execution, physical occurrence or
any cross-layer interpretation. No Canon, registry, frontier or existing
sealed probe status changes follow.
