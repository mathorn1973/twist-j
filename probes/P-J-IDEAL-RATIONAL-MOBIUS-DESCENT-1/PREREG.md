# P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / RESULT-EXPOSED /
PROOF-FIRST / NO FORMAL RUN YET**

This probe freezes one L1 arithmetic theorem package. It isolates the
ideal-to-rational Möbius descent in the J-derived real quadratic ring. It makes
no rapidity, analytic, physical, zeta-zero, or RH claim. Earlier incubation
runs are reconnaissance only and are not public evidence.

## Public identity, authority, and action layer

    probe:             P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1
    public claim lock: issue #581
    owner:             A. M. Thorn / delegated session 2026-08-27
    branch:            probe/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1
    path:              probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1/
    basis:             Public Canon v66,
                       public main abe931d3be30b1153c8b63b0764b01f374bef39b,
                       tag canon-v66,
                       CONTENT_COMMIT 8f11ec18825aa769308132254e8de35663006a1a,
                       CANON SHA-256
                       76de4fb05f7d1aed803e581a7d470e6ed8fd63923603ebe780e91990fb0be279,
                       339260 bytes
    action layer:      L1 arithmetic only
    layer lift:        none
    authority:         none until a later sealed Canon fold

The consumed public rows are exactly:

- J-GOLDEN-BRIDGE [T], for the golden arithmetic floor;
- REGULATOR-TWO-LOG-PHI [T], for the fundamental unit \(\varphi\);
- CYCLOTOMIC-CLASS-NUMBER-ONE [T], specifically
  \(h(\mathbb Q(\sqrt5))=1\).

J-RESIDUE-PERIOD, ARITHMETIC-RAPIDITY-DECOMPOSITION, and every
SPLIT-PRIME-RAPIDITY row are neighbors only. They are not consumed here.
They belong to successor work that retains orientations.

A later reviewed Canon fold may consider the following candidate rows:

1. J-IDEAL-COUNT-QUADRATIC-CHARACTER [T candidate];
2. J-IDEAL-RATIONAL-MOBIUS-DESCENT [T candidate];
3. J-MERTENS-IDEAL-TWOSUM [T candidate].

This probe itself changes no Canon, Registry, Frontier, dependency, or gate
file and promotes no public claim.

## Falsifier first

The theorem package is falsified by one exact counterexample to any frozen
universal statement below:

1. the projective fixed-point deficit fails to equal \(\chi_5(p)\);
2. the canonical associate domain fails to represent each nonzero principal
   ideal exactly once up to sign and units;
3. the exact ideal count differs from \(1*\chi_5\);
4. ideal valuations produce a value of \(b(n)\) different from the local
   prime-ideal factor;
5. \(b*\chi_5\) differs from the rational incidence Möbius function;
6. the Dirichlet-inverse route differs from either ideal route on its frozen
   overlap;
7. the residue law for \(S_5\), or either exact Mertens two-sum, fails.

The detector must also fire every frozen production-path mutation in G07.
Failure of a negative control is a detector defect and stops the probe.

A changed pinned byte, architecture disagreement, nonzero exit, nonempty
stderr, or stdout mismatch is an integrity STOP, not a mathematical
counterexample. Thresholds and mechanisms never move after the pin.

