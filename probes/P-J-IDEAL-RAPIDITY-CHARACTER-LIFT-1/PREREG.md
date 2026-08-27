# P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / NO FORMAL
RUN YET / CANON UNCHANGED**

Date: 2026-08-27.

This probe freezes one integral L1 arithmetic theorem package.  Its subject is
the rapidity-refined norm pushforward of ideal Moebius followed by the scalar
quadratic-character convolution.  It does not estimate a summatory function
and it does not promote any public status.  The written universal proofs below
are the proposed theorem-grade evidence; a post-pin verifier may only audit
the frozen mechanisms and finite ranges.

## Public identity, authority, and action layer

```text
probe:             P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1
public claim lock: issue #583
owner:             A. M. Thorn / delegated session 2026-08-27
branch:            probe/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1
path:              probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/
basis main:        e5cb69d8cdcaca7e6e35f10f4438365d7126be4f
canon:             Public Canon v66, tag canon-v66
CONTENT_COMMIT:    8f11ec18825aa769308132254e8de35663006a1a
CANON_SHA256:      76de4fb05f7d1aed803e581a7d470e6ed8fd63923603ebe780e91990fb0be279
CANON_BYTES:       339260
action layer:      L1 arithmetic and formal Euler-factor algebra only
layer lift:        none
authority:         none until a later sealed Canon fold
```

The basis contains two merged public predecessor probes:

- PR #582, `P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1`, merge
  `205b9347e3666aff749e7b16dafb8e9059d76cd8`, proves at L1 the prime-local
  ideal descent
  \(\mu=(N_*\mu_F)*\chi_5\), the fixed-point construction of \(\chi_5\),
  and the root-to-ideal cross-label;
- PR #579, `P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1`, merge
  `e5cb69d8cdcaca7e6e35f10f4438365d7126be4f`, proves the two-point rapidity
  shell and a **different**, rationally normalized Reynolds lift.

Those merged probes are public predecessor evidence, not new Canon authority,
and no status is inherited from them.  The authoritative Canon rows consumed
here are:

- `ARITHMETIC-RAPIDITY-DECOMPOSITION [T]`;
- `SPLIT-PRIME-RAPIDITY-CLASS [T]`;
- `SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`;
- `CYCLOTOMIC-CLASS-NUMBER-ONE [T]`, for principality of every ideal in
  \(\mathbb Q(\sqrt5)\), hence the generator-based rapidity class.

`J-RESIDUE-PERIOD [T]` is a collision-search neighbour only.  It is not used
in a definition or proof here.  The exact proposed identifiers below are new
under the issue-#583 claim lock; any collision discovered before the pin is a
STOP, not a reason to rename after execution.

## Proposed candidate rows

At most the following four rows may be offered to a later sealed fold:

```text
J-IDEAL-RAPIDITY-CHARACTER-LIFT [candidate-T]
  The integral group-ring arithmetic function bold_mu = bold_b*(chi_5[0])
  has the frozen split, inert, and ramified local factors below and
  augmentation mu.

J-RAPIDITY-TERNARY-SHELL-CENSUS [candidate-T]
  On squarefree input with a split prime divisors, bold_mu has exactly 3^a
  distinct Laurent monomials, coefficient l1 norm 3^a, and squared
  coefficient l2 norm 3^a; split prime powers at exponent at least two leave
  a nonzero refined residue whose augmentation is zero.

J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [candidate-T]
  The constant coefficient C_0 and the split-prime scalar factor O_5 have
  the frozen Euler products below and satisfy 1/zeta = C_0 O_5 in the domain
  of absolute convergence.

J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO [candidate-T]
  T(N)=sum_{n<=N} ||bold_mu(n)||_1 is at least the scalar squarefree
  absolute-value sum and hence T(N)>N/4.  Consequently the displayed direct
  coefficient-l1 triangle upper bound is not an o(N) bound.  No wider
  non-derivability claim is made.
```

This probe itself changes no Registry, Frontier, dependency, gate, workflow,
Canon, or status file.

## Falsifier first

One exact counterexample to any frozen universal statement below falsifies the
corresponding candidate row:

1. a local ideal factor, character factor, or coefficient of \(U_p(T)\)
   differs from the stated split, inert, or ramified form;
2. augmentation differs from rational Moebius for one positive integer;
3. a squarefree shell has a collision, a coefficient other than \(\pm1\),
   the wrong support or norm, or the wrong augmentation;
4. a split prime-power residue \(2-X-X^{-1}\) vanishes in the Laurent ring or
   has nonzero augmentation;
5. neutral-coefficient extraction differs from a stated local factor or from
   the closed \(C_0\) identity;
6. the prime-local or coefficientwise identity \(1/\zeta=C_0O_5\) fails;
7. the claimed direct-triangle inequality or its linear obstruction fails;
8. the integral ideal-character lift is identified with the Reynolds lift of
   PR #579, or one lift is substituted for the other in a gate.

The following are integrity STOPs rather than mathematical counterexamples:
a verifier exception, a changed pinned byte, architecture disagreement,
nonzero exit, nonempty stderr, stdout mismatch, a post-pin mechanism change,
or a scope claim outside L1 and formal Euler algebra.

## The six frozen fields

```text
EQUATION
  The local factors U_p, augmentation, squarefree ternary census, zero-class
  series C_0, split-prime factor O_5, and direct-triangle no-go in the exact
  forms proved below.

CODE
  probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/verify.py.  Python standard
  library only; exact integers, exact modular arithmetic, sparse
  exponent-vector Laurent polynomials, math.isqrt for integer roots, no
  floating-point assertion or comparison, deterministic stdout.

CARRIER
  F=Q(sqrt(5)), O_F=Z[phi], integral ideals, their L1 rapidity classes, the
  free abelian subgroup generated after one auxiliary orientation above each
  split rational prime, and its integral group ring.

SYSTEMATICS
  Local orientation choices are auxiliary.  Independent replacement
  X_p<->X_p^{-1} is a local relabelling action (C_2)^S.  The single global
  Gal(F/Q)=C_2 involution flips all pairs simultaneously and is not confused
  with that relabelling group.  Rapidity independence distinguishes Laurent
  monomials only; it supplies no summatory estimate.

THRESHOLD
  G01-G10 must pass exactly; every frozen negative control must fire through
  a production constructor; stdout must equal one committed LF
  EXPECTED.txt byte for byte; exit zero and empty stderr are required on
  x86_64 and aarch64.

LAYER
  L1 arithmetic and formal Euler-factor algebra.  No Haar or probability
  reading, Hecke character, automorphic induction, analytic continuation,
  zero statement, Mertens estimate, physical claim, or L2-L6 lift.
```

## 1. Exact carrier and the cross-labelled prime directions

Put

