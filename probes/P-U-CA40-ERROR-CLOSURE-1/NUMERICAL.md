# First numerical error-closure attempt

PUBLIC NON-CANONICAL. Conditional L1 computational record. Original text Apache-2.0.

Status: NOT_CERTIFIED. Completed numerical configurations: 0.
The exact supporting gate passed. Neither angle has a completed numerical
error certificate from this attempt.

## Immutable inputs and execution

Source pin: `3440928c77239bd26907a52810db7ec611f134d8`.
All twelve source/manifest files were publicly read back before execution.
Input SHA256: `ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Serialized exact-decimal input: 3918 bytes, SHA256
`720f167680bbb51549165a10ba04ce9688de43cc67bb4087cd4ce5be20ebb471`.
No pulse, scientific source, tolerance, initial thermal cutoff or numerical
configuration changed after the pin. There was one child launch and no retry.

Recorded platform: Debian GNU/Linux 13 (trixie), x86_64; Python 3.13.5,
NumPy 2.5.0; g++ (Debian 14.2.0-19) 14.2.0; libmpfr6 4.2.2-1,
libgmp10 2:6.3.0+dfsg-3. Development headers were extracted privately from
libmpfr-dev 4.2.2-1 and libgmp-dev 2:6.3.0+dfsg-3 without a system install.
Their package SHA256 values are respectively
`43cbe73a48cce65232ad5d4219a67dfdd0974f45aa88d381ae051d64052b996a`
and `68f392cc03f896ecc3764eb4844d2a898ff016f47dda160465f152f811152b81`.

Compilation used `-O3 -std=c++20 -fopenmp -ffp-contract=off
-fno-fast-math -fno-tree-vectorize`, the two extracted include directories,
`kernel.cpp validated_model.cpp -l:libmpfr.so.6 -l:libgmp.so.10` and an
explicit output path. The exact private command is retained in the archive.
The code uses explicit AVX-512 target attributes and directed instructions.
Binary: 270384 bytes, SHA256
`cb883d419a76bd063157ad82924121b82debe50dd3bf1dddb3724d25c117ed78`.
Compilation took 11.58361984975636 s, exit zero, empty stdout/stderr.
The exact gate took 0.3155597001314163 s; see RUN.md for its byte receipt.
These observed timings are separate from the numerical campaign.

## Manual resource stop

The numerical runner started at 2026-10-11T11:35:01.726825+00:00.
Only L8/G10/N512 was launched: 6435 propagated basis states and 19448 guard
states, retaining all seven modes and 120 initial thermal columns per case.
The declared 40-physical-core/80-logical-CPU, two-package topology passed
the launch checks. All 80 explicit CPU places and OpenMP worker settings
were requested. A read-only process observation measured approximately
79.965 CPU-seconds per wall second with 80 resident threads. The final
per-worker CPU/place report was not produced, so no completed mapping audit
is claimed.

Coefficient preparation, basis construction and startup fixtures had
returned: the program had written basis.json and opened progress.jsonl.
No fixture error or numeric fixture summary was emitted. At the manual
stop, more than 18 minutes after the scan was observed to have started,
no worker had reached its first 512-cell reporting point.
The same fixed loops recur at every active cell; the two longest branches
have 16384 cells. A steady-rate extrapolation therefore exceeded 9.6 hours
for that first wave, before the remaining tasks. This is a resource-planning
estimate, not a mathematical runtime lower bound or a numerical error bound.

The coordinator explicitly requested SIGTERM of its owned numerical runner
at 2026-10-11T12:00:42.242583+00:00 to avoid spending the rest of the budget
on an impractical implementation. This was an early manual resource stop,
**not expiry of the preregistered 28800-second ceiling** and not a
preregistered scientific stopping criterion. The runner terminated its
kernel process group, preserved the interruption, and returned exit code 2
with `NOT_CERTIFIED` and zero completed configurations. All three processes
were subsequently confirmed absent. No result was used to retune a pulse,
change a precision threshold, repair this pin or start a replacement run
under this identifier.

| Attempt | Saved child status | Child wall seconds | Source/input/binary custody |
| --- | --- | ---: | --- |
| L8/G10/N512 | STARTED, then interrupted | 1540.7681361753494 | PASS after child |

The interrupted code path preserves the child's original `STARTED` label
and lacks a child exit-code field. This does not mean the process is still
running. The runner's final result and the separate stop receipt establish
the interruption. Numerical runner wall time was 1540.8851180039346 s
(25 min 40.885 s); the outer capture measured 1541.000443533063 s.
The runner's stderr and both child stdout/stderr were empty. The other
three configurations were never launched.

## What is and is not available

No final endpoint vectors, branch error totals, pair coherences, six-pair
intervals or numerical radius decomposition were produced. The empty
progress file supplies no partial error bound. Those absent quantities are
unknown, not zero. The runtime's final MPFR coefficient summary, legacy eta
discrepancy and numeric fixture discrepancies are likewise unavailable.
No independent numerical replication is claimed; any architecture CI
replays only the small exact verifier.

The exact initial thermal omission remains
`680046581/794280046581`; its pair-distance radius is half that mass,
about 0.000428089931207. This is only the thermal contribution. It does
not close the missing dynamic projection, integration, roundoff, endpoint
jump or final overlap account for either angle.

The model treats the unchanged decimal inputs as exact rational parameters
and defines eta coherently from kappa and k*x. The frozen design would
report the mismatch from the legacy rounded eta table; this interrupted
attempt supplies no measured mismatch value. Supplied mode constants are
not certified apparatus measurements.

## Evidence and scope

The compact archive contains 28 first-attempt records and a manifest,
including the exact stdout, compilation records, launch, empty child
outputs, basis, empty progress, source/input pins, manual stop and final
interruption records. There are zero binary endpoint files.
Archive: 31821 bytes, SHA256
`1b21cf0fefaaaa0a7d124051ab56dec33e9156e6e59eb7ad276f7f52db28d5e3`.
The saved export SHA256 is
`287d2cc70ae2c015ddccea79727806305d46b9deb38e0ba2fb90b40eae0b74c5`.
The archive was read back and checked; raw private operational records
are not added to the public repository.

The proposed online certificate shares a process with the candidate and
would retain endpoint states and per-column totals, but not full quintic
trajectories. This attempt produced neither a completed certificate nor
those final states. Same-session static review and custody checks are not
blinded replication.

Five protected electronic registers and their external-reference marginal
remain unchanged only under the inherited exact-darkness premise. No ion
experiment, finite-carrier validation, heating/scattering model, radial
motion, complete work reservoir, physical contact admission, all-input
channel guarantee or Canon promotion follows from this record.
