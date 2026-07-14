# P-ENTROPY-BRIDGE-3 result

Status: FORMAL AARCH64 RECORD; PUBLIC X86_64 GATE PENDING

## Scientific decision (aarch64 leg)

```text
RESULT 10/10 ALL PASS, exit 0, stderr empty.
```

All ten preregistered gates passed on the first execution of the pinned
verifier (pin commit ab175284e57ec99e5e52b04a8f2a7bb2d0c326aa, public lock
issue 29, base c53a5c42a30c9773817f8c2d4d41f07069cf713f).

Recorded outcomes at the preregistered scope:

```text
G02 + G03          THE LIVING-SET STRUCTURE (C at the census scope): the
                   images of the two branch maps PARTITION the recurrent
                   core into two halves of 3125, and every branch map
                   restricted to either half is a bijection onto its own
                   image half (all four restrictions). All irreversibility
                   of a block sits in its first tick; past the first tick
                   the driven dynamics on the living set is invertible.
G04                the component split: every 20-attractor splits (10, 10)
                   across the halves, the 10-singlet splits (5, 5); living
                   trajectories 312 x 10 + 5 = 3125 = 5^5.
G05 + G06          THE UNIQUE-PAST LAW (C at the tested range): every
                   word-prefix composition of depth d = 1..12 at the
                   frozen anchors has image exactly 3125 and EVERY fiber
                   exactly 2; the backward tree is a caterpillar of width
                   exactly 2 with one death per level. Backward
                   indeterminacy does not accumulate: one ghost
                   alternative per step, killed one step deeper; the
                   infinite past over the word is unique.
G07                the tower carrier: the boundary process at multiples of
                   2^k on the seed-0 attractor occupies exactly 10 states,
                   5 in each half, for k in {1, 2, 4, 8}.
G08 + G09          the arithmetic side: ord(J mod lambda^i) =
                   (4, 20, 20, 20, 20, 20, 100, 100) for i = 1..8; orbit
                   spectrum of J on O/lambda^5 is {1: 1, 4: 1, 20: 156}.
G10                THE COUNTING IDENTITY: 3125 = 5^5 = |O/lambda^5|. The
                   living-trajectory count equals the lambda-tower
                   capacity at depth 5; the cut in selection form is a
                   selection of one living trajectory per (kappa, y), and
                   y mod lambda^5 has exactly the right cardinality.
G01                framework pin: recurrent core 6250 on 313 attractors.
```

No falsifier fired. The successor obligation (regularity, canonicity, and
the measure clause of the selection family) is out of scope of this probe
and remains open in ENTROPY-LAYER-BRIDGE [O].

## Two-architecture status

The aarch64 leg is recorded in RUN.md (stdout sha256 a4600f24...,
1612 bytes, EXPECTED.txt byte-identical). The public x86_64 gate runs in
the pull request check; this file is promoted after byte identity is
confirmed.
