# AUDIT: C-ENTROPY-MACKEY-OBSTRUCTION-4-N, Public Canon v28 -> v30

```text
STATUS:          NON-CANONICAL APPLICABILITY AUDIT
AUTHORITY:       NONE
DATE:            2026-08-02
PUBLIC HEAD:     Public Canon v30
TAG:             canon-v30
ACTIVATION:      b8d4d585820d04ebd008444661f3a71d6e24f423
CONTENT_COMMIT:  857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
AUDITED LANE:    notes/entropy-selection-recon-breaker-m2
LANE HEAD:       88026bbb109ec33cff7f96e8b2cc746cf2cc1751
PRIMARY PREREG:  2314e92ee0571cfe9c38e2bd11733ce4a1ba3cc8
SUCCESSOR PREREG:
                 258b40b2dff2c36ee854e099edd9cd1b672c0fd6
SUCCESSOR SHA256:
                 45192f7fcbe3b1699f69ccd35351c8a8ddc756e488a2f01ee0d0491e197f03e6
DECISION:        COMPATIBLE; EXECUTE SUCCESSOR UNCHANGED UNDER ITS
                 EXACT FROZEN V28 INPUT PACKAGE
PUBLIC EFFECT:   NONE
```

This audit creates no claim, changes no status, amends no preregistration,
authorizes no public probe, and supplies no evidence for the Mackey candidate.
It decides only whether the frozen successor breaker remains applicable after
Public Canon v29 and v30.

## 1. Compared authority states

The candidate and successor were frozen against:

```text
Public Canon v28
activation commit 3161cbc764f547c95a80c3bd5028acf71c2ef524
content commit    86a046007f89a64a696d013112a44f02e624dd2e
Canon SHA-256     4b720846ccd42c7ec808ab2acb21793962390b074bb3799d28c0f16c00165d2c
Canon bytes       154316
```

The current authority is:

```text
Public Canon v30
activation commit b8d4d585820d04ebd008444661f3a71d6e24f423
content commit    857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
Canon SHA-256     2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
Canon bytes       157167
```

Public Canon v29 inserted one scientific item, `ENTROPY-RG-RETURN [C]`,
through content commit
`13357f187d2cf5af0e62064395f4d56695409fb2` and activation commit
`607b3e587ec55acc91fd9c61947d600e1cdabc53`.

Public Canon v30 registers no claim and retires none. It republishes the v29
scientific ledger unchanged.

## 2. Field-by-field compatibility

### 2.1 Authority pin

The v28 pin remains part of the frozen historical decision surface.

- Primary prereg: `PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md:10-19`.
- Successor prereg: `PREREG-BREAKER-MACKEY4-2.md:20-30`.

Result: **different by design, not a defect**. Neither preregistration is
rewritten to say v30. This audit establishes applicability to v30 externally.

### 2.2 Finite architecture and generator table

The autonomous architecture and the five generator definitions used to rebuild
the target are unchanged byte for byte:

- `canon-v28:canon/CANON.md:194-204` equals
  `canon-v30:canon/CANON.md:194-204`;
- `canon-v28:canon/CANON.md:976-999` equals
  `canon-v30:canon/CANON.md:976-999`.

These are the inputs required by primary Field 2 items 4-6 and successor
construction C1-C3.

Result: **identical**.

### 2.3 Route A source, measure and equality convention

The complete public definition of

```text
K_TM, m_TM, S_K,
O_(K,lambda), normalized additive Haar,
tau_src(kappa,y) = (S_K kappa,Jy),
P_5, mu-a.e. equality, equivariance, Law_W, and A_A
```

is byte-identical in:

- `canon-v28:canon/CANON.md:1501-1568`;
- `canon-v30:canon/CANON.md:1501-1568`.

The registry row `ENTROPY-LAYER-BRIDGE` is byte-identical at line 166 in both
versions. Its frontier text, scheduler row and gate are also unchanged.

Result: **identical; `ENTROPY-LAYER-BRIDGE` remains `O / STOP`**.

### 2.4 Recurrent carrier, halves and component census

The v28 facts

```text
6250 recurrent states,
312 size-20 components and one size-10 component,
two living halves of 3125 states,
all four half restrictions bijective
```

appear at `canon-v28:canon/CANON.md:1614-1622`. The identical text appears,
shifted only by the new v29 paragraph, at
`canon-v30:canon/CANON.md:1637-1645`.

