# P-INTEGER-RECIPROCAL-SOURCE-ACTION-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3  
Ownership issue: https://github.com/mathorn1973/twist-j/issues/1642

## 1. Authority, question, and custody

The base is Public Canon v103: main and peeled canon-v103 at
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md freezes all five
normative file hashes and sizes. In particular canon/CANON.md is 1052518
bytes with SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
Both implementations check these actual local bytes during the formal gate.

Question: can the primitive integer K1 source-metric coupling choices
(chi, dipole ell, parity factor 2, and 324^n reader attenuation) be
structurally justified within the declared apparatus class, and can the
seventh-phase gate be upgraded to a reciprocal two-way source-metric
interaction that preserves an exact full-carrier bijection, primitive
common denominators, a uniform all-counter Lorentz domain across all
thirty ready histories, and a joint metric-and-source quadratic action?

Companion #1633 supplies the Hermitian source apparatus, #1639 the scaled
bridge, and #1641 the primitive-carrier one-way source-to-metric forcing.
None of those foreign branches is modified. This probe adds:
1. A structural classification theorem and finite audit for the four
   coupling ingredients (chi, ell, factor 2, and 324^n).
2. A reciprocal phase-6 update in which the field transition feeds back
   into the source register s via the scale-invariant modulo-2 dipole
   functional Phi(P,Q), together with a secular-resonance no-go proof for
   unattenuated numerator feedback.
3. A joint quadratic action A_joint[V,ell_0,N,chi] varying both the full
   metric/lapse/shift perturbation and the integer source variable chi.

PREREG.md, PROOF.md, SOURCE.md, verify.py, breaker.py, and FROZEN.sha256
will be committed, pushed, and read back before any scientific execution
or import. Only static reading, compilation, filesystem hashing, and
authority checks are allowed beforehand. The manifest hashes the other
five files; its own hash is recorded in the public pin receipt. No
post-run mutation of these six files is allowed.

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
reciprocal coupling lambda=1. The separately labelled negative controls
use lambda=0 (disabled coupling) or the one-way prescribed-source step
from #1641. Lambda is a fixed context key, not a dynamically updated or
charged coordinate.

The five sites are marked 0,...,4. Put m=324, ell=(1,-1,0,0,0), and

    (C P)_r=460*P_r+29*(P_(r-1)+P_(r+1))
                    +65*(P_(r-2)+P_(r+2)),
    a(k)=324 if k=1, otherwise 104976.

Subscripts of P are modulo five. At phase 6 read the source functional

    chi(H,R)=coefficient of j in (H-R)_01=H8[5]-R8[5]

and the reciprocal field-to-source parity-dipole functional

    Phi(P,Q)=sum_{r=0}^4 ell_r*((P_r mod 2)-(Q_r mod 2))
            =((P_0 mod 2)-(P_1 mod 2))-((Q_0 mod 2)-(Q_1 mod 2)),

where (t mod 2) in {0,1} is the standard least non-negative residue modulo
two. Thus Phi(P,Q) lies in {-2,-1,0,1,2}.

The declared positive account is

    E(x)=1+s^2-s*q+q^2+N(H)+N(R)+N(Z)+k+sum(P_r^2)+sum(Q_r^2).

The denominator is computed from k, not stored as a separate charged
coordinate. E is an arithmetic storage/admission account, not physical
energy.

## 3. Seven-phase reciprocal gate and exact partial inverse

The forward gate applies the listed change and increases p modulo seven:

| p before | Change |
| --- | --- |
| 0 | (s,q) -> (s-q,s) |
| 1 | H -> B(-q) H B(-q) dagger |
| 2 | H -> A^(-1) H (A^(-1)) dagger |
| 3 | H -> B(q) H B(q) dagger |
| 4 | H -> A H A dagger |
| 5 | Z -> Z+H-R |
| 6 | (s,P,Q,k) -> (s+lambda*Phi(P,Q), C*P-a(k)*Q+2*lambda*chi(H,R)*ell, P, k+1) |

