# The exact minimum temporal context of the prescribed native lift

**NON-CANONICAL, L1 theorem proposal. Proof-only addendum, 13 October 2026.**

This addendum sharpens the predecessor's upper bound of 24 externally supplied
contexts to an exact minimum of five. It uses the same checkpoint domain, native
generators, active action, and prescribed first-entry lift. It introduces no
gate. It does not change a Canon statement or an owner's status, and its new
conclusions are not covered by the predecessor's sealed formal run.

The immutable mathematical sources are the predecessor's
[NATIVE_PROOF.md](https://github.com/mathorn1973/twist-j/blob/59711070f75b56b2441b951dd9cd77bb1dfc5da2/probes/P-BETA-PENTAD-NATIVE-EXTENSION-1/NATIVE_PROOF.md)
for the prescribed lift and
[GEOMETRY_PROOF.md](https://github.com/mathorn1973/twist-j/blob/59711070f75b56b2441b951dd9cd77bb1dfc5da2/probes/P-BETA-PENTAD-NATIVE-EXTENSION-1/GEOMETRY_PROOF.md)
for the form, coordinates, and prescribed operation. The nine-step entry bound
is inherited from the predecessor's use of `TM-SHEET-SYNCHRONIZING-GRAPH`;
it is not a new synchronization claim of this addendum.

## 1. Statement and exact minimization problem

Let $X=\mathbb F_5^6$. Write the prescribed lift as

$$
\widehat\Phi_C(n,x)=(n,F_{C,n}(x)).
$$

We factor the **checkpoint component** $F_{C,n}(x)$. The unchanged time
coordinate is carried separately. The decoder is not given that time as an
additional input when computing the checkpoint component.

For a family $G$, an admissible context is a finite-valued function
$\kappa:\mathbb N_0\to\Sigma$ and a single decoder

$$
D:G\times X\times\Sigma\longrightarrow X,
\qquad D(C,x,\kappa(n))=F_{C,n}(x)
\tag{1}
$$

for every $n$, every $x\in X$, and every $C\in G$. The same context
serves every checkpoint and every operation in the family; it depends only on
time. Every fibre of $X$ is allowed at every starting time. Define
$M_G$ as the smallest number $|\kappa(\mathbb N_0)|$ of used symbols.

For the matrices specified below, the result is

$$
\boxed{M_{\{T\}}=M_{\mathrm{SO}(B,\mathbb F_5)}
       =M_{\mathrm{GL}(3,\mathbb F_5)}=5.}
\tag{2}
$$

Moreover, all three families induce the **same equivalence relation on time**:

$$
n\sim_G m\quad\Longleftrightarrow\quad
F_{C,n}(x)=F_{C,m}(x)\ \text{for all }C\in G,\ x\in X.
\tag{3}
$$

Indeed, equal context symbols must imply equivalence in (3). Conversely, the
equivalence class of time is an admissible context, with the decoder taking the
common output on that class. Thus the minimum is exactly the number of classes
in (3), whenever that number is finite. The rest of the proof identifies them.

## 2. Coordinates and the unchanged native system

All vector, matrix, and affine arithmetic below is over $\mathbb F_5$.
Bits and the switches introduced later are ordinary numbers in $\{0,1\}$.
The native checkpoint order is

$$
x=(p_1,p_4,p'_1,p'_4,q,r),\qquad
s=p_1+p_4+p'_1+p'_4,\qquad z=s+q+r.
$$

With $\mathbf1=(1,1,1,1)^\top$, write

$$
p=4s\mathbf1+w_1(1,-1,0,0)^\top
 +w_2(0,1,-1,0)^\top+w_3(0,0,1,-1)^\top.
\tag{4}
$$

This decomposition is unique. Explicitly,
$w_1=p_1-4s$, $w_2=p_1+p_4-8s$, and
$w_3=p_1+p_4+p'_1-12s$. Conversely,

$$
p=(4s+w_1,\;4s-w_1+w_2,\;4s-w_2+w_3,\;4s-w_3).
\tag{5}
$$

Thus $w\in\mathbb F_5^3$ parametrizes the whole 125-point fibre over
each $(s,q,r)$. Set

$$
B=\begin{pmatrix}2&4&0\\4&2&4\\0&4&2\end{pmatrix},\quad
A=\begin{pmatrix}4&1&0\\0&1&0\\0&1&4\end{pmatrix},\quad
P=\begin{pmatrix}0&4&1\\0&4&0\\1&4&0\end{pmatrix},
$$

$$
T=\begin{pmatrix}1&0&0\\3&4&0\\4&0&4\end{pmatrix},\quad
w_*=(1,4,3)^\top,\quad t=(2,3,1)^\top=2w_*,\quad
h(r)=(3,r,3+r)^\top.
\tag{6}
$$

Direct multiplication gives $\det B=4$,
$A^2=P^2=T^2=I$, $AP=PA$, and
$A^\top BA=P^\top BP=T^\top BT=B$; all three determinants are one.
In particular, for

$$
\mathrm{SO}(B,\mathbb F_5)
=\{C\in\mathrm{GL}(3,\mathbb F_5):C^\top BC=B,\ \det C=1\},
$$

the exact predecessor operation satisfies $T\in\mathrm{SO}(B,\mathbb F_5)$.

The complete native fibre maps are as follows. Together with (4)–(5), these
specify the maps on all six checkpoint coordinates, not merely their action
on a selected orbit.

| Native generator | New $(s,q,r)$ | New $w$ |
|---|---|---|
| $a$ | $(s,q,r)$ | $Aw$ |
| $b$ | $(-s,-q,-r)$ | $-Pw$ |
| $c$ | $(1-s,1-q,-r)$ | $-Pw+h(r)$ |
| $d$ | $(-s,1-q,1-r)$ | $-w+t$ |
| $e$ | $(-s,2-q,1-r)$ | $-w+t$ |

Each generator is an involution on the full checkpoint domain. In particular,
the $r$ change is part of $c$: since $Ph(r)=h(-r)$, two consecutive
$c$'s restore both the base and the fibre.

The driver is $\theta_n=\operatorname{popcount}(n)\bmod2$. At time $n$,
the native update selects the generator of index $z+2\theta_n\pmod5$
in the order $a,b,c,d,e$. Its sheet transitions, indexed by
$z=0,1,2,3,4$, are

$$
f_0=(0,4,0,4,4),\qquad f_1=(2,1,1,3,1).
\tag{7}
$$

The active union $z\in\{1,4\}$ is forward invariant. On this union the
prescribed action keeps $(s,q,r)$ fixed and sends

$$
w\longmapsto w_*+P^{\chi(z)}CP^{\chi(z)}(w-w_*),
\qquad\chi(1)=0,\quad\chi(4)=1.
\tag{8}
$$

This active action is already independent of time.

## 3. The first-entry lift and its inverse

For a given time and base $(n,s,q,r)$, let $\tau\ge0$ be the first
entry time into the active union under (7), and let $z_\tau$ be the arrival
sheet. Let $H$ be the composition of the native affine fibre maps along
those $\tau$ steps; $H=\mathrm{Id}$ for $\tau=0$. The base trajectory
and its selected word do not depend on $w$. Every map in that word is a
bijection between its source and target fibres, so $H$ is invertible.

The inherited first-entry coordinate and prescribed action are

$$
\mathcal K_{n,s,q,r}(w)
=(-1)^{n+\tau}P^{\chi(z_\tau)}(H(w)-w_*),
\qquad w'=\mathcal K_{n,s,q,r}^{-1}C\mathcal K_{n,s,q,r}(w).
\tag{9}
$$

This definition keeps the initial $(s,q,r)$ fixed in the final checkpoint.
It uses the inverse of the **specified word on a specified fibre**. It does
not require an inverse of the autonomous native update on its full domain.

If $\mathcal K=\lambda J$ for a scalar $\lambda\ne0$, then

$$
\mathcal K^{-1}C\mathcal K
=J^{-1}\lambda^{-1}C\lambda J=J^{-1}CJ
\tag{10}
$$

for every linear $C$. This equality is between entire affine actions,
including their translations. It does not merely compare their linear parts.

## 4. Five contexts and an explicit decoder

Put $\varepsilon_n=n\bmod2$ and define

$$
e_0(n)=1-\varepsilon_n,\qquad
e_2(n)=\varepsilon_n(1-\theta_n),\qquad
e_3(n)=\theta_n(1-\theta_{n+1}),\qquad
\kappa(n)=(e_0(n),e_2(n),e_3(n)).
\tag{11}
$$

The identity $\theta_{2m+1}=1-\theta_{2m}$ shows that its image is
exactly the following set. The representative times also prove occurrence.

| Class | Condition | Context | First occurrence |
|---|---|---|---:|
| $k_0$ | $n$ even, $\theta_n=0$ | $(1,0,0)$ | 0 |
| $k_1$ | $n$ odd, $(\theta_n,\theta_{n+1})=(1,1)$ | $(0,0,0)$ | 1 |
| $k_2$ | $n$ even, $\theta_n=1$ | $(1,0,1)$ | 2 |
| $k_3$ | $n$ odd, $\theta_n=0$ | $(0,1,0)$ | 3 |
| $k_4$ | $n$ odd, $(\theta_n,\theta_{n+1})=(1,0)$ | $(0,0,1)$ | 11 |

Set

$$
o_r=(4,4-r,1-r)^\top,\qquad u_r=(4+r,4,2-r)^\top,
\qquad R_r(w)=Aw+(r+1,0,1-r)^\top.
\tag{12}
$$

Here $R_r^2=\mathrm{Id}$ and $R_r(w_*)=u_r$. For a context
$k=(e_0,e_2,e_3)$, define

$$
J_{k,z,r}(w)=
\begin{cases}
P(A^{e_0}w-o_r),&z=0,\\
w-w_*,&z=1,\\
R_r^{e_2}(w)-w_*,&z=2,\\
P(A^{e_3}w-w_*),&z=3,\\
P(w-w_*),&z=4.
\end{cases}
\tag{13}
$$

All five formulas are invertible. Their inverses, for a coordinate value
$v$, are respectively

$$
J_{k,z,r}^{-1}(v)=
\begin{cases}
A^{e_0}(Pv+o_r),&z=0,\\
v+w_*,&z=1,\\
R_r^{e_2}(v+w_*),&z=2,\\
A^{e_3}(Pv+w_*),&z=3,\\
Pv+w_*,&z=4.
\end{cases}
\tag{14}
$$

The decoder unpacks (4), computes

$$
\boxed{w'=J_{k,z,r}^{-1}CJ_{k,z,r}(w),}
\tag{15}
$$

retains $(s,q,r)$, and repacks by (5). For each $C$, the inverse
checkpoint action is obtained by replacing $C$ with $C^{-1}$.
Equivalently $J(w)=Q(w-m)$, with the following data:

| Sheet | $Q$ | $m$ |
|---|---|---|
| 0 | $PA^{e_0}$ | $A^{e_0}o_r$ |
| 1 | $I$ | $w_*$ |
| 2 | $A^{e_2}$ | $w_*$ if $e_2=0$; $u_r$ if $e_2=1$ |
| 3 | $PA^{e_3}$ | $A^{e_3}w_*$ |
| 4 | $P$ | $w_*$ |

In every row $Q^2=I$, giving the full map
$w'=m+QCQ(w-m)$.

## 5. Proof that the decoder is the prescribed lift at every time

We prove that (13), with $k=\kappa(n)$, differs from (9) only by a
nonzero scalar. The driver is the fixed point of
$\mu(0)=01,\ \mu(1)=10$. Every three consecutive positions contain a
complete even-aligned substitution block, so neither `000` nor `111` occurs.
The relevant exits always occur by the inherited entry bound, restated and
proved in Section 8.

**Sheet 0.** Before the first occurrence of `11`, the driver word splits
uniquely into blocks `0` and `10`. A block `0` applies $a$ and stays
on sheet 0. A block `10` applies $c$, enters sheet 2, and applies
$c$ again to return to sheet 0. The whole double step, including
$r\mapsto-r\mapsto r$, is the identity. Thus the prefix reduces to
$A^j$, where $j$ is the number of singleton zeros, modulo two.

The terminating `11` applies $c$ and then $e$, entering sheet 1.
Using $t=2w_*$ and $Po_r=h(r)-w_*$, its active coordinate is

$$
e(c_r(w))-w_*=Pw-h(r)+w_*=P(w-o_r).
\tag{16}
$$

Here $c_r$ denotes the affine fibre map with the initial parameter
$r$; the native maps still update their bases as in the table.
Every `11` starts at an odd absolute index, since an even-aligned pair is
always `01` or `10`. If its first relative starting index is $\ell$,
then $\ell\equiv1-n\pmod2$. Each erased `10` has even length, hence
$j\equiv\ell\equiv1-n\pmod2$. Applying (16) after this prefix gives
$P(A^{e_0(n)}w-o_r)$, exactly the first row of (13).

**Sheet 2.** If $\theta_n=1$, $e$ immediately enters sheet 1 and
$e(w)-w_*=-(w-w_*)$. This gives the row with $e_2=0$.
If $\theta_n=0$, the first map is $c$, entering sheet 0 with
parameter $-r$ at time $n+1$. The just-proved formula uses
$e_0(n+1)=\varepsilon_n$. Substitution gives the explicit identities

$$
P(-Pw+h(r)-o_{-r})=-(w-w_*),
$$
$$
P\bigl(A(-Pw+h(r))-o_{-r}\bigr)
=-\bigl(R_r(w)-w_*\bigr).
\tag{17}
$$

Thus the extra involution $R_r$ is needed exactly when $n$ is odd
and $\theta_n=0$, which is $e_2(n)=1$.

**Sheet 3.** Each initial `1` applies $a$ and stays on sheet 3. The
first `0` applies $d$ and enters sheet 4. The initial run of ones has
length $j\in\{0,1,2\}$. Its parity is one exactly for the prefix
`10`, hence $j\equiv e_3(n)\pmod2$. The terminal active coordinate is

$$
P(d(A^j w)-w_*)=-P(A^{e_3(n)}w-w_*),
\tag{18}
$$

which agrees with (13) up to sign.

**Sheets 1 and 4.** Here $\tau=0$, so the last two active formulas
are the definition (8), with the irrelevant overall factor $(-1)^n$
in (9).

Together these cases show $\mathcal K=\lambda J$, with
$\lambda\in\{1,-1\}$, on every declared fibre and at every time.
Equation (10) proves (15) for every linear invertible $C$, establishing

$$
M_{\mathrm{GL}(3,\mathbb F_5)}\le5.
\tag{19}
$$

The argument proves the full-family upper bound algebraically; it does not
infer it from checking a finite sample of matrices.

## 6. Sharp lower bound from the single prescribed operation

Use the same three checkpoints at every time:

$$
x_0=(0,0,0,0,0,0),\quad x_2=(3,3,3,3,0,0),\quad
x_3=(2,2,2,2,0,0).
\tag{20}
$$

They have $(s,q,r,w)=(z,0,0,0)$ for $z=0,2,3$, respectively.
Substituting the exact $T$ from (6) into (15) gives the following
**output fibre triples**. The base $(s,q,r)$ stays fixed, so these
triples determine the full checkpoint outputs through (5).

| Context | Time | Output $w'$ on $x_0$ | Output $w'$ on $x_2$ | Output $w'$ on $x_3$ |
|---|---:|---|---|---|
| $k_0$ | 0 | $(3,4,0)$ | $(0,0,2)$ | $(3,0,0)$ |
| $k_1$ | 1 | $(1,4,4)$ | $(0,0,2)$ | $(3,0,0)$ |
| $k_2$ | 2 | $(3,4,0)$ | $(0,0,2)$ | $(2,0,0)$ |
| $k_3$ | 3 | $(1,4,4)$ | $(3,3,4)$ | $(3,0,0)$ |
| $k_4$ | 11 | $(1,4,4)$ | $(0,0,2)$ | $(2,0,0)$ |

All five rows are distinct. If fewer than five context symbols were used,
two of these times would receive the same symbol. For some common checkpoint
in (20), the decoder would then have the same inputs but require different
outputs. Therefore $M_{\{T\}}\ge5$. Since
$\{T\}\subseteq\mathrm{SO}(B,\mathbb F_5)
\subseteq\mathrm{GL}(3,\mathbb F_5)$,

$$
5\le M_{\{T\}}\le M_{\mathrm{SO}(B,\mathbb F_5)}
\le M_{\mathrm{GL}(3,\mathbb F_5)}\le5.
\tag{21}
$$

This proves (2). More strongly, equal values of $\kappa$ give equal
actions for all $C$, while different values give different actions
already for $T$, by the table. Hence for all three families,

$$
n\sim_G m\quad\Longleftrightarrow\quad\kappa(n)=\kappa(m).
\tag{22}
$$

**Three common test checkpoints are also necessary.** The classes
$k_0,k_1$ differ only in $e_0$, so their actions agree off sheet 0.
Similarly $k_1,k_3$ agree off sheet 2, and $k_1,k_4$ agree off
sheet 3. A common set distinguishing every pair must meet all three disjoint
sheets. It therefore contains at least three checkpoints. The table reaches
this bound. This concerns one fixed set of test checkpoints, not an adaptive
query model with a separately specified protocol.

## 7. The complete 24-factor quotient and the minimum window length

Since $\theta=\mu^3(\theta)$ and the blocks of $\mu^3$ have length
eight, every length-nine factor is contained in two consecutive blocks.
All four pairs `00`, `01`, `10`, `11` occur in $\theta$. Therefore the
exact language of length-nine factors is

$$
\mathcal L_9=
\{\mu^3(ab)[j:j+9]:ab\in\{00,01,10,11\},\ 0\le j<8\}.
\tag{23}
$$

The slice has nine symbols, starting at zero-based offset $j$. Every
element on the right occurs, because its pair $ab$ occurs in the fixed
point; the block decomposition proves the opposite inclusion. Thus (23)
is a finite complete certificate, not a completeness claim inferred from
a searched prefix. Removing repetitions from its 32 candidates yields:

| Context | All length-nine factors in that class | Count |
|---|---|---:|
| $k_0$ | `010110011`, `010110100`, `011001011`, `011001101`, `011010010`, `011010011` | 6 |
| $k_1$ | `110010110`, `110011010`, `110100101`, `110100110` | 4 |
| $k_2$ | `100101100`, `100101101`, `100110010`, `100110100`, `101001011`, `101001100` | 6 |
| $k_3$ | `001011001`, `001011010`, `001100101`, `001101001`, `010010110`, `010011001` | 6 |
| $k_4$ | `101100110`, `101101001` | 2 |

Only the first four bits are needed to compute the class. For
$b_i=\theta_{n+i}$,

$$
\boxed{
e_0=(b_0\mathbin\oplus b_1)(b_2\mathbin\oplus b_3),\qquad
e_2=(1-e_0)(1-b_0),\qquad e_3=b_0(1-b_1).}
\tag{24}
$$

For even $n$, both aligned pairs are opposite, and the product for
$e_0$ is one. For odd $n=2m+1$, the four bits are

$$
(1-\theta_m,\ \theta_{m+1},\ 1-\theta_{m+1},\ \theta_{m+2}).
$$

Both pairs being opposite would force
$\theta_m=\theta_{m+1}=\theta_{m+2}$, contradicting the absence of
`000` and `111`. Hence the product is zero for odd $n$, and (24)
agrees with (11). Explicitly:

| Context | Length-four prefixes |
|---|---|
| $k_0$ | `0101`, `0110` |
| $k_1$ | `1100`, `1101` |
| $k_2$ | `1001`, `1010` |
| $k_3$ | `0010`, `0011`, `0100` |
| $k_4$ | `1011` |

Three bits cannot suffice in the class of **fixed contiguous forward windows
of the driver, without extra time or parity information**. At $n=3$ and
$n=10$, the three-bit prefix is `010`, but the four-bit prefixes are
`0100` and `0101`; the contexts are $k_3$ and $k_0$. Their $T$
outputs on the same $x_0$ differ by Section 6. Every shorter forward
prefix is also shared. Thus four is the exact minimum window length in
this stated class.

## 8. Relation to the inherited nine-step bound

The three numbers measure different things:

| Quantity | Exact value |
|---|---:|
| Used symbols of a common time-only context on all fibres | 5 |
| Length of a sufficient fixed contiguous forward driver window | 4 |
| Uniform first-entry bound for the native sheet dynamics | 9 |

For completeness, the inherited entry bound follows directly from (7).
Sheet 3 exits at the first zero. Sheets 0 and 2 enter by the end of the
next complete `11`. Starts of `11` are exactly positions $2m+1$ with
$(\theta_m,\theta_{m+1})=(0,1)$. In a binary sequence with neither
`000` nor `111`, consecutive starts of `01` have separation at most four:
between them there is a run of one or two ones and a run of one or two zeros.
Thus consecutive starts of `11` in $\theta$ have separation at most
eight, yielding completion within nine forward steps from any time. The
initial prefix also satisfies this bound, with the first `11` starting
at index one.

The bound is sharp at $n=14,z=0$, where the nine read bits are
`101001011` and the sheets, including the starting sheet, are

$$
0,2,0,2,0,0,2,0,2,1.
\tag{25}
$$

There is no active sheet before the ninth step. This restates the inherited
`TM-SHEET-SYNCHRONIZING-GRAPH` boundary to distinguish it from the new
context minimum and the new four-bit compression.

## 9. Boundaries of the result

On the active union alone, (8) is independent of time, and the context minimum
is **one**. The value five requires the common full domain of all fibres at
every starting time, including transient fibres. It is not a minimum for
only the synchronized part of an orbit launched at time zero.

Five symbols are not a five-state autonomous clock. In fact,

$$
\kappa(0)=\kappa(10)=k_0,\qquad
\kappa(1)=k_1\ne k_4=\kappa(11).
\tag{26}
$$

There is no function $f$ on these five labels satisfying
$\kappa(n+1)=f(\kappa(n))$ for all $n$. A separate condition on
autonomous updating, or on an automaton reading the binary representation
of $n$, would define a different minimization problem.

The result concerns the prescribed action. It does not provide a native
generator word realizing $T$, a new physical gate, or a physical source
of the context. The fibre inverses in (9) do not restore global injectivity
of the original autonomous update; its previously established collisions
are compatible with every statement here.

The five time contexts are distinct from the ternary one-use reference of
the contact-reader problem and from a five-state complement in a specified
recovery problem for the original update. Equal numerical answers do not
identify those contracts. A set of five contexts does not specify a
probability distribution, a Shannon entropy of $\log5$, a temperature,
or a thermal cost. No Landauer relation or new physical law follows here.

## 10. Evidence and public scope

Equations (11)–(22) are the proof of the all-time, all-fibre, all-linear-
operation result. Equation (23) is the complete finite factor certificate.
Neither conclusion depends on interpreting a large local enumeration as
an additional public gate.

The reviewed source package additionally contains local certificates for
60,000 comparisons using literal six-coordinate generators and 600 full
affine-coordinate cases. The first count is 24 factors times 125 bases
times four affinely determining points times five chosen matrices; it is
not an enumeration of all matrices in $\mathrm{GL}(3,\mathbb F_5)$.
The second count is 24 factors times 25 relevant $(z,r)$ pairs.
The universal upper bound comes from scalar cancellation and the proof of
the complete coordinates above. Local reproductions are supporting evidence,
not a claim of a new byte-identical public gate on two architectures.

This addendum extends the reviewable mathematical content of the existing
draft. The predecessor's preregistration, verifier, run records, expected
output, and result statuses retain their original scope and bytes. Adding
this proof does not retroactively enlarge the old formal run or promote
this result into the Canon.
