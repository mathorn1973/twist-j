# C-COAXIAL-CENTER-CHARACTER-CENSUS-N: the center-compatible sign characters of the surviving coaxial group

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-T census, decision NONUNIQUE
ACTION LAYER:           L1 ALGEBRAIC STATE
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        NONE
PUBLIC OBJECT LOCK:     issue #686
SOURCE LANES:           notes/C-COAXIAL-INTEGRAL-2I-STEP-N (merged),
                        notes/C-COAXIAL-STEP-READING-FAMILY-N (merged)
WORKING MAP:            notes/PRACOVNI-MAPA-V71-2026-08-30, section 9.1
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
PROMOTION:              NONE
```

This note executes the first ordered step of the v71 working map: a complete
census of the sign characters of the surviving coaxial group that are
compatible with the spinor center. The frozen class is small by design, the
decision set is `UNIQUE / NONUNIQUE / EMPTY / STOP`, and the proven outcome
is **NONUNIQUE**, matching the expectation the map declared before this
census was executed. The census answers the map's question: the
ramified-reduction clause in the merged coaxial readout is a genuine
additional selection datum, not a consequence of central compatibility
alone.

## 1. Scope firewall

The domain is imported, frozen, from the merged source lanes: the surviving
determinant-one coaxial inverse-pair group

\[
S=\{\,q(r,m)=\zeta_{10}^{\,r}\varphi^{\,2m}\,\}
\;\cong\;\mu_{10}\times\langle\varphi^2\rangle,
\]

on the fixed labeled icosian placement of
[`C-COAXIAL-INTEGRAL-2I-STEP-N`](../C-COAXIAL-INTEGRAL-2I-STEP-N/README.md),
with the injective parametrization \((r\bmod 10,\ m\in\mathbb Z)\) and the
ramified readout \(\varepsilon\) of
[`C-COAXIAL-STEP-READING-FAMILY-N`](../C-COAXIAL-STEP-READING-FAMILY-N/README.md).
All placement conditions and firewalls of those lanes are inherited
unchanged; this census re-proves none of them and is silent outside them.

The census classifies **only** group homomorphisms \(\chi:S\to\{\pm1\}\).
It does not classify all admissible readings of \(S\), does not classify
characters into larger targets, does not select a physical decoder, makes
no statement about the canonical update \(U\), and creates no apparatus,
event, occurrence law, L5 stream, or L6 measure. The outcome `NONUNIQUE`
fires no registered falsifier: per the reading-family discipline,
nonuniqueness is a falsifier only against a frozen uniqueness claim, and no
registered claim asserts uniqueness of this sign character.

The expected outcome `NONUNIQUE` was declared in the working map before
this census was executed; the census was still run against the full frozen
decision set, with all four outcomes reachable a priori.

## 2. The frozen class

```text
domain:      the surviving coaxial group S, frozen in the source lanes
codomain:    {+1, -1} with exact integer equality
class:       ALL group homomorphisms chi : S -> {+-1}
condition:   chi(-1) = -1   (compatibility with the spinor center)
context:     the source-lane placement and the parametrization (r, m)
equality:    pointwise equality of functions on S
symmetries:  none quotiented; characters are compared as functions
choices:     none beyond the frozen parametrization
decision:    UNIQUE / NONUNIQUE / EMPTY / STOP
```

The class is complete by construction: every homomorphism to \(\{\pm1\}\)
is admitted, and the census closes it exactly.

## 3. Classification

**Written proof (theorem source; the companion program is an audit).**

1. \(S\cong\mathbb Z/10\times\mathbb Z\) through \((r,m)\), with the
   componentwise group law
   \(q(r_1,m_1)\,q(r_2,m_2)=q(r_1+r_2\bmod 10,\ m_1+m_2)\).
2. \(\{\pm1\}\) has exponent two, so every homomorphism factors through
   \(S/S^2\). Squares are exactly the elements with both parameters even,
   hence \(S/S^2\cong\mathbb F_2^2\) through \((r\bmod2,\ m\bmod2)\).
3. A homomorphism is determined by its values on the generators
   \(\zeta_{10}\) and \(\varphi^2\); each value lies in \(\{\pm1\}\), and
   the only relation \(\zeta_{10}^{10}=1\) is respected by every sign.
   Therefore

   \[
   \operatorname{Hom}(S,\{\pm1\})
   =\{\chi_{a,b}:a,b\in\mathbb F_2\},
   \qquad
   \chi_{a,b}\bigl(q(r,m)\bigr)=(-1)^{ar+bm},
   \]

   with exactly four elements.
4. The center is \(-1=\zeta_{10}^5=q(5,0)\), so
   \(\chi_{a,b}(-1)=(-1)^{5a}=(-1)^a\), and the condition
   \(\chi(-1)=-1\) holds exactly when \(a=1\).

> **Census theorem [candidate-T / L1, frozen scope].** The
> center-compatible sign characters of \(S\) are exactly
>
> \[
> \chi_{1,0}\bigl(q(r,m)\bigr)=(-1)^{r},
> \qquad
> \chi_{1,1}\bigl(q(r,m)\bigr)=(-1)^{r+m},
> \]
>
> two in number and distinct (they disagree exactly on the elements with
> odd boost count, witnessed by \(\varphi^2\)). The frozen census decision
> is **NONUNIQUE**, with cardinality exactly two.

The two admissible characters differ by the center-trivial boost parity
\(\chi_{0,1}(q(r,m))=(-1)^m\):

\[
\chi_{1,1}=\chi_{1,0}\cdot\chi_{0,1}.
\]

The kernels are structural: \(\ker\chi_{1,0}=\mu_5\times\langle\varphi^2
\rangle\) (the \(\mu_5\)-membership parity), and
\(\ker\chi_{1,1}=\{\,q(r,m):r+m\ \text{even}\,\}\).

## 4. The selection corollary

The merged readout's ramified leg satisfies, exactly,

\[
\varepsilon(q)=q\bmod\mathfrak p_5=(-1)^{r+m}=\chi_{1,1}(q).
\]

Therefore, inside the frozen class:

- central compatibility alone leaves the boost-parity twist undetermined —
  both \(\chi_{1,0}\) and \(\chi_{1,1}\) survive it;
- the clause "the sign character is realized by the \(\mathfrak p_5\)
  reduction" selects \(\chi_{1,1}\) uniquely.

So the ramified-reduction clause of
`C-COAXIAL-STEP-READING-FAMILY-N` is a genuine additional selection datum,
exactly as the working map asked to decide. This sharpens the bookkeeping
of that lane without degrading it: the lane declared \(\varepsilon\) as a
chosen leg, and the census now proves the choice is a real one-bit
selection, not a forced consequence. Per the reading-family discipline of
`POLICY.md` section 4, any later lane that uses "the" sign character of
\(S\) must either name its selection rule — for instance the ramified
realization above — or leave the corresponding conclusion open, because
the two admitted characters produce inequivalent outputs in the same
context.

## 5. Open obligations

- Characters of \(S\) into larger targets (\(\mu_5\), \(\mu_{10}\), unit
  hyperbola points) are not classified here.
- No structural place-readout realization of \(\chi_{1,0}\) is claimed;
  its description as the \(\mu_5\)-membership parity is a kernel
  statement, not a residue realization.
- No placement-independent statement; the placement classification stays
  open in the source lanes.
- Any promotion requires a fresh formal `probes/P-NAME/` lane under
  `POLICY.md`; the present files authorize no such move.

## 6. Local audit program

The companion file is [`verify.py`](verify.py). It uses only the Python
standard library and exact arithmetic in \(\mathbb Q(\zeta_5)\); every
sweep is exhaustive and deterministic, with no randomness. Its 16 checks
audit the parametrization, the componentwise group law, the square
subgroup, multiplicativity and well-definedness of all four characters,
the exhaustiveness of the classification, the center condition, the
distinctness witness, the twist identity, the exact identity
\(\varepsilon=\chi_{1,1}\) on a 130-element sweep, and the frozen
decision. A failure exits with status 1.

This local verifier is not a formal evidence directory, preregistration,
two-architecture computation gate, or probe. Any future public promotion
must start under a new formal `probes/P-NAME/` lane and follow
`POLICY.md`; the present files authorize no such move.
