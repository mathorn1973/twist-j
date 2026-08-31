# PROMO-CM-ALTERNATING-PRIMARY-LATTICE-SEAM

Status: **NON-CANONICAL / NO AUTHORITY / PROMOTION PACKAGE ONLY.**

Basis:

```text
public authority:       Public Canon v68
basis main:             1a184cf086cf55a5a4a5a55e5f62ab419c95a069
source claim issue:     #625
source probe PR:        #626
source probe:           P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1
source claim:           CM-ALTERNATING-PRIMARY-LATTICE-SEAM
source result:          candidate-T / L1 / CONFIRMED
formal pin:             1779535e221ef9efc9fcb6a577a21050dad9aa03
result head:            1395edf3abefdebc0ff5f18b5c8bee60133366e4
verifier sha256:        7ed314282477c48b3124f06c5b70d92e830b3f85a18ecf0841f0916bdd8f9061
expected/stdout sha256: 564874aa8b2bdf28577947dbb82e249cf8cb338aa19dbde3ce3cf352e21ec7ff
bundle manifest sha256: 7261b8e5aaf485df7e5494c74239de8689c5247b6b13484544ffe763ac0f6cb6
source merge:           1a184cf086cf55a5a4a5a55e5f62ab419c95a069
```

The source pull request passed the required GitHub-hosted Python 3.12 x86_64
and native aarch64 jobs with byte-identical stdout and aggregate `check` PASS.
The written proof carries the universal statements; the verifier is an exact
integer and rational audit.

This package changes no probe byte and creates no claim, status, Canon
version, Registry row, Frontier row, tag, or release. It freezes one later L1
theorem fold and corrects the result hierarchy and action boundary before that
fold.

## 1. Forcing hierarchy

Put

```text
E_Z = Alt^2(Z^4),
P(W) = M_J^T W M_J,
q(x) = x^2-3x+1,
r(x) = Phi_10(x),
H_Z = ker(q(P) on E_Q) intersect E_Z,
C_Z = ker(r(P) on E_Q) intersect E_Z,
Q = E_Z/(H_Z direct-sum C_Z).
```

The location of every possible primary seam is forced before the lattice
determinant is evaluated. Cayley--Hamilton and integrality give

```text
q(P)E_Z subset C_Z,
r(P)E_Z subset H_Z,
```

so both `q(P)` and `r(P)` annihilate `Q`. The exact Bezout identity

```text
(8-3x)r(x)+(3x^3-2x^2+2x-3)q(x)=5
```

therefore gives `5Q=0`. In particular, five is the only possible support
prime; consistently, `Res(q,r)=25` has the same sole prime divisor. The
genuinely computed seam-order datum is

```text
[E_Z:H_Z direct-sum C_Z]=5.
```

It follows that `Q` is one-dimensional over `F_5`. Only at this point does

```text
q(x)=(x+1)^2 mod 5,
r(x)=(x+1)^4 mod 5
```

force the full quotient action `P|Q=-1`. Before the index calculation, the
common root forces the sole eigenvalue `-1`, but a nonzero nilpotent Jordan
part on `Q` has not yet been excluded. Of the three seam
data--support, order, and multiplier--the index/order is the only independent
lattice measurement; the seam prime and, after that index is known, the
multiplier are algebraic consequences. The full intersection bases are, of
course, additional computed lattice data.

Also

```text
chi_P(x)=(x+1)^6 mod 5,
```

so Cayley--Hamilton gives `(P+I)^6=0` on `E_Z/5E_Z`: `-P` is unipotent at the
ramified place. This is a loss of primary transversality, not a literal
equality of the reduced rank-two and rank-four channels. Their reductions
meet in the one line represented by `Omega_1+2 Omega_2`; explicitly,
`Omega_1+2 Omega_2=3c1+c2+2c3+c4` modulo five.

## 2. Saturation and the integral retraction theorem

For a rational subspace `V_Q` of `E_Q`, the intersection `E_Z intersect V_Q`
is saturated by definition. Saturation of `H_Z` and `C_Z` is therefore a
sanity check, not a discovery. The substantive statements are their displayed
full bases and the index of their sum.

