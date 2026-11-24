# First pinned execution

PUBLIC / NON-CANONICAL / L1. Claim #1616.

pin_commit: 599f6407af7718ae66b87ec3117818663a309876
verifier_sha256: 74057db59047da2faaec0b6067c7b5c45dab44a104e5eef7c857e74e5fc3f36b
command: python3 probes/P-NATIVE-TWO-CELL-WORK-ADMISSION-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_sha256: 7e5a801e5dd480d65d4788058b5018913aec331fc1c0c0db59dc4b6838a56d39
stdout_bytes: 779
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The first scientific execution occurred after public pin and byte readback
of all five frozen files. Runtime was 1.02 seconds under the declared
120-second limit. EXPECTED.txt is the exact first stdout, not a predicted
or edited transcript. No failed run or code revision preceded this run.

The proof and finite witnesses were analytically known before pinning;
this is an exposed audit, not blind discovery. The original fixed-reader
proposal is rejected by its exact witness even though the verifier exits0.

Frozen custody (all unchanged from the pin):

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 11096 | c83ba17f99fbfe30ea358aae581664000b5ff3001d0cdcf345d85a8749d459d1 |
| PROOF.md | 17885 | ca57d0b465aeb4b6ecb7689a68607fa8ba965704d058b2d5e8d8a225bce772ad |
| README.md | 2007 | 9f5c43b8c5315c3905bb79eb7c7890ea634ea3ab2c6172b2f7401c08483525ac |
| SOURCES.tsv | 3984 | c57cbcbe6397908f7b2ae6b63b11d77f1c81bf3531383d58c46c3224923b58ac |
| verify.py | 18081 | 74057db59047da2faaec0b6067c7b5c45dab44a104e5eef7c857e74e5fc3f36b |

This record describes the local x86_64 leg only. Required GitHub Actions
replays must execute the final PR head on both x86_64 and aarch64, compare
this same verifier hash and EXPECTED.txt, and pass the aggregate check.
Their final run IDs and public readback belong to the PR handoff; none is
asserted successful in advance. Cross-architecture replay is computational
reproduction, not external independent mathematical or physical validation.
