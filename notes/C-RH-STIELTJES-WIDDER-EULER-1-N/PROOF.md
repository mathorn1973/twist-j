# Euler-half-plane Stieltjes and Widder reduction

```text
STATUS:        candidate-T / NON-CANONICAL INCUBATION
PUBLIC BASIS:  Public Canon v57
PARENT:        issue #471 under mathematical parent #374
RH:            unchanged and open
NOVELTY:       no novelty claimed for Widder's theorem or the Stieltjes class
```

## 0. Result and boundary

Let

```text
xi(s) = (1/2)s(s-1)pi^(-s/2)Gamma(s/2)zeta(s),
u=s(s-1),
q=2s-1,
f(u)=q^(-1)xi'(s)/xi(s),                 s>1.
```

Then:

1. `f` is the logarithmic derivative of one entire function in the functional
   equation variable `u`.
2. RH holds if and only if `f` is a Stieltjes function.
3. By Widder's theorem, RH holds if and only if the following inequalities all
   hold in the absolutely convergent Euler half-plane:

   ```text
   f(u)>=0,
   W_k(u):=(-1)^(k-1)D_u^(2k-1)[u^k f(u)]>=0
   for every k>=1 and every u>0.
   ```

4. The first two inequalities, `f>=0` and `W_1>=0`, hold unconditionally.
   Thus the first possible Widder obstruction is `W_2`.
5. A literal individual Euler prime atom is not Stieltjes: its boundary
   density changes sign infinitely often. Any positive source theorem must
   reorganize prime and archimedean terms globally.

This is an exact reduction, not a proof of RH and not evidence for RH. It does
not produce all inequalities. It identifies the missing source theorem and
removes finite zero data from the criterion.

## 1. The functional-equation coordinate

Put

```text
a=s-1/2,
X(a)=xi(1/2+a).
```

The functional equation `xi(s)=xi(1-s)` says exactly that `X` is even:

```text
X(a)=X(-a).
```

Since `X` is entire, its Taylor series contains only even powers. Therefore
there is a unique entire function `Y` such that

```text
X(a)=Y(a^2).
```

Indeed, if `X(a)=sum_(n>=0)c_(2n)a^(2n)`, then
`Y(w)=sum_(n>=0)c_(2n)w^n`, and the latter series has infinite radius.
Define

```text
calX(u)=Y(u+1/4).
```

Since

```text
u=s(s-1)=(s-1/2)^2-1/4=a^2-1/4,
```

we have

```text
calX(u)=xi(s)=xi(1-s).
```

Thus `calX` is single-valued and entire in `u`. The map

```text
s in (1,infinity) -> u=s(s-1) in (0,infinity)
```

is a bijection, with

```text
q=du/ds=2s-1=sqrt(1+4u)>1,
D_u=q^(-1)D_s.
```

## 2. Zeros and the genus-zero product

Let `rho` be a nontrivial zero of `xi`, with multiplicity `m_rho`, and put

```text
alpha=rho-1/2,
z_rho=rho(rho-1)=alpha^2-1/4.
```

The functional partner `1-rho` corresponds to `-alpha` and has the same
`z_rho`. Hence one zero of `calX` corresponds to one unordered functional pair
`{rho,1-rho}`, with the original multiplicity, not twice the multiplicity.
Complex conjugation sends `z_rho` to `conj(z_rho)`.

The centered function `X` is an even entire function of order one. The function
`Y` has order at most one half. Hadamard factorization of `Y` therefore has
genus zero and permits only a constant exponential factor. Since
`X(0)=xi(1/2)` is nonzero,

```text
X(a)=X(0) product_P (1-a^2/alpha_P^2)^(m_P),
```

where `P` runs once over unordered functional pairs. The product converges
locally uniformly because

```text
sum_P m_P/|alpha_P|^2 < infinity.
```

After the translation `a^2=u+1/4`,

```text
calX(u)=X(0) product_P
  (1-(u+1/4)/(z_P+1/4))^(m_P).
```

There is no nonconstant exponential factor. Logarithmic differentiation is
absolutely and locally uniformly convergent away from the zeros and gives

```text
f(u):=calX'(u)/calX(u)
     =sum_P m_P/(u-z_P).                            (2.1)
```

Every pole residue is the positive integer multiplicity. Distinct functional
pairs can share a pole only by sharing the same zero of `calX`; their
multiplicities then add and cannot cancel.

## 3. Exact Euler display on `s>1`

From the definition of `xi`,

```text
xi'(s)/xi(s)
 =1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2)+zeta'(s)/zeta(s).
```

For `s>1`, the logarithmic derivative of the Euler product is absolutely and
locally uniformly convergent:

```text
zeta'(s)/zeta(s)=-sum_(n>=2)Lambda(n)n^(-s).
```

