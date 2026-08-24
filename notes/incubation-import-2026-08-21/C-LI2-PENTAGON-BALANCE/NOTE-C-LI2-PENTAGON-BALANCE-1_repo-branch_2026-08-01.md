# C-LI2-PENTAGON-BALANCE-1. The golden modulus points as a five-term collapse, the balance against the Galois wall, and what the coincidence is worth

```
NOTE ID:        C-LI2-PENTAGON-BALANCE-1
STATUS:         NON-CANONICAL. Candidate document. No authority.
                Promotes nothing. Edits no normative file.
DATE:           2026-08-01
TARGET LINE:    public (mathorn1973/twist-j) on promotion; nothing promoted now
LAYER:          none declared. Archimedean special values only. No reading,
                no lift, no anchor. Any lift needs its own named gate.
SUPERSEDES:     C-LI2-MODULUS-POINTS-1, proposed but never opened, in
                notes/ARCHITECTURE lane recon of 2026-07-31 section 5.2.
                That proposal is strictly contained in section 3 below.
                One lane, not two.
SIBLING:        C-LI2-RELATIVE-BLOCH-SEAM-2, the hypothesis half, kept
                separate on purpose so that nothing here depends on it.
```

## 0. What this note is

An owner submission proposed a bridge between the registered Galois wall and
the modulus points of `J`, through the Rogers dilogarithm, with two uniqueness
branches and a Bloch-group layer. This note is the audited, corrected, merged
form. It records what was verified exactly, what was broken, what replaced the
broken parts, and what the surviving result is and is not worth.

Two sections of the submission did not survive. They are named in section 5,
with the replacement, rather than quietly dropped.

## 1. Currency gate

Run 2026-08-01 against a fresh clone of `mathorn1973/twist-j` main.

```
STATUS.md       STATE ACTIVE, CANON Public Canon v30, TAG canon-v30,
                AUTHORITY mathorn1973/twist-j main, CUTOVER 2026-07-13,
                CONTENT_COMMIT 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0,
                CANON_SHA256
                2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
                CANON_BYTES 157167
HEAD            b8d4d585820d04ebd008444661f3a71d6e24f423
ANCESTRY        tag canon-v30 and the content commit are both ancestors of main
SHA256SUMS      5 of 5 OK; canon/CANON.md hash and byte count match STATUS.md
GATE            PASS
```

## 2. What is already Canon, and is quoted rather than derived

Roughly half the submission is already in the live registry. It is quoted here
under its registered ids and nothing below is stronger than its source.

```
WALL-LI2-RUNG [T]       Re Li_2(sigma_a(J)) = pi^2/100 for a in {1,4} and
                        9 pi^2/100 for a in {2,3}; the Galois-orbit real-part
                        sum is pi^2/5; the sum divided by zeta(2) is 6/5; and
                        the excess above zeta(2) is pi^2/30. Real parts only,
                        no field-trace claim, no imaginary-part statement.
WALL-CIRCLE-LEMMA [T]   for N >= 3 and 1 <= a <= N-1,
                        Re Li_2(1 + zeta_N^a) = pi^2 (N-2a)^2/(2N)^2, and
                        sum_(a=1)^(N-1) Re Li_2(1 + zeta_N^a)
                          = pi^2 (N-1)(N-2)/(12N).
J-PROJECTIONS [T]       |J| = 1/phi, principal argument 2 pi/5.
```

The value `pi^2/30` is therefore not new. It is printed in the live
`WALL-LI2-RUNG` row. Anyone quoting this note as the discovery of `pi^2/30` is
quoting it wrong.

## 3. What is new, stated exactly

Write `r = |J| = phi^-1` and `L(x) = Li_2(x) + (1/2) log x log(1-x)` for the
Rogers dilogarithm on `0 < x < 1`.

### T1. The golden complement

```
1 - |J| = |J|^2 = J conj(J) = phi^-2
```

exact in `Q(sqrt5)`. The two right-hand members are the registered modulus
chord. This single equation is the engine of everything below: the golden
modulus point is its own complement after one squaring.

### T2. The collapse, and that the collapse forces the golden point

Put `x = y = r` in Abel's five-term relation for `L`. Both right-hand arguments
become `x(1-x)/(1-x^2) = x/(1+x)`. Setting that equal to `x^2` is, as an
integer polynomial identity,

```
x - x^2(1+x) = -x(x^2 + x - 1)
```

so the collapse holds if and only if `x^2 + x - 1 = 0`. The golden point is not
chosen and not fitted. It is the unique positive point at which Abel's relation
degenerates from five terms to two:

