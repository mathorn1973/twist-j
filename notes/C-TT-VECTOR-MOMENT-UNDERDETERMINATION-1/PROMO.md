# PROMO-C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1

Promotion proposal from the incubation lane. Consumable on its own. It
proposes; it does not promote. Public validation runs on
`mathorn1973/twist-j` under `POLICY.md` and `AGENTS.md`, which govern.

## 1. Identity

```text
candidate id      C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
public probe      P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
registry claim    TT-VECTOR-MOMENT-UNDERDETERMINATION
parent            TT-VECTOR-STATE-NORMALIZATION [O], unchanged, stays O
base commit       4020c5373453ef4b8466a8738337be187fc238b6
canon at base     Public Canon v50, ACTIVE
```

## 2. Proposed status and scope

Proposed status `T`. One claim, not three.

Scope, tight and stated as a boundary, not as a hedge: an existence and
minimality statement about two explicitly constructed finite laws on the
carrier `Z/5` at scale `a = 1`, plus a closure obstruction for any law with
deterministic pointwise modulus. It is a statement about which state data the
squaring readout does and does not determine. It is not a normalization, not a
state selection, not an action, not a Stage-B pullback, not a scalar spectrum,
not an `r_T(k)`, not a helicity or detector statement, and not a cosmological
observable. It makes no claim about `J`, the Plenum, forces, spacetime, Born,
measure, the observer, SI units, or layers L2 to L6.

## 3. Exact statement proposed for the Canon

Let `X = Z/5`, `z = zeta_5`, `a = 1`, and let a state be a random field
`v` on `X` with values in `Q(zeta_5)`. Write
`C_{xy} = E[v_x conj(v_y)]`, `P_{xy} = E[v_x v_y]`, `w_x = v_x^2`,
`S_w(k) = sum_r E[w_r conj(w_0)] z^{-k r}`, and let `rho` act on sites by
`(rho_u v)_x = v_{u^{-1} x}` for `u` in `(Z/5)^*`, with no accompanying action
on coefficients. Then the two laws

```text
A    v_x = z^{t_x},           (t_x) iid uniform on Z/5
B    v_x = z^{t_0} eps_x,     t_0 uniform on Z/5, independent of
                              (eps_x) iid uniform on {+1,-1}
```

are both invariant under site translation and under `rho`, both satisfy
`|v_x| = 1 pointwise almost surely, and both satisfy `E[v_x] = 0`,
`C_{xy} = delta_{xy}`, `P_{xy} = 0`; every monomial in `(v, conj(v))` of total
degree at most 3 has the same expectation under both, so every polynomial
functional of degree at most 3, in particular every quadratic, cannot
distinguish them; while the squaring readout gives `S_w(k) = 1` for all `k`
under `A` and `S_w(k) = 5 delta_{k,0}` under `B`. The minimal total degree at
which the two separate is exactly 4, and the separating monomials at degree 4
are exactly the 20 monomials `v_x^2 conj(v_y)^2` with `x != y`, each with
expectation 0 under `A` and 1 under `B`. Furthermore, any state with
`E[v_x] = 0`, `P_{xx} = 0` and `|v_x|^2 = a^2` almost surely at `a > 0` has
`E[|v_x|^4] = a^4` while the Isserlis closure requires `2 a^4`, so its fourth
cumulant is `K_{xx} = -a^4` and no such state is Gaussian. Exact arithmetic in
`Q(zeta_5)` throughout, at complete finite scope, with no float in any
assertion.

Consequence, stated inside the scope: the two-point and pseudo-covariance data
of the vector doublet do not determine the power spectrum of its squared
readout, and a Gaussian or Wick boundary is unavailable while the pointwise
modulus is held fixed.

## 4. Falsifier for the registry row

fires if any monomial in the field and its conjugate of total degree at most 3
has different expectations under the two displayed laws, if any displayed
moment, spectrum or cumulant differs from its stated exact value, if either
law fails invariance under site translation or under the displayed four-fold
site action, if the set of degree-4 separating monomials is not exactly the 20
monomials of the displayed shape, or if a state with deterministic pointwise
modulus and vanishing pseudo-covariance satisfies the Isserlis fourth moment
at positive scale; a pinned-bundle, transcript or architecture mismatch
without an exact mathematical negation is integrity STOP, not a scientific
falsifier

## 5. Verifier and pins

```text
PREREG.md    sha256 091ef70b0b0f65247afab229c1d4a8a9ade7ccdaa9a0009de6f26a052a7d519d  11477 B
verify.py    sha256 68238c8609a6e651a11f760d493045e015839bd3810ed05466823e21c2a3fc7c  13398 B
breaker.py   sha256 6fc905cec73a5bc3607b384723ea0d25eaf6c91a17828b64b64075c891bcff43   9112 B
EXPECTED.txt sha256 d547022e0aad57f2fa7ab36fa1a2c575f345c8169572130a7d6bb1e0a0acefe6   4313 B
BREAK.txt    sha256 0ac5a53d4046a123d666410004e6bc9545c942ec38e98ed88c950d866301064d   1064 B
```

Verifier: Python standard library only, exact `Fraction` coefficients on the
basis `{1, z, z^2, z^3}`, integer exponent arithmetic in `Z/5`, 63 gates,
5 seconds, exit 0, empty stderr, three consecutive byte-identical runs.
Breaker: closed-form character sums, no configuration enumerated, 13 gates,
zero breaks, including a full independent sweep of all 1001 monomials of total
degree at most 4 and a cross-binding of both closed forms to enumeration.

One leg only, x86_64. The public probe must still produce the local aarch64
leg and the GitHub x86_64 check with byte-identical stdout before any fold.
The proposed status `T` rests on the written proofs in
`C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1_RESULT_2026-08-17.md`, which the
verifier audits at complete finite scope; it does not rest on the run alone.

## 6. Dependency edges

```text
depends on   TT-SQUARING-DECODER [D]   for the squaring readout h = v^2 and
                                       its kernel {+1,-1}
