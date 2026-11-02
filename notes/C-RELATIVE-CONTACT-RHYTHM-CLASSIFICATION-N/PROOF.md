# Classification of the declared three-slot contact rhythms

**Status: NON-CANONICAL / L1 / candidate-T.** This is a proposed mathematical
derivation for a supplied contact and a supplied contact order. Finite census
assertions are identified separately below. This document does not amend the
Canon, establish a native-U derivation, identify the trace account with measured
energy, or construct a contact measuring apparatus.

The contact is the one defined in the Canon under **Integral relative contact
on the declared Cartesian carrier**. All definitions needed here are repeated
to make the argument self-contained. The proofs use exact algebra; the finite
computations audit their stated instances. No blind preregistration or formal
independence is claimed for their discovery.

## 1. Carrier, contact and accounts

Let
\[
O=\mathbb Z[j],\qquad 1+j+j^2+j^3+j^4=0,\qquad \rho=j^2.
\]
Use the marked basis \((1,j,j^2,j^3)\). For \(z=\sum_{i=0}^3z_i j^i\), set
\[
Q(z)=\frac{5\sum_i z_i^2-(\sum_i z_i)^2}{2}.
\]
This is the Canon's trace account \(q\), written with a capital letter to
distinguish it from the depth below. It is integer valued. Appending \(z_4=0\)
gives the exact identity
\[
2Q(z)=\sum_{0\le i<k\le4}(z_i-z_k)^2. \tag{1}
\]
Thus \(Q(z)=0\) exactly when \(z=0\). If \(z\ne0\), separate the \(k\)
occurrences of the lowest of the five coefficients from the remaining \(5-k\).
At least \(k(5-k)\ge4\) terms in (1) are at least one, so \(Q(z)\ge2\).
Bounded sublevel sets are finite. Multiplication by \(\rho\) preserves \(Q\):
in the five-coefficient presentation it is a cyclic shift followed by
subtraction of one common coefficient, both preserving (1).

The total contact on a labelled pair is
\[
C(a,b)=
\begin{cases}
(s+\rho t,s-\rho t),&a-b\in2O,\quad
s=(a+b)/2,\quad t=(a-b)/2,\\
(a,b),&a-b\notin2O.
\end{cases} \tag{2}
\]
All divisions in the admitted branch are integral. A refusal is an identity;
an admitted pair with \(a=b\) is also an identity, but **is not a refusal**.
Identity on the refused complement is supplied model data.

On \(O^3\), write \(A=C_{12}\), \(B=C_{23}\), and \(F=BA\): the left contact
acts first. For \(x=(a,b,c)\), put
\[
S(x)=a+b+c,\qquad E(x)=Q(a)+Q(b)+Q(c),
\]
\[
M(x)=Q(a-b)+Q(b-c)+Q(a-c)=3E(x)-Q(S(x)). \tag{3}
\]
Each contact preserves \(S\) and \(E\), by its center-relative form and the
parallelogram identity for \(Q\). Equation (3) proves conservation of \(M\).
Each contact satisfies \(C^5=I\): an admitted difference remains admitted
and is multiplied by \(\rho\), while a refused pair stays fixed. Consequently
\(F\) is a bijection preserving a finite \(E\)-level. Every trajectory is a
finite cycle, with no transient segment.

Let \(r(x)\in\{0,1,2\}\) count refusals during one tick, testing the right
contact on the state **after** the left contact. For a least cycle of length
\(P\), let \(R=\sum_{n=0}^{P-1}r(F^n x)\).

## 2. Parity field and exact first return

Modulo two, \(\Phi_5(X)=X^4+X^3+X^2+X+1\) has no linear root and is not
divisible by the only irreducible quadratic \(X^2+X+1\). It is therefore
irreducible, and \(O/2O\) is a field of sixteen elements. The residue of
\(\rho\) has exact order five. Thus \(1-\rho^k\) is invertible modulo two
for \(k=1,2,3,4\).