The rational `P`-equivariant primary projector is

```text
E_H = ((8-3P)r(P))/5
    = (-3P^5+11P^4-11P^3+11P^2-11P+8I)/5.
```

Its exact denominator five has the following intrinsic formulation:

```text
there is no Z[P]-linear retraction E_Z -> H_Z.
```

Indeed, any such retraction extends after tensoring with the rational field to
a `Q[P]`-linear retraction. The coprime primary types imply
`Hom_(Q[P])(C_Q,H_Q)=0`, so that extension must be the unique projector
`E_H`. Its exact denominator five prevents it from preserving `E_Z`. This is
a proved `[T]` corollary, not a proposed `[H]` row. Whether a future physical
decoder should use this projector is a different, still untyped question.

## 3. Generator and action-unit guard

The public CM pencil implies that its unimodular parameter generators are

```text
lambda = epsilon phi^n lambda_1,   epsilon in {+1,-1}, n in Z,
Pf(Omega_lambda)=(-1)^n,
J^*: (epsilon,n) -> (epsilon,n-2).
```

Consequently each fixed-Pfaffian locus has two antipodal `J`-orbits, exchanged
by complex conjugation. After the explicit identification `Omega~-Omega` the
locus becomes one `Z`-torsor. Alternatively, adjoining conjugation makes the
signed locus a torsor for `<J^*,C^*> ~= Z x C_2`, not for `J` alone. The two
forms have the same symplectic orientation in dimension four; the distinction
is generator sign, not orientation.

The canonical object is the ramified ideal

```text
(lambda_1)=(1-zeta_5),
```

not its displayed generator. `Omega_1` is a convenient basis element and a
chosen point on one member of the antipodal orbit pair, not a canonically
selected action carrier.
Choosing `Omega_1` and declaring its coefficient to be the unit is one
algebraic normalization, not two independent gains. A physical scalar period
still requires a paired cycle or current, dimensions, a phase law, and a typed
layer bridge.

## 4. Frozen public scope

The exact Registry scope string is:

```text
at L1 for E_Z=Alt^2(Z^4) in the fixed upper-triangular basis and P(W)=M_J^T W M_J, chi_P=(x^2-3x+1)Phi_10(x) gives the unique rational primary split E_Q=H_Q direct-sum C_Q with H_Q the public CM pencil and P restricted to C_Q of order ten; the displayed bases are the full integral intersections H_Z and C_Z, whose canonical sum has index five and quotient Q=Z/5; q(P) and Phi_10(P) annihilate Q, the Bezout identity forces 5Q=0, and after the index calculation the unique common mod-five root forces P=-1 on Q, while -P is unipotent on E_Z/5E_Z and the reductions of H_Z and C_Z meet in exactly F_5(Omega_1+2 Omega_2) rather than becoming equal; the unique rational P-equivariant projector E_H=((8-3P)Phi_10(P))/5 has exact denominator five, equivalently no Z[P]-linear retraction E_Z->H_Z exists; every nonzero phi^(+/-2) eigenform is Pfaffian-null of rank two; saturation of the two full intersections is automatic, Omega_1 is a displayed basis form rather than a canonical action unit, and no action, h, hbar, phase, 2 pi, entropy-area carrier, decoder, physical place, time orientation, Hurwitz branch or L2-L6 lift is selected
```

Its SHA-256 is

```text
4350d7f162389982e612565e05ab9e89c2ec772da28b0de56331b0ea1cdb8625
```

The exact falsifier string is:

```text
fires if the characteristic polynomial, irreducibility, rational primary split or order-ten circular restriction fails, if either displayed basis is not the full integral intersection, if the six-column index is not five or Q is not Z/5, if q(P) and Phi_10(P) do not annihilate Q, the Bezout forcing 5Q=0 or the mod-five common-root argument fails, P does not act as -1 on Q, -P is not unipotent on E_Z/5E_Z, or the reduced primary lattices do not meet in exactly F_5(Omega_1+2 Omega_2), if the projector identity or exact denominator five fails or a Z[P]-linear retraction E_Z->H_Z exists, or if a nonzero phi^(+/-2) eigenform is not Pfaffian-null of rank two; saturation itself is an automatic intersection lemma rather than an independent discovery; any canonical Omega_1 action-unit selection or physical, entropy-area, Hurwitz or L2-L6 reading is outside scope; an evidence-bundle or architecture mismatch without exact mathematical negation is integrity STOP
```

