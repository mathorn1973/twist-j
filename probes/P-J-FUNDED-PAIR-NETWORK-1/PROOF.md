# Funded contact networks: transport, sign boundary and a recurring record

NON-CANONICAL / L1. The chosen networks/readers are candidate-D.
The conditional statements below are candidate-T, author proofs pending
independent review. No claim of derivation of the entire architecture from J.

## 1. Primitive and positive account

Let O=Z[j], Phi5(j)=0, J=1+j^2, Jinv=-j-j^2, rho=j^2 and
phi=-j^2-j^3. Then J Jinv=1, h(J)=J conjugate(J)=g=2-phi,
g^(-1)=1+phi, and g is a positive unit in both real embeddings, not one.
For c=(c0,c1,c2,c3), q(c)=Tr(h(c))/2 equals
(5 sum ci^2-(sum ci)^2)/2. It is integral, q(c)>=sum ci^2/2, and
q(c)=0 iff c=0. Finite arrays have finite bounded-q sets.

On the parity-admitted four-cell domain, centers c,d and relative values u,v
are integral. The full account is 2h(c)+2h(d)+2h(u)+2h(v).
The forward reciprocal operation changes it by
2(g-1)(h(u)-g^(-1)h(v)). Thus the exact forward balance is h(v)=g h(u).
The inverse balance is h(u)=g h(v). The two nonzero domains are disjoint:
their intersection would give (g^2-1)h(u)=0 and hence u=0.

On the forward domain (u,v)->(Ju,Jinv v) swaps h(u),h(v), maps into the
inverse domain and is undone by that branch. The reverse argument holds on
the inverse domain. The complement is fixed. This proves B^2=I on O^4,
including parity rejections and occupied states. Both marked pair sums and
complete H and E are conserved. Relative field norms are unchanged.
This inherited mathematical primitive is the subject of issue #1968;
its restatement here specifies exactly the map composed below.

## 2. Autonomous fixed-site network

Let m>=4 be even, with 2m raw cells and fixed sites P_i=(z_(2i),z_(2i+1)).
K0 applies B to disjoint adjacent site pairs starting at even i; K1 starts
at odd i, with periodic boundary indices. Within either layer blocks are
disjoint. Hence K0^2=K1^2=I. Define T=K1 K0, applying K0 first.

The whole state is z. No integer counter, advancing instruction tape, input
word, external driver or separately uncharged controller is present.
The graph, marked sites and layer order are part of the supplied law. Treating
this two-layer composition as one mathematical tick is not a physical-time
or hardware-cost theorem. It is local on the marked graph: one complete tick
has dependency radius at most two sites. It is invariant under translation
by two sites. Translation by one exchanges the layer order.

T is a full-carrier bijection with inverse K0 K1, conserving S,H,E and each
fixed pair sum. Since every E-level is finite, every finite-ring trajectory
is periodic from its initial state. No limiting, floating-point or empirical
recurrence assumption is needed. This supplies no infinite stream of fresh
independent records or positive entropy from a fixed finite state family.

## 3. What cannot propagate while constituent pairs remain fixed

For a site with even difference, its center c_i never changes, and its
relative value has the form

    u_i(t)=J^(k_i(t)) u_i(0),    k_i(t) an integer.

An initially odd difference stays odd and its site is never updated. A site
with zero difference is fixed and cannot participate in a nontrivial B.
For every accepted gate the two relative Hermitian values are swapped;
for refusal neither changes. Thus their multiset is preserved.

For nonzero initial u_i, h(u_i(t))=g^(k_i(t))h(u_i(0)). Because g has infinite
multiplicative order and the coefficient field has no zero divisors, the
current h determines k_i uniquely on the actual orbit. It then determines
the actual u_i, not merely its norm. Centers remain fixed. Consequently,
when all site differences are even, the number of reachable full raw states
is at most m!/product_v multiplicity(v)!, where multiplicities refer to the
initial relative Hermitian values (including zero). This is an upper bound,
not a claim that every permutation is reachable. Odd-difference sites can
instead be left out as permanently frozen sites.

