# Execution record

The pinned GitHub copies of PREREG.md, kernel.py, verify.py, period.cpp and sweep.py were checked against the local Git blobs. Their lengths and SHA-256 values are recorded in the [public readback](https://github.com/mathorn1973/twist-j/issues/2013#issuecomment-6962827239). The Linux runner verified the input bytes again before running the new fixtures in a clean checkout of the pin.

```text
pin_commit: 769787e8c5046595e43e5b8307b7b28673927587
command: python3 probes/P-H3-HEAD-PULSE-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: bf35d8eb8c6094861ae55ae940a4047105ce2806b9702c0ff528192450fbf026
started_utc: 2026-11-17T22:27:22.995229+00:00
ended_utc: 2026-11-17T22:27:28.932169+00:00
exit_code: 0
stdout_bytes: 89687
stdout_lines: 6
stdout_sha256: f36440360bc51dec34b7637133d689f55ed6f13a1594b3e6513d0768ea801a46
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

[EXPECTED.txt](EXPECTED.txt) contains the five fixture records followed by the bare trace digest. The native evolution and inverse are checked at every tick in 425 fresh trials of 24 ticks and 15 streams of 3110 ticks. The four-coefficient C++ implementation independently uses the same initial configurations.

## C++ supplement

From the probe directory, with a new output directory:

```sh
g++ -std=c++20 -O3 period.cpp -o period
python3 sweep.py ./period /tmp/head-pulse-runs --jobs 4
```

The sweep has 425 short and 181 long cases. Each individual normalized LF stdout is bound by the digest in its [coverage row](COVERAGE.txt). [ALIASES.txt](ALIASES.txt) contains the union of word-class overlaps found anywhere in these runs. In this latter file a held cut uses index 2t for C and 2t+1 for B. A listed cross-start witness can use different ages. The primary transcript scores same-age, same-stage and same-bit witnesses separately.

| Platform | Compiler | Driver | Cases | Coverage bytes / SHA-256 | Aliases bytes / SHA-256 |
| --- | --- | --- | ---: | --- | --- |
| Linux x86_64 | GCC 11.4.0 | Python 3.10.12 | 606 | 94946 / 490a3a8a6420268ef8b425c4b4361e0b923ab3a137cc63e7808b201ec4b35954 | 612 / 8e23df1d1fcf9f160189ee881480d42dbc437f12fdaae31b45fce4b80204129f |
| macOS arm64 | Apple Clang 21.0.0 | Python 3.9.6 | 606 | 94946 / 490a3a8a6420268ef8b425c4b4361e0b923ab3a137cc63e7808b201ec4b35954 | 612 / 8e23df1d1fcf9f160189ee881480d42dbc437f12fdaae31b45fce4b80204129f |

Both sweeps exited 0 with empty stderr. The exact per-run digests agree across architectures for all 606 inputs.
