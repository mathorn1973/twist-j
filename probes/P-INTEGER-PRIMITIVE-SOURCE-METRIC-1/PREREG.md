# P-INTEGER-PRIMITIVE-SOURCE-METRIC-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session integer-primitive-source-metric-2026-10-19  
Ownership issue: https://github.com/mathorn1973/twist-j/issues/1640

## 1. Authority, question, and custody

The base is Public Canon v103: main and peeled canon-v103 at
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md freezes all five
normative file hashes and sizes. In particular canon/CANON.md is 1052518
bytes with SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
Both implementations check these actual local bytes during the formal gate.

Question: can a declared Hermitian source holonomy change a primitive
integer K1 metric at a common counter while retaining a total funded
bijection, exact denominators, a uniform Lorentz domain, and a compatible
prescribed-source quadratic metric action?

Companion #1633 supplies the source apparatus and #1639 a scaled carrier
with shared-bank coupling. Neither foreign branch is modified. This probe
adds an actual source term to the field gate, and uses primitive rather than
redundantly scaled numerators. SOURCE.md identifies their immutable pins,
the independent review, and earlier consumed scaled-bridge identifiers.

PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py, and FROZEN.sha256 will
be committed, pushed, and read back before any scientific execution or
import. Only static reading, compilation, filesystem hashing, and authority
checks are allowed beforehand. The manifest hashes the other five files;
its own hash is recorded in the public pin receipt. No post-run mutation of
these six files is allowed.

The commit connector exposes no author-email override. It records A. M.
Thorn with 221838986+mathorn1973@users.noreply.github.com, while the configured
project identity is A. M. Thorn <thorn@twistj.com>. This limitation was
publicly disclosed in the ownership issue before pin and execution. Commit
provenance is preserved without rewriting.

## 2. Declared carrier and arithmetic

Let O=Z[j], with 1+j+j^2+j^3+j^4=0 and conjugation j -> j^4.
Set phi=-j^2-j^3, J=1+j^2,
J^(-1)=-j-j^2, phi^(-1)=phi-1,
A=diag(J,phi), and B(q)=[[1,q],[0,1]].
A dagger denotes conjugate transpose.

An Hermitian register is the eight-integer tuple

    H8=(a0,a1,d0,d1,c0,c1,c2,c3),
    H=[[a0+a1*phi,c],[conjugate(c),d0+d1*phi]],
    c=c0+c1*j+c2*j^2+c3*j^3.

No positivity of H as a matrix is required. The arithmetic cost is

    N(H)=4*a0^2+4*a0*a1+6*a1^2
        +4*d0^2+4*d0*d1+6*d1^2
        +10*sum(c_i^2)-2*(sum(c_i))^2.

The core is

    x=(s,q,H,R,Z,P,Q,k,p),
    s,q in Z; H,R,Z in Herm_2(O);
    P,Q in Z^5; k>=1; p in {0,...,6}.

This is 38 integer coordinates. The funded state (x,b,epsilon), with b>=0
and epsilon in {-1,+1}, has 40 coordinates. The fixed model context is
coupling lambda=1. The separately labelled negative control lambda=0
removes the field forcing only. Lambda is a fixed context key, not a
dynamically updated or charged coordinate.

The five sites are marked 0,...,4. Put m=324, ell=(1,-1,0,0,0), and

    (C P)_r=460*P_r+29*(P_(r-1)+P_(r+1))
                    +65*(P_(r-2)+P_(r+2)),
    a(k)=324 if k=1, otherwise 104976.

Subscripts of P are modulo five. At phase 6 read

    chi(H,R)=coefficient of j in (H-R)_01=H8[5]-R8[5].

The declared positive account is

    E(x)=1+s^2-s*q+q^2+N(H)+N(R)+N(Z)+k+sum(P_r^2)+sum(Q_r^2).

The denominator is computed from k, not stored as a separate charged
coordinate. E is an arithmetic storage/admission account, not physical
energy.

## 3. Seven-phase forward gate and exact partial inverse

The forward gate applies the listed change and increases p modulo seven:

