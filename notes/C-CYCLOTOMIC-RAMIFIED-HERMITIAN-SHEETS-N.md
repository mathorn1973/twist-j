# C-CYCLOTOMIC-RAMIFIED-HERMITIAN-SHEETS-N

```text
STATUS:          NON-CANONICAL INCUBATION NOTE
AUTHORITY:       NO NORMATIVE AUTHORITY
TARGET LINE:     PUBLIC
PUBLIC CANON:    Public Canon v71 / canon-v71
PUBLIC BASE:     341cb01026cca2184b9e9dddef204c5e61934cc0
CLAIM ISSUE:     #662
ACTION LAYER:    L4 EXACT QUADRATIC SUPPORT ONLY
FORMAL PROBE:    NONE
PREREGISTRATION: NONE
VERIFIER / RUN:  NONE
CANON CHANGE:    NONE
REGISTRY CHANGE: NONE
```

This note freezes the mathematical end-state of one ramified Hermitian side
branch. It is reusable language and bookkeeping only. It creates no public
claim, evidence credit, physical reading, selector, or layer lift.

The order of presentation is deliberate: first the general mathematical form,
then attribution, then the `p = 5` specialization, and only then the typed
boundary.

The sealed predecessor `C-LORENTZ-HERM2-CARRIER-N` remains unchanged. The
completed public probe `P-J-NORM-TRACE-TANGENT-SEAM-1` remains unchanged and is
not folded here.

## 1. General odd-prime setup

[candidate-T / L4]

Let `p` be an odd rational prime and put

```text
K       = Q(zeta),
zeta     = zeta_p,
F       = K^+,
bar      = the involution K/F,
eta      = zeta + zeta^-1,
J        = 1 + zeta^2 = zeta eta,
P        = (1-zeta) in O_K,
mathfrak_p = P intersect O_F.
```

The element `eta` is a unit. One exact witness is

```text
1 + zeta^2 = (1-zeta^4)/(1-zeta^2),
```

so the numerator and denominator have the same `P`-valuation and their ratio
is a unit. Since

```text
J = zeta eta,
J bar(J) = eta^2,
```

the determinant-preserving normalized Hermitian congruence has scalar
normalization `c = +/- eta^-1` before the central sign is fixed.

Let

```text
A_J = diag(J,1).
```

The `J`-native normalization used below is

```text
c = eta^-1,
R(X) = c A_J X A_J^dagger.
```

For

```text
X = [[u,w],[bar(w),v]],
```

one obtains

```text
R(u,v,w) = (eta u, eta^-1 v, zeta w),
q(RX) = q(X),
q(X) = det X.
```

The determinant identity is exact:

```text
c^2 J bar(J) = eta^-2 eta^2 = 1.
```

## 2. Torsion normalization removes the central sign ambiguity

[candidate-T / L4]

The central sign is fixed algebraically, not by an archimedean positivity
choice.

Since

```text
J - 1 = zeta^2,
```

and `p` is odd,

```text
zeta = (J-1)^((p+1)/2).
```

Indeed

```text
(zeta^2)^((p+1)/2) = zeta^(p+1) = zeta.
```

The two determinant-preserving scalar choices satisfy

```text
(+eta^-1) J = zeta,    ord(zeta) = p,
(-eta^-1) J = -zeta,   ord(-zeta) = 2p.
```

Therefore the normalization is uniquely frozen by

```text
ord(cJ) = p.
```

Equivalently,

```text
cJ = zeta = (J-1)^((p+1)/2).
```

At the ramified prime this is also equivalent to selecting the root satisfying

```text
cJ == 1 mod P,
```

rather than the order-`2p` root `-zeta == -1 mod P`.

This determines the operator. It does not label either quadratic sheet as a
future or past sheet.

## 3. First ramified neighborhood

[candidate-T / L4]

The extension `K/F` is tamely ramified of degree two at the prime over `p`.
Thus

```text
mathfrak_p O_K = P^2.
```

Consequently

```text
B_p := O_K / mathfrak_p O_K
     ~= O_K/P^2
     ~= F_p[eps]/(eps^2).
```

With

```text
eps = 1-zeta mod P^2,
```

complex conjugation satisfies

```text
bar(eps) = -eps.
```

The involution is therefore trivial on the residue field but survives in the
first ramified neighborhood as the sign on the nilpotent direction.

Every Hermitian element of the special fiber has a unique form

```text
X(a,b,c0,d)
 = [[a, c0+d eps],
    [c0-d eps, b]],

a,b,c0,d in F_p.
```

Its determinant is

