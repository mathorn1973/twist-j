# C-COAXIAL-STEP-READING-FAMILY-N: one frozen candidate readout for the surviving coaxial ladder

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-T skeleton, candidate-D reading
ACTION LAYER:           L1 ALGEBRAIC STATE, L4 Hermitian-carrier boundary only
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        NONE
PUBLIC OBJECT LOCK:     issue #682
SOURCE LANE:            C-COAXIAL-INTEGRAL-2I-STEP-N (issue #680, PR #681)
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
PROMOTION:              NONE
```

The source lane, at commit
`8b6f10ec5ac2f6a67c07cac1b1dbc47f941d3497` of PR
[#681](https://github.com/mathorn1973/twist-j/pull/681), proves that on one
fixed labeled icosian placement, the
determinant-one coaxial inverse-pair steps that preserve the marked orbit
lattice are exactly those with even golden exponent, so the surviving
rapidities are `4 Z log phi`. This note takes the next step the reading-family
discipline of `POLICY.md` section 4 demands before any physical use: it
freezes one total, fully typed candidate readout for those surviving steps,
exhibits its exact values, and proves that this chosen readout decodes the step
exactly. The exact statements are `candidate-T`; the physical wording is a
frozen `candidate-D` dictionary. This note does not classify all readings
admissible under `POLICY.md` section 4 and does not prove compatibility among
alternative readings. Both questions remain open. Nothing here earns a public
status.

## 1. Scope firewall

Every statement below assumes the full frozen placement of the source lane:

1. one fixed, labeled binary icosahedral group `2I` in the fixed splitting
   \(B=(K/F,\sigma,-1)\), with the fivefold element \(\omega\) split as
   \(M(\omega)=\operatorname{diag}(\zeta_5,\zeta_5^{-1})\);
2. steps diagonal in the eigenbasis of that fixed fivefold element;
3. the explicit orbit lattice \(\Lambda=F_\Lambda\mathcal O_K^2\) built from
   the split images of \(1\) and \(i\);
4. determinant-one inverse pairs \(D(q)=\operatorname{diag}(q,q^{-1})\) with
   \(q\) in the displayed unit family.

The candidate readout is asserted only for the surviving subgroup on this
placement. Removing any condition leaves this note silent. No
placement-independent statement is made; the classification of differently
embedded or differently labeled `2I` placements remains open in the source
lane.

**No transfer to the canonical update \(U\) is allowed**, exactly as in the
source lane. This note is also **not** the registered decoder interface:
`D_matter`, `D_geom`, and `D_clock` acquire no content here, and no move is
made on `QUADRATIC-DECODER-DATA [O]`, `DEF-DECODER-COMPLETION-CONTRACT`, any
`QDD` row, `MINIMAL-READ-DERIVATION`, or the apparatus lanes. There is no
apparatus, realized event, occurrence law, sampling law, L5 stream, or L6
measure. The word *decode* below names one explicit inverse map of one frozen
readout tuple and nothing more.

The Hermitian-carrier calculation is an L4 boundary calculation only. It
makes no unnamed physical lift from the L1 algebraic state to L4.

Per the reading-family discipline, the boost leg below is selected
structurally as the restriction of an already registered reading, before and
independently of any target measurement; it is used to explain no measurement.
The other legs are frozen here at candidate status. If a later lane compares
any value below to a measurement, that lane must cite this readout as frozen
here, before the comparison.

## 2. Compatibility with registered rows and existing lanes

- The source lane
  `C-COAXIAL-INTEGRAL-2I-STEP-N` (issue
  [#680](https://github.com/mathorn1973/twist-j/issues/680), PR
  [#681](https://github.com/mathorn1973/twist-j/pull/681)), pinned here at
  commit `8b6f10ec5ac2f6a67c07cac1b1dbc47f941d3497`, supplies the diagonal
  lattice lemma and the universal survival criterion. The proof in this note
  depends on those imported results. The companion verifier reconstructs the
  orbit lattice and performs a finite exact regression audit of the survival
  criterion; that finite sweep is not an independent proof of the universal
  statement. PR #681 must therefore land before this note can leave draft.
- `BOOST-READING-SPLIT [T]` and `BOOST-COUNT-LADDER [D]` own the public
  golden boost ladder for \(k\geq0\): index \(k\) read as rapidity
  \(k\log\varphi\),
  velocity \(\beta_k=S_k/C_k\), Einstein composition as index addition. The
  readout below introduces **no new positive-orientation velocity value**:
  for \(m\geq0\), its boost leg is the registered ladder restricted to
  indices \(4\mathbb Z_{\geq0}\). The branch \(m<0\) is the candidate inverse
  extension derived in this note, not part of the cited registered range.
  Spinor inverse pairs reach exactly the even indices \(2\mathbb Z\); the
  lattice criterion halves that to \(4\mathbb Z\) for the full inverse-pair
  group.
- `CENTRAL-LIFT-PHASE [T]` concerns the central lift
  \(g_J=\operatorname{diag}(s,s^{-1})\) with \(s=\zeta_{10}/\sqrt\varphi\),
  which is not an algebraic-integer unit and not in the domain below. The
  two objects stay distinct.
- The public meanings of \(\log\varphi\) in `BOOST-COUNT-LADDER`, of
  \(2\log\varphi\) in the regulator, Mahler-measure, and toral-entropy rows,
  and of the step \(4\log\varphi\) here concern different objects; no
  identification is claimed.
- The determinant \(-1\) sign-twisted step of
  [`C-COMMON-CARRIER-ICOSIAN-1`](../C-COMMON-CARRIER-ICOSIAN-1/C-COMMON-CARRIER-ICOSIAN-1.md)
  lies outside the inverse pairs and outside this domain; nothing here
  touches it.
- The parallel drawn in section 5 to the two projections of
  `J-PROJECTIONS [T]` is attribution of wording only, not a new claim and
  not evidence for the axiom.

## 3. Exact setting

Let

\[
K=\mathbb Q(\zeta_5),\qquad
F=\mathbb Q(\sqrt5),\qquad
\mathcal O_K=\mathbb Z[\zeta_5],\qquad
\mathfrak p_5=(1-\zeta_5),
\]

\[
\varphi=-(\zeta_5^2+\zeta_5^3),\qquad
\zeta_{10}=-\zeta_5^3.
\]

The frozen unit family is

\[
\mathcal U=\{\,q_{r,n}=\zeta_{10}^{\,r}\varphi^{\,n}
: r\in\mathbb Z/10,\ n\in\mathbb Z\,\},
\]

and the parametrization is injective: \(\varphi\) is real and greater than
one, so the archimedean modulus determines \(n\), and the torsion factor then
determines \(r\). That \(\mathcal U\) exhausts \(\mathcal O_K^\times\) is
classical but is **not used**: the domain below is frozen as \(\mathcal U\).

The placement is the source lane's: the labeled `2I` with
\(M(\omega)=\operatorname{diag}(\zeta_5,\zeta_5^{-1})\), and the orbit
lattice \(\Lambda=F_\Lambda\mathcal O_K^2\) with

\[
F_\Lambda=
\begin{pmatrix}
1&a\\
0&b
\end{pmatrix},
\qquad
a=-\frac{\zeta_5^3}{1-\zeta_5},
\qquad
b=\frac{2+4\zeta_5+\zeta_5^2+3\zeta_5^3}{5},
\]

whose columns are the split images of the icosians \(1\) and \(i\).

By the source lane's diagonal lattice lemma, restricted to inverse pairs and
checked here only by a finite regression audit,

\[
D(q_{r,n})\Lambda=\Lambda
\;\Longleftrightarrow\;
q\equiv q^{-1}\pmod{\mathfrak p_5}
\;\Longleftrightarrow\;
n\in2\mathbb Z.
\]

Writing \(n=2m\), the **surviving coaxial group** is

\[
S=\{\,\zeta_{10}^{\,r}\varphi^{\,2m}\,\}
\;\cong\;\mu_{10}\times\langle\varphi^2\rangle,
\]

with the surviving rapidities \(\eta=2\log|q|=4m\log\varphi\).

## 4. The frozen candidate readout

Per `POLICY.md` section 4, this one candidate readout freezes all five data:

```text
domain:      the surviving coaxial group S on the fixed placement
codomain:    mu_5  x  H(F)  x  {+1,-1},
             H(F) = { (c,s) in F x sqrt5 F : c^2 - s^2 = 1 }
context:     the labeled placement (2I, omega, eigenbasis, Lambda),
             the principal archimedean embedding (boost orientation),
             the fivefold phase orientation zeta_5,
             the residue conventions at p_5 and (2)
equality:    componentwise exact equality in the stated codomains
overlaps:    the boost leg equals the registered BOOST-COUNT-LADDER
             reading at index 4m for m >= 0; the negative branch is the
             candidate inverse extension defined here; this chosen map
             assigns exactly one tuple to each step
```

The group operation on \(H(F)\) is

\[
(c,s)\cdot(c',s')=(cc'+ss',\,cs'+sc'),
\]

with unit \((1,0)\) and inverse \((c,s)^{-1}=(c,-s)\). Thus the displayed
codomain is a direct product of explicitly defined groups. The existence,
classification, and mutual compatibility of other candidate readings on the
same domain remain open under `POLICY.md` section 4. In particular, the
single-valuedness of this map is not a uniqueness claim among admissible
readings.

The three legs, for \(q=\zeta_{10}^{\,r}\varphi^{\,2m}\in S\):

1. **Phase leg.** \(\tau(q)=q/\bar q=\zeta_5^{\,r}\in\mu_5\).
2. **Boost leg.**
   \(b(q)=(\gamma,\gamma\beta)
   =\bigl(\tfrac{L_{4m}}2,\ \tfrac{\sqrt5}2F_{4m}\bigr)\in H(F)\),
   the exact point with
   \(\cosh\eta=\gamma\), \(\sinh\eta=\gamma\beta\), \(\eta=4m\log\varphi\).
3. **Ramified sign.** \(\varepsilon(q)=q\bmod\mathfrak p_5\in\{\pm1\}\subset
   \mathbb F_5^\times\), with the closed form
   \(\varepsilon(q)=(-1)^{r+m}\).

The two-adic readout \(\kappa(q)=q\bmod 2\in\mathbb F_{16}^\times\) is a
context-key readout, determined by the triple; section 8 states exactly what
it sees.

Declared symmetries: the center \(q\mapsto-q\) flips \(\varepsilon\) only;
inversion \(q\mapsto q^{-1}\) sends \((\tau,(c,s),\varepsilon)\) to
\((\bar\tau,(c,-s),\varepsilon)\); the Galois phase reorientations
\(\zeta_5\mapsto\zeta_5^k\) act coherently on the phase leg. Readings are
compared only at fixed context keys.

## 5. The readout is the eigenvalue reading of the Hermitian action

On the Hermitian carrier in the light-cone frame of the fixed eigenbasis,
the surviving step acts as

\[
D\,\begin{pmatrix}x_+&w\\ \bar w&x_-\end{pmatrix}D^{*}
=
\begin{pmatrix}
\varphi^{4m}x_+ & \tau(q)\,w\\
\overline{\tau(q)}\,\bar w & \varphi^{-4m}x_-
\end{pmatrix}.
\]

After complexifying the real Hermitian carrier, the spectrum of the step
action is exactly
\(\{\varphi^{4m},\varphi^{-4m},\zeta_5^{\,r},\zeta_5^{-r}\}\). In the fixed
phase orientation, the complex transverse coordinate \(w\) has eigenvalue
\(\tau(q)=\zeta_5^{\,r}\), while \(\bar w\) has the conjugate eigenvalue.
The modulus pair on the cone axes is the boost leg, and the argument pair on
the transverse plane is the phase leg. The readout is therefore not an added
decoration; it is the complete archimedean eigenvalue data of this step on
the complexified carrier, split into modulus and argument in the same sense
in which `J-PROJECTIONS [T]` splits the axiom (attribution of wording only).

Two exact companions:

- **Adjoint-to-step phase.** \(D^{*}D^{-1}
  =\operatorname{diag}(\zeta_5^{-r},\zeta_5^{\,r})
  =M(\omega)^{-r}\in\rho(2I)\). This ratio measures the difference between
  \(D^*\) and \(D\), so it records self-adjointness: it is the identity
  exactly when \(D^*=D\). It does **not** measure isometry or unitarity. The
  adjoint-to-step phase is exactly the fivefold tick opposite to the phase
  exponent, and it stays inside the labeled group. This generalizes the single
  \(D^{*}D^{-1}=\rho(\omega^{-1})\) check of the source lane.
- **The axiom's square.** With \(J=\zeta_5\varphi^{-1}\) exactly, the source
  lane's representative
  \(q^\ast=\zeta_{10}\varphi^{-2}=-\zeta_5J^2\) is selected only after
  fixing \(\tau=\zeta_5\), hence \(r\equiv1\pmod5\), choosing the contracting
  orientation \(m=-1\), and choosing the center representative
  \(r=1\pmod{10}\). It is then the noncompact survivor with smallest
  \(|m|>0\) in that oriented phase and center class. Multiplication by the
  center gives \(-q^\ast\); inversion reverses the boost orientation and
  conjugates the phase. Thus \(q^\ast\) is not an unqualified first element
  of \(S\). Its modulus reading
  \(\varphi^{-2}=|J|^2\) is the square of the axiom's modulus projection,
  and its phase reading is the single tick \(\zeta_5\).

## 6. Boost-leg values: the half-Lucas ladder

For every count \(m\),

\[
\gamma_m=\frac{L_{4m}}2,\qquad
\gamma_m\beta_m=\frac{\sqrt5}2F_{4m},\qquad
\beta_m=\frac{\sqrt5\,F_{4m}}{L_{4m}},\qquad
L_{4m}^2-5F_{4m}^2=4,
\]

so every reading value lies on the exact unit hyperbola
\(\gamma^2-(\gamma\beta)^2=1\). The ladder of Lorentz factors is half-Lucas:

\[
\gamma_0,\gamma_1,\gamma_2,\gamma_3,\gamma_4,\dots
=1,\ \tfrac72,\ \tfrac{47}2,\ 161,\ \tfrac{2207}2,\dots
\]

with the one-step recurrence \(\gamma_{m+1}=7\gamma_m-\gamma_{m-1}\) and the
half-integer step matrix

\[
\frac12\begin{pmatrix}7&15\\3&7\end{pmatrix}\in SL_2\!\bigl(\mathbb Z[\tfrac12]\bigr)
\quad\text{acting on}\quad
\Bigl(\tfrac{L_{4m}}2,\ \tfrac{F_{4m}}2\Bigr).
\]

Einstein composition is count addition,

\[
\beta_{m_1}\oplus\beta_{m_2}
=\frac{\beta_{m_1}+\beta_{m_2}}{1+\beta_{m_1}\beta_{m_2}}
=\beta_{m_1+m_2},
\]

which is the registered index-addition law of `BOOST-READING-SPLIT [T]`
on the nonnegative submonoid \(4\mathbb Z_{\geq0}\). The same formula for
negative counts is the candidate inverse extension derived here; it is not
attributed to the registered row. The verifier audits the group formula
exactly on its finite regression range.

On the Pell conic \(t^2-5x^2=1\) the reading points are
\((L_{4m}/2,\,F_{4m}/2)\). On the positive branch, the first positive
nontrivial surviving point is the half-integer point
\((\tfrac72,\tfrac32)\) at \(m=1\); the classical integer fundamental
\((9,4)\) sits at the registered index six, which the lattice excludes
(\(n=3\) is odd, and \(D(\varphi^3)\) breaks \(\Lambda\)); the first
positive nontrivial surviving integer point is \((161,72)\) at count
\(m=3\). The excluded primitive noncompact spinor step
\(u=\zeta_{10}\varphi^{-1}\) of the source lane would have read
\(\gamma=\tfrac32\); on the positive orientation, the lattice's first
admitted nontrivial Lorentz factor is \(\gamma=\tfrac72\) with
\(\beta=\tfrac{3\sqrt5}7\).

Sample readings:

| \(q\) | \((r,m)\) | \(\tau\) | \(\gamma\) | \(\gamma\beta\) | \(\varepsilon\) |
|---|---|---|---|---|---|
| \(1\) | \((0,0)\) | \(1\) | \(1\) | \(0\) | \(+1\) |
| \(-1\) | \((5,0)\) | \(1\) | \(1\) | \(0\) | \(-1\) |
| \(\zeta_{10}\) | \((1,0)\) | \(\zeta_5\) | \(1\) | \(0\) | \(-1\) |
| \(\varphi^2\) | \((0,1)\) | \(1\) | \(\tfrac72\) | \(\tfrac{3\sqrt5}2\) | \(-1\) |
| \(q^\ast=-\zeta_5J^2\) | \((1,-1)\) | \(\zeta_5\) | \(\tfrac72\) | \(-\tfrac{3\sqrt5}2\) | \(+1\) |
| \(-\varphi^6\) | \((5,3)\) | \(1\) | \(161\) | \(72\sqrt5\) | \(+1\) |

## 7. Exactness: the readings decode the step

With multiplication in \(\mu_5\), the hyperbola group law of section 4, and
multiplication in \(\{\pm1\}\), the total readout
\(R=(\tau,b,\varepsilon)\) is a group homomorphism from \(S\) to the stated
direct-product codomain, and:

- the archimedean pair \((\tau,b)\) has kernel exactly the center
  \(\{\pm1\}\): the physical legs alone read the step projectively, in the
  spinor double-cover sense;
- the ramified sign restores the center: the triple \(R\) is **faithful**;
- the inverse on \(\operatorname{im}R\) is explicit. Given a tuple
  \((\zeta_5^{\,a},(c,s),\varepsilon)\in\operatorname{im}R\):
  the hyperbola point determines \(m\) (the half-Lucas ladder is strictly
  monotone in \(|m|\) and \(s\) carries the sign); then

  \[
  r\equiv a\pmod 5,
  \qquad
  r\equiv m+\tfrac{1-\varepsilon}2\pmod 2,
  \]

  and the Chinese remainder theorem gives \(r\bmod 10\), hence
  \(q=\zeta_{10}^{\,r}\varphi^{\,2m}\).

So the chosen frozen readout loses nothing: the surviving coaxial step is
exactly reconstructible from its fivefold tick phase, its exact boost data,
and its ramified sign. The sweep audits in the verifier check kernel,
faithfulness, and the decode map element by element on a finite regression
range. No decoder is asserted on tuples outside \(\operatorname{im}R\).

## 8. What each finite place reads

- **The ramified place classifies and signs.** On the whole family
  \(\mathcal U\) the \(\mathfrak p_5\) readout is
  \((-1)^r3^n\in\mathbb F_5^\times\), a full four-cycle; the step survives
  exactly when that readout is a sign, and on survivors the readout is the
  spinor sign \((-1)^{r+m}\). The ramified place sees precisely what the
  lattice admits and, on the admitted steps, precisely what the archimedean
  legs cannot see.
- **The inert place above two reads a 15-clock.** In
  \(\mathbb F_{16}^\times\), \(\kappa(q)=\zeta_5^{\,3r}\varphi^{2m}\)
  determines and is determined by \((r\bmod5,\ m\bmod3)\). The source
  lane's survivor reduces to \(1+\zeta_5\) of order 15. The Lorentz factor
  \(\gamma_m\) is an **integer** exactly when \(3\mid m\), that is, exactly
  when the noncompact part of the two-adic readout is trivial.
- **Jointly, a 30-clock.** The two finite places together read exactly the
  cyclic quotient

  \[
  S\big/\langle-\varphi^6\rangle\;\cong\;\mathbb Z/30,
  \]

  and are blind exactly to the subgroup generated by \(-\varphi^6\)
  (rapidity \(12\log\varphi\) with a spinor sign). No reading of the number
  30 beyond this group-theoretic statement is claimed: no Coxeter-number,
  edge-count, or physical-clock interpretation is asserted.

The two-adic readout acts on units only; the source lane's open two-adic
comparison of the vertex lattice \(L\) against the trace-zero order
\(\mathcal O^0\) is untouched here.

## 9. Candidate results

> **Coaxial reading exactness [candidate-T / L1, frozen scope].** On the
> fixed placement, the surviving determinant-one coaxial inverse-pair steps
> form \(S=\{\zeta_{10}^{\,r}\varphi^{\,2m}\}\cong\mu_{10}\times\mathbb Z\).
> The readout triple, consisting of fivefold phase
> \(\tau(q)=q/\bar q=\zeta_5^{\,r}\),
> boost point \(b(q)=(L_{4m}/2,\ \tfrac{\sqrt5}2F_{4m})\) on
> \(\gamma^2-(\gamma\beta)^2=1\), and ramified sign
> \(\varepsilon(q)=(-1)^{r+m}\), is a group homomorphism; the archimedean
> pair alone has kernel exactly the center \(\{\pm1\}\); the triple is
> faithful with the explicit inverse on its image given in section 7.
> Composition reads as count addition. On the nonnegative boost leg this is
> the registered index-addition law restricted to
> \(4\mathbb Z_{\geq0}\); negative counts form the candidate inverse
> extension derived here.
>
> **Finite-key census [candidate-T / L1, frozen scope].** On \(S\) the
> \(\mathfrak p_5\) readout collapses to the sign \((-1)^{r+m}\), and
> survival within the inverse pairs is exactly "the \(\mathfrak p_5\)
> readout is a sign". The two-adic readout is the pair
> \((r\bmod5,\ m\bmod3)\) in \(\mathbb F_{16}^\times\); jointly the two
> finite places read exactly \(S/\langle-\varphi^6\rangle\cong\mathbb Z/30\);
> and \(\gamma_m\in\mathbb Z\) exactly when \(3\mid m\).
>
> **Reading dictionary [candidate-D, frozen readout].** The count \(m\) read
> as the coaxial substrate rapidity count \(4m\log\varphi\), \(\tau\) as the
> fivefold tick phase, \(\varepsilon\) as the spinor sign, and
> \(\beta_m=\sqrt5F_{4m}/L_{4m}\) as the decoder velocity, resting on
> `BOOST-READING-SPLIT [T]`, `BOOST-COUNT-LADDER [D]`, and the source-lane
> lattice lemma. First admitted noncompact reading:
> \(\gamma=\tfrac72\), \(|\beta|=\tfrac{3\sqrt5}7\).

The dictionary sentence is a frozen candidate reading, not a registered
row; registering any of it would be a later, separate Canon move under the
release procedure.

## 10. What this hands the decoder program, and what it does not

Hands over: one total, fully typed candidate readout, at incubation level, of
the shape the reading-family discipline demands: a frozen domain, codomain,
context keys, equality, and overlap rule; readout legs that are provably exact
and provably lossless with an explicit inverse on the image; and a census of
what each place of \(K\) contributes to the readout. A future formal lane can
audit a candidate reading against this shape.

Does not hand over: any content for `D_matter`, `D_geom`, or `D_clock`; any
totality, occurrence, or completeness statement; any apparatus, event, or
stream; any measure or probability; any uniqueness beyond the frozen scope;
any statement about \(U\); any placement-independent statement; any new
positive-orientation velocity value. It also does not classify alternative
readings or establish their compatibility under `POLICY.md` section 4.

## 11. Open obligations

- Classify the admissible `2I` placements before any placement-independent
  reading family (inherited from the source lane).
- Construct and compare the complete four-dimensional lattices with spatial
  sections \(L\) and \(\mathcal O^0\) at the two-adic place (inherited; the
  two-adic key here reads units, not that lattice pair).
- Decide whether the canonical update \(U\) belongs to the frozen class;
  until then the transfer prohibition is absolute.
- Classify candidate readings on this domain and establish explicit
  compatibility rules for any alternatives under `POLICY.md` section 4.
- Any promotion of the readout requires a fresh formal `probes/P-NAME/` lane
  under `POLICY.md`, with its own preregistration and accepted verifier;
  the present files authorize no such move.
- Whether \(\mathcal U=\mathcal O_K^\times\) is classical and unused here;
  a formal lane that needs it must import it explicitly.

## 12. Local audit program

The companion file is [`verify.py`](verify.py). It uses only the Python
standard library and exact arithmetic in \(\mathbb Q(\zeta_5)\). Its finite
sweeps are deterministic, with no randomness. The checks form a finite exact
regression audit of the placement data, sampled survival cases, reading legs,
Lucas ladder, composition law, kernel, faithfulness, decode map, and
finite-place census. They do not independently prove the universal survival
criterion imported from PR #681 at commit
`8b6f10ec5ac2f6a67c07cac1b1dbc47f941d3497`. A failure exits with status 1.

This local verifier is not a formal evidence directory, preregistration,
two-architecture computation gate, or probe. Any future public promotion
must start under a new formal `probes/P-NAME/` lane and follow `POLICY.md`;
the present files authorize no such move.
