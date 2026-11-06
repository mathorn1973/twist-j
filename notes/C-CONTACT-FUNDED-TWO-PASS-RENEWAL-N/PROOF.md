# Two funded source renewals on one exact Collatz cylinder

**Status: NON-CANONICAL / L1, candidate-T analytical construction.**

This construction supplies four explicit donor ports and uses only native
contacts to renew the complete three-port source after each of two odd
Collatz steps. All old and newly written depth records remain literally
present. The loading interface is an explicit affine function of the
input parameter, compiled for the fixed valuation prefix $(1,4)$.
No scientific execution is assumed in this proof.

## 1. Native law and an integral overwrite lemma

Work in $O=\mathbb Z[\rho]$, where
$1+\rho+\rho^2+\rho^3+\rho^4=0$. For a nonzero residue $e$ modulo five,
represented in $\{1,2,3,4\}$, put

$$
U_e=1-\rho^e,\qquad J_e=1+\rho^e.
$$

The native contact $C$ fixes $(a,b)$ if $a-b\notin2O$. Otherwise,
writing $a=s+t,b=s-t$, it sends the pair to
$(s+\rho t,s-\rho t)$. An enabled pair remains enabled, so $C^e$ is
exactly $e$ repetitions of this primitive and acts by

$$
C^e(a,b)=
\left(\frac{J_ea+U_eb}{2},\frac{U_ea+J_eb}{2}\right).
\tag{1}
$$

Every contact preserves the pair sum, the positive definite account

$$
Q(z)=\frac12\operatorname{Tr}(z\bar z)
    =\frac{5\sum_{i=0}^3z_i^2-(\sum_{i=0}^3z_i)^2}{2},
\qquad z=\sum_{i=0}^3z_i\rho^i,
\tag{2}
$$

and each labelled residue $\epsilon(z)=z|_{\rho=1}\in\mathbb F_5$.
It also preserves $a\bar a+b\bar b$ before taking the trace.
Indeed $a\bar a+b\bar b=2(s\bar s+t\bar t)$, and multiplying $t$
by $\rho$ does not change $t\bar t$. Each slot change is a multiple
of $\rho-1$, which proves the labelled residue assertion.
The complete pair map satisfies $C^5=\mathrm{id}$.

**Overwrite lemma.** Suppose $y-a\in U_eO$, and supply the donor

$$
D_e(a,y)=a+\frac{2(y-a)}{U_e}
        =\frac{2y-J_ea}{U_e}\in O.
\tag{3}
$$

Then one powered contact gives

$$
C^e(a,D_e(a,y))=(y,\ a+D_e(a,y)-y).
\tag{4}
$$

Indeed the initial difference is $-2(y-a)/U_e$, so the pair is enabled,
and substitution in (1) proves the first output. Sum conservation proves
the second. Since $U_e$ is an associate of $U_1$, the divisibility premise
is equivalent to $\epsilon(y)=\epsilon(a)$.
Indeed $U_e/U_1=1+\rho+\cdots+\rho^{e-1}$ is integral and has norm
$N(U_e)/N(U_1)=5/5=1$, so it is a unit.

This lemma does not prepare its donor. A donor chosen from an unknown
answer would be an answer-dependent loading assumption. The construction
below instead specifies all four donors as fixed integral affine
functions of one supplied parameter, before any contact is applied.

## 2. The exact arithmetic family and ready charts

Let $h\ge0$ be an integer and define

$$
n_0=64h+3,\qquad n_1=96h+5,\qquad n_2=18h+1.
\tag{5}
$$

They are positive odd integers, and

$$
3n_0+1=2n_1,\qquad 3n_1+1=16n_2.
\tag{6}
$$

Thus the exact odd-step valuations are $v_0=1,v_1=4$, and
$T(n_0)=n_1$, $T(n_1)=n_2$ for
$T(n)=\operatorname{oddpart}(3n+1)$. No runtime valuation test is used
to select the word below.

The ready source in chart $d\in\{1,2,3,4\}$ is