**First-return lemma.** For every \(y\in O^3\),
\[
\tau(y)=1+4r(y),\qquad F^{\tau(y)}(2y)=2F(y). \tag{4}
\]
The time \(\tau(y)\) is the first positive return of \(2y\) to \((2O)^3\)
at a whole-tick boundary. Exactly \(4r(y)\) refusals occur in this upper
return segment.

**Proof.** An admitted lower contact lifts in one upper contact to exactly
twice its lower output, still in the even sublattice. This includes an
admitted identity.

For a refused lower pair \((a,b)\), write \(\delta=a-b\notin2O\).
After \(k\) contacts on its doubled pair, its two entries are
\[
a+b+\rho^k\delta,\qquad a+b-\rho^k\delta. \tag{5}
\]
For \(k=1,2,3,4\), both have the same nonzero residue
\((1+\rho^k)\delta\) modulo two. The untouched third entry is even.
Hence the neighboring contact refuses at each intervening opportunity.
The fifth contact on the active pair restores \((2a,2b)\) exactly.

The complete tick order gives four cases:

| Lower left/right decisions | Upper whole ticks | Upper refusals |
|---|---:|---:|
| admitted / admitted | 1 | 0 |
| refused / admitted | 5 | 4 |
| admitted / refused | 5 | 4 |
| refused / refused | 9 | 8 |

In the second row, the first four right contacts refuse; the fifth left
contact restores the doubled lower input, and the right contact performs
the admitted lower action. In the third row, the admitted left action occurs
first, the right pair starts its five-cycle, and the next four left contacts
refuse. In the fourth row the fifth left contact and the first right contact
share the fifth whole tick. Four further right contacts complete the second
five-cycle. This is nine ticks, not ten.

Every inserted intermediate whole-tick state has exactly two slots with
nonzero parity and one even slot. There is no earlier even return. The
endpoints and refusal counts in all four rows prove (4). \(\square\)

**Least-period lifting.** If the lower cycle has least period \(P\) and
refusal count \(R\), its doubled cycle has
\[
P'=P+4R,\qquad R'=4R. \tag{6}
\]
Its even return states are exactly
\(2y,2F(y),\ldots,2F^{P-1}(y)\), in that cyclic order. The sum of their
first-return times is \(P+4R\). A shorter return to \(2y\) would itself be
an even return and imply a shorter lower cycle. The same decomposition
counts exactly \(4R\) upper refusals. This proves (6) also for fixed lower
states; no nontrivial-motion assumption is needed. Iteration gives
\[
R_d=4^dR_0,\qquad P_d=P_0+\frac{4R_0(4^d-1)}3. \tag{7}
\]
The inserted five-cycles belong to the doubled trajectory. Equation (4) does
not insert unprescribed microsteps into the original refused identity.

## 3. Avoiding the simultaneous parity section

Define
\[
H=\{(a,b,c):a-b\in2O,\ b-c\in2O\}.
\]
Membership is tested at whole-tick boundaries. In difference coordinates
\(u=a-b,\ v=b-c\), the admitted actions are
\[
A(u,v)=(\rho u,v+(1-\rho)u/2),\qquad
B(u,v)=(u+(1-\rho)v/2,\rho v). \tag{8}
\]

**No-H lemma and bounded search.** A cycle disjoint from \(H\) has least
period one or five. From any state outside \(H\), either its complete
one- or five-cycle is recognized, or a state in \(H\) occurs within eight
ticks. Eight is sharp.

**Proof.** If both differences are non-even, both contacts refuse and the
state is fixed. The state is also fixed when its sole even difference is zero.

If only \(v\) is even and nonzero, the left contact refuses. Under successive
right contacts,
\[
v_k=\rho^k v,\qquad u_k=u+(1-\rho^k)v/2.
\]
Either \(u_k\) becomes even for some \(1\le k\le4\), reaching \(H\) at the
end of that tick, or the five right contacts close the original cycle.
A first entry into \(H\) cannot occur at \(k=5\), because the original
non-even \(u\) has then returned.