All unlisted registers are unchanged. The inverse at p!=0 undoes the
previous source phase: (s',q')->(q',q'-s') at p=1, the inverse Hermitian
transports at p=2,3,4,5, and Z->Z-H+R at p=6.
At p=0, a backward step exists exactly when k>=2 and all five entries of

    C*Q-P+2*lambda*chi(H,R)*ell

are divisible by a(k-1). When this congruence holds, set

    P_prev=Q,
    Q_prev=(C*Q-P+2*lambda*chi(H,R)*ell)/a(k-1),
    s_prev=s-lambda*Phi(P_prev,Q_prev),
    k_prev=k-1,
    p_prev=6.

Because P_prev and Q_prev are recovered first from (P,Q,H,R,k), the exact
pre-step value Phi(P_prev,Q_prev) is available immediately to invert s.
H and R are unchanged during phase 6 and its inverse, so the same chi(H,R)
is available.

For direction epsilon, attempt y=T^epsilon x. If the inverse domain is
absent, or if c=b+E(x)-E(y)<0, set F(x,b,epsilon)=(x,b,-epsilon).
Otherwise set F(x,b,epsilon)=(y,c,epsilon). Define Rev(x,b,epsilon)
=(x,b,-epsilon). The claimed full-carrier inverse is Rev F Rev.

The bare height 7(k-1)+p increases by one under T. The proper account
makes each E+b shell finite. Bank-admitted edges cut a bare ray into finite
paths. A path with L vertices has least funded period 2L. For the ready
bare history x_t, define B_sharp(t)=max_{0<=j<=t} E(x_j)-E(x_0).
The last reachable t is the last index with B_sharp(t)<=b.

## 4. Initial data and the metric reading family

The ordered word table is the canonical ten-word set:

| word | u0 | u1 | beta(w)=Phi(P1,P0) |
| --- | ---: | ---: | ---: |
| 0010 | 1 | 0 | +1 |
| 0011 | 1 | 1 | 0 |
| 0100 | 0 | -1 | 0 |
| 0101 | 0 | 0 | 0 |
| 0110 | 1 | -1 | +2 |
| 1001 | -1 | 1 | -2 |
| 1010 | 0 | 0 | 0 |
| 1011 | 0 | 1 | -1 |
| 1100 | -1 | -1 | 0 |
| 1101 | -1 | 0 | 0 |

For bits w0,...,w3, ut=w_(t+2)-wt. Reduce sites modulo five.
P0 has ones at u0,u0+1; P1 has ones at u1,u1+1; all other entries are zero.
The ready core has P=P1,Q=P0,k=1,p=0, s=a,q=0,

    H=R=D=diag(0,1), D8=(0,0,1,0,0,0,0,0),
    Z=Z0=[[1,j],[conjugate(j),1]], Z08=(1,0,1,0,0,1,0,0).

All thirty ready histories use a in {-1,0,+1}, one of the ten words, and
lambda=1. Under reciprocal coupling, the ten a=0 histories are no longer
trivial unforced evolutions whenever beta(w)!=0: the initial metric shear
excites the source at the first field gate and produces a non-zero metric
response at k=3. True unforced free evolution is given by the lambda=0
control at a=0.

For n>=1 set D_n=2*m^(n-1), h_n=P_n/D_n; at n=0 use D_0=2.
The reading family has domain ready histories and counter n>=0, codomain
(Sym_4(Q))^5 with marked counter, and literal equality of all marked
entries:

    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1).

P=(2,0,0,0,0),k=1 is retained as a frozen degenerate counterexample to
unrestricted Lorentz signature on the full carrier.

## 5. Prospective mathematical claims and scope

B1 (Full-carrier reciprocal bijection): The reciprocal seven-phase gate T
is injective with the stated image domain; funded F is a total bijection,
F^(-1)=Rev F Rev, and E+b is conserved. Every shell is finite and every
funded orbit is purely periodic.

B2 (Structural classification of the coupling and primitive denominators):
Within the declared apparatus class:
1. For a single source loop with shear sigma in Z starting from D,
   (H(sigma)-R)_8 = (9*sigma^2,-5*sigma^2,0,0,-2*sigma,sigma,-sigma,0).
   Coordinate 5 (chi=coeff_j((H-R)_01)) is the unique coordinate equal to
   +sigma for all sigma in Z (unit-slope odd linear functional).
