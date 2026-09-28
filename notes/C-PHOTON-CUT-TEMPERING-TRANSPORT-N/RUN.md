# First frozen invocation

**PUBLIC / NON-CANONICAL. Engineering outcome: FAIL_IMPLEMENTATION_ANALYZER_TESTS.**

Pin: `42efd804047ab89aa80e79d37276366d5cfa8596`. All seven files were publicly
read back before invocation; issue #1261 records hashes and readback. The
checkout was clean at this exact pin. No source changed after the pin.

Platform: Linux aarch64; Python 3.12.3; compiler
`g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0`.
Compilation: `g++ -std=c++17 -O3 -Wall -Wextra -pedantic sample.cpp -o BINARY`.
Binary SHA-256: `538cd406bb2ed8c5d22d70cad719d0dc6b9684e80b76318967ddafb8ee025c35`.
The neutral command is `python3 run_pilot.py BINARY OUT`, from the pinned
notes package; OUT was a new directory. A detached shell captured the
controller return separately. Its exit code was 1 and stderr was empty.

Start UTC: 2026-09-28T07:14:58.403420+00:00.
Finish UTC: 2026-09-28T07:15:01.208181+00:00.

| Invocation | Exit | Seconds | stdout bytes | stderr bytes |
|---|---:|---:|---:|---:|
| sampler --audit | 0 | 0.065 | 59 | 0 |
| test_analyze.py | 1 | 2.739 | 0 | 3130 |

The sampler audit stdout equals the predeclared text and has SHA-256
`ca77c2a869d00235f493d8923abd08c64af61ac689c43eff1489023ae88840fc`.
The fixture stderr has SHA-256
`5e3084d5e785f2830dad9f0562217bb42269929b7536f41bbd86feea2d5f91f2`.
Empty files have the usual SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The controller stopped at its declared fixture gate. No production chain
was launched, and the production analyzer was not invoked. Consequently
there are no chain tables, analysis.json or analysis_execution.json. No
return code for a nonexistent analyzer invocation is inferred. The eight
actual ENGINEERING files are preserved; SHA256SUMS binds the other seven.
The stderr traceback contains only the neutral temporary execution path,
not a private hostname or credential. No program was rerun.

Frozen source hashes:

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 10642 | `15f07eaa87ea1976e844d4986ba0f15f5becb0beca1a00c784bc531d6617abef` |
| PROOF.md | 15033 | `f6ca22bb038bb1f47c98acf6c1011a703178f1b8414fe5e9731b1a1aa6ecad55` |
| REVIEW.md | 7220 | `1b0a43a4ed38c1dcd713c8200b3e904e2a94813c72057bbae95dc6706bb09d7f` |
| sample.cpp | 32754 | `f629b60e71079b8e14623a1cadd9b7aaac303fb72e859679bba7a82eb08f43a3` |
| analyze.py | 27438 | `02d39902b3ed93c02c8e22de6e977e7bc5955c1166b364da622813182cacbf83` |
| test_analyze.py | 12660 | `f2df50713d330eb60884feac6f4778965e37e84c9bd789a136163958eb2b7ec0` |
| run_pilot.py | 5205 | `3dbe211fdf85a221f6900d6a7b20f17bcfb4e1ca39633410f242ad86d8e89251` |

The identifier is consumed. Any correction requires its own successor and
prospective pin; this record does not authorize a retry of this source.
