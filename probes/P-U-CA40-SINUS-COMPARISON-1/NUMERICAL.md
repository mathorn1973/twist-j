# First floating campaign

PUBLIC NON-CANONICAL. Conditional L1 engineering evidence, not an interval certificate.
Original text Apache-2.0. All values below derive from the preserved first campaign.

Status: COMPLETE. Frozen engineering convergence screen: **UNRESOLVED**.
Completed configurations: 4/4. Numerical runner wall time: 784.574506676 s.
No frozen waveform, scientific source, tolerance, thermal cutoff or grid changed after the public pin.

## Reproducibility and numerical integrity

Source pin: `7cb20a3a1b6b8a55fbb6f690275df8648e507289`.
The ten source/manifest files were publicly byte-read back before execution.
Platform: Debian GNU/Linux 13 (trixie), x86_64, Python 3.13.5, GNU C++ 14.2.0.
NumPy 2.5.0 was used for endpoint-array validation and comparisons.
The declared two-package, two-NUMA-node, 40-physical-core/80-logical-CPU topology was checked.
Each completed kernel used 80 explicitly bound workers and all 80 distinct CPU places.
Compiler flags: `-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`;
the kernel uses explicit AVX-512 target attributes and checks CPU support.
Executable SHA-256: `c7baaef0c3f25b595e012a661c43dc2b42eec1751f58734187c7331939ce0fd5`.
Compilation: 6.02434649318 s. Exact gate: 0.765983203426 s.
These timings are separate from the numerical campaign. No speedup over another backend is inferred.

| Configuration | Dimension | Preparation (s) | Kernel (s) | Process (s) |
| --- | ---: | ---: | ---: | ---: |
| L4-N128 | 330 | 0.207817194983 | 10.352154443 | 10.6329550464 |
| L6-N128 | 1716 | 0.20807794854 | 115.307376491 | 115.727409542 |
| L6-N256 | 1716 | 0.384249569848 | 189.040671906 | 189.638748826 |
| L6-N512 | 1716 | 0.728245195001 | 466.71657899 | 467.677864136 |

Largest scalar dense/SIMD, adjoint, Hermiticity, single-mode or zero fixture error: 8.35553472161e-17.
Independent Python linear endpoint errors: alpha 9.32603861715e-16, phase 5.3290705182e-15 rad.
All completed runs passed these frozen integrity tolerances. This does not certify nonlinear time evolution.

## Thermal input and pair coherences

All seven modes use nbar=1/20. Enumerating total initial occupation <=3 retains 120 states
with their original unequal, unnormalized weights. The exact omitted mass is
`680046581/794280046581`.
Its floating display is 0.000856179862415; the thermal-only pair-distance radius is 0.000428089931207.
This initial tail is independent of dynamic projection and RK4 errors.

The following centers are |Gamma_S,ret-Gamma_L,full|/2. The different linear frames
and Weyl phase are restored before taking nonlinear branch overlaps. No individual
branch phase is fitted, and no discarded thermal mass is replaced by zero as a physical assumption.