If only \(u\) is even and nonzero, the same argument applies to successive
left contacts while the right one refuses. Either they close a five-cycle,
or within four left contacts the intermediate state lies in \(H\). If the
following right contact retains \(H\), the required whole-tick boundary
has already been found.

Otherwise that right contact leaves \(H\). Its input difference \(v_*\)
then has exact common two-adic valuation one: the even left difference is
changed by \((1-\rho)v_*/2\), which is non-even precisely in that case.
After \(k=1,2,3,4\) right contacts from this intermediate \(H\)-state,
the left difference is changed by \((1-\rho^k)v_*/2\) and is non-even.
All intervening left contacts therefore refuse. The fifth right contact
returns to that same intermediate \(H\)-state, now at a whole-tick boundary.
At most four additional ticks were needed, giving the bound eight. \(\square\)

For sharpness, take
\[
x_0=(1+\rho,1-\rho,-2),\qquad (u_0,v_0)=(2\rho,3-\rho).
\]
Its differences at times \(n=0,1,2,3\) are
\((2\rho^{n+1},3-\rho^{n+1})\); at times \(n=4,5,6,7\) they are
\((3-\rho^{n-3},2\rho^{n-3})\). Each of these eight states has exactly
one non-even difference, since \(1-\rho^k\ne0\) modulo two for
\(1\le k\le4\). At time eight the differences are \((2,2)\), and the
sum-zero state is \((2,0,-2)\in H\). These exact formulas give an eight-tick
first hit without relying on a search sample.

## 4. Complete classification by maximal depth

For \(z\in O\), let \(\nu_2(z)\) be the common divisibility exponent of its
four coefficients, with \(\nu_2(0)=\infty\). Set
\[
h(a,b,c)=\min\{\nu_2(a-b),\nu_2(b-c)\},\qquad
d=\max_{0\le n<P}h(F^n x). \tag{9}
\]
The fully diagonal state \((a,a,a)\) is separate:
\(P=1,R=0,M=0,h=d=\infty\). A nondiagonal cycle never reaches the fixed
diagonal, because \(F\) is bijective, and therefore has finite \(d\).

At fixed conserved sum \(S\), center integrally by
\[
T_S(a,b,c)=(3a-S,3b-S,3c-S). \tag{10}
\]
Common translation commutes with each contact. Multiplication by the odd
integer three preserves admission and commutes with its action. Therefore
\(T_SF=FT_S\), with the same refusal sequence. The map is injective on a
fixed-sum slice, so it preserves least period. Its differences are three times
the original differences, preserving \(h\) and \(d\). It is not asserted
to be injective on all of \(O^3\).

On the sum-zero slice, common divisibility of all differences by \(2^e\)
is equivalent to divisibility of all three entries by \(2^e\). The entries
are congruent to a common value, and their zero sum gives three times that
value zero modulo \(2^e\); three is invertible there. In particular \(H\)
is exactly the even sublattice on this slice.

Choose a phase attaining maximal \(d\) and write its centered state as
\(2^d v\), with \(v\in O^3\) and sum zero. The cycle of \(v\) cannot meet
\(H\). If it did, repeated use of the first-return lemma would place its
corresponding \(2^d\)-multiple on the upper cycle with depth at least \(d+1\),
a contradiction.

The no-H lemma gives exactly three nondiagonal primitive types:

| Primitive type | \(P_0\) | \(R_0\) |
|---|---:|---:|
| One refused contact and one admitted diagonal identity | 1 | 1 |
| Both contacts refused | 1 | 2 |
| One active edge cycles while the other always refuses | 5 | 5 |

In the last row the other edge cannot be an admitted diagonal: both differences
would then be even at an intermediate or initial state, and the no-H proof
would force a whole-tick visit to \(H\). A nonzero admitted relative difference
has exact order five, so this row is not a fixed state.

