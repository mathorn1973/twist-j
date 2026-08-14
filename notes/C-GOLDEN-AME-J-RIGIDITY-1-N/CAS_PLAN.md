# Exact CAS plan: `C-GOLDEN-AME-J-RIGIDITY-1-N`

Status: target-free design only.  No golden target equation was generated,
evaluated, reduced, factored, or solved in this work.  The only executed
algebra is the artificial test suite in `selftest.py`.

## 1. What must be frozen before any target computation

1. Pin the public source of the 112-entry tensor skeleton byte-for-byte.
2. Freeze the tensor-to-matrix convention and the three row/column maps for
   the bipartitions `01|23`, `02|13`, and `03|12`.
3. Freeze the normalization on the right side of each Gram equation.  It is
   `1` if the pinned object is the unitary matrix `U`, but `1/36` if the
   pinned object is the normalized four-party state.  This cannot be guessed.
4. Freeze a table mapping every coefficient tag to one of
   `q*a*x^k`, `q*b*x^k`, or `q*c*x^k`, with `q in QQ` and integer `k`.
   Negative exponents become positive powers of a separate variable `y`.
   Exponents must **not** be reduced modulo 20, and no known relation among
   `a,b,c,x` may enter the generator.
5. State explicitly whether occurrences such as the target value `i` deform
   with the common phase (`x^5`) or remain a fixed algebraic coefficient.
   That choice changes the theorem being tested and cannot be made after the
   result is seen.
6. Freeze generator normalization, variable order, monomial order, prime
   schedule, stop rules, target polynomials, and the real inequalities.

The proposed algebraic targets are

```text
f_c     = 2*c^2 - 1
f_pyth  = a^2 + b^2 - c^2
f_phi   = b^2 - a*b - a^2
f_20    = x^8 - x^6 + x^4 - x^2 + 1
```

The phase conclusion `f_20=0` selects a primitive twentieth root, but not a
particular complex embedding.  Identifying a particular oriented root needs a
separately frozen sign or isolating interval.  Defining `zeta5=x^4` is then
valid branchwise; it must not be silently identified with a preselected
embedding before that branch choice.

## 2. Exact equation generation

### Laurent algebraic envelope

Work first in

```text
R_L = QQ[a,b,c,x,y],       star(a,b,c,x,y)=(a,b,c,y,x),
```

and add `x*y-1`.  Thus `y` represents `x^-1` without negative exponents.
Build each `36 x 36` flattening `M_P` exactly from the frozen sparse table and
form

```text
G_P = M_P * star(M_P)^T - kappa*I_36.
```

Here `kappa` is the frozen rational normalization.  In the algebraic envelope
`x` and `y` are independent variables before `xy=1`; therefore use **all**
entries of `G_P`, or the upper triangle together with every star image.  Using
only one triangle would be unsound in this enlarged complex variety.  One
row-Gram equation per bipartition is enough when `kappa != 0`; column Grams
should be retained as a post-result audit, not as hidden extra generators.

For each polynomial:

1. clear rational denominators;
2. divide by integer content;
3. fix the sign by the leading term in a frozen order;
4. sort sparse monomials canonically;
5. deduplicate while retaining every `(partition,row,column)` provenance;
6. hash both the polynomial list and the provenance map.

No floating-point number is permitted in this stage.

### Exact real form

The Laurent envelope is deliberately stronger than the physical locus.  The
physical real ideal is constructed independently in

```text
R_R = QQ[a,b,c,u,v],       x=u+i*v, y=u-i*v,
```

with `u^2+v^2-1`.  Substitute into the upper triangular Gram entries and split
each into exact real and imaginary parts.  The semialgebraic branch is

```text
I_R = 0,  a>0, b>0, c>0.
```

If a target lies in the radical of the Laurent envelope, it is proved on the
physical branch automatically.  If it does not, this is not a negative
answer: the real positive branch can still force it.

## 3. Saturation and the first four exact questions

Let

```text
I0 = <x*y-1, all canonical Gram polynomials>.
I  = I0 : (a*b*c)^infinity.
```

The most portable saturation is Rabinowitsch elimination.  Introduce `s`, set

```text
K = I0 + <1-s*a*b*c>,
I = K intersect QQ[a,b,c,x,y].
```

This avoids depending on a CAS-specific `saturation` command and produces an
elimination certificate.  Saturation by `abc` must happen before radical or
component analysis; otherwise zero-amplitude components can manufacture a
false failure.