| p before | Change |
| --- | --- |
| 0 | (s,q) -> (s-q,s) |
| 1 | H -> B(-q) H B(-q) dagger |
| 2 | H -> A^(-1) H (A^(-1)) dagger |
| 3 | H -> B(q) H B(q) dagger |
| 4 | H -> A H A dagger |
| 5 | Z -> Z+H-R |
| 6 | (P,Q,k) -> (C P-a(k) Q+2 lambda chi(H,R) ell,P,k+1) |

All unlisted registers are unchanged. The inverse at p!=0 undoes the
previous source phase. In particular the inverse source kick is
(s',q')->(q',q'-s'), and the inverse detector write is Z->Z-H+R.
At p=0, a backward step exists exactly when k>=2 and all entries of

    C Q-P+2 lambda chi(H,R) ell

are divisible by a(k-1). Its result is

    (P,Q,k,p) -> (Q,(C Q-P+2 lambda chi ell)/a(k-1),k-1,6).

Thus the divisor is 324 from k=2 and 104976 from k>=3. H,R are unchanged
during the field gate and its inverse, so the same chi is available.

For direction epsilon, attempt y=T^epsilon x. If the inverse domain is
absent, or if c=b+E(x)-E(y)<0, set F(x,b,epsilon)=(x,b,-epsilon).
Otherwise set F(x,b,epsilon)=(y,c,epsilon). Define Rev(x,b,epsilon)
=(x,b,-epsilon). The claimed full-carrier inverse is Rev F Rev.

The bare height 7(k-1)+p increases by one under T. The proper account
makes each E+b shell finite. Bank-admitted edges cut a bare ray into finite
paths. A path with L vertices has least funded period 2L. For the ready
bare history x_t, define B_sharp(t)=max_{0<=j<=t} E(x_j)-E(x_0).
The last reachable t is the last index with B_sharp(t)<=b. This uses prefix
maxima and does not assume monotone E.

## 4. Initial data and the metric reading family

The ordered word table is exactly the canonical one:

| word | u0 | u1 |
| --- | ---: | ---: |
| 0010 | 1 | 0 |
| 0011 | 1 | 1 |
| 0100 | 0 | -1 |
| 0101 | 0 | 0 |
| 0110 | 1 | -1 |
| 1001 | -1 | 1 |
| 1010 | 0 | 0 |
| 1011 | 0 | 1 |
| 1100 | -1 | -1 |
| 1101 | -1 | 0 |

For bits w0,...,w3, ut=w_(t+2)-wt. Reduce sites modulo five.
P0 has ones at u0,u0+1; P1 has ones at u1,u1+1; all other entries are zero.
The ready core has P=P1,Q=P0,k=1,p=0, s=a,q=0,

    H=R=D=diag(0,1), D8=(0,0,1,0,0,0,0,0),
    Z=Z0=[[1,j],[conjugate(j),1]], Z08=(1,0,1,0,0,1,0,0).

The twenty target histories use a=-1,+1, one of the ten words, and lambda=1.
The ten a=0 histories are a declared zero-source control. The optional
canonical probability weights are not used: no occurrence law is claimed.

For n>=1 set D_n=2*m^(n-1), h_n=P_n/D_n; at n=0 use D_0=2.
The reading family has domain ready histories and counter n>=0, codomain
(Sym_4(Q))^5 with marked counter, and literal equality of all marked
entries:

    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1).

Its context fixes the source sign, word, lambda, five labelled sites, plus
polarization, zero cross component, normalization, derivative branch, and
counter convention. Histories with identical matrices at a counter are
allowed to overlap. No uniqueness among other reading contexts is claimed.
The same algebraic formula can be evaluated on the unrestricted carrier,
but Lorentz signature is claimed only for the ready histories and their
retraced prefixes. P=(2,0,0,0,0),k=1 is a frozen degenerate counterexample
to unrestricted Lorentz signature.

## 5. Prospective mathematical claims and scope

B1: The specified T is injective with the stated image domain; funded F is
a total bijection, F^(-1)=Rev F Rev, and E+b is conserved. Every shell is
finite and every funded orbit is purely periodic.