depends on   POL-READ [D]              only for the readout convention; no
                                       propagation, source or observable used
constrains   TT-VECTOR-STATE-NORMALIZATION [O]  narrows admissible closures;
                                       does not close it in either direction
does not     TT-QUADRATIC-INDUCED, TT-QUADRATIC-GERM, TT-SOURCE,
touch        COSMOLOGY-READING-DICTIONARY, SCHWARZSCHILD-TT-ENDPOINT
```

## 7. Exact edits the fold would make

`canon/REGISTRY.tsv`, one new row, schema
`claim_id status scope canon_section evidence falsifier`, evidence a path:

```text
TT-VECTOR-MOMENT-UNDERDETERMINATION	T	<statement from section 3, single field>	14. The gravitational wave program	probes/P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1	<falsifier from section 4>
```

`canon/FRONTIER.md`, under `## Tensor and radiation (TENSOR)`, the existing
`TT-VECTOR-STATE-NORMALIZATION [O]` bullet keeps its status, its queue line
and its decision line unchanged. One line is appended to that bullet:

```text
  Constraint: the registered TT-VECTOR-MOMENT-UNDERDETERMINATION shows that
  mean, two point covariance, pseudo covariance and every polynomial
  functional through degree three leave the squared-readout spectrum free, and
  that a Gaussian closure is unavailable at deterministic pointwise modulus;
  an admissible normalization must therefore freeze fourth moment data, the
  complete state, or an explicit non-Gaussian closure rule.
```

`canon/CANON.md`, section `14. The gravitational wave program`, one paragraph
carrying the statement of section 3 verbatim in prose, placed after the
`TT-SQUARING-DECODER` paragraph. The prose must avoid the machine-rejected
phrase list in `tools/check_canon.py`, in particular the words checked by
`PRIVATE_AUTHORITY_WORD`; the statement in section 3 already avoids them.

`canon/NORMATIVE.tsv`, one new row:

```text
TT-VECTOR-MOMENT-UNDERDETERMINATION	THEOREM	TT-VECTOR-MOMENT-UNDERDETERMINATION	T	L1		canon/CANON.md::14. The gravitational wave program
```

`canon/GATES.tsv`: no change. No gate is created and none is needed. The map
`v -> w = v^2` is an `L1` algebraic map of states inside this claim and
`S_w` is the power spectrum of the squared readout, not a tensor spectrum and
not `r_T(k)`. The moment `w` is identified with a physical tensor field, that
is a layer lift, it needs its own named and typed gate, and this proposal does
not supply one. The public ledger currently types `TT-SQUARING-DECODER`,
`POL-READ` and the parent as `NOT_APPLICABLE`, so the endpoint layers are not
fixed yet; fixing them is the parent's work.

`canon/CHANGELOG.md`, `canon/SHA256SUMS`, `canon/STATUS_COUNTS.tsv`,
`canon/DEPENDENCIES.tsv`, `canon/EVIDENCE.tsv`, `STATUS.md`: the ordinary
integer-versioned fold updates, `v50` to `v51`, with new hashes. No decimal
version. No `T-LOCK`.

## 8. What the fold must refuse

Refuse if the aggregate is read as closing the parent. Refuse if the row is
summarised anywhere as a normalization, a state selection, or a step toward
`r_T(k)`; no summary may exceed the status or scope of its source. Refuse if
the six-member amplification recorded in the result document is imported into
the frozen statement: it is proved but it was found after the freeze, and it
belongs in the public `PREREG.md` explicitly or nowhere. Refuse on a single
architecture.

## 9. Owner decisions this proposal does not take

```text
D1  whether the child probe carries only the pair (A, B) or the full
    six-member family. The wider form is proved and strictly stronger; the
    narrow form is what was frozen. One or the other, preregistered.
D2  whether the diagonal site-and-Galois variant of the four-fold action is
    worth a separate row. The trichotomy changes under it; that variant was
    excluded by systematic S2 of the preregistration and is untouched.
D3  whether the claim sits in section 14 or in section 18. It is a theorem,
    not a frontier item, which argues for 14; it exists only to constrain a
    section 18 obligation, which argues for a cross-reference either way.
```
