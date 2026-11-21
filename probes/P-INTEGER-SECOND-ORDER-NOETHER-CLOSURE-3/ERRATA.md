# Post-run errata for P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3

PUBLIC / NON-CANONICAL / NEW_DECLARED L1. A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

This file is additive. The six prospective files frozen at pin
`56437c4ef2c2e3a5aee679bb87b693395213f644` (`PREREG.md`, `PROOF.md`,
`SOURCE.md`, `verify.py`, `breaker.py`, `FROZEN.sha256`) and `EXPECTED.txt`
(1022 bytes, SHA-256
`16dd61af54d97da110bd5d01eaabb834d2b656e4c9bac69874dcca4a584075ee`) are
unchanged. Nothing here changes the scientific pin, the verifier, the
completed PASS, a status or a scope. Where this file and an earlier
statement disagree, this file supersedes that statement for downstream use;
the earlier text is not rewritten.

Basis: the independent analytical, custody and code review
[#1658 comment 6278532920](https://github.com/mathorn1973/twist-j/pull/1658#issuecomment-6278532920)
(verdict ACCEPT at the proved scope, four post-run corrections required),
and row E of `notes/canon/V104-RELEASE-REVIEW.md`, which requires these
corrections as explicit errata. Each value below was re-derived on
2026-11-08 from the repository objects named.

## 1. Two-point central quotient (`RESULT.md`, PR description)

`RESULT.md` states that the two-point central difference of the quartic
witness polynomial is `157/1296`. The correct value is **175/2592**.

For the specified witness,

```text
P(t) = 251/648 + (47/1296) t + (401/3456) t^2 + (1/32) t^3 + (251/10368) t^4
P(1) = 3085/5184,   P(-1) = 265/576,
(P(1) - P(-1))/2 = 47/1296 + 1/32 = 175/2592.
```

The exact derivative `p'(0) = 47/1296` and the cubic defect `c_3 = 1/32`
(`QUARTIC_CENTRAL_DEFECT=1/32`) are unchanged. The wrong numeral is not used
by the frozen proof or by either implementation.

## 2. Parameter pairs (`RESULT.md`, PR description)

"1140 ordered parameter pairs" must read **1140 unordered parameter pairs**.
The audit evaluates `6 * binom(20,2) = 6 * 190 = 1140` unordered pairs.

## 3. Registry digest in the frozen `SOURCE.md`

The `canon/REGISTRY.tsv` row of the frozen authority table prints a
truncated 56-character digest,
`5cd008147435bf1facfe93b2e05d9d73f647ad09659aac002195890d`. This is a
transcription error. The SHA-256 of `canon/REGISTRY.tsv` at Public Canon
v103 (`canon-v103` = `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, 532811
bytes) is

```text
5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d
```

Both frozen implementations already carry this complete value in their
authority tables. The same truncated digest also appears in the frozen
`SOURCE.md` of the predecessor `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2`;
the same correction applies there.

## 4. Companion #1652 pin and head in the frozen `SOURCE.md`

The frozen `SOURCE.md` names `P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1`
(draft PR #1652) with prospective pin
`a0841a10e922bf3b3db567f30e66c51c39175fc0` and post-review head
`98ec11df0cf1b0b4238867879fa07a675a4f7822`. Neither object exists in the
repository. The correct values are:

```text
prospective pin   5e072359a029233d1c2b266c0c4bed2269752535
                  (pin_commit in probes/P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1/RUN.md on main)
post-review head  98ec11dfd25f4a7b9b890fb03b484b0c0e24313e
                  (the corrected #1652 head inspected by the review on 2026-10-19)
```

## Scope notes carried from the review (no correction required)

- The pure-gauge identity `S_le2 = A_auto((I - epsilon G_psi) x)` is an exact
  polynomial pullback; it does not by itself prove global invertibility of
  that field map.
- The integer scales `16 m D^3 Q_psi` and `80 D^2 Q_psi` are sufficient
  common denominators; no minimality is claimed.
- The 120 inherited constraint-propagation vertex checks concern the baseline
  continuity identity, not a new nonlinear propagation theorem for the
  modified Euler-Lagrange equations.
