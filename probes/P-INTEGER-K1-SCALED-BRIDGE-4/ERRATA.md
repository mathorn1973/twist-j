# Post-run source and description errata for P-INTEGER-K1-SCALED-BRIDGE-4

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This file is additive. The six prospective files frozen at pin
`fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce` (`PREREG.md`, `PROOF.md`,
`SOURCE.md`, `verify.py`, `breaker.py`, `FROZEN.sha256`) and `EXPECTED.txt`
(1409 bytes, 27 lines, SHA-256
`61a71ef6ccee63c4e0e8ebc1f2c08ec48f11768cfa604d3969b2201bf8089ed1`) are
unchanged. The completed exact PASS stands as evidence of the pinned
computations; it is not relabelled. Nothing here changes the verifier, a
status or a scope, and nothing here is a Canon promotion or an Einstein
source law. Where this file and an earlier statement disagree, this file
supersedes that statement for downstream use; the earlier text is not
rewritten.

Basis: the post-run analytical and custody review
[#1639 comment 6263553901](https://github.com/mathorn1973/twist-j/pull/1639#issuecomment-6263553901)
(core B1 to B5 supported at the narrow frozen scope; CHANGES REQUESTED on the
source record and the PR summary), and row E of
`notes/canon/V104-RELEASE-REVIEW.md`, which requires explicit audit errata
for "actual v103 source, 11/13/40 coords, true reader/metric, admission not
source forcing, normalized breaker comparison". Each repository fact below
was re-checked on 2026-11-08 against the objects named.

## 1. Canon identity in the frozen `SOURCE.md`

The frozen `SOURCE.md` names the correct base commit but the wrong Canon:

| Field | Frozen `SOURCE.md` | Actual declared base |
|---|---|---|
| Public Canon | v1, tag `canon-v1` | **v103, tag `canon-v103`** |
| Base commit | `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` | `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d` (peeled `canon-v103`) |
| Content commit | not stated | `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66` |
| Canon SHA-256 | `31d2fbce3effe7fbca29ab7e65dc0cfbf3fb4aa9fc2ebdeaa4f33ca4739a6d6e` | `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b` |
| Canon bytes | 99872 | 1052518 |

The verifier checks the bytes of its own frozen files and reads no Canon file
at run time. The green replay therefore does not validate the Canon identity
asserted in `SOURCE.md`; this erratum does.

## 2. Unregistered identifiers

`SOURCE.md` cites `O-G-EINSTEIN-SOURCE-LAW-1 [O]` and `GATE-L1-L2-MANIFOLD`
as normative inputs, and `RESULT.md` names `O-G-EINSTEIN-SOURCE-LAW-1`. Neither
identifier occurs anywhere in `canon/` at Public Canon v103, nor in
`canon/CANON.md`, `canon/REGISTRY.tsv` or `canon/GATES.tsv` at v109. They are
informal labels of this probe, not registered claims or gates.

## 3. What the frozen construction actually is

The PR description summarised a different object. The frozen `PREREG.md`,
`PROOF.md` and code define:

- an **11-integer** K1 core `(U, W, k)`, a **13-integer** funded K1 carrier,
  and a **40-integer** combined funded source-holonomy-K1 apparatus
  (`2 + 8 + 8 + 8 + 5 + 5 + 1 + 1 + 1 + 1 = 40`). No 43-integer carrier and
  no stored four-bit word register is defined;
- the reader `h_k(r) = U_r / (2 * 324^k)` and the update
  `(U, W, k) -> (C U - 104976 W, U, k + 1)`, with the explicit
  congruence-guarded partial inverse. The claimed integer numerator with
  `D_n = 324^(n-1)` fails already at `n = 1`, where `h_1` has entries `1/2`;
- the **4 by 4** metric `g_r(U, k) = diag(-1, 1 + h_k(r), 1 - h_k(r), 1)`,
  with signature **(-,+,+,+)** on canonical reachable histories, and
  `det g_r = -(1 - h_k(r)^2)`. The determinant is not constant: for `w = 0010`,
  `r = 0`, `h_1 = 1/2` gives `det g_1 = -3/4` and `h_2 = 163/216` gives
  `det g_2 = -20087/46656`. The frozen proof supplies the strict negative
  bound `det g < -199/10000`, not determinant constancy. On the full integer
  carrier, outside canonical histories, `k = 1` and `U_r = 648` give the
  degenerate form `diag(-1, 2, 0, 1)`.

A faithful summary is: an exact scaled integer K1 carrier, a total funded
reflection bijection obtained from a partial inverse, sharp finite precision
horizons, a rational additive metric reader, and a shared-bank 40-integer
source/K1 apparatus.

## 4. Admission, not source forcing

The shared bank can admit or reject a K1 step. On fully admitted seven-phase
blocks the update factors into the six source-holonomy phases and one K1 step.
At fixed seed `w` and reached counter `k`, both source signs give exactly the
same metric. At bank `36214831147` the two signs reach different counters
after seven ticks; at bank `36214831203` both reach the same `h_2^(0010)`. The
source therefore changes admission and timing. It is not a source term in the
K1 recurrence.

## 5. Breaker comparison is normalised

`run_breaker_and_compare` strips every line and discards blank lines before
comparing. It enforces equality of normalised certificate lines, not raw
byte identity of the breaker's stdout. The external two-architecture
comparison of the complete verifier stdout is byte-exact and remains valid.
The two implementations differ in arithmetic (matrix and `Fraction` versus
cyclic-five coefficients and integer gcds), but the K1 initializer, operator,
account and reflection functions and the enumeration share one code
structure; the subprocess proves execution isolation, not independently
authored premises.

## 6. Predecessor history and counts

- The three predecessor pins remain ABANDONED records (#1636, #1637, #1638,
  merged 2026-11-08). The record status does not mean that no computation or
  false frozen expectation was met: `-1 -> -2` also corrected audit boxes,
  `J_INV` and the breaker's transport and norm; `-2 -> -3` corrected the
  shared canonical word list and initial-slice helper; the `-3` preregistration
  required `v_3(gcd(U_n, 2 * 324^n)) = 0`, which is false at `n = 1`
  (the gcd is 324, valuation 4), and `-4` changes the requirement to 4.
  The wrong `canon-v1` identity of item 1 was introduced in `-2`.
- The 2184 K1 test entries include overlapping sub-boxes. The number is an
  enumerated test-case count, not a count of distinct states.