## The six frozen fields

    EQUATION
      For F=Q(sqrt(5)), O_F=Z[phi], A=[[0,1],[1,1]],
      e_p=#Fix([A] on P^1(F_p)), chi_A(p)=e_p-1 and complete
      multiplicative extension:
          chi_A=chi_5,
          a_F=1*chi_A,
          b(n)=sum_{N(a)=n} mu_F(a),
          mu=b*chi_A,
          M(N)=sum_{a<=N} b(a) S_5(floor(N/a)).
      The displayed prime-local factors and the two residue-class forms of
      the last identity are frozen exactly as proved below.

    CODE
      probes/P-J-IDEAL-RATIONAL-MOBIUS-DESCENT-1/verify.py.
      Python standard library only; integer arithmetic and math.isqrt only;
      no floating-point or complex constants, true division, imported
      Möbius table, zeta data, environment dependence, or network access.
      Deterministic stdout; run from repository root.

    CARRIER
      O_F=Z[phi] with norm a^2+ab-b^2, its nonzero integral ideals,
      multiplication by phi on O_F/pO_F and P^1(F_p), exact root-defined
      prime-ideal valuations, and finite integer ranges:
      coefficient identities [-6,6]^4; primes p<=997 for the character;
      chi_A(n) for n<=20000; ideal enumeration n<=2000; inversion n<=3000;
      descent and trial-factor oracle n<=30000; Rota oracle n<=5000;
      S_5(m) for m<=10000; every Mertens identity for N<=5000;
      prime norm/cross-label census p<=300.

    SYSTEMATICS
      (a) mu_F is constructed only from exact prime-ideal valuations;
      (b) rational mu is forbidden as an input to a_F, b, mu_F, chi_A, or
          b*chi_A and is permitted only as two independent comparison
          oracles, Rota recurrence and isqrt trial factorization;
      (c) ideal associates are identified only by the proved unit domain,
          never by rapidity EQ and never by division x/y;
      (d) chi_A is defined dynamically at rational primes and only then
          extended completely multiplicatively; no fixed-point formula is
          asserted directly at prime powers or composite moduli;
      (e) the element route uses h(F)=1 and a proved complete coefficient
          bound, not a heuristic height window;
      (f) the all-n result is carried by the written prime-local proof; the
          finite verifier audits that proof and is not its logical source;
      (g) no identity involving zeta_F, zeta, L-functions, convergence, or
          zeros is used as an input.

    THRESHOLD
      All eight printed gates must pass exactly. Every G07 mutation must
      return its frozen first witness. stdout must equal one committed
      EXPECTED.txt byte for byte; exit zero and empty stderr are required.

    LAYER
      L1 arithmetic only. No L2 manifold, L3 boundary, L4 support, L5
      stream, L6 measure, Haar, probability, physical, Hecke, automorphic,
      analytic, zeta-zero, cancellation, or RH lift is made or consumed.

## 1. Ring arithmetic and the finite dynamical character

Put
\[
 F=\mathbb Q(\sqrt5),\qquad
 O_F=\mathbb Z[\varphi],\qquad
 \varphi^2=\varphi+1.
\]
For \(x=a+b\varphi\),
\[
 \bar x=(a+b)-b\varphi,\qquad
 N(x)=a^2+ab-b^2.
\]

