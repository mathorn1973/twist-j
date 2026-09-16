# Hodge and Tate conjectures: a CM5 calibration lane for TWIST-J

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83, tag `canon-v83`. This note changes no `canon/`
file, registers no claim, starts no formal public probe, and supplies no new
physical reading.

**Date:** 2026-09-11.

## 1. Purpose

There is a concrete mathematical reason to compare TWIST-J with Hodge and
Tate theory. The native cyclotomic field

\[
K=\mathbf Q(j)=\mathbf Q(\zeta_5)
\]

is a quartic CM field, and the public Canon already contains an exact
rank-four `Z[j]` carrier together with the full two-dimensional CM pencil of
`j`-invariant integral alternating forms. The same field occurs as a complex
multiplication field of a genus-two Jacobian.

The purpose of this note is narrow:

1. identify a standard polarized CM abelian surface carrying the same
   cyclotomic algebra;
2. compare its Hodge structure with the exact public CM pencil;
3. pass to good finite-field reductions and compare Frobenius with the
   arithmetic `C4 = Gal(K/Q)` action;
4. use known Hodge and Tate results as calibration targets before asking any
   open question.

No statement here claims progress on the Hodge conjecture or the Tate
conjecture. The hard step in both problems is algebraicity of distinguished
cohomology classes. Reproducing the correct carrier or symmetry is not that
step.

## 2. The common problem behind Hodge and Tate

For a smooth projective complex variety `X`, Hodge theory gives

\[
H^k(X,\mathbf C)=\bigoplus_{p+q=k}H^{p,q}(X).
\]

A codimension-`r` algebraic cycle gives a rational cohomology class of type
`(r,r)`. The Hodge conjecture asks whether every rational `(r,r)` class is a
rational linear combination of algebraic cycle classes:

\[
CH^r(X)\otimes\mathbf Q
\longrightarrow
H^{2r}(X,\mathbf Q)\cap H^{r,r}(X).
\]

The conjecture remains open in general.

For a variety over a finitely generated field, the Tate conjecture replaces
the Hodge decomposition by the Galois action on etale cohomology. Over a
finite field, one may equivalently look for the appropriate Frobenius
eigenclasses. After the Tate twist, the target is the Galois-fixed part

\[
H^{2r}_{\mathrm{et}}
 (X_{\overline F},\mathbf Q_\ell(r))^{\Gamma_F}.
\]

Again the difficult assertion is that the distinguished cohomology classes
come from algebraic cycles.

Thus the useful schematic comparison is

```text
Hodge: complex structure  -> rational (r,r) classes -> algebraic cycles?
Tate:  Galois/Frobenius   -> invariant classes       -> algebraic cycles?
```

For an integer-first programme this makes the Tate side particularly natural,
but the two sides should be studied together in the CM setting.

## 3. Current TWIST-J anchor

Public Canon v83 already proves the exact arithmetic structure needed for a
serious comparison. Put

\[
K=\mathbf Q(j),\qquad
\mathcal O_K=\mathbf Z[j],\qquad
K^+=\mathbf Q(\sqrt5),\qquad
\mathcal O_{K^+}=\mathbf Z[\varphi].
\]

With

\[
\lambda_1=j-j^{-1},\qquad
\lambda_2=j^2-j^{-2},
\]

the anti-real lattice is

\[
L=\{\lambda\in\mathcal O_K:\bar\lambda=-\lambda\}
 =\mathbf Z\lambda_1+\mathbf Z\lambda_2
 =\lambda_1\mathbf Z[\varphi].
\]

The Canon's CM pencil is

\[
\Omega_\lambda(h,k)
 =\frac1{5}\operatorname{Tr}_{K/\mathbf Q}
   (\lambda h\bar k).
\]

Writing

\[
\lambda=a\lambda_1+b\lambda_2,
\]

the exact Pfaffian is

\[
\operatorname{Pf}(\Omega_{a,b})
 =a^2-ab-b^2
 =N_{K^+/\mathbf Q}((a-b)+b\varphi).
\]

Public Canon v83 also proves that pullback by

\[
J=1+j^2
\]

acts on the parameter lattice by

\[
A_J=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix},
\qquad
\det A_J=1,
\qquad
\operatorname{tr}A_J=3,
\]

with eigenvalues `phi^2` and `phi^-2`.

