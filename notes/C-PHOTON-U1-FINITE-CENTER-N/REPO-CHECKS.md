# Repository checks and publication review

**PUBLIC-source, NON-CANONICAL.** A. M. Thorn, 2026-10-23. Apache-2.0.

The package changes one owned note only. Its authority basis remains
`e6240e2689bb22aab5f02bad90b75d3692bb96d9`, freshly confirmed as public
main after the audit. The source-pin scientific programs retain their
original SHA-256 values. The only changed pinned document is the expressly
identified coverage clarification in MEASUREMENT.md; first outputs remain
unchanged.

Local repository checks completed successfully:

| Command | Result |
|---|---|
| `python3 tools/check_policy.py` | POLICY PASS |
| `python3 -m unittest discover -s tools -p 'test_*.py'` | 210 tests, OK |
| `python3 tools/check_canon.py` | CANON PASS, v104, 576 claims |
| `python3 tools/check_ledger.py` | LEDGER PASS |
| `python3 tools/check_gate_contract.py` | GATE CONTRACT PASS |
| `python3 tools/check_verifier.py --base e6240e2689bb22aab5f02bad90b75d3692bb96d9` | VERIFY NOT APPLICABLE |
| `python3 tools/check_reproduce.py --base e6240e2689bb22aab5f02bad90b75d3692bb96d9` | REPRODUCE NOT APPLICABLE |
| `git diff --check` | No whitespace errors |

The verifier/reproduction results are inapplicability, not scientific
replays. The tool unit tests intentionally exercise failure branches and
print their test fixtures' FAIL lines; the complete suite exits zero.

Manual publication review covered the note's formulas, original scripts,
captured deterministic outputs, metadata and source attribution. It found
no credentials, private paths or hostnames, private transcripts, binary
artifacts or unreviewed third-party content. Runtime metadata use neutral
platform fields. All files are below the policy size limit. The scientific
scripts use the Python standard library and perform no network, shell,
credential or external-service operations.

Written argument and code review are in POSTPIN_REVIEW.md and
SAMPLER_REVIEW.md, with authorship and independence limits explicit. The
remaining production-qualification tests and all phase obligations stay
open. Public PR checks are read back on the final head separately; no
ordinary notes check is represented as a scientific two-architecture gate.