The exact registry row `ENTROPY-LIVING-SET` is unchanged.

Result: **identical**. This supplies the same input to successor gates C1, C3,
G2 and G5; it does not replace their required independent reconstruction.

### 2.5 Depth-five lambda carrier and source cycle data

The exact v28 statements

```text
ord(J mod lambda^i) = (4,20,20,20,20,20,100,100),
Spec(J on O/lambda^5) = {1:1,4:1,20:156},
|O/lambda^5| = 3125
```

are unchanged between v28 `canon/CANON.md:1624-1633` and v30
`canon/CANON.md:1647-1656`. `ENTROPY-COUNT-MATCH` is byte-identical.

Result: **identical**.

The candidate's source factor level `r` in `c_src(r)=158,315,629` is not the
renormalization scale `k` of `ENTROPY-RG-RETURN`. The new row neither proves nor
changes the source count at `r >= 2`.

### 2.6 Dihedral torsors

`COLOR-TORSOR-HOLONOMY [T]` remains byte-identical at
`canon/REGISTRY.tsv:40` in both versions. It still says that the 312 size-20
attractor halves are free `D_5` torsors and the singlet half is the five
reflection axes.

Result: **identical**.

### 2.7 Mirror and finite cocycle data

The v28 finite mirror statement is unchanged between v28
`canon/CANON.md:1664-1677` and v30 `canon/CANON.md:1687-1700`.
`ENTROPY-MIRROR-LAW` and `ENTROPY-AFFINE-COCYCLE` are byte-identical in the
registry.

Both remain explicitly finite and gauge-specific. Neither version publicly
asserts the candidate's stronger premise that one global marked `D_5`
representation supplies the same four edge labels on all components.

Result: **identical; the common-cocycle premise remains candidate-specific and
genuinely open to the successor breaker**.

### 2.8 Mackey menu and mixed control

The subgroup menu and equation

```text
{313,625,1563,3125},
312a+b=629,
unique mixed solution (a,b)=(2,5)
```

are frozen candidate mathematics, not a changed public Canon input. No v29 or
v30 row adds another subgroup orbit count or puts 629 into the common menu.

Result: **unchanged**.

### 2.9 ENTROPY-RG-RETURN

The only new scientific input since v28 is:

- v30 `canon/CANON.md:1614-1635`;
- v30 `canon/REGISTRY.tsv:171`;
- v30 `canon/DEPENDENCIES.tsv:207`.

It establishes fixed sets and multipliers of the block maps
`Phi^(k)_eps` for `k=0..14`. It is compatible with the older facts:

- at `k=0`, the own-letter map has one recurrent reflection centre and
  multiplier `-I`, consistent with the finite mirror statement;
- at `k=1 mod 4`, the block map returns the opposite full living half with
  identity multiplier, consistent with the cross restrictions being mutually
  inverse;
- every block-map image has 3125 states, extending the finite audit of
  `ENTROPY-BLOCK-HALVING`.

It does **not** test whether the same global marked `D_5` acts on every
component. It contains no common-cocycle, Mackey-range, Haar-quotient,
component-count obstruction, measurable-selection or measure claim.

The dependency ledger gives `ENTROPY-RG-RETURN` exactly one edge:

```text
ENTROPY-RG-RETURN -> DEF-ARCHITECTURE  REQUIRES
```

There is no edge from it to `ENTROPY-LAYER-BRIDGE`, the Mackey candidate, or
any common-cocycle premise. Existing bridge dependencies are unchanged.

Result: **additive and compatible, not load bearing for the frozen decision**.

### 2.10 Status ceiling and action layer

The candidate remains bounded by the same `C`-grade finite inputs and excludes
an `A_A=empty` conclusion. `ENTROPY-RG-RETURN` is itself `[C]`, at L5, and
explicitly adds no measure or all-scale law. It neither raises nor lowers the
candidate ceiling.

Result: **unchanged**.

## 3. Decision

```text
COMPATIBLE.
PREREG-BREAKER-MACKEY4-2 does not need retirement.
Its expected values, controls, thresholds and scope remain unchanged.
```

No scientific input needed by the frozen successor was changed or withdrawn.
The new v29 row is compatible with, but does not decide, its common-cocycle
gate. V30 contains no additional scientific change.

The owner ruling already forbids amendment of the frozen successor and names it
the sole live successor instrument. It also records that a successful successor
re-establishes only target-side items E4 and E6-E12 and leaves source items
E1-E3, E5 and E13 without a live breaker.