| Configuration | Sign | Branch pair | Distance center |
| --- | ---: | --- | ---: |
| L4-N128 | +1 | (4, 3), (4, 4) | 0.0437166861391 |
| L4-N128 | +1 | (4, 3), (1, 1) | 0.0440660950755 |
| L4-N128 | +1 | (4, 4), (1, 1) | 0.000503854639576 |
| L4-N128 | -1 | (4, 3), (4, 4) | 0.0247651803169 |
| L4-N128 | -1 | (4, 3), (1, 1) | 0.0249280590658 |
| L4-N128 | -1 | (4, 4), (1, 1) | 0.000350150239546 |
| L6-N128 | +1 | (4, 3), (4, 4) | 0.0437177881674 |
| L6-N128 | +1 | (4, 3), (1, 1) | 0.0440673142681 |
| L6-N128 | +1 | (4, 4), (1, 1) | 0.000503433548848 |
| L6-N128 | -1 | (4, 3), (4, 4) | 0.0247664738508 |
| L6-N128 | -1 | (4, 3), (1, 1) | 0.0249293688044 |
| L6-N128 | -1 | (4, 4), (1, 1) | 0.000349787960486 |
| L6-N256 | +1 | (4, 3), (4, 4) | 0.0437232058276 |
| L6-N256 | +1 | (4, 3), (1, 1) | 0.0440731183254 |
| L6-N256 | +1 | (4, 4), (1, 1) | 0.000612093040785 |
| L6-N256 | -1 | (4, 3), (4, 4) | 0.0247699644299 |
| L6-N256 | -1 | (4, 3), (1, 1) | 0.0249328688457 |
| L6-N256 | -1 | (4, 4), (1, 1) | 0.000411137687547 |
| L6-N512 | +1 | (4, 3), (4, 4) | 0.043723805459 |
| L6-N512 | +1 | (4, 3), (1, 1) | 0.0440737305915 |
| L6-N512 | +1 | (4, 4), (1, 1) | 0.000616105614882 |
| L6-N512 | -1 | (4, 3), (4, 4) | 0.0247702717634 |
| L6-N512 | -1 | (4, 3), (1, 1) | 0.02493317606 |
| L6-N512 | -1 | (4, 4), (1, 1) | 0.000413392321426 |

Thermal-only intervals at the last completed configuration (L6-N512):

| Sign | Branch pair | Thermal-only lower | Thermal-only upper |
| ---: | --- | ---: | ---: |
| +1 | (4, 3), (4, 4) | 0.0432957155278 | 0.0441518953903 |
| +1 | (4, 3), (1, 1) | 0.0436456406602 | 0.0445018205227 |
| +1 | (4, 4), (1, 1) | 0.000188015683675 | 0.00104419554609 |
| -1 | (4, 3), (4, 4) | 0.0243421818322 | 0.0251983616946 |
| -1 | (4, 3), (1, 1) | 0.0245050861288 | 0.0253612659912 |
| -1 | (4, 4), (1, 1) | 0 | 0.000841482252633 |

**These intervals are not total-error bounds.** They allow only the omitted initial thermal mass.
They leave finite-basis, integration and floating errors unbounded rigorously. The quantities are
coherent-input trace-distance estimates, not average gate infidelity, hardware error,
or a guarantee over all 25 active branches.

## Cutoff, integration and projection diagnostics

Endpoint-vector differences use the full complex vectors and unnormalized thermal weights,
with zero embedding of L4 into L6 and no phase alignment. Their formula is frozen in PREREG.md.

| Comparison | Case 0 | Case 1 | Case 2 | Case 3 | Case 4 | Case 5 | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| cutoff | 0.000850199075992 | 0.00126454374737 | 0.00126454374737 | 0.000417141856341 | 0.000497509623556 | 0.000497509623556 | 0.00126454374737 |
| time_coarse | 0.000142814815921 | 0.000167962994965 | 0.000167962994968 | 8.05538413672e-05 | 8.95447787166e-05 | 8.95447787179e-05 | 0.000167962994968 |
| time_fine | 8.77547844527e-06 | 1.04108254223e-05 | 1.0410825387e-05 | 4.88828469238e-06 | 5.56366722076e-06 | 5.56366719913e-06 | 1.04108254223e-05 |

Case order is +[(4,3),(4,4),(1,1)], then -[(4,3),(4,4),(1,1)].
The cutoff screen compares L4/128 to L6/128; coarse and fine time screens compare
L6/128 to L6/256 and L6/256 to L6/512. None is itself a rigorous discretization bound.

