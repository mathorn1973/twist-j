# Proof: residue, unit strip, scalar capacity and QDD Galois bridge

Status: theorem-grade derivation candidate for P-ZETA5-RESIDUE-STRIP-DECODER-1.
Scope: L1 arithmetic only.

The proof imports only the named public TWIST-J rows and standard external
number-theory theorems explicitly marked below. It does not import the
predecessor verifier output as proof.

## 1. Dedekind residue

External standard theorem, analytic class number formula:

    Res_(s=1) zeta_F(s)
      = 2^r1 (2 pi)^r2 h_F R_F / (w_F sqrt(|d_F|)).

For K=Q(zeta_5), public exact inputs are

    r1=0, r2=2, h_K=1, w_K=10, |d_K|=125, R_K=2 log(phi).

Therefore

    Res zeta_K
      = (2 pi)^2 * 2 log(phi) / (10 sqrt(125))
      = 8 pi^2 log(phi) / (50 sqrt(5))
      = 4 pi^2 log(phi) / (25 sqrt(5)).

For k=Q(sqrt(5)),

    r1=2, r2=0, h_k=1, w_k=2, d_k=5, R_k=log(phi),

so

    Res zeta_k = 4 log(phi)/(2 sqrt(5))
               = 2 log(phi)/sqrt(5).

Hence

    Res zeta_K / Res zeta_k = 2 pi^2/25.

The bookkeeping can be read directly before cancellation:

    (R_K/R_k) * ((2 pi)^2 / 2^2)
    --------------------------------
    sqrt(d_K/d_k) * (w_K/w_k)

      = 2 * pi^2 / (5 * 5)
      = 2 pi^2/25.

Thus the two denominator fives have different exact sources:
sqrt(125/5)=5 from discriminants and 10/2=5 from roots of unity.

For the quartic Dirichlet character modulo five normalized by

    kappa(1)=1, kappa(2)=i, kappa(3)=-i, kappa(4)=-1,

one has

    S = sum conjugate(kappa(a)) a
      = 1 - 2i + 3i - 4
      = -3+i,

so |S|^2=10. The standard primitive odd-character formula gives

    L(1,kappa)
      = -(pi i / 5^2) tau(kappa) S

up to the conventional harmless conjugation/sign choice of the Gauss sum,
and |tau(kappa)|^2=5. Therefore

    |L(1,kappa)|^2
      = pi^2 * 5 * 10 / 5^4
      = 2 pi^2/25.

Equivalently, the abelian factorization of the Dedekind zeta function gives

    zeta_K = zeta_k L(s,kappa)L(s,bar(kappa)),

with the real quadratic character kappa^2 already contained in zeta_k.

The Gaussian integer factorization -3+i=(1+i)(-1+2i), of norms 2 and 5,
is an exact witness only. No theorem here identifies those factors as a
structural derivation of w_K.

## 2. The oriented J-strip

Let alpha be nonzero and set

    A = |sigma_1(alpha)|^2,
    B = |sigma_2(alpha)|^2.

Both are positive real conjugates in Q(sqrt(5)), and AB=N_K/Q(alpha)>0.
Since

    |sigma_1(J)|^2 = phi^-2,
    |sigma_2(J)|^2 = phi^2,

one J-step gives

    A(J alpha)/B(J alpha) = phi^-4 A(alpha)/B(alpha).

The half-open intervals

    [phi^(4m), phi^(4m+4)),  m in Z,

partition the positive real line. Hence every J^Z orbit has exactly one
representative beta satisfying

    1 <= A(beta)/B(beta) < phi^4.

If alpha=J^n beta with beta in the strip, then

    log_(phi^4)(A(alpha)/B(alpha))
       = -n + t,  0<=t<1,

so

    n = -floor(log_(phi^4)(A/B)).

No logarithm is needed computationally.

Write the relative norm

    alpha bar(alpha) = u+v phi, u,v in Z.

For alpha=a+b zeta+c zeta^2+d zeta^3 direct multiplication gives

    u = a^2-ab+b^2-bc+c^2-cd+d^2,
    v = ab-ac-ad+bc-bd+cd,

and

    A = u+v phi,
    B = u+v-v phi,
    N(alpha)=AB=u^2+uv-v^2.

The lower strip inequality A>=B is equivalent to

    A-B = v sqrt(5) >=0,

hence v>=0. Since phi^4=2+3phi,

    phi^4 B - A = (u-v)(1+2phi).

The fixed factor 1+2phi is positive, so A<phi^4 B iff u-v>0. Thus

    1<=A/B<phi^4  iff  v>=0 and u-v>0.

This is the exact integer strip test. To normalize alpha, if v<0 multiply the
working element by J^-1 and increment n; if v>=0 but u-v<=0 multiply it by J
and decrement n. The positive ratio moves by one exact factor phi^4 each
iteration, so the process terminates at the unique strip representative.

This is the oriented counterpart of the predecessor strip
phi^-4 < A/B <= 1. The two are related by one boundary convention/orientation;
they are not competing decompositions.

## 3. Finite coefficient box and exact orbit count

For beta in the oriented strip write

    A/B = phi^(4t), 0<=t<1.

Since AB=N(beta),

    |sigma_1(beta)| = N(beta)^(1/4) phi^t,
    |sigma_2(beta)| = N(beta)^(1/4) phi^-t.

For beta=sum_(j=0)^3 a_j zeta^j, set a_4=0. Fourier inversion on C5 gives

    a_j = (1/5) sum_(m=1)^4 sigma_m(beta)
                         (zeta^(-mj)-zeta^(-4m)).

