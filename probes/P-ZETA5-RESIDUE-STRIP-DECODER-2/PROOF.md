# Proof: residue, unit strip, scalar capacity and QDD Galois bridge

Status: theorem-grade derivation candidate for P-ZETA5-RESIDUE-STRIP-DECODER-2.
Scope: L1 arithmetic only.

This proof imports only named public TWIST-J rows and standard external number
theory theorems explicitly marked below. It does not import predecessor
verifier output as proof.

## 1. Dedekind residue

External standard theorem, analytic class number formula:

    Res_(s=1) zeta_F(s)
      = 2^r1 (2 pi)^r2 h_F R_F / (w_F sqrt(|d_F|)).

For K=Q(zeta_5), public exact inputs are

    r1=0, r2=2, h_K=1, w_K=10, |d_K|=125, R_K=2 log(phi).

Therefore

    Res zeta_K
      = (2 pi)^2 * 2 log(phi) / (10 sqrt(125))
      = 4 pi^2 log(phi)/(25 sqrt(5)).

For k=Q(sqrt(5)),

    r1=2, r2=0, h_k=1, w_k=2, d_k=5, R_k=log(phi),

hence

    Res zeta_k
      = 4 log(phi)/(2 sqrt(5))
      = 2 log(phi)/sqrt(5).

Thus

    Res zeta_K / Res zeta_k = 2 pi^2/25.

Before cancellation the ratio is

    (R_K/R_k) * ((2 pi)^2/2^2)
    --------------------------------
    sqrt(d_K/d_k) * (w_K/w_k)

      = 2 * pi^2 / (5*5)
      = 2 pi^2/25.

The first denominator five is sqrt(125/5), the second is 10/2.

For the primitive quartic Dirichlet character modulo five with kappa(2)=i,

    kappa(1)=1, kappa(2)=i, kappa(3)=-i, kappa(4)=-1.

Therefore

    S = sum_(a=1)^4 conjugate(kappa(a)) a
      = 1 - 2i + 3i - 4
      = -3+i,

and |S|^2=10. The standard primitive odd-character formula expresses
L(1,kappa) through the Gauss sum tau(kappa), S and the conductor 5.
Using |tau(kappa)|^2=5 gives

    |L(1,kappa)|^2
      = pi^2 * 5 * 10 / 5^4
      = 2 pi^2/25.

Equivalently the abelian factorization is

    zeta_K(s) = zeta_k(s) L(s,kappa) L(s,bar(kappa)),

because the quadratic character kappa^2 is already the nontrivial real
quadratic factor inside zeta_k.

The Gaussian integer factorization -3+i=(1+i)(-1+2i), with norms 2 and 5, is
an exact witness only. No theorem here identifies that factorization as a
structural derivation of w_K=10.

## 2. The oriented J-strip

Let alpha be nonzero and put

    A = |sigma_1(alpha)|^2,
    B = |sigma_2(alpha)|^2.

Both are positive real conjugates in Q(sqrt(5)), and AB=N_K/Q(alpha)>0.
Since J=zeta_5/phi,

    |sigma_1(J)|^2 = phi^-2,
    |sigma_2(J)|^2 = phi^2,

so

    A(J alpha)/B(J alpha) = phi^-4 A(alpha)/B(alpha).

The half-open intervals

    [phi^(4m), phi^(4m+4)),  m in Z,

partition the positive real line. Therefore every J^Z orbit has exactly one
representative beta satisfying

    1 <= A(beta)/B(beta) < phi^4.

If alpha=J^n beta with beta in the strip, then

    log_(phi^4)(A(alpha)/B(alpha))
      = -n + t,  0<=t<1,

hence

    n = -floor(log_(phi^4)(A/B)).

No logarithm is required computationally.

Write

    alpha bar(alpha)=u+v phi,  u,v in Z.

For alpha=a+b zeta+c zeta^2+d zeta^3, direct multiplication gives

    u = a^2-ab+b^2-bc+c^2-cd+d^2,
    v = ab-ac-ad+bc-bd+cd.

The two real embeddings are

    A = u+v phi,
    B = u+v-v phi,

and

    N(alpha)=AB=u^2+uv-v^2.

Now

    A-B = v sqrt(5),

so A>=B iff v>=0. Also phi^4=2+3phi and direct reduction gives

    phi^4 B - A = (u-v)(1+2phi).

The fixed factor 1+2phi is positive. Therefore

    1 <= A/B < phi^4
      iff v>=0 and u-v>0.

This is the exact integer strip test. Multiplying by J or J^-1 changes the
ratio by one exact factor phi^-4 or phi^4, so repeated exact integer
comparisons terminate at the unique strip representative.

This orientation is the counterpart of the predecessor half-open strip
phi^-4 < A/B <= 1. They are related by one J-step and a boundary convention.

## 3. Finite coefficient box and ten representatives per ideal

For beta in the oriented strip write

    A/B = phi^(4t),  0<=t<1.

Since AB=N(beta),

    |sigma_1(beta)| = N(beta)^(1/4) phi^t,
    |sigma_2(beta)| = N(beta)^(1/4) phi^-t.

Write beta=sum_(j=0)^3 a_j zeta^j and set a_4=0. Fourier inversion on C5 gives

    a_j = (1/5) sum_(m=1)^4 sigma_m(beta)
                     (zeta^(-mj)-zeta^(-4m)).