B2: For every word and any integer chi history under the selected dipole,
the forced numerators are primitive and have least common denominator
d_n=2*m^(n-1), n>=1. For any exact common integer representation Ptilde/Dtilde
with Ptilde in Z^5 and Dtilde in Z>=1,

    Dtilde>=d_n,
    max(abs(Ptilde_r))>=ceil(d_n/5),
    sum(Ptilde_r^2)+Dtilde^2 >= (6/5)*d_n^2.

The actual account instead gives E>=sum(P_n^2)>=d_n^2/5. The pair bound is
not substituted into this account and does not cover compressed symbolic
descriptions.

B3: At field gates on the ready source history,
chi_n=a*(1,2,2,1,0,0) periodically. With
L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324,

    (Delta_c^2+L)h_n=J_n,
    J_n=lambda*chi_n*ell/m^n.

For lambda=1, a=+-1 and all words and counters,

    -299/500 < h_n(r) < 499/500,
    1+h_n(r)>201/500, 1-h_n(r)>1/500,
    det(g_n(r)) < -999/250000.

The proof compares to canonical free K1 on the zero-sum subspace; it must
exclude the constant zero mode explicitly. It bounds the added response by
1625/209304<1/125. A finite trajectory audit is not this all-counter proof.

B4: At word 0010, common initial bank 347057, both signs reach k=2 and

    P2(-)=(487,167,-230,130,94),
    P2(+)=(491,163,-230,130,94),
    h2(+)-h2(-)=ell/162.

The complete first-block E prefixes, including the initial core, are

    negative: 31,31,43,63,147,377,747,344440,
    positive: 31,31,43,63,147,377,803,347088.

The sharp first-seven-phase banks are 344409 and 347057; final banks at
the common 347057 are 2648 and 0. The occupied detector j coefficients
after six source phases are 0 and 2. Its old value is recovered by Z-H+R.

B5: Holding the source history fixed during variation, the canonical
full quadratic metric action A2 of DEF-K1-LINEAR-METRIC, with spatial
perturbation renamed V_ij, admits the added term

    (1/2)*sum_n <J_n,V_11-V_22>.

Vary the six metric components, lapse and shift before evaluating at
V=diag(h,-h,0), lapse=shift=0. The surviving derivative is
-(1/2)*sum <(Delta_c^2+L)h-J,delta V_11-delta V_22>; all other equations
vanish there. This is a prescribed-source quadratic plus-TT comparison.
It is indexed by the forward field counter, not each funded microtick.
There is no source variation, joint matter action, reciprocal
backreaction law, nonlinear Einstein equation, or continuum-limit claim.

All added registers, source functional, dipole, factor 2, attenuation law,
account, coupling, and reflection are NEW_DECLARED. The sourced rule is
not the canonical free rule and is not admitted as original-U dynamics.

## 6. Exact finite audit fixtures and counts

All arithmetic is integer or fractions.Fraction. No floats, random choices,
external numerical libraries, network access, or run-dependent inputs are
used. Ordered test entries may coincide as states; counts below count
entries, not distinct values. The two programs implement their own gates
and checks. Each named check must be non-vacuous.

### 6.1 Hermitian transport

The ordered 19-element fixture list HF is: zero; e_i then -e_i for i=0,...,7;
(1,-1,2,0,-2,1,0,1); (0,1,-1,2,1,0,-1,2), in H8 order.
For each check N>=2*sum(H8_i^2), with equality to zero iff H8=0.
For each apply A, A^(-1), and B(q) for q=-2,-1,0,1,2: 19*7=133 transport
entries. Check exact inverse, integer Hermitian closure, determinant
preservation, and the cost definition. The primary uses polynomial/matrix
arithmetic and also checks N=Tr_K/Q(tr(H^2)); the breaker uses independently
derived direct eight-coordinate formulas and real-pair determinants.

### 6.2 Full-carrier inverse, funding, and congruence

