# PROMO-C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2

Promotion proposal from the incubation lane, superseding the statement and
edit sections of `PROMO-C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1` where the
two differ, and resolving the three decisions that proposal left open.
Consumable on its own: a fold needs this document and nothing else. It
proposes; it does not promote. Public validation runs on
`mathorn1973/twist-j` under `POLICY.md` and `AGENTS.md`, which govern.

## 1. Identity

```text
candidate ids     C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 (pair, Wick no-go)
                  C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 (family, actions)
public probe      P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
registry claim    TT-VECTOR-MOMENT-UNDERDETERMINATION, one row per the owner
                  ruling of 2026-08-17
parent            TT-VECTOR-STATE-NORMALIZATION [O], unchanged, stays O
base commit       4020c5373453ef4b8466a8738337be187fc238b6
canon at base     Public Canon v50, ACTIVE
```

## 2. The three decisions, resolved

The -1 proposal listed three owner decisions in its section 9, numbered D1 to
D3 there. In the lane numbering after the one-row ruling they are D2, D3 and
D4. Resolutions:

### D2, pair versus family: family, now properly frozen

The objection to the family form was procedural, not mathematical: it was
proved after the -1 freeze and a frozen candidate may not import post-freeze
content. That objection is now discharged. Candidate -2 preregistered the
family statements P1 to P7 with their falsifiers before execution, verified
them on two architectures with byte-identical stdout, and survived an
independent closed-form breaker. Recommendation: the public probe carries the
family form. It is strictly stronger, it costs nothing extra in scope, and
the pair form of -1 is literally two of its six members. Candidate -1 remains
the audit trail for the pair and for the discovery order.

### D3, the diagonal site-and-Galois variant: no separate row

Resolved by computation. The variant is not a variant of the trichotomy; it
is a collapse. Writing `gamma_u` for the pointwise coefficient automorphism
`sigma_u(z) = z^u` and `rho_u` for the site action, the two move the family
index by inverse multiplications, `rho_u B_m = B_{u^{-1} m}` and
`gamma_u B_m = B_{u m}`, so their diagonal `D_u = gamma_u rho_u = rho_u
gamma_u` fixes every one of the seven laws, 28 of 28 measure checks, and
every moment of degree up to 6 on the independent closed-form path. One
consequence deserves the ink: the claim withdrawn as error E1 in this lane,
that arbitrary peak placement can coexist with four-fold invariance, is true
under the diagonal action, with the explicit peak map `m = 3 k_0 mod 5`. The
error was the identity of the acting group, not the phenomenon. All of this
is one clause of the single row, not a second row: same carrier, same family,
same readout, and a second row would invite a summary stronger than its
source.

### D4, canon section: 14, by registry precedent

Resolved by data, not taste. Cross-tab of `canon/REGISTRY.tsv` at the base
commit, 249 claim rows, status by canon_section, reproducible as

```text
awk -F'\t' 'NR>1{c[$4" | "$2]++} END{for(k in c) print c[k], k}' canon/REGISTRY.tsv
```

Section `18. The frontier` carries exactly 14 O rows and 2 H rows, zero T,
zero D, zero C, zero F. Every T row in the ledger lives in a content section;
section `14. The gravitational wave program` already carries 1 T and 3 D. A
theorem constraining a frontier obligation therefore sits in 14, and the
frontier keeps a one-line cross-reference under the parent bullet. That is
the existing house pattern and this proposal follows it.

## 3. Proposed status and scope

Proposed status `T`. One claim. Scope, tight: an existence, minimality and
symmetry statement about six explicitly constructed finite laws on the
carrier `Z/5` at scale `a = 1`, plus a closure obstruction for any law with
deterministic pointwise modulus. It is a statement about which state data the
squaring readout does and does not determine. It is not a normalization, not
a state selection, not an action functional, not a Stage-B pullback, not a
scalar spectrum, not an `r_T(k)`, not a helicity or detector statement, and
not a cosmological observable. It makes no claim about `J`, the Plenum,
forces, spacetime, Born, measure, the observer, SI units, or layers L2 to
L6, and no claim that the six laws exhaust their degree-3 equivalence class.