\[
F=\mathbb Q(\sqrt5),\qquad O_F=\mathbb Z[\varphi],\qquad
A=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

For a split prime \(p\ne5\), let \(r\) and \(1-r\) be the roots of
\(t^2-t-1\) modulo \(p\), and put

\[
\mathfrak p_r=(p,\varphi-r).
\]

In the basis \((1,\varphi)\), multiplication by \(\varphi\) is \(A\), and
\(E_t=\mathbb F_p(1,t)\) is the eigenline with eigenvalue \(t\).  On the other
hand,

\[
\mathfrak p_r/pO_F
=\ker(a+br)
=\operatorname{span}(-r,1)
=E_{1-r}=E_{-1/r}.
\]

Thus quotient-root and ideal-subspace labels are crossed.  At \(p=11\), the
roots are 4 and 8, so \(\mathfrak p_4/pO_F=E_8\), not \(E_4\).  At \(p=5\),
the repeated root is 3 and \(1-3=3\pmod5\), so the cross-label degenerates
without ambiguity.

The field has class number one.  For a nonzero integral ideal
\(\mathfrak a=(\alpha)\), define its rapidity class by

\[
r(\mathfrak a)=[\eta(\alpha)]
\in\mathbb R/(\log\varphi)\mathbb Z.
\]

Replacing \(\alpha\) by a unit multiple \(\pm\varphi^k\alpha\) changes
\(\eta\) by \(k\log\varphi\), so the class is independent of the generator.
Ideal multiplication adds these classes.  This is the only extension from
the registered prime classes to the ideal-Moebius sum used below.

Choose one prime ideal \(\mathfrak p_p\) above each split \(p\) and write

\[
X_p=[r(\mathfrak p_p)],\qquad
X_p^{-1}=[r(\bar{\mathfrak p}_p)].
\]

Conjugation exchanges the two.  For every finite split set \(S\), public
rapidity independence identifies the generated group ring with

\[
R_S=\mathbb Z[X_p^{\pm1}:p\in S].
\]

In particular it is an integral domain and its Laurent monomials have unique
exponent vectors.  No finite scan proves this input theorem; the verifier may
only consume it through that exact representation.

## 2. The integral ideal-character lift

Define the rapidity-refined ideal-Moebius norm pushforward

\[
\mathbf b(n)=
\sum_{N\mathfrak a=n}\mu_F(\mathfrak a)[r(\mathfrak a)]
\]

and the neutral scalar character function

\[
(\chi_5[0])(n)=\chi_5(n)[0].
\]

The object of this probe is the Dirichlet convolution

\[
\boxed{\boldsymbol\mu=\mathbf b*(\chi_5[0]).}
\]

Write \(T=p^{-s}\) formally.  At a split prime, the two prime ideals have
norm \(p\), rapidities \(X_p\) and \(X_p^{-1}\), and ideal-Moebius factor

\[
\mathbf B_p(T)=(1-X_pT)(1-X_p^{-1}T).
\]

Since \(\chi_5(p)=1\), its local character series is \((1-T)^{-1}\), hence

\[
\boxed{
U_p(T)=\frac{(1-X_pT)(1-X_p^{-1}T)}{1-T}.
}
\]

At an inert prime the unique prime ideal is \((p)\), of norm \(p^2\) and
rapidity zero.  Therefore \(\mathbf B_p(T)=1-T^2\), while the character
series is \((1+T)^{-1}\), and

\[
U_p(T)=\frac{1-T^2}{1+T}=1-T.
\]

At \(p=5\), the ramified prime ideal is \((\sqrt5)\), of norm 5 and rapidity
zero.  Here \(\mathbf B_5(T)=1-T\) and the character series is 1, so

\[
U_5(T)=1-T.
\]

Expanding the split factor gives

\[
\boxed{
\boldsymbol\mu(p)=[0]-[r_p]-[-r_p]
=1-X_p-X_p^{-1},
}
\]

and, for every \(k\ge2\),

\[
\boxed{
\boldsymbol\mu(p^k)=2[0]-[r_p]-[-r_p]
=2-X_p-X_p^{-1}.
}
\]

The factor is fixed by \(X_p\leftrightarrow X_p^{-1}\).  This invariance is
both global-Galois invariant and independent-local-relabeling invariant, but
the two symmetries are not identified.

## 3. Augmentation is rational Moebius

Let

\[
\varepsilon:R_S\longrightarrow\mathbb Z,
\qquad \varepsilon(X_p)=1
\]

be augmentation.  It is a ring homomorphism and commutes with Dirichlet
convolution.  At a split prime,

\[
\varepsilon U_p(T)
=\frac{(1-T)^2}{1-T}=1-T,
\]

and the inert and ramified factors already equal \(1-T\).  Unique
factorization of arithmetic Euler factors therefore gives, coefficient by
coefficient for every \(n\ge1\),

\[
\boxed{\varepsilon(\boldsymbol\mu(n))=\mu(n).}
\]

This is the oriented integral form of the merged scalar descent
\(\mu=(N_*\mu_F)*\chi_5\).  No rational Moebius value is used to define
\(\boldsymbol\mu\).

## 4. Exact ternary shell census

Let \(n\) be squarefree with \(a\) split prime divisors and \(b\) inert or
ramified prime divisors.  Multiplication of the degree-one local coefficients
gives

\[
\boxed{
\boldsymbol\mu(n)=
(-1)^b\prod_{\substack{p\mid n\\p\ \mathrm{split}}}
(1-X_p-X_p^{-1}).
}
\]

At each split prime the exponent choice is \(-1,0,+1\).  Rapidity
independence makes all resulting exponent vectors distinct.  Every
coefficient is \(\pm1\), and therefore

\[
\boxed{
|\operatorname{supp}\boldsymbol\mu(n)|
=\|\boldsymbol\mu(n)\|_1
=\|\boldsymbol\mu(n)\|_2^2
=3^a,
}
\]

while

\[
\varepsilon(\boldsymbol\mu(n))=(-1)^{a+b}=\mu(n).
\]

The \(3^a\) statement is frozen **only for squarefree input**.  At a split
prime power \(p^k\), \(k\ge2\), the coefficient
\(2-X_p-X_p^{-1}\) has support 3, coefficient \(\ell^1\) norm 4, and squared
coefficient \(\ell^2\) norm 6.  It is nonzero in the Laurent domain but has
augmentation zero.  If a global \(n\) is divisible by a split square and by
no inert or ramified square, the refined coefficient remains nonzero; an
inert or ramified square instead kills the corresponding local coefficient.

Thus scalar square-killing at a split prime is an exact cancellation of two
neutral copies against the two oriented copies, not absence of a refined
coefficient.

## 5. The zero-rapidity channel

Let \(c_0(n)\) be the coefficient of the identity Laurent monomial in
\(\boldsymbol\mu(n)\).  Free independence forces a global monomial to be
neutral exactly when its exponent at each split prime is zero.  Hence \(c_0\)
is multiplicative and its local series are

\[
\begin{array}{ll}
p\ \mathrm{split}:&
1+T+2T^2+2T^3+\cdots=\dfrac{1+T^2}{1-T},\\[6pt]
p\ \mathrm{inert}:&1-T,\\[2pt]
p=5:&1-T.
\end{array}
\]

Consequently, as an identity of formal local Euler factors and as an
absolutely convergent Euler product for \(\operatorname{Re}s>1\),

\[
\boxed{
C_0(s):=\sum_{n\ge1}\frac{c_0(n)}{n^s}
=\frac{L(s,\chi_5)L(2s,\chi_5)}{\zeta(4s)}
\frac{1-5^{-s}}{1-5^{-4s}}.
}
\]

Prime locally, with \(T=p^{-s}\), this is

\[
\frac{1-T^4}{(1-T)(1-T^2)}
=\frac{1+T^2}{1-T}
\quad(p\ \mathrm{split}),
\]

\[
\frac{1-T^4}{(1+T)(1+T^2)}=1-T
\quad(p\ \mathrm{inert}),
\]

and at \(p=5\) the correction leaves \(1-T\).  The factor
\((1-5^{-s})/(1-5^{-4s})\) corrects one local prime; its power-series
coefficient support is infinite, with local coefficients

\[
\frac{1-T}{1-T^4}
=\sum_{j\ge0}(T^{4j}-T^{4j+1}).
\]

It is therefore not called a finite-support correction.

## 6. The split-prime scalar orientation factor

Define

\[
\boxed{
O_5(s)=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}{1+p^{-2s}}.
}
\]

