# Prime-frequency families and signed compensation

A. M. Thorn

**NON-CANONICAL — proof appendix.**

This appendix constructs positive and negative families inside one finite
weighted moment. Their coefficients remain unchanged after all equal rational
frequencies are combined. Each selected determinant equation has only one
admissible solution, so averaging along a long character period cannot explain
their cancellation. A four-term construction has a strictly negative total;
nevertheless, deleting that total leaves a complement too large for the target
bound. The final section combines these exact constructions with the companion
arithmetic and analytic estimates to prove aggregate compensation with a power
saving in the relative error. All results here are unconditional.

## 1. The finite polynomial and its positive moment

Throughout, fix

$$
 \frac14<\sigma<\frac12,\qquad Y\ge10^{12},\qquad
 T=\sqrt Y,\qquad M=\lceil40T\rceil,
 \qquad K\ge1\text{ a finite integer}.
 \tag{P1}
$$

Write $\chi=\chi_5$ for the real primitive character modulo $5$, with
values $1,-1,-1,1,0$ on the classes $1,2,3,4,0$, respectively. Let
$\mathcal R$ contain $1$ and all squarefree products of primes
$p\equiv1,4\pmod5$, and put $f(r)=(-2)^{\omega(r)}$. As usual,
$\omega$ counts distinct prime factors, $\Omega$ counts them with
multiplicity, and $\operatorname{rad}(1)=1$. Define

$$
 \begin{aligned}
 A_M(t)&=\sum_{a\le M}\chi(a)a^{\sigma-1+it},\\
 B_M(t)&=\sum_{b\le M}\chi(b)b^{-2\sigma-2it},\\
 S_{Y,K}(\sigma+it)
 &=\sum_{\substack{r\le Y,\ r\in\mathcal R\\
                   v\le K,\ \operatorname{rad}(v)\mid r}}
 f(r)(-1)^{\Omega(v)}r^{-\sigma-it}v^{-2\sigma-2it},\\
 P(t)&=A_M(t)B_M(t)S_{Y,K}(\sigma+it).
 \end{aligned}
 \tag{P2}
$$

All sums in this appendix are finite. Combining terms with the same integer
numerator gives real integers

$$
 d_N=\sum_{\substack{r(vb)^2=N,\ r\le Y,\ r\in\mathcal R\\
                  v\le K,\ b\le M,\ \operatorname{rad}(v)\mid r}}
       f(r)(-1)^{\Omega(v)}\chi(b),\qquad
 P(t)=\sum_N\sum_{a\le M}
 d_N\chi(a)N^{-\sigma}a^{\sigma-1}(N/a)^{-it}.
 \tag{P3}
$$

Combining again, now over each rational frequency $\lambda=N/a$, writes
$P(t)=\sum_\lambda c_\lambda\lambda^{-it}$, with

$$
 c_\lambda=\lambda^{-\sigma}J(\lambda),\qquad
 J(\lambda)=\sum_{N/a=\lambda}\frac{d_N\chi(a)}a.
 \tag{P4}
$$

Use $\operatorname{sinc}(x)=\sin(x)/x$, continuously extended at zero,
and define the Fejér moment and its real kernel by

$$
 \begin{aligned}
 \mathscr F_T(P)&=\frac1{2\pi T}\int_{\mathbb R}
  \operatorname{sinc}^2\!\left(\frac{t-3T/2}{2T}\right)|P(t)|^2\,dt,\\
 \mathcal L_T(u)&=(1-T|u|)_+\cos(3Tu/2),\\
 \mathscr F_T(P)&=\sum_{\lambda,\mu}
  c_\lambda c_\mu\mathcal L_T(\log(\mu/\lambda))\ge0.
 \end{aligned}
 \tag{P5}
$$

The last identity follows by integrating each term of the finite product:
the Fourier transform of the squared sinc is the triangular function
$(1-T|u|)_+$. Translation by $3T/2$ supplies the phase
$e^{3iTu/2}$; pairing reverse ordered pairs gives its cosine. The integral
converges because a finite exponential sum is bounded and squared sinc is
integrable. We always count ordered pairs, including both orientations.
The kernel is nonnegative everywhere and is positive when $|u|<1/T$.

The squared target scale used below is

$$
 \mathcal N^2=\frac{Y^{2-2\sigma}}T.
 \tag{P6}
