# Execution record

The [public readback](https://github.com/mathorn1973/twist-j/issues/2019#issuecomment-6964254868) records the SHA-256 and lengths of the nine frozen inputs. The runner checked those bytes again before this command from the repository root.

```text
pin_commit: 209b57c987e028e13f046cd30e280105d12d90bc
command: python3 probes/P-H3-FUNDED-RECEIVER-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 9a0d678dfd7be69c5a05e4c26f01e711f008deaaddb6bc10a61651a5b16c0c8a
started_utc: 2026-11-17T23:38:28.494759+00:00
ended_utc: 2026-11-17T23:39:27.689042+00:00
exit_code: 0
stdout_bytes: 505792
stdout_lines: 335
stdout_sha256: f9f5bbc158978dbb89c9310479bdfb150b5a6ad9209be30be9b4f23403bc18e2
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The Linux verifier compiles the pinned four-coefficient audit using g++ -std=c++20 -O3. It checks the full M,U,H account from which Q follows, and the complete inverse of every C/B step. The census spans 328×85 = 27,880 launches, each evolved for 193 ticks, and 69,033 single-event comparisons of 65 ticks each. There were 9,867,985 checked native ticks. The original bare orbit of 622 ticks was checked separately.

For modes 0, 23, 300, 400 and 408 the separate five-coefficient Python evolution replayed all 85 launches per mode, matched every emission and all 17 integer fields of 899 events. Those five modes cover 140,460 native ticks in the Python replay, exclusive of the bare orbit and the additional detailed witness extraction. The C++ implementation uses the same Python-produced launch states, so its independence concerns evolution, accounting and event scoring.

[EXPECTED.txt](EXPECTED.txt) contains one reference line, the fixed-rule selection, 328 survey records and five full selected-mode records. Each survey record binds the entire ordered event table and complete launch list by SHA-256. A mode with no emission still has all 85 starts checked by both the preparation and the C++ input validator.

## Supplement

After the census, followup.py uses the same pinned kernel, funding code, fixed receiver and original event window to establish word identity, lifetime and duplicate witnesses. Run from the probe directory:

```sh
python3 -B followup.py . EXPECTED.txt > retention.txt
cmp retention.txt RETENTION.txt
```

This additional analysis is identified separately from the preregistered primary. It also matches all 124 native event rows of recipe 324, SHA-256 93ac2f205bbfcc8e5705a62fd7997f9fd579b4501f150d87026da96759f24916 in the registered row encoding.
