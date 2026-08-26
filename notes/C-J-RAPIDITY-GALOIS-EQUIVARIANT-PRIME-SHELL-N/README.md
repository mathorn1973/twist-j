# J rapidity and the Galois-equivariant prime shell

~~~text
STATUS:                    NON-CANONICAL / SYNTHESIS NOTE / NO STATUS PROMOTION
AUTHORITY:                 Public Canon v66 remains unchanged
PUBLIC BASE:               abe931d3be30b1153c8b63b0764b01f374bef39b
PUBLIC CONTENT COMMIT:     8f11ec18825aa769308132254e8de35663006a1a
PUBLIC CANON SHA-256:      76de4fb05f7d1aed803e581a7d470e6ed8fd63923603ebe780e91990fb0be279
DATE:                      2026-08-26
COMPANION CLAIM LOCK:      issue #578
COMPANION FORMAL PROBE:    PR #579, public replay PASS (x86_64 + aarch64), OPEN
FORMAL RUN FOR THIS NOTE:  NONE
CANON / REGISTRY CHANGE:   NONE
~~~

## 0. Decision

The useful outcome of this branch is not an RH proof. It is a sharper division
of the problem into four layers that should no longer be conflated:

1. the rank-two congruence carrier recovers the gcd-squared Gram,
   divisibility, Möbius inversion, the Mertens value at one point, and the
   Jordan character-shell multiplicities;
2. finite multiplication by \(\varphi\) recovers the splitting character
   \(\chi_5\) and identifies the two split fixed lines with the two prime-ideal
   directions;
3. the Galois-equivariant rapidity shell preserves those two directions before
   scalar descent and admits an exact group-ring Möbius lift;
4. no result obtained so far transfers estimates from the nontrivial oriented
   modes to the trivial character carrying \(M(N)\).

