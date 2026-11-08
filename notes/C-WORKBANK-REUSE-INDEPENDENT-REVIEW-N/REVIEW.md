# Mathematical review of the three v109 workbank scopes

NON-CANONICAL / L1. Detailed checks behind the verdicts in README.md. Target:
PR1879 PROOF.md at source pin `6f6570bbbddfc496131dd31c5fdacaaa9e1cd9e5`,
unchanged at head `d6a5f77169d1027a22959c41aa5a45a783643a3e`, read against
the scopes and falsifiers of PR1881 CLAIMS.md at
`337bf93c2f59d4f34a6395ef36de51aa3959c24e`. Notation follows PROOF.md:
O=Z[j], rho=j^2, u_e=1-rho^e, w_e=1+rho^e, u=u_1, w=w_1, b=w_2.
"Computed" marks a line confirmed by `review.py` in addition to the symbolic
check. No computation is a premise of an acceptance below.

## 0. Common law (PROOF section 1)

The contact agrees with Canon v108 RELATIVE-CONTACT-INTEGRAL-LAW: admission
when x-y is in 2O, output (s+rho t, s-rho t) with s=(x+y)/2 and t=(x-y)/2.
The checks are:

- On the admitted branch the difference becomes 2*rho*t, which is still in
  2O. Hence C^k(x,y)=(s+rho^k t,s-rho^k t), so C^5=id and every word is a
  bijection with literal inverse "reverse and replace C by C^4".
- The sum is s+s. Hermitian conservation follows from rho*conj(rho)=1, so
  E=Tr(H)/2 is conserved. Each slot changes by (rho-1)t, which lies in
  (1-j), so every labelled residue is preserved.
- rho is a unit, so the guard is rho-invariant. With the linear admitted
  branch and the identity refusal, this gives C(rho x,rho y)=rho C(x,y).
- C(x,y) and C(y,x) are the same map, since t changes sign. This is why
  both orientations obey the same phase rule in section 2.
- Phi_5 is irreducible over F_2 because 2 has order four modulo five. Hence
  O/2O=F_16, rho has order five there, and 1+rho^e is nonzero for e=1..4.

Computed: every distinct cached contact entry was certified for the sum, Q
(coefficient formula and trace formula), H, slot residues, orientation
symmetry, rho-equivariance including the guard, and C^5=id. Two rho
multiplication paths agreed (cyclic shift and j-basis map); 6629 entries
were certified in total.

## 1. Scope 1: positional-bank copying (PROOF sections 2-3)

**Guard on the b-family.** The pair (-rho^P b, rho^Q b) has difference
-b(rho^P+rho^Q). This is zero modulo two exactly when rho^P=rho^Q, that is
P=Q, because b is a unit of F_16. Then s=0 and t=-rho^P b, so the output is
(-rho^(P+1) b, rho^(P+1) b). Signs are kept, the phase is raised by one and
the value stays in the b-family. The phase abstraction (P,Q,R,S) with fixed
signs (-,+,-,+) is therefore exact along W6. Computed: all 25 (P,Q) cases,
in both orientations.

**Local table.** Each row was derived by hand with A=C14 (P,Q),
B=C45 (Q,R) and D=C16 (P,S):

    (0,0,0,0): A^2 (2,2,0,0); B refuses; A^3 (0,0,0,0); D^4 (4,0,0,4);
               A refuses; D (0,0,0,0).   AARAAAAAAARA, 10 admitted.
    (1,0,0,0): A^2 refuses; B (1,1,1,0); A^3 (4,4,1,0); D^4 refuses;
               A (0,0,1,0); D (1,0,1,1). RRAAAARRRRAA, 6 admitted.
    (0,1,0,0): A^2, B, A^3 refuse; D^4 (4,1,0,4); A refuses;
               D (0,1,0,0).              RRRRRRAAAARA, 5 admitted.

These agree with PROOF.md. Places 2 and 3 are never touched, and places 1
and 4 return to their inputs, so both source pairs are restored at the
twelve-contact boundary. Computed: the ring arithmetic equals the phase
model on all 625 states (P,Q,R,S). The quoted occupied-target example
(0,0,1,1)->(2,1,1,2) also holds.