This factor is scalar, depends only on the set of split primes, and is
independent of every auxiliary orientation choice.  It is not a character or
a rapidity twist.  For \(\operatorname{Re}s>1\), the product is absolutely
convergent.  At a split prime,

\[
\frac{1+T^2}{1-T}\frac{(1-T)^2}{1+T^2}=1-T,
\]

while at inert primes and at 5 the \(O_5\) factor is 1 and the \(C_0\) factor
already equals \(1-T\).  Therefore, prime by prime,

\[
\boxed{\frac1{\zeta(s)}=C_0(s)O_5(s)}
\qquad(\operatorname{Re}s>1),
\]

and equivalently

\[
\boxed{
O_5(s)=
\frac{\zeta(4s)}
{\zeta(s)L(s,\chi_5)L(2s,\chi_5)}
\frac{1-5^{-4s}}{1-5^{-s}}.
}
\]

These are exact factorizations, not an analytic simplification theorem.  No
continuation, zero cancellation, or zero-free region is inferred.

## 7. The narrow termwise-triangle no-go

For every finite Laurent polynomial \(f\),

\[
|\varepsilon(f)|\le\|f\|_1.
\]

Therefore

\[
|\mu(n)|
=|\varepsilon(\boldsymbol\mu(n))|
\le\|\boldsymbol\mu(n)\|_1
\]