```
2 L(r) = 3 L(r^2)
```

### T3. The term-count lemma

Taking the complement relation `L(r) + L(r^2) = zeta(2)` as first row and a
collapse `p L(r) = q L(r^2)` as second row gives the system `[[1,1],[p,-q]]`
with

```
det = -(p + q)
```

verified over all small `(p,q)`. For Abel's relation `(p,q) = (2,3)` and
`det = -5`. So the 5 in the defect is the term count of the functional
equation. That is worth printing, and it is worth stating plainly what it is
not: it is **not** an independent derivation of `p = 5` from the axiom. The
pentagon enters through Abel's relation; it does not come out of it.

### T4. The solved system

```
L(r)   = (3/5) zeta(2) = pi^2/10
L(r^2) = (2/5) zeta(2) = pi^2/15
L(r) - L(r^2) = (1/5) zeta(2) = pi^2/30
```

### T5. The Rogers correction cancels, and Landen follows

With `l = log phi`, both Rogers corrections equal `l^2`, hence

```
L(r) - L(r^2) = Li_2(r) - Li_2(r^2) = pi^2/30
Li_2(phi^-1) = pi^2/10 - log^2 phi
Li_2(phi^-2) = pi^2/15 - log^2 phi
Li_2(phi^-1) + Li_2(phi^-2) + 2 log^2 phi = zeta(2)
```

The last three are Landen's classical values. Here they are consequences, not
inputs. This is the content the retired `C-LI2-MODULUS-POINTS-1` proposal
carried, obtained as a corollary rather than imported.

### T6. The balance

```
sum_(a=1)^4 Re Li_2(sigma_a(J)) = 2 L(|J|) = 3 L(J conj(J)) = (6/5) zeta(2)
```

equivalently `W(J) - zeta(2) = L(|J|) - L(J conj(J)) = (1/5) zeta(2)`.

### T7. Balance selection

For integer `N >= 3`, `N != 4`, let `r_N` be the minimal nonzero modulus among
the `1 + zeta_N^a`, that is `2 sin(pi/2N)` for odd `N` and `2 sin(pi/N)` for
even `N`, and let `W_N` be the wall sum of `WALL-CIRCLE-LEMMA`. Then

```
W_N = 2 L(r_N)     <=>   N = 5
W_N = 3 L(r_N^2)   <=>   N = 5
```

Proof. `W_N/zeta(2) = (N - 3 + 2/N)/2` is strictly increasing for `N >= 3`.
`r_N` is strictly decreasing within each parity class, `sin` being increasing
on `(0, pi/2]`. `L` is strictly increasing on `(0,1)`, since
`L'(x) = -log(1-x)/(2x) - log(x)/(2(1-x))` has both terms positive. So the gap
is strictly increasing within each parity class and has at most one zero per
class. `N = 5` is a zero, both sides being `pi^2/5`. The even class has no
integer zero: the gap is negative at `N = 6` and positive at `N = 8`, so its
single crossing is interior. `N = 4` is excluded because `r_4 = sqrt2 > 1`,
where `L` is not defined. QED.

## 4. What the balance is worth, stated before anyone overreads it

This is the most important paragraph in the note.

By `WALL-CIRCLE-LEMMA`, `W_N/zeta(2) = (N-1)(N-2)/(2N)` is **rational for every
N**. By T4, `L(r)/zeta(2)` and `L(r^2)/zeta(2)` are rational. Both legs of the
balance therefore live, a priori and before any computation, in the same
one-dimensional `Q`-vector space `zeta(2)Q`. The balance is the statement

```
6/5 = 6/5
```

an equality of two rational numbers. It follows that no numerical agreement, at
any precision whatsoever, is evidence for a bridge between the two sides.
Verifying the balance to a thousand digits would add exactly nothing.

All the content is in the two derivations, and they are different derivations:

```
wall leg      Euler reflection plus the boundary evaluation
              Re Li_2(e^(i theta)) = pi^2 B_2(theta/2 pi), a Bernoulli fact
modulus leg   golden complement plus the Abel five-term collapse, a Bloch fact
```

No morphism between them is exhibited. The balance is recorded as an exact
equality of two independently derived rationals. It does not explain anything
yet.

## 5. The two corrections, and the replacement

The submission carried a section 3 with two uniqueness branches. Both were
attacked directly and both fell. They are recorded here rather than removed
silently, per the policy that a fired falsifier is first-class.

### 5.1 The wall-uniqueness branch was a shaped tautology

The condition tested was `Delta_N = zeta(2)/N`. Substituting the exact closed
form `Delta_N/zeta(2) = (N^2 - 5N + 2)/(2N)` turns it into

