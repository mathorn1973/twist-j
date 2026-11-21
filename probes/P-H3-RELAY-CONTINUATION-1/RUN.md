# Execution record for the rank-43 continuation

The [public registration](https://github.com/mathorn1973/twist-j/issues/2054) disclosed the exploratory counts before the formal runs. The [verifier commit](https://github.com/mathorn1973/twist-j/commit/050a9be48757348fd57021bcc68ab3b9f9fcaf3c) fixed the four inputs. Their Git blob IDs matched the public tree before formal execution. The driver's SHA-256 checks bind the original launch family, source kernel, and published prefix transcript.

The main revision at registration is [68812464c5566613b1000110e556968c9775fa95](https://github.com/mathorn1973/twist-j/commit/68812464c5566613b1000110e556968c9775fa95), the direct parent of the verifier pin. The main revision printed in the frozen PREREG.md has one extra trailing `e`. The calculation used the parent recorded by Git.

## Formal run

```text
pin_commit: 050a9be48757348fd57021bcc68ab3b9f9fcaf3c
command: python3 probes/P-H3-RELAY-CONTINUATION-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: af031b96bc46851d19eb2ae907e02f77f68d063ccf204068690a10872532b018
started_utc: 2026-11-21T15:19:31Z
ended_utc: 2026-11-21T15:31:17Z
exit_code: 0
stdout_bytes: 1539
stdout_lines: 8
stdout_sha256: 198ed32b967d202c0b729bc1c03e4de6e6ecbc3810b2709ec7880dfdd49cc1f3
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The x86_64 run used g++ (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0. EXPECTED.txt holds its stdout byte for byte. The last of the eight records explicitly reports `retrospective_confirmation` as `true`.

| Frozen input | SHA-256 |
| --- | --- |
| continuation.cpp | `ed5ebd3db63806b843d3f732bd870c63e1d4a6bbe279ac36d82377df76201636` |
| dynamics.hpp | `c82044fef60c4a822299e9e2ad6a676e75c51942d3780cb92fad8e19f29eae37` |
| PREREG.md | `dc4430f02b436a48d030be5de24430014cc7e9b6c199e65669767a69f72de16a` |
| verify.py | `af031b96bc46851d19eb2ae907e02f77f68d063ccf204068690a10872532b018` |

## Architecture reproduction

The result commit includes this exact transcript for replay on x86_64 and aarch64. Each architecture must reproduce it byte for byte. The result PR linked from [issue #2054](https://github.com/mathorn1973/twist-j/issues/2054) records the architecture checks against the result commit.

## Coverage and arithmetic

The verifier regenerated the rank-43 launch and advanced the complete 32-cell lattice from tick 1 through tick 1,073,741,824. The public prefix at tick 67,108,864 is an interior control. The repeated-writer history carries across it. For each tile the implementation reuses a computed transition only after an exact comparison of all 16 incoming rail values. Each tick preserves the ordering of contacts C and local operations B.

The verifier checked the fixed historical B2, including both material changes at cell 3, and audited transfer accounting. The Python five-coordinate kernel checked the fixed B2 operations and their inverses, the two contacts on the fixed path, and the final conserved account. The field digest covers all 512 integer coefficients at the ceiling. Event populations and the three matched-pair totals are in the [exact transcript](EXPECTED.txt).
