# P-J-IDEAL-RAPIDITY-CHARACTER-LIFT-1 result

Status: **PROVED AND AUDITED IN THE FROZEN L1 / FORMAL-EULER CLASS /
PUBLIC REPLAY PENDING / CANON UNCHANGED**

## Disposition

The result-exposed integral ideal-rapidity theorem package survives. The
written all-prime and all-integer proofs in PREREG.md are theorem-grade
candidate-T evidence at L1. The single accepted post-pin run returned 10/10
PASS, exit zero, empty stderr, and the exact 496-byte stdout committed as
EXPECTED.txt. All six production-pipeline mutations fired at their frozen
witnesses.

A later sealed Canon fold may decide whether to register:

- J-IDEAL-RAPIDITY-CHARACTER-LIFT [T];
- J-RAPIDITY-TERNARY-SHELL-CENSUS [T];
- J-ZERO-RAPIDITY-ORIENTATION-FACTORIZATION [T];
- J-RAPIDITY-TERM-WISE-TRIANGLE-NOGO [T].

This probe itself changes no public row. Public Canon v66 remains the sole
authority.

## The integral lift

Let

\[
F=\mathbb Q(\sqrt5),\qquad O_F=\mathbb Z[\varphi],
\]

and choose one of the two prime ideals above each split rational prime. Write

\[
X_p=[r_p],\qquad X_p^{-1}=[-r_p]
\]

in the integral group ring of the free abelian rapidity subgroup. Define

\[
\mathbf b(n)=
\sum_{N\mathfrak a=n}\mu_F(\mathfrak a)[r(\mathfrak a)]
\]

and

\[
\boxed{\boldsymbol\mu=\mathbf b*(\chi_5[0]).}
\]

The primary construction enumerates actual prime-ideal valuations before any
closed local factor is consulted. At a split prime it sums the valuation
choices \((i,j)\) on the two conjugate ideals with rapidity exponent \(i-j\).
At an inert prime it uses the unique norm-\(p^2\) ideal, and at 5 the unique
ramified norm-5 ideal. Thus the oriented information is retained before the
quadratic-character descent is applied.

For a split prime,

\[
\boxed{
U_p(T)=\frac{(1-X_pT)(1-X_p^{-1}T)}{1-T}.
}
\]

For an inert prime and for \(p=5\),

\[
\boxed{U_p(T)=1-T.}
\]

Consequently,

\[
\boxed{\boldsymbol\mu(p)=1-X_p-X_p^{-1}}
\]

at a split prime, while for every \(k\ge2\),

\[
\boxed{\boldsymbol\mu(p^k)=2-X_p-X_p^{-1}.}
\]

The latter coefficient is nonzero, has support 3, coefficient \(\ell^1\)
norm 4 and squared coefficient \(\ell^2\) norm 6, but its augmentation is
zero.

## Root-to-ideal cross-label

For a root \(r\) of \(t^2-t-1\) modulo a split prime, put

\[
\mathfrak p_r=(p,\varphi-r).
\]

Then

\[
\boxed{
\mathfrak p_r/pO_F
=\ker(a+br)
=E_{1-r}=E_{-1/r}.
}
\]

The quotient-root label and the eigenline label are crossed. At \(p=11\),
\(\mathfrak p_4/pO_F=E_8\), not \(E_4\). The projective fixed-line census
still gives

\[
\chi_5(p)=
\#\operatorname{Fix}([A]|\mathbb P^1(\mathbb F_p))-1.
\]

The verifier derives the prime-ideal type from this actual root census in the
primary ideal constructor; the residue character appears only in the later
descent convolution and in independent comparison routes.

## Rational Möbius is augmentation

Let \(\varepsilon(X_p)=1\). At every rational prime,

\[
\varepsilon U_p(T)=1-T.
\]

Therefore, coefficient by coefficient for every positive integer,

\[
\boxed{\varepsilon(\boldsymbol\mu(n))=\mu(n).}
\]

