# RECON: parallel RH branches on twist-j before the merge

```text
Status   NON-CANONICAL recon. No authority, no public change. Pre-merge
         intelligence requested by the owner ("podivej se na dalsi
         paralelni branche ... nez budeme delat merge").
Date     2026-08-13, evening. Repo head at survey: main = 6545c1d0 (v46).
Method   full ls-remote survey (108 branches), ahead/behind counts, content
         read of every branch ahead of main touching the RH complex,
         replatform reruns of their exact scripts on this session's
         x86_64 (independent leg).
```

## 1. Inventory

Of 108 remote branches, every RH-adjacent probe already sits in main with
0 ahead (P-PENTAGON-WEIL-1, P-J-LI-TORAL-HAAR-1, P-R2-LAMBDA-HAAR-1,
P-R2-SCALING-SHIFT-1, P-LAMBDA-COCYCLE-ANGLES-1/2, P-MOBIUS-TM-PRIME2-1,
P-TM-HANKEL-K3-TRANSFER-1, P-ARITH-RAPIDITY-1, P-SPLIT-PRIME-INDEPENDENCE-1,
P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1). Exactly THREE unmerged branches
carry live RH work, all pushed TODAY 2026-08-13 morning (08:20 to 08:58
CEST), all NON-CANONICAL, all on the same Suzuki complex, each from a
different side:

```text
BR-1  notes/c-rh-pythagoras-halfangle-n      1 commit,  issue #354, STOP.
      Predecessor lane. Stopped because the HTML rendering used for the
      source omitted the final two archimedean terms of Suzuki eq. (1.1).
      Note: this FIRES, in-house, exactly the provenance caution S-A of
      claude/RECON-PRIME-CAPACITY-SUZUKI (rendered pages lie); this
      session's own extraction was complete and witness-corroborated.
BR-2  notes/c-rh-pythagoras-halfangle-2-n    14 commits, issue #355.
      The screw-kernel side. Content: exact half-angle Krein factorization
      of each delayed prime leg G_(h_L) = <S,S> - <C,C>; pole screw kernel
      is rank-(1,1) (x0 x0 - y0 y0); Gamma/Hurwitz kernel = positive OU
      increments minus kappa Brownian counterterm; assembled WINDOWED
      source-side Krein-Gram factorization of the full G_g with no zero
      input; Gram-domination lemma (K PSD iff a contraction X+ -> X-
      exists), so RH iff per-window contractions exist; NO-LOCAL-
      CONTRACTION theorem: one leg is exactly indefinite (2x2 det
      -L^2/4), so no prime-by-prime contraction exists and any real T
      must mix channels; sqrt(i) discipline: half-phase is forced, a
      fixed zeta_8 is only the SU(2) central correction of the parity
      transform (det U = i), not a global selector. PROMO packages
      candidate theorems A-D, correctly scoped, no RH movement.
BR-3  notes/c-rh-capacity-contraction-1-n    2 commits, issue #357.
      The Weil-form side (Suzuki 2606.09096 localized Q_W^a). PREREG for
      the capacity route: q_P,a = ||V-||^2 - ||V+||^2 (delayed Krein
      factor), capacity candidate q_A,a = q_inf,a + ||V-||^2, gates G1-G6
      with the anti-circularity fences stated (no Douglas after the fact,
      no per-cutoff fitting, no RH/zero/Weil-positivity input), frozen
      negative conditions F-CAP-1..5. Breaker frozen. G3 (unconditional
      capacity positivity) is the live risk and is honestly UNDECIDED.
```

Replatform reruns this session (independent leg, x86_64, exact scripts):

```text
BR-2 verify.py  sha256 bef59752...  exit 0  (G1, G2, G4, G5 PASS)
BR-2 break.py   sha256 0148a4bd...  exit 0  (leg det/L^2 = -1/4; zeta_8
                                             non-uniqueness; boundary)
BR-3 break.py   sha256 b3d2ffc7...  exit 0  (leg inertia det = -1; Schur
                                             sign law; disjoint cutoff)
```

