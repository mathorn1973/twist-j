# Proofs for P-INTEGER-POSITIVE-KINETIC-JOINT-1

Scope: NON-CANONICAL, L1.  
Ownership: https://github.com/mathorn1973/twist-j/issues/1647.

This document proves the positive-kinetic coupled metric-and-source equations,
their exact integer storage and unrestricted 6-congruence partial inverse, the
23-coordinate funded bijection, simultaneous first-order stationarity of the
full metric and scalar source under the positive-kinetic joint action A_pos,
strict positive-definiteness and the exact discrete Noether energy-work law of
the action-derived quadratic physical Hamiltonian H_phys,n, exact conservation
of the positive-signature canonical symplectic Wronskian Omega_n^+, and the
all-counter causal bounds and exact witnesses stated in PREREG.md.

The public reference is Public Canon v103 at main and peeled canon-v103 commit
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. DEF-K1-LINEAR-METRIC supplies the
unforced five-site recurrence and full quadratic metric action A_2, and
K1-LINEAR-METRIC-COMPLETION supplies the unforced bound used in Section 6.

## 1. Cyclotomic arithmetic, transport, and source realization

Let O=Z[j] with 1+j+j^2+j^3+j^4=0 and conjugation j*=j^4. Set phi=-j^2-j^3 and
J=1+j^2. Then

    phi^2 = phi + 1, phi^(-1) = phi - 1,
    J^(-1) = -j - j^2, J * phi = j.

Consequently A=diag(J,phi) and A^(-1) have entries in O, and B(t)=[[1,t],[0,1]]
has inverse B(-t) for every integer t.

For c=c0+c1*j+c2*j^2+c3*j^3, conjugation is

    conjugate(c) = (c0 - c1) - c1*j + (c3 - c1)*j^2 + (c2 - c1)*j^3,

whose fixed elements have c1=0 and c2=c3, namely Z[phi]. Thus the eight
integer coordinates (a0,a1,d0,d1,c0,c1,c2,c3) parameterize all of Herm_2(O),
and congruence by A, A^(-1), and B(t) preserves Herm_2(O) and det(H) because
det(B(t))=1 and det(A)*conjugate(det(A))=j*conjugate(j)=1.

Direct multiplication gives the commutator group

    M(t) = A * B(t) * A^(-1) * B(-t) = [[1, t * v], [0, 1]],
    v = J/phi - 1 = -2 + j - j^2,
    v * conjugate(v) = 9 - 5 * phi =: w,

with M(s)*M(t)=M(s+t) and M(t)^(-1)=M(-t). For D_H=diag(0,1), the ready source
matrix H_Y = M(Y) * D_H * M(Y)^dagger has eight-coordinate tuple

    (H_Y)_8 = (9*Y^2, -5*Y^2, 1, 0, -2*Y, Y, -Y, 0),
    coeff_j((H_Y)_01) = Y,
    det(H_Y) = 0,