The strongest closed algebraic part is isolated in the companion public probe
[P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1, PR
#579](https://github.com/mathorn1973/twist-j/pull/579), locked by [issue
#578](https://github.com/mathorn1973/twist-j/issues/578). This Note records the
larger synthesis, the failed routes, the analytic candidate-D interface, and
the corrected open problem. It is not evidence for a Canon status move.

The resulting synthesis frontier (not a public Frontier row) is

\[
\boxed{\texttt{J-RAPIDITY-TRIVIAL-CHARACTER-TRANSFER}.}
\]

It explicitly permits two routes: a uniform growing-mode route
\(h=h(x)\to\infty\), and a genuinely non-diagonal transfer operator. Current
work does not prove that the second route is necessary.

## 1. Public inputs and the corrected support statement

The public authority is [Public Canon
v66](../../canon/CANON.md), not this Note and not PR #579. The inputs used here
are already registered:

- \(\varphi\) is on the J-derived real floor;
- [J-RESIDUE-PERIOD
  [T]](../../probes/P-J-RESIDUE-PERIOD-1/RESULT.md) owns
  \(\operatorname{ord}_m(\varphi)\) as the Pisano period in rational
  congruence quotients;
- [SPLIT-PRIME-RAPIDITY-CLASS
  [T]](../../probes/P-ARITH-RAPIDITY-1/RESULT.md) owns the unordered class
  \(\{r_p,-r_p\}\);
- [SPLIT-PRIME-RAPIDITY-INDEPENDENCE
  [T]](../../probes/P-SPLIT-PRIME-INDEPENDENCE-1/RESULT.md) owns the
  integer independence of any oriented finite family of split-prime classes.

The corrected statement about prime support is therefore:

\[
\boxed{\text{the dynamic channels selected so far have restricted support,}}
\]

but

\[
\boxed{O_F=\mathbb Z[\varphi]\text{ has scalar congruence reductions at every
rational prime.}}
\]

For \(p\ne5\), the reduction distinguishes split and inert primes by
\(\chi_5(p)\); \(p=5\) is ramified. The public rapidity channel sees the
split-prime directions and sends inert primes to the zero class. The scalar
congruence carrier does not lose the inert primes.

This is a statement about consequences of the J-derived real floor. It is not
a derivation or justification of the primitive J axiom.

## 2. The rank-two congruence carrier

This section records an elementary candidate-T package that is not part of the
formal scope of PR #579.

Let

\[
F=\mathbb Q(\sqrt5),\qquad O_F=\mathbb Z[\varphi],\qquad
Q_N=\operatorname{lcm}(1,\ldots,N)
\]

and define

\[
X_N=O_F/Q_NO_F,\qquad H_d=dO_F/Q_NO_F\quad(d\le N).
\]

Since \(O_F\) has rank two over \(\mathbb Z\),

\[
|X_N|=Q_N^2,\qquad |H_d|=(Q_N/d)^2,
\]

and, because every \(d\le N\) divides \(Q_N\),

\[
H_m\cap H_n=H_{\operatorname{lcm}(m,n)}.
\]

With normalized counting inner product and

\[
v_n=n\,\mathbf1_{H_n},
\]

one obtains exactly

\[
\langle v_m,v_n\rangle_N
=\frac{mn}{Q_N^2}|H_m\cap H_n|
=\frac{\gcd(m,n)^2}{mn}.
\]

Thus the Bernoulli-clock factor \(1/12\) is not part of the divisibility
geometry. It is the normalization of that particular observable.

Divisibility is intrinsic twice:

\[
d\mid n\iff H_n\subseteq H_d
\]

and

\[
d\mid n\iff n\langle v_d,v_n\rangle_N=d.
\]

Once this incidence relation is present, the Möbius function is the unique
integer function satisfying

\[
\sum_{d\mid n}\mu(d)=[n=1].
\]

It need not be supplied as a table.

### 2.1 One function, two exact scalar readings

Define

\[
F_N(x)=\sum_{d\le N}\mu(d)\mathbf1_{H_d}(x).
\]

The distinguished point belongs to every congruence subgroup, hence

\[
\boxed{F_N(0)=M(N).}
\]

The normalized global mean is

\[
\boxed{\operatorname{Avg}_{X_N}F_N
=\sum_{d\le N}\frac{\mu(d)}{d^2}.}
\]

In the incubation notation this is \(C^\sharp(N)/N^2\). The exact identity is
recorded here; this Note does not import or re-prove any claimed
RH-equivalence for a remainder term of \(C^\sharp\).

The conceptual split is already sharp: the global mean has an ordinary density
limit. In finite \(X_N\), the point \(0\) has normalized mass \(Q_N^{-2}\);
it becomes Haar-null only in the profinite limit. The hard summatory
information is concentrated at this distinguished shrinking-mass point.

### 2.2 Jordan shells are literal character multiplicities

The dual group is

\[
\widehat X_N\cong(\mathbb Z/Q_N\mathbb Z)^2.
\]

The number of characters of exact order \(q\mid Q_N\) is

\[
\#\{\chi:\operatorname{ord}\chi=q\}
=J_2(q)=q^2\prod_{p\mid q}(1-p^{-2}).
\]

For the normalized Fourier transform, every character of exact order \(q\)
has the same coefficient

\[
\widehat F_N(q)
=\sum_{\substack{d\le N\\q\mid d}}\frac{\mu(d)}{d^2}.
\]

Fourier inversion at zero gives

\[
F_N(0)
=\sum_{q\mid Q_N}J_2(q)\widehat F_N(q)
=\sum_{d\le N}\frac{\mu(d)}{d^2}\sum_{q\mid d}J_2(q)
=M(N),
\]

because \(\sum_{q\mid d}J_2(q)=d^2\). Therefore the standard factorization

\[
[\gcd(m,n)^2]
=A\,\operatorname{diag}(J_2)\,A^T
\]

has a concrete spectral meaning: \(J_2(q)\) is the multiplicity of the
order-\(q\) character shell on the rank-two congruence carrier.

The density

\[
\prod_p(1-p^{-2})=\zeta(2)^{-1}=6/\pi^2
\]

is correspondingly the density of points of the rank-two lattice not divisible
by any rational prime. This is classical lattice arithmetic, not a new J
theorem and not a cancellation mechanism.

## 3. What finite \(\varphi\)-dynamics adds

On

\[
V_p=O_F/pO_F\cong\mathbb F_p^2,
\]

multiplication by \(\varphi\) is represented in the basis
\((1,\varphi)\) by

\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad \chi_A(T)=T^2-T-1.
\]