More directly, multiply BOTH raw coordinates of any one site by -1.
Its difference parity and relative Hermitian value are unchanged. All branch
decisions are unchanged, and its updated coordinates are merely negated.
Thus this local sign flip commutes with every B respecting the fixed sites,
and with every fixed composition of them. More generally, admissible local
relative phases of unit Hermitian norm cannot change the account-dependent
branch decisions; no phase-mixing operation between sites is present.

Suppose two preparations differ only by this sign flip at a source site.
For every subsequent time their complete arrays OUTSIDE that source site
are identical. No reader confined there can distinguish the original sign.
This is a theorem for the full admitted carrier, not a short search failure.
It applies to the earlier common-payer inputs (2a,0,W,-W,0^12), a=+/-1,
W=Jrho: the payer changes but changes identically for both signs, and the
zero sites remain zero. A common raw-zero pair cannot be charged by this gate.

The conclusion is not that every funded network is impossible. It uses the
permanent constituent pairing. Section 6 changes that pairing explicitly.

## 4. Exact account transport on a prepared occupied background

For each site fix c_i in O, epsilon_i=+/-1, r_i mod5, a common nonzero integer a,
and let

    u_i=a epsilon_i rho^r_i J^eta_i, eta_i in {0,1},
    P_i=(c_i+u_i,c_i-u_i).

All differences are even and h(u_i)=a^2 g^eta_i. If adjacent occupations are
(0,1), the forward B exchanges their occupations; if (1,0), the reverse B
does. If they agree, neither nonzero balance condition holds and B is identity.
The local epsilon_i,r_i,c_i do not move. The code is invariant and the action
on eta is exactly the adjacent transposition, including its trivial equal case.

An occupation initially at even site i moves to i+1 under K0 and to i+2
under K1. One at odd site i moves to i-1 then i-2. Therefore

    eta_i(t)=eta_(i-2t)(0) for even i,
    eta_i(t)=eta_(i+2t)(0) for odd i.

This is an exact permutation factor for every binary word and every time.
On a finite ring T^(m/2)=I on the whole code; some words have smaller periods.
Oppositely directed signals cross without interacting on this particular
code, because the operation remains a coordinate permutation. Do not infer
phase transport, chaotic mixing or an interacting particle theory.

If all centers vanish and k occupations are high, the complete accounts are

    H=2a^2[m+k(g-1)],    E=a^2(4m+2k),    S=0.

A low site costs 4a^2, a high site 6a^2. A high occupation meeting a low
occupation transfers 2a^2 of half-trace account, with the complete Hermitian
transfer 2a^2(g-1), while the total is exactly unchanged. Nothing is refueled
or inserted after initialization. A larger prepared background has an explicit
larger initial cost; it is not a free supply of blank cells.

## 5. Remote common-account messages and their disappearance

Take m=4d, d>=1, a=1, centers0 and all epsilon=1,r=0. Input+ has its sole
high at site0, input- at site1. The initial arrays differ only at these two
source sites, and have common total account E=16d+2 and
H=8d+2-2phi. Every other raw coordinate, including the receiver, is common.
In particular receiver sites2d,2d+1 initially equal (1,-1); they are occupied,
not literal-zero or newly created memory.

For arbitrary arrays define the fixed rational reader

    R(z)=[q(z_(4d))+q(z_(4d+1))-q(z_(4d+2))-q(z_(4d+3))]/2.

Return NO_EXCESS when R=0, otherwise the tagged rational VALUE(R).
On these preparations, after complete ticks,

    R(T^t z_message)=message if t=d modulo 2d, otherwise 0.