and the direct termwise triangle route gives only

\[
\left|\sum_{n\le N}\mu(n)\right|
\le\sum_{n\le N}\|\boldsymbol\mu(n)\|_1.
\]

The right side is bounded below by the number of squarefree integers up to
\(N\).  An elementary linear lower bound suffices: the number of
nonsquarefree integers is at most

\[
N\sum_{m=2}^{\infty}\frac1{m^2}
<N\left(\frac14+
\sum_{m=3}^{\infty}\frac1{m(m-1)}\right)
=\frac{3N}{4}.
\]

Thus more than \(N/4\) integers up to \(N\) are squarefree.  Hence this
**specific direct
coefficient-\(\ell^1\) triangle expression** is not \(o(N)\) and cannot by
itself yield a Mertens cancellation estimate.  The \(3^a\) census shows the
exact local inflation on squarefree split shells.

No claim is made about every possible use of rapidity independence, about an
\(\ell^2\) or non-diagonal argument, or about a uniform family of characters.
In particular, this probe does not assert that fixed nonzero rapidity modes
control the trivial mode.  The integer Hecke infinity-type lattice is
discrete at zero, but zero is not isolated in the full rapidity dual; large
indices can approximate the trivial evaluation on any fixed finite set.

## 8. Mandatory distinction from the Reynolds lift

The merged PR #579 defines a rational, locally normalized final Reynolds lift
with split local factor

\[
R_p(T)=1-\frac{X_p+X_p^{-1}}2T.
\]

Its normalization is unique only inside the frozen two-resolvent class.  It
is squarefree and, on squarefree input, has coefficient \(\ell^1\) norm 1.
The present integral ideal-character lift instead has

\[
U_p(T)=\frac{(1-X_pT)(1-X_p^{-1}T)}{1-T},
\]

so already at \(p\)

\[
1-X_p-X_p^{-1}
\ne-\frac{X_p+X_p^{-1}}2,
\]

and at every \(p^k\), \(k\ge2\), the present coefficient is the nonzero
\(2-X_p-X_p^{-1}\), while the Reynolds coefficient is zero.  The present
lift lies in an integral group ring, has split power tails, and has squarefree
coefficient \(\ell^1\) norm \(3^a\).  The Reynolds lift lies in a rational
group ring, is squarefree, and has squarefree coefficient \(\ell^1\) norm 1.

The two constructions share Galois/relabeling invariance and augmentation
\(\mu\), but they do not share local coefficients, support, norm, integrality,
constant term, or defining universal property.  Neither is a rename,
specialization, or proof of the other.

## Exact verifier gates

The future sealed invocation is

```text
python3 probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/verify.py
```

The accepted verifier must print exactly ten grouped gates.

### G01. Fixed-point character and cross-labelled ideal directions

For every rational prime \(p\le997\), count the fixed lines of \(A\) on
\(\mathbb P^1(\mathbb F_p)\) by exact projective normalization, derive
\(\chi_A(p)=e_p-1\), and compare it with \(\chi_5(p)\).  Check \(p=2\) and
the repeated root at \(p=5\) explicitly.  At every split prime construct the
two kernels \(a+br=0\), verify that they are the two eigenlines with the
cross-label \(r\mapsto1-r\), and verify Galois exchange.  The same-root claim
must be tested at \(p=11\).

### G02. Three independent local constructions through exponent eight

For every prime type, compare coefficients through \(T^8\) from:

1. ideal-subset enumeration, namely
   \((1-XT)(1-X^{-1}T)\), \(1-T^2\), and \(1-T\);
2. coefficientwise convolution with the actual local character series
   \((1-T)^{-1}\), \((1+T)^{-1}\), and 1;
3. the frozen closed polynomial recurrence obtained by cross-multiplying the
   displayed rational functions.

The loop must use the prime and its derived type.  It must cover split,
inert, and ramified cases rather than compare a stored answer with itself.
Verify \(X\leftrightarrow X^{-1}\) invariance and local augmentation.  The
frozen split representatives are \(\{11,19,29,31,41,59\}\); the full
prime-type census remains \(p\le997\).