Taking absolute values and pairing complex conjugate embeddings,

    |a_j| <= (4/5)(|sigma_1(beta)|+|sigma_2(beta)|)
           < (4/sqrt(5)) N(beta)^(1/4),

because phi^t+phi^-t < phi+phi^-1=sqrt(5) for 0<=t<1, with equality excluded
at t=1. Therefore for N(beta)<=X every coefficient satisfies

    25 |a_j|^4 < 256 X.

The verifier searches exactly the complete integer box defined by this strict
inequality.

Public J-HARMONIC-SEAM gives

    O_K^x = mu_10 x <phi>,

and public CYCLOTOMIC-CLASS-NUMBER-ONE gives h_K=1. Since
J=zeta_5 phi^-1, quotienting the unit group by <J> leaves exactly ten classes:
every unit class has a torsion representative, and two distinct elements of
mu_10 cannot differ by J^n unless n=0 because |J^n| is not one for n!=0 in
the principal embedding.

Every nonzero integral ideal is principal. Its generators form one O_K^x
torsor, so modulo <J> it has exactly ten generator orbits. Section 2 gives
exactly one strip representative in each J-orbit. Therefore, for every X>=1,

    |B_X| = 10 A_K(X),

where A_K(X) is the number of nonzero integral ideals of norm at most X.

The ideal count itself is indepently generated from prime splitting in
Q(zeta_5). With T=p^-s, the local factors are

    p=5:         (1-T)^-1,
    p=1 mod 5:   (1-T)^-4,
    p=4 mod 5:   (1-T^2)^-2,
    p=2,3 mod 5: (1-T^4)^-1.

Thus the coefficient at p^e is respectively

    1,
    binom(e+3,3),
    e/2+1 if e even and 0 if e odd,
    1 if 4|e and 0 otherwise.

This gives a second exact count independent of lattice enumeration.

The half-width negative control 1<=A/B<phi^2 has exact upper test

    phi^2 B - A = (u-2v) phi,

hence it is v>=0 and u-2v>0. It is not a fundamental domain for J^Z.

## 4. Native scalar capacity

Import the public theorem U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]. On the
origin-zero reachable domain it states, for any stipulated target bijection L,

    R(n,x)=L^n G(ell_n(x)),

with ell_n onto F_5^5 and a bijection on each synchronized sheet n>=3.

Choose L(alpha)=J alpha and require nonzero integral scalar values. If two
distinct labels i,j satisfy

    G(i)=J^m G(j),

then choose n large enough that n>=3 and n+m>=3. The two reachable points with
labels i at time n and j at time n+m have the same scalar:

    J^n G(i) = J^(n+m) G(j).

Global injectivity therefore forces the 3125 labels into 3125 distinct J-orbits.
Because N(J)=1, a J-orbit has a uniform algebraic norm, and Section 2 provides
one strip representative. Thus the number of available orbits under norm bound
X is exactly |B_X|.

Conversely, any injection of F_5^5 into distinct strip representatives gives a
globally injective U-to-J reader. Hence

    X_min = min { X : |B_X| >= 3125 }.

The formal finite gate decides the endpoint. The exposed values
|B_940|=3110 and |B_941|=3150 imply X_min=941.

The lexicographic codebook is only one witness. No native theorem selects it.

## 5. QDD Galois sum-ratio identity

Use exactly the public Route A map

    alpha = iota_B0(v) = v_0+v_1 zeta+v_2 zeta^2+v_3 zeta^3,

with balanced rational/integer piston coordinates v_j. Public Route A defines

    <x,y>_tr = (1/5) Tr_K/Q(x bar(y)),
    G = I - (1/5) 1 1^T.

Therefore

    (1/5) Tr(alpha bar(alpha))
      = v^T G v
      = Q - s^2/5,

where Q=sum v_j^2 and s=sum v_j. Multiplying by five gives

    Tr(alpha bar(alpha)) = 5Q-s^2.

But alpha bar(alpha)=u+v phi lies in the real subfield. Its two real embeddings
are A and B, and K/k is quadratic with complex conjugation fixing this element.
Therefore

    Tr_K/Q(alpha bar(alpha))
      = 2 Tr_k/Q(alpha bar(alpha))
      = 2(A+B).

Hence exactly

    5Q-s^2 = 2(A+B).

For supported sources 5Q-s^2>0, so the existing registered conditional
incidence ratio rewrites without changing its value:

    s^2/[4(5Q-s^2)] = s^2/[8(A+B)].

Thus the existing QDD arithmetic reads the symmetric Galois sum A+B, while the
J-strip uses the positive ratio A/B. This is a relation between two existing
L1 arithmetic readings. It does not prove physical completeness, uniqueness,
occurrence, sampling or measurement.

## 6. Landau specialization

External standard theorem, Landau ideal-counting estimate: for a fixed number
field F of degree n,

    A_F(X) = kappa_F X + O_F(X^(1-2/(n+1))),

where kappa_F=Res_(s=1) zeta_F(s).

For K of degree four, the exponent is

    1 - 2/5 = 3/5.

Section 1 gives kappa_K exactly, therefore

    A_K(X)
      = [4 pi^2 log(phi)/(25 sqrt(5))] X + O_K(X^(3/5)).

The exact finite witness A_K(10^6)=339775 is an audit point, not a proof of the
asymptotic theorem.

## 7. Scope

Everything above is L1 arithmetic. The possible 25-element factorization
(mu_10/{+/-1}) x O_K/(1-zeta_5) is deliberately excluded until one concrete
native 25-carrier and its actions are frozen.

No physical clock, preferred decoder, Born law, apparatus, event, occurrence,
measure, SI scale or L2-L6 lift follows.