Put \(A_d=(4^{d+1}-1)/3\) for \(d\ge0\). Equation (7) proves
\[
\boxed{(P,R)=(A_d,4^d),\quad(2A_d-1,2\cdot4^d),
\quad(5A_d,5\cdot4^d).} \tag{11}
\]
All three classes are attained. Primitive preparations are \((1,0,0)\),
\((0,1,0)\), and \((1,-1,0)\), respectively; multiply them by \(2^d\).
Their primitive cycles have no \(H\), and the first-return construction
increases maximal depth by exactly one at every doubling. Numerical periods
alone do not identify a class: periods one and five occur in more than one
row/depth combination.

A short exact classifier follows. Center as in (10), seek an even state or
primitive cycle using at most eight ticks, divide an even state by two, and
repeat. Every division reduces the positive relative account by four. This
terminates at a primitive type and computes (11) without enumerating the
potentially long upper cycle. Translation, centering and division are
mathematical coordinate operations, not free apparatus operations or a
physical measurement protocol.

## 5. Sharp relative-account bounds

At a phase of maximal depth, subtract its third entry and divide by \(2^d\):
\[
z=((a-c)/2^d,(b-c)/2^d,0)\in O^3,\qquad M(x)=4^dM(z). \tag{12}
\]
Centering \(z\) produces exactly the primitive centered state above.
Consequently \(z\) has the same primitive type and its cycle avoids \(H\).
Every nondiagonal triple has at least two nonzero pair differences; (1) gives
\(M(z)\ge4\).

For primitive type III an active pair has integral form \((s+t,s-t)\),
with \(t\ne0\). If the third entry is \(c\), the quadratic identity gives
\[
M(z)=Q(2t)+Q(s+t-c)+Q(s-t-c)
     =6Q(t)+2Q(s-c)\ge12. \tag{13}
\]
These bounds are attained:

| Class at depth \(d\) | Sharp minimum of \(M\) | Attaining preparation |
|---|---:|---|
| I: \(P=A_d\) | \(4^{d+1}\) | \((2^d,0,0)\) |
| II: \(P=2A_d-1\) | \(4^{d+1}\) | \((0,2^d,0)\) |
| III: \(P=5A_d\) | \(12\cdot4^d\) | \((2^d,-2^d,0)\) |

Substitution into (11) gives, for every nondiagonal cycle,
\[
\boxed{3P\le2M-5.} \tag{14}
\]
The lower bounds on \(2M-5-3P\) in classes I, II, III are respectively
\(4^{d+1}-4\), zero, and \(4^{d+1}\). Thus every minimum-account class-II
preparation attains equality. It is also attained at \(d=0\) in class I
with \(M=4\). Nondiagonal fixed states are included; only the fully diagonal
case is excluded.

These are minima of the account of states in a specified class, not minimum
costs of a contact preparation procedure. Odd integer multiplication preserves
admission and least periods while multiplying \(M\) and \(E\) by its square.
The account does not uniquely determine a period.

## 6. Deepest marks and a hidden fivefold phase

On the centered sum-zero slice, each inserted intermediate state in (4) has
depth zero. Doubled lower return states have the lower depth plus one.
Induction shows that deepest upper phases are exactly the \(2^d\)-multiples
of primitive phases. Classes I and II have one per least cycle; class III
has exactly five.

For their spacing in class III, begin with any primitive tick. It has length
one and one refusal. Its lifted segments obey the additive first-return count
\((L,R)\mapsto(L+4R,4R)\). Starting at \((1,1)\), after \(d\) lifts the
length is \(A_d\). Every one of the five primitive ticks has this count.

| Class | Interval between deepest marks | Least period of full state |
|---|---:|---:|
| I | \(A_d\) | \(A_d\) |
| II | \(2A_d-1\) | \(2A_d-1\) |
| III | \(A_d\) | \(5A_d\) |

