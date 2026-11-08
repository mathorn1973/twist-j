<!-- SPDX-License-Identifier: Apache-2.0 -->

# Sources, custody and review status

**NON-CANONICAL / L1.** Reservation: [#1922][claim]. Readback date: 2026-11-06.

This package records exposed work. The computations were run in one review
session before the public reservation, against a recon text frozen privately
before its first execution. Nothing here is a preregistered public probe. For
the native part no new theorem is claimed.

## Public authority

The authority readback is [STATUS.md at public main][status]:

- State: ACTIVE, Public Canon v109.
- Activation and inspected main: `650029c20408f1dd665983d72225d0d195fd030e`.
- Content: `2b0f94ec1e0874bff9141259e0b7da80e6681ea6`.
- Tag: `canon-v109`; annotated object
  `a33f63339b16b69725bf856e403610614143f81f` resolves to that activation.
- Canon SHA-256:
  `035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383`.
- Canon size: 1,464,066 bytes.

All five normative files matched the pinned [SHA256SUMS][normative]. This is
file-custody validation, not a new execution of scientific evidence. The main
[two-architecture run 41722841143][main-ci], the [tag readback
41722907354][tag-ci] and the [release readback 41730671371][release-ci]
passed. They concern that authority tuple and confer no status on this note.

## Registered rows used

Line numbers refer to `canon/CANON.md` at the inspected main.

| Row | Status | Line | Used for |
| --- | --- | ---: | --- |
| native conventions | definition | 7239 | the update `U`, the selector, the five generators |
| U-NATIVE-CHART-AND-QDD-READBACK | T | 1058 | reachable sheet, conserved labels, `S`, `t_n`, `N_n` |
| U-NATIVE-APPARATUS-HISTORY-FACTOR | T | 1344 | closed quotient `(z,q,r)` and its table |
| U-NATIVE-WHOLE-SHEET-RETURN-WINDOWS | T | 17515 | (WR-3) to (WR-5) |
| RELATIVE-CONTACT-INTEGRAL-LAW | T | 13594 | ring, total contact, conserved sum, norm and residues |
| RELATIVE-CONTACT-FOUR-SLOT-MINIMUM | T | 13666 | only the displayed congruence `q(x)=2r(x)^2 mod 5` at line 13697 |

## Public probe inputs

Both pull requests were open drafts, unmerged, at the readback date. Their
x86_64, aarch64 and aggregate checks were successful.

| PR | Immutable head | Used here | CI run |
| --- | --- | --- | --- |
| #1908 | `8d39e90b5ae29e7586f33c3a3e5a0d653f04fe7c` | the bytes of [WORD.txt][w1908]; the counts table of [RESULT.md][r1908] | [41935448124][ci1908] |
| #1915 | `0e37679a60f577b809816c7daf29c8a243a637c8` | the stated windows and their lifted values in [PROOF.md][p1915]; its two pair laws, for comparison | [41996122385][ci1915] |

At the readback date #1908 had one submitted COMMENTED review and no
approval; #1915 had no submitted review. Successful CI and a review comment
are different evidence categories; neither merges or promotes a pull request.

Their scopes remain their own. The fixed word, its endpoints, its counts and
the counts of its slot-exchanged image are results of #1908. This note adds
the columns `N6`, `Q` and `H` on those runs and reads the published counts as
a comparison of two paths. The pair law is a result of #1915. The corollary
in NATIVE.md is proved from the registered rows alone and does not depend on
#1915. It adds the closed form in the registered function `S`, the tick law
for windows of either parity, and the extension to every origin-zero
trajectory from counter 3.

`WORD.txt` in this directory is a byte-identical copy of
`probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/WORD.txt` at the head above:
966 bytes, SHA-256
`6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7`. It is
copied because #1908 is not merged and the scripts must run from the
repository root. Both contact scripts check that hash before use.

## The frozen recon text

The working name of the recon is RECON-PATH-PHASE-ONE-CARRIER. Its text was
frozen at 2026-11-06T00:10Z, before the first execution of any script:
8965 bytes, SHA-256
`e557dab31e8a801b53f57af74d431c64697cfdc71b8b1199f856a6b8b1dfa0a6`. The
freeze was private. Its time and the order of events below are the session's
own record and cannot be checked from public data.

The text has three parts. Parts U and K are the subject of this note. Part D
concerns a different carrier, the D3 lattice, and a different question. It
lies outside reservation #1922 and is not published here. Its script ran in
the same session and none of its clauses fired. No statement of this note
rests on it, and nothing here is evidence for or against it.

[RECON-PREREG-EXTRACT.md](RECON-PREREG-EXTRACT.md) is therefore an extract.
Below its rule it carries the frozen text byte for byte, except that four
passages are replaced by bracketed markers. The extract body has 7853 bytes
and SHA-256
`d38e9a06ed5494d0ce669b41aedb29a034ff6e6a0b3333540a6e6ea5fe49379d`.

| Marker | Omitted bytes | SHA-256 of the omitted passage |
| --- | ---: | --- |
| O1, with its heading line | 1138 | `bb003a921fbc17e6f32356b2d41e6baeca2d555b39672a632e4a6abfab938d9c` |
| O2 | 24 | `70a1a7eb39e4142a634b9d8e699dbdb1c1e0b98766a77c47213b4a5831c8dc8f` |
| O3 | 138 | `829276502c4c81529e9050e2c487ccf72667620da18bf5f8b8f467ab79aac5a8` |
| O4 | 79 | `16c90a2b57e8539644b2a43ca6ef33fc219282756ee71d8f6125f7c71dc832d9` |

Putting the four passages back in place of their markers reproduces the
frozen bytes and the frozen hash. The complete text is retained with the
session records. The clauses of Parts U and K, their thresholds and the
declared hypothesis H_AREA are complete in the extract.

## The breaker

`break_recon_parts_u_k_2026-11-06.py` is an extract of the session breaker
(13583 bytes, SHA-256
`dd89ffc375f75f71a7f22fa650b6362d490fce76c45ef2b0f5c430da5a1e68b6`). Its
section B-D belongs to Part D and is removed: one docstring line (69 bytes,
SHA-256 `6c954c77ddb78663e8affacf0a4be7a23c513d28f950d6a4c405d43930681c27`)
is replaced by a notice, and 41 lines (1584 bytes, SHA-256
`121e00fd1b644984ada72fe3ce59950b4a9b1b51a3040a7954a3f63f60816a82`) are
replaced by a one-line comment. No other byte differs. The removed section
comes last and shares no state with the others. The extract was rerun from
the repository root. Its output equals the session output with the single
B-D line removed.

## What was exposed when

1. **Before the freeze.** As the frozen text lists: `STATUS.md`, the
   registry alpha rows, the text files and verifier sources of #1908, #1912,
   #1915 and #1917, and the counts table in `RESULT.md` of #1908. The frozen
   text also quotes the native conventions of the Canon and the contact law,
   which had therefore been read. The per-step traces in `EXPECTED.txt` of
   #1908 were replayed for byte identity but not read. No quantity of the
   frozen clauses was computed before the freeze.
2. **Frozen clauses.** U1 to U7 and K1 to K5 with their thresholds. K4
   replays a published table and is not a prediction. K3 is a blind
   consequence: `N6`, `Q` and `H` had not been computed or read. K5 declared
   the hypothesis H_AREA with its falsifier, and the falsifier fired.
3. **After the first run, not preregistered.** Theorem L and its proof; the
   path-difference lattices; the literal replay of the closed word; the
   search for the shortest closed word with a count outside `5Z` and the
   pair `P27`, `P35`; the check of the logarithmic coordinate; the breaker
   with its second potential and its random banks.
4. **While this note was written.** The frozen text derived the native
   expectations from the native law directly. Only afterwards were the
   registered chart, history-factor and return-window rows recognized as
   already implying them. The note therefore states a corollary, and its
   audit confirms registered theorems on this question. It is not a
   discovery about native U. The tick law of (C3), which extends the integer
   formula from even windows to windows of either parity, and its check
   `check_tick_law_2026-11-06.py` were also written at this stage. That
   check passed on its first run.

## Two harness errors

Both are kept. Neither touched a frozen clause or a threshold.

1. **Contact recon, run 1.** A side assertion expected 1556 states for the
   six-slot orbit of `I_0`. That size belongs to a different alphabet, a
   bank of 64 macro words, and not to the fifteen single contacts, whose
   orbit has 2060 states. The assertion was not a frozen clause. Run 1
   printed one `FAIL` line and `RESULT FAIL fails=1`; its output is
   `recon_contact_phase_2026-11-06.run1-side-assertion.stdout`. The assertion
   was replaced by a recorded `NOTE` line. Script SHA-256 before:
   `39cc3fe466f2b7ffff3722f9368627f5d13f0cbd50749e1f61fe218c329357cd`.
   The two outputs differ in that line and in the final line only.
2. **Breaker, run 1.** The affine tables kept entries unreduced, `-1` in
   place of `4`, so the test of the fibre row against `(1,4)` failed at
   counter 3 on the bare table of `b`. Run 1 printed
   `FAIL B-U for 3<=n<4096: composite 3->n has r-row (0,0,0,0,0,+-1) and
   piston rows free of q,r` and `RESULT FAIL fails=1`. The fix reduces the
   table entries modulo 5 in one line. Script SHA-256 before:
   `f41b1432c588c79c15bbd316ea0d488392cff11d3593b740d89a49eb8a417ef4`. All
   other lines of the two outputs are identical. The run 1 output is quoted
   and not attached, because the breaker is published as an extract.

## Evidence limits

- One session and one architecture: x86_64, Python 3.13.18, Ubuntu 24.04.
  Every finite statement is at most candidate-C. Byte identity on a second
  architecture has not been established for these scripts.
- The breaker uses separate code paths written in the same session. It is
  authoring quality assurance, not independent review.
- Proposition K and Theorem L are written proofs at candidate-T, pending
  independent mathematical review.
- The orbit of `I_-2` is capped at 200000 states with 98710 edges skipped.
  Statements about it are lower bounds on the explored part.
- The note was prepared in a Claude review session at Marek's request. The
  complete frozen text, the session breaker and the run 1 outputs are
  retained with the session records.

Ordinary notes CI checks repository integrity and the applicable existing
rules. It does not run these scripts, test these proofs or satisfy a
two-architecture computation gate.

## Disposition

Keep these results as NON-CANONICAL candidates. A later formal probe on any
of them needs its own question, falsifiers and verifier, frozen and publicly
pinned before execution, with this note disclosed as exposed knowledge. No
Canon, registry, frontier, gate, predecessor probe or workflow is changed.

[claim]: https://github.com/mathorn1973/twist-j/issues/1922
[status]: https://github.com/mathorn1973/twist-j/blob/650029c20408f1dd665983d72225d0d195fd030e/STATUS.md
[normative]: https://github.com/mathorn1973/twist-j/blob/650029c20408f1dd665983d72225d0d195fd030e/canon/SHA256SUMS
[main-ci]: https://github.com/mathorn1973/twist-j/actions/runs/41722841143
[tag-ci]: https://github.com/mathorn1973/twist-j/actions/runs/41722907354
[release-ci]: https://github.com/mathorn1973/twist-j/actions/runs/41730671371
[w1908]: https://github.com/mathorn1973/twist-j/blob/8d39e90b5ae29e7586f33c3a3e5a0d653f04fe7c/probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/WORD.txt
[r1908]: https://github.com/mathorn1973/twist-j/blob/8d39e90b5ae29e7586f33c3a3e5a0d653f04fe7c/probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/RESULT.md
[p1915]: https://github.com/mathorn1973/twist-j/blob/0e37679a60f577b809816c7daf29c8a243a637c8/probes/P-U-PAIR-PHASE-WORK-1/PROOF.md
[ci1908]: https://github.com/mathorn1973/twist-j/actions/runs/41935448124
[ci1915]: https://github.com/mathorn1973/twist-j/actions/runs/41996122385