This is not a definition by scalar Möbius values. It is the augmentation of
the independently constructed ideal-Möbius and finite-dynamical character
join.

## Exact ternary shells

If \(n\) is squarefree with \(a\) split prime factors and \(b\) inert or
ramified prime factors, then

\[
\boldsymbol\mu(n)=
(-1)^b\prod_{\substack{p\mid n\\p\ \mathrm{split}}}
(1-X_p-X_p^{-1}).
\]

Public rapidity independence makes all exponent words in
\(\{-1,0,1\}^a\) distinct. Hence

\[
\boxed{
|\operatorname{supp}\boldsymbol\mu(n)|
=\|\boldsymbol\mu(n)\|_1
=\|\boldsymbol\mu(n)\|_2^2
=3^a,
}
\]

with every coefficient equal to \(\pm1\), and

\[
\varepsilon(\boldsymbol\mu(n))=(-1)^{a+b}=\mu(n).
\]

The theorem is squarefree-only. At split squares the refined coefficient is
not zero; scalar square-killing is exact cancellation inside augmentation.
An inert or ramified square kills the corresponding refined local factor.

## The zero-rapidity coefficient

Let \(c_0(n)\) be the coefficient of the identity Laurent monomial. Its local
series are

\[
p\ \mathrm{split}:\quad
1+T+2T^2+2T^3+\cdots=\frac{1+T^2}{1-T},
\]

and

\[
p\ \mathrm{inert}\ \text{or}\ p=5:\quad 1-T.
\]

Thus, as formal local identities and as absolutely convergent Euler products
for \(\operatorname{Re}s>1\),

\[
\boxed{
C_0(s)=
\sum_{n\ge1}\frac{c_0(n)}{n^s}
=\frac{L(s,\chi_5)L(2s,\chi_5)}{\zeta(4s)}
\frac{1-5^{-s}}{1-5^{-4s}}.
}
\]

The ramified correction has the infinite local expansion

\[
\frac{1-T}{1-T^4}
=\sum_{j\ge0}(T^{4j}-T^{4j+1});
\]

it is a one-prime Euler correction, not a finite-support term.

## The orientation factor

Define the scalar split-prime product

\[
\boxed{
O_5(s)=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}{1+p^{-2s}}.
}
\]

It depends only on the set of split primes and not on an auxiliary
orientation. It is neither a rapidity character nor a twist. Prime by prime,

\[
\boxed{\frac1{\zeta(s)}=C_0(s)O_5(s)}
\qquad(\operatorname{Re}s>1),
\]

equivalently

\[
\boxed{
O_5(s)=
\frac{\zeta(4s)}
{\zeta(s)L(s,\chi_5)L(2s,\chi_5)}
\frac{1-5^{-4s}}{1-5^{-s}}.
}
\]

The verifier audited \(C_0\) both by neutral extraction from the full Laurent
object and by an independent four-sequence Dirichlet convolution. It audited
\(O_5\) both from its split-prime Euler coefficients and from the independent
closed \(\zeta/L\) coefficient expression. Their convolution equals the Rota
Möbius sequence through the frozen range.

## Narrow termwise no-go

For every Laurent polynomial,

\[
|\varepsilon(f)|\le\|f\|_1.
\]

Therefore

\[
T(N):=\sum_{n\le N}\|\boldsymbol\mu(n)\|_1
\ge\sum_{n\le N}|\mu(n)|.
\]

The elementary squarefree union bound gives

\[
\boxed{T(N)>N/4.}
\]

Consequently the displayed direct coefficient-\(\ell^1\) triangle bound is
not an \(o(N)\) bound. This is the entire negative theorem. It says nothing
against an \(\ell^2\) argument, a growing mode \(h=h(N)\), or a non-diagonal
mode-mixing kernel.

## Reynolds separation

The normalized final Reynolds lift merged in PR #579 has split factor