Since

```text
q^(-1)(1/s+1/(s-1))
 =q^(-1)(2s-1)/(s(s-1))
 =1/u,
```

we obtain the exact source-side formula

```text
f(u)=1/u+(1/q)[(1/2)psi(s/2)-(1/2)log pi
               -sum_(n>=2)Lambda(n)n^(-s)],          (3.1)
q=2s-1, u=s(s-1), s>1.
```

Every differentiated von Mangoldt series used in a Widder expression is
locally uniformly absolutely convergent on `s>1`, because for every fixed
integer `r>=0` and every `sigma>1`,

```text
sum_(n>=2)Lambda(n)(log n)^r n^(-sigma)<infinity.
```

Thus the complete real-variable criterion below lies inside the ordinary
Euler-product half-plane. No limit at `s=1` and no zero table is used.

## 4. Stieltjes equivalence

Use the Stieltjes convention

```text
h(u)=C+integral_[0,infinity)dmu(t)/(u+t),
C>=0, mu>=0, integral dmu(t)/(1+t)<infinity.
```

### 4.1 RH implies Stieltjes

Under RH, each functional pair is

```text
rho=1/2+i gamma,
1-rho=1/2-i gamma,
gamma>0,
```

and

```text
z_rho=rho(rho-1)=-(gamma^2+1/4).
```

Equation (2.1) becomes

```text
f(u)=sum_(gamma>0)m_gamma/(u+gamma^2+1/4)
    =integral_[0,infinity)dmu(t)/(u+t),

mu=sum_(gamma>0)m_gamma delta_(gamma^2+1/4).
```

The measure is nonnegative. Its Stieltjes integrability follows from the
paired-product convergence:

```text
sum_(gamma>0)m_gamma/(1+gamma^2+1/4)<infinity.
```

Thus `f` is Stieltjes, with `C=0`.

### 4.2 Stieltjes implies RH

Assume that the real function `f` on `(0,infinity)` is Stieltjes. Its
Stieltjes representation extends analytically to

```text
C minus (-infinity,0].
```

The xi-side expression (2.1) is meromorphic. The two analytic functions agree
on the positive real axis, hence on the connected common domain by the
identity theorem.

Write a nontrivial zero as

```text
rho=beta+i gamma,
0<beta<1,
gamma!=0.
```

Then

```text
z_rho
 =beta(beta-1)-gamma^2+i gamma(2beta-1).
```

If `beta!=1/2`, the imaginary part is nonzero, so `z_rho` lies outside the
Stieltjes cut. Equation (2.1) has there a pole with positive integer residue.
No other pole can cancel it. But the Stieltjes continuation is analytic there,
a contradiction. Therefore every nontrivial zero has `beta=1/2`. This is RH.

We have proved

```text
RH iff f is a Stieltjes function.                    (4.1)
```

This is a pole-location reformulation, not an Euler-side positivity proof.

## 5. Widder's exact real-variable hierarchy

Widder's theorem, in the form restated and proved by Sokal in
arXiv:0902.0065, Theorem 1, says that a real-valued function `h` on
`(0,infinity)` is Stieltjes if and only if it is smooth and

```text
F_(0,0)(u)=h(u)>=0,
F_(k-1,k)(u)>=0 for every k>=1,
```

where

```text
F_(n,k)(u)=(-1)^n D_u^(n+k)[u^k h(u)].
```

For `n=k-1`, this is

```text
F_(k-1,k)(u)
 =(-1)^(k-1)D_u^(2k-1)[u^k h(u)].
```

Applying the theorem to `f` and using (4.1) gives the exact criterion

```text
RH iff f(u)>=0 and W_k(u)>=0
       for every k>=1 and every u>0,                  (5.1)

W_k(u):=(-1)^(k-1)D_u^(2k-1)[u^k f(u)].
```

Since `D_u=q^(-1)D_s`, the same criterion in the ordinary Euler half-plane is

```text
RH iff f(s)>=0 and

(-1)^(k-1)(q^-1 D_s)^(2k-1)
[(s(s-1))^k(q^-1 xi'(s)/xi(s))]>=0

for every k>=1 and every real s>1.                    (5.2)
```

The differential operator is an iterated operator. Derivatives hit `q^-1` at
each iteration. It must not be replaced by `q^(-(2k-1))D_s^(2k-1)`.

No finite initial part of (5.1) is sufficient.

## 6. The first rung is unconditional

For any nontrivial zero, put

```text
z=-A+iB,
A=gamma^2+beta(1-beta)>0,
B=gamma(2beta-1).
```

If `B!=0`, the conjugate functional pair supplies `conj(z)`. Its contribution
to `f` is

```text
1/(u-z)+1/(u-conj(z))
 =2(u+A)/((u+A)^2+B^2)>0.                    (6.1)
```

