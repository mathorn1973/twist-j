# PROMO-C-AFFINE-READING-CHARACTER-CENSUS-1

Hand-off artifact. A public fold can consume this document without reading
anything else. It proposes nothing by itself and promotes nothing by existing.

```text
candidate id     C-AFFINE-READING-CHARACTER-CENSUS-1
target line      PUBLIC, mathorn1973/twist-j main
basis            Public Canon v60, tag canon-v60,
                 content commit 18b21bdaf2c2236c9444b120900277ccfb63e050,
                 head at freeze f9b7438747e612eeebf63cb3ac95283fcb2a7085
candidate label  candidate-T at L1
proposed status  T
proposed scope   L1 only
```

## 1. Exact statement proposed for the registry

```text
claim_id   AFFINE-READING-CHARACTER-CENSUS
status     T
scope      at L1 for the public carrier V = Q^5/<1> with M_J multiplication by
           J = 1 + zeta_5^2, D_J = M_J - I, and G = AGL_1(F_5) of order 20:
           G has exactly four linear characters and the linear degree is empty
           in every one of them, so no nonzero linear reading of the carrier
           exists, invariant or phase weighted; the quadratic degree carries
           exactly two lines, the invariant q_+ and the epsilon graded q_-,
           and nothing in the two order four sectors; Sym^3 V is exactly the
           regular representation of G with multiplicities (1,1,1,1,4) and
           dimension 20; the smallest odd invariant degree is 3 and the unique
           cubic invariant K satisfies the exact identity
           3K = p_1^3 + 6 p_1 q_+ - 25 p_3, so the sign of the state is
           readable at degree three and the invariant ring is not concentrated
           in even degrees; no element of G acts as -I, chi_V takes values in
           {-1,0,4}, and the invariant fingerprint of degree at most five
           separates G orbits on the exhaustive test set {-2..2}^4 minus zero,
           so the carrier state is recoverable up to the 20 element orbit;
           exact affine representation theory only, with no measurement,
           apparatus, instrument, observer, decoder, Born rule, probability,
           record, photon, light, matter, energy density, cosmology,
           expansion, contraction, hidden fraction, SI value, or L2 to L6 lift
canon_section  the section that already hosts AFFINE-READING-DEGREE-CENSUS
evidence       probes/P-AFFINE-READING-CHARACTER-CENSUS-1/
falsifier      not applicable at status T
```

## 2. Falsifier of the underlying route, one line

Exhibit a nonzero linear form `f` on `V` and a linear character `lambda` of `G`
with `f(rho(g) x) = lambda(g) f(x)` for all `g` and all `x`. One such `f` kills
the route.

Secondary falsifier: any disagreement between the projector rank route and the
Molien route at any of the 24 gated cells, or a failure of
`sum_lambda m_lambda(d) + 4 m_V(d) = C(d+3,3)`.

## 3. Dependency edges

```text
requires   AFFINE-READING-DEGREE-CENSUS      (T)  V absolutely irreducible,
                                                  dim End_(Q[G])(V) = 1,
                                                  (V*)^G = 0, dim(Sym^2 V*)^G = 1
requires   AFFINE-QUADRATIC-FORM-UNIQUENESS  (T)  the q_+ line and its Gram
relates to P-J-ODD-MOTOR-MEDIATED-BRIDGE-2   (merged probe, no canon row)
                                                  Sym^2 V = 1 + epsilon + 2V
                                                  and the q_- sign form
```

The new row **extends and must not restate** the two required rows. Degree one
in the invariant sector and the `q_+` line are already public. What is new is
the other three character sectors at degree one, the full graded census through
degree five with the Molien series through degree twelve, the regular
representation identity at degree three, the cubic invariant with its closed
form, and the orbit separation counterweight.

## 4. Artifacts and pins

