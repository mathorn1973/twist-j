# Receiver audit execution record

**NON-CANONICAL / L1. Actual bounded candidate-C evidence; independent acceptance pending.**

The prospective source pin is
`262fa528968145ec8f501c8193aab946896997f6`.
The verifier is 17,948 bytes with SHA-256
`39aa493ee1a21e9a94d7decad3b20ad8a6f4311dcb87ea33a96169688dfb916f`.
All six new source/manifest files were read back from GitHub at that pin
and matched their local Git blobs before first scientific execution.
RECEIVER-SHA256SUMS binds the five scientific inputs. The two predecessor
source manifests remain unchanged.

The executable source path was passed absolutely to Python; a portable
equivalent command from this note directory is:

    python3 -I -B verify_receiver.py

The original first receipt names the repository-relative source path.
Its process working directory was this note directory. Both launchers
fixed PYTHONHASHSEED=0, LC_ALL=C.UTF-8 and TZ=UTC, with a 300-second
subprocess limit and RLIMIT_AS=1,073,741,824 bytes.

| Lane | Environment | Started UTC | Elapsed seconds |
|---|---|---|---:|
| First execution | Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12 | 2026-11-07T08:58:29.149120+00:00 | 0.8511417649999999 |
| Clean public-pin reproduction | Debian GNU/Linux 12, aarch64, Python 3.11.2 | 2026-11-07T08:59:01.703975+00:00 | 2.4948031539970543 |

Both exited zero, without timeout, with empty stderr and 184,018 assertions
PASS. The second lane cloned the public branch, detached the exact pin,
checked clean Git state, and verified all three scientific source manifests
before running.

The exact stdout is 626 bytes, including its final newline. SHA-256:

    a13b76b5dd5418b1a252914a19c43eac5ce71093fd87cc68230417fa884fabf3

Both outputs were retrieved and compared byte for byte. Empty stderr
has SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
RECEIVER-EXPECTED.txt contains the actual first output; RECEIVER-RUNS.json
retains the neutral execution metadata.

No assertion, input, threshold, resource limit or source changed after the
pin. Only AST parsing and static review occurred before the pin. There
was no failed or discarded scientific attempt. The verifier does not
import or rerun the previous field verifiers and does not computationally
prove the universal spectral or no-dictionary-selection theorems.

Repository CI is separate from this notes audit. A second architecture
reproduces the authored verifier; it does not constitute independent
authorship or independent scientific acceptance.