```
N^2 - 5N + 2 = 2      i.e.      N(N - 5) = 0
```

The equation is its own answer. A condition whose normal form is `N(N-5) = 0`
cannot be evidence that `N = 5` is distinguished; it is that assertion, written
as an equation. True and worthless. Removed.

### 5.2 The modulus-uniqueness branch overclaimed

The submission restricted to odd `N` without justification and then concluded
over the whole root-circle family. For even `N` the minimal nonzero modulus is
`2 sin(pi/N)`, not `2 sin(pi/2N)`. Sweeping both parities over `N = 3..4000`:

```
1 - r_N = r_N^2   holds at   N in {5, 10}
```

because `r_10 = 2 sin(pi/10) = phi^-1` exactly. The five-term collapse happens
at order 10 as well. The printed uniqueness is unique-among-odd-N only.

This is a correction, not a demolition. `Q(zeta_10) = Q(zeta_5)`, so orders 5
and 10 are two root-circle presentations of one field and both present the same
point. The statement that survives is about the field, not the order.

### 5.3 The replacement, and why it is better

T7 tests the candidate's own equation against every order in the family instead
of a condition shaped to have the answer 5. It is not post hoc, and it kills the
`N = 10` counterexample that defeats 5.2:

```
W_10 = (18/5) zeta(2)          2 L(r_10) = (6/5) zeta(2)          not equal
```

So the balance is a strictly stronger selector than the modulus condition alone.
Section 3 of the submission is replaced by T7 in its entirety.

## 6. The Bloch layer, proved part only

The hypothesis half lives in `C-LI2-RELATIVE-BLOCH-SEAM-2` and nothing in this
note depends on it. What is proved here, and was proved in-session rather than
cited:

```
A1  delta([x]) = x wedge (1-x). Since 1 - r = r^2 and 1 - r^2 = r, both wedges
    are multiples of r wedge r and vanish. So [r], [r^2] and
    beta = [r] - [r^2] lie in B(Q(sqrt5)). That field is real quadratic, so
    r_2 = 0 and its Bloch group is finite: beta is torsion by rank, not by
    citation. And 5 L(beta) = zeta(2), so beta is 5-torsion under the standard
    normalisation.
A2  For z = 1 + zeta_N^a we have 1 - z = -zeta_N^a, a root of unity, hence
    torsion, hence delta([z]) = 0 in Lambda^2 tensor Q for EVERY N and a.
    Every wall point is already a Bloch class. Verified in Z[zeta_5]: each
    1 - sigma_a(J) has exact multiplicative order 10.
A3  The submission's explicit five-term expression at (-zeta_5, 1 + zeta_5) is
    a genuine Abel relation. All five arguments verified as exact identities in
    Z[zeta_5]:
        x            = -zeta_5                 = 1 - sigma_3(J)
        y            = 1 + zeta_5              = sigma_3(J)
        (1-x)/(1-xy) = -zeta_5^2               = 1 - J
        1 - xy       = 1 + zeta_5 + zeta_5^2   = zeta_5^2 / J
        (1-y)/(1-xy) = 1 + zeta_5^2 + zeta_5^3 = -(zeta_5 + zeta_5^4) = -|J|
    This was attacked and held.
```

A2 is new relative to the submission and it cuts both ways. There is a genuine
common home: both the modulus points and the wall points are Bloch classes. But
the canonical regulator on `B(Q(zeta_5))` at a complex place is the
Bloch-Wigner function, which is imaginary-part data, while the Canon's wall
operator is `Re Li_2`, real-part data and explicitly not a field trace. The two
are orthogonal components of the same `Li_2` values, and the wall sits on the
component the Bloch regulator does not see. Combined with section 4, any
relative-regulator route must explain a rational, with an operator that is
provably not the Bloch-Wigner regulator, and cannot be tested numerically even
in principle. That is stated in the sibling note as its governing difficulty.

## 7. Decoder and channel bookkeeping

Three findings. The negative one is worth more than the other two.

### 7.1 The Rogers dilogarithm is a named cross-channel bridge

At the golden point the ordinary dilogarithm mixes both `J` axes, carrying both
`pi^2` and `log^2 phi` (T5). The Rogers counterterm `(1/2) log x log(1-x)` is
exactly a modulus-channel counterterm, and at the golden point it removes the
`log^2 phi` content completely, leaving rational multiples of `zeta(2)`. So `L`
has a modulus carrier and an argument value. That is a named bridge in one
line, and it is cleaner than the Landen partition of the retired
`C-LI2-MODULUS-POINTS-1`, which still carries `2 log^2 phi` explicitly.