**Embedding and induction.** Module p uses the negative entry of source pair
p, the positive entry of source pair q=p+1 and target pair p. Module p
touches target pair p only. Therefore the target pair is still fresh when
its module starts. The source is restored at every module boundary, so at
module p exactly one of r=p, r=q or "elsewhere" holds, as the local lemma
requires. Induction over p=0..4 gives K(M[r],M_empty)=(M[r],M[r]).
Exactly one module has p=r and one has q=r, so 6+5+3*10=41 contacts are
admitted, independent of r. The literal inverse has 4*60=240 contacts and
inverts K on the whole carrier. The account is 30+30=60 at the endpoints.
Computed: all five r on a 20-slot carrier, the source checked at all five
module boundaries, 41 admitted contacts, and inverse restoration.

**Fresh-target hypothesis.** The hypothesis is necessary, not only
sufficient. Computed: for all 25 occupied targets (M[r],M[p]), the source
bank is not restored. Each case reduces to one of three local rows, for
example (1,0,1,1)->(1,1,1,0) when r=p. K is also not an involution:
K K (M[2],M_empty) differs from (M[2],M_empty). Both observations stay
outside the positive contract, as CLAIMS.md says.

**Optional remark.** The rotated corollary of PROOF section 3 is also
proved by equivariance: rho^t(M[r],M_empty) maps to rho^t(M[r],M[r]) with
the same admission pattern. Computed for 25 cases. A fold may state it at
the same scope. It is not needed for scope 3.

Verdict: **ACCEPT** at the stated scope. The admission pattern still
depends on r, so the CLAIMS.md warning about timing-trace privacy is
correct.

## 2. Scope 2: four-place obstruction (PROOF section 4)

Suppose F(E)=E and F(A)=T. By section 0, F commutes with multiplication by
rho, so F(T)=F(rho E)=rho F(E)=rho E=T. F is injective, so A=T. A and T
differ only in places 3 and 4, where they read (-b,b) and (-rho b,rho b).
So (1-rho)b=0, and b=0 because O is a domain and rho is not 1. This
contradicts b being nonzero. The argument uses no orbit enumeration, no
search and no minimality.

For b=0 we have E=A=T=0, and the identity word satisfies both conditions,
so the restriction b!=0 is essential. The statement allows no auxiliary
reference. In the twenty-place copier the other source pairs act as
unrotated references, which is why that copier does not contradict the
statement.

**Optional remark.** The proof uses only injectivity and rho-equivariance.
It therefore also excludes words that mix in whole-slot SWAPs among the
same four places. Stating this is optional; the scope as written is correct.

**Sanity computation, not a dependency.** BFS over all words acting on the
triple (E,A,T), for b=1+rho^2, 1 and u, reaches 1800 joint states in each
case, the same number as the "1800-state BFS" named in PR1879
PROVENANCE.md, whose exact search was not seen. No reached
word has F(E)=E together with F(A)=T, and F(T)=rho F(E) on every reached
word. The single orbit of A has 45 states and does contain T. So some word
satisfies F(A)=T alone. The obstruction lies in the joint condition, as the
equivariance proof says.

Verdict: **ACCEPT** at the stated scope.

## 3. Scope 3: finite reuse with retained archives (PROOF sections 5-8)

**Read core (section 5).** The block equations agree with Canon v108 "One
explicit read word"; the block named K_p in the Canon is L_p in PROOF. That
construction is part of the accepted v108 theorem and is not re-accepted
here. By hand, the four-row E_c table was re-derived. For example, in row
(u,u,w), A0 gives (u_2,w_2) because u-w=-2rho; Bc refuses because u-w_2 is
-rho*w and w is nonzero modulo two; A0^4 restores; and Bc^4 gives (0,2).
Computed: the rebuilt word S has the stated block lengths and equals the
WORD535 fixture contact by contact. On all ten inputs, at all twenty R
boundaries, R restores source, clock, g, h and t, and an inactive read
preserves both banks. An event writes only the selected fresh bank, with
label -(r+t). W=S^10 ends at
(Y_(s+10),X_r,0,u,0,0,w,0,M[-r],M[-r-Delta_s]), and the literal W^-1 with
21400 contacts restores I(s,r).

**Modulo-nine event derivation (PR1881).** The first read at step t sees
source phase s+t; the second read, after F^-1, sees s+t-1. Both see clock
phase r+t. For t in 0..9 the solutions are those stated in CLAIMS.md: for
s=0 the events are (0,first), (1,second) and (9,first); for s=1 they are
(0,second), (8,first) and (9,second). The selector visits A, B and skip in
that order, so the labels are -r and -r-Delta_s with Delta_0=1 and
Delta_1=8 (that is 3 modulo five). The third event skips. Computed: the
event list read from execution equals this formula for all ten inputs.
**CONFIRMED** as exposition of the existing v108 table.

