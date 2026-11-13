# Review of the original execution records

**NON-CANONICAL; L1; result-record review, not a new scientific run.**

Reviewer: A. M. Thorn / capacity-theory review lane, 2026-10-23.
Accepted scientific code pin reported by the coordinator:
`9b0406c3bf4ea2c9f8d9afe17596ea5308907713`.

Only the original stdout, stderr and run-metadata files were inspected in this review. The two scientific programs were neither executed nor imported. A separate standard-library JSON parser compared the recorded fields, with unit-name normalization only.

## Exact record hashes

| Record | SHA-256 |
|---|---|
| verify stdout | `327d81693491db6ea76aa3c7cb3edf60bea475edd4a6531f3297f4afc4e15360` |
| break stdout | `88c9702586852f4f968ce905c1f6f874d647ffb37f9b18b536e49744e0472569` |
| verify stderr | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| break stderr | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Both metadata records report exit code zero, no timeout, Python 3.12.14 and x86_64. Both stderr files are empty. The builder ends with ALL PASS; the breaker ends with a PASS summary. This is one architecture only.

## Comparison

The complete 288-key census agrees on every `(unit,n,m)` with four units, 1<=n<=12 and 2<=m<=7. Comparison included the feasibility decision, total state count, and the complete source-cycle count for every finite row. There were no missing, extra or mismatching keys.

- 276 keys are finite: 82 positive and 194 negative.
- 12 keys describe the two infinite zeta quotients, each repeated for six alphabets. These are INFINITE dispositions, not negative finite-reader results.
- The builder records explicit quotient enumeration for all 31 finite quotients through n=8, totaling 5,712,901 representatives across these separate quotients. The largest quotient has 4,873,055 states. These enumeration records agree with its determinant/cycle census; the independent overlapping comparison above agrees with the latter. This does not claim that the breaker independently enumerated all 5,712,901 representatives.

All six sufficient-onset records agree:

| Absolute modulus exponent | Alphabet | n0 | Sufficient onset |
|---|---:|---:|---:|
| 1 | 2 | 4 | 31 |
| 2 | 2 | 2 | 10 |
| 2 | 3 | 2 | 10 |
| 2 | 4 | 2 | 13 |
| 2 | 5 | 4 | 26 |
| 2 | 6 | 12 | 101 |

The breaker reports 91 successful tail-audit rows, matching the declared thirteen-horizon ranges for J, phi^-1 and J^2. The builder reports those same ranges and successful completion. Its stdout does not print each tail count, so this review does not claim a bytewise or per-value comparison of unprinted tail numbers. The onset values are conservative sufficient bounds, not least feasible horizons.

The four denominator/stride pairs agree exactly: (2,1), (5,2), (16,3), (256,6). The additional breaker-only exclusion onsets and 228 small-permutation controls are reported separately; they are not mislabeled as overlapping builder checks.

## Interpretation checks

The finite census contains the predicted binary failure for J at n=5. J admits a binary reader at n=7 while phi^-1 does not, illustrating that phase changes finite feasibility despite the shared eventual threshold. J^2 admits a seven-letter reader at n=1 and n=2, so its eventual maximum of six must not be restated as a prohibition at every finite horizon. Zeta admits one-tick readers with two through five letters and has infinite quotients at n=5 and n=10.

Different successful construction modes or multiplicities in the two outputs are not discrepancies: the contract asks for existence and valid certificates, not a common or minimal c. The analytical all-n theorem, exact selected-support preparation contract, and absence of a physical sampling interpretation remain separate from this finite audit.

**Disposition:** the inspected original records support PASS for the declared overlapping finite audit. No scientific rerun, second architecture, Canon promotion, physical occurrence law, or independent rederivation of the all-n theorem is supplied by this output review.