The discriminant is five, so the orbit structure detects all three local
types.

- If \(p\equiv\pm2\pmod5\), \(V_p\) is the field \(\mathbb F_{p^2}\) and
  every nonzero point has period \(\operatorname{ord}_p(\varphi)\).
- If \(p\equiv\pm1\pmod5\), there are two eigenlines \(E_r,E_s\).
  Their nonzero sectors have sizes \(p-1,p-1\), and the generic sector has
  size \((p-1)^2\). Their periods are respectively
  \(\operatorname{ord}(r)\), \(\operatorname{ord}(s)\), and their lcm.
- At \(p=5\), the 24 nonzero points split as one orbit of length four and one
  orbit of length twenty.

These orbit facts explain the arithmetic structure of a Jordan shell. They do
not yet explain cancellation.

### 3.1 The splitting character is a fixed-point deficit

Let

\[
e_p=\#\operatorname{Fix}\bigl([A]:\mathbb P^1(\mathbb F_p)
\longrightarrow\mathbb P^1(\mathbb F_p)\bigr).
\]

A finite point \([1:t]\) is fixed exactly when

\[
t^2-t-1=0\pmod p.
\]

The point at infinity is not fixed. Hence

\[
e_p=
\begin{cases}
2,&p\equiv\pm1\pmod5,\\
0,&p\equiv\pm2\pmod5,\\
1,&p=5,
\end{cases}
\]

and therefore

\[
\boxed{\chi_5(p)=e_p-1.}
\]

This remains correct at \(p=2\). The splitting character is thus produced by
finite \(\varphi\)-dynamics; no residue lookup table modulo five is required.

### 3.2 The fixed lines are the prime-ideal directions

For a split prime \(p\ne5\) and a root \(t^2-t-1=0\pmod p\), write

\[
\mathfrak p_a=(p,\varphi-a).
\]

The exact identification is cross-labelled:

\[
\boxed{E_t=\mathbb F_p(1,t)=\mathfrak p_{1-t}/pO_F.}
\]

The same-root label is false; \(p=11\) gives the smallest mandatory breaker.
Consequently the two projective fixed points, the two prime ideals above \(p\),
and the public rapidity pair are one equivariant two-point object:

\[
\{E_t,E_{1-t}\}
\longleftrightarrow
\{\mathfrak p_{1-t},\mathfrak p_t\}
\longleftrightarrow
\{r_p,-r_p\}.
\]

Scalar descent uses only the number \(e_p\). The rapidity shell preserves the
identity of the two branches before that collapse.

### 3.3 Exact ideal-Möbius join

Let \(\mu_F\) be the ideal Möbius function and

\[
b(n)=\sum_{N\mathfrak a=n}\mu_F(\mathfrak a).
\]

Extend \(\chi_A(p)=e_p-1\) completely multiplicatively, with
\(\chi_A(5)=0\). Then \(\chi_A=\chi_5\) and

\[
\boxed{\mu=b*\chi_A.}
\]

The identity is already visible prime by prime:

| rational prime | ideal-Möbius local series | \(\chi_A\) local series | product |
|---|---:|---:|---:|
| split | \((1-T)^2\) | \((1-T)^{-1}\) | \(1-T\) |
| inert | \(1-T^2\) | \((1+T)^{-1}\) | \(1-T\) |
| ramified \(p=5\) | \(1-T\) | \(1\) | \(1-T\) |

Thus the scalar Möbius function decomposes into two different J-derived
readings:

\[
\text{ideal incidence}\longrightarrow b,
\qquad
\text{finite }\varphi\text{-dynamics}\longrightarrow\chi_5,
\qquad
b*\chi_5=\mu.
\]

This is elementary candidate-T mathematics in this Note. It has not been
promoted by a public probe or Canon fold.

## 4. Why route (i) still does not produce cancellation

Every scalar congruence subgroup is invariant under the unit:

\[
\varphi H_d=H_d.
\]

Therefore

