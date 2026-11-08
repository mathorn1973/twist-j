<!-- SPDX-License-Identifier: Apache-2.0 -->

# Paired native phase and bounded endpoint work

**NON-CANONICAL / L1 / conditional candidate-T.** The conclusions apply to
the specified native trajectories, integer lift, clock readings and work
classes. The source is Public Canon v109 at public `main`
`650029c20408f1dd665983d72225d0d195fd030e`. The native law, occupied-sheet
rule and chart are pinned to `canon/CANON.md` lines 7240–7253 and
17526–17642. The dimensionless tick is `METRO-TICK` in `canon/REGISTRY.tsv`
line 189 and `canon/CANON.md` lines 28566–28570.

## Native trajectory and integer lift

Write the checkpoint as $x=(p_1,p_2,p_3,p_4,q,r)\in\mathbb F_5^6$ and its
trace as $z=p_1+p_2+p_3+p_4+q+r$. The initial counter is zero and the initial
checkpoint is any point of $X_1\cup X_4$, where $X_z$ is the complete sheet
of trace $z$. The unchanged selector uses the fixed Thue–Morse bit
$\theta_n=s_2(n)\bmod 2$ at counter $n$, with $s_2$ the binary digit sum.
It advances the counter by one on every native tick. Let $h=0$ on $X_1$ and
$h=1$ on $X_4$. Set

$$
\begin{aligned}
A_p&=p_1+p_3,& B_p&=p_2+p_4,& C_p&=p_1-p_3-2,& D_p&=p_2-p_4-1,\\
v&=(A_p,B_p,(-1)^h C_p,(-1)^h D_p).
\end{aligned}
$$

The chart $(h,v,r)$ determines the checkpoint. In fact $h$ determines $z$,
$v$ determines $A_p,B_p,C_p,D_p$ when $h$ is known, and division by two
recovers the pistons from their sums and differences. Then
$q=z-A_p-B_p-r$ in $\mathbb F_5$. By WR-4 the native tick acts by

$$
h_{n+1}=1-\theta_n,\qquad v_{n+1}=-v_n,\qquad
r_{n+1}=-r_n+c_n\pmod 5,\qquad c_n=h_n\mathbin{\mathrm{xor}}\theta_n.
$$

For $n\ge1$ the occupied sheet therefore has $h_n=1-\theta_{n-1}$.
Choose any integer $\widetilde r_0$ reducing to $r_0$ and define the supplied
lift $\widetilde r_{n+1}=-\widetilde r_n+c_n$ over the integers, with
$c_n$ represented by $0$ or $1$. Its reduction is native $r_n$ at every
tick. Changing $\widetilde r_0$ by $5m$ changes $\widetilde r_n$ by
$(-1)^n5m$, so displacements over even lengths are independent of the
initial representative.

## Pairing the native ticks

For $k\ge1$ put $e_k=[\theta_{k-1}\ne\theta_k]$, using brackets for the
integer indicator. The identities $\theta_{2k}=\theta_k$ and
$\theta_{2k+1}=1-\theta_k$ follow by appending a binary digit. They give
the following two pair laws on the occupied trajectory.

| Starting counter | Bits used | Initial $h$ | Pair $(c_n,c_{n+1})$ | Final $h$ | $\Delta\widetilde r$ |
| --- | --- | --- | --- | --- | ---: |
| $2k$ | $\theta_k,1-\theta_k$ | $\theta_{k-1}$ | $(e_k,0)$ | $\theta_k$ | $-e_k$ |
| $2k-1$ | $1-\theta_{k-1},\theta_k$ | $1-\theta_{k-1}$ | $(0,e_k)$ | $1-\theta_k$ | $+e_k$ |

Indeed the first bit sets the intermediate $h$ to its complement. Substituting
it into the second XOR gives the displayed two $c$ values. The two sign
changes cancel on $v$, and the lifted recurrence adds $-c_n+c_{n+1}$ to
$\widetilde r$. In either row $h$ toggles exactly when $e_k=1$.

At each checkpoint the Chinese remainder theorem defines one hand
$\ell\in\mathbb Z/10\mathbb Z$ by $\ell=r\pmod 5$ and $\ell=h\pmod 2$.
On the even pair its change is $-e_k\pmod{10}$ and on the odd pair it is
$+e_k\pmod{10}$. The unique nearest signed representative of each paired
change is $0$ or the displayed $\pm1$, for both the $r$ residue modulo five
and the hand modulo ten. Thus the accumulated nearest pair increments
coincide with $\Delta\widetilde r$ from the supplied integer recurrence.
This comparison concerns pairs of ticks. Endpoint residues alone admit
integer displacements differing by a multiple of the modulus.

## Exact finite returns

Use the finite clock reading $n\bmod 5$ from `METRO-TICK` and retain also
the previous and current Thue–Morse bits. Along the odd pairs from $n=1$,
the three consecutive ten-tick windows have the following parent words.
Each word contains the six endpoints of five comparisons.

| Native window | Parent word | Number of changes | $\Delta\widetilde r$ |
| --- | --- | ---: | ---: |
| $1\to11$ | $\theta_0\cdots\theta_5=011010$ | $4$ | $+4$ |
| $11\to21$ | $\theta_5\cdots\theta_{10}=001100$ | $2$ | $+2$ |
| $21\to31$ | $\theta_{10}\cdots\theta_{15}=010110$ | $4$ | $+4$ |