The relevant registered theorem rows include
`CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]`,
`CM-REAL-DIFFERENT-PRIMARY-SEAM [T]`,
`CM-RAMIFIED-PFAFFIAN-ROOT [T]`, and
`CM-PERIOD-LATTICE-NONSELECTION [T]`.

The last of these is an important boundary. The Canon explicitly does **not**
select a torus, manifold, homology class, polarization, period integral, or
physical geometry from the CM pencil alone. This note does not override that
boundary. It asks for an external algebraic-geometric realization and an
exact comparison.

## 4. A standard CM surface with the same fifth-root algebra

Consider the genus-two curve

\[
C:\quad y^2=x^5-1
\]

and its Jacobian

\[
A=\operatorname{Jac}(C).
\]

The order-five automorphism

\[
T:(x,y)\mapsto(jx,y)
\]

induces an action of `Z[j]` on `A` and on `H_1(A,Z)`.

A basis of holomorphic differentials is

\[
\omega_1=\frac{dx}{y},\qquad
\omega_2=\frac{x\,dx}{y}.
\]

Directly,

\[
T^*\omega_1=j\omega_1,
\qquad
T^*\omega_2=j^2\omega_2.
\]

Hence the CM type is

\[
\Phi=\{\sigma_1,\sigma_2\},
\qquad
\sigma_a(j)=j^a.
\]

Because `[K:Q]=4=2 dim A`, this is a genuine CM realization of the same
quartic cyclotomic field used by TWIST-J.

Rationally,

\[
H_1(A,\mathbf Q)
\]

is one-dimensional over `K`. Integrally it is a rank-one projective
`O_K`-module, hence a fractional ideal. For `Q(zeta_5)` the class number is
one, so after choosing a generator one may identify the lattice with
`O_K`. This generator choice is not canonical and must remain visible in any
comparison with the marked TWIST-J pencil.

## 5. Why the polarization comparison is the first exact test

The Jacobian carries its canonical principal polarization. Since `T` comes
from an automorphism of the curve, this polarization is `T`-invariant.

For a rank-one CM lattice, a compatible alternating form has the standard
trace shape

\[
E_\xi(x,y)
 =\operatorname{Tr}_{K/\mathbf Q}(\xi x\bar y),
\qquad
\bar\xi=-\xi,
\]

with an additional sign condition at the embeddings in the chosen CM type to
make it a Riemann form.

This is exactly the structural shape already present in the public TWIST-J
pencil, with `xi = lambda/5`.

Therefore the first useful question is not whether two abstract symplectic
lattices are isomorphic. In rank four that would be far too weak. The test is
simultaneous:

```text
integral lattice
+ multiplication by j
+ chosen CM type {sigma_1,sigma_2}
+ principal polarization
+ J = 1+j^2 pullback action.
```

Under an explicit `O_K`-module identification of `H_1(A,Z)` with the public
cyclotomic lattice, the canonical Jacobian polarization should be expressed
as one definite unimodular member

\[
\Omega_{a,b},
\qquad
a^2-ab-b^2=\pm1,
\]

up to the declared generator, sign, and Galois choices.

The coordinate and positivity part of this calibration can already be solved
exactly inside the public CM pencil, as follows. An explicit integral homology
basis for the Jacobian is still a separate formal gate.

## 5A. Exact CM5 polarization-coordinate calibration

In the fixed public basis `(1,j,j^2,j^3)`, Canon v83 displays

\[
\Omega_1=
\begin{pmatrix}
0&1&0&0\\
-1&0&1&0\\
0&-1&0&1\\
0&0&-1&0
\end{pmatrix},
\]

and

\[
\Omega_2=
\begin{pmatrix}
0&0&1&-1\\
0&0&0&1\\
-1&0&0&0\\
1&-1&0&0
\end{pmatrix}.
\]

The full `j`-invariant alternating family in the same basis may equivalently
be written

\[
\Omega_{e,f}=
\begin{pmatrix}
0&f&e&-e\\
-f&0&f&e\\
-e&-f&0&f\\
e&-e&-f&0
\end{pmatrix}.
\]

Comparison is coefficient-by-coefficient and requires no basis change:

\[
\boxed{\Omega_1=\Omega_{0,1}},
\qquad
\boxed{\Omega_2=\Omega_{1,0}}.
\]

Therefore for the Canon coordinates

\[
\Omega_{(a,b)}=a\Omega_1+b\Omega_2
\]

one has simply

\[
\boxed{e=b,\qquad f=a}.
\]

The Pfaffian becomes