### G03. Global lift and augmentation

For every \(n\le20000\), construct \(\boldsymbol\mu(n)\) both
multiplicatively from the local \(U_p\) coefficients and by global
coefficientwise convolution \(\mathbf b*(\chi_5[0])\).  Use sparse integer
exponent-vector Laurent dictionaries.  Compare augmentation with rational
Moebius computed independently by exact trial factorization, and with the
Rota recurrence on the full frozen range \(n\le20000\).  No rational Moebius
table may enter a
definition of \(\mathbf b\) or \(\boldsymbol\mu\).

### G04. Ternary squarefree census and split-square residue

Exhaust every subset of the six frozen split primes
\(\{11,19,29,31,41,59\}\), both alone and multiplied by the frozen inert and
ramified factors \(\{2,5\}\), separately and together.  Verify distinct
exponent vectors, coefficient signs, support, \(\ell^1\), squared \(\ell^2\),
and augmentation.  For each frozen split prime and exponents 2 through 8,
verify support 3, \(\ell^1=4\), \(\ell_2^2=6\), nonvanishing, and zero
augmentation.  Verify that an inert or ramified square kills the coefficient.

### G05. Neutral coefficient from the full Laurent object

For every \(n\le10000\), extract the zero exponent vector directly from the
full \(\boldsymbol\mu(n)\) dictionary and compare it with an independently
implemented multiplicative local formula.  Check local exponents 0 through 8:
split \((1,1,2,2,\ldots)\), inert and ramified \((1,-1,0,0,\ldots)\).
Augmentation before neutral extraction is forbidden.

### G06. Independent coefficient audit of the closed \(C_0\) formula

Through \(n=10000\), form the right-hand coefficients by exact Dirichlet
convolution of four independently constructed sequences:

1. \(\chi_5(n)\);
2. \(\chi_5(\sqrt n)\) on perfect squares and zero otherwise;
3. \(\mu(\sqrt[4]n)\) on perfect fourth powers and zero otherwise, with
   Moebius supplied by the exact Rota/sieve route;
4. the local 5-correction, supported with coefficient \(+1\) at
   \(5^{4j}\), coefficient \(-1\) at \(5^{4j+1}\), and zero at the other
   5-powers.

Enumerate the square and fourth-power supports sparsely by increasing integer
roots with exact multiplication and an exact integer stopping inequality; no
floating root is permitted.  This route must not call the
neutral-coefficient constructor of G05 or rebuild its local Euler factors.

### G07. The \(O_5\) factorization by two routes

First verify the split, inert, and ramified coefficient identities exactly
through exponent eight by denominator recurrence and finite series
convolution, without formal division.  Then, through
\(n=5000\), build \(O_5\) only from its split-prime local series
\((1-T)^2/(1+T^2)\), convolve its coefficients with the G05 coefficients, and
compare with independently computed rational Moebius.  Finally audit the
equivalent closed \(\zeta/L\) coefficient expression by an independent exact
Dirichlet-convolution route, including that its 5-local factor is 1 after
correction.

### G08. The narrow direct-triangle no-go

For every \(n\le5000\), verify
\(|\varepsilon(\boldsymbol\mu(n))|\le
\|\boldsymbol\mu(n)\|_1\) and the partial inequality

\[
\sum_{n\le N}\|\boldsymbol\mu(n)\|_1
\ge\sum_{n\le N}|\mu(n)|
\]

at the frozen checkpoints \(N\in\{10,100,1000,5000\}\).  Together with the
exact \(3^a\) census already audited on every G04 shell, this gate audits the
universal written
inequality; it does not test or reject \(\ell^2\), growing-mode, or
non-diagonal transfer mechanisms.

### G09. Pipeline-level negative controls

All of the following mutations must fire through the production pipeline and
report the frozen witnesses \((11,11,5,11,5,209)\):

1. collapse every rapidity variable to 1 before neutral-coefficient
   extraction; the first disagreement is \(n=11\);
2. omit the split character denominator \((1-T)\); the first split witness is
   \(p=11\);
3. omit the 5-local correction in the independent G06 route; the first
   disagreement is \(n=5\);
