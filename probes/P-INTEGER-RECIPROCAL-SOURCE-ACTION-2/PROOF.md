# Analytical Proofs for P-INTEGER-RECIPROCAL-SOURCE-ACTION-2

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-RECIPROCAL-SOURCE-ACTION-2  
Ownership: https://github.com/mathorn1973/twist-j/issues/1642

This document gives complete analytical proofs for claims B1-B5 frozen in
PREREG.md. All results are stated and proved within the declared
NON-CANONICAL L1 scope over Public Canon v103.

## 1. Reciprocal carrier, exact partial inverse, and funded bijection: B1

### 1.1 Cyclotomic ring, Hermitian transport, and positive cost

In O=Z[j] with 1+j+j^2+j^3+j^4=0 and conjugation j^*=j^4, the real subring
is O^+=Z[phi] with phi=-j^2-j^3 and phi^2=phi+1. The units J=1+j^2 and phi
have exact inverses J^(-1)=-j-j^2 and phi^(-1)=phi-1, so A=diag(J,phi) and
B(q)=[[1,q],[0,1]] lie in GL_2(O) with det(A)=J*phi=j and det(B(q))=1.
Conjugate transposition X -> M X M^dagger preserves 2x2 Hermitian matrices
over O and multiplies the determinant by det(M)*det(M)^*=1.

In the eight-integer representation

    H8=(a0,a1,d0,d1,c0,c1,c2,c3),
    H=[[a0+a1*phi,c],[c^*,d0+d1*phi]],
    c=c0+c1*j+c2*j^2+c3*j^3,

the arithmetic cost is

    N(H)=Tr_K/Q(tr(H^2))
        =4*a0^2+4*a0*a1+6*a1^2
        +4*d0^2+4*d0*d1+6*d1^2
        +10*sum_{i=0}^3 c_i^2 - 2*(sum_{i=0}^3 c_i)^2.

Because 4*u^2+4*u*v+6*v^2 = (2*u+v)^2 + 5*v^2 >= 2*(u^2+v^2) and, by
Cauchy-Schwarz, 10*sum c_i^2 - 2*(sum c_i)^2 >= 2*sum c_i^2, every
Hermitian register satisfies

    N(H) >= 2*||H8||_2^2,

with N(H)=0 if and only if H8=0.

### 1.2 Exact partial inverse of the reciprocal seven-phase gate