The endpoint parent bits of all three words are zero, so $h=1$ at
$n=1,11,21,31$. The bits
$(\theta_{n-1},\theta_n)$ are $(0,1)$ at all four cuts, and $n\bmod5=1$.
The pair law fixes $v$, hence all four pistons and the trace agree at
those cuts on every admitted trajectory. The first two displacements
are different modulo five, giving different marked fibre phases
$j^4$ and $j^2$ for the character $r\mapsto j^r$.

For the particular preparation $x_0=(1,3,4,2,1,0)$ on $X_1$, $v=0$.
The chart inverse gives the same piston tuple $(1,3,4,2)$ for either
trace when $v=0$. At $n=1,11,21,31$ the reference pair $(q,r)$ is,
respectively, $(4,0),(0,4),(3,1),(4,0)$. Each native tick fixes the
pistons. Every
per-tick difference of a piston-only energy is zero, so the first two
windows have identical piston work records and identical tick counts.
A rule from those records and the common finite boundary clock readings
to the marked fibre phase would give the same value on both windows.

The three odd windows sum to $+10$ in the lift. The even lane from $n=2$
uses the same fifteen $e_k$ with the opposite sign and sums to $-10$ at
$n=32$. Its $h$ agrees at both cuts, since the common parent word starts
and ends with zero. The even lane has $n\bmod5=2$ and previous/current bits
$(1,1)$ at both cuts. In either lane the trace and $v$ return, and $\pm10$
reduces to zero modulo five. The chart inverse then restores the entire
checkpoint, including $q$ and $r$, on every admitted trajectory. The full
counter advances by thirty. The nonzero integers $\pm10$ record the
accumulated lift, while the modular phase on each thirty-tick return is
the identity.

## Exact imbalance of paired flips and ticks

Let $v_2(k)$ be the exponent of two in $k>0$. Going from $k-1$ to $k$
turns $v_2(k)$ trailing ones into zeroes and turns the next zero into a
one. The change in binary digit sum is $1-v_2(k)$. Thus

$$e_k=[v_2(k)\text{ is even}].$$

Define $A(M)=\sum_{k=1}^{M}e_k$ for $M\ge0$ with $A(0)=0$. For $k\ge0$,
$e_{4k+1}=e_{4k+3}=1$ and $e_{4k+2}=0$. For $k\ge1$, $e_{4k}=e_k$.
Summing complete blocks and then the trailing $r$ terms gives, for
$r\in\{0,1,2,3\}$,

$$
A(4m+r)=2m+A(m)+[r\ge1]+[r\ge3].
$$

For $D(M)=3A(M)-2M$ the same recursion is

$$
D(4m+r)=D(m)+\begin{cases}
0,&r=0\text{ or }3,\\
1,&r=1,\\
-1,&r=2.
\end{cases}
$$

Iterating to $D(0)=0$ proves the exact identity

$$
D(M)=N_1(M\text{ in base }4)-N_2(M\text{ in base }4),
$$

where $N_i$ counts digits equal to $i$. Leading zeroes have no effect.
On $0\le M<4^s$ the sharp minimum and maximum are $-s,+s$. They occur at
the words of $s$ digits all equal to $2$ or all equal to $1$, respectively,
which represent $2(4^s-1)/3$ and $(4^s-1)/3$. Every integer between the
extrema occurs, by using the required number of $1$ or $2$ digits and
filling the remaining places with zeroes. In particular $D(M)=o(M)$ and
$A(M)/M\to2/3$. For a linear combination of flip count and pair count,
the primitive integer combination that cancels the linear term is
$3A-2M$, up to an overall sign. Its residual is unbounded in both
directions.

## Bounded endpoint work and finite capacity

Fix an admitted trajectory and the even cuts from $n=2$. After $M$ pairs
the elapsed tick count is $2M$ and the signed lift displacement is
$-A(M)$. Let $E(n,x)$ be a real-valued endpoint potential bounded on
this sequence of cuts. Suppose constants $a,b\in\mathbb R$ satisfy

$$
E(2+2M,x_{2+2M})-E(2,x_2)=a(2M)+b(-A(M))\qquad(M\ge0).
$$

The right side equals $(2a-2b/3)M-(b/3)D(M)$. Boundedness and division by
$M$ force $a=b/3$. The sharp extremes of $D$ then force $b=0$, hence
$a=0$. For any nonzero coefficient of the lift, subtracting any linear
drift leaves either a nonzero linear term or the same unbounded digit
residual. The bound here concerns the values of $E$ along the actual
even cuts. A finite checkpoint reading with a fixed real potential has
that bound automatically, whereas a potential using the full counter
can be unbounded.

For a separate, prescribed integer account add $D(M)$ to an initial bank
$B_0$, so $B_M=B_0+3A(M)-2M$. The bank changes by $3e_{M+1}-2$ between
successive even cuts. Requiring $0\le B_M\le C$ through $M=4^s-1$
is equivalent to $B_0\ge s$ and $B_0+s\le C$ by the sharp extrema. The
minimum capacity is $2s$, with the unique ready value $B_0=s$ at that
capacity. These bounds are on the specified balance at even cuts. The
bank account and the integer lift are supplied arithmetic records.
Physical action normalization, an electromagnetic phase dictionary and
an inference of the fine-structure constant remain open.
