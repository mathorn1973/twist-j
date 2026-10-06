# Conditional source-table classification

Status: NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Candidate proof, subject to the separate review and disposition in this package.
All definitions and membership tests are those of the frozen PREREG.md.
This proof was developed analytically before the new finite audits were run.

## 1. Statement and exact scope

Within the declared ten-entry control-table class there are 4608 distinct
complete reversible maps W, of which 600 are involutions. Their complete
commutators K_(W,i) are exactly four maps:

    q_i -> q_i + 3 chi(h),

with every other coordinate fixed. Here chi(0)=1, chi(-h)=chi(h), and the
two independent binary values chi(1),chi(2) are unrestricted. The statement
holds on all X=F5^12 times {0,1}, including occupied eta and arbitrary q,r.

Within the declared three-active-reference-label table class there are
30 readers satisfying the marked ready contract. Five are pointwise
involutive. There are five literal complete endpoint-reader maps, each
represented by six tables. They form one orbit under native q translation.
The 30 tables form one orbit under the product of q translation and internal
reference relabeling, with trivial table stabilizers. These statements do
not independently admit the source reading, control class, reference
interface, preparation or endpoint reading.

## 2. Native identities and faithful reduction

The explicitly given b,d,e are involutions. Direct substitution gives
tau_i=e_i d_i as q_i -> q_i+1 with all other coordinates fixed, and
tau_i^-1=d_i e_i. The full involution I=b_x b_y negates both q coordinates
and both r coordinates. Consequently, on the full carrier,

    I tau_i I = tau_i^-1.

On each row-major piston matrix b is multiplication by minus the matrix
that swaps the two rows. Its determinant is -1. Applying the same map to
both matrices therefore negates their polarized determinant reading:
h(I s)=-h(s). This is an identity of the source coordinates, independent
of all q,r and eta values. Both tau_i preserve h.

For nonzero h, each data orbit {s,I s} has two distinct elements, since
the two h values differ. Choose its representative with h=k, k=1 or 2.
Including eta gives four labels (u,eta) in the order 2u+eta. A control
table acts by

    (u,eta) -> (u xor a((-1)^u k,eta), beta((-1)^u k,eta)).

This is an arbitrary permutation of the four labels precisely when W is
bijective on that orbit. The same permutation acts on every data orbit
in that sign pair. Thus the two nonzero sign pairs each contribute S4.

At h=0, the table cannot inspect u. On a free data orbit it acts as

    (u,eta) -> (u xor a(0,eta), beta(0,eta)).

It is reversible if and only if beta(0,.) permutes the two bits. There
are two choices of beta and four independent choices of a(0,.), hence
eight maps. Each commutes with the sign flip
J=(02)(13), because a and beta do not depend on u. Conversely every
permutation commuting with J has this form. This is its centralizer in S4.

Fixed data points of I at h=0 cause no missing condition. On such a point
W acts only by the already bijective beta on eta, and therefore remains
bijective. The conjugation identity W I=I W on h=0 follows directly from
the coordinate formula and holds at free and fixed points alike.

No two different admitted tables become the same complete W. For each h
the frozen witness Xp=(1,0,0,0), Yp=(0,0,0,2h) has that reading, and I moves
its pistons. Changing either a or beta at either eta changes its complete
output. This proves faithfulness, including at h=0.

The four-label description is used to classify the table, not to assume
that tau remains inside a chosen data orbit. In general it does not. The
full-coordinate expression for E below, together with I tau I=tau^-1,
is what transfers the contact result to the complete carrier.

## 3. Complete controls and the four contact laws

The full control class is the direct product

    C_S4(J) times S4 times S4,

so it contains 8*24*24=4608 maps. At h=0, beta=id allows all four a
choices to be involutions; beta exchanges the bits and requires its two
a values to coincide, allowing two further choices. S4 has ten
involutions: its identity, six transpositions and three products of two
disjoint transpositions. Thus exactly 6*10*10=600 controls are involutive.

For an arbitrary admitted W, E_W=W I W^-1 is an involution. On either
nonzero sign pair its four-label action is one of the three matchings

| Matching | Label permutation | Data action | Bit action |
|---|---|---|---|
| J | (02)(13) | I | eta |
| H | (01)(23) | id | eta xor 1 |
| D | (03)(12) | I | eta xor 1 |

These are exactly the conjugates of J in S4. At h=0, E_W=I because W
commutes with I there. It follows on the complete carrier that

    E_W(s,eta) = (I^chi(h) s, eta xor epsilon(h)),

where chi and epsilon are even functions of h, chi(0)=1, epsilon(0)=0,
and the nonzero-pair possibilities are (chi,epsilon)=(1,0),(0,1),(1,1).
These are full data actions: the same I negates both q and both r. No
independent or untracked q lift has been inserted into the reduction.

Because tau_i preserves h and eta, the native inversion identity yields

    E_W tau_i E_W = tau_i^((-1)^chi(h)).