$$

This is a scale for the complete signed moment. A large positive subfamily
does not give a lower bound for that complete moment.

## 2. An explicit supply of primes and unique coefficients

Let $\vartheta(x;5,c)=\sum_{p\le x,\ p\equiv c\ (5)}\log p$.
Bennett, Martin, O'Bryant and Rechnitzer, Theorem 1.2, equation (1.12), with
the constants in (1.10)–(1.11), gives

$$
 \left|\vartheta(x;5,c)-\frac x4\right|
 \le\frac{x}{840\log x}
 \quad ((c,5)=1,\ x\ge8\cdot10^9).
 \tag{P7}
$$

This is the only external prime-counting input in the construction.
[Primary source: *Explicit bounds for primes in arithmetic progressions*.](https://arxiv.org/pdf/1802.00085v3)

Set
$\mathscr P_Y=\{Y/2<p\le Y:p\equiv1,4\pmod5\}$ and
$n=|\mathscr P_Y|$. Apply (P7) in the two classes at $Y$ and $Y/2$.
Since $\log(Y/2)\ge\tfrac12\log Y$,

$$
 \left|\sum_{p\in\mathscr P_Y}\log p-\frac Y4\right|
 \le\frac{Y}{210\log Y},\qquad
 \frac{Y}{8\log Y}\le n\le\frac{Y}{\log Y},\qquad n\ge58T.
 \tag{P8}
$$

Indeed, the weighted sum lies between $Y/8$ and $Y/2$; division by
$\log Y$ and $\log(Y/2)$ gives the first two bounds for $n$.
For the last one it suffices that $T\ge464\log Y$. The ratio
$\sqrt Y/\log Y$ is increasing for $Y>e^2$, and at $Y=10^{12}$
the inequality follows already from $\log10<3$. Thus no prime list or
enumeration is needed. The same range gives
$p>Y/2>M$ and $40T\le M\le(81/2)T$.

For every $p\in\mathscr P_Y$, the equation $r(vb)^2=p$ has the unique
solution $r=p,v=b=1$, hence $d_p=-2$. If $M/2<a<M$, then
$(p,a)=1$. An equality $N/a'=p/a$, with positive integers
$a'\le M$, forces $N=kp$, $a'=ka$, and consequently $k=1$.
There are no additional terms at this rational frequency in the full
polynomial (P2). In particular,

$$
 J(p/a)=-\frac{2\chi(a)}a,\qquad
 c_{p/a}=-2\chi(a)p^{-\sigma}a^{\sigma-1}
 \quad(p\in\mathscr P_Y,\ M/2<a<M).
 \tag{P9}
$$

This uniqueness is uniform in $K$. It is stronger than identifying a term
before rational frequencies are combined.

## 3. Positive occupied singleton fibres

Choose the denominator set

$$
 \mathscr A_M=\{a\in\mathbb Z:M/2+2<a<M-2,\ \chi(a)=1\},
 \qquad m=|\mathscr A_M|\ge M/5-4\ge M/6.
 \tag{P10}
$$

The count follows by counting the two residue classes in the indicated
interval. Each $\log(p/a)$, with $p\in\mathscr P_Y$ and
$a\in\mathscr A_M$, lies in an interval of length $\log4$, namely
$(\log(Y/(2M)),\log(2Y/M))$. Partition that interval into half-open bins
of length $1/(20T)$, allowing the final bin to be shorter. Their number
$B$ satisfies $B\le29T$.

Let $m_j$ count all pairs $(p,a)$ in bin $j$, and let $m_{p,j}$
count the pairs with a specified prime. The number $V$ of ordered pairs
in a common bin with different primes obeys

$$
 \begin{aligned}
 V&=\sum_jm_j^2-\sum_p\sum_jm_{p,j}^2
    \ge\frac{n^2m^2}{B}-nm^2
    \ge\frac{n^2m^2}{2B}\\
  &\ge\frac{n^2M^2}{2088T}
    \ge\frac{Y^2M^2}{133632T\log^2Y}.
 \end{aligned}
 \tag{P11}
$$

Here $n\ge2B$ by (P8). The subtraction removes all equal-prime pairs,
including diagonal pairs. Every remaining pair has distinct frequencies:
an equality $p/a=p'/a'$ with $p\ne p'$ would force $p\mid a$,
contrary to $a<M<p$.

For these pairs, set $h=pa'-p'a$. Then

$$
 0<|h|<\frac{YM}{10T}<5Y,\qquad
 \left|\log\frac{p'a}{pa'}\right|<\frac1{20T}.
 \tag{P12}
$$

For fixed $p,p',h$, any two integral solutions of
$pa'-p'a=h$ differ by
$(a,a')\mapsto(a+pz,a'+p'z)$. Because $p,p'>M$, there is at most
one solution with $1\le a,a'\le M$. Thus (P11) counts actual occupied
singleton determinant fibres. Each has different squarefree numerator cores
$p,p'$; there is no character period to average inside such a fibre.

Let $P_+$ be the contribution to (P5) of exactly the ordered pairs in
(P11). Both coefficients have the same sign, and

$$
 c_{p/a}c_{p'/a'}
 =4(pp')^{-\sigma}(aa')^{\sigma-1}
 \ge4Y^{-2\sigma}M^{2\sigma-2},\qquad
 \mathcal L_T(u)\ge\frac{19}{20}\cos\frac3{40}>\frac9{10}.
 \tag{P13}
$$

It follows that

$$
 \boxed{\quad
 \frac{Y^{2-2\sigma}M^{2\sigma}}{37120T\log^2Y}
 \le P_+
 \le144\frac{Y^{2-2\sigma}M^{2\sigma}}{T\log Y}.
 \quad}
 \tag{P14}
$$

For completeness, the upper bound needs no estimate for primes in short
intervals. For fixed $p,a,a'$, the larger necessary condition
$|\log(p'a/(pa'))|<1/T$ places $p'$ in an interval centered
multiplicatively at $q=pa'/a\le2Y$, of length at most $8Y/T$.
It contains at most $9Y/T$ integers. There are at most $nm^2$ choices
of $p,a,a'$, and each coefficient product is at most
$16Y^{-2\sigma}M^{2\sigma-2}$. Use $n\le Y/\log Y$, $m\le M$
and $|\mathcal L_T|\le1$ to obtain (P14).

In particular, this positive part alone exceeds the scale $\mathcal N^2$
by a factor bounded below by a constant times
$T^{2\sigma}/\log^2Y$. Therefore an argument taking absolute values
term by term over all occupied singleton fibres cannot establish the target
scale. This conclusion concerns that absolute-value argument, not the value
of the signed moment.

## 4. A neighbouring negative family

There is an explicit negative family of comparable size in the same finite
polynomial. Define an injection on $\mathscr A_M$ by

$$
 \tau(a)=
 \begin{cases}a+1,&a\equiv1\pmod5,\\a-1,&a\equiv4\pmod5.
 \end{cases}
 \qquad \chi(\tau(a))=-1.
 \tag{P15}
$$

Represent each reverse pair in (P11) by its orientation $p<p'$. Replace
the second denominator $a'$ by $\tau(a')$, and then include both
orientations again. The injection and the sign change show that the images
are distinct and disjoint from the positive family. All denominators remain
strictly between $M/2$ and $M$, so (P9) and the singleton argument
continue to apply. The new logarithmic distance is less than $1/(10T)$,
and every image contribution is strictly negative. Denote their sum by
$P_-$.

