# Complete lambda-six inverse and pure-J data dynamics

**Status: PASS; candidate-T analytical result with a successful exact local audit. NON-CANONICAL until a separate fold.** Action layer L1. The first formal execution of `P-J-LAMBDA6-DECODER-INTERFACE-2` completed from public pin `79c8cd3cdb7df40eedd59e12bf70832c8cbc4b2d`. Both the author and independently frozen review programs returned PASS. No scientific falsifier fired.

The independently reviewed proof establishes the complete arithmetic interface on every nonzero scalar in `O=Z[zeta5]` with algebraic norm at most 941. The local run is one x86_64 execution; required clean x86_64/aarch64 CI byte identity is a separate gate and was pending when this result was written. No two-architecture result or Canon promotion is inferred here.

## Established scope

For `lambda=1-zeta5` and `J=1+zeta5^2`, the exact datum is

`D6(alpha)=(S(alpha),S(J alpha),alpha mod lambda^6 O)`.

The implementation supplies an encoder and a total recognizer/inverse. On a valid reading it returns the original alpha, its unique representative beta in the original half-open strip `0<=v<u`, the signed integer k satisfying `alpha=J^k beta`, and the norm. It rejects malformed and nonimage readings. Zero remains outside the domain. Six canonical least-significant-first lambda digits specify the ideal residue; no approximate or componentwise-mod-five interpretation is used.

The proof covers termination before scalar representability is known, exact boundary handling, both signs of k, residue transport during normalization, and soundness/completeness of the finite strip lookup. Its decreasing integer measure is `2u+1[v>=u]`; the finite translated tests do not replace the all-integer argument.

On every syntactically valid datum, including nonimages, the exact maps

```text
T6(s0,s1,r)         = (s1,3*s1-s0,Jr)
T6_inverse(s0,s1,r) = (3*s0-s1,s0,J^-1r)
```

are mutually inverse, with the last coordinate multiplied in the ideal quotient and converted back to canonical digits. They preserve image membership and intertwine D6 with multiplication by J and J^-1. These are pure-J data dynamics, not an implementation of native U.

The residue ring has 15625 elements and characteristic 25: five times 1 is nonzero, whereas twenty-five times 1 is zero. Its additive group therefore is not isomorphic to that of `F5^6`. The six digits encode a set with carries.

## Actual finite audit

The author audit regenerated the complete original strip from all `17^4=83521` coefficient vectors. It recovered 3150 scalars and matched the inherited compact-strip SHA-256:

`6a08d7de33b4cadb615f942b37202540dd6dea0f59f2412ffb822389c7c1cdab`.

All 15625 canonical residues were checked against an independent exact inverse-multiplication-matrix ideal oracle. The complete normalized arithmetic input space contains 405 admissible trace pairs, including 260 pairs not represented by a strip scalar. Crossing every such pair with every residue gave:

| Complete normalized input audit | Observed count |
|---|---:|
| Readings checked | 6328125 |
| Exact image readings accepted | 3150 |
| Nonimage readings rejected | 6324975 |
| Translated nonimage cases rejected | 810 |

Every accepted normalized reading returned its exact scalar, the same strip representative, exponent zero and correct norm. No incompatible residue or nonrepresentable trace pair was accepted.

The remaining actual primary audit counts were:

| Audit | Observed count or fixed cases |
|---|---|
| Data-operator cases over all residues | 46875 |
| Signed strip cases | 22050 |
| Exponents for every strip scalar | -31, -7, -1, 0, 1, 7, 31 |
| Additional unit exponents | -257, 257 |
| Included/excluded boundary representatives | 110 |
| Malformed-input cases | 69 |
| Early invalid-trace cases | 1629 |
| Directly verified disjoint depth-five collision pairs | 30 |

The independent program was frozen before exposure to the author implementation. Its polynomial-ring and inverse-ideal-matrix oracle also returned PASS, with 1362903 checks: 78125 data-permutation cases, 140625 image classifications, 22050 valid translates, 32 large translates and 77 malformed cases. These coverage categories and the total check counter measure different levels of assertions; they are not claimed to sum to the same quantity. It bound the tested API to SHA-256 `6b9545e392fb452c49a056244b4823ffacbdb804acd505513bff07a9d94a08ee`.

Code independence, exposed mathematical targets, static proof review and architecture reproduction are distinct. Their custody is preserved in REVIEW-PREREG.md, REVIEW-FREEZE.json, REVIEW-STATIC.md and SUCCESSOR-REVIEW.md.

## Minimum-depth conclusion and retained census status

The analytical minimum uses the unchanged original norm bound, both original traces and the ideal-reading sequence. Equal traces imply `N(alpha-beta)<=16*941=15056`, whereas a nonzero lambda-six multiple has norm at least `5^6=15625`; hence depth six is injective on the complete norm-bounded integral domain.

The three disclosed depth-five pairs and their ten root-of-unity translates give thirty disjoint collisions in the inherited 3150-element strip. Therefore `K_5<=3150-30=3120<3125`, and every smaller positive depth is also insufficient. At depth six, `K_6=3150`. This proves both the first injective depth and the first depth with at least 3125 strip keys are exactly six, independently of the earlier computed value of K_5.

The native-label interpretation retains the registered observed-reader class, all-sheet availability, and absence of a separately supplied time. No minimum among other observation types is asserted. The earlier eight-depth census and its exact intermediate counts were exposed inputs, preserved in their original separate bundle. They were not rerun here and are not promoted by this interface result.

## Execution and disposition

The actual command was `python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-2/verify.py`. The local execution used Python 3.12.10 on Windows 11, x86_64, from `2026-10-03T23:26:18.162951+00:00` to `2026-10-03T23:26:34.136001+00:00`. The wrapper validated its frozen input manifest and ran both child programs. Exit code was 0; stderr was empty. Scientific stdout was one 1249-byte UTF-8/LF JSON line, SHA-256:

`1104009a53640c1fc226418db83d1c4c254ee7e12d69e649599e04ae06f273df`.

The wrapper verifier SHA-256 was `9e3b4af0fcfb680500fc04f7343ffe8f7f82bb24e893258523d2b2d6bd5f7625`; the validated INPUTS.sha256 file digest was `0411a673d1d514490a3745938c3a59d24f4809f5909663be08e062b48645e6b6`. RUN.md and the exact stdout records provide the execution custody. EXPECTED.txt is the actual successful stdout, not a pre-run fabricated target.

Predecessor `P-J-LAMBDA6-DECODER-INTERFACE-1` was abandoned before scientific execution because Git normalized a review-freeze metadata file after its raw-byte hash was recorded. Its identifier remains consumed. This successor preserved the scientific carrier, algorithms, test domains and thresholds while repairing byte custody under a new public pin; the predecessor packaging failure is not a scientific counterexample.

The old mod-25 decoder remains unchanged. The proven reduction is in the residue alphabet, from `5^8` to `5^6`; the full reading still contains two unbounded integer traces. This result supplies no speedup claim, finite total storage, physical acquisition or energy saving, preferred dictionary, corruption detection, native source-controlled contact, realization of U, occurrence law or higher-layer bridge.