```text
PREREG-C-AFFINE-READING-CHARACTER-CENSUS-1.md
  sha256  473f64da93c9b6c488ffe266bb33c1b9c54705c8debc85166757b80aa192ba40
  bytes   11599      lines 264      final LF yes

verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py
  sha256  829f91d1269f4802c2dfb0e0afba1b9bd78e0830bb665547719f5371bc2ff430
  bytes   13274

EXPECTED.txt              exact stdout of the single formal candidate run
RESULT-...md              result record including the fired self-check
BREAK-...py               the independent third code path
```

## 5. Preconditions the public fold must satisfy before pinning

These are not optional. The candidate is honest about its own defect.

1. **Fix the basis extraction.** The candidate verifier uses
   `rref_pivots(tp(A))` where it must use `rref_pivots(A)`. Measured effect:
   at degree three the extracted invariant was the zero polynomial and at
   degree five only one of three was independent. G1 through G8 are untouched
   and the `SEPARATING-AT-5` label stands a fortiori, but no minimality claim
   about the separating degree may be carried from the candidate run. The
   public verifier must extract correctly and must gate the extracted family
   rank against the computed dimension at every degree.
2. **Do not reuse this identifier.** The public probe is a new preregistration
   under a public issue, pinned before first execution, on branch
   `probe/P-AFFINE-READING-CHARACTER-CENSUS-1`.
3. **Two architectures.** Byte identical stdout on x86_64 and aarch64 plus the
   aggregate check. The candidate ran on one architecture only, so nothing here
   is computation grade yet.
4. **Per gate output granularity.** Print one line per gate from its own
   boolean. Do not print several gate names from one aggregate. This is the
   same defect flagged in the audit of `P-J-ODD-MOTOR-MEDIATED-BRIDGE-2` and it
   should not be inherited.
5. **No tautological gates.** Every asserted mathematical step must be
   computed, not encoded as a constant that is true by inspection.
6. **Prose hygiene.** `tools/check_canon.py` rejects the words sealed,
   internal, private, hidden and unpublished anywhere in the hashed canon
   files. Draft the canon prose against the tool, not after it.

## 6. Registry, frontier and canon edits the fold would make

```text
REGISTRY.tsv   add one row, AFFINE-READING-CHARACTER-CENSUS, status T,
               scope as in section 1, evidence the probe directory,
               falsifier field as the schema requires for a T row
FRONTIER.md    add one open obligation:

  - O-LINEAR-READING-APPARATUS-LIFT [O]: the passage from the L1 character
    graded reading census to L4 support and L5 stream. Required before any
    apparatus, record or measurement reading of the census: the support
    carrier, the instrument or write map, the record codomain, the exact
    equality, the normalization, and a complete acyclic dependency graph.
    Falsifier: exhibit one registered L4 or L5 readout whose emitted record is
    a nonzero linear function of the L1 carrier state.
    Decision: STOP until every typed field above is public and frozen; closes
    positively only with a complete typed bridge compatible with
    AFFINE-READING-CHARACTER-CENSUS and AFFINE-READING-DEGREE-CENSUS; closes
    negatively if a registered readout emits a nonzero linear record.

CANON.md       extend the section that hosts AFFINE-READING-DEGREE-CENSUS with
               the graded table, the Molien coefficients, the regular
               representation identity at degree three, the cubic invariant and
               its closed form, and the orbit separation statement. Integer
               versioned sealed fold with new hashes across CANON.md, CORE.md,
               FRONTIER.md, REGISTRY.tsv, CHANGELOG.md and SHA256SUMS.
```

## 7. What this does not license

It does not license any statement about what an apparatus can or cannot record.
It does not license reading the census as a claim about light, matter, energy
density, expansion, contraction, or any hidden fraction of anything. The
physical reading that motivated the candidate was tested and came back split:
the linear void is real and now complete across all character sectors, and the
claim that only even or contractive quantities are readable is false, because
an odd cubic invariant exists at degree three and the invariants separate
orbits. Both halves must travel together or neither should be quoted.