\[
\operatorname{Pf}(\Omega_{e,f})
 =f^2-ef-e^2
 =a^2-ab-b^2,
\]

so the two parametrizations are not merely equivalent quadratic forms. They
are the same trace-form pencil in the same integral basis. In particular,

\[
\operatorname{Pf}(\Omega_1)=1,
\qquad
\operatorname{Pf}(\Omega_2)=-1,
\]

and both displayed forms are unimodular.

Now impose the CM type selected by the Jacobian,

\[
\Phi=\{\sigma_1,\sigma_2\},
\qquad
\sigma_r(j)=j^r.
\]

For

\[
\xi_{e,f}
 =\frac{f(j-j^{-1})+e(j^2-j^{-2})}{5},
\]

the two relevant imaginary parts have, up to a common positive real factor,
the signs of

\[
\varphi f+e
\]

and

\[
f-\varphi e.
\]

Thus, up to the global sign convention for the Riemann form, the polarization
cone is characterized by

\[
\varphi f+e>0,
\qquad
f-\varphi e>0.
\]

For the two public basis forms this gives

\[
\Omega_1:\quad (e,f)=(0,1),
\qquad
(\varphi f+e,\ f-\varphi e)=(\varphi,1),
\]

whereas

\[
\Omega_2:\quad (e,f)=(1,0),
\qquad
(\varphi f+e,\ f-\varphi e)=(1,-\varphi).
\]

Consequently

\[
\boxed{\Omega_1\text{ lies in the CM polarization cone}}
\]

while

\[
\boxed{\Omega_2\text{ does not lie in either global-sign polarization cone}}
\]

for the Jacobian CM type. Negating `Omega_2` reverses both signs and therefore
does not repair their mismatch.

There is also a useful classification statement. Write

\[
\lambda=a\lambda_1+b\lambda_2
       =\lambda_1\eta,
\qquad
\eta=(a-b)+b\varphi
     =f+e\varphi^{-1}.
\]

Then

\[
\operatorname{Pf}(\Omega_{a,b})
 =N_{K^+/\mathbf Q}(\eta).
\]

A positive principal polarization in this CM type requires `eta` to be a
totally positive unit of norm `+1`. Since

\[
\mathcal O_{K^+}^{\times}=\{\pm\varphi^n:n\in\mathbf Z\},
\]

the totally positive units are exactly

\[
\varphi^{2n}.
\]

Changing the generator of the rank-one `O_K`-module by the unit
`u=varphi^n` multiplies the trace parameter by

\[
u\bar u=\varphi^{2n}.
\]

Hence all `j`-invariant principal polarizations compatible with this CM type
form one `O_K^times`-equivalence class, represented by

\[
\boxed{[\Omega_1]}.
\]

This does **not** mean that the bare public CM pencil canonically selects
`Omega_1`. The selection here uses additional external data: the algebraic
curve, its CM type, and the requirement of a positive principal polarization.
It therefore preserves the public `CM-PERIOD-LATTICE-NONSELECTION [T]`
boundary.

Finally the `J` action agrees without a convention change. In `(e,f)`
coordinates, pullback by `J=1+j^2` gives

\[
(e,f)\longmapsto(2e-f,\ f-e).
\]

Since `(a,b)=(f,e)`, this is exactly

\[
\binom{a'}{b'}
=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}
\binom{a}{b},
\]

which is the public Canon matrix `A_J`.

The coordinate, Pfaffian, positivity, principal-polarization-class, and
`J`-pullback checks therefore agree exactly. What remains for a formal
Jacobian calibration is not this classification, but the construction of an
explicit integral homology basis and `O_K`-module identification carrying the
canonical Jacobian intersection form into that class.

## 6. Hodge calibration

For this surface the Hodge side is deliberately not frontier mathematics.
The family is useful because its answer is known.

For an odd prime `p`, the Jacobian of

\[
y^2=x^p-1
\]

is a standard stably nondegenerate CM family. In particular, for `p=5`, the
Hodge classes on every self-power `A^n` are generated by divisor classes.
Equivalently, this family satisfies the Hodge conjecture for all powers and
contains no exceptional higher-codimension Hodge classes beyond the algebra
generated by divisors.

For the present CM type this can also be seen through the usual character
criterion. Let

\[
G=\operatorname{Gal}(K/\mathbf Q)\simeq C_4.
\]

The odd-character sums attached to

