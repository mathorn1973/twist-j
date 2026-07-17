# P-J-LI-FEJER-CARRIER-1 preregistration draft

```text
STATUS:             BLOCKED-PREDEFINITION
LAYER:              L6 measure
SCIENTIFIC SCOPE:   necessary shape/kill test for one named J-native carrier
MOMENT BRIDGE:      outside this probe, O
RH:                 O
PUBLIC AUTHORITY:   none
DATE:               2026-07-16
```

This is an incubation protocol, not a public `PREREG.md`.  No probe branch
should be opened and no first formal run should occur until G0 names one
specific carrier and freezes its construction bytes.  Searching over carriers
after seeing the reference output is outside scope.

## 0. Logical split

Two different problems must not be combined.

`P-J-LI-FEJER-CARRIER-1` is a necessary shape probe for one independently
derived positive J-carrier.  It can kill a carrier using its mass, atom, and
Fejér behavior.  A PASS does not prove Li moments or RH.

The separate open lift is

\[
\boxed{
\widehat{\sigma_J}(m)=t_m(\xi_J)
\quad\text{for every }m\in\mathbb Z.
}
\]

The reference module uses the root-filter-normalized function

\[
Z_J(s):=operatorname{MerCont}
\frac{\mathcal P_0(s)}{5^{1-s}-1}=\zeta(s),
\qquad
\xi_J(s):=rac12s(s-1)\pi^{-s/2}\Gamma(s/2)Z_J(s),
\]

and the standard Li coefficients

\[
\lambda_n(\xi_J)
:=
\frac1{(n-1)!}
\left.
\frac{d^n}{ds^n}
\left[s^{n-1}\log\xi_J(s)\right]
\right|_{s=1}.
\]

Freeze

\[
\lambda_0=0,
\qquad
\lambda_{-m}=\lambda_m,
\qquad
t_m:=\lambda_{m+1}+\lambda_{m-1}-2\lambda_m.
\]

Herglotz gives the equivalence between positive definiteness and existence of
a finite positive Borel measure.  Li's criterion together with the previously
proved CND/Toeplitz equivalence supplies the final RH equivalence:

\[
(t_m)\text{ positive definite}
\iff
\exists\,\text{ finite positive Borel }\sigma:\
\widehat\sigma(m)=t_m\text{ for every }m
\iff \mathrm{RH}.
\]

Equality with the one independently predeclared measure \(\sigma_J\) is a
stronger construction claim: it implies RH, but RH alone does not identify
that particular carrier.  Its identifier is `J-LI-MOMENT-BRIDGE [O]`; a
future public probe, if appropriate, must have a separate name such as
`P-J-LI-MOMENT-BRIDGE-1`.

## 1. One-way dependency graph

The construction graph must have only the direction

\[
J\text{-data}
\longrightarrow
(\mathcal H_{J,\chi_0},U_{J,\chi_0},v_{J,\chi_0})
\longrightarrow
\mu_J
\longrightarrow
\sigma_J.
\]

The reference graph

\[
\xi
\longrightarrow
\lambda_n
\longrightarrow
t_m
\]

may enter only a comparison gate.  No edge may lead back from the reference
graph into the carrier construction.

## 2. Gates

### G0 — PREDEFINITION

Before a pin exists, freeze:

1. the exact definitions of the full complex carrier
   \((\mathcal H_J^{\rm full},U_J^{\rm full},v_J^{\rm full})\) and of its
   projected objects
   \((\mathcal H_{J,\chi_0},U_{J,\chi_0},v_{J,\chi_0})\), including the
   convention that the inner product is linear in its first variable;
2. every domain, closure, parameter, cutoff, and convention;
3. the trivial \(C_4\) projector and its reducing action;
4. the archimedean block and the ramified block at \(5\);
5. the Fourier convention
   \(\widehat\sigma(m)=\int_{\mathbb T}z^{-m}\,d\sigma(z)\), the conjugation
   pushforward \(\iota(z)=\overline z\), and normalized angular measure
   \(d\theta/(2\pi)\);
6. the construction source hash and dependency allowlist.

The present draft is blocked here.  "Find some measure" is not a
preregisterable object.

### G1 — INPUT PURITY

The following are absolutely forbidden construction dependencies:

- \(\zeta\), \(\xi\), \(\lambda_n\) (including \(\lambda_1\)), or \(t_m\);
- zeta zeros;
- a prime table or von Mangoldt coefficients;
- the standard Weil or target Herglotz form;
- encoded target tables or results of a previous fit.