**One cycle (section 6).** W touches only slots 0..30. K(11,a) touches only
bank A and archive a; K(21,d) touches only bank B and archive d. Both
copiers start with a valid present record and a fresh target. Both restore
their source at the end. So the core just before W^-1 equals W(I(s,r)) on
all 31 coordinates, not merely on its labels. Since W^-1 is a two-sided
inverse on O^31 and leaves the complement alone, U(a,d) maps
(I(s,r),M_empty,M_empty) to (I(s,r),M[-r],M[-r-Delta_s]), with 82 admitted
copy contacts. The identity holds with any untouched complement.

**Induction (section 7).** Pi_(j+1) exchanges slots 0..4 with cartridge j+1.
The rest of the core is the common ready state, so the core becomes
I(s_(j+1),r_(j+1)) and the cartridge receives the restored input j. The
controls, working banks and archives are untouched. The next archive pair
has not been touched before, so it is fresh. Section 6 then applies with
the whole earlier occupied state as complement. All five bullets of the
induction hypothesis carry over to j+1, and the base case is section 6.
Retention follows from supports: after its own copier, archive pair j is
touched by no later U or Pi.

**Counts.** 26870 = 5350 + 2*60 + 21400 contacts per cycle, so 26870k
contacts and 5(k-1) swaps in total. The literal inverse has 4*26870k =
107480k contacts. For k=3 this gives 80610 and 322440, and with 1000 tuples
403050000 contact applications and 20000 swaps.

**Accounts (section 8).** Q(u)=5, Q(w)=Q(b)=3, Q(Y_a)=8, Q(X_r)=6 and
controls 8 give a core account of 82. In general:

- slots: 31+20k+5(k-1)=26+25k;
- account: 82+60k+14(k-1)=68+74k;
- auxiliary account: 68+60k on 26+20k addresses;
- sum: 4+2(k-1)=2(k+1).

Residues are (0,2,0) for every Y_a, (2,3) for every X_r and (3,2)^5 for
every bank. Every swap therefore exchanges equal residues, and the full
residue vector is invariant on this family.

**Supplement, not required.** H(Y_a)=4, H(X_r)=4+2j^2+2j^3, the controls
give 4, and each bank gives 10-10j^2-10j^3. Hence

    H_total = (24+28k) - (20+18k)(j^2+j^3).

For k=3 this is 108-74j^2-74j^3, as reported by PR1879. Computed for
k=1..5.

**Decoder.** It reads only the 2k archive banks. It accepts only the five
exact M[p] patterns, so an empty or invalid bank is rejected. The labels
(-r,-r-Delta_s) give d=Delta_s modulo five, which is 1 or 3. That
determines s, and r=-a. The map from inputs to archives is therefore
injective on all 10^k tuples. The counting bound 5^B>=10^k is ordinary
pigeonhole for a reader restricted to B five-valued marked banks. It gives
at least 5 banks for k=3, against 6 built. The bound is attained only at
k=1 (2 banks); in general the construction is an upper bound.

**Computed.** Exhaustive P_k for k=1, 2 and 3: 10, 100 and 1000 tuples.
At every W, K, W^-1 and Pi boundary the checks were the complete closed
form for core, archives and cartridges, and the complete E, sum, H and
residue vector. The checks also covered 41 admitted contacts per copier,
equal swap residues, the common auxiliary preparation, archive-only
decoding, injectivity and complete literal-inverse restoration. Samples of
30 tuples at k=4 and k=5 passed and are not proof. Inside each U, R/S
boundaries and copier module boundaries were not re-instrumented on the
full carrier. They were checked separately on the 31-slot core and the
20-slot copier.

Verdict: **ACCEPT** at the stated scope. Two limits must stay attached: the
induction is over a family of carriers whose prepared inputs and fresh
archive stock grow with k, and the inputs are supplied and loaded by fixed
swaps. The preserved boundaries in CLAIMS.md state both.

## 4. Points checked and found consistent

- PREREG "clock X_(r+10)" equals X_r; the proof writes X_r.
- PREREG "Y_n=F^n(0,2,0)" equals the closed nine-phase formulas (computed).
- RESULT's 40 rotated cases with 8400 contacts are 15*(12+48) +
  25*(60+240).
- The aggregate CI job skips its failure step under
  `if: needs.architecture.result != 'success'`, which is the pass path;
  both architecture jobs concluded success.
- After the final run, a static reading of the target verify.py showed that
  it refuses to run under `-O` (`sys.flags.optimize` guard). The optimizer
  qualification recorded in PR1881 for the supplied review code does not
  apply to the frozen verifier. This is not an implementation review of
  verify.py.

No error was found in the statements under review.
