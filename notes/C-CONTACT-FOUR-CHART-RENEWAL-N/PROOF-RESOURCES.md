# Resource conditions for literal depth retention and strict source reload

**Status: NON-CANONICAL / L1, candidate-T analytical results.**

This note compares the original supplied source with the four-chart source.
It proves exact accounts and necessary conditions for a proposed reload.
It supplies no reload word, attainable funding minimum, or autonomous
selection of the next chart. No numerical execution is used below.

## 1. Contact invariants and the two ready interfaces

Let $O=\mathbb Z[\rho]=\mathbb Z[j]$, where $\rho=j^2$ has order five. Put
$J=1+\rho$, $u=1-\rho$, and

$$
U_d=1-\rho^d,\qquad J_d=1+\rho^d
\quad(d\in\{1,2,3,4\}).
$$

The native contact is the identity when $a-b\notin2O$. Otherwise, writing
$a=s+t,b=s-t$, it sends $(a,b)$ to $(s+\rho t,s-\rho t)$.
Every contact preserves the sum, each labelled residue modulo $uO$, and

$$
Q(a)+Q(b),\qquad Q(z)=\frac12\operatorname{Tr}(z\bar z).
$$

Here $O/uO\simeq\mathbb F_5$, with $\rho\mapsto1$.
In the basis $(1,\rho,\rho^2,\rho^3)$,

$$
Q(z)=\frac{5\sum_i z_i^2-(\sum_i z_i)^2}{2}.
$$

This is a positive definite integer quadratic form. The contact also
preserves the stronger real-quadratic account $a\bar a+b\bar b$ before
taking its trace.

For the supplied gain $q=3$, the ready interfaces are

$$
E(n)=(4un,\;4(2-\rho)n,\;2J),\qquad
F_d(n)=(U_dn,\;(12-J_d)n,\;2J_d).
$$

Their accounts and sums are

$$
\begin{aligned}
Q(E(n))&=272n^2+12,
&S_E(n)&=4(3-2\rho)n+2J,\\
Q(F_d(n))&=260n^2+12,
&S_d(n)&=2(6-\rho^d)n+2J_d.
\end{aligned}
$$

Here $Q$ and $S$ of a tuple mean the sum of its slot accounts and the sum
of its values. Throughout, $n>0$ is odd,

$$
x=3n+1=2^v m,\qquad v\ge1,\qquad m>0\text{ odd}.
$$

The one-pass formulas apply when the declared cascade has sufficient
depth. The resource statements concern successful passes only.

## 2. The exact cost of fresh literal records

### 2.1. Original source

The original cascade starts with active value $uJx$. After its $v$
successful divisions its active value and fresh records are

$$
A_E=uJ^{v+1}m,\qquad
R_{E,s}=u^2J^s2^{v-s}m\quad(1\le s\le v).
$$

Put $\alpha=J\bar J$. Then

$$
\alpha^2-3\alpha+1=0,\qquad
u\bar u=4-\alpha,\qquad
(u^2J)\overline{(u^2J)}=5.
$$

The last identity follows from $(4-\alpha)^2\alpha=5$.
Define $c_r=Q(J^r)$. The two real conjugates of $\alpha$ give

$$
c_0=2,\qquad c_1=3,\qquad c_{r+2}=3c_{r+1}-c_r.
$$

Consequently

$$
Q(R_{E,s})=5c_{s-1}4^{v-s}m^2,
\qquad
Q(A_E)=(c_v+c_{v+1})m^2.
$$

The cascade conserves the initial active account $5x^2$, so the total
account of the new records is exactly

$$
\boxed{\mathcal R_E(v,m)
 =[5\cdot4^v-c_v-c_{v+1}]m^2.}
\tag{1}
$$

Their sum as ring elements, a different invariant from their total
account, is

$$
\boxed{r_E(v,m)=uJ(2^v-J^v)m.}
\tag{2}
$$

Both formulas also follow by telescoping the active value. More finely,
the sum of $R_{E,s}\overline{R_{E,s}}$ is
$(\alpha+1)(4^v-\alpha^v)m^2$.

For every actual positive odd $3n+1$ step,

$$
\mathcal R_E(v,m)\ge55,
\tag{3}
$$

with equality only at $n=m=1$, where $v=2$. Indeed for $v\ge2$ the
first two records alone contribute at least $40+15=55$, with equality
only if $v=2,m=1$. For $v=1$, admissibility implies $n\ge3,m\ge5$,
so (1) gives $\mathcal R_E=10m^2\ge250$.

### 2.2. Four-chart source