2. Among non-zero integer vectors u in Z^5 with sum_r u_r=0 (required to
   preserve the canonical mean sum_r h_n(r)=1), the minimal Euclidean
   norm is ||u||_2^2=2, attained by the 20 elementary dipoles e_r-e_s
   (r!=s). Fixing the canonical marked adjacent pair {0,1} and positive
   orientation at site 0 selects ell=(1,-1,0,0,0) uniquely. Moreover,
   because supp(ell)={0,1} has size 2, among the 3 unassigned sites
   {2,3,4} there is for every canonical word at least one site r_* with
   P_1(r_*)=0 and ell(r_*)=0, guaranteeing P_n(r_*)!=0 mod 3 for all n>=2.
3. In P'=C*P-a(k)*Q+kappa*chi*ell, any odd integer kappa flips the parity
   sum_r P_2(r) on odd chi and causes P_2 = P_1+ell = 0 mod 2 whenever
   chi_1 is odd and P_1=(1,1,0,0,0) (occurring on the 4 canonical words
   0010,0101,1010,1101), collapsing the common denominator from 648 to
   324. Thus kappa=2 is the minimal positive integer preserving primitive
   denominator d_n=2*m^(n-1) across all canonical words and integer
   histories.
4. Dividing the integer gate by D_(n+1)=2*m^n produces J_n=lambda*chi_n*ell/m^n
   automatically without an extra attenuation parameter. The encoding
   and actual-account bounds from #1641 continue to hold verbatim.

B3 (Reciprocal source oscillator and uniform all-counter Lorentz domain):
On every ready history (word w, initial seed a in {-1,0,1}, lambda=1):
1. Because P_n = P_1 mod 2 for all n>=1, the modulo-2 backreaction
   annihilates the m^(n-1) scale growth and satisfies
   Phi(P_1,P_0)=2*<ell,K_{11,0}-K_{22,0}>=beta(w) at k=1 and
   Phi(P_k,P_(k-1))=0 for all k>=2.
2. Consequently, the source holonomy sequence chi_n (n>=1, with chi_0=0)
   solves the exact second-order discrete oscillator equation

       (Delta_c^2+1)chi_n = chi_(n+1)-chi_n+chi_(n-1)
                          = a + lambda*beta(w)
                          = a + 2*lambda*<ell,K_{11,0}-K_{22,0}>,

   with six-periodic closed form
   chi_n(w,a) = a*p^(0)_n + lambda*beta(w)*p^(1)_n, where
   p^(0)=(1,2,2,1,0,0) and p^(1)=(0,1,2,2,1,0) repeated modulo 6.
3. Since |chi_1|=|a|<=1 and |chi_t|<=2|a|+2|beta(w)|<=6 for all t>=2, the
   forced metric response relative to the unforced free history h_n^free
   satisfies at all counters n>=0 and all sites r:

       ||h_n - h_n^free||_infty <= ||h_n - h_n^free||_2
         < (5/2)*(1/m + 6*sum_{t=2}^infty m^(-t))
         = 1645/209304 < 1/125.

   Combining with the canonical free bound -59/100<h_n^free(r)<99/100
   yields -299/500<h_n(r)<499/500, 1+h_n(r)>201/500, 1-h_n(r)>1/500, and
   det g_n(r)<-999/250000<0 for all 30 ready histories and all n>=0.
4. Conversely (secular-resonance no-go), an unattenuated numerator
   feedback chi_(n+1)-chi_n+chi_(n-1)=a+lambda*<ell,P_n> drives
   chi_n ~ m^(n-2) and injects a non-decaying O(m^(-2)) resonant coupling
   that violates the all-counter response bound 1/125.

B4 (Fixed-counter witnesses, zero-seed backreaction, and funded periods):
At word 0010 (where beta(0010)=+1):
- The first-block energy prefixes (heights 0,...,7) are:
  a=-1: 31,31,43,63,147,377,747,344440 (sharp bank 344409),
  a=0:  30,30,30,40,40,30,30,345012 (sharp bank 344982),
  a=+1: 31,31,43,63,147,377,803,347090 (sharp bank 347059).