$$
F_d(n)=(U_dn,\ (12-J_d)n,\ 2J_d).
\tag{7}
$$

Its three labelled residues are $(0,0,4)$, and
$Q(F_d(n))=260n^2+12$ for every chart.
Here $Q(U_d)=5$, $Q(12-J_d)=255$, and $Q(2J_d)=12$ by expansion
of the traces.
Two powered prefix contacts $C_{01}^d,C_{02}^d$ produce active value
$U_{2d}(3n+1)$ and the occupied leftovers

$$
b_d(n)=2(3J_d-\rho^d)n,\qquad
c_d(n)=3U_d^2n+J_d^2.
\tag{8}
$$

For a declared depth cap $12$, the ensuing thirteen fresh-zero contacts
have exponents $[2^sd]_5$, $s=1,\ldots,13$, where brackets mean the
representative in $\{1,2,3,4\}$. Because
$U_eJ_e=U_{2e}$, an accepted powered contact maps

$$
(U_ey,0)\longmapsto(U_{2e}y/2,\ U_e^2y/2).
\tag{9}
$$

Each such contact removes one factor of two. Multiplication by every
$U_e$ preserves powers-of-two divisibility, since it is a unit modulo
two: the identity $\prod_{e=1}^4 U_e=5$ proves invertibility modulo two,
and exact division by two gives induction for higher powers.
When the active slot becomes odd, every later fresh-zero contact
is refused. Therefore a successful depth-$v$ pass ends with active
$U_{d'}m$, where $d'=[2^{v+1}d]_5$, and records

$$
U_{[2^sd]_5}^{\,2}2^{v-s}m,\quad 1\le s\le v.
\tag{10}
$$

This is a fixed word on each supplied chart, with its entire unused
zero suffix retained.

## 3. Four explicit affine donor ports

First use chart $d=1$. The first pass ends in chart $4$, and the second
in chart $3$. The following table specifies each donor $B_i(h)=P_ih+Q_i$
in the basis $(1,\rho,\rho^2,\rho^3)$.

| Donor | $P_i$ | $Q_i$ |
|---|---|---|
| $B_1$ | $(1600,832,448,320)$ | $(84,46,26,18)$ |
| $B_2$ | $(-192,0,192,0)$ | $(-6,0,6,-4)$ |
| $B_3$ | $(648,516,204,-108)$ | $(34,26,10,-6)$ |
| $B_4$ | $(-288,0,0,288)$ | $(-12,0,0,16)$ |

All coefficients are fixed integers. The initial donor residues are
$(4,1,4,4)$, independently of $h$.

These polynomials obey the following exact integral identities:

$$
\begin{aligned}
B_1&=D_1\bigl(b_1(n_0),(12-J_4)n_1\bigr),\\
B_2&=D_1\bigl(c_1(n_0),2J_4\bigr),\\
B_3&=D_4\bigl(b_4(n_1),(12-J_3)n_2\bigr),\\
B_4&=D_4\bigl(c_4(n_1),2J_3\bigr).
\end{aligned}
\tag{11}
$$

For example, reducing with the cyclotomic relation gives

$$
\begin{aligned}
B_1={}&(25+13\rho+7\rho^2+5\rho^3)n_0
          +(9+7\rho+5\rho^2+3\rho^3),\\
B_2={}&-3U_2n_0+(3-3\rho^2-4\rho^3),\\
B_4={}&-3U_3n_1+(3+\rho^3).
\end{aligned}
$$

For the third donor, putting $z=\rho^4$ gives

$$
B_3=(132h+8)-(516h+26)z
                  -(624h+32)z^2-(312h+16)z^3.
$$

Multiplying this expression by $1-z$ gives
$2(11-z^2)n_2-2(3+5z+2z^2)n_1$, the numerator in (3).
The other three identities follow by the same multiplication, or by
the displayed simplified expressions. This proves (11) for all $h$,
without a finite table of input answers.

Consequently, after the first pass, $C_{1,B_1}$ and $C_{2,B_2}$ renew
the missing two ports of $F_4(n_1)$. After the second pass,
$C_{1,B_3}^4$ and $C_{2,B_4}^4$ renew those of $F_3(n_2)$.
The active port already has the required value and is not touched by
either renewal pair.

## 4. All four charts, complete slot layout, and the native word

Let $\sigma_d$ be the ring automorphism $\rho\mapsto\rho^d$.
It preserves $2O$, hence the contact guard, and

$$
\sigma_d C^e=C^{[de]_5}\sigma_d
\tag{12}
$$

on every pair, enabled or refused. This transports the base construction
to every supplied initial chart. It is an algebraic comparison of
different loaded states and words, not a physical Galois gate.

Use the following thirty-five labelled slots.

| Slots | Complete initial contents |
|---|---|
| $0,1,2$ | $F_d(n_0)$ |
| $3,\ldots,15$ | Thirteen zeros for the first pass |
| $16,\ldots,28$ | Thirteen zeros for the second pass |
| $29,30,31,32$ | $\sigma_d B_1(h),\ldots,\sigma_d B_4(h)$ |
| $33,34$ | Arbitrary supplied old archives $\omega_0,\omega_1\in O$ |

The old archives may be fixed commonly over the input family. They are
not acted on at any point. Thus there are thirty-three core slots and
two untouched old archive slots.

Define the chronological word

$$
W_e^{[a]}=
C_{01}^e\,C_{02}^e\,
\prod_{s=1}^{13}C_{0,a+s-1}^{[2^se]_5},
\tag{13}
$$

where factors are applied from left to right. Put $\delta=[4d]_5$.
The full chronological program is

$$
\boxed{
W_d^{[3]}\,
C_{1,29}^{d}C_{2,30}^{d}\,
W_\delta^{[16]}\,
C_{1,31}^{\delta}C_{2,32}^{\delta}.}
\tag{14}
$$

Every exponent means literal repetition of the same native contact.
All edges and exponents are predetermined from the supplied chart $d$.
There is no runtime edge selection, answer lookup, or discarded bank.

The four $W_d$ lengths in primitive contacts are respectively
$34,38,37,41$. They follow from
$|W_d|=2d+30+[2d]_5$. Since $\delta=5-d$,
$|W_d|+|W_\delta|=75$, while the renewals use
$2d+2\delta=10$ additional contacts. Hence every complete word has
exactly **85 native contacts**, grouped into 34 powered-contact factors,
independently of $h$ and $d$.

After the first renewal the actual source is exactly $F_\delta(n_1)$.
After the second renewal it is exactly $F_{[3d]_5}(n_2)$. These are
literal port equalities, not normalized mathematical readouts.

## 5. Complete final state, including the spent donors

The first archive has the single nonzero value

$$
\text{slot }3=U_{[2d]_5}^{\,2}n_1;
\qquad \text{slots }4,\ldots,15=0.
\tag{15}
$$

The second archive is

$$
\begin{aligned}
\text{slot }16&=8U_{[3d]_5}^{\,2}n_2,&
\text{slot }17&=4U_d^2n_2,\\
\text{slot }18&=2U_{[2d]_5}^{\,2}n_2,&
\text{slot }19&=U_{[4d]_5}^{\,2}n_2,
\end{aligned}
\tag{16}
$$

with slots $20,\ldots,28$ zero. Neither renewal touches any of these
records, and the second pass does not touch the first archive.

For base chart one, write the four final donor values as
$L_i(h)=\widetilde P_i h+\widetilde Q_i$:

| Final donor | $\widetilde P_i$ | $\widetilde Q_i$ |
|---|---|---|
| $L_1$ | $(832,992,352,224)$ | $(42,53,21,13)$ |
| $L_2$ | $(0,-384,384,0)$ | $(4,-14,18,-2)$ |
| $L_3$ | $(642,132,-180,-474)$ | $(33,6,-10,-25)$ |
| $L_4$ | $(576,576,576,1152)$ | $(30,28,28,58)$ |

Each row follows from the exact second output $a+B_i-y$ in (4).
For initial chart $d$, slots $29,\ldots,32$ end at
$\sigma_dL_1(h),\ldots,\sigma_dL_4(h)$.
Slots $33,34$ remain exactly $\omega_0,\omega_1$.
Together with the final source and archives, this specifies every slot.

The inverse reverses the thirty-four powered-contact factors and
replaces each $C^e$ by $C^{5-e}$ on the same pair. Its primitive length
is $5\cdot34-85=85$ contacts. It restores all thirty-five slots,
including both archives and every donor. This is a complete-state
inverse, not an erasure of records while keeping the forward answer.

## 6. Exact funding and its disposition

Trace invariance makes every account below independent of $d$.
Direct expansion in (2) gives the supplied four-port bank account

$$
\boxed{B(h)=5\,422\,160h^2+555\,480h+14\,368.}
\tag{17}
$$

The final donor account is

$$
\boxed{B_{\rm final}(h)=5\,851\,540h^2+585\,660h+14\,798.}
\tag{18}
$$

The full accounting, excluding the unchanged old archives, is:

| Part | Exact account |
|---|---|
| Initial ready source | $1\,064\,960h^2+99\,840h+2352$ |
| Initial supplied bank | $5\,422\,160h^2+555\,480h+14\,368$ |
| Initial total | $6\,487\,120h^2+655\,320h+16\,720$ |
| Final ready source | $84\,240h^2+9360h+272$ |
| All new records | $551\,340h^2+60\,300h+1650$ |
| Final donor bank | $5\,851\,540h^2+585\,660h+14\,798$ |

The last three rows sum to the initial total. The record row follows
independently from $Q(U_e^2)=15$:

$$
Q(\text{new records})=15n_1^2+1275n_2^2.
\tag{19}
$$

For a second check on the donor polynomial, the individual initial
accounts are

$$
\begin{aligned}
Q(B_1)&=3\,768\,320h^2+393\,600h+10\,292,\\
Q(B_2)&=184\,320h^2+11\,520h+212,\\
Q(B_3)&=1\,054\,800h^2+110\,040h+2872,\\
Q(B_4)&=414\,720h^2+40\,320h+992.
\end{aligned}
$$

The final pair accounts are

$$
\begin{aligned}
Q(L_1)+Q(L_2)&=2\,483\,200h^2+240\,960h+5969,\\
Q(L_3)+Q(L_4)&=3\,368\,340h^2+344\,700h+8829.
\end{aligned}
$$

At $h=0$, the arithmetic is $3\to5\to1$. The first donor pair changes
from account $10\,504$ to $5969$, paying exactly $4535$ into the
source increase and first records. The second pair changes from $3864$
to $8829$, receiving $4965$ from that step's source decrease after its
records are retained. The complete account is

$$
16\,720=272+1650+14\,798.
$$

Adding $Q(\omega_0)+Q(\omega_1)$ to both sides accounts for the two old
archives. Sum, full embedding accounts, and labelled residues are also
preserved, since every displayed transformation is an actual contact.
No claim of a minimal bank or a physical energy calibration is made.

## 7. Proof-only corollary: a finite valuation-prefix compiler

The same construction applies to every preset finite positive valuation
word $\nu=(v_1,\ldots,v_H)$, with $H\ge1$. This is an analytical
corollary; it does not enlarge a finite numerical audit.

Put $S_0=0$, $S_i=\sum_{j=1}^i v_j$, and $S=S_H$.
There is one odd residue $r$ modulo $2^{S+1}$ whose first $H$ odd-step
valuations are exactly $\nu$. Choose its positive representative
$1\le r<2^{S+1}$. Then the whole cylinder

$$
n_0(h)=r+2^{S+1}h,\qquad h\ge0,
$$

has that same valuation prefix, and its successive odd values are

$$
n_i(h)=2^{S+1-S_i}3^i h+\beta_i,
\qquad
\beta_0=r,\quad
\beta_i=\frac{3\beta_{i-1}+1}{2^{v_i}}\text{ positive odd}.
\tag{20}
$$

For completeness, prove the cylinder statement by induction. After
an $i$-step prefix there is one initial odd class modulo $2^{S_i+1}$.
Writing its positive representative as $r_i$, the current odd value
over that class is $b+2\cdot3^i t$, where $b=T^i(r_i)$ is odd.
The requirement that its next valuation be $v$ is

$$
\frac{3b+1}{2}+3^{i+1}t
 \equiv2^{v-1}\pmod{2^v}.
$$

The slope is odd, so this selects exactly one $t$ modulo $2^v$.
It therefore extends the initial class uniquely modulo
$2^{S_i+v+1}$, and imposes the exact valuation, not merely a lower
bound. Starting from the single odd class modulo two proves the
claim. Substituting the final initial class through the known affine
branches gives (20).

Fix an initial chart $d_0$, and precompute

$$
d_i=[2^{S_i+i}d_0]_5.
$$

For each stage $i=1,\ldots,H$, supply two donor polynomials

$$
\begin{aligned}
A_i(h)&=D_{d_{i-1}}\!
 \left(b_{d_{i-1}}(n_{i-1}(h)),
       (12-J_{d_i})n_i(h)\right),\\
G_i(h)&=D_{d_{i-1}}\!
 \left(c_{d_{i-1}}(n_{i-1}(h)),2J_{d_i}\right).
\end{aligned}
\tag{21}
$$

These are integral affine polynomials in $O[h]$. To see the coefficient
integrality, both the old and desired second-source values have all
coefficients in $U_1O$. For the third-source difference, the linear
coefficient is a multiple of $U_{d_{i-1}}^2$, and the constant
coefficient has residue $4-4=0$. Hence each difference in (21) is
coefficientwise divisible by $U_{d_{i-1}}$, an associate of $U_1$.
Formula (3) then lies in $O[h]$, without input-dependent division.

Choose finite depth caps $D_i\ge v_i$, supply $D_i+1$ distinct fresh
zero ports per stage, and apply its chart word followed by the two
overwrite contacts of power $d_{i-1}$. The source becomes exactly
$F_{d_i}(n_i)$ after each renewal. All previous record ports are
excluded from subsequent edges. Each used donor ends at the explicit
value $a+D-y$ from (4); no occupied port is suppressed.

The entire bank is supplied once at the start. Its exact finite account
is

$$
B_\nu(h)=\sum_{i=1}^H\bigl(Q(A_i(h))+Q(G_i(h))\bigr),
$$

a quadratic polynomial in $h$. The construction uses

$$
3+\sum_{i=1}^H(D_i+1)+2H
\tag{22}
$$

core slots, in addition to any untouched old archives, and one
predetermined finite native word for the supplied $\nu,d_0$.
The example above is $\nu=(1,4)$, $r=3$, $D_1=D_2=12$.

The corollary compiles a supplied finite itinerary. It does not determine
that itinerary for an unrestricted raw input or prepare its affine
donor bank from a raw scalar without additional resources. Different
itineraries or longer horizons generally require different initial
bank coefficients, record ports, and native words.

## 8. What this construction establishes

The word really restores both missing source ports after each pass,
keeps the active output, and retains every new and old archive.
It proves a sufficient contact construction for the declared two-step
family and explicitly supplied bank, not merely an invariant lower bound.

The input premise is the complete affine loader in the slot table.
It does not follow from supplying one raw scalar slot $n_0$. The four
donor formulas contain no runtime $T$, valuation, or lookup, but their
coefficients were designed for the known finite prefix $(1,4)$.
Thus the result is a compiled exact branch, with unbounded parameter
$h$ and input-dependent account $B(h)$; it is not a universal source
loader or one common finite account over all inputs.

The final donor values differ from their initial preparation. Their
renewal for further steps has not been proved. The result supplies
neither an autonomous selector for an unknown next valuation/chart,
nor an indefinitely reusable bank, unbounded history capacity,
gain selection, a native-U identification, an occurrence law, or
Collatz convergence. All of those would require their own complete
interfaces and resource arguments.