4. replace \(X_p^{-1}\) by a duplicate \(X_p\) inside the actual ideal-local
   constructor; the first split witness is \(p=11\);
5. send the ramified prime 5 through the inert ideal-choice branch; the
   augmentation first fails at \(n=5\);
6. identify the independent variables \(X_{11}\) and \(X_{19}\) inside
   Laurent multiplication; the support drops from 9 to 5 at \(n=209\).

The duplicate-orientation mutation must pass through the production
Laurent-multiplication pipeline.  The representation must sum repeated
exponents; a hand-built constant comparison or an early representation error
does not satisfy the control.

### G10. Reynolds separation and deterministic-source firewall

Using exact integer-scaled coefficients, compare the already public Reynolds
factor with the present integral factor and verify the frozen differences at
\(p\) and \(p^2\) for all six split representatives.  The verifier must reject
accidental substitution of one lift for the other.

In the same grouped gate, an AST call-graph and source audit must establish:
standard library only; no environment read, network, random source, clock, or
floating-point operation; no hidden call from the root-derived ideal/refined
constructors to a residue table, closed local lift, neutral/orientation
factor, or rational Moebius oracle; deterministic sorted output.  The source
audit must also reject negative integer exponents in executable power
operations.

The universal conclusions come from the written proofs, not extrapolation
from these finite bounds.  The formal time budget is 600 seconds.  The exact
success line is `VERIFY RESULT 10/10 ALL PASS`.

## Formal pin and two-architecture execution discipline

Before the immutable public pin, only static syntax and source inspection are
permitted.  No gate, breaker, expected-output generator, or partial formal
execution may run.  `PREREG.md` and the accepted `verify.py` must be committed
and pushed together on the issue-#583 branch, then read back from the remote
pin with blob identities, SHA-256 values, byte counts, and LF line endings
recorded publicly.

Only after that readback may the first accepted formal run occur.  It is run
from the repository root as

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1/verify.py
```

The accepted stdout is normalized to LF and committed once as
`EXPECTED.txt`; stderr must be empty and the exit code zero.  `RUN.md` records
the exact pin, interpreter, OS, and architecture without scientific
interpretation.  The unchanged pinned verifier must then replay on both
x86_64 and aarch64 and produce byte-identical stdout.  A mismatch is an
integrity STOP.  No threshold, equation, mechanism, negative control, or
expected byte may move after the pin; any required post-pin change consumes
this probe identity and requires a fresh successor.

Earlier incubation runs, transcripts, ZIP files, and expected outputs are
development evidence only.  None is copied into the formal record.

## Successor obligation and closure target

This probe does not decide `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`.  That
obligation closes at RH strength only if a separately declared,
non-circular mechanism derives, for every \(\delta>0\),

\[
\left|
\sum_{n\le N}\operatorname{aug}(\boldsymbol\mu(n))
\right|
=O_\delta(N^{1/2+\delta})
\]

from controlled nontrivial information on the full refined shell, without
assuming an equivalent Mertens estimate, a zero statement for \(\zeta\), or
the target bound itself.  A weaker explicitly stated cancellation rate may be
recorded as partial progress but does not close the RH-strength obligation.

The bridge must leave open at least two mathematically distinct routes:

1. a uniform growing-mode diagonal route \(h=h(N)\), with an explicit
   approximation and transfer error;
2. a non-diagonal mixing or kernel route on the full rapidity dual, with a
   controlled operator norm and reconstruction error.

Bounds for each fixed nonzero integer mode do not alone close the obligation.
No Hecke, automorphic, Selberg-Delange, physical, Haar, probability, or RH
claim is evidence for the present probe.

## Decision

```text
candidate-T rows
  only if the written all-prime/all-n proofs stand, G01-G10 pass exactly on
  both architectures, every negative control fires through the stated
  constructors, and no scope or mathematical falsifier fires.

C only
  if all finite audits pass but review finds a gap in a universal proof.

F
  if an exact counterexample to a frozen mathematical statement survives
  review.

STOP
  on a pin violation, architecture/output mismatch, collision, authority
  mismatch, Reynolds conflation, circular use of rational Moebius, or any
  analytic, physical, or RH scope drift.
```
