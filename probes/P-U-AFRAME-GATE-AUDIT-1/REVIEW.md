# Independent review of P-U-AFRAME-GATE-1

PUBLIC / NON-CANONICAL / L1 / candidate-T.
Reviewer/session: ChatGPT-v103-RA-20261016-05ccc15f, claim #1559.
Author A. M. Thorn; original work Apache-2.0.

## Decision and exact object

**ACCEPT at the frozen L1 scope. No blocking mathematical, implementation,
custody or required-check finding.** The submitted proof survives an
independently written proof and implementation. This is a review
recommendation for the lane-A submission, not a merge, Canon promotion,
physical interpretation, or acceptance of the present audit by its owner.

Reviewed author submission:
[draft PR #1557](https://github.com/mathorn1973/twist-j/pull/1557), exact head
`5c8a675cc114dd3e1f4d95226fd22ba82e3891fa`, spec pin
`7b06ea6b377930f6edeb84cb330b9d69f1b82c51`, claim
[#1550](https://github.com/mathorn1973/twist-j/issues/1550).
Its entire diff adds nine files in `probes/P-U-AFRAME-GATE-1/` and changes
no other path. The six initial files are unchanged at the result head;
only `EXPECTED.txt`, `RUN.md` and `RESULT.md` were subsequently added.

Our independent spec is `a19a2f38517863a480476abb35fa45bfa4dfdfeb`;
our first-run record is `dac3cd215314b2d426ecfebe76890e082df9691c`.
Our five initial files remain unchanged. Both submissions use Public Canon
v102 at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, whose normative content
is `b04e22dd3ed8e4240cff347364f24670d4183a4d`. The prescribed authority,
source hashes, tag/main ancestry and publication checks were verified.

## Independence and exposure chronology

The expected hypotheses in #1548 and the author's PREREG were known.
Before our pin and first record, the admitted author material was only
`PREREG.md` and `SOURCES.tsv` at its immutable spec. The author proof,
implementation, transcripts, run/result reports and exposing PR diff
remained unopened. Same-session helpers worked inside this one RA claim;
they are not additional independent reviewers.

| Event | Public custody evidence |
| --- | --- |
| v102 release gate completed | Run `38956254023`, attempt 2, completed 2026-10-16 20:55:11 UTC |
| Author pin/readback | [#1550 receipt](https://github.com/mathorn1973/twist-j/issues/1550#issuecomment-6224691403), 21:06:05 UTC; six byte-identical initial files |
| Author specification exposed to RA | [#1548 metadata](https://github.com/mathorn1973/twist-j/issues/1548#issuecomment-6224691745), 21:06:06 UTC |
| Author first record | Commit `5c8a675cc114dd3e1f4d95226fd22ba82e3891fa`; [result metadata](https://github.com/mathorn1973/twist-j/issues/1548#issuecomment-6224731896), 21:08:48 UTC |
| Our independent public pin/readback | [#1559 receipt](https://github.com/mathorn1973/twist-j/issues/1559#issuecomment-6225089549), 21:31:25 UTC; all five initial files byte-identical |
| Our first execution | 21:31:52.735827 through 21:31:54.240138 UTC, clean Linux x86_64 tree at the pin; F1-F9 PASS, exit 0, empty stderr |
| Our first result committed, pushed and read back | `dac3cd215314b2d426ecfebe76890e082df9691c`; [barrier-release receipt](https://github.com/mathorn1973/twist-j/issues/1559#issuecomment-6225116366), 21:33:11 UTC |
| Author comparison | Began only after the preceding committed/publicly read-back record; proof, code, results, custody and CI then inspected |

No execution, import, dry run or benchmark of our scientific code occurred
before our pin. The own first run had no repair or retry. The later
prescribed reproduction of the author program is explicitly a replay of
the author's implementation, not our independent implementation.

## Complete mathematical and implementation review

The author references below name sections of its frozen `PROOF.md` and
functions of its frozen `verify.py`. Our `PROOF.md` and F1-F9 verifier are
the independent comparison, already committed before author exposure.

| Falsifier | Review conclusion |
| --- | --- |
| F1 native premises | All 15625 states and 78125 generator cases use the actual six-coordinate maps. Involutions, quotient/trace laws, fixed counts and the 011 synchronization agree with v102. Both selector bits are covered. These are inherited premises. |
| F2 field/image | The unchanged integer matrices satisfy the factorization, commutation, inverse, determinant, unimodular image certificate and energy-scale identities. Exhaustion covers all 625 residues. Author Proposition 1 also proves the complete integer image criterion through `5 Z^4` being contained in `L Z^4`; it does not infer that infinite criterion from sampled lifts. |
| F3 comparison/gate | Proposition 2 correctly identifies `h=0` with `W(p)` in the 25-point image `C`. It proves the gate counts 625 overall, 125 per trace sheet and 250 in `X14`. The explicit energies 2 and 3 disprove an H-isometry of W. |
| F4 generator laws | Proposition 3 and all 15625-state checks agree. The map `p -> (h(p),h(ap))` is bijective, so no h-only a law exists. The zero/nonzero witness is valid. Exactly 25 gated states survive a, exactly the 125 with r=0 survive c, and b,d,e preserve gate membership and its complement. |
| F5 full selector | All ten branches are derived and tested on 31250 state-bit pairs. The c branch retains its signed r contribution; no trace is added as a seventh coordinate. |
| F6 all-time statement | Theorem 5 has an explicit base and an induction step on the entire 12500-pair synchronized domain. The next h is -h or -J2 h, both invertible. The gate and its complement are forward invariant for any future binary driver. Exact image, two preimages, one fixed point and 249 moved gated points per bit are correct. |
| F7 inheritance | The V law, its 625 values with ten preimages each, and the preimage of S are correct. The gate comprises 13 complete sign fibres, one of size 10 and twelve of size 20. Gate invariance is expressly inherited from U-NATIVE-INVARIANT-AND-NOWRITE. See the phase qualification below. |
| F8 complete prefix | Section 6 proves the chronological words ace/bbd/cce/dbd/ebd and all h1,h2,h3 formulas. In cce, the second c uses the already negated r. Separate-time counts are not confused with simultaneous survival. Exactly 625 preparations are gated from n=3 and exactly 401 from n=0; the latter split is 1,125,25,125,125. The zero preparation has r3=1. |
| F9 finite regression | The zero orbit includes all 4097 boundaries 0 through 4096. All 15625 preparations are checked through boundary 40, with synchronized assertions at every boundary 3 through 40. Both proof and result label this as regression; it is not the all-time proof. |

The implementations are distinct. The author uses direct coordinate
formulas and recursive determinant expansion; our verifier uses sparse
affine rows, precomputed transitions and permutation determinants. The
author represents a sign fibre by `frozenset({V,-V})`; ours uses its
lexicographically smaller representative. Neither verifier contains a
precomputed expected value for either set digest.

All numerical assertions use exact integers or residues. The author
checks divisibility before integer division. Its success text is emitted
only after the underlying assertions complete. There is no random input,
tolerance, fitted parameter, network access or floating arithmetic in the
scientific implementation. Its runtime custody check reads only its
frozen initial files. Complete finite checks support the written proof;
they do not replace its quantifier arguments.

## Independent set agreement and reproductions

Both first outputs compute the following digests from sorted tuples with
one LF-terminated comma-separated row per tuple. These are actual output
agreements, not newly selected targets.

| Set | Rows | Author and independent SHA-256 |
| --- | ---: | --- |
| G14 | 250 | `373778349c9cb18ff376e726b23d381d0c62a26c7c5d6c9f2d8c31e2e395b097` |
| All-time gated initial states | 401 | `1640c7f998e9fb47a45e2b08182e34ee847b0c7073e91d0864fb3307a165b312` |

The different implementations have different descriptive transcripts.
Author stdout is 1295 bytes / 12 lines, SHA-256
`9be841f9aeb89c9962ea43387d52d8d9cc9aca3b74e2d916824e6607deff8e36`;
our stdout is 1044 bytes / 14 lines, SHA-256
`5fae6e8c596460e3b1d2a71a6460c0d3d7ddaf4ad10fc9e33e3db576158e1477`.
Each transcript is separately reproduced against its own exact EXPECTED.

On Linux x86_64 / Python 3.12.14, the unchanged repository command
`python3 tools/check_verifier.py --base a632c6a162dc87e60104d7a478e7650a6d5c4a1b`
returned `VERIFY PASS` separately for our completed record and for the
author's exact result head. These are reproductions, not extra independent
implementations. All six author initial files were also compared against
its spec pin and its INPUTS manifest; no byte changed.

The author's required [workflow run 38967260429](https://github.com/mathorn1973/twist-j/actions/runs/38967260429),
attempt 1, has the exact reviewed head and completed successfully. Logs of
[aarch64 job 117196701975](https://github.com/mathorn1973/twist-j/actions/runs/38967260429/job/117196701975)
and [x86_64 job 117196702392](https://github.com/mathorn1973/twist-j/actions/runs/38967260429/job/117196702392)
both contain `VERIFY PASS` with verifier SHA-256
`d9fe50b340e527f08003dcaaacab8d798a5d3b306157f48aa189fbd67d0743a0`
and the author stdout hash above. The
[aggregate check 117197043252](https://github.com/mathorn1973/twist-j/actions/runs/38967260429/job/117197043252)
also passed. The publication job is correctly skipped for this PR event.
The present RA PR has its own required checks; their head-specific receipt
belongs in its public conversation after completion.

## Nonblocking qualifications retained by this review

### Gate membership, exact image and fixation

The author's summary phrase "set preservation" in PROOF section 5 and
RESULT answer 4 must be read as forward preservation of membership. The
exact statement, already established by its proof and code, is

```text
T_t(G14) = G intersect X_(4+2t mod 5),
|T_t(G14)| = 125,   |G14| = 250,
every image point has two preimages in G14.
```

It is not equality `T_t(G14)=G14`, and it is not pointwise fixation.
For any later synthesis use the exact image or the phrase "gate membership
is preserved." This is a wording qualification, not a failed theorem.

### The known trace phase in the V explanation

The author's PROOF section 5 and RESULT inheritance paragraph compress the
full Klein law into two V functionals. With
`A=2V1+V2`, `B=2V3+V4`, and the known `chi(z)` in `{1,-1}`, the precise
reconstruction is

```text
h1=(A+chi(z) B)/2,   h2=(A-chi(z) B)/2   in F5.
```

The equality `h=0 iff A=B=0` proves gate invariance directly from
`V(next)=-V`. To distinguish the whole vector step `-h` from `-J2 h`, one
also uses whether the already known trace phase changes sign. The author
has this phase in its sheet table and proves the main theorem directly
from the generators, so there is no proof gap. Later reuse should retain
the phase when describing the entire vector law.

### Failure diagnostics

The author's `need(condition,label)` retains the first failing predicate
but would not print its full state/bit witness. The frozen author contract
does not require that diagnostic detail and no predicate failed. Our
independent implementation does retain such witnesses. This is a useful
future implementation improvement, not grounds to modify either frozen
source or reopen the completed run.

## Inheritance, scope and handoff

The underlying U maps, sheet synchronization, quotient, fixed-point table,
field algebra, integer image criterion and sign-class invariant
`R={V,-V}` are inherited; the readout V itself changes sign at each step.
This submission explicitly calculates the selected W/L residue
identification, all generator and selector readouts, the nonclosure of a,
and the full preparation classification. Its all-time permanence on X14
does not establish a new writable invariant or a new physical memory.

The negative controls remain part of the accepted scope: W is not an
energy isometry, a is not h-closed, a zero gate is not a fixed checkpoint,
and the actual zero preparation does not keep r=0. No universal integer
trajectory of U, minimum-energy lift, physical preparation, port, contact,
message transfer or L2-L6 actuation is derived. No sibling lane's result
was used as an input to this audit.

The author submission satisfies the stated review criteria at this exact
head. The present audit is handed to a different controller, who should
verify its immutable pin/first-record chronology, source and file hashes,
complete F1-F9 coverage, comparison qualifications, and its own required
two-architecture PR checks. Same-session helper reviews do not discharge
that handoff. Both public submissions remain NON-CANONICAL at candidate
scope; Public Canon v102 remains the authority.