\[
\Phi=\{\sigma_1,\sigma_2\}
\]

are nonzero, so the type is nondegenerate. Since `K/Q` is abelian and the
surface is simple, nondegeneracy is stable under self-products.

This gives a strict calibration target:

> Starting only from the exact cyclotomic eigenspace data and the admitted CM
> realization, can the TWIST-J algebraic machinery reproduce the known
> divisor-generated Hodge tensor algebra of `A^n`?

Agreement would establish a correct external realization. It would not prove
anything new about the Hodge conjecture.

## 7. Tate calibration by good reduction

The curve

\[
y^2=x^5-1
\]

has good reduction at rational primes

\[
p\ne2,5.
\]

The exclusion of `p=5` is load-bearing. Five is ramified in `Q(zeta_5)` and
is also the native prime of several TWIST-J residue constructions. Those
native mod-five structures must not be identified with a good reduction of
this Jacobian at five, because there is no such good reduction.

At a good prime, let `F_p` denote the arithmetic `p`-power Frobenius on
geometric points. Then directly

\[
F_pT=T^pF_p.
\]

Thus Frobenius acts on the fifth-root label as

\[
j\mapsto j^p.
\]

This is exactly the cyclotomic Galois element `sigma_p`. The four nonzero
residue classes modulo five therefore give

\[
\begin{array}{c|c|c}
p\bmod5 & \operatorname{ord}_5(p) & j\mapsto\\
\hline
1&1&j\\
4&2&j^{-1}\\
2&4&j^2\\
3&4&j^3
\end{array}
\]

and expose the complete arithmetic `C4` by ordinary prime reduction.

For a fixed good prime and a fixed power `A^n`, the Tate calibration can be
phrased exactly. Compute the Frobenius action on etale cohomology and compare
its codimension-`r` invariant subspace, equivalently the `p^r` eigenspace
before Tate twist, with the subspace generated by known algebraic cycles.

This can be done first in cases where the answer is already known. The point
is to test whether the TWIST-J cyclotomic bookkeeping naturally reproduces
the Hodge-to-Frobenius passage, not to infer Tate from a few finite examples.

## 8. Why Hodge and Tate belong in one note

For abelian varieties the two theories are unusually close. Deligne proved
that Hodge cycles on abelian varieties are absolute Hodge cycles. In CM
settings this gives strong control over their behavior under embeddings and
reduction. Milne developed precise routes by which Hodge information for CM
abelian varieties controls Tate and standard conjectures for corresponding
finite-field abelian varieties.

The natural comparison diagram for this lane is therefore

```text
O_K = Z[j]
   |
   v
polarized CM Hodge structure
   |
   +--> Hodge classes on A^n
   |
   v  good reduction p != 2,5
ell-adic Galois representation
   |
   +--> Frobenius/Tate classes on A_p^n
```

The left and middle portions are highly constrained exact algebra. The final
question, whether every distinguished cohomology class is algebraic, is where
the genuine Hodge/Tate difficulty begins.

## 9. Proposed exact work programme

This note itself does not preregister a probe. If promoted later, a formal
probe should freeze at least the following gates before computation.

### Gate A: integral CM identification

Construct an explicit integral basis of `H_1(A,Z)` and an exact
`P in GL_4(Z)` intertwining the curve automorphism `T` with the public
multiplication-by-`j` matrix.

### Gate B: principal polarization coordinates

Using the same frozen `P`, pull the canonical Jacobian intersection form into
the public lattice and verify that it lies in the `O_K^times`-equivalence
class `[Omega_1]` identified in section 5A. Record its exact `(a,b)` and
`(e,f)` representative and all dependence on the fractional-ideal generator,
orientation, and Galois choice.

The abstract coordinate and positivity classification of section 5A is a
note-level exact derivation. This gate asks for the explicit Jacobian homology
realization, not a second derivation of the same pencil identity.

### Gate C: Hodge positivity

Independently verify on the explicit Gate-B representative the Riemann
positivity condition at the selected CM type

\[
\Phi=\{\sigma_1,\sigma_2\}.
\]

This is the step that distinguishes a polarized Hodge realization from a bare
symplectic coincidence.

### Gate D: existing `J` action

Under the same identification, verify that pullback by `J=1+j^2` on the
polarization pencil gives exactly the already public matrix

\[
A_J=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}.
\]

No new status is earned by reproducing an existing Canon theorem.

### Gate E: Hodge tensor census