Consequently K_(W,i)=[E_W,tau_i] is q_i translation by
(-1)^chi(h)-1. This is 0 for chi=0 and -2=3 in F5 for chi=1. All pistons,
both r values, the other q, and eta return. The inverse is q_i translation
by -3 chi(h). In particular, this action is independent of whether the
bit is already occupied, and covers fixed I data without a genericity
assumption.

Each matching has eight preimages under S4 conjugation, since the
centralizer has size eight. Thus each nonzero pair has eight controls
giving chi=0 and sixteen giving chi=1. Among involutive controls the
matching J has six preimages, H has two and D has two. To see this without
a numerical census, the identity, three double transpositions and the two
transpositions (02),(13) centralize J; the remaining four transpositions
split into two pairs conjugating J to H and D. Therefore an involutive
control has two choices for chi=0 and eight for chi=1 on a nonzero pair.

The exact fibres over complete contact maps are:

| Profile chi(1)chi(2) | All reversible W | Involutive W | chi(h) in F5 |
|---|---:|---:|---|
| 00 | 512 | 24 | 1-h^4 |
| 01 | 1024 | 96 | 1+2h^2+2h^4 |
| 10 | 1024 | 96 | 1+3h^2+2h^4 |
| 11 | 2048 | 384 | 1 |
| Total | 4608 | 600 | |

For completeness, put c1=chi(1), c2=chi(2). The coefficients in
1+A h^2+B h^4 solve 1+A+B=c1 and 1+4A+B=c2, giving
A=2(c2-c1) and B=3(c1+c2)-1 in F5. An even function is specified on
h^2=0,1,4; these are distinct field elements, so the degree-at-most-four
even representative is unique.

Explicit involutive witnesses require no search. Set W=id at h=0. On a
nonzero pair for which the desired chi value is 1, set W=id. On a pair
for which it is 0, use

    W(s,eta)=(I^(sigma(h) xor eta) s, sigma(h)),

with sigma(k)=0 and sigma(-k)=1. This exchanges the two diagonal labels
(0,1) and (1,0) and fixes the other two, conjugating J to H. Combining
the two choices on the two sign pairs gives every profile. Choosing the
diagonal exchange on both pairs is exactly the supplied v100 W_b, whose
frozen ten-digit table ID is 0102023131.

Thus the source-table premises permit four contact laws, including the
v100 law. Even among involutions, W_b is one of 24 different full controls
with the same complete contact endpoints. This is a conditional
classification of declared controls, not a negative closure of the live
native-contact question or an assertion that unique W is necessary.

## 4. All admitted reference tables

Write a_q=P_q(0). The ready contract is equivalent to

    P_q(0)=P_(q+3)(1), hence P_q(1)=a_(q+2).

Since P_q permutes three labels, a_q and a_(q+2) must differ. Their two
values also determine P_q(2) as the remaining label. This establishes a
bijection between all admitted tables and the proper three-colorings of
the five-cycle with edges q -> q+2. It proves completeness of a reader
construction from ready-column assignments, without assuming any
pointwise involutivity.

An independent set in a five-cycle has at most two vertices. Hence each
proper three-coloring has color multiplicities (2,2,1). Choose the
singleton position in five ways and its color in three ways. The remaining
four-vertex path must alternate the two other colors, in two ways.
There are therefore 5*3*2=30 literal reader tables.

For a pointwise involutive P_q the allowed ordered pairs
(P_q(0),P_q(1)) are exactly

    (0,1), (1,0), (2,1), (0,2).

Regard these as directed edges. Every closed walk passes through 0; its
successive excursions from 0 are 0->1->0, of length two, or
0->2->1->0, of length three. A closed walk of length five must contain
one of each excursion. Up to cyclic starting position there is exactly
one such walk, and its five positions give five different tables. The
supplied v100 table is one, so all five are its q translates. The
singleton ready-column color is 2 for these five tables.

No new reference-size lower bound is claimed: the prior CONTACT-RECORD
minimum three is a source result, while this theorem classifies the fixed
three-active-label interface already declared in the question.

## 5. Complete endpoints, equality and stabilizers

Put H_q=P_(q+3)^-1 P_q. The full reader R_P acts by

    (q,r) -> (q+3,H_q(r)),

fixing all other native coordinates. Every H_q fixes r=3,4 and sends 0
to 1. Its full inverse is

    (q',r') -> (q'-3, P_(q'-3)^-1 P_(q')(r')).

Two admitted tables have identical endpoints if and only if they differ
by one common left relabeling L in S3. The forward implication follows
by equating H'_q=H_q and rearranging:

    P'_q P_q^-1 = P'_(q+3) P_(q+3)^-1.

Addition by 3 is a single cycle on F5, so the left-hand side is the same
L for every q. The converse follows by cancellation. The action of S3
on tables is free because each P_q is invertible. Each complete endpoint
therefore has exactly six tables, and there are five complete endpoints.