\[
R_p(T)=1-\frac{X_p+X_p^{-1}}2T.
\]

It is rationally normalized, squarefree, and has squarefree coefficient
\(\ell^1\) norm 1. The present lift is integral, has the neutral term at
degree one, the nonzero split prime-power tail, and squarefree coefficient
\(\ell^1\) norm \(3^a\). They share Galois/relabeling invariance and scalar
augmentation, but not their coefficients, support, norms, integrality,
constant term, or defining universal property. Neither is a rename or
specialization of the other.

## Frozen gate readout

1. projective fixed-line character and corrected cross-label: PASS for every
   prime \(p\le997\);
2. root-derived ideal choices, local character convolution, and denominator
   recurrence: PASS through exponent 8 for every prime type;
3. global ideal-character convolution versus multiplicative \(U_p\): PASS
   for every \(n\le20000\), including Rota and trial augmentations;
4. all 64 subsets of \(\{11,19,29,31,41,59\}\), with multipliers
   \(1,2,5,10\), and every frozen split prime power through exponent 8:
   PASS for the exact \(3^a\) census and the nonzero split-square residue;
5. neutral extraction: PASS through \(n=10000\), including all local
   coefficients through exponent 8;
6. independent \(C_0\) coefficient construction: PASS through \(n=10000\);
7. local and global \(C_0O_5=1/\zeta\): PASS through exponent 8 and
   \(n=5000\);
8. direct-\(\ell^1\) inequalities: PASS at every integer through 5000 and at
   all frozen checkpoints;
9. all six pipeline mutations: FIRE at the exact witnesses
   \(11,11,5,11,5,209\);
10. Reynolds separation, deterministic Laurent serialization, LF/AST source
    rules, and ideal-construction call-graph firewall: PASS.

## Fired negative controls

All mutations entered the same constructors used by the positive gates:

1. scalarizing before neutral extraction first disagrees at \(n=11\);
2. omitting the split character denominator first disagrees at \(p=11\);
3. omitting the ramified \(C_0\) correction first disagrees at \(n=5\);
4. duplicating the two split orientations first breaks star invariance at
   \(p=11\);
5. treating the ramified prime 5 as inert breaks augmentation at \(n=5\);
6. identifying \(X_{11}=X_{19}\) collapses support from 9 to 5 at \(n=209\).

The corrected root-to-ideal cross-label is also explicitly checked at 11;
the same-root label fails there.

## Exact open boundary

The surviving successor is

```text
TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]
```

It must explain the summatory smallness of the distinguished evaluation
\(X_p\mapsto1\) directly. Independence separates channels; it does not make
their augmentation small. Fixed nonzero integer modes alone do not approach
the trivial integer mode, while the full rapidity dual still permits large
modes to approximate the trivial evaluation on any fixed finite support.

An RH-strength closure must derive, without assuming an equivalent scalar
Mertens estimate or a zeta-zero statement,

\[
\left|\sum_{n\le N}\varepsilon(\boldsymbol\mu(n))\right|
=O_\epsilon(N^{1/2+\epsilon}).
\]

Both a uniform growing-mode route and a non-diagonal kernel route remain open.

## Evidence boundary

The accepted local formal leg is arm64/aarch64, macOS 26.5.2, CPython 3.9.6.
The pull-request workflow must replay the unchanged pinned verifier on
GitHub-hosted x86_64 and aarch64 with Python 3.12 and require both outputs to
equal EXPECTED.txt byte for byte. Until that workflow passes, public replay
and the two-architecture computation gate remain pending.

No Canon, Registry, Frontier, dependency, workflow, gate, existing probe, or
Note file is changed by this probe. Public Canon v66, content commit
`8f11ec18825aa769308132254e8de35663006a1a`, SHA-256
`76de4fb05f7d1aed803e581a7d470e6ed8fd63923603ebe780e91990fb0be279`,
and 339260-byte content remain unchanged.
