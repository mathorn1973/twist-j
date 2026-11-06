# P-INTEGER-JOINT-VARIATION-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session integer-joint-variation-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1645

## 1. Question, authority and custody

Can the metric and a dynamical source satisfy both continuous
Euler-Lagrange equations exactly while every stored state coordinate is
an integer, with a Hermitian source realization, continued reciprocal
feedback, an unrestricted reversible admission rule, and an all-counter
Lorentz domain on the thirty specified initial histories?

Public Canon v103 is active at main and peeled canon-v103 commit
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md records the five
actual normative hashes and sizes; both programs verify those local bytes.
canon/CANON.md is 1052518 bytes, SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.

The independent review of #1644 at pin
3ae3ea66e1e3c633c048ece10e3baf43f144d8c7 and result head
d47c813c0347e6341b5802b3c8633c4103dc3810 is recorded at
https://github.com/mathorn1973/twist-j/pull/1644#issuecomment-6267871040.
Its finite PASS remains intact. Its actual source variation is generally
nonzero, and its parity feedback on ready histories acts only once. This
probe retains the continuous reciprocal term instead. It uses a new
common scale and a new source law; it does not inherit primitive-denominator
optimality, the old source micro-law, or the unsupported no-go claim.

Before any scientific execution or import, freeze PREREG.md, PROOF.md,
SOURCE.md, verify.py, breaker.py and FROZEN.sha256, publish the pin and
read all six files back. Static reading, AST parsing and file hashing are
allowed before that point. No frozen file will change after execution.
Both implementations compare exact quantities, with no floating point,
rounding, clipping, fitting, selected seeds or numerical tolerances.

## 2. Selected coupled equations and integer carrier

Let m=324, ell=(1,-1,0,0,0), e=(1,1,1,1,1), and

    (C P)_r=460 P_r+29(P_(r-1)+P_(r+1))+65(P_(r-2)+P_(r+2)),
    L=(648 I-C)/324.

Spatial indices are modulo five. The source context a is fixed in
{-1,0,1}. It is not a changing state coordinate. The selected equations
for all n>=1 are

    h_(n+1)-2 h_n+h_(n-1)+L h_n = chi_n ell/m^n,
    chi_(n+1)-chi_n+chi_(n-1) = a-<ell,h_n>/m^n.

Here h_n is a rational five-vector and chi_n a rational scalar. Define

    D_n=2*m^(n*(n-1)/2) for n>=0,
    P_n=D_n h_n, Y_n=D_n chi_n.

In particular D_0=D_1=2. This common scale is sufficient, not asserted
primitive or optimal. The underlying time counter stays discrete even
though the action is varied over real comparison variables.

The unrestricted core is x=(P,W,Y,V,H,k), where P,W are arbitrary integer
five-vectors, Y,V are arbitrary integers, H is an arbitrary eight-integer
Hermitian register defined below, and k>=1. There are 21 integer core
coordinates. With bank b>=0 and direction epsilon in {-1,1}, the funded
carrier has 23 integer coordinates. No readiness constraints are imposed
on the full carrier.