Pairing complex-conjugate embeddings and using absolute values yields

    |a_j| <= (4/5)(|sigma_1(beta)|+|sigma_2(beta)|)
           < (4/sqrt(5)) N(beta)^(1/4),

because for 0<=t<1,

    phi^t + phi^-t < phi + phi^-1 = sqrt(5).

Thus every beta with N(beta)<=X satisfies the strict integer bound

    25 |a_j|^4 < 256 X.

This is the complete finite coefficient box used by the verifier.

Public J-HARMONIC-SEAM gives

    O_K^x = mu_10 x <phi>,

and public CYCLOTOMIC-CLASS-NUMBER-ONE gives h_K=1. Since

    J = zeta_5 phi^-1,

the quotient of O_K^x by <J> has exactly ten classes represented by mu_10.
Indeed, if two roots of unity xi,eta differ by J^n, then taking absolute value
in the principal embedding gives 1=phi^-n, hence n=0 and xi=eta.

Every nonzero integral ideal is principal. Its generators form one
O_K^x-torsor, so modulo <J> there are exactly ten generator orbits. Section 2
places exactly one representative from each such J-orbit in the strip.
Therefore, for every X>=1,

    |B_X| = 10 A_K(X),

where B_X is the set of strip representatives with norm at most X and A_K(X)
is the number of nonzero integral ideals of norm at most X.

Independently, prime splitting in Q(zeta_5) gives local ideal factors

    p=5:          (1-T)^-1,
    p=1 mod 5:    (1-T)^-4,
    p=4 mod 5:    (1-T^2)^-2,
    p=2,3 mod 5:  (1-T^4)^-1.

Hence the coefficient at p^e is respectively

    1,
    binom(e+3,3),
    e/2+1 if e is even and 0 if e is odd,
    1 if 4 divides e and 0 otherwise.

This is a second exact count independent of lattice enumeration.

## 4. Native scalar capacity

Import the public theorem U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]. On the
origin-zero reachable domain, for every stipulated target bijection L,

    R(n,x)=L^n G(ell_n(x)),

where ell_n is onto F_5^5 and is a bijection on each synchronized sheet n>=3.

Choose the target bijection L(alpha)=J alpha on nonzero integral scalars.
Suppose two distinct labels i,j satisfy

    G(i)=J^m G(j).

Choose n large enough that n>=3 and n+m>=3. Then the reachable point carrying
label i at time n and the reachable point carrying label j at time n+m have
the same scalar:

    J^n G(i)=J^(n+m)G(j).

Thus global injectivity across all reachable sheets forces all 3125 labels into
distinct J-orbits.

Because J has norm one, each orbit has one strip representative of the same
norm. Therefore a uniform norm bound X provides exactly |B_X| available
orbits. Conversely any injection of F_5^5 into B_X yields a globally
injective U-to-J reader. Hence

    X_min = min{X: |B_X|>=3125}.

The frozen finite counts |B_940|=3110 and |B_941|=3150 decide

    X_min=941.

The lexicographic injection ordered by (norm, coefficient tuple) is one
existence witness. Nothing in the native theorem selects that codebook or even
selects L=times J among all target bijections.

## 5. QDD Galois sum-ratio identity

Use exactly the public Route A map

    alpha = iota_B0(v)
          = v_0 + v_1 zeta + v_2 zeta^2 + v_3 zeta^3.

The registered trace pairing is

    <x,y>_tr = (1/5) Tr_K/Q(x bar(y)),

and in the B0 basis its Gram matrix is

    G = I - (1/5) 1 1^T.

For Q=sum v_j^2 and s=sum v_j,

    (1/5) Tr_K/Q(alpha bar(alpha))
      = v^T G v
      = Q - s^2/5.

Therefore

    Tr_K/Q(alpha bar(alpha)) = 5Q-s^2.

But alpha bar(alpha) lies in the real subfield k. Its two real embeddings are
A and B, while K/k is quadratic and complex conjugation fixes the element.
Therefore

    Tr_K/Q(alpha bar(alpha))
      = 2 Tr_k/Q(alpha bar(alpha))
      = 2(A+B).

Consequently

    5Q-s^2 = 2(A+B).

On every supported QDD source the denominator is positive, so the already
registered incidence ratio rewrites exactly:

    s^2/[4(5Q-s^2)] = s^2/[8(A+B)].

Thus the existing QDD arithmetic supplies the symmetric Galois sum A+B,
whereas the J-strip normalization uses the positive ratio A/B. This is a
relation between two existing L1 arithmetic readings. It does not establish
physical completeness, uniqueness, occurrence, sampling or measurement.

## 6. Landau specialization

External standard theorem, Landau ideal counting: for a fixed degree-n number
field F,

    A_F(X)=kappa_F X + O_F(X^(1-2/(n+1))),

where kappa_F=Res_(s=1) zeta_F(s).

For K of degree four,

    1-2/(4+1)=3/5.

Using Section 1,

    A_K(X)
      = [4 pi^2 log(phi)/(25 sqrt(5))] X + O_K(X^(3/5)).

The finite value A_K(10^6)=339775 is only an exact audit witness and is not a
proof of the asymptotic theorem.

## 7. Scope boundary

All statements above are L1 arithmetic. The possible future factorization of a
concrete 25-element native carrier as

    (mu_10/{+/-1}) x O_K/(1-zeta_5)

is explicitly outside this proof until one exact carrier, its actions and
equality are frozen.

No physical clock, preferred decoder, Born rule, apparatus, event, occurrence,
measure, SI scale or L2-L6 bridge follows.
