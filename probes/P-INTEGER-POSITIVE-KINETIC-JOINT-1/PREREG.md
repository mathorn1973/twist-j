# P-INTEGER-POSITIVE-KINETIC-JOINT-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3  
Ownership: https://github.com/mathorn1973/twist-j/issues/1647

## 1. Question, authority and custody

Can the linear TT metric sector and a dynamical scalar source satisfy both
continuous Euler-Lagrange equations simultaneously from a joint quadratic action
whose source kinetic sign is **positive** (matching the TT metric kinetic sign),
yielding an action-derived strictly positive-definite quadratic physical
Hamiltonian obeying an exact discrete Noether energy-work law and an identically
conserved positive-signature canonical symplectic form, while every stored state
coordinate is an integer on an unrestricted 21/23-coordinate reversible carrier
with an all-counter Lorentzian metric domain on the thirty ready histories?

Public Canon v103 is active at main and peeled canon-v103 commit
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md records the five actual
normative hashes and sizes; both implementations verify those local bytes.
canon/CANON.md is 1052518 bytes, SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.

In the predecessor probe P-INTEGER-JOINT-VARIATION-1 (Draft PR #1646, issue
#1645, pin fe5456f1aac8adcc3fdb0222df81f7e2fc773977, result head
d4a707bd1ecab7d839e2d32371aed7bde6885f31), continuous joint metric-and-source
stationarity and sustained every-step feedback were established with an explicit
negative relative kinetic sign on the scalar source action. This probe resolves
that limitation by giving the scalar source a positive kinetic term and proving
positivity of the resulting action-derived quadratic Hamiltonian, its exact
Noether work balance, and exact conservation of the positive-signature
symplectic Wronskian.

Before any scientific execution or import, freeze PREREG.md, PROOF.md,
SOURCE.md, verify.py, breaker.py and FROZEN.sha256, publish the pin and read
all six files back from GitHub. Static reading, AST parsing and file hashing
are allowed before that point. No frozen file will change after execution. Both
implementations compare exact quantities, with no floating point, rounding,
clipping, fitting, selected seeds or numerical tolerances.

## 2. Positive-kinetic coupled equations and integer carrier

Let m=324, ell=(1,-1,0,0,0), e=(1,1,1,1,1), and

    (C P)_r = 460 P_r + 29(P_(r-1) + P_(r+1)) + 65(P_(r-2) + P_(r+2)),
    L = (648 I - C)/324.

Spatial indices are modulo five. The source context a is fixed in {-1,0,1}.
The positive-kinetic coupled Euler-Lagrange equations for all n>=1 are

    h_(n+1) - 2 h_n + h_(n-1) + L h_n = chi_n ell / m^n,
    chi_(n+1) - chi_n + chi_(n-1) = a + <ell, h_n> / m^n.

Here h_n is a rational five-vector and chi_n a rational scalar. Define the
sufficient common integer scale

    D_n = 2 * m^(n*(n-1)/2) for n>=0,
    P_n = D_n h_n, Y_n = D_n chi_n.

In particular D_0=D_1=2. This common scale is sufficient, not asserted
primitive or optimal.

The unrestricted core is x=(P,W,Y,V,H,k), where P,W are arbitrary integer
five-vectors, Y,V are arbitrary integers, H is an arbitrary eight-integer
Hermitian register defined below, and k>=1. There are 21 integer core
coordinates. With bank b>=0 and direction epsilon in {-1,1}, the funded carrier
has 23 integer coordinates.