Proof: the high is at 2t mod4d for input+, and 1-2t mod4d for input-.
The receiver's two site costs differ by two exactly at the stated times.
The first nonzero reading is t=d, with no earlier signal at this reader.
The entire state returns at 2d. This is a transmitted, recurring passage
signal. The reader needs no current counter, but its observation boundary is
the full two-layer update; the intermediate layer need not preserve its tag.
There is no retained archive after passage and no new independent trial when
the same signal returns. This encoding is not substituted for the failed
unknown-sign encoding of section 3.

## 6. Changing constituent pairs: four cells suffice for a recurring record

Now use FOUR raw cells and two groupings on their cyclic adjacency:
B0 acts in the order (0,1,2,3), B1 in the order (1,2,3,0).
Each is the same complete primitive B. Define T4=B1 B0, with inverse B0 B1.
Both preserve S,H,E. This has no driver word or unbounded counter either.
It does not keep the old two constituent sites fixed.

Let W=Jrho. Use common payer (W,-W), raw-zero receiver cell1, source cell0=2a,
where a=+/-1. Define

    A_+=(2,0,W,-W),
    C_+=(1+J,1-J,rho,-rho),
    B_+=(2,-W,W,0),
    A_-=(-2,0,W,-W),
    C_-=(-1-J,J-1,rho,-rho).

Each has H=4+2g=8-2phi and E=14. S=2a. The two inputs have the same full
Hermitian and trace accounts, though different conserved sums.

B0 sends A_a to C_a and back, by the known funded exchange. On A_a, B1
refuses by parity. On C_+, its first half-difference is -rho and its second
is -J, with centers0 and1. It takes the forward branch and yields B_+.
On B_+ it takes the inverse branch back to C_+. B0 refuses on B_+ by parity.
On C_-, B1 instead sees relative values0 and1, so refuses by balance.
Therefore the COMPLETE cycles are

    T4: A_+ -> B_+ -> C_+ -> A_+,
    T4: A_- -> C_- -> A_-.

All states within each cycle are distinct, so the periods are exactly3 and2.
They give an all-time occupied-state continuation proof, not a finite prefix.
The first post-tick payer pair is (W,0) for input+, (rho,-rho) for input-;
thus the source sign has actually affected cells initially outside its pair.
This explicitly delimits section 3. Those payer states alias at later times,
so this is NOT an all-time payer-only sign decoder.

The permanently marked raw receiver cell1 cycles as

    input+: 0,-W,-rho,0,...
    input-: 0,rho,0,... .

Tr(W)=-2 and Tr(rho)=-1. Hence the fixed total cell reader BLANK at zero,
VALUE(sign Tr(y)) at nonzero y returns a at EVERY nonblank state of both
cycles. The positive record survives two consecutive complete boundaries;
the negative record one. All intermediate B0 boundaries are either blank
or have the same correct sign as well. No opposite sign ever appears on
these declared two orbits. The semantic reader is supplied and is not a
physical detector selected independently from experiment.

This is an autonomous finite recurring record with explicit continuing
erasure, not permanent storage, source depletion or independent renewal.
The signal is also not a proof of remote phase propagation through an
arbitrarily large re-paired lattice. Combining this source with section 5's
remote account code requires a separate exact interface; it is not silently
assumed here.

## 7. Interpretation limits and next exact interface

Both constructions use finite arrays and fixed local updates. Neither requires
an infinite spatial carrier, an increasing number of slots or unbounded cell
values along its stated orbit. Pair preparation and network design remain
premises. No identification of account with measured energy, ticks with
proper time, or signals with photons, gravity or Born outcomes follows.

The next meaningful extension is a frozen extended re-pairing geometry with
one common initially occupied receiver or literal-zero receiving cell, an
unknown local phase source and a complete continuing readable-history
contract. The fixed-pair no-export result must not be evaded by relabeling
an energy-position code as the old source phase. The small recurring writer
and remote account conveyor are separate proven constructions, not yet one
complete phase-to-remote-record apparatus.