## 5. Frozen Canon insertion

Insert the following block in `canon/CANON.md` under `## 4. The two places`,
immediately after `CM-ALTERNATING-PENCIL [T]`.

```markdown
### CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]

Let `P(W)=M_J^T W M_J` act on
`E_Z=Alt^2(Z^4)=Z^6` in upper-triangular coordinate order, and put

```text
q(x)=x^2-3x+1,
r(x)=Phi_10(x)=x^4-x^3+x^2-x+1.
```

Exactly

```text
chi_P(x)=q(x)r(x).
```

Both irreducible factors occur once. Hence

```text
E_Q=H_Q direct-sum C_Q,
H_Q=ker q(P),
C_Q=ker r(P),
```

and `P|C_Q` has exact order ten. The hyperbolic plane is exactly the public
CM pencil, with full integral intersection

```text
H_Z=Z Omega_1 direct-sum Z Omega_2.
```

The full circular intersection has basis

```text
c1=(-1, 0,1,0,0,0),
c2=( 0,-1,0,1,0,0),
c3=( 0,-1,0,0,1,0),
c4=(-1, 0,0,0,0,1).
```

These intersections are automatically saturated. The nontrivial integral
statement is

```text
[E_Z:H_Z direct-sum C_Z]=5,
Q=E_Z/(H_Z direct-sum C_Z)=Z/5.
```

Both `q(P)` and `r(P)` annihilate `Q`. The exact identity

```text
(8-3x)r(x)+(3x^3-2x^2+2x-3)q(x)=5
```

forces `5Q=0`; the index is the independently computed lattice datum. Since
`q=(x+1)^2` and `r=(x+1)^4` modulo five, one-dimensionality then forces
`P|Q=-1`. Moreover `chi_P=(x+1)^6` modulo five, so `-P` is unipotent on
`E_Z/5E_Z`. The two reduced primary lattices lose transversality along the
line generated by `Omega_1+2 Omega_2`; they do not become equal.

The unique rational `P`-primary projector is

```text
E_H=((8-3P)r(P))/5.
```

Its smallest denominator is exactly five. Equivalently, there is no
`Z[P]`-linear retraction `E_Z -> H_Z`: after tensoring with the rational
field, any such retraction must equal `E_H` because the two primary types are
coprime.

Pfaffian covariance gives `Pf(PW)=Pf(W)`. Every nonzero eigenform with
eigenvalue `phi^2` or `phi^-2` is therefore Pfaffian-null and has rank two;
it is not symplectic.

The ramified ideal `(lambda_1)=(1-zeta_5)` is canonical, but `lambda_1` is a
chosen generator and `Omega_1` its associated displayed basis form, not a
canonical origin or action unit. On either fixed
Pfaffian locus, signed unimodular forms form two antipodal `J`-orbits; only an
explicit quotient `Omega~-Omega` turns them into one `Z`-torsor. No action,
`h`, `hbar`, phase, `2 pi`, entropy-area carrier, physical place, time
orientation, decoder or L2-L6 lift follows.
```

## 6. Exact ledger rows for a later fold

Add this exact six-column `canon/REGISTRY.tsv` row:

```tsv
CM-ALTERNATING-PRIMARY-LATTICE-SEAM	T	at L1 for E_Z=Alt^2(Z^4) in the fixed upper-triangular basis and P(W)=M_J^T W M_J, chi_P=(x^2-3x+1)Phi_10(x) gives the unique rational primary split E_Q=H_Q direct-sum C_Q with H_Q the public CM pencil and P restricted to C_Q of order ten; the displayed bases are the full integral intersections H_Z and C_Z, whose canonical sum has index five and quotient Q=Z/5; q(P) and Phi_10(P) annihilate Q, the Bezout identity forces 5Q=0, and after the index calculation the unique common mod-five root forces P=-1 on Q, while -P is unipotent on E_Z/5E_Z and the reductions of H_Z and C_Z meet in exactly F_5(Omega_1+2 Omega_2) rather than becoming equal; the unique rational P-equivariant projector E_H=((8-3P)Phi_10(P))/5 has exact denominator five, equivalently no Z[P]-linear retraction E_Z->H_Z exists; every nonzero phi^(+/-2) eigenform is Pfaffian-null of rank two; saturation of the two full intersections is automatic, Omega_1 is a displayed basis form rather than a canonical action unit, and no action, h, hbar, phase, 2 pi, entropy-area carrier, decoder, physical place, time orientation, Hurwitz branch or L2-L6 lift is selected	4. The two places	probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1	fires if the characteristic polynomial, irreducibility, rational primary split or order-ten circular restriction fails, if either displayed basis is not the full integral intersection, if the six-column index is not five or Q is not Z/5, if q(P) and Phi_10(P) do not annihilate Q, the Bezout forcing 5Q=0 or the mod-five common-root argument fails, P does not act as -1 on Q, -P is not unipotent on E_Z/5E_Z, or the reduced primary lattices do not meet in exactly F_5(Omega_1+2 Omega_2), if the projector identity or exact denominator five fails or a Z[P]-linear retraction E_Z->H_Z exists, or if a nonzero phi^(+/-2) eigenform is not Pfaffian-null of rank two; saturation itself is an automatic intersection lemma rather than an independent discovery; any canonical Omega_1 action-unit selection or physical, entropy-area, Hurwitz or L2-L6 reading is outside scope; an evidence-bundle or architecture mismatch without exact mathematical negation is integrity STOP
```

Add this `canon/NORMATIVE.tsv` row:

```tsv
CM-ALTERNATING-PRIMARY-LATTICE-SEAM	THEOREM	CM-ALTERNATING-PRIMARY-LATTICE-SEAM	T	L1		canon/CANON.md::CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T]
```

Add these two `canon/DEPENDENCIES.tsv` rows:

```tsv
CM-ALTERNATING-PRIMARY-LATTICE-SEAM	CM-ALTERNATING-PENCIL	REQUIRES	the public CM basis, Pfaffian law, unimodular locus and pullback action are inherited inputs and are characterized, not re-earned
CM-ALTERNATING-PRIMARY-LATTICE-SEAM	J-STEP	REQUIRES	the public integral multiplication-by-J matrix defines the pullback P on alternating forms
```

Add this `canon/EVIDENCE.tsv` row:

```tsv
CM-ALTERNATING-PRIMARY-LATTICE-SEAM	EV-CM-ALTERNATING-PRIMARY-LATTICE-SEAM	PUBLIC_PROBE	probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1	7261b8e5aaf485df7e5494c74239de8689c5247b6b13484544ffe763ac0f6cb6	bundle-manifest-sha256-v1	two-architecture
```

For a Public Canon v69 fold, add this declaration to
`canon/HISTORY.tsv`:

```tsv
CANON69-DECLARE-CM-ALTERNATING-PRIMARY-LATTICE-SEAM	1	2026-08-28	canon-v69-candidate	CM-ALTERNATING-PRIMARY-LATTICE-SEAM	DECLARE	-	T	4350d7f162389982e612565e05ab9e89c2ec772da28b0de56331b0ea1cdb8625	EV-CM-ALTERNATING-PRIMARY-LATTICE-SEAM	probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1	7261b8e5aaf485df7e5494c74239de8689c5247b6b13484544ffe763ac0f6cb6	Public Canon v69 registers the unique rational CM primary plane, the full integral primary lattices, their computed index-five seam, its algebraically forced five-primary support and the forced quotient action after the index computation, the exact denominator-five no-retraction theorem and the Pfaffian-null eigenform guard at L1; saturation is not counted as a discovery, Omega_1 is not selected as an action unit, and no physical or higher-layer bridge moves.
```

If the theorem is folded in a later release than v69, only the event id,
release label, date and release-form rationale may be rebased. The scope SHA,
evidence identity, status and scientific content remain frozen.