- At the common bank 347059, both a=-1 and a=+1 reach k=2,p=0 with residual
  banks 2650 and 0, numerators P2(-)=(487,167,-230,130,94) and
  P2(+)=(491,163,-230,130,94), and metric contrast
  h2(+)-h2(-)=(1,-1,0,0,0)/162.
- At the second field gate (k=3, D_3=209952), the reciprocal source values
  are chi_2(-1)=-1, chi_2(0)=+1, chi_2(+1)=+3, giving
  P3(-)=(120111,-6141,-59422,98366,57038),
  P3(0)=(120977,-7007,-59350,98366,56966),
  P3(+)=(121843,-7873,-59278,98366,56894),
  whereas the unforced free numerator is
  P3^free=(120975,-7005,-59350,98366,56966).
  Thus even for zero initial source seed a=0, the gravitational
  backreaction excites the source and alters the third metric slice by
  h3(0)-h3^free=(1,-1,0,0,0)/104976.
- Because the reciprocal update shifts s at height 7 from a to a+1, the
  second-block shear is q_2=a+1 (which vanishes for a=-1, making its
  second-block Hermitian transports free until height 13). Consequently,
  the eight benchmark funded orbits on word 0010 have exact least periods
  14,26,28,14,14,14,18,14.

B5 (Joint metric-and-source quadratic action):
Define the joint action on compactly supported perturbations of all six
spatial metric components V_ij, lapse ell_0, shift N_i, and source
sequence chi_n (with chi_0=0):

    A_joint[V,ell_0,N,chi]
      = A_2[V,ell_0,N]
      + (lambda/2)*sum_{n>=1} (chi_n/m^n)*<ell,V_{11,n}-V_{22,n}>
      - sum_{n>=0} (1/2)*(chi_(n+1)-chi_n)^2
      + sum_{n>=1} [(1/2)*chi_n^2 - (a+2*lambda*<ell,K_{11,0}-K_{22,0}>)*chi_n].

1. Varying V_ij, ell_0, and N_i independently before evaluating at the
   plus-TT representative V=diag(h,-h,0), ell_0=0, N_i=0 gives the exact
   sourced field equation (Delta_c^2+L)h_n = lambda*chi_n*ell/m^n at every
   interior counter n>=1, while all other metric, lapse, and shift
   variations vanish identically.
2. Varying chi_n at the plus-TT representative gives the Euler-Lagrange
   gradient

       d A_joint / d chi_n
         = -[(Delta_c^2+1)chi_n - (a+lambda*beta(w))]
           + lambda*<ell,h_n>/m^n.

   On the reciprocal trajectory, the O(1) bracket vanishes identically at
   every n>=1, leaving only the exponentially small tail
   lambda*<ell,P_n>/(2*m^(2n-1)) with absolute value strictly bounded by
   2*D_n/(2*m^(2n-1)) = 2/m^n <= 1/162 < 1/2. Because the local reduced
   action is concave quadratic in chi_n with second derivative -1, the
   integer value chi_n is the strict global maximizer on the integer
   lattice Z at every counter n>=1, with unit-shift action margin
   A_joint,local(h_n,chi_n) - A_joint,local(h_n,chi_n+-1)
   = 1/2 -+ lambda*<ell,P_n>/(2*m^(2n-1)) > 40/81 > 0.

## 6. Exact finite verification protocol

### 6.1 Normative authority, ring identities, and Hermitian transport

Check the five normative file sizes and SHA-256 digests in SOURCE.md.
Check the 19 Hermitian fixtures (zero, +-unit basis vectors, and
(1,-1,2,0,-2,1,0,1), (0,1,-1,2,1,0,-1,2)) across the 7 gate pairs
(A,A^-1), (A^-1,A), and (B(q),B(-q)) for q in {-2,-1,0,1,2}: 19*7=133
transport checks, verifying closure, exact inverse, determinant
preservation, N(H)>=2*||H8||_2^2, and N(H)=Tr_K/Q(tr(H^2)).

### 6.2 Full-carrier inverse, funding, and congruence