## 4. Exact statement proposed for the Canon

Let `X = Z/5`, `z = zeta_5`, and let a state be a random field `v` on `X`
with values in `Q(zeta_5)`. Write `w_x = v_x^2` and
`S_w(k) = sum_r E[w_r conj(w_0)] z^{-k r}`. Let `rho_u` act on sites by
`(rho_u v)_x = v_{u^{-1} x}` and let `gamma_u` apply the coefficient
automorphism `sigma_u(z) = z^u` pointwise, `u` in `(Z/5)^*`. Then the six
laws

```text
A     v_x = z^{t_x},              (t_x) iid uniform on Z/5
B_m   v_x = z^{t_0 + m x} eps_x,  m in Z/5, t_0 uniform, independent of
                                  (eps_x) iid uniform on {+1, -1}
```

are invariant under site translation, have deterministic pointwise modulus
one, and agree on the mean, on `C = delta`, on `P = 0`, and on every
polynomial functional of total degree at most three; the squared readout has
`S_w = 1` under `A` and `S_w(k) = 5 delta_{k, 2m mod 5}` under `B_m`, and the
uniform mixture over nonzero `m` has `S_w(k) = (5/4)(1 - delta_{k,0})`; the
minimal separating degree is exactly four, and for every pair of the six the
degree-four separators are exactly the twenty monomials
`v_x^2 conj(v_y)^2` with `x != y`, whose values `0` under `A` and
`z^{2 m (x - y)}` under `B_m` read the family index; at degree five the only
separators from `A` are the ten fifth powers `v_x^5` and `conj(v_x)^5`, with
values `1` and `0`, and no two of the `B` laws separate at any odd degree;
the site action sends the index `m` to `u^{-1} m`, the coefficient action
sends it to `u m`, and their diagonal fixes every law, so for every mode
`k_0` the member `B_{3 k_0 mod 5}` is diagonally invariant with peak exactly
at `k_0`; and any state with zero mean, zero pseudo-covariance and
deterministic pointwise modulus `a > 0` has `E[|v_x|^4] = a^4` against the
Isserlis value `2 a^4`, hence fourth cumulant `K_{xx} = -a^4`, so no Gaussian
or Wick closure exists at fixed modulus. Exact arithmetic in `Q(zeta_5)`
throughout, at complete finite scope, with no float in any assertion.

Consequence, stated inside the scope: second-order and degree-three data
leave the squared-readout spectrum free across a full `Z/5` index and its
mixtures, the freedom survives the diagonal four-fold symmetry, and a
Gaussian boundary is unavailable while the pointwise modulus is held fixed.

## 5. Falsifier for the registry row

fires if any monomial of total degree at most three has different
expectations under any two of the six displayed laws, if any displayed
moment, spectrum, separator set, separator value, action-table entry or
cumulant differs from its stated exact value, if any of the six laws fails
invariance under site translation, if the diagonal action fails to fix any of
them, if the degree-four separator set of any pair is not exactly the twenty
displayed monomials, if the degree-five inventory is not exactly the ten
displayed fifth powers with the displayed values, or if a state with
deterministic pointwise modulus and vanishing pseudo-covariance satisfies the
Isserlis fourth moment at positive scale; a pinned-bundle, transcript or
architecture mismatch without an exact mathematical negation is integrity
STOP, not a scientific falsifier

## 6. Verifier and pins

Candidate -2, this directory:

```text
PREREG.md    sha256 4e2d4b8291d16bd288fa25eccf8d7f04eb8b0ab3df576766c9ca43fd76f4e8f6  11978 B
verify.py    sha256 a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67  13802 B
breaker.py   sha256 1ea4b98e174c5271f17310f76c60dad1051faa512fe2393a58d5297cfb899738   9809 B
EXPECTED.txt sha256 711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c   3013 B
BREAK.txt    sha256 cf6902200fa6bf9a8896dc95099fb5aa3900ce2f1c1eb6ca75d6e8b210e9a642    986 B
```

Candidate -1, sibling directory, byte-exact and untouched:

```text
PREREG.md    sha256 091ef70b0b0f65247afab229c1d4a8a9ade7ccdaa9a0009de6f26a052a7d519d  11477 B
verify.py    sha256 68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c  13398 B
EXPECTED.txt sha256 d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6   4313 B
```

The -2 verifier: 40 gates, complete enumeration through degree five over the
six laws, complete pushforward measure checks for four group actions, 18
seconds on the slower leg. The -2 breaker: 11 gates on the independent
closed-form character path, including the diagonal moment identity at every
degree up to six and the two orbit identities. Two architectures,
byte-identical stdout, recorded in `RUN_TWO_ARCH.md`; the same holds for -1.
The GitHub x86_64 required check remains for the public probe.

## 7. Dependency edges

```text
depends on   TT-SQUARING-DECODER [D]   for the squaring readout and its kernel
depends on   POL-READ [D]              readout convention only
constrains   TT-VECTOR-STATE-NORMALIZATION [O]  narrows admissible closures;
                                       does not close it in either direction
does not     TT-QUADRATIC-INDUCED, TT-QUADRATIC-GERM, TT-SOURCE,
touch        COSMOLOGY-READING-DICTIONARY, SCHWARZSCHILD-TT-ENDPOINT
```

## 8. Exact edits the fold would make

`canon/REGISTRY.tsv`, one new row, schema
`claim_id status scope canon_section evidence falsifier`, the scope being the
section 4 statement as a single field and the falsifier the section 5 text:

```text
TT-VECTOR-MOMENT-UNDERDETERMINATION	T	<section 4 statement>	14. The gravitational wave program	probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1	<section 5 falsifier>
```

`canon/FRONTIER.md`, under the parent bullet, status, queue and decision
lines unchanged, one appended line:

```text
  Constraint: the registered TT-VECTOR-MOMENT-UNDERDETERMINATION shows that
  mean, two point covariance, pseudo covariance and every polynomial
  functional through degree three leave the squared-readout spectrum free
  across a full Z/5 family that the diagonal four-fold action fixes, and that
  a Gaussian closure is unavailable at deterministic pointwise modulus; an
  admissible normalization must therefore freeze fourth moment data, the
  complete state, or an explicit non-Gaussian closure rule.
```

`canon/CANON.md`, section `14. The gravitational wave program`, one paragraph
carrying the section 4 statement in prose, after the `TT-SQUARING-DECODER`
paragraph, avoiding the machine-rejected phrase list of
`tools/check_canon.py`; the statement above already avoids it.

`canon/NORMATIVE.tsv`, one new row:

```text
TT-VECTOR-MOMENT-UNDERDETERMINATION	THEOREM	TT-VECTOR-MOMENT-UNDERDETERMINATION	T	L1		canon/CANON.md::14. The gravitational wave program
```

`canon/GATES.tsv`: no change. No gate is created and none is needed; the maps
`v -> v^2` and `gamma_u` are `L1` algebraic operations on states inside this
claim, and the moment `w` is identified with a physical tensor field is the
moment a named and typed gate is required, which this proposal does not
supply.

`canon/CHANGELOG.md`, `canon/SHA256SUMS`, `canon/STATUS_COUNTS.tsv`,
`canon/DEPENDENCIES.tsv`, `canon/EVIDENCE.tsv`, `STATUS.md`: the ordinary
integer-versioned fold updates, `v50` to `v51`, with new hashes. No decimal
version. No `T-LOCK`.

## 9. What the fold must refuse

Refuse if the aggregate is read as closing the parent. Refuse if the row is
summarised anywhere as a normalization, a state selection, or a step toward
`r_T(k)`. Refuse a second row for the diagonal clause. Refuse a fold on one
architecture, and refuse a public probe whose PREREG does not carry the
family form explicitly; nothing may be imported from these notes by
reference alone.

## 10. What remains with the owner

One word: whether the public probe preregisters the family statement of
section 4 as recommended, or the narrower -1 pair statement. Everything else
in this lane is either computed or ruled. The earlier comment in the lane
issue still awaits the owner's strike-through, which is the owner's hand and
not this proposal's.