Multiplication by \(\varphi\) in the basis \((1,\varphi)\) is
\[
 A=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
A finite projective point \([1:t]\) is fixed by \([A]\) exactly when
\[
 t^2-t-1=0\pmod p.
\]
The point at infinity is not fixed. Hence \(e_p\) is the number of roots of
this polynomial in \(\mathbb F_p\). Define at primes
\[
 \chi_A(p)=e_p-1
\]
and extend \(\chi_A\) completely multiplicatively.

For \(p\ne2,5\), the discriminant is 5, so
\[
 e_p=1+\left(\frac5p\right)
     =1+\left(\frac p5\right)
\]
by quadratic reciprocity. Directly, \(e_2=0\) and \(e_5=1\). Therefore
\[
 \boxed{\chi_A=\chi_5}.
\]
This is a prime-level dynamical construction followed by multiplicative
extension, not a composite-modulus fixed-point assertion.

For a root \(r\), the prime ideal
\(\mathfrak p_r=(p,\varphi-r)\) has quotient kernel
\[
 a+br=0.
\]
Thus its line in \(O_F/pO_F\) is
\(\operatorname{span}(-r,1)\), which is the \(A\)-eigenline of the
conjugate root \(1-r=-1/r\). This cross-label is load-bearing; the
same-root label is false, already at \(p=11\).

## 2. A proved exact fundamental domain for associates

Let
\[
 \sigma_+(x)=a+b\varphi,\qquad
 \sigma_-(x)=a+b(1-\varphi),\qquad
 q(x)=\frac{|\sigma_+(x)|}{|\sigma_-(x)|}.
\]
The nonzero denominator follows because the rational norm form has no
nonzero rational null vector. Multiplication by \(\varphi\) sends \(q\) to
\(\varphi^2q\). Since the public unit basis gives
\(O_F^\times=\{\pm\varphi^k:k\in\mathbb Z\}\), every unit orbit has exactly
one class modulo sign in the half-open domain
\[
 \boxed{1\le q(x)<\varphi^2}.
\]
In integer coordinates this is exactly
\[
 \boxed{b(2a+b)\ge0,\qquad a(2b-a)<0}.
\]
Indeed, the first inequality is
\(\sigma_+(x)^2\ge\sigma_-(x)^2\). The second says that
\(x\varphi^{-1}=(b-a)+a\varphi\) has embedding ratio below 1, which is
equivalent to \(q(x)<\varphi^2\).

The exact reduction steps are
\[
 (a,b)\xmapsto{\cdot\varphi}(b,a+b),\qquad
 (a,b)\xmapsto{\cdot\varphi^{-1}}(b-a,a).
\]
After entering the half-open domain, the sign is fixed by
\(a>0\), or \(a=0,b>0\). No height heuristic, finite unit window, EQ
relation, or quotient is used.

The sign normalization and the two domain inequalities sharpen the coefficient
bound. They force \(a>0\). If \(b\ge0\), then
\(0\le b<a/2\) and
\[
 n=N(x)=a^2+ab-b^2\ge a^2>b^2.
\]
If \(b<0\), the first domain inequality forces \(b\le-2a\). Writing
\(c=-b\ge2a\),
\[
 n=-N(x)=c^2+ac-a^2\ge c^2\ge a^2.
\]
Thus in both cones
\[
 \boxed{|a|,|b|\le\sqrt n}.
\]
The complete integer search bound is therefore the sharper exact bound
\[
 \boxed{B(n)=\operatorname{isqrt}(n)}.
\]
The closed boundary is load-bearing when \(n\) is a square. Completeness is
a theorem from the inequalities, not a machine assumption.

Two nonzero elements are associates exactly when their canonical
representatives agree. The independent lattice check uses the basis
\[
 (a,b)^T,\qquad(b,a+b)^T
\]
of the principal ideal \(xO_F\).

## 3. Exact ideal valuations and ideal Möbius

Because \(h(F)=1\), every nonzero integral ideal has a generator, and the
fundamental domain enumerates it once.

Let \(x=a+b\varphi\), \(n=|N(x)|\), and
\(p^e\Vert n\). Let \(m\) be the largest integer for which \(p^m\) divides
both \(a\) and \(b\), and write \(x=p^m x_0\).

- If \(p\) splits, let \(r,s\) be the two roots of
  \(t^2-t-1\). Put \(\delta=e-2m\). If \(\delta>0\), exactly one of
  \(a_0+b_0r\) and \(a_0+b_0s\) vanishes modulo \(p\); the two prime-ideal
  valuations are \((m+\delta,m)\), in the root-labelled order. If
  \(\delta=0\), they are \((m,m)\).
- If \(p\) is inert, \(pO_F\) is prime of norm \(p^2\), necessarily
  \(e=2m\), and its valuation is \(m\).
- If \(p=5\), the unique ramified prime is
  \(R=(\sqrt5)\), \(5O_F=R^2\), and \(v_R(x)=e\).

The ideal Möbius value is then defined only from these valuations:
\[
 \mu_F((x))=
 \begin{cases}
  0,&\text{some prime-ideal valuation is at least 2},\\
  (-1)^k,&\text{exactly \(k\) valuations equal 1}.
 \end{cases}
\]
Finally
\[
 \boxed{b(n)=\sum_{N\mathfrak a=n}\mu_F(\mathfrak a)}.
\]

The implementation of this route is firewalled from the residue table,
the closed local \(b\), and both rational Möbius oracles.

## 4. Universal local proof

Unique prime-ideal factorization gives
\[
 a_F(p^k)=
 \begin{cases}
  k+1,&p\text{ split},\\
  [2\mid k],&p\text{ inert},\\
  1,&p=5.
 \end{cases}
\]
Since
\[
 (1*\chi_A)(p^k)=\sum_{j=0}^k\chi_A(p)^j,
\]
the same three cases give
\[
 \boxed{a_F=1*\chi_A=1*\chi_5}.
\]

The prime-local ideal-Möbius factors are
\[
 B_p(T)=
 \begin{cases}
  (1-T)^2,&p\text{ split},\\
  1-T^2,&p\text{ inert},\\
  1-T,&p=5.
 \end{cases}
\]
The local series of \(\chi_A\) are respectively
\[
 (1-T)^{-1},\qquad(1+T)^{-1},\qquad1.
\]
Prime by prime,
\[
 B_p(T)\sum_{j\ge0}\chi_A(p)^jT^j=1-T.
\]
The right side is the local factor of the rational incidence Möbius
function. Equality of the multiplicative coefficients proves
\[
 \boxed{\mu=b*\chi_A=b*\chi_5}
\]
for every positive integer. No zeta or \(L\)-function identity is used.

## 5. The Mertens two-sum

Let
\[
 S_5(m)=\sum_{d\le m}\chi_5(d).
\]
One period gives, according to \(m\bmod5=0,1,2,3,4\),
\[
 S_5(m)=0,1,0,-1,0.
\]
Summing the descent identity over \(n\le N\) yields
\[
 \boxed{
 M(N)=\sum_{a\le N}b(a)
 S_5\!\left(\left\lfloor\frac Na\right\rfloor\right)}.
\]
Equivalently,
\[
 \boxed{
 M(N)=
 \sum_{\substack{a\le N\\\lfloor N/a\rfloor\equiv1\ (5)}}b(a)
 -
 \sum_{\substack{a\le N\\\lfloor N/a\rfloor\equiv3\ (5)}}b(a)}.
\]

## 6. Frozen exact gates

### G01 — golden ring and dynamic character

For every \(a,b,c,d\in[-6,6]\), verify exact ring multiplication,
conjugation, and norm multiplicativity. For every prime \(p\le997\), compare
the normalized projective fixed-line census, the root census, and
\(1+\chi_5(p)\). Extend only the prime deficits multiplicatively and compare
\(\chi_A(n)=\chi_5(n)\) for every \(n\le20000\).

### G02 — canonical ideals and valuation Möbius

In the one complete box
\[
 |a|,|b|\le\operatorname{isqrt}(2000)=44,
\]
enumerate the sign-normalized fundamental-domain representatives with
\(1\le|N(x)|\le2000\). Audit canonical idempotence, unit invariance, and
agreement with equality of the principal-ideal lattices. Construct
\(\mu_F\) only from the frozen root-defined valuations. For every
\(n\le2000\), require
\[
 a_F^{\rm enum}(n)=\sum_{d\mid n}\chi_5(d),\qquad
 b^{\rm enum}(n)=b^{\rm local}(n).
\]

### G03 — rational descent

For every \(n\le30000\), require
\[
 (b^{\rm state}*\chi_A)(n)=\mu_{\rm trial}(n),
\]
where \(b^{\rm state}\) enumerates the local prime-ideal valuation states
and is separately required to equal \(b^{\rm local}\) on the same range.
The trial oracle uses exact factorization with math.isqrt. On
\(n\le5000\), also require equality with the independent Rota recurrence
\(\sum_{d\mid n}\mu_{\rm Rota}(d)=[n=1]\).

### G04 — independent Dirichlet inversion

Build \(a_F=1*\chi_5\) and its Dirichlet inverse without calling either
\(b\) route. Require
\[
 b^{\rm inv}=b^{\rm local}\quad(n\le3000),
\]
and compare with the enumerated ideal route only on the declared overlap
\(n\le2000\).

### G05 — residue law and both summatory readings

Require the direct and residue-law values of \(S_5(m)\) to agree for every
\(m\le10000\). For every \(N\le5000\), compare the cumulative Rota Mertens
sum with both displayed ideal two-sums.

### G06 — prime norm census and cross-label

For every prime \(p\le300\), use only the roots of
\(t^2-t-1\) and a complete search with
\(B(p)=\operatorname{isqrt}(p)\). Require two norm-\(p\) ideal classes in
the split case, none in the inert case, and one at \(p=5\). For every split
root, verify that \(\operatorname{span}(-r,1)\) has eigenvalue \(1-r\);
the same-root label must fail at \(p=11\).

### G07 — production-path negative controls

Every mutation must run through the same constructors used by the positive
gates and return the frozen first witness:

1. replacing \(\chi_5\) by the principal character modulo 5 breaks descent
   first at \(n=2\);
2. treating the inert prime 2 as split breaks the ideal/local \(b\)
   comparison at \(n=2\);
3. omitting the ramified local factor breaks the ideal-count comparison
   first at \(n=5\);
4. sign-only deduplication, with no unit reduction, overcounts first at
   \(n=1\);
5. the equal-norm pair \(u=3+\varphi\), \(v=1-3\varphi\) is not associate;
   the exact numerator of \(u/v\) is \(3-10\varphi\), not divisible by 11,
   but the verifier must decide nonassociateness without division;
6. replacing the closed bound \(B(n)=\operatorname{isqrt}(n)\), for
   \(n\ge2\), by \(\operatorname{isqrt}(n)-1\) first misses the
   boundary class \((2)\) at \(n=4\), represented by \(2+0\varphi\).

A hard-coded inequality or constant-vs-constant comparison does not count.

### G08 — exact-source and construction firewalls

Parse the verifier AST. Reject float or complex constants, true division,
calls to float, complex, round, square-root functions other than isqrt,
logarithms, exponentials, dynamic import, eval/exec, environment access, or
non-whitelisted imports. Reject a negative integer exponent. Verify by AST
call inspection that the element/valuation route cannot call the residue
character, local \(b\), or either rational Möbius oracle.

## 7. Formal execution protocol

Before any formal gate execution, commit and push exactly this PREREG.md and
the accepted verify.py. Record the full commit and both file SHA-256 values
on issue #581. Compilation and static AST inspection are allowed before the
pin; the scientific gates are not.

After the public pin, use a clean readback of that exact commit and run from
the repository root with deterministic locale, timezone, hash seed, and
bytecode disabled. Accept only exit code zero, empty stderr, and one exact
stdout. Commit that stdout as LF EXPECTED.txt together with neutral RUN.md
and RESULT.md. The pull request must change only this probe directory and
must pass byte-identically on GitHub-hosted x86_64 and aarch64 Python 3.12.

If the pinned run does not complete, the identifier is abandoned under
POLICY.md and cannot be repaired or reused. No post-pin edit, amend, rebase,
squash, or force-push is permitted.

## 8. Explicit exclusions and successors

This probe does not preserve the identities of the two split prime ideals,
their rapidities, or their Galois orientations. It does not construct the
integral \(3^a\) shell, the normalized Reynolds lift of public PR #579, a
Hecke character, a trivial-character transfer, or any cancellation bound.

The normalized two-point Reynolds lift in PR #579 and the future integral
ideal-character lift are distinct objects: they have different local
coefficients, supports, norms, and integrality. A successor must use a fresh
identifier, consume the merged descent by name or carry equally strong ideal
gates, and state that distinction explicitly. The suggested public order is

\[
 \text{ideal-rational descent}
 \longrightarrow
 \text{Galois-equivariant integral shell}
 \longrightarrow
 \text{trivial-rapidity evaluation bridge [O]}.
\]
