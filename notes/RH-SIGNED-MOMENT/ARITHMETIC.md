# Arithmetic coefficients, diagonal energy, and local moments

**NON-CANONICAL — proof appendix.**

**Author: A. M. Thorn**

This appendix proves exact formulas for the finite coefficients, a
uniform bound for their coalesced rational-frequency energy, and a
reduction of the signed moment to pairs having different squarefree
numerator parts and different rational frequencies. It also proves the
normalization and comparison used for the local moment. All results are
unconditional. The sole analytic input to the same-core estimate is the
uniform fourth-moment consequence (A32) proved in
[ANALYTIC.md, section 4](ANALYTIC.md#4-fourth-moments-uniformly-in-every-finite-cutoff).

## 1. Definitions and exact numerator coefficients

Fix $1/4<\sigma<1/2$ and real $Y,M,K\ge1$. All summation
variables are positive integers, and all cutoffs are literal.
Let $\chi=\chi_5$ be the real character modulo 5 with values
$\chi(1)=\chi(4)=1$, $\chi(2)=\chi(3)=-1$, and
$\chi(0)=0$. A prime is called split when it is congruent to
1 or 4 modulo 5. Let $\mathcal R$ consist of 1 and the squarefree
products of split primes, and set
$f(r)=(-2)^{\omega(r)}$ on $\mathcal R$, zero elsewhere.
Write $\ell(v)=(-1)^{\Omega(v)}$, where $\Omega$ counts prime
factors with multiplicity, and $\operatorname{rad}(1)=1$. Define

$$
\begin{split}
A_M(t)&=\sum_{a\le M}\chi(a)a^{\sigma-1+it},\\
B_M(t)&=\sum_{b\le M}\chi(b)b^{-2\sigma-2it},\\
S_{Y,K}(s)&=
\sum_{\substack{r\le Y,\ r\in\mathcal R\\
v\le K,\ \operatorname{rad}(v)\mid r}}
f(r)\ell(v)r^{-s}v^{-2s},\\
\mathcal P(t)&=A_M(t)B_M(t)S_{Y,K}(\sigma+it).
\end{split}
\tag{R1}
$$

Coalesce the integer numerators before multiplying by $A_M$:

$$
\begin{split}
B_M(t)S_{Y,K}(\sigma+it)&=\sum_Nd_NN^{-\sigma-it},\\
D_r(n;M,K)&=
\sum_{\substack{v\mid n,\ n/M\le v\le K\\
\operatorname{rad}(v)\mid r}}\ell(v),\\
\boxed{d_{rn^2}=f(r)\chi(n)D_r(n;M,K)}
&\qquad(r\le Y,\ r\in\mathcal R).
\end{split}
\tag{R2}
$$

All other squarefree parts have zero coefficient. To prove the formula,
write every representation as $N=r(vb)^2$. Uniqueness of the
squarefree part gives $n=vb$, and the restrictions on $b,v$ are
exactly those in $D_r$. Since every prime dividing $v$ is split,
$\chi(v)=1$, so $\chi(b)=\chi(n)$, including when both are zero.
No coprimality between $r$ and $n$ is required. In particular,
nonzero coefficients satisfy $5\nmid n$, $n\le MK$, and
$\chi(N)=1$.

Put $n_r=\prod_{p\mid r}p^{v_p(n)}$. If $n\le M$ and
$n_r\le K$, all $r$-smooth divisors of $n$ are admitted.
In particular this holds when $n\le\min(M,K)$. In this complete
region the exact cancellation is

$$
D_r(n;M,K)
=\prod_{p\mid r}\sum_{j=0}^{v_p(n)}(-1)^j
=:\psi_r(n)
=\mathbf1_{\{v_p(n)\ {\rm even\ for\ all}\ p\mid r\}}.
\tag{R3}
$$

Thus every surviving exponent of $p\mid r$ in $rn^2$ is
$1\pmod4$. Outside the complete region, the finite divisor sum
in (R2) remains essential.

## 2. Short sums and correlations of fixed cores

The parity mask has the unique representation

$$
\psi_r(n)=1
\quad\Longleftrightarrow\quad
n=w^2u,\qquad \operatorname{rad}(w)\mid r,\qquad (u,r)=1.
\tag{R4}
$$

For an interval $I=(x,x+H]$ with $x,H\ge0$, put
$Z=\max(2,x+H)$. Then

$$
\left|\sum_{n\in I}\chi(n)\psi_r(n)\right|
\le
2^{\omega(r)+1}
\prod_{p\mid r}\left(1+\frac{\log Z}{2\log p}\right).
\tag{R5}
$$

Indeed, fix $w$ in (R4) and expand
$\mathbf1_{(u,r)=1}=\sum_{d\mid(u,r)}\mu(d)$.
For $d\mid r$, $\chi(d)=1$. An arbitrary interval sum of
$\chi$ has absolute value at most 2, because its partial sums
over a period are $0,1,0,-1,0,0$. There are
$2^{\omega(r)}$ choices of $d$. The number of possible $w$
is bounded by the product in (R5), by counting each prime exponent.
If the interval is inside the complete region, multiplication by
$|f(r)|$ bounds the corresponding sum of $d_{rn^2}$.
The displayed dependence on $r$ is part of the assertion.

There is also an explicit correlation for fixed cores. Fix
$r,r'\in\mathcal R$ and a nonzero integer $h$. Let
$x\ge\max(0,-h)$, $H\ge0$, and
$Z=\max(2,x+H,x+H+h)$. Define

$$
\begin{split}
c_5(h)&=
\begin{cases}4,&5\mid h,\\-1,&5\nmid h,\end{cases}\\
\kappa(r,r';h)&=
\prod_{\substack{p\mid rr'\\p\nmid(r,r')}}\frac p{p+1}
\prod_{p\mid(r,r')}\frac{p-p^{-v_p(h)}}{p+1}.
\end{split}
\tag{R6}
$$

Then

$$
\boxed{
\sum_{x<n\le x+H}
\chi(n)\chi(n+h)\psi_r(n)\psi_{r'}(n+h)
=\frac{Hc_5(h)}5\,\kappa(r,r';h)
+O_{r,r',h}\!\left((1+\log Z)^{\omega(r)+\omega(r')}\right).}
\tag{R7}
$$

This is uniform in $x,H$ for the stated fixed parameters.
To prove it, use the exact identity
$\psi_r(n)=\sum_{d\mid n,\ \operatorname{rad}(d)\mid r}\ell(d)$
and its counterpart for $r'$. The congruences
$d\mid n,\ e\mid n+h$ are compatible exactly when $(d,e)\mid h$.
If compatible, they form one residue class modulo $[d,e]$, which
is coprime to 5. On each five successive terms of this progression,
the character correlation sums to $c_5(h)$. Direct enumeration
modulo 5 proves that value. Hence

$$
\sum_{\substack{x<n\le x+H\\d\mid n,\ e\mid n+h}}
\chi(n)\chi(n+h)
=\frac{Hc_5(h)}{5[d,e]}+O(1).
\tag{R8}
$$

There are $O_{r,r'}((1+\log Z)^{\omega(r)+\omega(r')})$
pairs $d,e\le Z$. Their errors give the error in (R7).
The infinite main series is absolutely convergent: on compatible
pairs, $1/[d,e]=(d,e)/(de)\le |h|/(de)$.
For a fixed set $S$ of $k\ge1$ primes,

$$
\sum_{\substack{d>Z\\p\mid d\Rightarrow p\in S}}\frac1d
\ll_S \frac{(1+\log Z)^{k-1}}Z.
\tag{R9}
$$

For completeness, in the shell $(Ze^j,Ze^{j+1}]$, fixing
$k-1$ prime exponents leaves a bounded number of choices for the
last. The number of possibilities is
$O_S((1+\log Z+j)^{k-1})$. Summation against $e^{-j}/Z$
proves (R9). The empty prime set has zero tail. Since $H\le Z$,
extending $d,e\le Z$ to infinity changes the main term by no more
than the error in (R7).

The resulting Euler factor at a prime in only one core is
$\sum_{i\ge0}(-1)^ip^{-i}=p/(p+1)$. For a prime in both cores,
put $a=v_p(h)$. Grouping by $m=\min(i,j)$ gives

$$
\begin{split}
\sum_{\substack{i,j\ge0\\\min(i,j)\le a}}
(-1)^{i+j}p^{-\max(i,j)}
&=\sum_{m=0}^a p^{-m}
\left(1+2\sum_{k\ge1}(-p^{-1})^k\right)\\
&=\frac{p-p^{-a}}{p+1}.
\end{split}
\tag{R10}
$$

This proves (R7). Every factor of $\kappa$ is positive. On an
interval where both divisor sums in (R2) are complete, multiplication
by $f(r)f(r')$ gives the actual correlation of $d_{rn^2}$ and
$d_{r'(n+h)^2}$. The sign of its main term is
$\operatorname{sgn}(f(r)f(r')c_5(h))$.
The error is not claimed uniform in growing $r,r',h$.
Moreover, the moment below involves denominators $a,a'$ as well.
Thus (R7) alone does not estimate that moment.

## 3. Positive coefficient estimates and the core weight

Let $a_\chi=1*\chi$, where $*$ is Dirichlet convolution.
At a split prime its local coefficients are $a_\chi(p^e)=e+1$;
at an inert prime they are 1 for even $e$ and 0 for odd $e$;
at 5 they are 1. Thus $a_\chi$ is nonnegative. The partial sums
of $\chi$ are at most 1, so

$$
\sum_{n\le x}a_\chi(n)
=\sum_{m\le x}\sum_{d\le x/m}\chi(d)\le x,
\qquad
\sum_{n\le x}\frac{a_\chi(n)}n\le1+\log x
\quad(x\ge1).
\tag{R11}
$$

The second inequality follows by partial summation. For every
positive integer $h$, summing the last convolution variable with
the first inequality in (R11), and then dropping the product
restriction on the remaining variables, gives

$$
\sum_{n\le x}a_\chi^{*h}(n)\le x(1+\log x)^{h-1},
\qquad
\sum_{n\le x}a_\chi^{*h}(n)n^{-2\sigma}
\le\frac{x^{1-2\sigma}}{1-2\sigma}(1+\log x)^{h-1}.
\tag{R12}
$$

For the weighted estimate, partial summation and
$1+\log t\le1+\log x$ reduce the bound to
$x^{1-2\sigma}+2\sigma\int_1^x t^{-2\sigma}dt \le x^{1-2\sigma}/(1-2\sigma)$.

Define

$$
\begin{split}
V_r&=\prod_{p\mid r}(1-p^{-2\sigma})^{-1},\\
W_\sigma(Y)&=\sum_{\substack{r\le Y\\r\in\mathcal R}}
f(r)^2r^{-2\sigma}V_r^2,\\
\mathfrak C_\sigma&=
\prod_{p\ {\rm split}}
\left(1+\frac4p\bigl((1-p^{-2\sigma})^{-2}-1\bigr)\right).
\end{split}
\tag{R13}
$$

The product converges, and

$$
\boxed{
W_\sigma(Y)\le
\frac{\mathfrak C_\sigma}{1-2\sigma}
Y^{1-2\sigma}(1+\log Y).}
\tag{R14}
$$

Indeed, on squarefree split integers,
$4^{\omega(r)}=a_\chi^{*2}(r)$, so (R12) gives
$\sum_{r\le x,r\in\mathcal R}4^{\omega(r)} \le x(1+\log x)$.
Put $\delta_p=(1-p^{-2\sigma})^{-2}-1>0$ and
$\delta(d)=\prod_{p\mid d}\delta_p$ for $d\in\mathcal R$.
Expand $V_r^2=\sum_{d\mid r}\delta(d)$. Dropping the restriction
$(d,u)=1$ after $r=du$ increases the positive sum, giving

$$
\begin{split}
\sum_{\substack{r\le x\\r\in\mathcal R}}4^{\omega(r)}V_r^2
&\le
\sum_{\substack{d\le x\\d\in\mathcal R}}
4^{\omega(d)}\delta(d)
\sum_{\substack{u\le x/d\\u\in\mathcal R}}4^{\omega(u)}\\
&\le x(1+\log x)
\sum_{d\in\mathcal R}\frac{4^{\omega(d)}\delta(d)}d
=\mathfrak C_\sigma x(1+\log x).
\end{split}
\tag{R15}
$$

Since $\delta_p=O_\sigma(p^{-2\sigma})$, the Euler product
converges absolutely. Weighted partial summation as in (R12)
now proves (R14).

## 4. Rational coalescence and exact torus energy

For relatively prime positive integers $j,k$, define the real
rational coefficient

$$
J(j,k)=
\sum_{\substack{a,b\le M,\ v\le K,\ r\le Y\\
r\in\mathcal R,\ \operatorname{rad}(v)\mid r\\
k r(vb)^2=ja}}
\frac{\chi(a)\chi(b)f(r)\ell(v)}a.
\tag{R16}
$$

The factor $1/a$ follows from
$a^{\sigma-1}N^{-\sigma}=a^{-1}(N/a)^{-\sigma}$.
Consequently, with $\lambda=j/k$,

$$
\mathcal P(t)=\sum_{\lambda=j/k}c_\lambda\lambda^{-it},
\qquad c_\lambda=J(j,k)\lambda^{-\sigma},
\qquad
E_J=\sum_\lambda c_\lambda^2.
\tag{R17}
$$

All sums are finite: $j\le YK^2M^2$ and $k\le M$.
Equal rational frequencies are combined before taking the square.

Take one unit-circle coordinate $z_p$ for each prime occurring
in (R1), with product probability Haar measure. For a positive
rational $q$, put $z(q)=\prod_pz_p^{v_p(q)}$, allowing negative
exponents. Replace $n^{-it}$ by $z(n)$. The phases of $A_M$,
$B_M$, and $S_{Y,K}$ are then $z(a)^{-1}$, $z(b)^2$,
and $z(r)z(v)^2$, respectively. Unique factorization gives
$\int z(q)\overline{z(q')}\,dz=\mathbf1_{q=q'}$, hence

$$
\boxed{E_J=\|\mathcal P\|_{L^2(\mathbb T)}^2
=\|A_MB_MS_{Y,K}\|_{L^2(\mathbb T)}^2.}
\tag{R18}
$$

This torus identity tests equality of frequencies exactly; it makes
no replacement of a finite time average by an infinite one.

Let $d_m(n)$ be the coefficient of $\zeta(s)^m$, for a positive
integer $m$. The pointwise inequality

$$
d_m(n)^2\le d_{m^2}(n)
\tag{R19}
$$

has a direct counting proof. At $p^e$, the left side counts pairs
of compositions of $e$ into $m$ nonnegative parts. Every such
pair occurs as the row and column sums of a nonnegative integer
$m$-by-$m$ matrix of total $e$: fill rows against the remaining
column totals successively. The set of these matrices has size
$d_{m^2}(p^e)$. Its map to the two margins is onto, proving the
inequality at each prime power and therefore at every $n$.

For $u>1/2$ and
$L(z)=\sum_{n\le M}b_n n^{-u}z(n)$, $|b_n|\le1$,
the coefficients of $L^m$ have modulus at most $d_m(n)n^{-u}$.
Orthogonality and (R19) give

$$
\|L\|_{2m}^{2m}
\le\sum_n d_m(n)^2n^{-2u}
\le\zeta(2u)^{m^2}.
\tag{R20}
$$

Both coordinate inversion and coordinate squaring preserve Haar
measure. Applying (R20) to $A_M,B_M$, for every even $q\ge2$,
therefore yields

$$
\|A_M\|_q\le\zeta(2-2\sigma)^{q/4},
\qquad
\|B_M\|_q\le\zeta(4\sigma)^{q/4}.
\tag{R21}
$$

These estimates are independent of $M$ and of the torus dimension.

## 5. Support moments and uniformity in the smooth cutoff

For a positive integer $b_0$, define

$$
F_U^{(b_0)}(z)=
\sum_{\substack{r\le U,\ r\in\mathcal R\\(r,b_0)=1}}
f(r)r^{-\sigma}z(r),\qquad U\ge1.
\tag{R22}
$$

Since $|f(r)|^2=a_\chi^{*2}(r)$ on $\mathcal R$, (R12)
implies

$$
\|F_U^{(b_0)}\|_2
\le(1-2\sigma)^{-1/2}
U^{1/2-\sigma}(1+\log U)^{1/2}.
\tag{R23}
$$

For the fourth moment, the unweighted coefficients of
$(F_U^{(b_0)})^2$ are bounded in modulus by the coefficients
of $\prod_{p\ {\rm split}}(1+2p^{-s})^2$.
At each prime their values are bounded by $d_4(p^e)$; their
squares are bounded by $d_{16}(p^e)$, using (R19).
At a split prime this is exactly the local coefficient of
$a_\chi^{*8}$. The positive majorant may also include the other
primes, absent from the polynomial. The length of the square is
at most $U^2$, so (R12) proves

$$
\|F_U^{(b_0)}\|_4^4
\le\frac{U^{2(1-2\sigma)}}{1-2\sigma}(1+2\log U)^7.
\tag{R24}
$$

Choose an even integer $q\ge8$, and put
$p=2q/(q-4)$. Then $2<p\le4$ and
$1/p=(1-8/q)/2+(8/q)/4$. Interpolation between (R23)
and (R24) gives

$$
\|F_U^{(b_0)}\|_p
\le C_\sigma U^{1/2-\sigma}
(1+\log U)^{1/2+10/q}.
\tag{R25}
$$

The constant is independent of $q,b_0,U$, since only two fixed
endpoint constants are interpolated.

In the $v$-term of $S_{Y,K}$, put $k=\operatorname{rad}(v)$.
If $k>Y$ or a prime of $k$ is not split, the term is absent.
Otherwise $r=ku$ with $(k,u)=1$ and
$f(r)=f(k)f(u)$. Multiplication by $z(k)z(v)^2$ preserves
every torus norm. Equation (R25) consequently gives

$$
\left\|\sum_{\substack{r\le Y,\ r\in\mathcal R\\k\mid r}}
f(r)r^{-\sigma}z(r)\right\|_p
\le C_\sigma
Y^{1/2-\sigma}
\frac{2^{\omega(k)}}{\sqrt{k}}
(1+\log Y)^{1/2+10/q}.
\tag{R26}
$$

The exponent $k^{-1/2}$ is exact: it is the product of
$k^{-\sigma}$ and $k^{-(1/2-\sigma)}$.
Minkowski's inequality now sums the $v^{-2\sigma}$ factors.
Its positive majorant is

$$
\begin{split}
\mathscr R_\sigma
&=\sum_{\substack{v\ge1\\p\mid v\Rightarrow p\ {\rm split}}}
v^{-2\sigma}
\frac{2^{\omega(\operatorname{rad}(v))}}
{\sqrt{\operatorname{rad}(v)}}\\
&=\prod_{p\ {\rm split}}
\left(1+\frac2{\sqrt p(p^{2\sigma}-1)}\right)<\infty.
\end{split}
\tag{R27}
$$

Convergence follows from $1/2+2\sigma>1$. Absorbing this product
into a constant depending only on $\sigma$, we obtain

$$
\|S_{Y,K}\|_p\le
C_\sigma Y^{1/2-\sigma}(1+\log Y)^{1/2+10/q}.
\tag{R28}
$$

This estimate is uniform in $q\ge8$ even and in every finite
$Y,K\ge1$. In particular, no relation between $K,M$, and a
time parameter has been imposed.

## 6. The full diagonal theorem

Put $L_Y=1+\log Y$ and
$Z_\sigma=\zeta(2-2\sigma)\zeta(4\sigma)>1$.
Since $2/q+1/p=1/2$, Hölder's inequality, (R18), (R21), and
(R28) prove

$$
\boxed{
E_J\le C_\sigma
Y^{1-2\sigma}L_Y^{\,1+20/q}Z_\sigma^{q/2},
\qquad q\ge8\ {\rm even}.}
\tag{R29}
$$

Here $C_\sigma$ is independent of $q,Y,M,K$.
Choosing a fixed even $q\ge\max(8,20/\eta)$ gives, for every
$\eta>0$,

$$
\boxed{E_J\ll_{\sigma,\eta}
Y^{1-2\sigma}(1+\log Y)^{1+\eta}
\quad\text{uniformly for }Y,M,K\ge1.}
\tag{R30}
$$

One can also minimize the logarithmic loss. The expression
$(q/2)\log Z_\sigma+(20/q)\log L_Y$ has continuous minimum
$\sqrt{40\log Z_\sigma\log L_Y}$. Choose the next even integer
above its minimizer, or 8 if larger. Rounding, and the bounded
initial range of $Y$, cost only a $\sigma$-dependent factor.
Thus

$$
E_J\ll_\sigma Y^{1-2\sigma}L_Y
\exp\!\left(\sqrt{40\log Z_\sigma\log L_Y}\right).
\tag{R31}
$$

The numerator energy $E_{\rm num}=\sum_Nd_N^2N^{-2\sigma}$
has the same bound (R30), uniformly in $M,K$. Indeed, in the
Hölder proof of (R29), replace $A_M$ by the constant 1, whose
every torus norm is 1. This proves (R29) for $E_{\rm num}$
with $Z_\sigma$ replaced by $\zeta(4\sigma)$, hence the claim.

There is an additional exact character factorization. A nonzero
representation in (R16) has $N=r(vb)^2$, $\chi(N)=1$,
and $5\nmid Na$. Reducing $N/a=j/k$ with $d=(N,a)$ gives
$\chi(j)\chi(k)=\chi(N)\chi(a)\chi(d)^2=\chi(a)$.
If $\widetilde J$ is defined by (R16) with $\chi(a)$ omitted
but with $5\nmid a$ explicitly retained, then

$$
J(j,k)=\chi(j)\chi(k)\widetilde J(j,k),
\qquad
E_J=\sum_{(j,k)=1}\widetilde J(j,k)^2(j/k)^{-2\sigma}.
\tag{R32}
$$

Both coefficient systems vanish when $5\mid jk$. The factors
$\chi(b),f(r),\ell(v)$ remain in $\widetilde J$.
Thus the original factor $\chi(a)$ cannot reduce the coalesced
diagonal. Its effect on distinct-frequency interactions remains
present in the finite moment.

## 7. Exact Fejer normalization and logarithmic blocks

The following identities apply to any finite polynomial
$P(t)=\sum_\lambda c_\lambda e^{-it\log\lambda}$ with positive
frequencies; the coefficients may be complex until the real-kernel
formula below. Let $T\ge2$, $h=1/T$, $t_0=3T/2$, and
$\operatorname{sinc}(x)=\sin(x)/x$, with value 1 at zero.
Define

$$
\begin{split}
d\mu_T(t)&=\frac1{2\pi T}
\operatorname{sinc}^2\!\left(\frac{t-t_0}{2T}\right)\,dt,\\
\mathscr F_T(P)&=\int_{\mathbb R}|P(t)|^2\,d\mu_T(t),\\
\mathcal B_P(z)&=
\sum_{z<\log\lambda\le z+h}c_\lambda e^{-it_0\log\lambda}.
\end{split}
\tag{R33}
$$

Then $d\mu_T$ is a probability measure, and the exact block
identity is

$$
\boxed{
\mathscr F_T(P)=
\frac1h\int_{\mathbb R}|\mathcal B_P(z)|^2\,dz
=\sum_{\lambda,\mu}
c_\lambda\overline{c_\mu}\,
e^{it_0\log(\mu/\lambda)}
\left(1-\frac{|\log(\mu/\lambda)|}{h}\right)_+.}
\tag{R34}
$$

To check both constants, a term with $x=\log\lambda$ is present
for $z\in[x-h,x)$; the overlap of two such intervals has length
$(h-|x-x'|)_+$. Expanding the block square proves the last
expression in (R34). With the Fourier convention
$\widehat g(\tau)=\int_{\mathbb R}g(z)e^{-i\tau z}dz$,
direct integration of the indicator of $[-h,0]$ gives

$$
\widehat{\mathcal B_P}(\tau)=
h e^{i\tau h/2}\operatorname{sinc}(h\tau/2)P(t_0+\tau).
\tag{R35}
$$

Plancherel therefore gives
$h^{-1}\|\mathcal B_P\|_2^2 =(h/(2\pi))\int\operatorname{sinc}^2(h\tau/2) |P(t_0+\tau)|^2d\tau$, exactly the first expression in (R34).
Taking $P=1$ also verifies that $\mu_T$ has mass 1.

For real coefficients define

$$
\mathcal L_T(u)=(1-T|u|)_+\cos(3Tu/2).
$$

Pairing the two orientations of each pair gives

$$
\mathscr F_T(P)=
\sum_\lambda c_\lambda^2+
2\sum_{\lambda<\mu}c_\lambda c_\mu
\mathcal L_T\!\left(\log\frac\mu\lambda\right).
\tag{R36}
$$

The kernel is positive whenever $0<|u|<1/T$, since
$3/2<\pi/2$, and zero for $|u|\ge1/T$.
Thus every nonzero off-diagonal term has the sign of its coefficient
product. This positivity of the kernel does not make the signed
off-diagonal sum nonnegative.

The sharp interval moment is bounded by this same local form:

$$
\boxed{
\frac1T\int_T^{2T}|P(t)|^2dt
\le C_F\mathscr F_T(P),\qquad
C_F=\frac{2\pi}{\operatorname{sinc}^2(1/4)}<7.}
\tag{R37}
$$

On $[T,2T]$, the sinc argument in (R33) has absolute value at
most $1/4$. On that range sinc is positive and decreasing in
the absolute value: the derivative sign follows from
$\sin x-x\cos x=\int_0^x u\sin u\,du>0$.
This proves the comparison. The elementary bounds
$\sin x\ge x-x^3/6$ at $x=1/4$ and $\pi<22/7$ give
$\operatorname{sinc}(1/4)\ge95/96$ and
$C_F\le(44/7)(96/95)^2<7$.

At $Y=T^2$, write $\mathcal N^2=Y^{2-2\sigma}/T$.
The sufficient local test for a sharp moment of order
$\mathcal N^2T^\epsilon$ is therefore

$$
\int_{\mathbb R}|\mathcal B_{\mathcal P}(z)|^2dz
\ll_{\sigma,\epsilon}
\frac{Y^{2-2\sigma}}{T^2}T^\epsilon.
\tag{R38}
$$

There is no unestimated far-frequency remainder in (R34);
the compact support of its kernel is exact. But (R38) is a
sufficient test for the sharp interval moment, not an asserted
equivalent test: its time integral is over the whole real line.

For clarity, an exactly equivalent projected-block test is also
available. Define a bounded Fourier multiplier on $L^2(\mathbb R)$
by
$$
\widehat{\mathcal D_Tg}(\tau)=
\frac{\mathbf1_{\{|\tau|\le T/2\}}}
{\operatorname{sinc}(h\tau/2)}\,\widehat g(\tau).
$$
Its norm is at most $\operatorname{sinc}(1/4)^{-1}$.
Equation (R35) and Plancherel give the exact identity
$$
\frac1T\int_T^{2T}|P(t)|^2dt
=2\pi T\,\|\mathcal D_T\mathcal B_P\|_2^2.
\tag{R39}
$$
This projection is nonlocal in the logarithmic block variable $z$.
It explains precisely the distinction between the sufficient test
(R38) and an equivalent one.

## 8. The entire contribution of one squarefree core

Split (R1) according to its squarefree numerator part:

$$
\begin{split}
\mathcal P&=\sum_{\substack{r\le Y\\r\in\mathcal R}}\mathcal P_r,\\
\mathcal P_r(t)&=
f(r)r^{-\sigma-it}A_M(t)B_M(t)V_{r,K}(t),\\
V_{r,K}(t)&=
\sum_{\substack{v\le K\\\operatorname{rad}(v)\mid r}}
\ell(v)v^{-2\sigma-2it}.
\end{split}
\tag{R40}
$$

Pointwise, $|V_{r,K}(t)|\le V_r$. Therefore
$\sum_r|\mathcal P_r(t)|^2 \le W_\sigma(Y)|A_M(t)B_M(t)|^2$.
The companion [analytic appendix, (A32)](ANALYTIC.md#4-fourth-moments-uniformly-in-every-finite-cutoff)
proves the following all-length estimate with exactly the measure (R33):

$$
\mathscr F_T(A_MB_M)\ll_{\sigma,\epsilon}T^\epsilon,
\qquad T\ge2,\quad M\ge1.
\tag{R41}
$$

Its constants are independent of $M$; it uses no zero hypothesis.
Combining (R14) and (R41) gives

$$
\boxed{
0\le\mathcal Q_{\rm core}:=
\sum_r\mathscr F_T(\mathcal P_r)
\ll_{\sigma,\epsilon}
Y^{1-2\sigma}(1+\log Y)T^\epsilon,}
\quad Y,M,K\ge1.
\tag{R42}
$$

This is the complete signed sector with the same core. It includes
unequal numerators, arbitrary permitted denominator pairs, and all
their internal coalescences. No triangle inequality across distinct
cores was used. Equation (R42) does not bound the sum of absolute
values of the individual pair terms.

Let $E_r$ be the coalesced rational-frequency diagonal within
$\mathcal P_r$, so $E_r=\|\mathcal P_r\|_{L^2(\mathbb T)}^2$.
On the torus too, $|V_{r,K}|\le V_r$. Hölder and (R21) with
$q=4$ imply

$$
\sum_rE_r
\le W_\sigma(Y)\|A_MB_M\|_{L^2(\mathbb T)}^2
\le W_\sigma(Y)\zeta(2-2\sigma)^2\zeta(4\sigma)^2.
\tag{R43}
$$

It follows that the whole same-core, unequal-frequency sector has
absolute value
$$
\left|\sum_r\bigl(\mathscr F_T(\mathcal P_r)-E_r\bigr)\right|
\ll_{\sigma,\epsilon}
Y^{1-2\sigma}(1+\log Y)T^\epsilon.
\tag{R44}
$$
Here the absolute value is taken after summing that signed sector.

## 9. Exact intersection subtraction and the remaining sector

For the support in (R2), define the real amplitude and frequency
$$
w_{r,n,a}=d_{rn^2}(rn^2)^{-\sigma}\chi(a)a^{\sigma-1},
\qquad
\lambda_{r,n,a}=\frac{rn^2}{a},\qquad a\le M.
$$
Let $\mathcal C_{\rm dc}$ be the ordered sum

$$
\mathcal C_{\rm dc}=
\sum_{\substack{r\ne r',\ \lambda_{r,n,a}\ne\lambda_{r',n',a'}\\
|\log(\lambda_{r',n',a'}/\lambda_{r,n,a})|<1/T}}
w_{r,n,a}w_{r',n',a'}
\mathcal L_T\!\left(
\log\frac{\lambda_{r',n',a'}}{\lambda_{r,n,a}}\right).
\tag{R45}
$$

All indices range over the actual finite supports, and both
orientations are included. The exact, disjoint partition is

$$
\boxed{
\mathscr F_T(\mathcal P)
=E_J+\sum_r\bigl[\mathscr F_T(\mathcal P_r)-E_r\bigr]
+\mathcal C_{\rm dc}.}
\tag{R46}
$$

Indeed, all equal rational frequencies belong to the fully
coalesced diagonal $E_J$, including collisions between different
cores. Among unequal frequencies, pairs with equal cores belong
to the middle term, and the other pairs to (R45).
Subtracting $E_r$ removes exactly the intersection of the
equal-core and equal-frequency classes. This is necessary even
though the complete same-core sector is nonnegative.

At $Y=T^2$, equations (R30), (R42), and (R43) yield, after
absorbing logarithms into arbitrarily small powers,

$$
\boxed{
\mathscr F_T(\mathcal P)
=\mathcal C_{\rm dc}
+O_{\sigma,\epsilon}(Y^{1-2\sigma}T^\epsilon),
\qquad M,K\ge1.}
\tag{R47}
$$

In particular,
$$
\frac{E_J}{\mathcal N^2}
\ll_{\sigma,\eta}\frac{(1+\log Y)^{1+\eta}}T,\qquad
\frac{\mathcal Q_{\rm core}}{\mathcal N^2}
\ll_{\sigma,\epsilon}\frac{(1+\log Y)T^\epsilon}{T}.
\tag{R48}
$$

Thus the proposed Fejer test is reduced, with the same arbitrary
epsilon convention, to the signed upper bound

$$
\mathcal C_{\rm dc}
\ \stackrel{?}{\ll}_{\sigma,\epsilon}\
\mathcal N^2T^\epsilon,\qquad Y=T^2.
\tag{R49}
$$

Positivity of the full moment and (R47) already imply
$\mathcal C_{\rm dc}\ge -O_{\sigma,\epsilon}(Y^{1-2\sigma}T^\epsilon)$.
The unproved direction in (R49) is its upper bound.
The fixed-parameter correlation (R7) and the uniform diagonal
bound (R30) do not provide that different-core cancellation.
The reduction (R49) is equivalent to the Fejer test, and remains
only sufficient for the sharp interval target through (R37).
The [analytic appendix](ANALYTIC.md) gives the currently available
global bound and its transfer to the analytic tail; the
[prime-cancellation appendix](PRIME-CANCELLATION.md) examines
explicit signed families inside (R45).