### 7.2 It does not supply a modulus anchor. Negative result, recorded.

The 2026-07-31 recon left this open. It is now answered and the answer is no.

```
zeta(2)/5 is dimensionless. The Rogers bridge moves the modulus point's VALUE
onto the argument axis. It does not supply a SCALE. An SI anchor requires a
measured quantity and nothing here is measured.
```

Therefore no frontier row moves. `METRO-EDGE-SCALE [O]` is untouched.
`CURVATURE-OPERATOR-CANONICAL [O]` is untouched. Anyone tempted to read the
golden rationalisation as an anchor should stop at this paragraph.

### 7.3 A repair to a channel classification, before it is written

A channel classification keyed on value type alone files this lane as
argument-side and never notices that it touches the modulus axis at all:

```
carrier channel   MODULUS    (r = |J| = phi^-1,  J conj(J) = phi^-2)
value channel     ARGUMENT   (rational multiples of zeta(2))
```

Carrier channel and value channel must be two separate fields, with a named
bridge defined as precisely a row where the two differ. Cheapest possible
moment to fix that is before the classification is preregistered.

### 7.4 The lift this note refuses

The coefficients 2 and 3 in T2 and T6 are the left and right term counts of
Abel's relation. They take those values at every point where the collapse
occurs and carry no dependence on `J` whatsoever. They are **not** two forces
and **not** three spatial dimensions. There is nothing here for a decoder
reading to attach to. The temptation is named explicitly because `p = 5` and
`d = 3` are program constants and the reading is otherwise easy to slip into.

## 8. Explicit non-claims

```
1  No field-trace claim. No imaginary-part claim. Im Li_2(J) is not zero.
2  No morphism between the wall derivation and the modulus derivation.
3  No physical lift, no layer, no anchor, no SI statement.
4  No claim that the 5-torsion of beta and the order-5 cyclotomy are the same
   5. They are both 5 and that is all that is shown.
5  T7 selects an ORDER, not a field. Q(zeta_10) = Q(zeta_5).
6  Nothing here is stronger than WALL-LI2-RUNG or WALL-CIRCLE-LEMMA.
```

## 9. Falsifiers

```
F1  x - x^2(1+x) = -x(x^2+x-1) fails
F2  2 L(phi^-1) != 3 L(phi^-2), or either differs from 3 zeta(2)/5, 2 zeta(2)/5
F3  the Galois-orbit real-part sum differs from (6/5) zeta(2)
F4  det [[1,1],[p,-q]] != -(p+q) for some p, q
F5  some integer N >= 3, N != 4, other than 5 satisfies W_N = 2 L(r_N) or
    W_N = 3 L(r_N^2)
F6  monotonicity (i), (ii) or (iii) in the T7 proof fails
F7  1 - r_N = r_N^2 holds at some N outside {5, 10}
F8  any of the five Abel arguments at (-zeta_5, 1 + zeta_5) differs from the
    printed value in Z[zeta_5]
F9  delta([1 + zeta_N^a]) is shown nonzero in Lambda^2 tensor Q for some N, a
F10 either pinned script fails on exact re-run at the recorded hash
```

All ten are exact. None is a threshold that can be moved after the fact.

## 10. Evidence, grade, and what a public probe would still need

```
verify_li2_pentagon_balance_1.py   67 checks, 0 failures
  every assertion exact: Fraction, Q(sqrt5) pairs, Z[zeta_5] integer vectors,
  integer polynomial identities. Decimals appear only on lines tagged WITNESS
  and are never asserted against.
break_li2_pentagon_balance_1.py    29 checks, 0 failures, 2 hits
  deliberately a different code path: Li_2 by Simpson quadrature of
  -log(1-t)/t, not the verifier's Bernoulli series; uniqueness attacked by
  exhaustive sweep rather than by proof; the odd-N restriction challenged.
  The two hits are sections 5.1 and 5.2, both removed above as a result.
hashes                             see SHA256SUMS in this directory
platform                           Ubuntu 24.04, x86_64, Python 3.11.
```

Grade is **audit, not probe**, and the note says so rather than letting a reader
assume otherwise:

```
1  the verifier was written after the source material was read, so there is no
   pin before first execution
2  one architecture only; no byte-identity leg
3  notes/ is not reproduced by the pull-request gate, by design
```

A public probe on this lane would need a fresh preregistration with the six
fields, a pin on `probe/P-LI2-PENTAGON-BALANCE-1` before first execution, and
two architectures with byte-identical stdout. Nothing in this note is a
substitute for that, and nothing here authorises a registry, frontier or Canon
edit.