The following are forbidden as calibration inputs, but may occur as exact
outputs of a derivation frozen from the declared blocks:

- \(\gamma\) or \(\log(2\pi)\);
- arithmetic or local terms derived from the frozen \(\{\infty,5\}\) block.

The construction is also forbidden from using network access, undeclared
files or environment variables, randomness, or encoded target tables.

The reference-defined functions, Li coefficients, zeros, and target forms
occur only in a separate reference module.  Any permitted construction-side
derivation of constants or local terms must be frozen in G0 and audited here.
Rescaling \(v_J\) after the fact to match \(\lambda_1\) is forbidden.

### G2 — TRIVIAL-SECTOR LIFT

Isolate the completed trivial \(C_4\) sector.  Positivity of the whole Artin
packet is not enough.  The projector must obey

\[
P_{\chi_0}=P_{\chi_0}^*=P_{\chi_0}^2,
\qquad
[P_{\chi_0},U_J^{\rm full}]=0,
\qquad
v_{J,\chi_0}=P_{\chi_0}v_J^{\rm full}.
\]

The projected space and operator are

\[
\mathcal H_{J,\chi_0}=P_{\chi_0}\mathcal H_J^{\rm full},
\qquad
U_{J,\chi_0}=U_J^{\rm full}|_{\mathcal H_{J,\chi_0}}.
\]

Thus the projected subspace is reducing.  From this point, \(\mathcal H_J\),
\(U_J\), and \(v_J\) abbreviate these projected trivial-sector objects.
Define

\[
\mu_J(B)
=
\langle v_J,E_{U_J}(B)v_J\rangle,
\qquad
\sigma_J=\mu_J+\iota_*\mu_J.
\]

### G3 — POSITIVITY

Prove

\[
U_J^*U_J=U_JU_J^*=I,
\qquad
\|v_J\|<\infty,
\qquad
\sigma_J\ge0.
\]

One exact negative quadratic vector falsifies the carrier.  A finite prefix of
positive Toeplitz matrices does not prove positivity at all orders.

### G4 — MASS

The construction module must first derive, without target input or post-hoc
normalization, its own exact symbolic output

\[
M_J:=\mu_J(\mathbb T).
\]

Only the separate reference comparator may then certify

\[
\boxed{
M_J
=1+\frac\gamma2-\frac12\log(4\pi),
}
\]

and hence

\[
\boxed{
\sigma_J(\mathbb T)
=2+\gamma-\log(4\pi).
}
\]

Any exact mismatch kills the candidate.

The target constants are forbidden as construction inputs or calibration
parameters, not as outputs of a frozen derivation from the declared
archimedean block.  Exact equality requires a symbolic or proof certificate.
Disjoint rigorous intervals can certify failure; overlapping intervals alone
leave this gate unresolved.

### G5 — NO ATOM

Prove constructionally

\[
E_{U_J}(\{1\})v_J=0,
\]

equivalently

\[
\mu_J(\{1\})=\sigma_J(\{1\})=0.
\]

A finite sampled profile cannot close this gate.

### G6 — FEJÉR SCALING

Put

\[
F_{n-1}(z)
:=
\frac1n\left|\sum_{k=0}^{n-1}z^k\right|^2,
\qquad
S_J(n)
:=
\int_{\mathbb T}F_{n-1}\,d\sigma_J.
\]

The construction module must derive and pin an asymptotic decomposition

\[
S_J(n)=A_J\log n+B_J+R_J(n).
\]

The separate reference comparator must then prove

\[
A_J=1,
\qquad
B_J=\gamma-1-\log(2\pi).
\]

A bare big-\(O\) claim is not sufficiently frozen.  Before a formal run,
choose a rational \(C_F>0\) and an integer \(N_F\ge2\), and pin a proof
artifact establishing

\[
\boxed{
|R_J(n)|
\le
C_F\frac{\log n}{\sqrt n}
\quad(n\ge N_F).
}
\]

The same \(C_F,N_F\) and proof hash must survive validation; tuning them after
a result is forbidden.  The certificate must contain exact finite base cases
plus an analytic tail bound, or another complete proof for all
\(n\ge N_F\).  A finite computational range supplies only finite-range C
evidence or a counterexample, never PASS for the universal gate.

Before activation, also freeze the proof-validation trust boundary: either a
machine-checkable certificate and pinned checker, or a named human proof-audit
procedure listing every imported lemma and assumption.  A prose tail claim or
an unchecked proof hash cannot close G6.