## 7. Changelog and release boundary

Add this scientific paragraph to the Public Canon v69 changelog entry; a
combined fold may place its other independently frozen deltas beside it.

```text
CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T] identifies the public CM pencil as
the unique rational hyperbolic primary plane, computes the full integral
primary lattices and their index-five seam, derives its forced five-primary
support and minus-one quotient action, proves the denominator-five
equivariant no-retraction theorem, and protects the Pfaffian-null real
eigenlines. Saturation is not counted as a discovery, Omega_1 is not selected
as an action unit, and no action, entropy-area, Hurwitz, decoder or higher-layer
reading is promoted.
```

The theorem is not added to `canon/CORE_SELECTION.tsv`. A later release fold
updates the version identity in `canon/CORE.md` and the release-form files by
the normal sealed activation procedure; this promotion package does not guess
their final hashes or content commit.

## 8. Expected one-row ledger delta

Relative to Public Canon v68:

```text
claims:                   337 -> 338
T:                        214 -> 215
D:                         43 -> 43
C:                         33 -> 33
H:                          2 -> 2
O:                         28 -> 28
F:                         17 -> 17
live H/O:                  30 -> 30
normative items:          383 -> 384
dependency edges:         616 -> 618
evidence rows:            337 -> 338
history rows:             860 -> 861
gates:                     11 -> 11
evidence none:             45 -> 45
one-architecture:           9 -> 9
recorded-audit:             31 -> 31
two-architecture:         252 -> 253
```

No `canon/FRONTIER.md`, `canon/FRONTIER_PROGRAMS.tsv`, gate, minimal
reproduction, decoder or CORE-selection row is added.

If this item is combined with other frozen promotions, the aggregate right
endpoints change accordingly. This package must still contribute exactly
`+1` claim, `+1 T`, `+1` normative item, `+2` dependency edges, `+1`
evidence row, `+1` history row and `+1` two-architecture row, with zero delta
to every other status and to FRONTIER, gates and CORE selection.

## 9. Physical and program boundary

No separate `[H]` row is opened for the projector obstruction: the
nonexistence of an integral equivariant retraction is already proved and
belongs inside this `[T]` row. Identifying it with an existing five-adic step
gluing would require an explicit comparison map and equality theorem; this
package makes neither claim.

The already-public exact rows imply the scalar rewriting

```text
script-Q = 2 pi exp(-h_top)
```

from `script-Q phi^2=2 pi` and `h_top=2 log phi`. This earns no new row here.
Its interpretation as an action quantum remains a separately typed physical
bridge, and neither `2 pi` nor a phase law is supplied by the exterior-square
theorem. The Hurwitz branch is replaced, not retained in parallel.

## 10. Fold checks and stop conditions

A later fold must regenerate the normative checksums from the assembled
content tree and run the repository's full changed-Canon escalation on x86_64
and aarch64. STOP and do not promote if any of these occurs:

```text
scope SHA mismatch
bundle-manifest mismatch
any Registry/NORMATIVE/DEPENDENCIES/EVIDENCE/HISTORY disagreement
an item contribution other than +1 claim, +1 T, +1 normative item,
  +2 dependencies, +1 evidence row, +1 history row and +1 two-architecture row
any FRONTIER, gate, decoder or CORE-selection semantic delta
wording that treats saturation as an independent discovery
wording that claims the whole two reduced channels are equal modulo five
wording that calls Omega_1 a canonical action unit or a selected physical h
wording that promotes script-Q=2 pi exp(-h_top) as a physical action law
wording that restores Hurwitz as a parallel justification
any changed source-probe byte
any failed x86_64, aarch64 or aggregate check
any normative SHA256 mismatch
```

## 11. Promotion ceiling

The only scientific promotion authorized by this package is

```text
CM-ALTERNATING-PRIMARY-LATTICE-SEAM [T], L1.
```

It is exactly one future row. No `[D]`, `[H]` or `[O]` row, no action or `h`
identification, no new `script-Q` claim, no `2 pi` or phase law, and no
Hurwitz branch is added.