and satisfies M(Y'-Y) * H_Y * M(Y'-Y)^dagger = H_(Y').

For K=Q(j), Tr_(K/Q)(1)=4, Tr_(K/Q)(j^t)=-1 (t=1,2,3,4), and Tr_(K/Q)(phi)=2,
giving the positive trace cost

    N(H) = Tr_(K/Q)(tr(H^2))
         = 4*a0^2 + 4*a0*a1 + 6*a1^2 + 4*d0^2 + 4*d0*d1 + 6*d1^2
           + 10*sum_i c_i^2 - 2*(sum_i c_i)^2
         >= 2 * ||H8||_2^2,

with N(H)=0 if and only if H=0, and on the ready family

    N(H_Y) = 294*Y^4 + 52*Y^2 + 4.

## 2. Positive-kinetic integer lift and unrestricted partial inverse

Let m=324, ell=(1,-1,0,0,0), e=(1,1,1,1,1), and let C be the symmetric
circulant matrix with first row (460,29,65,65,29). Put L=(648*I-C)/324. For
fixed context a in {-1,0,1}, the positive-kinetic coupled Euler-Lagrange
equations for n>=1 are

    (Delta_c^2 + L) h_n = chi_n * ell / m^n,
    (Delta_c^2 + 1) chi_n = a + <ell, h_n> / m^n,            (2.1)

where Delta_c^2 f_n = f_(n+1) - 2*f_n + f_(n-1).

### 2.1 Common scale and symmetric integer recurrence

Define D_n = 2 * m^(n*(n-1)/2) for n>=0, so D_0=D_1=2 and for all n>=1:

    D_(n+1) / D_n = m^n,
    D_(n+1) / D_(n-1) = r_n = m^(2*n-1).

Multiplying (2.1) by D_(n+1) and setting P_n = D_n * h_n, Y_n = D_n * chi_n
yields the exact integer recurrence

    P_(n+1) = m^(n-1) * C * P_n - r_n * P_(n-1) + Y_n * ell,
    Y_(n+1) = m^n * Y_n - r_n * Y_(n-1) + a * D_(n+1) + <ell, P_n>.   (2.2)

Unlike the indefinite model in #1646, the current-slice linear operator in
(2.2),

    A_n^+ = [[m^(n-1) * C, ell], [ell^T, m^n]],

is symmetric with respect to the positive-definite Euclidean inner product on
R^5 x R (kinetic metric G_kin = diag(I_5, +1) = I_6).

### 2.2 Unrestricted 21-coordinate core and 6-congruence partial inverse

On the unrestricted 21-coordinate core x=(P,W,Y,V,H,k) in
Z^5 x Z^5 x Z x Z x Herm_2(O) x Z_(>=1), the macro-step T(x) is defined by

    P' = m^(k-1) * C * P - r_k * W + Y * ell,
    Y' = m^k * Y - r_k * V + a * D_(k+1) + <ell, P>,
    W' = P, V' = Y, k' = k + 1,
    H' = M(Y' - Y) * H * M(Y' - Y)^dagger.                   (2.3)

For a candidate x'=(P',W',Y',V',H',k') with k'>=2, put n=k'-1. Any predecessor
x under T must have P=W', Y=V', k=n, and therefore must satisfy

    W = (m^(n-1) * C * W' + V' * ell - P') / r_n,
    V = (m^n * V' + a * D_(n+1) + <ell, W'> - Y') / r_n,
    H = M(V' - Y') * H' * M(V' - Y')^dagger.                 (2.4)

Hence a predecessor exists if and only if all five components of
m^(n-1)*C*W'+V'*ell-P' and the scalar m^n*V'+a*D_(n+1)+<ell,W'>-Y' are
divisible by r_n = m^(2*n-1). At k'=1 no predecessor exists. Thus T is injective
on the entire unrestricted core, and (2.4) is its exact partial inverse on its
image. Corrupting any single entry of (P',Y') by +1 shifts the corresponding
numerator in (2.4) by -1, which cannot be divisible by r_n >= 324.

Since C*e = 648*e = 2*m*e and <e,ell> = 0, summing the five coordinates of the
first equation in (2.1) gives sum h_(n+1) - 2*sum h_n + sum h_(n-1) = 0. Because
sum h_0 = sum h_1 = 1 on all ten canonical words, sum h_n = 1 and sum P_n = D_n
hold for all n>=0.

## 3. Funded bijection, finite shells, and sharp horizons

With E(x) = 1 + k + ||P||_2^2 + ||W||_2^2 + Y^2 + V^2 + N(H), bank b>=0, and
direction epsilon in {-1,+1}, the funded update F(x,b,epsilon) moves to
(y, b+E(x)-E(y), epsilon) when y=T^epsilon(x) exists and b+E(x)-E(y)>=0, and
reflects to Rev(x,b,epsilon)=(x,b,-epsilon) otherwise. By the exact partial
invertibility of T in Section 2, Rev*F*Rev*F = identity on the entire
unrestricted 23-coordinate funded carrier, conserving E+b. Every shell E+b=M is
finite, every admitted path of L vertices has least period 2*L, and on any
ready trajectory x_1,x_2,... the sharp bank required to reach counter N is
B_sharp(N) = max_(1<=n<=N) E(x_n) - E(x_1). Mean conservation sum P_n = D_n and
Cauchy-Schwarz give E(x_n) >= ||P_n||_2^2 >= D_n^2/5 = (4/5)*m^(n*(n-1)) for
all n>=1.

## 4. Positive-kinetic joint action, physical Hamiltonian, and symplectic law

### 4.1 Full joint action and simultaneous continuous stationarity

Keep all six independent components of the symmetric spatial metric perturbation
Vmetric, the lapse ell_0, and the three shifts N_i in the canonical quadratic
metric action A_2[Vmetric,ell_0,N] before evaluating on the TT representative.
Define the positive-kinetic joint action

    A_pos[Vmetric, ell_0, N, chi]
      = A_2[Vmetric, ell_0, N]
      + (1/2) * sum_(n>=0) (chi_(n+1) - chi_n)^2
      - sum_(n>=1) [chi_n^2 / 2 - a * chi_n]
      + (1/2) * sum_(n>=1) (chi_n / m^n) * <ell, Vmetric11_n - Vmetric22_n>.  (4.1)

For finite-support perturbations in n>=1 (fixing h_0 and chi_0 at n=0, while
h_1 and chi_1=a select the solution of the Euler-Lagrange equations without
being frozen against virtual variations at n=1), summation by parts on the
positive source kinetic term gives

    delta [ (1/2) * sum_(n>=0) (chi_(n+1) - chi_n)^2 ]
      = - sum_(n>=1) (Delta_c^2 chi_n) * delta chi_n,

while delta [ - sum_(n>=1) (chi_n^2 / 2 - a * chi_n) ] = - sum_(n>=1) (chi_n - a) * delta chi_n,
and the interaction contributes +(1/2)*sum_(n>=1) <chi_n*ell/m^n, delta Vmetric11_n - delta Vmetric22_n>
+ sum_(n>=1) (<ell, Vmetric11_n - Vmetric22_n>/(2*m^n)) * delta chi_n.
Evaluating at the TT representative Vmetric_n = diag(h_n, -h_n, 0), ell_0 = 0,
N_i = 0, where (Vmetric11_n - Vmetric22_n)/2 = h_n and all longitudinal, trace,
off-diagonal, lapse and shift gradients of A_2 vanish identically, we obtain

    delta A_pos
      = -(1/2) * sum_(n>=1) <(Delta_c^2 + L) h_n - chi_n * ell / m^n,
                             delta Vmetric11_n - delta Vmetric22_n>
      - sum_(n>=1) [(Delta_c^2 + 1) chi_n - a - <ell, h_n> / m^n] * delta chi_n.  (4.2)

Both continuous Euler-Lagrange residuals vanish if and only if (h_n, chi_n)
satisfies (2.1).

At a fixed counter n>=1 with neighbors held fixed, the reduced local action is

    A_local(v, xi)
      = (||v - hprev||^2 + ||hnext - v||^2) / 2 - <v, L * v> / 2
      + ((xi - chiprev)^2 + (chinext - xi)^2) / 2
      - xi^2 / 2 + a * xi + xi * <ell, v> / m^n.             (4.3)

Its exact gradients for arbitrary off-shell comparison values (v, xi) are

    grad_v A_local = 2*v - hprev - hnext - L*v + xi*ell / m^n,
    d_xi A_local   = xi - chiprev - chinext + a + <ell, v> / m^n.  (4.4)

Because A_local is quadratic with strictly positive-definite Hessian
diag(2*I_5 - L, +1) + O(m^(-n)), every central unit difference equals the exact
derivative (4.4).

### 4.2 Action-derived positive-definite physical Hamiltonian and Noether work law

On the zero-sum dynamical metric perturbation htilde_t = h_t - (1/5)*e in e^perp
and shifted source chitilde_t = chi_t - a in R, the homogeneous wave-oscillator
operators are Delta_c^2 + L and Delta_c^2 + 1. For any symmetric operator K and
bond variables u = q_n - q_(n-1), v = (q_n + q_(n-1))/2, the algebraic identity

    <q_(n-1), K * q_n> = <v - u/2, K * (v + u/2)> = <v, K * v> - (1/4) * <u, K * u>

shows that the bond quadratic form

    H_K(q_(n-1), q_n) := (1/2) * ||q_n - q_(n-1)||^2 + (1/2) * <q_(n-1), K * q_n>

equals the sum of squares

    H_K(q_(n-1), q_n) = (1/2) * <u, (I - K/4) * u> + (1/2) * <v, K * v>.    (4.5)

Applying (4.5) to K=L on e^perp (where 1/2 < lambda_- < lambda_+ < 1, so
I - L/4 >= (3/4)*I and L >= (1/2)*I) and to K=1 on R (where 1 - 1/4 = 3/4)
proves that the action-derived physical Hamiltonian

    H_phys,n = H_h,n + H_chi,n,
    H_h,n    = (1/2) * ||h_n - h_(n-1)||^2 + (1/2) * <h_(n-1), L * h_n>,
    H_chi,n  = (1/2) * (chi_n - chi_(n-1))^2 + (1/2) * (chi_(n-1) - a) * (chi_n - a)  (4.6)

satisfies the exact sum-of-squares decomposition and coercive lower bounds

    H_h,n   = (1/2) * <u_h, (I - L/4) * u_h> + (1/2) * <v_h, L * v_h>
           >= (3/8) * ||u_h||^2 + (1/4) * ||v_h||^2 >= 0,
    H_chi,n = (3/8) * u_chi^2 + (1/2) * v_chi^2
            = (1/2) * (chitilde_n^2 - chitilde_n * chitilde_(n-1) + chitilde_(n-1)^2)
           >= (1/4) * (chitilde_n^2 + chitilde_(n-1)^2) >= 0.               (4.7)

Furthermore, for any sequence q_t,

    H_K(q_n, q_(n+1)) - H_K(q_(n-1), q_n)
      = (1/2) * (||q_(n+1) - q_n||^2 - ||q_n - q_(n-1)||^2)
        + (1/2) * <q_(n+1) - q_(n-1), K * q_n>
      = <(Delta_c^2 + K) q_n, (q_(n+1) - q_(n-1)) / 2>.                     (4.8)

Summing (4.8) over the metric and source sectors and substituting the
Euler-Lagrange equations (2.1) (noting <ell, e> = 0 and Delta_c^2 a = 0) yields
the exact discrete Noether energy-work identity for all n>=1:

    H_phys,n+1 - H_phys,n
      = (chi_n / m^n) * <ell, (h_(n+1) - h_(n-1)) / 2>
      + (<ell, h_n> / m^n) * ((chi_(n+1) - chi_(n-1)) / 2).                 (4.9)

When the coupling is disabled, the right-hand side of (4.9) vanishes and
H_phys,n is strictly conserved at every counter.

### 4.3 Exact conservation of the positive-signature canonical symplectic form

Let z^(1)=(h^(1),chi^(1)) and z^(2)=(h^(2),chi^(2)) be any two solutions of the
homogeneous coupled equations (2.1) with a=0. On bond (n-1,n) (n>=1), define

    Omega_h,n   = <h_(n-1)^(1), h_n^(2)> - <h_n^(1), h_(n-1)^(2)>,
    Omega_chi,n = chi_(n-1)^(1) * chi_n^(2) - chi_n^(1) * chi_(n-1)^(2),
    Omega_n^+   = Omega_h,n + Omega_chi,n.                                  (4.10)

Using h_(n+1) + h_(n-1) = (2*I - L)*h_n + (chi_n / m^n)*ell and
chi_(n+1) + chi_(n-1) = chi_n + <ell, h_n> / m^n, the one-step increments are

    Omega_h,n+1 - Omega_h,n
      = <h_n^(1), h_(n+1)^(2) + h_(n-1)^(2)> - <h_(n+1)^(1) + h_(n-1)^(1), h_n^(2)>
      = (1 / m^n) * (chi_n^(2) * <ell, h_n^(1)> - chi_n^(1) * <ell, h_n^(2)>),  (4.11)

and

    Omega_chi,n+1 - Omega_chi,n
      = chi_n^(1) * (chi_(n+1)^(2) + chi_(n-1)^(2)) - (chi_(n+1)^(1) + chi_(n-1)^(1)) * chi_n^(2)
      = (1 / m^n) * (chi_n^(1) * <ell, h_n^(2)> - chi_n^(2) * <ell, h_n^(1)>).  (4.12)

Adding (4.11) and (4.12) cancels the reciprocal coupling terms identically at
every counter n>=1:

    Omega_(n+1)^+ - Omega_n^+ = 0,  hence  Omega_n^+ = Omega_1^+  for all n>=1. (4.13)

Notice that this cancellation relies directly on the **positive** relative
kinetic sign: for the indefinite Wronskian Omega_n^- = Omega_h,n - Omega_chi,n,
the increments (4.11) and (4.12) add rather than cancel.

## 5. Spatial spectrum and retarded Green bounds

As proved from C = 460*I + 29*(S+S^(-1)) + 65*(S^2+S^(-2)), the nonzero
eigenvalues of L = (648*I - C)/324 on e^perp are

    lambda_+ = (235 + 18*sqrt(5)) / 324,
    lambda_- = (235 - 18*sqrt(5)) / 324,

each of multiplicity two, satisfying 1/2 < lambda_- < lambda_+ < 1. The
retarded Green operator G_h(t) of Delta_c^2 + L on e^perp satisfies
||G_h(t) * ell||_2 < sqrt(16/3) < 5/2 for all t>=1. The retarded Green kernel
G_chi(t) of Delta_c^2 + 1 is the periodic sequence (0,1,1,0,-1,-1,...)_t, which
satisfies |G_chi(t)| <= 1 for all t>=0.

## 6. Simultaneous causal bounds and the Lorentz domain

Let h^free be the canonical unforced K1 history for the same word and let
chi_0^0 = 0, chi_n^0 = a*(1,2,2,1,0,0)_n for n>=1. The differences
delta h_n = h_n - h_n^free and delta chi_n = chi_n - chi_n^0 vanish at n=0,1
and obey the exact retarded representations

    delta h_n   = sum_(t=1)^(n-1) G_h(n-t) * ell * chi_t / m^t,
    delta chi_n = sum_(t=1)^(n-1) G_chi(n-t) * <ell, h_t> / m^t.            (6.1)

Because |G_chi(n-t)| <= 1, the induction step is identical in magnitude to that
of #1646: assuming -299/500 < h_t(r) < 499/500 for t<n gives |<ell, h_t>| < 798/500 < 2,
whence

    |delta chi_n| <= sum_(t=1)^(n-1) |<ell, h_t>| / m^t < 2 / (m - 1) = 2 / 323,
    |chi_n| < 2 + 2 / 323 = 648 / 323 < 3,

and using |chi_1| <= 1 and |chi_t| < 3 for t>=2 gives

    ||delta h_n||_infty <= ||delta h_n||_2
                        < (5/2) * (1/324 + 3/(324*323))
                        = 1630 / 209304 < 1 / 125.                          (6.2)

Combined with the canonical free bound -59/100 < h_n^free(r) < 99/100, this
establishes for all thirty ready histories and all n>=0:

    -299/500 < h_n(r) < 499/500,
    det g_n(r) = -(1 - h_n(r)^2) < -999/250000 < 0,                         (6.3)

so g_n(r) = diag(-1, 1+h_n(r), 1-h_n(r), 1) has Lorentz signature (-,+,+,+) at
every counter.

## 7. Exact witnesses, energy-work balance, symplectic exchange, and periods

### 7.1 Direct source contrast at word 0010

At word 0010, P_0=(0,1,1,0,0), P_1=(1,1,0,0,0), and <ell, P_1>=0. For a=-1 and
a=+1, at n=2:

    P_2(-) = (487,167,-230,130,94), Y_2(-) = -1296,
    P_2(+) = (491,163,-230,130,94), Y_2(+) = 1296,
    D_2 = 648, h_2(+) - h_2(-) = ell / 162.

### 7.2 Positive-kinetic zero-seed reciprocal witness at word 0011, a=0

At word 0011 and a=0, P_0=P_1=(0,1,1,0,0), Y_0=Y_1=0, and <ell, P_1>=-1. The
first positive-kinetic step (2.2) gives

    P_2 = (94,165,165,94,130), Y_2 = -1, D_2 = 648, chi_2 = -1 / 648.       (7.1)

At the second step, C*P_2 = (68630,97971,97971,68630,86702) and Y_2 = -1 give

    P_3 = m * C * P_2 - m^3 * P_1 - ell
        = (22236119, -2269619, -2269620, 22236120, 28091448),
    D_3 = 68024448,
    h_3 - h_3^free = -ell / 68024448.                                       (7.2)

Since <ell, P_2> = 94 - 165 = -71, the full positive-kinetic source update at
n=2 gives

    Y_3 = m^2 * Y_2 + <ell, P_2> = -104976 - 71 = -105047,

whereas the control retaining feedback only at n=1 has Y_3^first-only = -104976
(chi_3^first-only = -1/648). Hence the continued-feedback contrast is

    chi_3^pos - chi_3^first-only = -71 / 68024448.                          (7.3)

### 7.3 Exact physical Hamiltonian work and symplectic exchange witnesses

For word 0011, a=0, at bond n=1: h_0=h_1=P_1/2 and (648*I-C)*P_1 =
(-94,159,159,-94,-130), so <P_0, (648*I-C)*P_1> = 318 and

    H_phys,1 = H_h,1 = 318 / (8 * 324) = 53 / 432, H_chi,1 = 0.

At bond n=2, since chi_1=0, H_h,2 = H_h,1 = 53/432, while chi_2 = -1/648 gives
a strictly positive excited source energy

    H_chi,2 = (1/2) * (-1/648)^2 = 1 / 839808 > 0,
    H_phys,2 - H_phys,1 = +1 / 839808,                                      (7.4)

matching the Noether work right-hand side
(<ell, h_1>/324) * ((chi_2 - chi_0)/2) = (-1/648) * (-1/1296) = +1/839808.

For the pair z^(1) = (0010, a=0) and z^(2) = (0011, a=0), at bonds n=1 and n=2:
Omega_h,1 = Omega_h,2 = 1/4 and Omega_chi,1 = Omega_chi,2 = 0. Between bond n=2
and bond n=3, chi_2^(1)=0, chi_2^(2)=-1/648, and <ell, h_2^(1)> = 324/648 = 1/2,
so by (4.11)-(4.12):

    Omega_h,3 - Omega_h,2     = (-1/648) * (1/2) / 324^2 = -1 / 136048896,
    Omega_chi,3 - Omega_chi,2 = +1 / 136048896,
    Omega_3^+ = Omega_2^+ = Omega_1^+ = 1 / 4.                              (7.5)

### 7.4 Sharp first budget and the nine least funded periods

For word 0011, a=0: E(x_1)=10, ||P_2||^2=89022, Y_2^2=(-1)^2=1, and
N(H_(-1)) = 294*(-1)^4 + 52*(-1)^2 + 4 = 350, so E(x_2)=89378 and the sharp
first-step bank is 89368 (while 89367 reflects).

For all ready n=1,2,3, |P_r| < D_n and |Y_n| < 3*D_n imply E(x_n) < 24000*D_n^4.
For word 0010 with a in {-1,+1}, |chi_(n+1)| > 1/2 for n=1,2,3 implies
E(x_(n+1)) > (294/16)*m^(4*n)*D_n^4 > 24000*D_n^4 > E(x_n). For word 0011, a=0,
|Y_3| = 105047 > 10^5 gives E(x_3) > E(x_2), and <ell, P_3> = 24505738 gives

    Y_4 = m^3 * Y_3 - m^5 * Y_2 + <ell, P_3>
        = -71 * m^3 + 24505738 = -2390362166,

so |Y_4| > 2*10^9 and E(x_4) > 294*(2*10^9)^4 > 24000*D_3^4 > E(x_3). Thus
E(x_1) < E(x_2) < E(x_3) < E(x_4) for all three seeds, and the nine least
funded periods for targets N=1,2,3 are 2,4,6,2,4,6,2,4,6.
