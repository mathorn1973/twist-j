# Authority and validation record

**NON-CANONICAL / L1 / conditional analytical candidate-T.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: #1803. Date: 2026-10-27.

## Public basis

STATUS.md was read first from the GitHub connector. Public main remains
`892a0b11089d34e241e1eb76d2c03247022d18e6`, identical to the peeled
`canon-v105` tag. Declared content commit
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc` is an ancestor.
POLICY.md, AGENTS.md, canon/CORE.md and canon/FRONTIER.md were read at this
same basis. All five normative SHA-256 values match canon/SHA256SUMS.
canon/CANON.md has 1295029 bytes and SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

Public main workflow 40082129555 has successful x86_64, aarch64 and
aggregate check jobs. Tag publication 40084587620 and release publication
40087227867 succeeded; canon-v105 is the published immutable release.
These establish the basis, not mathematical acceptance of this candidate.

The startup collision check enumerated 321 actual remote heads with
git ls-remote --heads origin, searched current notes/probes/registry and
current issues/PRs, and found no duplicate of this scoped item. The broader
#1802 synthesis and #1799/#1800/#1801 spatial/triad work retain their owners.
This reservation was then published as #1803 before note files were written.

## Exact comparison sources

- #1793: `6f8e8e93a3b459695262c50c2ccbd120cdeb7e99`,
  notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/PROOF.md, SHA-256
  `e1133dbf1fb8226390c2b5eccbc3681fe56368d2ba23c3764248b9a5a9f0d7fd`.
  Its public mathematical review is COMMENTED with PASS, while the note
  remains NON-CANONICAL. The common minus in V_g a=-K_g a is retained here.
- #1768: `811daddc3b2f085ee5bc6f50261ac95a4c11fe44`,
  notes/C-SPECTRAL-ENERGY-FINITE-RECORD-N/ENERGY.md and FINITE_BATTERY.md.
- #1795: `e4d165c5c5471ea5746013f7f8f5c394512f9884`,
  notes/C-DIRAC-FINITE-ROTOR-CLOCK-N/PROOF.md and README.md. This is a
  different target; no spatial or repetition theorem is imported.

The source files were read directly at the stated GitHub revisions. Old
attached internal Canons are not authority or evidence for this package.

## Validation distinction

All new mathematical statements are proof-only. No scientific executable,
numerical experiment, finite gate enumeration or computation-grade
promotion is supplied. The separate assistant contexts in REVIEW.md are
same-session exposed-text analytical checks, not external independent
acceptance and not a blind breaker run.

Administrative validation uses the unchanged repository tools and exact
normative checksum file. Local results before publication:

```text
python3 tools/check_policy.py: POLICY PASS
python3 tools/check_canon.py: CANON PASS v105 claims=577
python3 tools/check_ledger.py: LEDGER PASS
python3 tools/check_gate_contract.py: GATE CONTRACT PASS gates=26
python3 -m unittest discover -s tools -p 'test_*.py': 210 tests, OK
sha256sum -c canon/SHA256SUMS: all five files OK
git diff --check: no whitespace errors
git diff BASE -- canon/: empty
```

The unittest stdout includes deliberately exercised failure messages from
its fixtures; the complete suite exits zero and reports OK. Those messages
are not scientific failures of this candidate. The final committed diff
also goes through the repository's changed-path verifier/reproduction
runners before the draft is opened. Public PR CI and mathematical review
remain separate gates; neither is claimed in this pre-publication record.

## Publication

Only the eight Markdown files in this candidate directory are included.
The commit uses A. M. Thorn <thorn@twistj.com> for both author and committer.
The reviewed commit is transported by Git and published on its own notes
branch. The draft PR requests mathematical review of the note package.
It does not change Canon, registry, frontier, probes, gates or workflows,
and requests no merge, activation or release.