For small self-powers `A^n`, perform an exact character census of Hodge
tensors and verify agreement with the known divisor-generated answer. The
proof target is symbolic and representation-theoretic, not a floating-point
period calculation.

### Gate F: four Frobenius classes

Choose good primes representing all four elements of `(Z/5Z)^*`, for example
one prime in each residue class `1,2,3,4 mod 5`. Verify

\[
F_pT=T^pF_p
\]

and compute exact Frobenius characteristic polynomials and Tate-invariant
counts at frozen powers and codimensions.

Only after all six calibration gates survive should the lane move toward a
CM type with exceptional Hodge classes or toward Weil classes, where the
algebraicity problem is genuinely nontrivial.

## 10. Breakers and nonclaims

The lane is weakened or abandoned if any of the following occurs:

1. the canonical Jacobian polarization cannot be matched to the public CM
   pencil while preserving the same integral `j` action;
2. matching requires an undeclared basis, sign, Galois, or polarization choice
   that changes the conclusion;
3. the Hodge tensor census disagrees with the known divisor-generated result;
4. the finite-field comparison requires identifying the bad prime `5` with a
   good CM reduction;
5. Frobenius/Galois agreement holds only after an outcome-dependent choice;
6. a cohomology-class match is described as an algebraic-cycle theorem
   without an actual cycle construction or an independent theorem supplying
   algebraicity.

In particular,

\[
\boxed{\text{classifying a Hodge or Tate class is not proving it algebraic.}}
\]

TWIST-J would begin to matter to an open Hodge or Tate problem only if its
exact algebra supplied a new mechanism that constructs, forces, or excludes
algebraic cycles beyond already known cases.

## 11. Preliminary verdict

This lane is relevant to TWIST-J now, but as a calibration and realization
programme, not as a Millennium-problem claim.

The connection is concrete because the public Canon already contains the
quartic CM carrier, its anti-real trace-form lattice, the real-quadratic norm

\[
a^2-ab-b^2,
\]

and the hyperbolic `J` pullback

\[
\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.
\]

Classical CM geometry supplies a genus-two abelian variety carrying the same
fifth-root algebra. Hodge theory supplies the complex decomposition and
polarization test. Good reduction supplies Frobenius and the Tate-side
arithmetic test.

The useful route is therefore

```text
TWIST-J exact CM pencil
 -> polarized CM realization
 -> known Hodge census
 -> good reduction
 -> known Tate census
 -> only then exceptional cycles.
```

The coordinate and positivity subproblem of the first arrow is now solved at
note level: the two public basis forms are `(e,f)=(0,1)` and `(1,0)`, and the
Jacobian CM type selects the principal-polarization class `[Omega_1]`. The
remaining first-arrow work is the explicit integral homology identification
and an independent formal reproduction. No Hodge or Tate conjecture claim is
created by this calibration.

## References

- Clay Mathematics Institute, *Hodge Conjecture*:
  https://www.claymath.org/millennium/hodge-conjecture/
- C. McMullen, course notes containing the explicit genus-two fifth-root
  Jacobian example:
  https://people.math.harvard.edu/~ctm/home/text/class/harvard/213b/19/html/home/course/course.pdf
- K. A. Ribet, *Hodge classes on certain types of abelian varieties*,
  American Journal of Mathematics 105 (1983), 523-538:
  https://doi.org/10.2307/2374267
- P. Deligne, *Hodge Cycles on Abelian Varieties*:
  https://www.jmilne.org/math/Documents/Deligne82.pdf
- J. S. Milne, *The Tate conjecture over finite fields*:
  https://www.jmilne.org/math/xnotes/TateAim.pdf
- J. S. Milne, *The Tate and Standard Conjectures for Certain Abelian
  Varieties*:
  https://arxiv.org/abs/2112.12815

## Internal anchors

- `canon/CANON.md`, Public Canon v83.
- `canon/REGISTRY.tsv`, especially
  `CM-ALTERNATING-PRIMARY-LATTICE-SEAM`,
  `CM-REAL-DIFFERENT-PRIMARY-SEAM`,
  `CM-RAMIFIED-PFAFFIAN-ROOT`, and
  `CM-PERIOD-LATTICE-NONSELECTION`.
- `notes/C-CM-2I-QCARRIER-1/` and `notes/C-CM-2I-QCARRIER-2/` as earlier
  non-canonical CM-side explorations. Those notes do not establish the Hodge
  or Tate realization proposed here.