The single combined macro-step, with r_k=m^(2*k-1), is

    P' = m^(k-1) C P - r_k W + Y ell,
    Y' = m^k Y - r_k V + a D_(k+1) + <ell, P>,
    W' = P, V' = Y, k' = k + 1,
    H' = M(Y' - Y) H M(Y' - Y)^dagger.

Notice that the current-slice coupling matrix

    A_k^+ = [[m^(k-1) C, ell], [ell^T, m^k]]

is symmetric with respect to the positive-definite Euclidean metric I_6.

For a candidate x' with k'>=2, put n=k'-1. Its predecessor exists if and only
if all six entries of the following numerators are divisible by r_n:

    W_prev = (m^(n-1) C W' + V' ell - P') / r_n,
    V_prev = (m^n V' + a D_(n+1) + <ell, W'> - Y') / r_n.

Then P_prev=W', Y_prev=V', k_prev=n, and

    H_prev = M(V' - Y') H' M(V' - Y')^dagger.

At k'=1 no backward step exists. H adds no congruence restriction.

## 3. Cyclotomic realization and positive admission account

Use O=Z[j], 1+j+j^2+j^3+j^4=0, conjugation j*=j^4, phi=-j^2-j^3, J=1+j^2,
J^(-1)=-j-j^2, phi^(-1)=phi-1, A=diag(J,phi), B(t)=[[1,t],[0,1]], and
D_H=diag(0,1). Then

    v = J/phi - 1 = -2 + j - j^2, v v* = 9 - 5 phi,
    M(t) = A B(t) A^(-1) B(-t) = [[1, t v], [0, 1]].

An H8 tuple (a0,a1,d0,d1,c0,c1,c2,c3) denotes

    H = [[a0 + a1 phi, c], [c*, d0 + d1 phi]],
    c = c0 + c1 j + c2 j^2 + c3 j^3.

Its positive arithmetic trace cost is

    N(H) = 4 a0^2 + 4 a0 a1 + 6 a1^2 + 4 d0^2 + 4 d0 d1 + 6 d1^2
           + 10 sum(c_i^2) - 2(sum c_i)^2
         = Tr_(Q(j)/Q)(tr(H^2)) >= 2 ||H8||^2.

The ready source realization is H_Y = M(Y) D_H M(Y)^dagger, namely

    H_Y8 = (9 Y^2, -5 Y^2, 1, 0, -2 Y, Y, -Y, 0),
    N(H_Y) = 294 Y^4 + 52 Y^2 + 4.

Transport by M(Y'-Y) preserves H=H_Y and det(H)=0 on ready histories, where
coeff_j(H_01)/D_k = Y/D_k = chi_k.

Define the admission account

    E(x) = 1 + k + ||P||^2 + ||W||^2 + Y^2 + V^2 + N(H).

For y=T^epsilon x, if the inverse domain is absent or b+E(x)-E(y)<0, reflect
(x,b,epsilon)->(x,b,-epsilon). Otherwise move to (y,b+E(x)-E(y),epsilon). Let
Rev negate epsilon. PROOF.md establishes F^(-1)=Rev F Rev on the entire
unrestricted carrier, conserved E+b, finite shells, and least period 2L on an
admitted path of L vertices.

## 4. Positive-kinetic joint action, physical Hamiltonian and symplectic form

For the ten canonical words below, u_t=w_(t+2)-w_t. P_t has ones at u_t and
u_t+1 modulo five, and zero elsewhere, for t=0,1.

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
P=P_1, W=P_0, Y=2a, V=0, H=H_(2a). At n=0, h_0=P_0/2, chi_0=0 and H_0=D_H; at
n=1, h_1=P_1/2 and chi_1=a. The metric reader is

    g_n(r) = diag(-1, 1 + h_n(r), 1 - h_n(r), 1).

### 4.1 Positive-kinetic joint action

The joint action adds a positive-kinetic discrete Klein-Gordon source action to
the canonical full quadratic metric action A_2:

    A_pos[Vmetric, lapse, shift, chi]
      = A_2[Vmetric, lapse, shift]
      + (1/2) sum_(n>=0) (chi_(n+1) - chi_n)^2
      - sum_(n>=1) (chi_n^2 / 2 - a chi_n)
      + (1/2) sum_(n>=1) (chi_n / m^n) <ell, Vmetric_11,n - Vmetric_22,n>.

On the TT representative Vmetric_n=diag(h_n,-h_n,0), lapse=shift=0, the joint
kinetic form is strictly positive-definite:

    T_n(Delta h_n, Delta chi_n) = (1/2) ||Delta h_n||^2 + (1/2) (Delta chi_n)^2.

Vary all six symmetric spatial metric components, lapse, shift, and chi
independently for finite-support perturbations in n>=1 (fixing h_0 and chi_0,
with h_1 and chi_1 selecting the solution without being frozen against virtual
variations at n=1) before evaluating at Vmetric=diag(h,-h,0), lapse=shift=0.
The full first variation is

    delta A_pos
      = -(1/2) sum_(n>=1) <(Delta_c^2 + L) h_n - chi_n ell / m^n,
                           delta Vmetric_11,n - delta Vmetric_22,n>
      - sum_(n>=1) [(Delta_c^2 + 1) chi_n - a - <ell, h_n> / m^n] delta chi_n.

All other metric, lapse and shift gradients vanish at the TT representative,
and both remaining Euler-Lagrange residuals vanish identically on the coupled
positive-kinetic recurrence.

### 4.2 Action-derived positive-definite physical Hamiltonian and Noether work law

For each bond (n-1,n) with n>=1, define the zero-sum metric perturbation
htilde_t = h_t - (1/5) e and shifted source chitilde_t = chi_t - a, together
with bond differences and midpoints

    u_h = h_n - h_(n-1), v_h = (htilde_n + htilde_(n-1)) / 2,
    u_chi = chi_n - chi_(n-1), v_chi = (chitilde_n + chitilde_(n-1)) / 2.

The action-derived quadratic physical Hamiltonian is

    H_phys,n = H_h,n + H_chi,n,
    H_h,n   = (1/2) ||h_n - h_(n-1)||^2 + (1/2) <h_(n-1), L h_n>
            = (1/2) <u_h, (I - L/4) u_h> + (1/2) <v_h, L v_h>,
    H_chi,n = (1/2) (chi_n - chi_(n-1))^2 + (1/2) (chi_(n-1) - a)(chi_n - a)
            = (3/8) u_chi^2 + (1/2) v_chi^2.

Because L on e^perp has eigenvalues (235 +/- 18 sqrt(5))/324 in (1/2, 1), both
H_h,n and H_chi,n are strictly positive-definite on (e^perp)^2 and R^2:

    H_h,n   >= (3/8) ||u_h||^2 + (1/4) ||v_h||^2 >= 0,
    H_chi,n >= (1/4) (chitilde_n^2 + chitilde_(n-1)^2) >= 0.

Along every solution of the positive-kinetic coupled recurrence, H_phys,n obeys
the exact discrete Noether energy-work identity for all n>=1:

    H_phys,n+1 - H_phys,n
      = (chi_n / m^n) <ell, (h_(n+1) - h_(n-1)) / 2>
      + (<ell, h_n> / m^n) ((chi_(n+1) - chi_(n-1)) / 2).

When the coupling is disabled, H_phys,n+1 = H_phys,n for all n>=1.

### 4.3 Positive-signature canonical symplectic Wronskian conservation

For any two solutions z^(1)=(h^(1),chi^(1)) and z^(2)=(h^(2),chi^(2)) of the
homogeneous coupled system (in particular, all ready histories in context a=0),
define on bond (n-1,n) for n>=1:

    Omega_h,n(z^(1), z^(2))   = <h_(n-1)^(1), h_n^(2)> - <h_n^(1), h_(n-1)^(2)>,
    Omega_chi,n(z^(1), z^(2)) = chi_(n-1)^(1) chi_n^(2) - chi_n^(1) chi_(n-1)^(2),
    Omega_n^+(z^(1), z^(2))   = Omega_h,n(z^(1), z^(2)) + Omega_chi,n(z^(1), z^(2)).

Because the positive-kinetic coupling is symmetric in the positive inner
product, the metric and source Wronskian increments cancel identically at every
step:

    Omega_(n+1)^+(z^(1), z^(2)) = Omega_n^+(z^(1), z^(2)) = Omega_1^+(z^(1), z^(2))

for all n>=1, even though Omega_h,n and Omega_chi,n individually vary with n.

### 4.4 All-counter causal bounds and Lorentz signature

Simultaneous causal induction in PROOF.md establishes, for every n>=0 and all
thirty ready histories:

    |chi_n - chi_n^0| < 2/323, |chi_n| < 648/323 < 3,
    ||h_n - h_n^free||_infty < 1630/209304 < 1/125,
    -299/500 < h_n(r) < 499/500,
    det g_n(r) < -999/250000 < 0,

where h^free is the canonical unforced history for the same word and
chi_n^0 = a*(1,2,2,1,0,0)_n (with chi_0^0=0).

## 5. Fixed exact witnesses

Direct source witness: word 0010, a=-1 and +1 have, at n=2,

    P2(-) = (487,167,-230,130,94), Y2(-) = -1296,
    P2(+) = (491,163,-230,130,94), Y2(+) = 1296,
    D2 = 648, h2(+) - h2(-) = ell / 162.

Positive-kinetic reciprocal witness: word 0011, a=0 has

    P0 = P1 = (0,1,1,0,0), Y0 = Y1 = 0,
    P2 = (94,165,165,94,130), Y2 = -1, D2 = 648,
    P3 = (22236119,-2269619,-2269620,22236120,28091448),
    Y3 = -105047, D3 = 68024448.

Thus chi_2 = -1/648 and h3 - h3^free = -ell / 68024448. A control retaining
feedback at n=1 but disabling it thereafter has chi_3 = -1/648; the fully
coupled positive-kinetic source has chi_3 = -105047/68024448, so

    chi_3^pos - chi_3^first-only = -71 / 68024448.

Along this zero-seed witness, the action-derived physical Hamiltonian has

    H_phys,1 = 53 / 432,
    H_chi,2  = 1 / 839808 > 0,
    H_phys,2 - H_phys,1 = 1 / 839808 > 0.

And for the pair of zero-seed histories (0010, a=0) and (0011, a=0), at n=3:

    Omega_h,3 - Omega_h,2     = -1 / 136048896,
    Omega_chi,3 - Omega_chi,2 = +1 / 136048896,
    Omega_3^+ = Omega_2^+ = Omega_1^+ = 1 / 4.

For the zero-seed witness (0011, a=0), E(x1)=10, E(x2)=89378 and the sharp
first-step bank is 89368 (89367 reflects).

## 6. Exact finite audit and controls

### 6.1 Authority, ring and transport

Both programs check all five normative files by size and SHA-256. Use the 19
Hermitian fixtures HF (zero, the positive and negative eight unit tuples in
basis order, and (1,-1,2,0,-2,1,0,1), (0,1,-1,2,1,0,-1,2)): 133 transport
checks under A, A^(-1), and B(t) for t=-2,-1,0,1,2, plus 95 holonomy checks
under M(t).

### 6.2 Unrestricted core and funded inverse

Use the 171 base (a,core) fixtures (a=-1,0,1; i=0,...,18; k=1,2,3) with
P=(i-9,1,-2,0,3), W=(2,-1,0,1,9-i), Y=i%5-2, V=(i//5)%5-2, H=HF[i], plus the
decreasing-energy fixture a=0, k=1, P=(0,0,324,0,0), W=(65,29,460,29,65),
Y=V=0, H=D_H: 172 core fixtures and 172*2*6*2=4128 funded cases across all five
motion/reflection branches, plus 114*6=684 corrupted-image rejection checks.

### 6.3 Histories, joint action variations, Hamiltonian and symplectic audits

Evolve all ten words in table order, a=-1,0,1, through counter 12: 30*13=390
history records, hashed in word, a, n order as

    word|a|n|P0,P1,P2,P3,P4|Y|D|H0,H1,H2,H3,H4,H5,H6,H7\n

The local positive-kinetic action is

    A_local(v,xi) = (||v-hprev||^2 + ||hnext-v||^2)/2 - <v,Lv>/2
                    + ((xi-chiprev)^2 + (chinext-xi)^2)/2
                    - xi^2/2 + a xi + xi <ell,v> / m^n.

For every history and n=1,2,5,11, check all six exact central unit differences:
30*4*6=720 vanishing joint variations.

Audit six off-shell cases at n=2 (the five unit shifts from word 0011, a=0
plus v=(1/3,-2/5,0,3/7,-1), xi=-2/3, hprev=(0,)*5, hnext=(1,)*5, chiprev=1/2,
chinext=-3/4, a=1) against the exact positive-kinetic gradients

    g_h   = 2 v - hprev - hnext - L v + xi ell / m^n,
    g_chi = xi - chiprev - chinext + a + <ell,v> / m^n:

36 nonzero off-shell derivative checks.

Audit the action-derived physical Hamiltonian H_phys,n across all 30 ready
histories:
- For all 12 bonds n=1,...,12 (30*12=360 checks): verify the exact sum-of-squares
  identity for H_h,n and H_chi,n, the coercive bounds
  H_h,n >= (3/8)||u_h||^2 + (1/4)||v_h||^2 and
  H_chi,n >= (1/4)(chitilde_n^2 + chitilde_(n-1)^2), and strict positivity
  H_phys,n > 0.
- For all 11 steps n=1,...,11 (30*11=330 checks): verify the exact discrete
  Noether work identity for H_phys,n+1 - H_phys,n.
- For all 30 uncoupled histories across n=1,...,11 (30 trajectory conservation
  checks): verify H_phys,n == H_phys,1 for every n=1,...,12.
This gives 360+330+30=720 Hamiltonian checks.

Audit the positive-signature canonical symplectic Wronskian Omega_n^+ across
all 45 unordered word pairs (w_1, w_2) in context a=0 and all 12 bonds
n=1,...,12: require Omega_n^+(z^(w_1), z^(w_2)) == Omega_1^+(z^(w_1), z^(w_2))
at every bond, giving 45*12=540 symplectic checks.

### 6.4 Negative controls and complete funded cycles

Check seven negative controls:
1. Disable field-to-source feedback at word 0011, a=0: chi stays 0 and the
   continuous positive-kinetic source gradient at n=1 is -1/648 != 0.
2. Disable feedback after n=1: chi_3^pos - chi_3^first-only = -71/68024448.
3. Disable source-to-field coupling while retaining feedback: h stays free, and
   the metric gradient at n=2 is -ell/68024448 != 0.
4. Use the negative-kinetic source recurrence (feedback=-1, as in #1646): its
   positive-kinetic source gradient at word 0011, a=0, n=1 is -1/324 != 0, its
   indefinite Wronskian fails Omega_3^+ == Omega_1^+ on the positive-kinetic
   trajectories (leaving residual -1/68024448), and its negative-kinetic source
   energy at n=2 is -1/839808 < 0.
5. Omit Hermitian transport at word 0011, a=0, k=2: H_c1=0 != Y_2=-1.
6. Use incorrect first inverse divisor m^2: rejects valid first image while
   exact divisor m recovers the seed.
7. Unrestricted core P=(2,0,0,0,0), k=1: degenerate metric diag(-1,2,0,1) with
   determinant zero.

Check the nine complete funded cycles for seeds (0010,-1), (0010,+1), (0011,0)
and targets N=1,2,3: least periods 2,4,6,2,4,6,2,4,6.

## 7. Certificate grammar and completion

Each implementation emits this same 23-line certificate as raw ASCII bytes with
exactly one LF after every line, including the last:

    CERTIFICATE=P-INTEGER-POSITIVE-KINETIC-JOINT-1
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
    HAMILTONIAN_CHECKS=720
    SYMPLECTIC_CHECKS=540
    DIRECT_CONTRAST=1/162,-1/162,0,0,0
    ZERO_SOURCE_CHI2=-1/648
    RECIPROCAL_CONTRAST=-1/68024448,1/68024448,0,0,0
    CONTINUED_SOURCE_CONTRAST=-71/68024448
    ZERO_SOURCE_WORK1=1/839808
    SYMPLECTIC_EXCHANGE3=-1/136048896,1/136048896,1/4
    ZERO_SOURCE_FIRST_BANK=89368
    CYCLE_PERIODS=2,4,6,2,4,6,2,4,6
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

The primary runs breaker.py using the same Python executable with -I in a
separate process, requiring exit zero, empty stderr and unmodified 23-line
certificate byte identity. It then appends two lines:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Registered falsifier keys: AUTHORITY, RING, TRANSPORT, HOLONOMY, COST,
INITIAL_DATA, INTEGER, BARE_INVERSE, FUNDED_INVERSE, CONSERVATION, BRANCH,
IMAGE_GUARD, RECURRENCE, MEAN, SOURCE_READER, LORENTZ, RESPONSE_BOUND,
SOURCE_BOUND, ACTION, OFFSHELL_ACTION, HAMILTONIAN, SYMPLECTIC, FIXED_COUNTER,
CONTROL, SHARP_BUDGET, PERIOD, CERTIFICATE, BREAKER_BYTES.