For i=0,...,18, k=1,2,3, and p=0,...,6, define 399 cores:

    s=i%3-1, q=(i//3)%3-1,
    H=HF[i], R=HF[(i+5)%19], Z=HF[(i+11)%19],
    P=(i-9,1,-2,0,3), Q=(2,-1,0,1,9-i).

For each core x, set y=T(x), verify T^(-1)(y)=x and height(y)=height(x)+1.
For each z in the ordered pair (x,y), set delta=E(T(z))-E(z).
The six labelled banks are 0,1,772,max(0,delta-1),max(0,delta),
max(0,delta+1). Test both directions at all six banks: 399*2*6*2=9576
funded entries. Verify both inverse compositions using Rev F Rev, account
conservation, carrier membership, and that the branch taken equals the
specified domain and bank rule. Overlapping banks are retained as entries.

For each i and predecessor k=1,2 take its p=6 core, advance once, and add
1 to P[2] of that image. The 38 corruptions must have no backward image
and must reflect unchanged with direction reversed at bank 1000000000.
The k=1,p=0 lower boundary must reflect in direction epsilon=-1 too,
regardless of bank.

### 6.3 Histories and stationary-action variations

For words in the table order and a in (-1,0,1), evolve the ready bare
lambda=1 history through n=24. Retain field records at n=0,...,24:
10*3*25=750 records. At each complete source block check chi against the
declared six-cycle; at every field record check the primitive common
denominator, sum h=1, and the stated rational metric bounds. Cross-check
the integer gate against a separate rational recurrence in each program.
Check the exact forced equation for n=1,...,23 and the unforced a=0 control. Compare
the forced histories with their corresponding free field history and
require abs(delta h)<1/125.

For each of the 30 histories, each n in (1,2,7,23), and each site r=0,...,4,
perform one exact central variation of the local reduced action

    A_local(v)= (||v-h_(n-1)||^2+||h_(n+1)-v||^2)/2
               - <v,Lv>/2 + <J_n,v>.

Require [A_local(h_n+e_r)-A_local(h_n-e_r)]/2=0:
30*4*5=600 exact finite variations. These audit the TT reduction; the
full metric/lapse/shift statement is proved in PROOF.md.

### 6.4 Fixed-counter contrast and complete bounce cycles

For word 0010, verify all B4 arrays, both sharp budgets and their bank
minus one, common-bank equality of reached counter, detector write and
recovery, and the exact metric difference. With the same two ready signs
and lambda=0, the field outputs coincide with canonical unforced P2;
the source/detector distinction remains. Omitting chi in the inverse
congruence must reject the actual first forced image for each sign.
Using 104976 at the first update must violate the correct sum.
Check the stated unrestricted degenerate readout as a scope counterexample.

Independently traverse each of these eight funded orbits through its first
return and require no earlier repeated state:

| a | bank | least period |
| --- | ---: | ---: |
| -1 | 772 | 14 |
| -1 | 344409 | 18 |
| -1 | 347057 | 24 |
| -1 | 344408 | 14 |
| +1 | 772 | 14 |
| +1 | 344409 | 14 |
| +1 | 347057 | 18 |
| +1 | 347056 | 14 |

Require exact return of every register, bank, and direction, and E+b
conservation at each microtick. These periods include the free next source
kick when a first field update spends the bank exactly.

## 7. Independent certificate grammar

Each implementation produces its own identical ASCII certificate below,
with fields in this order, decimal integers without plus signs or leading
zeroes (except the four-character word), lowercase SHA-256, and exactly one
LF after each line, including the last. No spaces occur in comma lists.

    CERTIFICATE=P-INTEGER-PRIMITIVE-SOURCE-METRIC-1
    AUTHORITY_FILES=5
    TRANSPORT_CHECKS=133
    CORE_FIXTURES=399
    FUNDED_CASES=9576
    IMAGE_DEFECTS=38
    HISTORY_RECORDS=750
    HISTORY_SHA256=<computed>
    ACTION_VARIATIONS=600
    PREFIX_NEG=31,31,43,63,147,377,747,344440
    PREFIX_POS=31,31,43,63,147,377,803,347088
    P2_NEG=487,167,-230,130,94
    P2_POS=491,163,-230,130,94
    SHARP_BANKS=344409,347057
    COMMON_FINAL_BANKS=2648,0
    METRIC_CONTRAST=1/162,-1/162,0,0,0
    CYCLE_PERIODS=14,18,24,14,14,14,18,14
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

All reported scientific arrays and counts come from the implemented
calculation and must also match their prospective values; copying a PASS
line alone is not a check.

The history hash is SHA-256 of the concatenation of the 750 records,
ordered by word table, then a=-1,0,1, then n=0,...,24. A record is

    word|a|n|P0,P1,P2,P3,P4|D\n

Here P0,...,P4 are the five entries of the primitive numerator at that
counter, not the initial slice labels. D=2 at n=0 and D=2*324^(n-1) at
n>=1. The record has exactly one LF, no spaces, no Unicode, no header.

breaker.py is a standalone separate implementation, not a library imported
by verify.py. Its successful stdout is exactly the certificate. verify.py
first computes its own certificate, then executes breaker.py using the
same Python executable with -I in a subprocess. Require exit zero,
empty stderr, and raw stdout byte identity, without strip, split/rejoin,
or newline normalization. The primary successful stdout is its certificate
followed by exactly

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Both programs catch only a dedicated ScientificFailure carrying a stable
falsifier key. Such an observed failed check completes the gate with exit
zero, empty stderr, and two ASCII lines:

    FALSIFIER=<key>
    RESULT=FAIL

Unexpected runtime/fixture errors are not caught as a scientific result:
they exit nonzero and trigger the POLICY.md abandoned-pin route. This
includes a breaker subprocess with nonzero exit or nonempty stderr:
the primary raises an uncaught runtime/protocol error in those cases.
A breaker that completes with its specified scientific FAIL stdout has
exit zero and empty stderr; disagreement with the primary then fires
BREAKER_BYTES as a completed scientific failure. For this one mismatch
case, the primary emits three lines: FALSIFIER=BREAKER_BYTES, then
BREAKER_STDOUT_HEX followed by "=" and the lowercase hex encoding of the
complete child stdout, then RESULT=FAIL, each terminated by LF. Thus the
child's exact bytes are retained in the completed failure record. All
other scientific failures use the two-line format above.

## 8. Falsifiers, publication, and interpretation

One exact violation fires the corresponding stable falsifier: AUTHORITY,
RING, TRANSPORT, COST, BARE_INVERSE, FUNDED_INVERSE, CONSERVATION, BRANCH,
IMAGE_GUARD, INITIAL_DATA, SOURCE_PATTERN, DENOMINATOR, MEAN, RECURRENCE,
LORENTZ, RESPONSE_BOUND, ACTION, PREFIX, SHARP_BUDGET, DETECTOR,
FIXED_COUNTER, CONTROL, PERIOD, CERTIFICATE, or BREAKER_BYTES. The labels
BREAKER_EXIT and BREAKER_STDERR instead denote uncaught runtime protocol
errors, not ScientificFailure keys. Thresholds and fixtures never move
after the pin.

A completed FAIL is preserved with its stdout and result. Unexpected
nonzero execution is recorded as ABANDONED, with no EXPECTED.txt or RUN.md,
and consumes this identifier. Any successor must use a new identifier and
new prospective pin. No evidence from an abandoned predecessor is silently
promoted to a successful run.

The first completed run freezes EXPECTED.txt, RUN.md, and RESULT.md.
The draft PR must run the same files on clean GitHub x86_64 ubuntu-latest
and aarch64 ubuntu-24.04-arm, Python 3.12. Inspect both actual probe replay
logs and the aggregate check. The CI gate is identical stdout from these
different architectures. A passing finite gate audits B1-B5; the proofs
and their assumptions remain independently reviewable.

The breaker author did not read the new primary verifier or PROOF.md, but
did participate in mathematical specification discussion and was exposed
to another team member's analytical report. Independence is asserted for
implementation code, not for the entire project context or a separate
human laboratory. No canonical status is assigned by this probe.