```text
q(X) = ab - (c0+d eps)(c0-d eps)
     = ab - c0^2.
```

Thus the nilpotent anti-invariant coordinate `d` is invisible to the quadratic
null equation.

The radical is exactly

```text
L_ram
 = { X(0,0,0,d) : d in F_p },
```

and has `p` points.

## 4. Canonical square-class double sheet

[candidate-T / L4]

Consider the nonradical null locus

```text
Q_p^x = { X : q(X)=0 } minus L_ram.
```

Its residue-field symmetric matrix is

```text
M_X = [[a,c0],[c0,b]].
```

For every `X in Q_p^x`, `M_X` is nonzero of rank one. Hence

```text
M_X = mu x x^T
```

for some `mu in F_p^x` and nonzero `x in F_p^2`.

The square class

```text
[mu] in F_p^x/(F_p^x)^2 ~= C_2
```

is independent of the representation. If

```text
mu x x^T = nu y y^T,
```

then `y=t x` for some nonzero `t` and `mu/nu=t^2`.

Therefore the nonradical null locus has a canonical algebraic two-sheet
partition

```text
L_square,
L_nonsquare.
```

This is a square-class partition. No order, positivity, future/past label, or
physical interpretation is included.

The ternary residue-field cone `ab=c0^2` has `p^2` points, of which one is the
zero matrix. The nilpotent coordinate `d` is free. Hence

```text
|{q=0}|       = p^3,
|L_ram|       = p,
|Q_p^x|       = p^3-p,
|L_square|    = p(p^2-1)/2,
|L_nonsquare| = p(p^2-1)/2.
```

The Hermitian-square cone

```text
C_p^square = { v v^dagger : v in B_p^2 }
```

is exactly

```text
{0} union L_square,
```

so

```text
|C_p^square| = 1 + p(p^2-1)/2.
```

## 5. The sheet invariant already factors through the residue field

[candidate-T / L4]

The sheet class depends only on `(a,b,c0)` and is independent of `d`.
Therefore the first ramified neighborhood restores the involution but does not
enrich the sheet invariant outside the vertex.

In particular,

```text
C_p^square intersect L_ram = {0}.
```

The first-order Jordan direction is the `eps` direction. On the off-diagonal
pair `(c0,d)`, multiplication by

```text
zeta = 1-eps
```

has the unipotent form

```text
(c0,d) -> (c0,d-c0),
```

with nilpotent part

```text
N(c0,d) = (0,-c0),
N != 0,
N^2 = 0,
im N = ker N = L_ram.
```

This Jordan information lands in the radical direction that the square-class
sheet invariant does not read.

Exact negative content:

```text
first ramified neighborhood: involution restored,
sheet invariant:             residue-field pullback,
Jordan direction:            invisible to sheet class outside the vertex.
```

No impossibility statement about every conceivable additional marking is made.

## 6. Mod-8 action classification

[candidate-T / L4]

The two canonical sheets are acted on by square classes.

For the antipode

```text
X -> -X,
```

the sheet multiplier is `-1`, so the sheet character changes by

```text
chi_p(-1).
```

For the torsion-normalized operator `R`, reduction modulo `P` gives

```text
eta == 2,
c   == 2^-1,
J   == 2,
zeta == 1.
```

If

```text
M_X = mu x x^T,
```

then the residue action is

```text
M_(RX)
 = 2^-1 diag(2,1) M_X diag(2,1)
 = (2^-1 mu) y y^T
```

for `y=diag(2,1)x`. Therefore the `R` sheet character changes by

```text
chi_p(2^-1) = chi_p(2).
```

The complete action law is consequently determined by

```text
(chi_p(-1), chi_p(2)),
```

hence by `p mod 8`:

```text
p mod 8 | antipode | R
--------+----------+------
1       | fix      | fix
3       | swap     | swap
5       | fix      | swap
7       | swap     | fix
```

This is the correct attribution surface. No row of the table selects a unique
prime.

## 7. The p = 5 specialization

[candidate-T / L4, attribution to the full p == 5 mod 8 class]

For `p=5`,

```text
eta = zeta_5 + zeta_5^-1 = phi^-1,
c   = eta^-1 = phi,
R(u,v,w) = (phi^-1 u, phi v, zeta_5 w).
```

At the first ramified neighborhood,

```text
B_5 ~= F_5[eps]/(eps^2),
bar(eps)=-eps.
```

The exact counts are

```text
|{q=0}|       = 125,
|L_ram|       = 5,
|L_square|    = 60,
|L_nonsquare| = 60,
|C_5^square|  = 61.
```