Here is an explicit cancellation bound. For a base pair, put
$u=\log(p'a/(pa'))$, $u'=\log(p'a/(p\tau(a')))$, and
$r=(\tau(a')/a')^{\sigma-1}$. The interior margins give
$|u-u'|<2/M$, while the mean value theorem gives $|r-1|\le4/M$.
The kernel is globally Lipschitz, with constant at most $5T/2$. Hence

$$
 |\mathcal L_T(u)-r\mathcal L_T(u')|
 \le\frac{5T+4}{M}\le\frac{7T}{M}.
 \tag{P16}
$$

If $W$ denotes the sum of the positive coefficient products before
inserting the kernel, then $P_+\ge(9/10)W$. Summing (P16), in both
orientations, proves

$$
 |P_++P_-|\le\frac{70T}{9M}P_+<\frac{8T}{M}P_+
 \le\frac15P_+,\qquad
 -\frac65P_+\le P_-\le-\frac45P_+.
 \tag{P17}
$$

This is a uniform constant-factor certificate. It does not assert a lower
bound for the paired residual, nor the power-decaying relative error needed
for the complete target moment.

## 5. Four disjoint actual families

A second construction uses the single residue class

$$
 \mathscr A^{(1)}_M
 =\{a\in\mathbb Z:M/2+4<a<M-4,\ a\equiv1\pmod5\},
 \qquad m_1\ge M/10-3\ge M/12.
 \tag{P18}
$$

Repeat the bin construction of Section 3 with this denominator set. Let
$V_0$ count its ordered equal-bin pairs with different primes, and let
$P_0$ be their positive contribution. The identical argument, with
$m_1\ge M/12$, gives

$$
 \begin{aligned}
 V_0&\ge\frac{n^2M^2}{8352T}
       \ge\frac{Y^2M^2}{534528T\log^2Y},\\
 \frac{Y^{2-2\sigma}M^{2\sigma}}{148480T\log^2Y}
 &\le P_0\le144\frac{Y^{2-2\sigma}M^{2\sigma}}{T\log Y}.
 \end{aligned}
 \tag{P19}
$$

Again choose the canonical orientation $p<p'$ for each reverse pair.
For every such base $((p,a),(p',a'))$, take the four ordered pairs

$$
 \bigl(p/a,\ p'/(a'+j)\bigr),\qquad j=0,1,2,3,
 \tag{P20}
$$

and their reverses. Let $Q_j$ be the respective sums. Then $Q_0=P_0$,
and the coefficient signs are $+,-,-,+$.

All four families are disjoint as families of actual coalesced frequency
pairs. To see this, orient any image with the smaller prime first. This
recovers $p,p',a$. The residue of its second denominator modulo $5$
recovers $j\in\{0,1,2,3\}$, and subtracting $j$ recovers $a'$.
The uniqueness in (P9) excludes additional rational representations. The
margin in (P18) keeps every shifted denominator in $(M/2,M)$, so each
pair still has different prime cores, different frequencies and a singleton
determinant fibre.

For $C=p'a/p$ and every real $x\in[a',a'+3]$, the common-bin
condition gives

$$
 \left|\log\frac Cx\right|
 \le\left|\log\frac C{a'}\right|+\log(1+3/a')
 <\frac1{20T}+\frac6M\le\frac1{5T}.
 \tag{P21}
$$

Consequently all the shifted kernels are positive and stay strictly inside
their support. The next section determines the sign of their weighted
four-term combination.

## 6. Strict concavity, including the cusp

**Weighted concavity lemma.** Put $\alpha=\sigma-1$, and let $T\ge10$.
On any interval where $|\log(C/x)|\le1/(5T)$, define
$F(x)=x^\alpha\mathcal L_T(\log(C/x))$. Its distributional second
derivative satisfies

$$
 dF'(x)\le-\frac{T^2}{10}x^{\alpha-2}\,dx.
 \tag{P22}
$$

The statement includes any crossing of $x=C$. To prove it, write
$v=T|u|\le1/5$. Away from $u=0$, direct differentiation gives

$$
 \frac{\mathcal L_T''(u)}{T^2}
 =3\sin(3v/2)-\frac94(1-v)\cos(3v/2)
 \le\frac9{10}-\frac95\frac{191}{200}
 =-\frac{819}{1000}\le-\frac45.
 \tag{P23}
$$

Here $\sin(3v/2)\le3/10$ and
$\cos(3v/2)\ge1-(3/10)^2/2=191/200$. Also
$|\mathcal L_T|\le1$ and $|\mathcal L_T'|\le5T/2$. Thus the
ordinary second derivative of $F$ is

$$
 F''(x)=x^{\alpha-2}
 \{\alpha(\alpha-1)\mathcal L_T-(2\alpha-1)\mathcal L_T'
                                      +\mathcal L_T''\}
 \le x^{\alpha-2}
       \left(\frac{21}{16}+\frac{25T}{4}-\frac{4T^2}{5}\right)
 \le-\frac{T^2}{10}x^{\alpha-2}.
 \tag{P24}
$$

The last inequality holds for $T\ge10$: after division by $T^2$,
the upper bound is at most
$21/1600+5/8-4/5=-259/1600<-1/10$.

It remains to check the cusp, rather than assuming twice differentiability
there. The one-sided first derivatives are

$$
 F'(C-)=C^{\alpha-1}(\alpha+T),\qquad
 F'(C+)=C^{\alpha-1}(\alpha-T).
 \tag{P25}
$$

Therefore $dF'$ has the additional atom
$-2TC^{\alpha-1}\delta_C$, which is negative. There is no crossing of
the support endpoints $|u|=1/T$. Combining this atom with (P24) proves
(P22).

For the application, use the nonnegative continuous function
$W(y)=y$ on $[0,1]$, $W(y)=1$ on $[1,2]$,
$W(y)=3-y$ on $[2,3]$, and zero elsewhere. It has
$\int W=2$ and
$W''=\delta_0-\delta_1-\delta_2+\delta_3$. Integration by parts with
the signed measure $dF'$, followed by (P22), gives

$$
 \begin{aligned}
 F(a')-F(a'+1)-F(a'+2)+F(a'+3)
 &=\int W(x-a')\,dF'(x)\\
 &\le-\frac{T^2}{5}(a'+3)^{\alpha-2}<0.
 \end{aligned}
 \tag{P26}
$$

The possible cusp only strengthens this inequality. Multiplying by the
positive prefactor $8(pp')^{-\sigma}a^{\sigma-1}$ supplies the
contribution of one quartet and its reverse from (P20). Moreover,
$a'+3<M$ and
$(1+3/a')^{\sigma-1}\ge1/2$, so

$$
 (a'+3)^{\sigma-3}\ge\frac{a'^{\sigma-1}}{2M^2}.
 \tag{P27}
$$

The corresponding positive base kernel is at most one. Summing (P26) over
all canonical bases therefore proves the strict signed inequality

$$
 \boxed{\quad
 Q:=Q_0+Q_1+Q_2+Q_3
 \le-\frac{T^2}{10M^2}P_0<0.
 \quad}
 \tag{P28}
$$

Equivalently, the absolute contribution of the two negative families exceeds
the sum of the two positive families by at least
$T^2P_0/(10M^2)$. This is an estimate for disjoint terms of the actual
moment, with all original coefficient weights retained.

## 7. Why deleting this negative total cannot prove the target

Define its exact complement in the complete moment by
$R_Q=\mathscr F_T(P)-Q$. This is a sum of the remaining pair terms;
it need not be the squared norm of a separate polynomial. Positivity of
$\mathscr F_T(P)$ gives

$$
 R_Q\ge-Q
 \ge\frac{\mathcal N^2}{1484800}
       \frac{T^2M^{2\sigma-2}}{\log^2Y}
 \ge c_\sigma\mathcal N^2\frac{T^{2\sigma}}{\log^2Y},\qquad
 c_\sigma=\frac{(81/2)^{2\sigma-2}}{1484800}>0.
 \tag{P29}
$$

The last step uses the fixed choice $M=\lceil40T\rceil$, rather than
letting $M/T$ grow. In particular, for every fixed
$0\le\varepsilon_0<2\sigma$,

$$
 \frac{R_Q}{\mathcal N^2T^{\varepsilon_0}}\longrightarrow\infty
 \qquad(Y\longrightarrow\infty).
 \tag{P30}
$$

Although dropping a negative quantity gives the valid inequality
$\mathscr F_T(P)\le R_Q$, a target-sized upper bound for this particular
remainder is false. The negative quartet family must participate in any
successful compensation at that scale. This does not rule out the target
bound for the complete $\mathscr F_T(P)$, which includes $Q$.

The concavity argument is also local in sign and frequency: it uses a
positive first character value, the stated four residue classes, and (P21).
It provides no sign rule for every other pair in the polynomial.

## 8. Aggregate compensation in the complete moment

We now restrict to $1/4<\sigma<13/50$. Two companion results are needed;
their precise roles are stated here so that the local constructions above
remain separate from the analytic estimate.

First, [the analytic appendix, (A64)](ANALYTIC.md) proves, uniformly for finite
$M,K$, the bound for the entire real-line integral in (P5),

$$
 0\le\mathscr F_T(P)
 \ll_{\sigma,\varepsilon}\mathcal N^2T^{2\nu_\sigma+\varepsilon},
 \qquad
 \nu_\sigma=
 \frac{2860\sigma-169}{9578}
 +\frac{1261-2860\sigma}{3528},
 \qquad0<\nu_\sigma<\sigma,\quad2\nu_\sigma<1.
 \tag{P31}
$$

No hypothesis about zeros of a Dirichlet $L$-function is used in that
result. A bound only on $[T,2T]$ would not substitute for (P31).

Second, define $C_{\mathrm{dc}}$ by expanding (P3) in (P5) and retaining
exactly the ordered pairs with both different squarefree numerator cores
and different rational frequencies. If $E_J=\sum_\lambda c_\lambda^2$
is the fully combined frequency diagonal, and $C_{\mathrm{sc}}$ is the
different-frequency contribution with the same numerator core, the partition
is exactly
$\mathscr F_T(P)=E_J+C_{\mathrm{sc}}+C_{\mathrm{dc}}$.
[The arithmetic appendix, (R45)–(R47)](ARITHMETIC.md) proves

$$
 C_{\mathrm{dc}}=\mathscr F_T(P)
       +O_{\sigma,\varepsilon}(Y^{1-2\sigma}T^\varepsilon).
 \tag{P32}
$$

Thus all equal-frequency collisions are assigned to $E_J$, including
those arising from different numerator cores. They are excluded from
$C_{\mathrm{dc}}$. The unique prime frequencies in (P9) ensure that
$P_+$ and the quartet families belong to the remaining different-core,
different-frequency contribution without this ambiguity.

Since $Y=T^2$, the error in (P32) is
$\mathcal N^2T^{-1+\varepsilon}$. Combining (P31)–(P32) with the lower
bound for $P_+$ in (P14) proves

$$
 \boxed{\quad
 \frac{C_{\mathrm{dc}}-P_+}{P_+}
 =-1+O_{\sigma,\varepsilon}
       \left(T^{-2(\sigma-\nu_\sigma)+\varepsilon}\log^2Y\right).
 \quad}
 \tag{P33}
$$

For sufficiently small fixed $\varepsilon>0$, the error tends to zero
with a power saving. The rest of the actual different-core contribution
therefore cancels this positive family with a proved relative accuracy.
Equation (P33) does not identify that rest with the neighbouring family
$P_-$; additional positive and negative terms remain in it.

For the negative quartet family, positivity makes the direction of the
corresponding error explicit. Equations (P29) and (P31) give

$$
 \boxed{\quad
 0\le\frac{R_Q}{-Q}-1
 =\frac{\mathscr F_T(P)}{-Q}
 \ll_{\sigma,\varepsilon}
       T^{-2(\sigma-\nu_\sigma)+\varepsilon}\log^2Y.
 \quad}
 \tag{P34}
$$

Hence the complementary terms match $-Q$ from above to the same relative
power accuracy, even though that complement itself exceeds the target scale
by a growing factor. The two conclusions (P33) and (P34) concern different
specified subfamilies of one finite object; neither replaces the full signed
sum by its absolute values.

For example, at the exact value $\sigma=51/200$,

$$
 \nu_\sigma=\frac{7069361}{33791184},\qquad
 2(\sigma-\nu_\sigma)
 =\frac{38684773}{422389800}.
 \tag{P35}
$$

The relative power in (P33)–(P34) is thus approximately $0.09158548$ in
$T$. If the stronger target
$\mathscr F_T(P)\ll_{\sigma,\varepsilon}\mathcal N^2T^\varepsilon$
were established, the same divisions would instead give relative errors
$O(T^{-2\sigma+\varepsilon}\log^2Y)$, with power $0.51$ at this
value of $\sigma$. That stronger moment estimate remains open here.

## References and dependency scope

- M. A. Bennett, G. Martin, K. O'Bryant and A. Rechnitzer,
  *Explicit bounds for primes in arithmetic progressions*, Illinois Journal
  of Mathematics **62** (2018), 427–532. Theorem 1.2 and (1.10)–(1.12).
  [Author manuscript](https://arxiv.org/pdf/1802.00085v3).
- [Arithmetic structure and the exact partition](ARITHMETIC.md): used only
  for (P32) and its consequences.
- [Analytic moment estimates](ANALYTIC.md): used only for (P31) and its
  consequences. The local families, their signs, and the no-pruning result
  (P29)–(P30) do not require that estimate.