This includes class III at \(d=0\), when every phase is deepest and the mark
is constantly one. A return of a mark need not be a return of the full state.

For example, \((4,0,2)=2(2,0,1)\) has \(E=40,S=6,M=48,d=1,P=25\).
Its five deepest states are
\[
(2+2\rho^k,2-2\rho^k,2),\qquad k=0,1,2,3,4,
\]
at times \(0,5,10,15,20\). Intermediate phases have depth zero.

A stronger pair keeps the specified accounts and local invariant residues
identical. Define
\[
w=1-j,\qquad v=2-j-j^2,\qquad
X=(6w,0,0),\qquad Y=(2w+2v,2w-2v,2w). \tag{15}
\]
Here \(Q(w)=5,Q(v)=15\). The quadratic identities give
\[
E(X)=E(Y)=180,\quad S(X)=S(Y)=6w,\quad M(X)=M(Y)=360.
\]
The state \(X/2=(3w,0,0)\) is a primitive class-I fixed state since
\(3w\notin2O\). The state \(Y/2=(w+v,w-v,w)\) is a primitive class-III
cycle: after \(k\) left contacts it is
\((w+\rho^kv,w-\rho^kv,w)\), whose right difference
\(-\rho^kv\notin2O\). Formula (4) therefore proves analytically
\[
P(X)=5,\quad P(Y)=25,\quad d(X)=d(Y)=1,
\]
\[
h(F^nX)=h(F^nY)=
\begin{cases}1,&5\mid n,\\0,&5\nmid n.\end{cases} \tag{16}
\]
Let \(\sigma(z)=\sum_i z_i\pmod5\), the residue modulo the ideal \((1-j)\).
Each slot's \(\sigma\) is preserved: an admitted increment is
\((\rho-1)t\in(1-j)O\), and refusal changes nothing. Both \(w\) and \(v\)
have \(\sigma=0\), so every local residue of both trajectories is zero.

Thus even the full infinite depth history, supplemented by these accounts
and local residues, does not determine full-state period. The stronger
coefficient residues in \(O/5O\) already differ at time zero:
\[
X:\ (1,4,0,0),(0,0,0,0),(0,0,0,0),
\]
\[
Y:\ (1,1,3,0),(3,0,2,0),(2,3,0,0).
\]
The invariant \(O/(1-j)\cong\mathbb F_5\) must not be confused with
coefficient reduction in \(O/5O\), which has 625 elements per slot.

## 7. General injectivity bound for coefficient readings

Fix \(S\) and \(M\), and reduce all twelve state coefficients modulo a
positive integer \(m\). If distinct states collide, then \(x-y=mz\), with
\(z\ne0\) and \(\sum_i z_i=0\). At least two slots of \(z\) are nonzero:
\[
E(x-y)=m^2E(z)\ge4m^2. \tag{17}
\]
For centered triples \(X_i=3x_i-S,\ Y_i=3y_i-S\), equation (3) gives
\(E(X)=E(Y)=3M\). The parallelogram identity yields
\[
9E(x-y)=E(X-Y)\le2E(X)+2E(Y)=12M. \tag{18}
\]
Hence a collision requires \(3m^2\le M\), proving
\[
\boxed{3m^2>M\ \Longrightarrow\
\text{coefficient reduction modulo }m\text{ is injective at fixed }S,M.}
\tag{19}
\]
This is sufficient, not a universal necessary condition. For the difference
reading \(u=a-b,v=b-c\), the same conclusion holds when \(\gcd(3,m)=1\):
\(3b=S-u+v,\ a=b+u,\ c=b-v\) reconstruct the absolute residues.

On \(E=32,S=4\), equation (3) gives \(M=64\). Formula (19) proves
injectivity already for \(m=5\), and also for \(m=8\). The states
\((4,0,0)\) and \((0,4,0)\) collide modulo four, so eight is the least
sufficient power of two. The assertion that five is the least positive
integer modulus additionally uses the modulo-three collision recorded by
the finite shell audit.