The Legendre values are

```text
chi_5(-1)=+1,
chi_5(2)=-1.
```

Therefore

```text
antipode: fixes each algebraic sheet,
R:        swaps the two algebraic sheets.
```

Also

```text
C_5^square = -C_5^square.
```

This last identity does not collapse the double sheet. It states only that
`-1` is a square modulo five, so the antipode preserves each square-class
sheet.

The `p=5` result is not unique to five. The same fix/swap pattern occurs for
every prime `p == 5 mod 8`.

## 8. Attribution firewall

[candidate-D / interpretation boundary]

The following parts are uniform and carry no `p=5` selection content:

```text
J = zeta eta,
eta is a unit,
determinant normalization,
ord(cJ)=p torsion normalization,
B_p ~= F_p[eps]/eps^2,
bar(eps)=-eps,
q=ab-c0^2,
canonical square-class double sheet,
first-order Jordan direction,
mod-8 action classification.
```

The `p=5` specialization contributes only its membership in the congruence
class `p == 5 mod 8` and the already known identities

```text
eta=phi^-1,
c=phi.
```

This note is therefore not evidence selecting five, `K=Q(zeta_5)`, or the
TWIST-J axiom.

## 9. Typed open boundary

[O / NON-CANONICAL TYPING DEBT]

No physical reading of the two sheets is defined.

The missing slot is

```text
D_sheet : {L_square,L_nonsquare} -> PhysicalData.
```

Any future candidate must freeze at least

```text
domain,
codomain,
physical context,
equality or equivalence relation,
overlap rule,
independently justified measurable distinction,
occurrence or selection rule if outputs differ.
```

Until such a typed reading exists, the statements

```text
R fixes a sheet,
R swaps sheets,
antipode fixes a sheet,
antipode swaps sheets
```

are algebraic congruence facts only. They are not a time arrow, causal flip,
future/past distinction, event, occurrence law, measurement, Born rule,
physical dynamics, or L5/L6 conclusion.

The ramified place therefore speaks to the quadratic form and its canonical
square-class decomposition, but no public map presently assigns a physical
label to either class.

## 10. Dispositions from this side branch

[NON-CANONICAL BOOKKEEPING]

### D1. Standalone norm-one fold not pursued

The proposed fold based on

```text
dim_R T_K^1(R)=3=1+2
```

was rejected as a new J-specific row. The same decomposition occurs for every
totally imaginary quartic field. After attribution, the J-specific regulator
and torsion content are already owned by existing public theorem rows.

This disposition does not weaken the completed theorem scope of
`P-J-NORM-TRACE-TANGENT-SEAM-1`. It says only that no additional standalone
J-row is earned by the `3=1+2` decomposition.

### D2. Proposed ramified-Jordan formal probe not pursued

A proposed probe whose positive clauses were

```text
dim L_ram = 1,
N != 0,
N^2 = 0,
im N = ker N = L_ram
```

was rejected before any formal probe lock or pin. In the frozen odd-prime
carrier those clauses are structural consequences of the first ramified
neighborhood and do not define a genuine scientific decision surface.

The Jordan calculation is retained here as a lemma, not as evidence-bearing
formal computation.

### D3. Corrected interpretation of C_5^square = -C_5^square

The identity does not mean the algebraic double sheet disappears. The
nonradical null locus still has two canonical square classes of 60 points each.
The identity means that the antipode acts within, rather than between, those
classes.

### D4. Corrected central-sign objection

A temporary objection claimed that determinant preservation left an
unresolvable choice `c=+/-eta^-1`. That objection is rejected.

The J-native torsion condition

```text
ord(cJ)=p
```

selects `c=eta^-1` because the alternatives have orders `p` and `2p`.
This fixes the operator but still does not label either square-class sheet as
future or past.

## 11. Return point

[O / NON-CANONICAL]

If this branch is revisited, do not reopen the killed fold or the killed Jordan
probe. Start from the typed debt:

```text
D_sheet does not exist.
```

A future positive route must derive or independently justify a physical
meaning for the square-class distinction. A future negative route must freeze
a complete admissible reading class before claiming that no such meaning can
exist.

Until then the mathematical endpoint is complete enough for reuse:

```text
odd p cyclotomic ramified Hermitian carrier
  -> first ramified involution survives
  -> determinant ignores the nilpotent sheet coordinate
  -> nonradical null cone has two canonical square-class sheets
  -> antipode/R sheet action is classified by p mod 8
  -> p=5 lies in the fix/swap branch
  -> no physical sheet label is supplied.
```