## 2. Collision matrix against C-SUZUKI-LOCAL-CAPACITY-NOGO-1

No claim collision. The three lanes plus ours attack the same wall at four
different levels, and the statements are disjoint:

```text
leg inertia          BR-3 G1 + BR-2 F1: one delayed block has both signs
                     (2x2 inertia, det -1; det -L^2/4 kernel form)
leg kernel           BR-2 NO-LOCAL-CONTRACTION: no per-leg contraction
                     between half-angle quadratures (exact)
measure/curvature    OURS (+ M-4 attribution): A'' < 0 window, dA not
                     nonnegative, dP dominates dA at q = 2, ramp class
                     EMPTY, BOTH summed screw kernels indefinite at (3,6),
                     norm-1 forced
capacity candidates  BR-3 q_A,a (Weil carrier) and BR-2 X_(+,a) (screw
                     carrier): TWO different explicit capacity forms for
                     the same prize
```

Convergences worth naming so the program does not count one insight three
times: every lane independently proves some form of "local routes are dead,
mixing is forced"; every lane independently states the circularity fence
(a contraction obtained after assuming positivity earns nothing); BR-2's
Gram-domination lemma and this session's diagonal-model lemma (recon 11.2)
are the same lemma family, stated for fixed feature curves and for free
models respectively; together they say: fixed canonical features make the
contraction statement contentful, free models collapse it to RH verbatim.

## 3. One disclosure

This session's freeze-time collision scan checked project docs, main's
notes/, probes/ and REGISTRY.tsv but NOT remote branches; BR-1..BR-3
existed (unmerged) hours before the PREREG froze. Outcome: no content
collision, but by luck, not discipline. Procedural fix proposed for the
next contract or AGENTS touch: a collision scan must include
`git ls-remote --heads` and open issues.

## 4. Merge recommendation

```text
M1  MERGE BR-2 (no squash). Strongest new structural piece: the windowed
    source-side Krein factorization plus the leg no-go. Replatform rerun
    passed here. Suggested at-merge addition, one paragraph in its
    RESULT.md: cross-reference the sibling no-gos (leg inertia BR-3,
    measure-level C-SUZUKI-LOCAL-CAPACITY-NOGO-1) as DISTINCT statements
    of one moral, to prevent double counting.
M2  MERGE BR-3 (no squash). Lane-B prereg with correct fences. At merge,
    add the same cross-reference paragraph, and note that its q_A,a and
    BR-2's X_(+,a) are two inequivalent-looking capacity candidates that
    must enter ONE G0-frozen classification (decoder-note discipline);
    two candidates before G0 is exactly the NONUNIQUE risk the frame
    exists to catch.
M3  BR-1: dead predecessor without an in-branch STOP record. Either merge
    with an added one-line STOP-RECORD file citing #355 R0, or keep the
    branch unmerged as archive. Do not merge as live.
M4  OUR BUNDLE: contrary to the working assumption, C-SUZUKI-LOCAL-
    CAPACITY-NOGO-1 was NOT yet in the repo; it lived in the project
    incubation lane. It is now staged on the local branch
    notes/c-suzuki-local-capacity-nogo-1 (two commits as
    A. M. Thorn <thorn@twistj.com>: PREREG frozen sha 37cc1a43, then
    verify.py + break.py + RESULT.md; security grep clean). Push from
    this session is DENIED by the git proxy (repo not in the session's
    authorized set). Options: authorize the repo for this session, or
    push from an owner machine, or commit the four delivered files by
    hand. Before the push lands, open a public issue claim for the lane,
    matching the #354/#355/#357 convention of the siblings.
M5  After the merges, the RH complex has four registered incubation
    lanes and one classification obligation. Proposed next structural
    doc AT MERGE TIME (not before): a notes/ index mapping lane -> level
    (leg / kernel / measure / capacity) with each falsifier, so the next
    session starts from the map instead of the branches.
```

RH remains O. Nothing in this recon moves any status.