For a locally absolutely continuous carrier, an optional stronger certificate
may use

\[
\ell(\theta)
:=
-\log\left(2\left|\sin\frac\theta2\right|\right),
\]

for which

\[
\int_{-\pi}^{\pi}
F_{n-1}(e^{i\theta})\ell(\theta)
\frac{d\theta}{2\pi}
=H_n-1.
\]

If \(w_J=\ell+h_J\), freeze a continuous representative of \(h_J\) at zero.
The constant term then requires

\[
h_J(0)=-\log(2\pi).
\]

A frozen Hölder bound with exponent \(\alpha\ge\tfrac12\), or a directly
verified modulus of continuity whose Fejér convolution has the required
rate, plus control of the measure away from \(1\), can provide explicit
\(C_F,N_F\).  Merely saying \(h_J=O(1)\) is insufficient for the constant and
remainder.

### G7 — OPTIONAL FINITE MOMENTS

One may freeze a finite set \(M\subset\mathbb Z\) and test

\[
\widehat{\sigma_J}(m)=t_m
\qquad(m\in M).
\]

One exact mismatch kills the carrier.  PASS is at most C evidence on that
finite set and cannot be promoted into an all-\(m\) bridge.

Exact equality requires a symbolic certificate.  Disjoint rigorous intervals
can certify failure, whereas overlapping intervals alone are unresolved.

### G8 — ALL-M MOMENT BRIDGE

This gate is explicitly outside the shape probe:

\[
\widehat{\sigma_J}(m)=t_m
\qquad(m\in\mathbb Z).
\]

Moment equality alone does not prove the provenance of an explicit formula.
A separate subgate must freeze the test-function space and decomposition and
show that the same carrier reproduces the arithmetic side, archimedean
contribution, pole terms, trivial zeros, and the local normalization at \(5\),
without importing the target.  Both subgates remain O.

## 3. Mandatory preregistration fields

```text
Equation:       exact G2-G7 definitions and Fourier/Fejér conventions
Code version:   separate construction and reference modules, both pinned
Carrier:        declared J-architecture only; no external dataset
Systematics:    C4 sector, symmetrization, dtheta/(2pi), F_(n-1),
                C_F, N_F, cutoffs, closures, and interval conventions
Proof artifact: hash, dependency manifest, exact base cases, analytic tail,
                and a pinned checker or named proof-audit procedure
Failure:        one exact mismatch or one forbidden dependency
Layer:          L6 measure; no all-n promotion from a finite range
```

## 4. Falsifiers

The candidate fails if:

1. reference data enter the construction dependency graph;
2. \(v_J\) is normalized using the target \(\lambda_1\);
3. the trivial \(C_4\) sector is not isolated;
4. an exact negative quadratic form appears;
5. the mass is wrong;
6. an atom occurs at \(1\);
7. the Fejér coefficient differs from one;
8. the asymptotic constant differs from \(\gamma-1-\log(2\pi)\);
9. the frozen uniform bound fails;
10. any frozen reference moment disagrees.

Before G8, each failure falsifies the proposed carrier, not RH.

## 5. No-go guard: shape is not the moment sequence

Mass, atomlessness, and Fejér asymptotics do not determine all Fourier
moments.  Start with a positive measure having positive mass on two disjoint
arcs separated from \(1\), and add a sufficiently small zero-mass signed
perturbation that moves mass from one arc to the other.  Positivity, total
mass, and absence of an atom at \(1\) survive; the Fejér mean changes by only
\(O(1/n)\), but Fourier coefficients change.

Therefore

\[
\boxed{
\text{Fejér shape PASS}
\not\Longrightarrow
\widehat\sigma=t.
}
\]

Proposed guard rows:

```text
FEJER-SHAPE-IMPLIES-LI-MOMENTS          F
TARGET-MOMENT-HERGLOTZ-AS-CONSTRUCTION  proof-invalid guard
```

## 6. Frozen status cut

```text
J-LI-FEJER-IDENTITY          conditional algebraic T under the exact all-n norm identity
J-LI-FEJER-SCALING           T as a necessary implication under the exact all-n norm identity
P-J-LI-FEJER-CARRIER-1       BLOCKED-PREDEFINITION
J-LI-MOMENT-BRIDGE           O
J-LI-COCYCLE-REALIZATION     O
RH                           O
PUBLIC REGISTRATION          absent
```