## 4. Strict execution conditions

Compatibility does not broaden the frozen independence package.

1. The clean implementing session receives exactly the material permitted by
   `PREREG-BREAKER-MACKEY4-2.md:65-103`.
2. Every public Canon input supplied to that session is read from the exact
   `canon-v28` tag, not from the current working-tree copy of v30.
3. In particular, the session must not receive:
   - this compatibility audit;
   - current v30 section 3;
   - `probes/P-ENTROPY-RG-RETURN-1/`;
   - any project summary, adjudication digest or paraphrase of a forbidden
     file.
4. The v30 applicability conclusion is attached only after the clean run, by
   an adjudicating session.
5. `mackey4_cocycle.py` is frozen and hashed before its first execution on
   `F_5^6`. Only syntax checks and synthetic `D_5` unit tests permitted by the
   frozen preregistration may precede that pin.
6. A successful successor result supplies no full two-route Mackey result. The
   separate source-side preregistration required by the owner ruling remains
   necessary.

At audited lane head `88026bbb109ec33cff7f96e8b2cc746cf2cc1751`,
`mackey4_cocycle.py` is absent and no result or run record under breaker 2
exists, consistent with the freeze record.

## 5. Stop and retirement conditions

Stop and retire breaker 2 in favour of a new identifier if any of the following
occurs:

- implementation requires an output or premise from `ENTROPY-RG-RETURN`;
- the clean session reads current-v30-only scientific material or the new probe
  code;
- any frozen generator, Route A type, recurrent carrier, living-half,
  depth-five spectrum, torsor or mirror input is shown not to be identical;
- a new registered dependency makes the RG row load bearing for the candidate;
- expected values, controls, thresholds or scope must move;
- the first claim-carrier execution occurs before the code pin;
- any forbidden material reaches the implementing session by summary or
  handoff rather than direct file access.

Any such event is a preregistration/input defect, not evidence for or against
the public entropy bridge.

## 6. Local pre-pin preparation record

This section is adjudicator-side bookkeeping. It is not part of the frozen v28
input package and must not be supplied to the clean implementing session.

```text
SESSION:        target_breaker_author
WORKTREE:       D:/twistj-mackey-target
BRANCH:         codex/mackey4-cocycle-prepin
BASE:           258b40b2dff2c36ee854e099edd9cd1b672c0fd6
CODE:           notes/entropy_selection/mackey4_cocycle.py
CODE STATUS:    UNCOMMITTED, UNSTAGED, NOT PINNED
FINAL SHA-256:  c00a2897f6dc5038e0e08a4c22e310bae0e219206cf0200636dbf168584038e4
FINAL BYTES:    48471
CLAIM CARRIER:  NOT EXECUTED
```

The clean session declared that it read only the frozen whitelist and that no
`F_5^6`, recurrent core, real target gate, network, GitHub, git history, other
branch/worktree, forbidden file or expected target output was accessed.

Permitted pre-pin checks:

```text
py_compile                         PASS, Python 3.9.13
synthetic-only run 1               exit 0, stderr 0
synthetic-only run 2               exit 0, stderr 0
synthetic-only run 3               exit 0, stderr 0
synthetic-only run 4               exit 0, stderr 0
synthetic stdout, all four         925 bytes
synthetic stdout SHA-256           e6205bab0bbfb005c4c1d0cb11ed501984e4c86d722126326b6dff7aab4f4321
controls                           N1 REJECT, N2 REJECT, N3 ACCEPT
```

Run 1 used code SHA-256
`b4e15d2237466794585c4625c439b1814a8d425da814322637cfa3b88665eac5`
and runs 2 and 3 used
`21828515f0da036b584dbea254516eb96ea6d020534fadde5444ebc1d6f8812b`.
Static review then found that `C1` input mismatches would be misclassified as
`B2-F1`; the clean author changed only that exception and handler path. Run 4
used the final SHA-256 above and retained the same synthetic transcript.

The first code hash and the raw hashes of the first two identical transcripts
were reconstructed after the fact rather than recorded contemporaneously;
wall-clock timestamps are also unavailable. This limitation is disclosed and
earns no evidential credit. Runs 3 and 4 supplied contemporaneous raw-byte
captures. Two wrapper attempts failed before launching the instrument and are
not executions.

No real-target execution is authorized until governance permits an immutable
code pin and the exact pinned bytes have been independently read back.
