# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1. Fourth-moment underdetermination of the squaring readout, and a fixed-modulus Wick no-go

```text
STATUS:          NON-CANONICAL INCUBATION CANDIDATE
PUBLIC CLAIMS:   none
CANDIDATE ID:    C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
DATE:            2026-08-17
BASE COMMIT:     4020c5373453ef4b8466a8738337be187fc238b6
CANON AT BASE:   Public Canon v50, ACTIVE
PARENT ROW:      TT-VECTOR-STATE-NORMALIZATION [O], unchanged, still O / STOP
TARGET ROW:      TT-VECTOR-MOMENT-UNDERDETERMINATION, one row, proposed T
TARGET PROBE:    P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1, not yet opened
GATES.tsv:       untouched. No gate created and none needed.
```

This directory carries a frozen incubation candidate. It has no authority, it
promotes nothing, and it edits no file under `canon/`. Public validation runs
under `POLICY.md` and `AGENTS.md`, which govern over anything written here.

## The result in one paragraph

On the carrier `Z/5` at scale `a = 1` there are two explicitly constructed
finite laws on the vector doublet that agree on the mean, on the two-point
covariance, on the pseudo-covariance, and on the expectation of every
polynomial functional of degree at most three, that are both invariant under
site translation and under the four-fold site action, and that both have
deterministic pointwise modulus; yet under the registered squaring readout
their squared-image power spectra are the flat `1` and the single-mode
`5 delta_{k,0}`. The minimal degree at which they separate is exactly four,
and the separating monomials at degree four are exactly the twenty of the form
`v_x^2 conj(v_y)^2` with `x != y`. Separately, any law with vanishing mean,
vanishing pseudo-covariance and deterministic pointwise modulus at positive
scale has fourth cumulant `-a^4`, so it is not Gaussian and a Wick closure is
not an available repair. Consequence for the parent: an admissible
normalization must freeze fourth-moment data, the complete state, or an
explicit non-Gaussian closure rule. The parent is not closed in either
direction.

## Contents

```text
PREREG.md              the six preregistration fields, frozen and hashed
                       before the verifier was executed for the first time
verify.py              exact verifier, Q(zeta_5), standard library only,
                       63 gates, no float in any assertion
breaker.py             independent breaker on a disjoint code path: closed-form
                       character sums, 13 gates, zero breaks
EXPECTED.txt           frozen stdout of verify.py
BREAK.txt              frozen stdout of breaker.py
RESULT.md              the written proofs and the result record
RUN_TWO_ARCH.md        the two-architecture run evidence; supersedes the
                       paragraph headed ONE LEG ONLY inside RESULT.md
PROMO.md               the promotion proposal, consumable on its own
ISSUE-407-COMMENT.md   the corrected incubation comment, to be posted by the
                       author in place of the earlier comment in that thread
SHA256SUMS             pins for every file above
```

Naming note, because names drift between the lines. `PROMO.md` cites the
result document by the long name
`C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1_RESULT_2026-08-17.md`; that document
is `RESULT.md` here. Match by content, not by identifier.

## Owner decisions recorded

```text
D1  one registry row, not three. Owner ruling 2026-08-17. The three frozen
    statements S1, S2 and S3 are parts of a single claim
    TT-VECTOR-MOMENT-UNDERDETERMINATION, not separate rows.
D2  the narrow pair versus the six-member family: still open. The wider form
    is proved in RESULT.md section A1 but was found after the freeze, so it
    must be preregistered explicitly in the public probe or left out.
D3  the diagonal site-and-Galois variant of the four-fold action: still open,
    excluded here by systematic S2 of the preregistration.
D4  section 14 versus section 18 for the row: still open.
```

## What must happen before anything moves

1. Post `ISSUE-407-COMMENT.md` in place of the earlier comment in that thread.
2. Open a public claim issue for `P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1`.
3. Pin the probe under `probes/` on its own branch, disclosing that `verify.py`
   is byte identical to the file frozen here, exactly as the audit chain for an
   earlier candidate did.
4. Produce the GitHub x86_64 required check at pull-request time. The two
   local architecture legs already exist and are recorded in `RUN_TWO_ARCH.md`.
5. Only then a sealed integer-versioned fold, `v50` to `v51`, if the review
   agrees with the scope in `PROMO.md`.

No step above is done by the presence of this directory.