For i=0,...,18, k=1,2,3, and p=0,...,6, define the 399 cores:

    s=i%3-1, q=(i//3)%3-1,
    H=HF[i], R=HF[(i+5)%19], Z=HF[(i+11)%19],
    P=(i-9,1,-2,0,3), Q=(2,-1,0,1,9-i).

For each core x, set y=T(x), verify T^(-1)(y)=x (including exact recovery
of s via Phi(P,Q) at p=6) and height(y)=height(x)+1.
For each z in (x,y), set delta=E(T(z))-E(z) and test all six banks
0,1,772,max(0,delta-1),max(0,delta),max(0,delta+1) in both directions:
399*2*6*2=9576 funded cases. Verify both inverse compositions via
Rev F Rev, E+b conservation, carrier membership, and branch coverage.

For each i and predecessor k=1,2, advance its p=6 core once and add 1 to
P[2] of that image. All 38 corruptions must have no backward image and
reflect unchanged at bank 1000000000, as must the k=1,p=0 lower boundary.

### 6.3 Structural coupling-selection audit

Execute 34 exact structural checks:
1. For sigma in {-2,-1,1,2} (4 checks), run one source loop from D and
   verify (H(sigma)-R)_8 = (9*sigma^2,-5*sigma^2,0,0,-2*sigma,sigma,-sigma,0)
   and that coordinate 5 is the unique coordinate equal to sigma.
2. Enumerate all non-zero zero-sum vectors in {-1,0,1}^5; verify there are
   exactly 20 minimal-norm vectors (||u||_2^2=2, 20 checks), each a
   site-permutation of ell=(1,-1,0,0,0), with ell the unique one supported
   on {0,1} having u_0>0.
3. For each of the 10 canonical words at a=1 (10 checks), compare odd
   coupling factor kappa=1 against kappa=2 at k=2: verify that kappa=2
   gives gcd(P_2,648)=1 on all 10 words whereas kappa=1 fails primitivity
   (giving gcd(P_2,648)=2) on exactly the 4 words 0010,0101,1010,1101.

### 6.4 Reciprocal histories and joint-action variations

For all 10 words in table order and a in (-1,0,1), evolve the ready bare
lambda=1 reciprocal history through n=24 (retaining 10*3*25=750 records)
plus the source loop at n=24 to read chi_24. At each n=1,...,24 verify the
closed-form six-periodic pattern chi_n = a*p^(0)_n + beta(w)*p^(1)_n; at
each n=1,...,23 verify both the source oscillator equation
chi_(n+1)-chi_n+chi_(n-1)=a+beta(w) and the forced field equation
(Delta_c^2+L)h_n=chi_n*ell/m^n. Verify primitive common denominators,
sum_r h_n(r)=1, Lorentz bounds -299/500<h_n(r)<499/500, and response bound
|h_n(r)-h_n^free(r)| < 1645/209304 < 1/125 against the unforced (lambda=0,
a=0) reference history.

For each of the 30 histories and each n in (1,2,7,23), evaluate the local
joint slice action

    A_joint,local(v,xi)
      = (||v-h_(n-1)||^2+||h_(n+1)-v||^2)/2 - <v,Lv>/2
      + (lambda*xi/m^n)*<ell,v>
      - [((xi-chi_(n-1))^2+(chi_(n+1)-xi)^2)/2
         - xi^2/2 + (a+lambda*beta(w))*xi].

Perform 5 central metric variations (r=0,...,4):
[A_joint,local(h_n+e_r,chi_n)-A_joint,local(h_n-e_r,chi_n)]/2 = 0
(30*4*5=600 metric variations), and 1 central + lattice-optimality source
variation:
[A_joint,local(h_n,chi_n+1)-A_joint,local(h_n,chi_n-1)]/2
= lambda*<ell,P_n>/(2*m^(2n-1)) with absolute value < 1/162 and strict
lattice optimality A_joint,local(h_n,chi_n)-A_joint,local(h_n,chi_n+-1)
> 40/81 (30*4*1=120 source variations), totaling 720 variations.

### 6.5 Fixed-counter contrast, backreaction witnesses, and bounce cycles

For word 0010, verify the energy prefixes for a in (-1,0,1), the sharp
first-block budgets (344409,347059) for a in (-1,1) and their bank-minus-1
reflections, the common-bank (347059) residual banks (2650,0), P2(-),
P2(+), detector write/recovery, and metric contrast (1,-1,0,0,0)/162.
Verify the second-block reciprocal numerators P3(-), P3(0), P3(+), the
zero-seed contrast h3(0)-h3^free=(1,-1,0,0,0)/104976, and the comparison
against the one-way prescribed-source control (where P3(a)-P3^one-way(a)
=(2,-2,0,0,0) for all a in (-1,0,1)). Also verify the negative controls:
lambda=0 coupling disabled, omitted inverse chi, omitted inverse s
backreaction (which fails to recover the predecessor core at k=2,p=0 for
word 0010), wrong first divisor 104976, and the unrestricted degenerate
core P=(2,0,0,0,0),k=1.

Independently traverse each of these eight funded orbits on word 0010
through its first return and require no earlier repeated state:

| a | bank | least period |
| --- | ---: | ---: |
| -1 | 772 | 14 |
| -1 | 344409 | 26 |
| -1 | 347059 | 28 |
| -1 | 344408 | 14 |
| +1 | 772 | 14 |
| +1 | 344409 | 14 |
| +1 | 347059 | 18 |
| +1 | 347058 | 14 |

## 7. Independent certificate grammar

Each implementation produces its own identical 25-line ASCII certificate
below, with fields in this order, decimal integers without plus signs or
leading zeroes, lowercase SHA-256, and exactly one LF after each line:

    CERTIFICATE=P-INTEGER-RECIPROCAL-SOURCE-ACTION-1
    AUTHORITY_FILES=5
    TRANSPORT_CHECKS=133
    CORE_FIXTURES=399
    FUNDED_CASES=9576
    IMAGE_DEFECTS=38
    COUPLING_SELECTION_CHECKS=34
    HISTORY_RECORDS=750
    HISTORY_SHA256=<computed>
    ACTION_VARIATIONS=720
    PREFIX_NEG=31,31,43,63,147,377,747,344440
    PREFIX_ZERO=30,30,30,40,40,30,30,345012
    PREFIX_POS=31,31,43,63,147,377,803,347090
    P2_NEG=487,167,-230,130,94
    P2_POS=491,163,-230,130,94
    P3_NEG=120111,-6141,-59422,98366,57038
    P3_ZERO=120977,-7007,-59350,98366,56966
    P3_POS=121843,-7873,-59278,98366,56894
    SHARP_BANKS=344409,347059
    COMMON_FINAL_BANKS=2650,0
    METRIC_CONTRAST=1/162,-1/162,0,0,0
    ZERO_SEED_CONTRAST=1/104976,-1/104976,0,0,0
    CYCLE_PERIODS=14,26,28,14,14,14,18,14
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

The history hash is SHA-256 of the concatenation of the 750 records,
ordered by word table, then a=-1,0,1, then n=0,...,24, with format

    word|a|n|P0,P1,P2,P3,P4|D\n

breaker.py is a standalone separate implementation executed by verify.py
using the same Python executable with -I in a subprocess. Require exit
zero, empty stderr, and raw stdout byte identity. The primary successful
stdout is its certificate followed by

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Both programs catch only ScientificFailure carrying a registered falsifier
key, outputting FALSIFIER=<key> and RESULT=FAIL (plus BREAKER_STDOUT_HEX
when FALSIFIER=BREAKER_BYTES). Unexpected runtime/protocol errors exit
nonzero.

## 8. Falsifiers, publication, and interpretation

Registered falsifier keys: AUTHORITY, RING, TRANSPORT, COST, BARE_INVERSE,
FUNDED_INVERSE, CONSERVATION, BRANCH, IMAGE_GUARD, COUPLING_SELECTION,
INITIAL_DATA, SOURCE_PATTERN, DENOMINATOR, MEAN, RECURRENCE, LORENTZ,
RESPONSE_BOUND, ACTION, PREFIX, SHARP_BUDGET, DETECTOR, FIXED_COUNTER,
BACKREACTION, CONTROL, PERIOD, CERTIFICATE, and BREAKER_BYTES.
Runtime protocol error labels are BREAKER_EXIT and BREAKER_STDERR.

The first completed run freezes EXPECTED.txt, RUN.md, and RESULT.md,
followed by clean GitHub Actions replay on x86_64 ubuntu-latest and
aarch64 ubuntu-24.04-arm with Python 3.12. No canonical status is
assigned by this probe.
