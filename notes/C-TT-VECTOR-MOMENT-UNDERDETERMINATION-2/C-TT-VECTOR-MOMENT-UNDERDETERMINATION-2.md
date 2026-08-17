# C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2. The family, the value table, the diagonal collapse, and the degree-5 signature

```text
STATUS:          NON-CANONICAL INCUBATION CANDIDATE
PUBLIC CLAIMS:   none
CANDIDATE ID:    C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2
DATE:            2026-08-17
BASE COMMIT:     4020c5373453ef4b8466a8738337be187fc238b6
CANON AT BASE:   Public Canon v50, ACTIVE
LINEAGE:         sibling of C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1, branch
                 commit 05cf23f4118c86e60b876c7665d07016c14db549
PARENT ROW:      TT-VECTOR-STATE-NORMALIZATION [O], unchanged, still O / STOP
TARGET ROW:      TT-VECTOR-MOMENT-UNDERDETERMINATION, one row, proposed T
GATES.tsv:       untouched. No gate created and none needed.
```

This directory carries a frozen incubation candidate. It has no authority, it
promotes nothing, and it edits no file under `canon/`. Candidate -1 in the
sibling directory stays byte-exact and is not modified.

## The result in one paragraph

The underdetermination of the squaring readout is not a pair but a `Z/5`
family. The six laws `A` and `B_0` to `B_4` on the carrier `Z/5` at unit
scale agree on every polynomial functional through degree three, all have
deterministic pointwise modulus and translation invariance, and their
squared-readout spectra range over the flat spectrum and all five single-mode
peaks. For every one of the fifteen pairs the degree-four separators are
exactly the same twenty monomials `v_x^2 conj(v_y)^2`, whose values
`z^{2m(x-y)}` read the family index. At degree five the only separators from
`A` are the ten fifth powers, the first place the `p = 5` structure shows in
the moment hierarchy. The site four-fold action and the pointwise coefficient
automorphism move the index by inverse multiplications, so their diagonal
fixes every law: arbitrary peak placement is compatible with full diagonal
four-fold invariance, with the explicit map `m = 3 k_0 mod 5`. The claim
withdrawn as error E1 earlier in this lane is true under the diagonal action;
the error was the identity of the acting group. Two architectures,
byte-identical stdout, verifier 40 of 40, independent closed-form breaker 11
of 11, zero breaks. The parent is not closed in either direction.

## Contents

```text
PREREG.md        the six preregistration fields, frozen and hashed before the
                 verifier was executed for the first time
verify.py        exact verifier, Q(zeta_5), standard library only, 40 gates,
                 no float in any assertion
breaker.py       independent breaker on a disjoint code path: closed-form
                 character sums, 11 gates, zero breaks
EXPECTED.txt     frozen stdout of verify.py
BREAK.txt        frozen stdout of breaker.py
RESULT.md        the written proofs of P1 to P7 and the result record
RUN_TWO_ARCH.md  the two-architecture run evidence
PROMO.md         the promotion proposal, superseding the -1 proposal where
                 they differ, resolving decisions D2, D3, D4
SHA256SUMS       pins for every file above
```

## Decisions this candidate resolves

```text
D2  pair versus family: FAMILY, now properly frozen here. The procedural bar
    of -1, post-freeze content may not be imported, is discharged by a fresh
    preregistration. Recommendation: the public probe carries the family.
D3  diagonal site-and-Galois variant: NO separate row. Computed collapse:
    the diagonal fixes every law; it enters the single row as one clause.
D4  canon section: 14, by registry precedent. Section 18 carries only O and
    H rows, 14 O plus 2 H, zero theorems; every T row lives in a content
    section. Cross-tab in PROMO.md, reproducible from REGISTRY.tsv.
```

Remaining with the owner: the one-word choice between the family statement
and the narrower -1 pair statement for the public PREREG, and the
strike-through of the superseded comment in the lane issue.

## What must happen before anything moves

1. Owner word on the family form.
2. Public claim issue for `P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1`.
3. Probe pinned under `probes/` on its own branch with the chosen statement
   preregistered explicitly; nothing imported from these notes by reference.
4. GitHub x86_64 required check at pull-request time. The two local
   architecture legs already exist for both candidates.
5. Only then a sealed integer-versioned fold, `v50` to `v51`, if the review
   agrees with the scope in `PROMO.md`.

No step above is done by the presence of this directory.