\[
\boxed{F_N(\varphi x)=F_N(x).}
\]

Equivalently, \(\widehat F_N\) is constant on every dual
\(\varphi\)-orbit. In a cyclic Koopman basis on an orbit of length \(\ell\),
only the invariant mode \(k=0\) survives. At \(x=0\), every character equals
one, so the entire orbit contributes only

\[
\ell\,\widehat F_N(q).
\]

There is no phase cancellation. Finite \(\varphi\)-orbits identify the local
arithmetic of the shell but do not explain Möbius cancellation for this
observable.

This no-go is exact and narrow. It does not say that all finite
\(\varphi\)-dynamics is useless; it says that the invariant scalar \(F_N\)
cannot acquire cancellation merely by changing to the orbit basis.

## 5. The Galois-equivariant oriented shell

The companion public probe retains the split pair before scalarization. With
one temporary orientation above each split prime, let \(u_p\) denote the
corresponding formal rapidity generator and let \(u_p^*=u_p^{-1}\).

The local two-point shell is

\[
\mathscr S_p=
\{(E_t,\mathfrak p_{1-t},r_{\mathfrak p_{1-t}},2t-1):
t\in\mathbb F_p,\ t^2-t-1=0\},
\]

with branch exchange acting simultaneously on every component.

### 5.1 There is one local odd direction

On the two fixed lines the odd subspace is

\[
B_p^-=\mathbb F_p(2t-1),\qquad(2t-1)^2=5.
\]

It is an odd subspace or sign module, not an odd algebra: odd times odd is
even. Wedge, tangent multiplier, Lefschetz, and \(2A-I\) readings supply no
second independent local odd direction.

As a \(\mathbb Z[C_2]\)-module, the integral two-point permutation
module is the non-split extension

\[
0\longrightarrow\mathbb Z_{\rm sgn}
\longrightarrow
\mathbb Ze_{\mathfrak p}\oplus\mathbb Ze_{\bar{\mathfrak p}}
\longrightarrow\mathbb Z_{\rm triv}
\longrightarrow0.
\]

The sum/difference lattice has index two. A normalized invariant local lift
therefore requires \(1/2\).

### 5.2 The frozen Reynolds lift

Only in the explicitly frozen two-resolvent class, invariance and normalized
augmentation force

\[
\widetilde C_p(T)=
\frac12\left((1-u_pT)^{-1}+(1-u_p^{-1}T)^{-1}\right).
\]

Then

\[
(1-u_pT)(1-u_p^{-1}T)\widetilde C_p(T)
=1-\frac{u_p+u_p^{-1}}2T.
\]

No uniqueness among all symmetric formal series is claimed.

The ordinary scalar correction \((1-T)^{-1}\) fails before augmentation.
Relative to the scalar squarefree target \(1-T\), the exact identity is

\[
\frac{(1-u_pT)(1-u_p^{-1}T)}{1-T}
=(1-T)+(2-u_p-u_p^{-1})\frac{T}{1-T}.
\]

Thus the second summand is a nonzero tail.

### 5.3 The squarefree group-ring Möbius lift

For squarefree \(n\), let \(S(n)\) be its set of split prime divisors. The
oriented lift is

\[
\widetilde\mu(n)=
\frac{\mu(n)}{2^{|S(n)|}}
\sum_{\varepsilon_p=\pm1}
\prod_{p\in S(n)}u_p^{\varepsilon_p},
\]

and it is zero for nonsquarefree \(n\). It satisfies exactly

\[
\operatorname{aug}\widetilde\mu(n)=\mu(n),\qquad
\widetilde\mu(n)^*=\widetilde\mu(n),\qquad
\|\widetilde\mu(n)\|_1=|\mu(n)|.
\]

The public split-prime rapidity independence makes all
\(2^{|S(n)|}\) displayed monomials distinct. The companion probe also audits
an independent ideal-incidence plus correction convolution yielding the same
lift, so the displayed occurrence of \(\mu\) is not the only construction.

For

\[
P_N=\sum_{n\le N}\widetilde\mu(n),
\]

two exact functionals are

\[
\boxed{\operatorname{aug}P_N=M(N)}
\]

and