The single combined macro-step, with r_k=m^(2*k-1), is

    P'=m^(k-1) C P-r_k W+Y ell,
    Y'=m^k Y-r_k V+a D_(k+1)-<ell,P>,
    W'=P, V'=Y, k'=k+1,
    H'=M(Y'-Y) H M(Y'-Y)^dagger.

All right-hand sides use the old state. There is no external phase
schedule and no hidden source multiplier. k remains an explicit precision
and history counter. Admission charges the combined macro-step; it does
not assert a bank charge after each factor of M.

For a candidate x' with k'>=2, put n=k'-1. Its predecessor exists exactly
when all six entries of the following numerators are divisible by r_n:

    W_prev=(m^(n-1) C W'+V' ell-P')/r_n,
    V_prev=(m^n V'+a D_(n+1)-<ell,W'>-Y')/r_n.

Then P_prev=W', Y_prev=V', k_prev=n, and

    H_prev=M(V'-Y') H' M(V'-Y')^dagger.

At k'=1 no backward step exists. H adds no congruence restriction.

## 3. Cyclotomic realization and positive account

Use O=Z[j], 1+j+j^2+j^3+j^4=0, conjugation j*=j^4,
phi=-j^2-j^3, J=1+j^2, J^(-1)=-j-j^2, phi^(-1)=phi-1,
A=diag(J,phi), B(t)=[[1,t],[0,1]]. D_H=diag(0,1).

    v=J/phi-1=-2+j-j^2, v v*=9-5 phi,
    M(t)=A B(t) A^(-1) B(-t)=[[1,t v],[0,1]].

An H8 tuple (a0,a1,d0,d1,c0,c1,c2,c3) denotes

    H=[[a0+a1 phi,c],[c*,d0+d1 phi]],
    c=c0+c1 j+c2 j^2+c3 j^3.

Its positive arithmetic cost is

    N(H)=4 a0^2+4 a0 a1+6 a1^2+4 d0^2+4 d0 d1+6 d1^2
         +10 sum(c_i^2)-2(sum c_i)^2
        =Tr_(Q(j)/Q)(tr(H^2)) >= 2 ||H8||^2.

The ready source realization is H_Y=M(Y) D_H M(Y)^dagger, namely

    H_Y8=(9Y^2,-5Y^2,1,0,-2Y,Y,-Y,0),
    N(H_Y)=294Y^4+52Y^2+4.

Transport by M(Y'-Y) preserves H=H_Y and det(H)=0 on ready histories.
There the independent reader coeff_j(H_01)/D_k equals Y/D_k=chi_k.
On arbitrary core states the field is coupled to Y; the Hermitian register
is an invertible realization/monitor and need not satisfy H_c1=Y. The new
source equation is not derived from the original source gates or native U.

Define

    E(x)=1+k+||P||^2+||W||^2+Y^2+V^2+N(H).

For y=T^epsilon x, if the inverse domain is absent or
b+E(x)-E(y)<0, reflect (x,b,epsilon)->(x,b,-epsilon). Otherwise move to
(y,b+E(x)-E(y),epsilon). Let Rev negate epsilon. PROOF.md establishes
F^(-1)=Rev F Rev on the entire unrestricted carrier, conserved E+b,
finite shells, and least period 2L on an admitted path of L vertices.

For a ready bare sequence x_n, n>=1, the sharp bank for reaching counter
N is max_(1<=n<=N) E(x_n)-E(x_1). Its last admitted counter is the largest
N whose sharp bank is at most b. This uses prefix maxima and assumes no
global monotonicity of E. The actual stored-state bound is
E(x_n)>=||P_n||^2>=D_n^2/5=(4/5)m^(n*(n-1)). It is not a lower bound for
every possible exact encoding.

## 4. Ready histories, full action and all-counter bounds

For the ten words below, u_t=w_(t+2)-w_t. P_t has ones at u_t and u_t+1
modulo five, and zero elsewhere, for t=0,1.

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

For every word and every a in (-1,0,1), the ready core at k=1 is
P=P_1,W=P_0,Y=2a,V=0,H=H_(2a). At n=0, h_0=P_0/2, chi_0=0 and
H_0=D_H; at n=1, h_1=P_1/2 and chi_1=a. The metric reader is

    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1).

The joint action uses the canonical full quadratic metric action A_2:

    A_joint[Vmetric,lapse,shift,chi]
      = A_2[Vmetric,lapse,shift]
      + (1/2) sum_(n>=1) (chi_n/m^n)<ell,Vmetric_11,n-Vmetric_22,n>
      - (1/2) sum_(n>=0) (chi_(n+1)-chi_n)^2
      + sum_(n>=1) (chi_n^2/2-a chi_n).

The register V in the integer carrier is a previous source numerator; it
is not the comparison metric Vmetric. The source kinetic term has the
opposite sign to the TT metric kinetic term. This indefinite quadratic
action is a NEW_DECLARED model, with no claim of a positive physical
matter Hamiltonian or stable quantum matter.

Variations have finite support in counters n>=1 and fix h_0 and chi_0.
The initial values h_1,chi_1 select the solution of the Euler-Lagrange
equations; they are not frozen against virtual variations at n=1.
The parameter a is held fixed and is not a functional of boundary metric
variables. Infinite sums are interpreted through finite action changes
and local Euler-Lagrange equations, not asserted convergent total actions.

Vary all six symmetric spatial metric components, lapse, shift, and chi
independently before evaluating at Vmetric=diag(h,-h,0), lapse=shift=0.
The full first variation is the metric residual times
-(delta Vmetric_11-delta Vmetric_22)/2 plus the source residual

    chi_(n+1)-chi_n+chi_(n-1)-a+<ell,h_n>/m^n

times delta chi_n. All other metric/lapse/shift gradients vanish at that
representative. Both remaining residuals vanish exactly on the coupled
recurrence. No lattice maximization replaces the source derivative.

PROOF.md uses the correct nonzero spectrum
(235 +/- 18 sqrt(5))/324 of L, its zero-sum Green bound below 5/2 on ell,
and the scalar source Green sequence taking only 0,+1,-1. Simultaneous
causal induction proves, for every n>=0 and all thirty ready histories,

    |chi_n-chi_n^0|<2/323, |chi_n|<648/323<3,
    ||h_n-h_n^free||_infty<1630/209304<1/125,
    -299/500<h_n(r)<499/500,
    det g_n(r)<-999/250000<0.

Here h^free is the canonical unforced history for the same word and
chi_n^0=a*(1,2,2,1,0,0)_n is the source oscillator with feedback disabled
(chi_0^0=0). The finite audit below checks these consequences; the
all-counter statement rests on the analytical induction.

## 5. Fixed exact witnesses

Direct source witness: word 0010, a=-1 and +1 have, at n=2,

    P2(-)=(487,167,-230,130,94), Y2(-)=-1296,
    P2(+)=(491,163,-230,130,94), Y2(+)=1296,
    D2=648, h2(+)-h2(-)=ell/162.

This contrast compares the two selected a contexts, which set both the
initial source amplitude and the constant source forcing. The reciprocal
and continued-feedback witnesses below stay within the single a=0 context.

Reciprocal witness: word 0011, a=0 has

    P0=P1=(0,1,1,0,0), Y0=Y1=0,
    P2=(94,165,165,94,130), Y2=1, D2=648,
    P3=(22236121,-2269621,-2269620,22236120,28091448),
    Y3=105047, D3=68024448.

Thus chi_2=1/648 and h3-h3^free=ell/68024448. A control retaining feedback
at n=1 but disabling it thereafter has chi_3=1/648; the fully coupled
source differs by 71/68024448 because <ell,h2>=-71/648. This is a response
to the evolved field, not solely to initial data.

For this zero-seed witness E(x1)=10, E(x2)=89378 and the sharp bank for
the first step is 89368. That bank reaches k=2 with bank zero, reflects
before k=3, and has least funded period four. Bare k=3 values are not
claimed reachable at that first-step budget.

## 6. Exact finite audit and controls

### 6.1 Authority, ring and transport

Both programs check all five normative files by size and SHA-256.
Let HF consist of zero, the positive and negative eight unit tuples
(in basis order, positive then negative), and
(1,-1,2,0,-2,1,0,1), (0,1,-1,2,1,0,-1,2): 19 fixtures.
Check closure, inverse, determinant and cost for each fixture under A,
A^(-1), and B(t) for t=-2,-1,0,1,2: 133 transport checks.
For every fixture and t=-2,-1,0,1,2, compare M(t) transport with the four
declared A/B factors, reverse it and check determinant: 95 holonomy checks.

### 6.2 Unrestricted core and funded inverse

For a=-1,0,1, i=0,...,18, and k=1,2,3 use

    P=(i-9,1,-2,0,3), W=(2,-1,0,1,9-i),
    Y=i%5-2, V=(i//5)%5-2, H=HF[i].

These give 171 (context,core) entries. Add one decreasing-energy entry
with a=0,k=1,P=(0,0,324,0,0),W=(65,29,460,29,65),Y=V=0,H=D_H.
There are exactly 172 core fixtures. For each x compute y=T(x), require
T^(-1)(y)=x and k(y)=k(x)+1. When T^(-1)(x) exists, also check its forward
image. For each z in (x,y), let delta=E(T(z))-E(z); use banks
0,1,772,max(0,delta-1),max(0,delta),max(0,delta+1) and both directions.
Check both inverse compositions, carrier membership and E+b for all
172*2*6*2=4128 funded cases. Require coverage of forward/backward motion,
forward/backward bank rejection, and absent backward domain.

For the 114 base entries with k in {1,2} (all a,i), corrupt each of the
five current P numerators and the current Y numerator of T(x) by +1,
separately. All 684 images must fail the backward congruences and reflect
at bank 1000000000. Also check k=1 lower boundaries explicitly.

### 6.3 Histories and exact action variations

Evolve all ten words in table order, a=-1,0,1, through counter 12.
There are 30*13=390 history records. Check both rational difference
equations at n=1,...,11, exact decoding, sum P_n=D_n, sum h_n=1, integral coordinates,
the Hermitian reader and ready shape, det(H)=0, the cost formula, all
bounds in section 4, and the declared storage lower bound for core counters
n>=1. The n=0 record contains the explicitly prescribed initial data.

Hash the concatenated ASCII records in word, a, n order, with exactly
one LF per record and decimal integers without leading zeroes:

    word|a|n|P0,P1,P2,P3,P4|Y|D|H0,H1,H2,H3,H4,H5,H6,H7\n

At n=0 use H=D_H and Y=0. Each implementation derives its own history.

The local action is

    A_local(v,xi)= (||v-hprev||^2+||hnext-v||^2)/2-<v,Lv>/2
                   -((xi-chiprev)^2+(chinext-xi)^2)/2
                   +xi^2/2-a xi+xi<ell,v>/m^n.

For every history and n=1,2,5,11, check all six exact central unit
differences: the five TT field coordinates and the scalar source.
All 30*4*6=720 differences must equal zero, with no tolerance.
This executable count refers to the reduced TT-plus-source action; full
metric/lapse/shift variations are proved analytically in PROOF.md.

Separately audit six off-shell cases at n=2. The first five begin with
the word-0011,a=0 solution and change only: current v_0 by +1; current xi
by +1; next chi by +1; next h_2 by +1; previous chi by -1. The sixth is
v=(1/3,-2/5,0,3/7,-1), xi=-2/3, hprev=(0,0,0,0,0),
hnext=(1,1,1,1,1), chiprev=1/2, chinext=-3/4, a=1.
For each case, all six central differences must equal the independently
derived gradients

    g_h=2v-hprev-hnext-Lv+xi ell/m^n,
    g_chi=chinext-xi+chiprev-a+<ell,v>/m^n.

Require a nonzero gradient in each case: 36 off-shell derivative checks.
These include both mixed derivatives and the source residual sign that
was not tested off shell in #1644.

### 6.4 Negative controls and complete funded cycles

Use separately labelled comparison contexts only; the main law is fixed:

1. Disable field-to-source feedback: word0011,a=0 keeps chi=0 and h free;
   its continuous joint source derivative at n=1 is -1/648, not zero.
2. Disable feedback after its first step: the chi_3 contrast is
   71/68024448 as in section 5.
3. Disable source-to-field coupling while retaining feedback: word0011,
   a=0 keeps h free, but its metric gradient at n=2 is ell/68024448.
4. Reverse the feedback sign: the source gradient at word0011,a=0,n=1
   is -1/324, not zero.
5. Omit the Hermitian transport: at word0011,a=0,k=2 the reader H_c1
   no longer equals Y=1.
6. Use the incorrect first inverse divisor m^2: the valid word0011,a=0
   first image is rejected, whereas the exact inverse recovers its seed.
7. On unrestricted core P=(2,0,0,0,0),k=1, the metric has a zero diagonal
   entry and determinant zero. This keeps the ready-domain restriction
   of the Lorentz claim explicit.

For each seed (0010,-1), (0010,+1), (0011,0), and each target N=1,2,3,
set the bank to max_(1<=n<=N)E(x_n)-E(x_1). Require E(x_(N+1)) to exceed
that peak, then traverse the funded orbit through its first return with
no earlier repetition. The nine periods, in this order, must be
2,4,6,2,4,6,2,4,6. These banks are fixed by a prospective formula, not
chosen after a run. Also check bank 89367 rejects the first zero-seed
step while bank 89368 admits it with zero residual.

## 7. Certificate grammar and completion

Each implementation emits this same 19-line certificate as raw ASCII
bytes with exactly one LF after every line, including the last:

    CERTIFICATE=P-INTEGER-JOINT-VARIATION-1
    AUTHORITY_FILES=5
    TRANSPORT_CHECKS=133
    HOLONOMY_CHECKS=95
    CORE_FIXTURES=172
    FUNDED_CASES=4128
    IMAGE_DEFECTS=684
    HISTORY_RECORDS=390
    HISTORY_SHA256=<computed lowercase SHA-256>
    JOINT_VARIATIONS=720
    OFFSHELL_VARIATIONS=36
    DIRECT_CONTRAST=1/162,-1/162,0,0,0
    ZERO_SOURCE_CHI2=1/648
    RECIPROCAL_CONTRAST=1/68024448,-1/68024448,0,0,0
    CONTINUED_SOURCE_CONTRAST=71/68024448
    ZERO_SOURCE_FIRST_BANK=89368
    CYCLE_PERIODS=2,4,6,2,4,6,2,4,6
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

The primary runs breaker.py using the same Python executable with -I in
a separate process, requiring exit zero, empty stderr and unmodified
certificate byte identity. It then appends two lines:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Only a ScientificFailure with a registered key is caught. It emits
FALSIFIER=<key> and RESULT=FAIL, with the actual child stdout hex also
preserved for BREAKER_BYTES. Runtime/protocol errors remain nonzero.
Registered keys: AUTHORITY, RING, TRANSPORT, HOLONOMY, COST, INITIAL_DATA,
INTEGER, BARE_INVERSE, FUNDED_INVERSE, CONSERVATION, BRANCH, IMAGE_GUARD,
RECURRENCE, MEAN, SOURCE_READER, LORENTZ, RESPONSE_BOUND, SOURCE_BOUND,
ACTION, OFFSHELL_ACTION, FIXED_COUNTER, CONTROL, SHARP_BUDGET, PERIOD,
CERTIFICATE, BREAKER_BYTES.

After the first completed gate, preserve exact EXPECTED.txt and a factual
RUN.md/RESULT.md. Open one draft PR for the unchanged repository workflow
to replay on x86_64 and aarch64 with Python 3.12. No claim of Canon
promotion, full nonlinear Einstein dynamics, physically acceptable matter,
native-U realization, minimal precision cost or continuum limit follows.
