# Ready receiver exchange and the reference boundary of energy selection

**PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T.**
Author: A. M. Thorn. Apache-2.0.
Claim [#1620][claim]. Analytical pin:
851c4ef0ef43690c245ef3208d436a924080bbb7.
Exact source custody: [SOURCES.tsv](SOURCES.tsv).
Frozen questions and exposure: [CONTRACT.md](CONTRACT.md).

The original native step cannot send fresh source content into the completed
receiver after synchronization. We prove that statement for its entire
future, then construct a complete ready-content exchange \(W\) and identify
what this exchange leaves unresolved. The normalized relative energy family
has two separately conserved magnitude counts. A sharp two-block witness
can distinguish their price, but neither \(W\), linear coupling, nor certain
nonlinear reference-independent contacts can do so. A full reference-reading
counterexample locates the precise additional permission.

Every conclusion below is an exact analytical statement on a named carrier.
Neither a target-designed contact nor an unpriced relative reference is
treated as a physically admitted apparatus. No new scientific program,
enumeration, numerical calculation or experiment is evidence for this note.

## 1. Literal native state and the supplied one-shot record

Native coordinates are
\[
 x=(a,b,c,d,q,r)=(p_1,p_4,p'_1,p'_4,q,r)\in\mathbb F_5^6,\qquad
 z=a+b+c+d+q+r,\quad \Gamma(x)=(z,q,r).
\]
All coordinate algebra is in \(\mathbb F_5\). Counts, real accounts and
the original counter are ordinary integers or reals, as stated.

The original counter gives \(\theta_n=\operatorname{popcount}(n)\bmod2\);
the actual letter has index \(z+2\theta_n\) in the ordered alphabet
\(a,b,c,d,e\). Thus
\[
 U(n,x)=(n+1,g_{z+2\theta_n}(x)).
 \tag{1}
\]
A row label in this table is a letter, not a coordinate:

| Letter | Complete checkpoint image | Controller image |
|---|---|---|
| \(a\) | \((b,a,d,c,q,r)\) | \((z,q,r)\) |
| \(b\) | \((-c,-d,-a,-b,-q,-r)\) | \((-z,-q,-r)\) |
| \(c\) | \((2-c,1-d+r,2-a,1-b-r,1-q,-r)\) | \((2-z,1-q,-r)\) |
| \(d\) | \((2-a,1-b,3-c,4-d,1-q,1-r)\) | \((2-z,1-q,1-r)\) |
| \(e\) | \((2-a,1-b,3-c,4-d,2-q,1-r)\) | \((3-z,2-q,1-r)\) |

These are the canonical generators and the literal formulas used in
[#1619, section 1][relative]. Each letter is an affine involution.
State-dependent selection in (1) is not the same object as one freely
chosen word of these letters.

Keep the original split
\[
 S=(a,c),\qquad M=(b,d),\qquad R=(b,d,q,r).
 \tag{2}
\]
The complete receiver includes the shared \(q,r\). The source content
reader below also uses these shared coordinates.

For independent new and old contents \(\lambda,\mu\in\mathbb F_5\),
#1619 specializes the canonical one-shot record to
\[
 x_{\lambda,\mu}(0)=(\lambda,\mu,-\lambda,-\mu,0,0).
\]
The actual origin-zero prefix is \(a,c,e\), giving
\[
\begin{array}{c|c}
n&x_{\lambda,\mu}(n)\\ \hline
0&(\lambda,\mu,-\lambda,-\mu,0,0)\\
1&(\mu,\lambda,-\mu,-\lambda,0,0)\\
2&(2+\mu,1+\lambda,2-\mu,1-\lambda,1,0)\\
3&(-\mu,-\lambda,1+\mu,3+\lambda,1,1).
\end{array}
\tag{3}
\]
The first actual \(a\) already swaps the raw piston blocks. The prescribed
completion reader is BLANK before cut 3 and PRESENT(\(\lambda\)) from
cut 3 onward. The old \(\mu\) remains readable at the source. This
native prefix and occupied-input interpretation are inherited from
#1619 and canonical U-NATIVE-SOURCE-RECEIVER-RECORD; their discovery is
not claimed here.

The reference in the relative account is a second actual native cell,
not a frozen zero vector or a history computed by a reader. For (3)
it starts at zero and follows the same table with \(\lambda=\mu=0\).
Section 4 treats the larger comparison carrier.

## 2. No new receiver information anywhere in the synchronized future

### 2.1 The complete future theorem

The set \(\mathcal X_{14}=\{x:z\in\{1,4\}\}\) is invariant for either bit.
The actual selection and next trace are:

| Old \(z\) | Bit | Letter | New \(z\) |
|---:|---:|---|---:|
| 1 | 0 | \(b\) | 4 |
| 4 | 0 | \(e\) | 4 |
| 1 | 1 | \(d\) | 1 |
| 4 | 1 | \(b\) | 1 |

In each case \(z'=4+2\theta\). The three receiver maps are
\[
\begin{aligned}
 g_b^R(b,d,q,r)&=(-d,-b,-q,-r),\\
 g_d^R(b,d,q,r)&=(1-b,4-d,1-q,1-r),\\
 g_e^R(b,d,q,r)&=(1-b,4-d,2-q,1-r).
\end{aligned}
\tag{4}
\]
None reads either source piston.

**Future noninterference theorem.** Start two checkpoints in
\(\mathcal X_{14}\) with equal trace and equal complete receiver.
For any common future binary word, their traces and receivers agree
after every prefix of that word.

**Proof.** At the empty prefix the assertion is the hypothesis. Equal
trace and common next bit select the same row of the table. The next
trace is common, and (4) computes the next receiver from the common old
receiver alone. Induction proves the assertion for every finite prefix,
hence at every time in any infinite common continuation. \(\square\)

Quantification over arbitrary common words strengthens the mathematical
statement; it does not add a physical drive-input port to (1).

For the original counter starting at zero, canonical synchronization
gives
\[
 z_n=4+2\theta_{n-1}\qquad(n\ge3).
 \tag{5}
\]
At a fixed such cut and receiver, exactly five source states have that
trace:
\[
 a\in\mathbb F_5,\qquad c=z-b-d-q-r-a.
 \tag{6}
\]
This is also a family of reachable checkpoints, not merely a formal
trace fiber. The initial \(z=0\) sheet follows \(a,c,e\); that fixed
affine composition maps it bijectively onto the whole \(z=1\) sheet
at cut 3. Each subsequent selected letter maps the prescribed trace
sheet bijectively onto the next. Thus (6) is not reduced by requiring
some origin-zero preparation. Its five source states remain invisible
to the entire future receiver.

### 2.2 What the theorem covers

A reader of the current receiver and a common time cannot distinguish
these preparations. Neither can a reader of the entire subsequent
receiver history. An added observation register with the same initial
state and an update depending only on these common inputs stays equal
by the same induction.

For a finite product of independent native copies, require equal trace
and complete receiver in **each** matched pair of copies, and the same
future drive for that pair. Applying the theorem componentwise proves
equality of the complete product receiver history. Correlation among
the hidden initial source choices does not change this implication.
Adding more uncoupled copies increases state capacity without supplying
a source-to-receiver contact on this tail.

The theorem has a precise boundary. Changing source pistons so that
trace changes can alter selection. Such an intervention is outside the
same-trace comparison and must be counted as an added controller
contact. A new register that reads source or changes the old dynamics
also supplies a new input to the proof and is not covered.

Allowing different starting positions in the Thue-Morse word does not
provide arbitrarily long unsynchronized windows. The canonical
TM-SHEET-SYNCHRONIZING-GRAPH theorem gives a sharp upper bound of nine
steps from any such origin; its eight-step nonsynchronizing witness is
10100101. That bound is inherited from [Canon v103][canon], not obtained
by a new computation here. For the specified origin zero, (5) starts
at cut 3.

This strengthens #1619's common-cut equality \(x_5=x_3\). The new
statement concerns all future observations after synchronized
same-receiver preparation; it does not merely rule out one timing pair.

## 3. A complete exchange of already completed contents

### 3.1 The prepared carrier and the two fixed readers

Define
\[
 A=a+c,\quad B=b+d,\quad C=a-c-2,\quad D=b-d-1
\]
and take the entire carrier
\[
 \mathcal H=\{A=2B,\ B\in\{2,3\},\ z\in\{1,4\}\}.
 \tag{7}
\]
On it \(A\in\{1,4\}\), \(B=3A\), and \(k=Az\) has \(k^2=1\).
The prepared contents are
\[
 \mu=1+2kC,\qquad \lambda=3-BzD=3-3kD.
 \tag{8}
\]
The canonical receiver computes \(z=3B+q+r\) from \(R\); the source
computes \(z=4A+q+r\) from \((a,c,q,r)\). Therefore (8) uses exactly
the ports declared in #1619. On all of \(\mathcal H\) the receiver
readiness conditions \(B\in\{2,3\}\) and \(3B+q+r\in\{1,4\}\)
are true, so its reading is always PRESENT(\(\lambda\)), including zero.

At fixed controls, invert (8):
\[
 C=k(2+3\mu),\qquad D=k(1+3\lambda).
 \tag{9}
\]
Indeed \(2^{-1}=3\) in \(\mathbb F_5\), and \(k^{-1}=k\).
The full inverse parametrization is
\[
\begin{aligned}
 B&=3A,&q&=z-4A-r,\\
 a&=3(A+C+2),&c&=3(A-C-2),\\
 b&=3(B+D+1),&d&=3(B-D-1).
\end{aligned}
\tag{10}
\]
Hence
\[
 \mathcal H\ \simeq\
 \{1,4\}^2\times\mathbb F_5^3,\quad
 (A,z,r,\mu,\lambda),
 \qquad |\mathcal H|=500.
 \tag{11}
\]
This cardinality follows from a bijection, not a state enumeration.

The \(q,r\) access in the source reader matters. For example, set
\(A=1,C=1,B=3,D=0,r=0\). The same source pistons are \(S=(2,4)\).
Choosing \(z=1,q=2\) gives \(\mu=3\), whereas \(z=4,q=0\) gives
\(\mu=4\). Both are in \(\mathcal H\). Thus no function of the two
source pistons alone equals the specified \(\mu\) throughout this carrier.

### 3.2 Unique fixed-control swap and its inverse

Keep \(A,B,q,r\) fixed and set
\[
 \boxed{W:\quad C'=D+k,\qquad D'=C-k.}
 \tag{12}
\]
The total trace and \(k\) then remain fixed. Substituting (9) yields
\[
 C'=k(2+3\lambda),\qquad D'=k(1+3\mu).
\]
Thus, on the entire carrier,
\[
 W:(\mu,\lambda)\longmapsto(\lambda,\mu).
 \tag{13}
\]
Equations (9)--(10) make this the unique map with the required content
swap and fixed controls. Applying (12) twice gives \(C''=C,D''=D\);
therefore \(W^2=\mathrm{id}\) on all of \(\mathcal H\).

The receiver remains ready, obtains the source content, and the old
receiver content is retained in the existing source port. No old
content is erased. This is a reset-free content exchange of a completed
receiver, not a new blank-to-present completion event.

### 3.3 Commutation with the actual continuation

The actual \(b,d,e\) branches act on the prepared variables as follows:

| Actual branch | \(A\) | \(z\) | \(C,D,k\) | \(r\) |
|---|---|---|---|---|
| \(b\) | \(-A\) | \(-z\) | unchanged | \(-r\) |
| \(d\) at \(z=1\) | \(-A\) | \(z\) | all negated | \(1-r\) |
| \(e\) at \(z=4\) | \(-A\) | \(z\) | all negated | \(1-r\) |

This is direct substitution in section 1; \(B\) also negates. It proves
\(\mathcal H\) is forward invariant and both contents (8) are constant
under every actual tail branch. Formula (12) commutes with leaving
\(C,D,k\) unchanged and with negating all three. Since \(W\) preserves
the selection inputs \(z,\theta_n\), its lift that leaves \(n\) fixed
satisfies
\[
 \widehat W U=U\widehat W
 \quad\text{on }\mathbb N_0\times\mathcal H.
 \tag{14}
\]

This does not make \(W\) an iterate of \(U\). All actual continuation
keeps \(\mu,\lambda\) separately constant, so no such continuation
executes (13) when the contents differ.

The inverse scopes also differ. \(W\) is a permutation of the whole
500-state \(\mathcal H\). At a known preceding controller slice, the
selected original letter is a bijection to the next slice with that
same letter as inverse. On the union of both trace sheets the selected
step can merge inputs: for a fixed bit both old traces go to the same
new trace. In coordinates (11), each old trace sheet maps onto the
whole prescribed next trace sheet while keeping the contents. The
original \(U\) therefore has no global checkpoint inverse on that union.
Adding the advancing counter does not separate two inputs at the same
old time that have already merged.

### 3.4 Even a fixed word in all five letters cannot give this whole \(W\)

Every fixed composition of the five original letters is affine on
\(\mathbb F_5^6\), even when intermediate points leave \(\mathcal H\).
Consider the four points with \(A,z\in\{1,-1\}\), \(C=D=r=0\):
\[
 x(A,z)=(3A+1,\ 4A+3,\ 3A-1,\ 4A-3,\ z-4A,\ 0).
 \tag{15}
\]
They lie in \(\mathcal H\), and their alternating rectangular sum is
zero because (15) is affine in \(A,z\). Any affine image, followed by
the affine coordinate reading \(C\), must have the same zero alternating
sum. But (12) gives \(C(Wx(A,z))=Az\), whose alternating sum is
\[
 1-(-1)-(-1)+1=4\ne0\quad\text{in }\mathbb F_5.
\]
This contradiction proves \(W|_{\mathcal H}\) is not the restriction of
any one affine map. Therefore no one fixed original-letter word realizes
it on all of \(\mathcal H\).

The quantifier over the whole carrier is essential. This does not
exclude realization on a particular control section, or by a newly
supplied state-dependent selector. Those would require their own law.

Conversely, commutation alone is very permissive. In coordinates (11)
the actual step changes only \((A,z,r)\), fixing \((\mu,\lambda)\).
Every fixed permutation of the 25 content pairs, lifted with unchanged
controls, therefore commutes with that step. This gives an \(S_{25}\)
subgroup of commuting maps, not a classification of the entire
centralizer. \(W\) is unique for the prescribed fixed-control exchange;
it is not selected merely by commutation.

## 4. What the relative account does and does not determine

### 4.1 The original signed-permutation account

Take an actual signal \(x\) and actual reference \(\rho\) with common
counter and \(\Gamma(x)=\Gamma(\rho)\). The full comparison state retains
both cells. Their difference
\[
 \delta=(a-a_\rho,b-b_\rho,c-c_\rho,d-d_\rho)
 \quad\text{lies in}\quad
 V=\{\delta\in\mathbb F_5^4:\textstyle\sum_i\delta_i=0\}.
 \tag{16}
\]
The common controller selects the same letter, and remains common.
Subtracting section 1 cancels every translation, including the
\(r\)-dependent part of \(c\):

| Letter | Difference image |
|---|---|
| \(a\) | \((\delta_b,\delta_a,\delta_d,\delta_c)\) |
| \(b,c\) | \((-\delta_c,-\delta_d,-\delta_a,-\delta_b)\) |
| \(d,e\) | \(-\delta\) |

This is the whole-prefix difference law supplied by #1619. Define
ordinary integer counts
\[
 N_1=\#\{i:\delta_i\in\{1,-1\}\},\qquad
 N_2=\#\{i:\delta_i\in\{2,-2\}\}.
\]
Each is separately conserved by all five letters.

A common even nonnegative function \(f:\mathbb F_5\to\mathbb R_{\ge0}\)
with \(f(0)=0\) has weights \(f(\pm1)=\alpha,\ f(\pm2)=\beta\).
The account is \(\alpha N_1+\beta N_2\).
When \(\alpha>0\), fixing the common unit gives exactly
\[
 \boxed{E_\kappa=N_1+\kappa N_2,\qquad \kappa=\beta/\alpha\ge0.}
 \tag{17}
\]
The unnormalizable edge \(\alpha=0\) is not included in (17).
Strict positivity on all nonzero differences requires \(\kappa>0\).
For example, a pair \((2,0,-2,0)\) has positive account only if
\(\kappa>0\).

Let the balanced integer representative be
\(\ell(0,1,2,3,4)=(0,1,2,-2,-1)\):

| Common coordinate reading | Weight \(\kappa\) |
|---|---:|
| \(\ell(t)^2\) | 4 |
| \(\ell(t)^4\) | 16 |
| \(\mathbf1_{t\ne0}\) | 1 |

In particular \(E_4\) means the **square** account, not the fourth-power
coordinate account. The fourth-power alternative is \(E_{16}\).
Original conservation does not determine their relative price after
unit calibration. Independent products and compositions of the same
signed-permutation laws cannot change that conclusion.

### 4.2 Four different invariant classifications

The family (17) does not exhaust conserved functions even if one reads
only \(\delta\). The linear coordinates
\[
 u=\delta_a+\delta_b,\quad
 v=\delta_a+\delta_c,\quad
 w=\delta_a+\delta_d
 \tag{18}
\]
are a bijection \(V\to\mathbb F_5^3\): recover
\(\delta_a=3(u+v+w)\), then
\(\delta_b=u-\delta_a,\delta_c=v-\delta_a,\delta_d=w-\delta_a\).
The difference table gives

| Letter | Action on \((u,v,w)\) |
|---|---|
| \(a\) | \((u,-v,-w)\) |
| \(b,c\) | \((u,-v,w)\) |
| \(d,e\) | \((-u,-v,-w)\) |

The second row flips \(v\); composing it with the first flips \(w\);
combining these flips with the last gives the flip of \(u\).
Thus all five letters generate all eight independent sign changes.
Their orbits are exactly \((u^2,v^2,w^2)\in\{0,1,4\}^3\). Every
function invariant under **all five letters** is consequently
\[
 F(\delta)=H(u^2,v^2,w^2),
 \tag{19}
\]
with arbitrary values on 27 classes.

The **tail** group generated by \(b,d,e\) flips \(v\) independently
and flips \(u,w\) together. The pair \((u,w)\) has one zero orbit and
12 two-point sign orbits. Hence the tail has \(3\cdot13=39\) orbits,
classified by
\[
 (v^2,u^2,w^2,uw),\qquad (uw)^2=u^2w^2.
 \tag{20}
\]
When both \(u,w\) are nonzero the product chooses their relative sign;
when one is zero its square already determines the remaining sign
orbit. This proves completeness of (20), including the zero cases.

For two cells in \(\mathcal H\) with common \(\Gamma\),
\(z=4A+q+r\) fixes their common \(A\), then \(B,k\). Their differences
satisfy
\[
 V_{\rm prep}=\{(s,t,-s,-t):s,t\in\mathbb F_5\},\qquad v=0.
 \tag{21}
\]
Tail \(b\) is the identity on \((s,t)\), and \(d,e\) negate both.
There are 13 orbits. The paired action of \(W\) swaps \(s,t\), so
in the remaining coordinates it sends \((u,w)\) to \((u,-w)\).
Together with global negation this generates independent signs of
\(u,w\), giving 9 orbits \((u^2,w^2)\).

These statements have different domains:

| Domain and required invariance | Complete class data | Classes |
|---|---|---:|
| \(V\), all five letters | \((u^2,v^2,w^2)\) | 27 |
| \(V\), tail \(b,d,e\) | \((v^2,u^2,w^2,uw)\) with compatibility | 39 |
| \(V_{\rm prep}\), tail | \((u,w)\) modulo common sign | 13 |
| \(V_{\rm prep}\), tail and \(W\) | \((u^2,w^2)\) | 9 |

They classify functions only of the difference invariant under the named
groups. They are not classifications of all full-state, time-dependent
or physically admitted energy readings.

### 4.3 \(W\) exchanges the account without selecting its price

For a common prepared signal/reference pair, (12) has the same \(k\)
on both cells. Subtraction and (10) give
\[
 \delta'=(\delta_b,\delta_a,\delta_d,\delta_c).
 \tag{22}
\]
With the split (2),
\[
 (E_S^f,E_M^f)\longmapsto(E_M^f,E_S^f),\qquad
 \Delta E_M^f=-\Delta E_S^f.
 \tag{23}
\]
This holds for every common even \(f\), not only a square.
The reference with \((\mu_\rho,\lambda_\rho)=(0,0)\) is itself fixed
by \(W\); one may leave that actual reference on its original trajectory.
For a general reference the paired claim transforms it along with the
signal.

Thus \(W\) reduces the prepared tail's invariant classes from 13 to 9,
yet preserves both magnitude counts and every \(E_\kappa\). A complete
reversible overwrite with exact relative balance does not by itself
select physical energy. The assertion (22) is on prepared pairs inside
\(\mathcal H\); it is not an unproved extension of \(W\) to every pair
in #1619's larger original comparison carrier.


## 5. The sharp block count and two distinct energy thresholds

### 5.1 One complete zero-sum block cannot distinguish the square

**One-block theorem.** Every map \(T:V\to V\) satisfying
\(E_4(T\delta)=E_4(\delta)\) for every \(\delta\) preserves
\(N_1,N_2\) individually and hence every \(E_\kappa\).

**Proof.** Compare any input and output and write
\(r=\Delta N_1,\ s=\Delta N_2\), as ordinary integers. Conservation gives
\[
 r+4s=0,\qquad |r|\le4.
 \tag{24}
\]
If \(s\ne0\), the only possibilities are \((r,s)=(4,-1)\) or
\((-4,1)\). Since a block has four entries and
\(N_1+N_2\le4\), either possibility forces the count pair exchange
\[
 (N_1,N_2)=(4,0)\longleftrightarrow(0,1).
\]
But a vector with exactly one nonzero coordinate \(\pm2\) cannot have
zero sum in \(\mathbb F_5\). It is not in \(V\). Therefore \(s=r=0\)
for every input. \(\square\)

No linearity, continuity, native admission or invertibility was needed.
The theorem is about this four-coordinate zero-sum difference carrier
without an additional changing account. An extra priced degree of freedom
changes the hypothesis.

### 5.2 Two blocks attain the bound inside the prepared directions

On \(V^2\), consider
\[
 X=((2,0,-2,0),(0,0,0,0)),\qquad
 Y=((1,1,-1,-1),(1,1,-1,-1)).
 \tag{25}
\]
Every individual block has zero sum, and in each block both its source
sum and memory sum vanish. Thus all blocks in (25) lie in
\(V_{\rm prep}\). Their accounts are

| State | \(N_1\) | \(N_2\) | \(E_\kappa\) |
|---|---:|---:|---:|
| \(X\) | 0 | 2 | \(2\kappa\) |
| \(Y\) | 8 | 0 | 8 |

A transition between these endpoints, with no other changing account,
conserves this family precisely when
\[
 \boxed{\kappa=4.}
 \tag{26}
\]
Exchanging the two vectors and fixing every other point is a complete
involution of \(V^2\) conserving \(E_4\). This proves mathematical
existence in two blocks, while section 5.1 excludes one. Therefore two
is the sharp minimum number of these complete difference blocks.

The prepared endpoints correspond to actual signal states in
\(\mathcal H\) relative to a fixed prepared reference: (9)--(10) allow
every pair of content differences. They do not require changing readiness,
source sum, memory sum or control data. An admitted transition is still
missing from the original native dynamics.

Two differences can share one actual reference: a full comparison has
state \((n,\rho,x_1,x_2)\) with equal \(\Gamma\) in all three cells.
The two-block bound is not a theorem that the smallest physical machine
has two, three or four parts. It counts mathematical difference blocks
under specified resource restrictions.

Choosing a transposition because (26) gives the desired value is
circular as a physical derivation. Minimality alone cannot select the
square either. For example, the one-block transposition
\[
 (2,0,-2,0)\longleftrightarrow(1,1,-1,-1)
\]
would instead select \(\kappa=2\). It conserves \(E_2\), not \(E_4\),
and does not contradict the one-block theorem.

### 5.3 Energy 8 is sharp on prepared directions; energy 6 on all \(V\)

In a prepared block \((s,t,-s,-t)\), each magnitude count is even.
For any number of these blocks, a nonzero count change preserving
\(E_4\) therefore has
\[
 |\Delta N_2|\ge2,\qquad |\Delta N_1|=4|\Delta N_2|\ge8.
\]
One endpoint has at least eight unit-class entries, so its common
\(E_4\) is at least 8. The pair (25) attains 8 with two blocks.
Consequently, for two or more prepared blocks, 8 is the exact lowest
square-account shell permitting a count-changing conversion.

The larger \(V^m\) permits an earlier shell. For \(m=2\), use
\[
 X_6=((2,-1,-1,0),0),\qquad
 Y_6=((1,1,-1,-1),(1,-1,0,0)).
 \tag{27}
\]
All blocks are zero-sum. The accounts are \(2+\kappa\) and 6; at
\(\kappa=4\) both are 6 with changed counts.

To see no smaller shell suffices, any vector in \(V\) containing a
\(\pm2\) entry needs either another magnitude-two entry, giving account
at least 8, or at least two magnitude-one entries to make the same
block's sum zero, giving account at least 6. A single additional
\(\pm1\) cannot cancel \(\pm2\) in \(\mathbb F_5\). Thus below 6 no
zero-sum block has \(N_2>0\); for a count-changing energy match some
endpoint must have \(N_2>0\). This proves the lower bound on any product.
Embedding (27) with zero extra blocks attains it for every \(m\ge2\).

The first block of \(X_6\), for example, has source sum \(2-1=1\)
and memory sum \(-1+0=-1\). Hence (27) is not a prepared same-control
witness of the kind (25). The values 6 and 8 concern different carriers.

## 6. Doubling symmetry and the global parallelogram law

### 6.1 Doubling-equivariant maps, for any number of blocks

Multiplication by 2 in \(\mathbb F_5\) exchanges the two magnitude
classes, so
\[
 N_1(2\delta)=N_2(\delta),\qquad
 N_2(2\delta)=N_1(\delta).
 \tag{28}
\]
Let \(T:V^m\to V^m\) preserve \(E_4\) everywhere and satisfy
\[
 T(2\delta)=2T(\delta)\qquad\text{for all }\delta.
 \tag{29}
\]
For a fixed input write the count changes as \(r,s\).
Square conservation at that input gives \(r+4s=0\).
Apply it also at \(2\delta\), using (28)--(29), to obtain
\[
 s+4r=0.
\]
These equations are ordinary integer equations, not equations modulo five.
Their determinant is \(-15\ne0\), hence \(r=s=0\).
Thus every \(E_\kappa\) is conserved.

No bijectivity or full linearity was required. All \(\mathbb F_5\)-linear
maps satisfy (29). An affine map preserving \(E_4\) must send zero to
zero because \(E_4\) vanishes only there, so its translation part is zero
and it too is covered. The same proof works on a declared subcarrier
closed under doubling where both hypotheses hold everywhere.

A contact required to conserve a square only on one branch does not
satisfy this theorem's hypothesis. Nor does a contact exchanging energy
with another separately priced store satisfy the stipulated isolated
\(E_4\) conservation. Those changes must be stated.

Although \(W\)'s raw formula contains \(Az\), its common-control
difference action (22) is just a permutation. It confirms this
obstruction rather than converting the two magnitude classes.

### 6.2 A global real quadratic law on the additive finite carrier is zero

Let \(Q\) be real-valued on an additive \(\mathbb F_5\) space, \(Q(0)=0\),
and require the global parallelogram identity
\[
 Q(x+y)+Q(x-y)=2Q(x)+2Q(y)\qquad\text{for all }x,y.
 \tag{30}
\]
Setting \(x=0\) gives \(Q(-y)=Q(y)\), and setting \(y=x\) gives
\(Q(2x)=4Q(x)\). Therefore \(Q(4x)=16Q(x)\). But \(4x=-x\), so
also \(Q(4x)=Q(x)\). Hence \(15Q(x)=0\) over the reals and
\[
 \boxed{Q=0.}
 \tag{31}
\]

This does not contradict \(E_4\). The latter squares chosen balanced
integer representatives, whose addition wraps at five. Even the
one-coordinate reading \(q(t)=\ell(t)^2\) has
\(q(2+2)+q(2-2)=1\), while \(2q(2)+2q(2)=16\).
It fails (30), exactly where the integer lift and modular addition differ.
An integer lift or further amplitude structure is an additional
mathematical ingredient; this observation does not derive its physical
selection or native realization.

## 7. Reference rigidity extends beyond linear contact laws

### 7.1 From prepared pistons to content differences

Take signal and reference in \(\mathcal H\) at the same \(\Gamma\).
Equations (9)--(10) imply
\[
 \delta=(-k\Delta\mu,-k\Delta\lambda,k\Delta\mu,k\Delta\lambda).
 \tag{32}
\]
For example, \(\Delta C=3k\Delta\mu\), so
\(\delta_a=3\Delta C=4k\Delta\mu=-k\Delta\mu\); the other entries
follow in the same way. Since \(k=\pm1\), the magnitude counts are
twice the corresponding counts in the content differences.

For \(m\) signal blocks and \(d=2m\) content coordinates, define
\[
 D_\kappa(x,y)=2\sum_{i=1}^d f_\kappa(x_i-y_i),
 \quad
 f_\kappa(0)=0,\ f_\kappa(\pm1)=1,\ f_\kappa(\pm2)=\kappa.
 \tag{33}
\]
This is the same relative account expressed in content coordinates.
A single physical reference with contents \(\rho\in\mathbb F_5^2\)
corresponds to the repeated vector
\[
 \mathsf D_m\rho=(\rho_1,\rho_2,\ldots,\rho_1,\rho_2)
 \in\mathbb F_5^{2m}.
 \tag{34}
\]
It is a diagonal two-dimensional subset, not an arbitrary vector in
\(\mathbb F_5^{2m}\). This matters in the next two different theorems.

### 7.2 One map preserving every pairwise square preserves every price

Suppose a single map \(F:\mathbb F_5^d\to\mathbb F_5^d\) satisfies
\[
 D_4(Fx,Fy)=D_4(x,y)\qquad\text{for every }x,y.
 \tag{35}
\]
Positivity makes it injective; finiteness makes it bijective.
The pairs at the smallest positive value \(D_4=2\) differ by
\(\pm1\) in exactly one coordinate. These are precisely the edges of
the Cartesian product of \(d\) five-cycles.

Let \(L(x,y)\) be the unweighted shortest-path distance in this graph,
and let \(c_1,c_2\) count unit and double magnitude coordinate differences.
A step changes only one coordinate by one cyclic unit, so a shortest
path has length
\[
 L=c_1+2c_2.
\]
It is attained by changing each coordinate along its shortest cycle arc.
Since \(F\) is a bijection preserving graph edges in both directions,
it preserves \(L\). At the same time
\(D_4=2c_1+8c_2\). Direct elimination gives, for every \(\kappa\),
\[
 \boxed{D_\kappa=(4-\kappa)L+(\kappa/2-1)D_4.}
 \tag{36}
\]
Thus (35) forces preservation of every \(D_\kappa\).

This argument includes arbitrary nonlinear maps satisfying (35);
no unproved classification of finite metric isometries is needed.
Its crucial assumption is **one map applied separately to both
arbitrary endpoints**. A contact that actually reads one shared
reference is a different map of a different carrier.

### 7.3 Five settings of one unchanged shared reference already suffice

There is a direct theorem on the shared-reference carrier itself.
Fix the prepared controls and \(m\) signal content pairs
\(x\in(\mathbb F_5^2)^m\). For the physical reference content \(\rho\),
write
\[
 E_\kappa(x;\rho)=D_\kappa(x,\mathsf D_m\rho).
\]
Consider a signal map \(T(x)\) that is the **same function for the
reference settings being compared** and leaves the actual reference
unchanged. It need not be linear, injective or a permutation.

For a central reference \(\rho\), set \(d=2m\) and
\[
 D=E_4(x;\rho),\qquad
 R=\sum_{j=1}^2
 \bigl(E_4(x;\rho+e_j)+E_4(x;\rho-e_j)\bigr).
 \tag{37}
\]
These five accounts determine both central magnitude counts exactly:
\[
 \boxed{N_1=\frac{4R-11D-16d}{5},\qquad
        N_2=\frac{4D-R+4d}{5}.}
 \tag{38}
\]
They are piston-difference counts, including the factor two in (32).

**Proof.** Let \(q(t)=\ell(t)^2\) and
\(S(t)=q(t+1)+q(t-1)\). Evenness reduces the pointwise identities to
three magnitude cases:

| \(t\) | \(q(t)\) | \(S(t)\) |
|---|---:|---:|
| 0 | 0 | 2 |
| \(\pm1\) | 1 | 4 |
| \(\pm2\) | 4 | 5 |

Substitution in these three rows proves on all of \(\mathbb F_5\)
\[
 \mathbf1_{\{\pm1\}}(t)=\frac{-3q(t)+4S(t)-8}{5},
 \qquad
 \mathbf1_{\{\pm2\}}(t)=\frac{2q(t)-S(t)+2}{5}.
 \tag{39}
\]
Put \(t_i=x_i-(\mathsf D_m\rho)_i\). Then \(D=2\sum_i q(t_i)\).
In the four shifted reference settings each coordinate is shifted
twice on its own reference axis and unchanged twice on the other axis.
Consequently
\[
 R=2\sum_i S(t_i)+2D.
\]
Sum (39) over the \(d\) coordinates and multiply the indicators by two,
using (32). This gives (38). \(\square\)

It follows that the entire normalized family is reconstructed by
\[
 \boxed{
 E_\kappa(x;\rho)=
 \frac{(4\kappa-11)D+(4-\kappa)R+(4\kappa-16)d}{5}.
 }
 \tag{40}
\]
If the same map \(T\) conserves the square account at
\(\rho,\rho\pm e_1,\rho\pm e_2\), its input and output have equal
\(D,R\). Therefore (38)--(40) give separate conservation of the two
central counts and of every \(E_\kappa(x;\rho)\).

Five settings are sufficient; no claim of a smallest possible reference
test set is made. The conclusion holds at each central \(\rho\) for
which these five conservation conditions hold. Requiring them at every
\(\rho\) yields a statement on all shared-reference preparations.

This is not a theorem that a physical apparatus must implement the
same signal map regardless of its reference. Nor does it permit changing
the reference afterward while pretending the apparatus has stayed in
the same preparation. It says exactly what follows if those common-map
and fixed-reference hypotheses are imposed.

### 7.4 A shell-preserving transposition fails the other-reference test

In two-signal content coordinates, let
\[
 X_c=(2,0,0,0),\qquad Y_c=(1,1,1,1)
\]
and let \(\mathsf C\) transpose them, fixing all other points.
It fixes zero, and
\[
 D_4(X_c,0)=D_4(Y_c,0)=8.
\]
Thus it preserves the square account relative to zero everywhere.
But at the other repeated reference
\[
 Z=(0,1,0,1)=\mathsf D_2(0,1)
\]
it fixes \(Z\) and gives
\[
 D_4(X_c,Z)=2(4+1+0+1)=12,\qquad
 D_4(Y_c,Z)=2(1+0+1+0)=4.
 \tag{41}
\]
Hence the same \(\mathsf C\) does not conserve the account for that
reference. Both endpoints are legitimate prepared contents at the same
controls. This is a direct distinction between one reference shell,
all shared-reference preparations under a fixed signal map, and the
all-pairs condition (35).


## 8. A complete contact that reads the actual reference

### 8.1 The full three-cell prepared carrier

Retain three actual checkpoints \(\xi_0,\xi_1,\xi_2\in\mathcal H\)
with common \(\Gamma\), and one common original counter \(n\).
The first cell is the reference. At a fixed counter the carrier has
coordinates
\[
 (\gamma,h_0,h_1,h_2),\qquad
 \gamma=(A,z,r)\in\{1,4\}^2\times\mathbb F_5,\qquad
 h_i=(\mu_i,\lambda_i)\in\mathbb F_5^2.
 \tag{42}
\]
Common \(\Gamma\) fixes common \(A,B,k\) by \(z=4A+q+r\).
Conversely, (9)--(10) reconstructs each complete checkpoint from (42).
It follows that this whole common prepared layer has
\[
 20\cdot25^3=312500
 \tag{43}
\]
states at each fixed counter. This is the union of both permitted trace
sheets, not the number of states at one prescribed synchronized trace
cut of the origin-zero history.

Write \(\rho=h_0\) for the reference's two **contents** and
\(c=(h_1,h_2)\in\mathbb F_5^4\). The actual reference checkpoint
\(\xi_0\) is still present and recoverable from \(\gamma,\rho\);
the notation does not replace it with a chosen constant.

### 8.2 A reference-controlled full involution

Let \(\mathsf C\) be the full transposition from section 7.4 and put
\(\mathsf D\rho=(\rho_1,\rho_2,\rho_1,\rho_2)\). Define
\[
 \boxed{
 \mathsf T:(n,\gamma,\rho,c)\longmapsto
 (n,\gamma,\rho,\mathsf D\rho+\mathsf C(c-\mathsf D\rho)).
 }
 \tag{44}
\]
All additions are in \(\mathbb F_5\). The counter, complete reference
and all controller data are unchanged. Equations (9)--(10) specify
every signal piston after the contact. The rule is defined on every
state in (42), including all occupied contents and the branches on
which \(\mathsf C\) does nothing.

For a fixed input let \(d_c=c-\mathsf D\rho\).
The first application sends it to \(\mathsf C(d_c)\); reference and
controls are unchanged. The second sends it back by
\(\mathsf C^2=\mathrm{id}\). Hence (44) is a full involution, with
itself as inverse on the entire declared carrier.

Its relative account is
\[
 E_\kappa=2\sum_{i=1}^4 f_\kappa((d_c)_i).
 \tag{45}
\]
The only changed relative contents are \(X_c,Y_c\), with values
\(2\kappa,8\). Every other point is fixed. It follows that
\[
 \mathsf T\text{ preserves }E_4\text{ on the entire carrier, for every
 actual reference }\rho,
 \tag{46}
\]
and conservation on its changed branch in the normalized family (45)
requires precisely \(\kappa=4\). By (32), its changed piston differences
are exactly \((-k)X\leftrightarrow(-k)Y\), with \(X,Y\) from (25).
No identification
between arbitrary content coordinates and raw piston coordinates is
being assumed.

There is no contradiction with either theorem in section 7.
The signal map in (44) depends explicitly on the actual reference.
If the reference changes, the locations of the transposed signal
contents translate with it. This is not the same signal function for
five different reference settings, and it is not one independent map
applied to both arbitrary endpoints in (35).

### 8.3 Compatibility with original continuation and with ready exchange

The common original continuation advances the one counter once and
applies its selected letter to every checkpoint. In (42) it has the form
\[
 U^{[3]}(n,\gamma,\rho,c)=
 (n+1,\upsilon_{\theta_n}(\gamma),\rho,c),
 \tag{47}
\]
where the controller update \(\upsilon\) is given by the table in
section 3.3. All content coordinates are unchanged. Since (44) reads
only contents and leaves the controls and counter fixed,
\[
 \mathsf T U^{[3]}=U^{[3]}\mathsf T.
 \tag{48}
\]
This proof does not assume a global inverse of \(U^{[3]}\).
That step retains the merging of trace sheets discussed in section 3.3;
on known preceding slices its component letter inverses remain valid.

Apply \(W\) to all three cells at once, leaving their common counter
fixed. If \(P_2\) swaps the two contents and \(P_4\) swaps them in
each of the two signal pairs, the full contact is
\[
 \mathsf W:(\rho,c)\longmapsto(P_2\rho,P_4c),
 \qquad P_4\mathsf D=\mathsf D P_2.
\]
Therefore
\[
 c-\mathsf D\rho\longmapsto P_4(c-\mathsf D\rho).
\]
This proves that \(\mathsf W\) is a full involution preserving every
\(E_\kappa\) in (45), and it commutes with \(U^{[3]}\).
It retains old contents in the corresponding source ports. No claim
that \(\mathsf T\) and \(\mathsf W\) commute with each other is needed
or made.

Thus both mathematical operations can be specified on the same complete
three-cell comparison carrier, with their inverse domains and relative
accounts explicit. This is stronger than a transposition of abstract
differences alone.

### 8.4 The permission still missing

The law (44) was **chosen using the desired \(E_4\) shell**.
Its existence proves that a joint reference-reading contact escapes the
reference-independent obstructions. It does not independently derive
the square weight. The same original \(U^{[3]}\) fixes all contents
and never supplies its nontrivial branch.

Likewise, commutation with original continuation supplies no occurrence
rule, actuation, schedule, material implementation or native gate
decomposition. Section 3.4 shows how many content permutations share
that commutation property. The declarations (12) and (44) must remain
additional transition laws until their selection and execution have
an independent source.

No extra coordinate has been hidden in their displayed maps; all
coordinates of the declared comparison apparatus are retained.
Nevertheless, the physical cost and source of executing such a chosen
law have not been supplied by merely writing a full finite permutation.
The relative account also leaves the common apparatus and reference
pricing open. These are distinct obligations.

## 9. New inputs, retained old contents and the independently priced bank

### 9.1 Repeated swapping is not a supply of independent messages

Using \(W\) twice restores the two existing contents. Further independent
messages require a source-loading or inter-cell transfer mechanism.
A complete finite mathematical extension can use \(L\) additional
five-valued content ports:
\[
 P(m,s_1,\ldots,s_L)=(s_1,\ldots,s_L,m).
 \tag{49}
\]
The first port is the fixed receiver. After successive applications it
contains \(s_1,\ldots,s_L,m\). All old contents remain in the full state;
the inverse rotates in the other direction, and \(P^{L+1}\) is the
identity on every input. A particular input with repeated contents may
have a shorter orbit; no universal orbit length \(L+1\) is asserted.

Equation (49) supplies a finite input-and-archive prescription only
when its extra ports, their independent preparation and this coupling
are admitted. Independent original \(U\) copies do not implement (49)
by themselves. An externally written new source must count the old
source content and its inverse just as an overwritten receiver must.

For one fixed new receiver content, a reversible overwrite must keep
the five possibilities of the old receiver distinguishable outside that
receiver. The existing source port in (13) has exactly that capacity.
More generally, if \(L\) independent old five-valued contents must
remain recoverable from the full state while current receiver and
other stipulated fixed data agree, there are \(5^L\) possible histories.
Injectivity requires at least \(5^L\) distinguishable environment states.
This is a cardinality argument, not a thermodynamic lower bound.
A finite environment cannot retain an indefinitely growing archive
of independent messages without a bound on retained history.

### 9.2 A complete decision rule inside the declared energy family

Suppose the rest of a proposed apparatus has an independently specified
real account \(B\). Its definition and scale are fixed without choosing
the unknown \(\kappa\). The candidate total reading is
\[
 \mathcal E_\kappa=N_1+\kappa N_2+B.
\]
Every admitted contact must then satisfy
\[
 \boxed{\Delta N_1+\kappa\Delta N_2+\Delta B=0.}
 \tag{50}
\]
Whenever \(\Delta N_2\ne0\), it yields the unique candidate
\[
 \boxed{\kappa=-\frac{\Delta N_1+\Delta B}{\Delta N_2}.}
 \tag{51}
\]
When \(\Delta N_2=0\), the residual
\(\Delta N_1+\Delta B\) must vanish independently of \(\kappa\).
Consequently:

| Admitted transition equations | Disposition of the declared family |
|---|---|
| Every \(\Delta N_2=0\) and every remaining residual is zero | The weight remains unselected. |
| Some \(\Delta N_2\ne0\), all such equations give the same admissible weight, and all zero-coefficient residuals vanish | That weight is selected within this family. |
| Two equations disagree, a zero-coefficient residual is nonzero, or the required weight is inadmissible | No reading in the declared family fits this apparatus. |

Admissibility means \(\kappa\ge0\) for a nonnegative account and
\(\kappa>0\) when positive contrast is required. The second row does
not establish completeness or uniqueness among all conceivable energy
readings; section 4.2 already displays larger invariant classes.

A first independently admitted contact may calibrate (51), and further
independently admitted contacts can reject the family. If instead one
defines \(\Delta B=-\Delta E_\kappa\) after choosing the desired weight,
every weight is given its own compensating account. That is not
selection. Nor does that prescription establish a state function on
the independently declared bank coordinates or a transition implementing it.

The common reference is a present physical state in the declared
comparison product. Summing two differences against it does not price
that reference, and changing it changes both differences at once.
Even a successful selection of \(\kappa=4\) in (45) would still leave
preparation, common motion, counter and any actuation resources to be
included in a justified full physical account.

## 10. Synthesis with the post-v103 contact program

The results above separate three tasks that must meet on one admitted
apparatus: bringing an independent new content into an already completed
receiver, retaining all old information required for the inverse, and
selecting a physical account by independently admitted transitions.
They need not happen in one microstep. None follows merely from the
other two.

The relevant branches address different parts of that problem:

| Source | What it supplies at its frozen scope | What it does not supply here |
|---|---|---|
| [#1596][common] | A declared common-carrier/interface analysis with a STOP_UNTYPED boundary. | A typed identification between the area/Weyl carrier and a funded native contact. |
| [#1605][contact] and its [energy note][phase] | Exact phase/sinus-energy distinctions, the band-diagonal \(\cos k\) relation and corrected contact/finite-time scopes. | A translation of the particle channel into these native piston differences and a priced reference/controller account. |
| [#1612][work] | An added \(K_{\rm src}\) with complete paid-record construction and the specified \(H=15\to5\) source transition. Its original integer-chain alphabet preserves \(H\) on that source class. | A word of that original alphabet executing \(K_{\rm src}\), or original-native admission. |
| [#1613][rational] | An exact audit of a separate declared rational contact and its finite effective-history boundary. | A native \(\mathbb F_5\) contact law or an identification of its rational account with the present relative one. |
| [#1615][closure] | Actual native provenance of free phases and a sufficiently fine residue reading of the entire stipulated work machine. | Admission of its paid branch from the native free image: the free reading stays at \(H=15\), while the accepted work branch has \(H=5,r_0=10\). |
| [#1617][admission] | Exact obstructions for its fixed timing/encoding attempt, alongside a native centered-block exchange benchmark. | Reusable completion or an identification of that benchmark's account with the paid source machine. |
| [#1619][relative] | An actual native one-shot record, preserved old occupied content and whole-prefix conservation against an actual reference. | New arrivals after completion or selection of one physical energy from its common-even family. |
| This note | All-future receiver noninterference; a complete ready \(W\); sharp count-changing bounds; nonlinear reference restrictions; full chosen reference-reading contact. | An independent original-native occurrence/selection law or full physical price. |

The first two files in the source manifest are direct premises for the
new algebra. The remaining files ground this comparison of interfaces
and limits; their verifiers are not executed, their owners are not taken
over, and no new status is inferred for them.

In particular, the unresolved particle channel
\[
 (0,\pi)\longrightarrow(\pi/2,\pi/2)
\]
and its candidate difference
\[
 2\sqrt{1+m^2}-2m
\]
remain on the #1605 walk/particle description. Nothing here identifies
that quantity with the integer work payment 10, the weight \(\kappa\),
or a count of balanced native differences. The exact finite ratio
\(m/\arctan m>1\) for \(m>0\) is retained; an existence-cost or entropy
interpretation is still a hypothesis. Adding the accounts or equating
their values without a common typed reading would recreate the very
interface gap under investigation.

A decisive next construction must therefore name:

| Obligation | Required concrete data |
|---|---|
| Actual admitted contact | Whole state, fixed transition and its source of permission, triggering/control data, every accepted/refused/occupied branch, and the exact inverse domain. |
| New receiver content | Independent loading or transport into a source, ready-receiver transition, preservation of old content, and the location of the following input. |
| Energy selection | A non-neutral count-changing event derived independently of the target weight, plus an independently priced account for every other changing resource. |
| Reference and common apparatus | Preparation and any movement of the actual reference, common coordinates, counter and driver; their costs cannot disappear solely by taking differences. |

The explicit \(W\) states what a ready rewrite must accomplish.
The pair (25) states the smallest prepared difference conversion capable
of distinguishing the square. Equations (38)--(40) state why a contact
that is independent of the reference cannot quietly claim such selection
while conserving the specified five reference profiles. Equation (44)
shows exactly how reading the reference can escape that prohibition,
and exactly why choosing such a rule is not yet its derivation.

The current delivery is a set of authored L1 candidate proofs and
conditional constructions. It supplies no Canon promotion, external
independent scientific review, new experimental result or physical
closure.

[claim]: https://github.com/mathorn1973/twist-j/issues/1620
[canon]: https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md
[relative]: https://github.com/mathorn1973/twist-j/blob/2135bb39d1ebb4c8c4205c0620b23bf4b36131bb/notes/C-NATIVE-RELATIVE-TRANSFER-ACCOUNT-N/PROOF.md
[admission]: https://github.com/mathorn1973/twist-j/blob/ad7c08ab67498431ca85717c1f53f0866f5c9280/probes/P-NATIVE-TWO-CELL-WORK-ADMISSION-1/PROOF.md
[closure]: https://github.com/mathorn1973/twist-j/blob/f7c55c419fc0660da2f0b2004333b01aea26032e/notes/C-SOURCE-RAMIFIED-CONTACT-CLOSURE-N/PROOF.md
[work]: https://github.com/mathorn1973/twist-j/blob/2c305c0ed36d5f99b47bd9316256d2b10bb05f3a/probes/P-FIELD-SOURCE-WORK-RECORD-1/PROOF.md
[common]: https://github.com/mathorn1973/twist-j/blob/a6d2b0d30b9d6703fffb15b187c58fa6ad71e229/notes/C-J-AREA-COMMON-CARRIER-JUNCTION-N/PROOF.md
[contact]: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/CONTACT-KINEMATICS.md
[phase]: https://github.com/mathorn1973/twist-j/blob/da39ea38df90bbf594e90a00f0532964e4e1f041/notes/C-J-PHASE-ENERGY-COMPATIBILITY-N/ENERGY.md
[rational]: https://github.com/mathorn1973/twist-j/blob/3edeb861945cfeb0203d7699cc8085df2ff7a705/probes/P-EVEN-CONTACT-3ADIC-TEST-1/PROOF.md