\[
\boxed{\operatorname{CT}P_N=
\sum_{\substack{n\le N\\n\text{ has no split prime divisor}}}\mu(n).}
\]

Here CT denotes the algebraic identity coefficient. No Haar or probabilistic
interpretation is used in this result.

### 5.4 Global Galois symmetry is not the local gauge group

The factor \(2^{-|S(n)|}\) is not forced by the single global group

\[
\operatorname{Gal}(F/\mathbb Q)\cong C_2,
\]

which reverses every chosen orientation simultaneously. For two split primes,
for example,

\[
\frac12(u_pu_q+u_p^{-1}u_q^{-1})
\]

is already globally Galois invariant.

Within the frozen local two-resolvent Euler-Reynolds class and its
orientation-cube product, the full normalization is forced by the conjunction
of

1. local Euler multiplicativity;
2. normalized Reynolds descent at each split prime;
3. invariance under independent relabelling of each split pair,

namely the local gauge action

\[
(C_2)^{S(n)}.
\]

This distinction is load-bearing.

## 6. Fired and frozen routes

The following labels are local to this Note. They do not create Registry rows.

| route | disposition | exact reason |
|---|---|---|
| \(C_\varphi=2A-I\) fixed-line census | **[F]** | \(C_\varphi\equiv I\pmod2\), so all three points of \(\mathbb P^1(\mathbb F_2)\) are fixed; use \(A\), not \(C_\varphi\), for \(\chi_5\) |
| \(\varphi\)-orbit basis for the scalar \(F_N\) | **[F]** | \(F_N(\varphi x)=F_N(x)\); only the invariant Koopman mode survives |
| J-residue orders as a universal orientation selector | **[F]** | the partial \(p=11\) success does not persist; explicit failures occur at \(p=89,281\), and the lcm passage is not multiplicative |
| a second finite local odd direction on the frozen two-point shell | **[F]** | every tested algebraic reading lies in the single line \(B_p^-\) |
| ordinary scalar correction | **[F]** | the tail \((2-u-u^{-1})T/(1-T)\) remains |
| a raw fixed nonzero Hecke-mode sum as a direct square-root surrogate for \(M(N)\) | **[F]**, conditional on the candidate-D factorization and \(G_h(1)\ne0\) | its expected summatory scale is \(x/(\log x)^{3/2}\), not square-root scale |
| “\(h=0\) is isolated in the full rapidity dual” | **[F]** | large integer modes return arbitrarily close to the trivial character on every fixed finite prime set |

The failed selector and \(C_\varphi\) routes are preserved here rather than
repaired into weaker success statements.

## 7. Candidate-D Hecke interface

This section is an analytic interpretation, not part of PR #579 and not a
public theorem.

Let

\[
\eta(\alpha)=\frac12\log
\left|\frac{\sigma_1(\alpha)}{\sigma_2(\alpha)}\right|,
\qquad L=\log\varphi.
\]

Multiplication by a unit shifts \(\eta\) by an integer multiple of \(L\).
Since \(O_F\) has class number one, the formula

\[
\Psi_h((\alpha))
=\exp\left(\frac{2\pi ih}{L}\eta(\alpha)\right),
\qquad h\in\mathbb Z,
\]

is the natural conductor-one ideal-character candidate. Its archimedean
parameter is

\[
\tau_h=\frac{\pi h}{L}.
\]

Evaluation on the group-ring shell is

\[
\operatorname{ev}_h(u_p)
=\exp(2\pi ih\,r_p/L).
\]

Put

\[
a_h(n)=\operatorname{ev}_h\widetilde\mu(n),\qquad
D_h(s)=\sum_{n\ge1}\frac{a_h(n)}{n^s}.
\]

At a split prime,

\[
D_{h,p}(s)=
1-\cos(2\pi h r_p/L)\,p^{-s};
\]

at an inert or ramified prime it is \(1-p^{-s}\).