The core carrier X consists of 38-integer tuples
x=(s,q,H,R,Z,P,Q,k,p) with k>=1 and p in {0,...,6}.
Phases p=0,...,5 act only on source and detector registers:
- p=0 sends (s,q) -> (s-q,s), with unique inverse (s',q') -> (q',q'-s')
  at output phase p'=1;
- p=1,2,3,4 apply B(-q), A^(-1), B(q), A by congruence, with unique
  inverses B(q), A, B(-q), A^(-1) at output phases p'=2,3,4,5;
- p=5 sends Z -> Z+H-R, with unique inverse Z' -> Z'-H+R at p'=6.

At phase p=6, the reciprocal gate fixes q,H,R,Z and sends

    (s,P,Q,k,6) -> (s',P',Q',k',0),
    P'=C*P-a(k)*Q+2*lambda*chi(H,R)*ell,
    Q'=P,
    s'=s+lambda*Phi(P,Q),
    k'=k+1,

where a(1)=324, a(k)=104976 for k>=2, chi(H,R)=H8[5]-R8[5], and

    Phi(P,Q)=((P_0 mod 2)-(P_1 mod 2))-((Q_0 mod 2)-(Q_1 mod 2)).

Suppose a core (s',q,H,R,Z,P',Q',k',0) lies in the image of phase 6.
Then k'=k+1>=2, P=Q', and

    C*Q'-P'+2*lambda*chi(H,R)*ell = a(k'-1)*Q.

Hence all five entries of C*Q'-P'+2*lambda*chi(H,R)*ell are divisible by
a(k'-1), which uniquely determines both field registers of the predecessor:

    P_prev = Q',
    Q_prev = (C*Q'-P'+2*lambda*chi(H,R)*ell)/a(k'-1).

Once P_prev and Q_prev are recovered, the functional Phi(P_prev,Q_prev) is
uniquely determined by (P_prev,Q_prev), so the predecessor source register
is uniquely recovered by

    s_prev = s' - lambda*Phi(P_prev,Q_prev).

Conversely, any core at phase p'=0 with k'>=2 satisfying the five-entry
congruence modulo a(k'-1) has this exact predecessor in X at phase 6, and
applying T to that predecessor reproduces (s',q,H,R,Z,P',Q',k',0).
Since the output phase p'=(p+1) mod 7 identifies the preceding phase p,
images from distinct phases are disjoint. Therefore T is injective on X
with the stated exact backward domain.

In particular, adding 1 to entry P'[2] of any phase-6 image changes the
backward residual C*Q'-P'+2*lambda*chi*ell in entry 2 by -1. Since
a(k'-1)>=324>1, the corrupted state cannot be divisible by a(k'-1) and has
no backward image. Likewise, any state with k'=1,p'=0 has no backward image.

### 1.3 Funded reflection bijection, finite shells, and least periods

For a funded state S=(x,b,epsilon) with b>=0 and epsilon in {-1,+1}, the
funded step F attempts y=T^epsilon(x) and proposed bank c=b+E(x)-E(y).
If y is defined and c>=0, F(S)=(y,c,epsilon); otherwise
F(S)=Rev(S)=(x,b,-epsilon).

Both branches preserve M=E(x)+b and b>=0. If S=(x,b,epsilon) is accepted
to (y,c,epsilon), then Rev(F(S))=(y,c,-epsilon) has reverse target
T^(-epsilon)(y)=x and proposed reverse bank c+E(y)-E(x)=b>=0, so
F(Rev(F(S)))=(x,b,-epsilon)=Rev(S), giving (Rev F Rev)(F(S))=S.
If S is rejected, F(S)=Rev(S), so Rev(F(S))=S, which is again rejected by F
to Rev(S), giving (Rev F Rev)(F(S))=Rev(Rev(S))=S. Thus

    F^(-1) = Rev F Rev

on the entire funded carrier.

Because s^2-s*q+q^2 = (s-q/2)^2 + (3/4)*q^2 >= (s^2+q^2)/2 and
N(H)>=2*||H8||_2^2, the core account

    E(x)=1+s^2-s*q+q^2+N(H)+N(R)+N(Z)+k+||P||_2^2+||Q||_2^2

is positive and proper on X. Every shell E(x)+b=M contains only finitely
many funded states. On a fixed shell M, the bare height t(x)=7*(k-1)+p
increases by 1 under every forward step T, and an edge between x and T(x)
is admitted in either direction if and only if max(E(x),E(T(x)))<=M.
Thus each connected component of admitted edges is a finite simple path
of L>=1 vertices ordered by height, traversed forward and backward with
reflections at both ends, yielding a purely periodic orbit of least
funded period 2L. For a ready core x_0 at k=1,p=0 (where T^(-1)(x_0) is
absent), the admitted forward path at initial bank B reaches the largest
bare height t such that

    B_sharp(t) = max_{0<=j<=t} E(T^j(x_0)) - E(x_0) <= B,

and has least funded period 2*(t+1). This proves B1.

## 2. Structural classification of the coupling and primitive denominators: B2

### 2.1 Unique unit-slope odd linear source functional chi

Starting from H=R=D=diag(0,1) at phase 1 with shear q=sigma in Z, one
complete four-gate Hermitian transport (phases 1,2,3,4) applies the loop
matrix

    C_sigma = A * B(sigma) * A^(-1) * B(-sigma) = [[1, sigma*v],[0, 1]],
    v = J*phi^(-1) - 1 = -2 + j - j^2,

with v*v^* = 9 - 5*phi. Conjugating D=[[0,0],[0,1]] by C_sigma gives

    H(sigma) = C_sigma * D * C_sigma^dagger
             = [[sigma^2*(9-5*phi), sigma*v],
                [sigma*v^*, 1]].

Subtracting R=D yields

    (H(sigma)-R)_8 = (9*sigma^2, -5*sigma^2, 0, 0, -2*sigma, sigma, -sigma, 0).

Among the eight integer coordinates of H(sigma)-R:
- coordinates 0 and 1 are purely quadratic in sigma (9*sigma^2 and
  -5*sigma^2), which are even in sigma and cannot distinguish the sign of
  the source;
- coordinates 2, 3, and 7 vanish identically;
- coordinates 4, 5, and 6 are linear in sigma with coefficients -2, +1,
  and -1.

Therefore coordinate 5, namely chi(H,R)=coeff_j((H-R)_01)=H8[5]-R8[5], is
the unique coordinate of H(sigma)-R that equals +sigma for every integer
shear sigma (the unique unit-slope odd linear coordinate functional).
Moreover, when sigma_1,...,sigma_m are applied in successive source blocks
starting from D, the upper-triangular matrices C_(sigma_t) commute:

    C_(sigma_m)...C_(sigma_1) = [[1, (sum_{t=1}^m sigma_t)*v],[0, 1]],

so at the end of block m,

    chi_m = sum_{t=1}^m q_t,

where q_t is the shear register during block t.

### 2.2 Minimal zero-sum dipole ell and modulo-3 site protection

Let P_(n+1) = C*P_n - a(n)*P_(n-1) + kappa*chi_n*u with u in Z^5.
Since the canonical metric slices satisfy sum_r h_n(r)=1, i.e.
sum_r P_n(r)=D_n=2*m^(n-1), and since e^T*C = 648*e^T = 2*m*e^T, the sum
of coordinates satisfies

    sum_r P_(n+1)(r) = 2*m*D_n - a(n)*D_(n-1) + kappa*chi_n*sum_r u_r
                     = D_(n+1) + kappa*chi_n*sum_r u_r.

Hence preserving the canonical mean sum_r h_n(r)=1 for non-zero source
histories requires sum_r u_r = 0.

Any non-zero integer vector u in Z^5 with sum_r u_r = 0 has at least one
positive and at least one negative integer entry, so

    ||u||_2^2 = sum_{r=0}^4 u_r^2 >= 1^2 + (-1)^2 = 2,

with equality if and only if u = e_r - e_s for distinct sites r!=s.
There are exactly 5*4 = 20 such minimal-norm integer dipoles in Z^5,
forming a single orbit under the symmetric group S_5 (and two orbits of 10
under the dihedral group D_5 of the 5-cycle: nearest-neighbor and
second-neighbor pairs). Selecting the canonical marked adjacent pair {0,1}
and positive orientation at site 0 uniquely specifies

    ell = e_0 - e_1 = (1,-1,0,0,0).

This minimal two-site support also protects the 3-adic valuation of the
primitive numerator: the complement {0,1,2,3,4}\{0,1} = {2,3,4} has 3
sites, while for every canonical word the initial numerator P_1 has only
two ones. By the pigeonhole principle, there is at least one site
r_* in {2,3,4} where P_1(r_*)=0 and ell(r_*)=0, ensuring that the source
forcing never touches site r_*.

### 2.3 Parity factor kappa=2 and all-counter primitive denominators

Consider the general integer forcing

    P_2 = C*P_1 - m*P_0 + kappa*chi_1*ell,
    P_(n+1) = C*P_n - m^2*P_(n-1) + kappa*chi_n*ell   (n>=2),

with candidate denominator D_n = 2*m^(n-1) = 2^(2n-1)*3^(4n-4).
Modulo 2, C = J_5 + I, m = 0, and sum_r P_1(r) = 2 = 0, so C*P_1 = P_1 mod 2.
Thus at n=1,

    P_2 = P_1 + kappa*chi_1*ell   (mod 2).

If kappa is odd (for example kappa=1) and chi_1 is odd (such as a=+-1),
then whenever a canonical word has P_1=(1,1,0,0,0) (which holds for the
four words 0010, 0101, 1010, and 1101), we have P_1 = ell mod 2 and hence

    P_2 = P_1 + ell = (0,0,0,0,0)   (mod 2).

Every entry of P_2 is then even, so gcd(P_2(0),...,P_2(4),D_2) >= 2 and the
common denominator D_2=648 fails to be minimal (collapsing to 324).

Conversely, when kappa=2 (the minimal positive even integer), the forcing
term 2*lambda*chi_n*ell is always 0 mod 2. By induction on n>=1, since
sum_r P_n(r) = D_n = 0 mod 2 and m = 0 mod 2,

    P_n = P_1   (mod 2)   for all n>=1.

Since P_1 has two 1s and three 0s, gcd(P_n(0),...,P_n(4),2) = 1 for every
n>=1.

Modulo 3, C = -I - J_5 and m = 0. At the site r_* in {2,3,4} where
P_1(r_*)=0 and ell(r_*)=0, we have sum_r P_1(r)=2 and

    P_2(r_*) = -P_1(r_*) - sum_r P_1(r) + 2*lambda*chi_1*ell(r_*)
             = -0 - 2 + 0 = 1   (mod 3).

For every n>=2, sum_r P_n(r) = D_n = 0 mod 3 and ell(r_*)=0, so

    P_(n+1)(r_*) = -P_n(r_*)   (mod 3),

which implies P_n(r_*) = (-1)^(n-2) != 0 (mod 3) for all n>=2 (and P_1 has
two entries equal to 1 != 0 mod 3). Since D_n has only prime factors 2 and
3, no prime divides both D_n and all five entries of P_n. Therefore, for
every canonical word and every integer sequence chi_n,

    gcd(P_n(0),P_n(1),P_n(2),P_n(3),P_n(4),D_n) = 1,
    gcd(P_n(0),P_n(1),P_n(2),P_n(3),P_n(4)) = 1,

and d_n = D_n = 2*m^(n-1) is the exact least common denominator of h_n at
every counter n>=1.

### 2.4 Attenuation 324^n and representation cost bounds

Dividing the integer gate P_(n+1) = C*P_n - a(n)*P_(n-1) + 2*lambda*chi_n*ell
by D_(n+1) = 2*m^n and substituting h_n = P_n/D_n and C/m = 2*I - L gives

    h_(n+1) - 2*h_n + h_(n-1) + L*h_n = (2*lambda*chi_n*ell)/(2*m^n)
                                      = (lambda*chi_n/m^n)*ell = J_n.

Thus the m^(-n) = 324^(-n) attenuation in J_n is not a separately tuned
decay parameter: it is the exact ratio between the unit-scale integer
source coupling 2*lambda*chi_n*ell and the canonical reader denominator
D_(n+1)=2*m^n. The explicit pair-encoding bound
sum_r Ptilde_r^2 + Dtilde^2 >= (6/5)*d_n^2 and the actual-account bound
E(x) >= ||P_n||_2^2 >= d_n^2/5 = (4/5)*m^(2n-2) follow immediately by
Cauchy-Schwarz as in #1641. This completes B2.

## 3. Reciprocal source oscillator, no-go theorem, and uniform Lorentz domain: B3

### 3.1 Scale-invariant modulo-2 backreaction and the source oscillator law

On any ready history for word w and initial source seed a in {-1,0,1}:
- At the start of block 1 (k=1, p=0), P=P_1, Q=P_0, s_0=a, q_0=0.
- Phase 0 updates (s,q) to (a,a), so during block 1 the shear is q_1=a and
  at phase 6 we read chi_1 = q_1 = a.
- At phase 6 of block 1 (k=1 -> 2), the field registers update to
  (P_2,P_1) and the source register updates to

      s_1 = a + lambda*Phi(P_1,P_0).

  Because P_0 and P_1 are {0,1}-valued vectors with P_0=2*h_0 and
  P_1=2*h_1, and K_{11,0}-K_{22,0} = (h_1-h_0)/2 - (- (h_1-h_0)/2) = h_1-h_0,
  we have

      beta(w) := Phi(P_1,P_0) = <ell, P_1 - P_0> = 2*<ell, h_1 - h_0>
               = 2*<ell, K_{11,0} - K_{22,0}> in {-2,-1,0,1,2}.

- At every subsequent field gate k=n -> n+1 with n>=2, the input field
  registers are P=P_n and Q=P_(n-1). By Theorem 2.3,

      P_n = P_1 (mod 2)   and   P_(n-1) = P_1 (mod 2)   for all n>=2.

  Therefore (P_n(r) mod 2) = (P_(n-1)(r) mod 2) for every site r, and

      Phi(P_n,P_(n-1)) = 0   for all n>=2.

Let (s_n,q_n) denote the source registers at phase 6 of block n (for n>=1,
after the phase-0 kick of block n and before the phase-6 update). With
(s_0,q_0)=(a,0) at k=1,p=0:
- At phase 0 of block n, (s,q) becomes (s_(n-1)' - q_(n-1), s_(n-1)'), so
  q_n = s_(n-1)' and s_n = q_n - q_(n-1).
- At phase 6 of block n, s_n' = s_n + lambda*delta_(n,1)*beta(w), so for
  every n>=1:

      q_(n+1) = s_n' = q_n - q_(n-1) + lambda*delta_(n,1)*beta(w).

Since chi_n = sum_{t=1}^n q_t (with chi_0 := 0), taking first differences
q_n = chi_n - chi_(n-1) and summing from t=1 to n yields for every n>=1:

    chi_(n+1) - chi_n = sum_{t=1}^n q_(t+1)
                      = sum_{t=1}^n (q_t - q_(t-1)) + lambda*beta(w)
                      = q_n - q_0 + lambda*beta(w)
                      = chi_n - chi_(n-1) + a + lambda*beta(w),

since q_1 = s_0 - q_0 + q_0 = a. Rearranging gives the exact second-order
discrete Klein-Gordon oscillator equation for all n>=1:

    (Delta_c^2 + 1)chi_n = chi_(n+1) - chi_n + chi_(n-1)
                         = a + lambda*beta(w)
                         = a + 2*lambda*<ell, K_{11,0} - K_{22,0}>,

with initial values chi_0 = 0 and chi_1 = a.

The homogeneous equation xi_(n+1)-xi_n+xi_(n-1)=0 has characteristic roots
e^(+-i*pi/3) of period 6. By linearity, the unique solution with chi_0=0,
chi_1=a, and constant right-hand side a+lambda*beta(w) for n>=1 is the
six-periodic sequence

    chi_n(w,a) = a*p^(0)_n + lambda*beta(w)*p^(1)_n,

where for n=1,2,3,4,5,6 (mod 6):

    p^(0) = (1, 2, 2, 1, 0, 0),
    p^(1) = (0, 1, 2, 2, 1, 0).

In particular, for a in {-1,0,1}, beta(w) in {-2,-1,0,1,2}, and lambda=1:
- at n=1: |chi_1| = |a| <= 1;
- at all n>=2: |chi_n| <= 2*|a| + 2*|beta(w)| <= 2 + 4 = 6.

### 3.2 Secular-resonance no-go theorem for unattenuated numerator feedback

To see why the modulo-2 scale filter Phi(P,Q) is mathematically required,
consider what happens if one replaces Phi(P,Q) by the unattenuated integer
numerator coupling <ell, P_n>, i.e.

    chi_(n+1) - chi_n + chi_(n-1) = a + lambda*<ell, P_n>.

Because P_n = 2*m^(n-1)*h_n grows exponentially like m^(n-1) = 324^(n-1)
while the homogeneous source operator Delta_c^2+1 has unit-modulus
eigenvalues, the forced source holonomy grows as

    chi_n = (2*lambda/(m + m^(-1) - 1))*m^(n-2)*<ell, h_(n-1)> + O(m^(n-3)).

Substituting this growing chi_n into the field source
J_n = (lambda*chi_n/m^n)*ell gives

    J_n = (2*lambda^2/(m^2*(m + m^(-1) - 1)))*<ell, h_(n-1)>*ell + O(m^(-3)),

whose m^n factors cancel! Instead of an exponentially damped forcing, the
field equation acquires a permanent O(m^(-2)) non-normal delay feedback
that shifts the normal-mode frequencies by delta_omega = O(m^(-2)) and
produces secular amplitude drift delta_h_n ~ n*m^(-2), violating the
1/125 response bound (while the Green-function series sum_{t=1}^{n-1}
(5/2)*|chi_t|*m^(-t) exceeds 1/125 already by n=9). Furthermore, the
Hermitian source cost N(H_n) = 294*chi_n^4 grows like 294*m^(4n-8),
dominating the field cost ||P_n||_2^2 ~ m^(2n-2).

By contrast, modulo-2 reduction maps Z[1/m] consistently by annihilating
all multiples of m=324, extracting the exact m^0 initial-slice shear
beta(w) and keeping chi_n bounded and 6-periodic for all counters n>=1.

### 3.3 All-counter Green-function response bound and Lorentz signature

Let delta_h_n = h_n - h_n^free be the difference between the reciprocally
forced history and the canonical free K1 history for the same word w.
Since h_0 = h_0^free and h_1 = h_1^free, delta_h_n solves

    (Delta_c^2 + L)delta_h_n = J_n = (lambda*chi_n/m^n)*ell   (n>=1),
    delta_h_0 = delta_h_1 = 0.

Because sum_r ell_r = 0 and L commutes with the cyclic shift S, delta_h_n
lies in the four-dimensional zero-sum subspace 1^perp for all n>=0.
On 1^perp, the eigenvalues of L = [188*I - 29*(S+S^(-1)) - 65*(S^2+S^(-2))]/324
are

    mu_1 = (235 + 36*sqrt(5))/324,
    mu_2 = (235 - 36*sqrt(5))/324,

each of multiplicity two. Write mu_j = 2 - 2*cos(theta_j) = 4*sin^2(theta_j/2).
Then

    sin^2(theta_j) = mu_j*(4 - mu_j)/4 >= mu_2*(4 - mu_2)/4.

Since 36*sqrt(5) = sqrt(6480) satisfies 80 < 36*sqrt(5) < 81, we have
mu_2 > (235 - 81)/324 = 77/162 and 4 - mu_2 > 4 - 155/324 = 1141/324 > 7/2,
so

    sin^2(theta_j) > (77/162)*(7/8) = 539/1296 > 8/25

(since 25*539 = 13475 > 10368 = 8*1296), whence sin(theta_j) > 2*sqrt(2)/5
for both j=1,2.

By Duhamel's formula on 1^perp,

    delta_h_n = sum_{t=1}^{n-1} G_(n-t) J_t,

where on each eigenspace G_s = sin(s*theta_j)/sin(theta_j) has spectral
norm ||G_s||_(2->2) <= 1/sin(theta_2) < 5/(2*sqrt(2)). Since ||ell||_2 = sqrt(2),
every step s>=1 satisfies

    ||G_s ell||_infty <= ||G_s ell||_2 <= ||G_s||_(2->2)*||ell||_2
                      < (5/(2*sqrt(2)))*sqrt(2) = 5/2.

Using |chi_1| <= 1 and |chi_t| <= 6 for all t>=2, we obtain for every n>=0:

    ||delta_h_n||_infty <= sum_{t=1}^{n-1} (5/2)*|chi_t|*m^(-t)
                        < (5/2)*(1/m + 6*sum_{t=2}^infty m^(-t))
                        = (5/2)*(1/m + 6/(m*(m-1)))
                        = (5*(m+5))/(2*m*(m-1))
                        = (5*329)/(2*324*323)
                        = 1645/209304 < 1/125,

since 1645 * 125 = 205625 < 209304.

Combining ||h_n - h_n^free||_infty < 1/125 with the canonical all-counter
free-K1 bound -59/100 < h_n^free(r) < 99/100 gives, for all 30 ready
histories, all counters n>=0, and all sites r in {0,1,2,3,4}:

    h_n(r) > -59/100 - 1/125 = -299/500,
    h_n(r) <  99/100 + 1/125 =  499/500,
    1 + h_n(r) > 201/500 > 0,
    1 - h_n(r) >   1/500 > 0,
    det g_n(r) = -(1 - h_n(r)^2) < -(1 - (499/500)^2) = -999/250000 < 0.

Thus g_n(r) = diag(-1,1+h_n(r),1-h_n(r),1) has strict Lorentzian signature
(-,+,+,+) at every counter n>=0 on all 30 ready histories and their
retraced prefixes. This proves B3.

## 4. Fixed-counter witnesses, zero-seed backreaction, and periods: B4

### 4.1 First-block energy prefixes and common-bank contrast at word 0010

For word 0010, u_0=1, u_1=0, P_0=(0,1,1,0,0), P_1=(1,1,0,0,0), and
beta(0010) = Phi(P_1,P_0) = (1-1) - (0-1) = +1.
At height 0 (k=1,p=0), N(D)=6, N(Z_0)=16, ||P_1||_2^2=||P_0||_2^2=2, and
s^2-s*q+q^2 = a^2, so E_0 = 1 + a^2 + 6 + 6 + 16 + 1 + 2 + 2 = 30 + a^2.

During block 1 (heights 0,...,6), the shear is q_1=a:
- For a=0, H remains D with N(H)=6 at heights 0,...,5, and Z remains Z_0
  at height 6, so the energies at heights 0,...,6 are
  30, 30, 30, 40, 40, 30, 30 (since A^(-1) D (A^(-1))^dagger has
  diagonal 2-phi with cost 16=6+10 at heights 3,4).
  At height 6 -> 7, chi_1=0, P_2(0) = C*P_1 - 324*P_0 = (489,165,-230,130,94)
  with ||P_2(0)||_2^2 = 344978, and the reciprocal gate updates s from 0 to
  s_1' = 0 + 1 = +1 (with q=0), increasing s^2-s*q+q^2 from 0 to 1 and k
  from 1 to 2. Thus E_7(0) = 30 - 2 + 344978 + 1 + 1 = 345012, giving
  PREFIX_ZERO = (30,30,30,40,40,30,30,345012) and sharp bank 344982.
- For a=-1 and a=+1, heights 0,...,6 have the identical source costs
  31, 31, 43, 63, 147, 377, and after detector write at height 6:
  E_6(-1)=747 and E_6(+1)=803.
  At height 6 -> 7:
  - For a=-1: chi_1=-1, P_2(-1) = (487,167,-230,130,94) with
    ||P_2(-1)||_2^2 = 343692, and s updates from -1 to s_1' = -1 + 1 = 0
    (while q=-1), keeping s^2-s*q+q^2 = 0 - 0 + 1 = 1 unchanged!
    Thus E_7(-1) = 747 - 2 + 343692 + 1 = 344440, giving
    PREFIX_NEG = (31,31,43,63,147,377,747,344440) and sharp bank
    344440 - 31 = 344409.
  - For a=+1: chi_1=+1, P_2(+1) = (491,163,-230,130,94) with
    ||P_2(+1)||_2^2 = 346284, and s updates from +1 to s_1' = +1 + 1 = +2
    (while q=+1), increasing s^2-s*q+q^2 from 1 to 4 - 2 + 1 = 3 (an
    increase of +2). Thus E_7(+1) = 803 - 2 + 346284 + 1 + 2 = 347090,
    giving PREFIX_POS = (31,31,43,63,147,377,803,347090) and sharp bank
    347090 - 31 = 347059.

At the common bank 347059, both a=-1 and a=+1 reach k=2,p=0 with residual
banks 347059 - 344409 = 2650 and 0, and exact metric difference

    h_2(+1) - h_2(-1) = (P_2(+1) - P_2(-1))/648 = (4,-4,0,0,0)/648
                      = (1,-1,0,0,0)/162.

### 4.2 Second-block backreaction and zero-seed contrast at k=3

At height 7 (k=2,p=0) on word 0010, the source registers are (s,q)=(a+1,a).
Phase 0 of block 2 sends (s,q) to (1, a+1), so the second-block shear is
q_2 = a+1, and after phases 1,2,3,4 of block 2 the source reading is

    chi_2(a) = q_1 + q_2 = 2*a + 1,

giving chi_2(-1)=-1, chi_2(0)=+1, and chi_2(+1)=+3 (compared to -2, 0, +2
in the one-way prescribed-source model). Applying phase 6 at height 13
produces the k=3 numerators:

    P_3(-1) = (120111, -6141, -59422, 98366, 57038),
    P_3(0)  = (120977, -7007, -59350, 98366, 56966),
    P_3(+1) = (121843, -7873, -59278, 98366, 56894),

whereas the unforced free numerator (lambda=0, a=0) is

    P_3^free = (120975, -7005, -59350, 98366, 56966).

Therefore, for the zero-seed history a=0, the gravitational backreaction
from the initial slice shear beta(0010)=+1 excites chi_2(0)=+1 and shifts
the k=3 metric reading by

    h_3(0) - h_3^free = (P_3(0) - P_3^free)/(2*324^2)
                      = (2,-2,0,0,0)/209952
                      = (1,-1,0,0,0)/104976.

Moreover, for every a in {-1,0,+1}, comparing the reciprocal numerator
P_3(a) against the one-way prescribed-source numerator P_3^one-way(a) gives
the exact backreaction shift

    P_3(a) - P_3^one-way(a) = 2*lambda*beta(0010)*ell = (2,-2,0,0,0).

### 4.3 Second-block energy profile and exact least funded periods

In block 2 (heights 7,...,14) on word 0010:
- For a=-1: at height 7, (s,q)=(0,-1) with E_7(-1)=344440. Phase 0 sends
  (s,q) to (1,0), so the second-block shear is q_2 = 0!
  Because q_2 = 0, phases 1 and 3 (B(0)=I) are the identity, while phase 2
  (A^(-1)) and phase 4 (A) conjugate H_1 and then undo the conjugation!
  Specifically, H_1 has N(H_1)=350, A^(-1) H_1 (A^(-1))^dagger has
  N=120=350-230, and A restores H_1 with N=350. Thus the energies at
  heights 7,8,9,10,11,12 are

      344440, 344440, 344440, 344210, 344210, 344440,

  none of which exceeds 344440! At height 12 -> 13 (phase 5, detector
  write), Z updates from Z_1 to Z_2 = Z_1 + H_1 - R, increasing N(Z) by
  1062 to E_13(-1) = 345502 (relative barrier 345502 - 344440 = 1062 above
  height 7), and at height 14, E_14(-1) = 30924887187.
  Consequently:
  - At bank 344409 (residual bank 0 at height 7): the orbit traverses
    heights 7,8,9,10,11,12 with zero additional peak cost and reflects at
    the height 12 -> 13 detector barrier (cost +1062). The admitted path has
    L = 13 vertices (heights 0,...,12) and exact least period 2*13 = 26!
  - At bank 347059 (residual bank 2650 at height 7): since 2650 >= 1062, the
    orbit also passes height 13 (residual bank 2650 - 1062 = 1588) and
    reflects at the height 13 -> 14 second field gate. The admitted path
    has L = 14 vertices (heights 0,...,13) and exact least period 2*14 = 28!
- For a=+1: at height 7, (s,q)=(2,1) with E_7(+1)=347090. Phase 0 sends
  (s,q) to (1,2) (keeping s^2-s*q+q^2 = 3), and phase 1 applies B(-2) to
  H_1, raising E_9(+1) to 348666 (relative barrier +1576). Thus at its
  sharp bank 347059 (residual bank 0 at height 7), the orbit reaches height
  8 for free and reflects before height 9, giving L = 9 vertices (heights
  0,...,8) and exact least period 2*9 = 18.
- All banks below the respective first-block sharp threshold (bank 772 and
  sharp-1 for a=-1,+1, plus bank 344409 for a=+1) reach height 6 (L=7
  vertices) and have exact least period 2*7 = 14.

Thus the eight benchmark orbits on word 0010 have exact least periods

    14, 26, 28, 14, 14, 14, 18, 14.

This completes B4.

## 5. Joint metric-and-source quadratic action: B5

### 5.1 Full joint action before plus-TT restriction

With the canonical spatial derivative operator D_sp (satisfying
D_sp^T = -D_sp and D_sp^T D_sp = -D_sp^2 = L), extrinsic curvature
perturbations K_ij, spatial quadratic form G_2(V), linearized scalar
curvature R_1(V), and canonical quadratic metric action A_2[V,ell_0,N],
define the joint quadratic action for compactly supported perturbations of
(V_ij, ell_0, N_i, chi_n) (with chi_0 = 0):

    A_joint[V,ell_0,N,chi]
      = A_2[V,ell_0,N]
      + (lambda/2)*sum_{n>=1} (chi_n/m^n)*<ell, V_{11,n} - V_{22,n}>
      - sum_{n>=0} (1/2)*(chi_(n+1) - chi_n)^2
      + sum_{n>=1} [(1/2)*chi_n^2 - (a + 2*lambda*<ell, K_{11,0} - K_{22,0}>)*chi_n].

Here K_{11,0} - K_{22,0} = (V_{11,1} - V_{11,0} - V_{22,1} + V_{22,0})/2 is
fixed by the prescribed initial slices at n=0,1.

### 5.2 Independent variation of all metric, lapse, and shift components

Varying all six symmetric spatial metric components V_ij, the lapse ell_0,
and the three shift components N_i independently at interior slices n>=1
while holding initial boundary data (n=0,1) fixed, and only afterwards
evaluating at the plus-TT representative

    V_n = diag(h_n, -h_n, 0),   ell_0 = 0,   N_i = 0,

gives the exact first variation

    delta_(V,ell_0,N) A_joint
      = -(1/2)*sum_{n>=1} <(Delta_c^2 + L)h_n - (lambda*chi_n/m^n)*ell,
                           delta V_{11,n} - delta V_{22,n}>.

All off-diagonal, longitudinal, trace, lapse, and shift equations vanish
identically at this representative, and vanishing of the transverse-traceless
variation yields the exact forced field equation

    (Delta_c^2 + L)h_n = (lambda*chi_n/m^n)*ell = J_n

at every interior counter n>=1.

### 5.3 Variation of the source coordinate and integer-lattice optimality

Varying the source variable chi_n at interior counter n>=1 while evaluating
V_n = diag(h_n,-h_n,0) (where (V_{11,n}-V_{22,n})/2 = h_n and
2*<ell,K_{11,0}-K_{22,0}> = beta(w)) gives the local slice action

    A_joint,local(v,xi)
      = (||v - h_(n-1)||_2^2 + ||h_(n+1) - v||_2^2)/2 - <v, L*v>/2
      + (lambda*xi/m^n)*<ell, v>
      - [((xi - chi_(n-1))^2 + (chi_(n+1) - xi)^2)/2
         - (1/2)*xi^2 + (a + lambda*beta(w))*xi].

For fixed v=h_n, A_joint,local(h_n,xi) is a concave quadratic polynomial in
xi with leading term -(1/2)*xi^2 (second derivative -1). Its exact first
derivative (and exact central unit difference) at xi = chi_n is

    [A_joint,local(h_n,chi_n+1) - A_joint,local(h_n,chi_n-1)]/2
      = -[(chi_(n+1) - chi_n + chi_(n-1)) - (a + lambda*beta(w))]
        + (lambda/m^n)*<ell, h_n>.

By Theorem 3.1, the O(1) oscillator residual
(chi_(n+1)-chi_n+chi_(n-1)) - (a+lambda*beta(w)) vanishes identically at
every n>=1! Thus the source variation equals the pure high-counter metric
tail

    tau_n := (lambda/m^n)*<ell, h_n> = (lambda*<ell, P_n>)/(2*m^(2n-1)).

Since -299/500 < h_n(r) < 499/500 at every site r on all 30 ready histories,
|<ell, h_n>| = |h_n(0) - h_n(1)| < 499/500 + 299/500 = 798/500 < 2, so for
all n>=1 and lambda=1:

    |tau_n| < 2/m^n <= 2/324 = 1/162 < 1/2.

Because A_joint,local(h_n,xi) is quadratic in xi with second derivative -1,
for any non-zero integer perturbation k in Z\{0},

    A_joint,local(h_n, chi_n) - A_joint,local(h_n, chi_n + k)
      = (1/2)*k^2 - k*tau_n
      >= |k|*(1/2 - |tau_n|) > |k|*(1/2 - 1/162) = (80/162)*|k| >= 40/81 > 0.

Therefore, at every counter n>=1, the reciprocal integer pair (h_n, chi_n)
is simultaneously an exact stationary point of the continuous metric
variation and the strict global maximizer of the discrete integer source
variation on Z, with the continuous source gradient vanishing exponentially
at rate O(324^(-n)).

### 5.4 Scope boundaries

These proofs establish B1-B5 within the declared NON-CANONICAL L1 scope:
- The structural justification of (chi, ell, 2, 324^n) classifies them
  within the declared two-by-two Hermitian loop and five-site primitive K1
  carrier; the choice of marked adjacent pair {0,1} and sign orientation
  remain explicit context conventions.
- The reciprocal phase-6 gate couples field slices back to the source via
  modulo-2 parity reduction, which acts at the m^0 scale while filtering
  out higher-power m^(n-1) terms as required by the secular-resonance no-go
  theorem.
- Full nonlinear Einstein geometry, native-U operator realization,
  continuum manifold limits, and physical energy/clock identifications
  remain separate future obligations.