| Configuration | Maximum norm drift | Maximum top-shell weight | Maximum sampled projection integral |
| --- | ---: | ---: | ---: |
| L4-N128 | 0.000711408063902 | 0.124208298549 | 1.58448634923 |
| L6-N128 | 0.000990428921607 | 0.00139008200839 | 0.0616494086471 |
| L6-N256 | 3.64600726721e-05 | 0.00138840038527 | 0.0615858502077 |
| L6-N512 | 1.18802905735e-06 | 0.00138776891037 | 0.0615827017607 |

The norm screen uses the maximum over all completed configurations, including coarse steps;
the other two frozen screens require cutoff and fine-step vector differences <=1e-4.
We preserve the resulting screen verdict rather than changing it after seeing refinement.
A large top-shell weight is a diagnostic for an individual retained initial state, not its
thermal probability. Projection integrals are RMS combinations of per-column sampled
triangle-majorant integrals at RK stage approximations. They are not certified all-time bounds.
The kernel retains the minimum raw displacement norm deficit; tolerated roundoff clamping
does not make the residual calculation interval arithmetic.

Last completed configuration, L6-N512, branch detail:

| Case | Retained overlap Re | Im | Norm drift | Top shell | Sampled integral | Minimum raw deficit |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0.870992841668 | 0.478854399548 | 1.01460191981e-06 | 0.000588891664501 | 0.0348067643697 | -6.88338275268e-15 |
| 1 | 0.906908741424 | 0.399032736319 | 1.18802905225e-06 | 0.00138776891037 | 0.0615827017337 | -5.77315972805e-15 |
| 2 | 0.906908741424 | 0.399032736319 | 1.18802905735e-06 | 0.00138776891037 | 0.0615827017607 | -5.77315972805e-15 |
| 3 | 0.964487774122 | 0.25414751837 | 5.71944776873e-07 | 0.000172733730982 | 0.0146868796747 | -5.99520433298e-15 |
| 4 | 0.975052886069 | 0.205524947682 | 6.37867948683e-07 | 0.000289295569156 | 0.0225406975231 | -7.32747196253e-15 |
| 5 | 0.975052886069 | 0.205524947682 | 6.37867964004e-07 | 0.000289295569156 | 0.022540697603 | -7.32747196253e-15 |

The retained same-branch overlap is a specified-purification echo. It is not the Uhlmann
fidelity of the mixed bus state or a numerical measurement of protected-source coherence.

## Custody

The first exact stdout is preserved in EXPECTED.txt and RUN.md. The numerical records retain
original stdout/stderr, all configuration receipts, progress, source/input/binary hashes,
basis metadata, independent linear fixtures and full complex endpoints. No run was replaced.
Compact evidence archive: 76136 bytes, SHA-256 `b1816c6d7bc9e7b8dc39fdd41571e2dda5c298168f391f3003ef5dc513609429`.
This compact archive contains text/JSON records and a complete evidence inventory; endpoint
binaries are retained separately, not represented as included in that archive. Their receipts:

| Endpoint artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| numerical/L4-N128/states/endpoints.bin | 3801600 | `b5d96117e076aa60f7235e2d07abb015fb9ea70fa61e8c53ea2a47909b148f59` |
| numerical/L6-N128/states/endpoints.bin | 19768320 | `e0e6ecbdf0119c6ddfb86ad6893f9c48bb4c085bf935aeded333d1122e9b6a8e` |
| numerical/L6-N256/states/endpoints.bin | 19768320 | `5333db0748a5f47d9f87c00ecdcc7e68d0b1db97706420e62adb351eebcce6e5` |
| numerical/L6-N512/states/endpoints.bin | 19768320 | `680aa5c681389c27ee588f2ef8ef0a1038c7bbbaae00809a9c317c8371ee1b70` |

Public source and the fixed input are sufficient to reproduce the finite calculation.
Private infrastructure names, raw progress streams and binary payloads are not committed.
The source/control physical assumptions and unknown-source/full-informative-contact boundary
remain exactly those in DERIVATION.md and PREREG.md.