## 8. Complete finite shell audit and binary observation

The following census is an **exact finite computational assertion**, separate
from the general derivations. Completeness has a proved enumeration bound.
For each of the four marked coefficients of a slot, with
\(i,j,k\in\{0,1,2,3\}\) throughout (20),
\[
4Q(a)-5a_i^2
=\sum_{j\ne i}(2a_j-a_i)^2
+2\sum_{\substack{j<k\\j,k\ne i}}(a_j-a_k)^2\ge0. \tag{20}
\]
If \(Q(a)\le32\), then \(|a_i|\le5\). Enumerating this box gives 1811
possible slots. Enumerate all ordered pairs with \(Q(a)+Q(b)\le32\), set
\(c=4-a-b\), and retain exactly those with \(Q(c)=32-Q(a)-Q(b)\). Every
state on the shell occurs once. The audit checks that \(F\) permutes them:

| Least period | Cycles | States | Cycles with a concentrated mark |
|---:|---:|---:|---:|
| 1 | 2218 | 2218 | 0 |
| 5 | 72 | 360 | 0 |
| 9 | 26 | 234 | 0 |
| 21 | 2 | 42 | 2 |
| 41 | 1 | 41 | 1 |
| Total | 2319 | 2895 | 3 |

Independently of this census, (14) proves \(P\le41\) everywhere on the shell,
and \((0,4,0)\) attains it.

Define
\[
g(a,b,c)=1\iff\operatorname{sort}(Q(a),Q(b),Q(c))=(0,0,32).
\]
Since \(Q\) vanishes only at zero and the sum is four, the marked states
are exactly the three permutations of \((4,0,0)\). The census verifies one
mark in each of the two period-21 cycles and the period-41 cycle. All other
2812 states remain unmarked forever.

Given these audited cycles, the infinite binary observation has exactly
\(21+41+1=63\) classes: 21 pairs of corresponding edge-cycle phases, 41
individual middle-cycle phases, and one class of all unmarked states.

The **42-sample distinction** follows from this observation structure.
Include the sample at \(n=0\). Through length 21, the prefixes are the zero
word and each possible single-one word, giving \(L+1\) prefixes.
For \(22\le L\le41\), the 21 period-21 prefixes and the \(L+1\) zero or
single-one prefixes overlap in \(42-L\) single-one words, giving \(2L-20\).
At length 42 all 63 infinite classes are distinct. Sharpness is witnessed
by period-21 and period-41 words with their first mark at \(n=20\):
their first 41 samples agree, and sample \(n=41\) separates them.

This identifies an observation class using prior knowledge of the finite
shell. It differs from waiting for two marks and measuring their actual
separation. For a period-41 marked trajectory the second mark can occur as
late as \(n=81\), with the first sample at zero. Neither procedure is
implemented here as an integral-contact apparatus.

The audit counts absolute coefficient residue classes for moduli \(2,3,4,5\)
as \(136,1935,2791,2895\), respectively. Thus five is the least positive
integer modulus injective on this shell. Difference residues have counts
\(136,81,2791,2895\); the discrepancy at modulus three agrees with the
missing invertibility of three. These finite counts do not extend (19)
into an unproved general necessity.

## 9. Scope of the proposed result

The general candidate theorems are (4), (6), the no-H lemma with sharp bound
eight, (11), the sharp class-specific account bounds, (14), the deepest-phase
description, obstruction (15)–(16), and sufficient injectivity bound (19).
The shell census and finite audit families are computational evidence at
their stated domains. They do not establish the proofs' generality by
extrapolation or change their public status.

The contact and ordered schedule remain supplied. This work supplies no
native-U realization of the switching apparatus, occurrence law, physical
calibration, or funded contact implementation of the mark, counter and retained
record. A formula classifying a preparation is not a device measuring an
interval from a stream of marks.