If `B=0`, the one real pole contributes `1/(u+A)>0`. Since the series is
absolutely convergent, summing (6.1) proves

```text
f(u)>0 for every u>0                             (6.2)
```

without RH.

For `k=1`, Widder's quantity is

```text
W_1(u)=D_u[u f(u)].
```

The conjugate-pair contribution is

```text
D_u[u/(u-z)+u/(u-conj(z))]
 =2[A(u+A)^2+B^2(2u+A)]/((u+A)^2+B^2)^2>0.       (6.3)
```

The real-pole contribution is `A/(u+A)^2>0`. The series again converges
absolutely, since each term is `O(1/|z|)`. Therefore

```text
W_1(u)>0 for every u>0                            (6.4)
```

unconditionally.

Consequently the first possible obstruction in Widder's minimal hierarchy is

```text
W_2(u)=-D_u^3[u^2 f(u)].
```

The exact rational breaker confirms the sharpness of this statement on a
synthetic off-line orbit: `f>0` and `W_1>0`, but `W_2<0`.

## 7. One-pole formula for every rung

For one pole `z`, polynomial division gives

```text
u^k/(u-z)
 =sum_(j=0)^(k-1) z^j u^(k-1-j)+z^k/(u-z).       (7.1)
```

The polynomial has degree `k-1`, so its derivative of order `2k-1` vanishes.
Also

```text
D_u^(2k-1)[1/(u-z)]
 =-(2k-1)!/(u-z)^(2k).
```

Multiplying by the Widder sign yields

```text
(-1)^(k-1)D_u^(2k-1)[u^k/(u-z)]
 =(2k-1)!(-z)^k/(u-z)^(2k).                    (7.2)
```

For a conjugate pair, the contribution is

```text
2(2k-1)! Re[((-z)/(u-z)^2)^k].                 (7.3)
```

For a critical-line pole, `z=-t<0`, the base in (7.3) is the positive real
number `t/(u+t)^2`, so every rung is positive. For an off-line pair the base is
nonreal except at isolated choices of `u`; its powers can enter the negative
half-plane. The complete hierarchy detects every off-cut pole by (4.1) and
Widder's theorem. Formula (7.3) explains why a small angular defect or a high
ordinate can postpone the first negative rung.

This is not a replacement for issue #469. That issue owns an explicit finite
window and tail bound. Here no height bound is claimed.

## 8. Literal prime-local Stieltjes positivity fails

For `ell>0`, isolate the unsigned Euler atom

```text
p_ell(u)=exp(-ell s(u))/q,
q=sqrt(1+4u),
s=(1+q)/2.
```

Take the upper lip of the branch cut below `-1/4`:

```text
u=-1/4-y^2/4+i0,
y>0.
```

For the principal square root,

```text
q=iy,
s=(1+iy)/2.
```

Writing

```text
C=cos(ell y/2),
S=sin(ell y/2),
E=exp(-ell/2),
```

we obtain

```text
p_ell(u)
 =E(C-iS)/(iy)
 =E(-S-iC)/y.
```

Hence its upper-lip Stieltjes density is

```text
-(1/pi)Im p_ell(u)
 =E cos(ell y/2)/(pi y).                       (8.1)
```

This changes sign infinitely often as `y` increases. Multiplying by the
nonzero Euler coefficient, including its minus sign, only reverses the sign
pattern and does not make it nonnegative.

Therefore an individual prime or prime-power term in the literal Euler sum is
not a Stieltjes function. The archimedean and prime terms must be reorganized
globally if the Euler side is to prove (5.1). This is a bounded local no-go. It
does not exclude a different prime-defined quadratic object or a global
operator construction.

## 9. What has and has not moved

### Earned at candidate grade

```text
[candidate-T] xi descends to an entire functional-equation coordinate u.
[candidate-T] RH iff its logarithmic derivative f is Stieltjes.
[candidate-T] RH iff the complete Euler-half-plane Widder hierarchy holds.
[candidate-T] f>0 and W_1>0 unconditionally.
[candidate-T] the one-pole formula (7.2).
[candidate-T] literal per-prime Stieltjes positivity is impossible.
[candidate-C] exact synthetic controls, including low W_2 failure and a
              delayed first failure at rung 32 for the high control.
```

### Not earned

```text
No proof of any W_k>=0 for all k>=2.
No proof or evidence for RH.
No finite-prefix criterion.
No actual zero exclusion.
No J-native Weil carrier.
No movement of LAMBDA-COCYCLE-ANGLES [H].
No public Canon, Registry, Frontier, evidence, or probe result.
```

The source bar is now exact. A genuine positive advance must prove every
Widder inequality from the global Euler and archimedean expression (3.1), or
construct an independently positive object whose Stieltjes transform is `f`.