For \(h\ne0\), standard automorphic induction of a real-quadratic Hecke
character points to a dihedral Maass cusp form \(\pi_h\). In this
conductor-one \(F=\mathbb Q(\sqrt5)\) case, the expected local conductor
calculation gives level five and nebentypus \(\chi_5\). This Note does not
prove that local calculation. A primary modern reference for the underlying
real-quadratic Hecke-to-Maass construction is Daichi Tanaka,
[Explicit Construction of Maass Wave Forms and Their Petersson Inner
Products](https://arxiv.org/abs/2601.21588).

Matching the unramified Euler factors to first order gives the candidate-D
factorization

\[
\boxed{
D_h(s)=H_h(s)
\left[
\frac{L(s,\chi_5)}
{\zeta(s)L(s,\pi_h)}
\right]^{1/2}
}
\]

with the remaining Euler product \(H_h\) expected to be holomorphic and
nonzero in a suitable half-plane. The branch, ramified factor, uniformity in
\(h\), and analytic continuation required for a theorem are not discharged
here.

For a fixed \(h\ne0\), if those hypotheses and the relevant nonvanishing at
\(s=1\) hold, Selberg-Delange predicts

\[
\sum_{n\le x}a_h(n)
=
\frac{G_h(1)}{\Gamma(-1/2)}
\frac{x}{(\log x)^{3/2}}
+o_h\left(\frac{x}{(\log x)^{3/2}}\right),
\]

where \(G_h\) is the factor left after extracting
\(\zeta(s)^{-1/2}\). Thus, when \(G_h(1)\ne0\), the raw sum at one fixed
nonzero mode has the wrong scale to serve directly as an RH-scale surrogate
for \(M(N)\). This does not exclude a renormalized remainder followed by an
additional transfer. The analytic hypotheses and the asymptotic are
candidate-D, not verifier output. A primary reference for the method is Régis
de la
Bretèche and Gérald Tenenbaum, [Remarks on the Selberg--Delange
method](https://arxiv.org/abs/2010.12929).

At \(h=0\),

\[
a_0(n)=\mu(n),\qquad D_0(s)=\zeta(s)^{-1}.
\]

The hard scalar channel is precisely the trivial character.

### 7.1 The corrected topology of the zero mode

Two statements must be kept separate.

In the discrete lattice of conductor-one infinity types,

\[
\tau_h=\frac{\pi h}{L},
\]

the zero parameter is separated from every nonzero parameter by the gap

\[
\frac{\pi}{L}.
\]

But it is not isolated in the pointwise topology of the rapidity dual.
SPLIT-PRIME-RAPIDITY-INDEPENDENCE gives rational independence of any finite
set \(r_{p_1}/L,\ldots,r_{p_k}/L\) together with one. Kronecker/Weyl recurrence
therefore supplies arbitrarily large integers \(h\) for which

\[
\exp(2\pi ih r_{p_j}/L)
\]

is simultaneously arbitrarily close to one for all \(j\le k\).

Consequently the fixed-\(h\) calculation supports only the narrower
conditional no-go

\[
\boxed{\text{no raw fixed nonzero mode directly supplies the RH-scale
bound for }M(N)\text{ when }G_h(1)\ne0.}
\]

It does not exclude a renormalized fixed-mode remainder, nor a diagonal
sequence \(h=h(x)\to\infty\) that approximates the trivial character on a
growing prime set.

## 8. The open transfer contract

The next question is not “do the nonzero modes exist?” They do. It is:

\[
\boxed{\text{how can estimates on oriented nontrivial modes control
the trivial character without inserting the desired cancellation?}}
\]

A valid \(\texttt{J-RAPIDITY-TRIVIAL-CHARACTER-TRANSFER}\) result must start
from the companion probe's explicitly defined oriented rapidity shell, ideal
incidence, and finite \(\varphi\)-dynamics, and must account quantitatively for every coefficient,
conductor, and approximation error. Importing RH, a zero-free statement
equivalent to RH, or \(M(N)=O(N^{1/2+\varepsilon})\) as an assumption is
circular.

### Route A: uniform growing-mode diagonal transfer

Choose nonzero integers \(h=h(N)\) such that the characters approach one on
the split-prime support relevant to \(P_N\). Two estimates are required
simultaneously:

1. a reconstruction bound
   \[
   |\operatorname{aug}P_N-\operatorname{ev}_{h(N)}P_N|
   \le E_{\rm rec}(N);
   \]
2. a mode bound uniform in the growing archimedean conductor
   \[
   |\operatorname{ev}_{h(N)}P_N|
   \le E_{\rm mode}(N,h(N)).
   \]

Success requires

\[
E_{\rm rec}+E_{\rm mode}
=O_\varepsilon(N^{1/2+\varepsilon}).
\]

A recurrence theorem alone supplies no usable rate. A fixed-\(h\)
Selberg-Delange estimate is not uniform in this regime. Both the simultaneous
approximation cost and the analytic conductor growth must enter the same
inequality.

A negative theorem showing that every such recurrence forces a conductor cost
too large for the target bound would close this route without closing Route B.

### Route B: non-diagonal mode mixing

Let \(V_N\) be the span of all group-ring monomials that actually occur for
\(n\le N\). Construct a finite or absolutely summable kernel \(K_N\) over
nonzero modes and an error functional \(\mathcal E_N\) such that

\[
\operatorname{aug}f
=
\sum_{h\ne0}K_N(h)\operatorname{ev}_h f+\mathcal E_N(f)
\qquad(f\in V_N).
\]

The identity for \(P_N\) must follow from this functional identity; fitting one
numerical equality only to \(P_N\) is not admissible. A valid result must prove:

- the functional identity on all of \(V_N\), not merely pointwise convergence
  for one fixed support vector;
- finiteness or absolute summability of \(K_N\), with a declared norm strong
  enough to survive the available mode estimates;
- a uniform analytic estimate across every mode used;
- an independently constructed dual-norm bound
  \(\|\mathcal E_N\|_{V_N^*}\le\delta_N\), including an explicit consequence
  \(|\mathcal E_N(P_N)|\le E_{\rm err}(N)\);
- no augmentation or trivial-character component hidden in \(\mathcal E_N\),
  and no kernel or error functional fitted using \(P_N\) or \(M(N)\).

In particular, a useful transfer must close the joint estimate

\[
\sum_{h\ne0}|K_N(h)|E_{\rm mode}(N,h)+E_{\rm err}(N)
=O_\varepsilon(N^{1/2+\varepsilon}).
\]

Without these error conditions, the vacuous choice
\(K_N=0,\ \mathcal E_N=\operatorname{aug}\) would satisfy the displayed
identity and prove nothing.

This route may be formulated adelically or as an operator on the Hecke-mode
lattice, but the carrier alone is not evidence for cancellation. Number-field
Bost-Connes systems show that profinite, ideal, and adelic arithmetic dynamics
are natural objects; they do not supply this transfer. See Marcelo Laca,
Nadia S. Larsen, and Sergey Neshveyev, [On Bost-Connes type systems for number
fields](https://arxiv.org/abs/0710.3452).

## 9. Status map

These are synthesis labels only.

| object or statement | status in this Note | public consequence |
|---|---|---|
| rank-two congruence gcd frame and Jordan shell count | candidate-T, elementary, not formally probed here | none |
| fixed-point formula \(\chi_5(p)=e_p-1\) and \(\mu=b*\chi_5\) | candidate-T, local verifier history only | none |
| Galois-equivariant prime shell, index-two descent, frozen Reynolds lift, group-ring \(\widetilde\mu\) | candidate-T under review in public PR #579; Canon fold not performed | none yet |
| Hecke character and automorphic-induction interface | candidate-D | none |
| factorization of \(D_h\) and fixed-\(h\) Selberg-Delange asymptotic | candidate-D | none |
| failures listed in section 6 | [F] inside this Note only | no Registry row |
| \(\texttt{J-RAPIDITY-TRIVIAL-CHARACTER-TRANSFER}\) | [O] inside this Note only | no Frontier row |

## 10. Governance boundary

This Note changes no Canon text, Registry row, Frontier entry, dependency,
gate, workflow, probe, or reproduction. It contains no formal run. Its
candidate-T, candidate-D, [F], and [O] annotations are a research map, not
public statuses.

The companion probe may be merged or rejected independently. Even if merged,
it records evidence only. A later sealed Canon fold would be required to
register any theorem or frontier row.