Do **not** begin with a full primary decomposition.  For each frozen target
`f` ask, in this order:

1. Does the normal form of `f` modulo a Groebner basis of `I` vanish?  If yes,
   `f in I`.
2. If not, apply the radical membership test

   ```text
   1 in I + <1-t*f>  iff  f in radical(I).
   ```

3. If that also fails, test the real positive counterexample formula

   ```text
   Exists(a,b,c,u,v): I_R and a>0 and b>0 and c>0 and f!=0.
   ```

   Exact unsatisfiability proves the target only on the intended real branch.
4. Only after a failure, decompose the responsible components or construct an
   exact positive deformation witness.

This sequence is usually much cheaper and answers the preregistered question
without computing mathematical structure that was not requested.

## 4. Coordinate systems used only as independent cross-checks

The raw `a,b,c,x,y` ideal remains primary.  Two derived coordinate systems can
make the calculation much smaller.

### Quadratic amplitude lift

Every Gram entry is quadratic in the amplitudes.  Introduce

```text
A=a^2, B=b^2, C=c^2, D=ab, E=ac, F=bc.
```

The Gram generators become linear in `A,...,F` over the Laurent phase ring.
Add all `2 x 2` minors of

```text
[ A D E ]
[ D B F ]
[ E F C ]
```

and saturate by `A*B*C`.  The targets become

```text
2*C-1,  A+B-C,  B-D-A,  Phi20(x).
```

For the real physical branch also require `A,B,C,D,E,F>0`.  The complete
minor ideal is essential; using only `D^2=AB`, etc. can add spurious complex
components.

### Ratio/scale chart

On the saturated chart `a!=0`, add

```text
b-r*a=0, c-q*a=0, A-a^2=0.
```

Then eliminate `a,b,c`.  The golden amplitude target is `r^2-r-1`; positivity
selects the unique root in `(1,2)`.  This chart is a cross-check, not a
replacement for the raw ideal.

For the phase introduce `T=x+y`.  Modulo `xy-1`,

```text
Phi20(x) = x^4 * (T^4 - 5*T^2 + 5).
```

Since `x` is invertible, the phase target is equivalently
`T^4-5*T^2+5`.  Do not impose that trace reduction on equations which have not
first been proved invariant under `x <-> y`.

## 5. Groebner, elimination, radical, and component strategy

1. Start over several finite fields with degree-reverse-lexicographic order.
   Record dimension, degree, Hilbert series, leading monomials, and phase and
   amplitude elimination degrees.
2. Over `QQ`, compute a degree-reverse-lexicographic basis first.  If the
   saturated ideal is zero-dimensional, convert to lexicographic order by
   FGLM instead of starting lex directly.
3. Eliminate to the following rings independently:

   ```text
   QQ[x]              phase eliminant
   QQ[T]              phase-trace eliminant
   QQ[A,B,C,D]        amplitude relations
   QQ[r]              positive amplitude-ratio eliminant
   ```

4. Factor every eliminant over `QQ`.  A factor containing the target is not by
   itself a proof: show which saturated components and which real isolated
   branches survive.
5. Compute `radical(I)`, minimal associated primes, or a full primary
   decomposition only if the four membership tests do not settle the claim.
   For a zero-dimensional ideal use a rational univariate representation or
   triangular decomposition.  For a positive-dimensional component compute
   its exact dimension and exhibit either a parametrization or a certified
   sample point.

An exact deformation is the correct negative certificate: give algebraic
parameters/minimal polynomials and isolating intervals, substitute them into
all Gram equations exactly, prove `abc!=0` and positivity, and prove at least
one target polynomial nonzero.

## 6. Real-root isolation

For a zero-dimensional realified ideal:

1. obtain a rational univariate representation `h(z)` plus rational functions
   for `a,b,c,u,v`;
2. squarefree-factor `h` over `QQ`;
3. isolate every real root with rational Sturm intervals or Thom encodings;
4. evaluate the signs of `a,b,c` exactly on every box;
5. retain only `a,b,c>0` and `u^2+v^2=1`;
6. evaluate all four target signs exactly.

The trace phase polynomial has four real roots, isolated for example in
`(-2,-3/2)`, `(-3/2,-1)`, `(1,3/2)`, `(3/2,2)`.  This is not yet an oriented
choice of `x`: the sign of `v` must also be fixed or reported as conjugate
branches.