These five endpoints can be written explicitly in the fixed labels.
Let j be the unique q at which a_q has its singleton color. Define
T=(1,0,2) and Z=(1,2,0), in image-tuple notation. Then

    H_q = T if q=j-1 or j+1; H_q = Z otherwise.

To verify the pattern it suffices to compute it for the supplied table,
where j=2: H=(Z,T,Z,T,Z). The 30-table count, the six-table endpoint
fibres and the five q translates prove this covers every admitted table.
In particular these five endpoints really differ on occupied references,
although every one sends a ready reference to 1.

Let S_t be actual native q translation by t. Replacing P_q by P_(q+t)
changes the endpoint to S_-t R_P S_t and moves j to j-t. Thus the five
endpoints form one free q-translation orbit. The table q action is also
free: any nonzero stabilizing translation would make P_q constant, which
contradicts the ready contract. There are six table q orbits and one
pointwise-involutive table q orbit.

The combined table action of C5 times S3 is free. If a translation t
and a relabeling L fix a table, then for nonzero t, iteration five times
gives L^5=id. Every S3 element has order 1,2 or 3, so L=id, reducing to
the impossible nonzero translation stabilizer. For t=0, table
invertibility directly gives L=id. Hence the 30 tables form one joint
orbit with trivial stabilizers. Under the induced action on endpoints,
the stabilizer is exactly {0} times S3: all internal relabelings cancel,
and no nonzero q translation fixes an endpoint.

| Object and action | Objects | Orbits | Orbit size | Stabilizer size |
|---|---:|---:|---:|---:|
| Tables under q translation | 30 | 6 | 5 | 1 |
| Involutive tables under q translation | 5 | 1 | 5 | 1 |
| Tables under internal S3 | 30 | 5 | 6 | 1 |
| Tables under C5 times S3 | 30 | 1 | 30 | 1 |
| Endpoints under q translation | 5 | 1 | 5 | 1 |
| Endpoints under internal S3 | 5 | 5 | 1 | 6 |
| Endpoints under C5 times S3 | 5 | 1 | 5 | 6 |

Internal relabeling does not preserve pointwise involutivity. For example,
the supplied P_1 is the identity; left-composing its whole table with a
three-cycle makes P_1 a three-cycle. The resulting table is still admitted
and has exactly the same complete endpoint, but is not pointwise
involutive. Algebraic relabeling and physical admission are separate
questions.

## 6. Pairing with all contacts and the exact ambiguity

For any admitted contact law and reader, the complete coupling
C_P^-1 K_(W,i) C_P has action

    q' = q + 3 chi(h),
    r' = P_(q')^-1 P_q(r).

All remaining coordinates are unchanged. Its inverse uses

    q = q' - 3 chi(h),
    r = P_q^-1 P_(q')(r').

These identities hold for all five reference values, every q, all pistons
and occupied eta. If chi(h)=0 the complete map is the identity. If chi(h)=1
it has the endpoint H above; from r=0 the output is 1 for every unknown q.
Thus the prepared output is exactly chi(h).

There are twenty different full paired maps: four contact laws times
five endpoint types. Differences between contact laws are witnessed by
their q translations. For a fixed law all five endpoint differences can
be witnessed at h=0, where every law is active. Each full paired map of
profile c has 6 times the W-fibre count in section 3 as its literal
(W,P) representations. In the involutive-W / pointwise-involutive-P
subclass it has exactly the corresponding involutive W-fibre count,
because each endpoint has one such P table.

Ready readout identifies only four law profiles. In the frozen
calibration query class, one separate ready-reference experiment at h=1
and one at h=2 give the pair (chi(1),chi(2)) and distinguish all four.
One query has only the two marked outputs 0,1 and cannot distinguish
four laws; at h=0 it is constant. Thus two queries are necessary and
sufficient within this declared class. These are separate prepared
experiments, not a claim of reusable memory, a reset or a realized
physical detector.

The remaining source-table choice is therefore two binary response
values, after the stated h,I and table-dependence premises are fixed.
The v100 response is the profile 00. Selecting it requires a further
reason for inactivity on both nonzero sign pairs. This note supplies
no target-independent physical reason for that restriction.

## 7. Limits of the theorem

- The table class, source reading h and distinguished involution I are
  premises. Completeness refers to this class alone. The motivating
  successful v100 example was known before the class was frozen.
- The theorem neither derives C or W_a nor admits the control alphabet,
  the reference coupling, preparation or endpoint interpretation from J
  or autonomous U. It does not close QUADRATIC-MEMORY-NATIVE-CONTACT.
- Literal equality of K or C_P^-1 K C_P endpoints does not identify W
  prefixes or compiler words that use W as a generator. In particular it
  makes no claim about the compiled T_alg q lift or a replacement in V.
- Reversible occupied-reference maps are covered. Fresh archives,
  completion flags, reset, autonomous scheduling, event selection,
  physical time, energy, scale and cross-layer lifts are not supplied.
- Written proof and finite audit are separate evidence. The new runs are
  local one-architecture audits, and ordinary notes CI cannot promote
  them to a public scientific two-architecture gate.