The four-chart prefix uses $C_{01}^d$ followed by $C_{02}^d$. Direct
substitution gives its active value $U_{2d}x$ and occupied leftovers

$$
b_1=2(3J_d-\rho^d)n,\qquad c_2=3U_d^2n+J_d^2.
$$

The predetermined powered cascade uses $e_s=2^sd\bmod5$ and writes

$$
R_{F,s}=U_{e_s}^{\,2}2^{v-s}m,\qquad
A_F=U_{d'}m,\qquad d'=2^{v+1}d\bmod5.
$$

These are literal contact identities: $U_eJ_e=U_{2e}$, and an admitted
$C^e$ on $(U_ey,0)$ yields $(U_{2e}y/2,U_e^2y/2)$.
Although $C^e$ uses $e$ native contacts, it performs one such division.
The pair remains enabled throughout those $e$ contacts.

Expanding the traces gives
$Q(U_e)=5$, $Q(J_e)=3$, and $Q(U_e^2)=15$. Therefore

$$
\boxed{\mathcal R_F(v,m)
 =15m^2\sum_{s=1}^v4^{v-s}
 =5(x^2-m^2),}
\tag{4}
$$

and

$$
\boxed{r_F(d,v,m)=U_{2d}x-U_{d'}m.}
\tag{5}
$$

The general supplied source
$(U_dn,(4q-J_d)n,2J_d)$ has account
$(32q^2-12q+8)n^2+12$, confirming the coefficient $260$ at $q=3$.
Its three labelled residues at $q=3$ are $(0,0,4)$ for every $n,d$.

For every positive odd step,

$$
\mathcal R_F(v,m)\ge75,
\tag{6}
$$

with equality only at $n=m=1,v=2$. That case gives $5(16-1)=75$.
If $n\ge3$, then $x\ge10$ and $m\le x/2$, so
$\mathcal R_F\ge15x^2/4\ge375$.

## 3. Necessary funding for a strict reload

Suppose the input contains a ready source at $n$, an additional account
$B$, and old archives. Require the output to contain the corresponding
ready source at $m$, all newly written depth records **literally in
separate retained slots**, the unchanged old archives, and any remaining
workspace. The remaining account is nonnegative. Thus

$$
\boxed{
\begin{aligned}
B&\ge\Delta_E=272(m^2-n^2)+\mathcal R_E(v,m),\\
B&\ge\Delta_F=260(m^2-n^2)+\mathcal R_F(v,m).
\end{aligned}}
\tag{7}
$$

In the second line the output chart is $d'$. Old archives cancel only
because they must remain unchanged. The occupied source leftovers must
still be included in whatever final workspace the reload produces.

For $3\to5$, the comparison is exact:

| Interface | Ready-source increase | New literal records | Necessary additional account |
|---|---:|---:|---:|
| Original $E$ | $4352$ | $250$ | $B\ge4602$ |
| Four-chart $F$ | $4160$ | $375$ | $B\ge4535$ |

These are lower bounds, not attainable minima. The original same-slot
reload $E(3)\to E(5)$ is separately impossible because a labelled residue
would have to change from $4\cdot3=2$ to $4\cdot5=0$ in $\mathbb F_5$;
no value of $B$ repairs that obstruction. The
four-chart source removes that particular input-dependent residue.

### Sum and workspace capacity

Let the initial auxiliary sum be $\Sigma$. Write $S_{\rm in}$ and
$S_{\rm out}$ for the two ready-source sums, and $r$ for (2) or (5).
If there are $M$ unrestricted final workspace slots, their sum and
account must be

$$
W=\Sigma+S_{\rm in}-S_{\rm out}-r,\qquad
Q_{\rm work}=B-\Delta.
$$

For $M\ge1$, the Cauchy inequality for the positive definite form $Q$
implies

$$
Q(W)\le M Q_{\rm work},\qquad
\boxed{B\ge\Delta+\frac{Q(W)}{M}.}
\tag{8}
$$

If $M=0$, one instead requires $W=0$ and $B=\Delta$ exactly.
Any designated ports required to remain zero are not unrestricted
workspace.

Both ready-source sums are even in $O$, whereas both record sums are
nonzero modulo $2O$: their final active value is odd and their initial
active value is even. Thus an even initial auxiliary sum cannot leave
all residual workspace zero. Sum, labelled residues, and the two real
embedding accounts impose conditions beyond (7). None implies that a
contact word reaching the specified state exists.

For example, at repeated original fixed-point steps $1\to1$, each batch
has account $55$ and sum

$$
r=u^2J(2+J),\qquad Q(r)=5Q(3+\rho)=85.
$$

After $N$ such batches with the same source restored, (8) becomes

$$
B\ge55N+\frac{Q(\Sigma-Nr)}{M}.
\tag{9}
$$

For a zero-sum initial bank this is
$B\ge55N+85N^2/M$, a stronger necessary condition at fixed workspace size.

## 4. Finite account cannot retain literal batches indefinitely

Assume $N$ successful steps, a fresh ready source after every step,
and literal retention of every new batch. Starting from $n_0$ and
ending at $n_N$, conservation yields

$$
\begin{aligned}
B&\ge272(n_N^2-n_0^2)+
       \sum_{i=0}^{N-1}\mathcal R_E(v_i,n_{i+1}),\\
B&\ge260(n_N^2-n_0^2)+
       \sum_{i=0}^{N-1}\mathcal R_F(v_i,n_{i+1}).
\end{aligned}
$$

Since $n_N\ge1$, (3) and (6) give the respective horizon bounds

$$
\boxed{55N\le B+272(n_0^2-1),\qquad
       75N\le B+260(n_0^2-1).}
\tag{10}
$$

Even repetition of the arithmetic fixed point consumes new positive
archive account under this literal-retention requirement. A finite
initial account therefore cannot support it indefinitely. A changed,
recycled, or compressed history representation would require a different
contract; it is not covered by the literal-batch premise.

## 5. Scaling the whole apparatus preserves a higher residue obstruction

For any integer $r\ge0$, suppose **every** initial slot belongs to $u^rO$.
Then every native contact word preserves each labelled slot modulo
$u^{r+1}O$.

To prove this, consider one enabled pair. For $r\ge1$, since $2$ is
coprime to $u$, it is invertible modulo $u^rO$. The conditions
$a-b\in u^rO$ and $a-b=2t$ imply $t\in u^rO$. The two slot changes are
$-ut$ and $ut$, both in $u^{r+1}O$. Refused contacts do nothing.
All slots remain in $u^rO$, so induction applies to the whole word.
For $r=0$, $t\in O$ already gives the same conclusion directly.

In particular, multiplying the complete original apparatus and every
auxiliary by $u^r$ does not repair its same-slot reload obstruction.
The scaled second ready port can change from
$u^r4(2-\rho)n$ to $u^r4(2-\rho)m$ only if $n=m\bmod5$.
For $r\ge1$, an auxiliary outside the common ideal $u^rO$ is necessary
to evade this higher-layer argument, but its presence is not sufficient
for a reload. For $r=0$, the underlying labelled residue modulo $uO$
is an invariant on the whole allowed ring.

## 6. A finite affine initial loader cannot fund universal strict readiness

There is a separate obstruction even if new records need not be retained.
Suppose an apparatus has a fixed finite number of initial slots

$$
z_\ell(n)=a_\ell n+b_\ell,\qquad a_\ell,b_\ell\in O,
$$

with coefficients independent of $n$. Its complete initial account is
a fixed quadratic polynomial $P(n)=p_2n^2+p_1n+p_0$, and in particular
$P(n)=O(n^2)$. Suppose contacts, with no later supplied account, must
leave a strict ready $E(n_i)$ or $F_{d_i}(n_i)$ after each successive
odd Collatz step, for every positive odd input.

Take $n_0=2^k-1$, $k\ge2$. The first $k-1$ steps have valuation one,
and exact induction gives

$$
n_i=3^i2^{k-i}-1\quad(0\le i\le k-1).
$$

Indeed, for $i\le k-2$,
$3n_i+1=2(3^{i+1}2^{k-i-1}-1)$ with an odd expression in parentheses.
Thus $n_{k-1}=2\cdot3^{k-1}-1$, and

$$
\frac{n_{k-1}}{n_0}\longrightarrow\infty.
$$

Strict readiness at that finite prefix endpoint requires

$$
P(2^k-1)\ge\gamma(2\cdot3^{k-1}-1)^2+12,
\qquad \gamma=272\text{ or }260.
$$

Dividing by $(2^k-1)^2$ makes the left side tend to the finite
coefficient $p_2$ and the right side diverge. This is a contradiction.
Every step used in this argument has depth one; increasing a bounded
depth cap does not resolve it.

The theorem does not assume an infinite growing Collatz orbit or any
failure of the Collatz conjecture. It uses finite, explicit prefixes with
different starting inputs. It applies regardless of program length or
chart control, because conserved account alone suffices. Finitely many
affine initial charts give the same result by taking one common quadratic
upper bound. It excludes the
stated fixed finite affine loader and strict-ready interfaces. A finite
input family with explicitly supplied funding, a different representation,
or a separately declared loading law must be assessed under its own
resource and reachability conditions.