If a positive-dimensional branch remains, univariate root isolation is not
enough.  Use exact cylindrical algebraic decomposition or real quantifier
elimination on the counterexample formula.  Mathematica `Reduce/Resolve`,
Maple `RegularChains[SemiAlgebraicSetTools]`, or QEPCAD are suitable independent
engines; none is present in the current sandbox.  A numerical optimizer is
diagnostic only and cannot close this gate.

## 7. Modular reconnaissance and lifting

Modular work begins only after the public pin.  Its role is discovery and
resource estimation, not final proof.

1. Clear all denominators and reject primes dividing contents, frozen
   denominators, or required leading coefficients.
2. Use a preregistered deterministic prime list (or a deterministic rule such
   as the first primes in a stated congruence class).  A congruence such as
   `p=1 mod 20` is useful for phase diagnostics but must not replace generic
   primes.
3. Across at least three good primes compare dimension, degree, Hilbert series,
   initial ideal, and eliminant degrees.  Disagreement marks an unlucky prime
   or an unstable computation.
4. Reconstruct candidate rational bases/eliminants by CRT and rational
   reconstruction only after the modular shape stabilizes.
5. Verify every reconstructed polynomial and every Groebner relation anew over
   `QQ`.  A modular match alone is never the theorem.

A single nonzero residue can prove that a *specific explicitly evaluated
integer polynomial* is nonzero, as in earlier finite-field witnesses.  It does
not by itself certify ideal nonmembership or completeness of an elimination.

## 8. Certificate bundle

The result bundle should contain:

* exact source and preregistration pins and SHA-256 manifests;
* canonical equation list plus complete Gram provenance;
* CAS names, versions, executable/container hashes, coefficient field,
  variable order, monomial order, memory/time limits, and stdout/stderr;
* saturation elimination basis;
* Groebner basis and, ideally, its transformation matrix from the input;
* exact membership identities `f=sum(q_i*g_i)`;
* for radical membership, a Nullstellensatz identity
  `1=sum(q_i*g_i)+q*(1-t*f)`, or an explicit power `f^N in I`;
* factorization multiplication checks;
* rational univariate representation, Sturm chains, isolating intervals, and
  exact sign tables for the real branch;
* two byte-identical runs and a separate exact sparse certificate verifier;
* a second engine or architecture for the decisive certificate;
* a firewall report confirming no known `phi`, `J`, `Phi20`, or target value
  entered equation construction.

A checkable Groebner certificate verifies that every output basis element is
in the input ideal and that every Buchberger S-polynomial reduces to zero.
This is stronger than trusting a CAS transcript.  Large coefficient vectors
may be compressed, but their uncompressed hashes must be pinned.

## 9. Engine choices

Recommended primary route:

1. **Singular** for sparse Groebner bases, elimination, saturation, modular
   reconnaissance, and GTZ minimal/primary decomposition.
2. **SageMath** as the exact equation/orchestration and root-isolation layer,
   while recording when Sage delegates a calculation to Singular.  Sage plus
   its bundled Singular is one engine, not two independent checks.
3. **Magma** as an independent licensed check for Groebner, saturation,
   radical, primary decomposition, and zero-dimensional solving, if a license
   is available.

Open alternatives are Macaulay2 (saturation, radical, primary decomposition),
OSCAR/Singular.jl, or CoCoA.  For a decisive equality, an independent custom
sparse verifier of the exported membership identity can replace a second
large CAS.  SymPy is acceptable only for equation-generation regression and
small examples, not as the primary engine for this ideal.

The current sandbox has none of Sage, Singular, Magma, Macaulay2, Julia/OSCAR,
CoCoA, PARI/GP, Mathematica, Maple, QEPCAD, or Z3.  It has Python 3.12, NumPy,
SciPy, and GMP/MPFR runtime libraries.  NumPy/SciPy are not exact CAS systems.
Therefore a target run here would be both technically unsuitable and contrary
to the requested preregistration firewall.

## 10. Stop/go sequence

1. Freeze and hash the sparse symbolic constructor.
2. Run only target-free structural checks: support count, flattening maps,
   star closure, equation provenance, and artificial unit tests.
3. Publish preregistration and its exact commit/tree/hash.
4. Only then verify that the known golden point satisfies the generated ideal.
   A failure is `STOP-CONSTRUCTION`, not an invitation to edit the freeze.
5. Run deterministic modular reconnaissance.
6. Run the four exact membership tests over `QQ`.
7. If necessary, isolate the real positive branch.
8. Publish the smallest decisive exact certificate and independent replay.
