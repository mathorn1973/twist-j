# Waveform-derived source audit: first numerical result

PUBLIC — NON-CANONICAL. Conditional theoretical/numerical result;
no ion experiment or physical apparatus certification.

The first frozen campaign returned `MODEL_WAVEFORM_CHECK` on 2026-10-10.
Both nominal auxiliary gates met their preregistered numerical requirements.
The global-echo negative control strongly disturbed the source, and the
frozen hidden-D perturbation also produced a nonzero source witness.
The stress cases were reported without redesigning the waveform.

The immutable source pin is
[`1e078f6281b8f9ce813b6f08200d9caedf1bac14`](https://github.com/mathorn1973/twist-j/tree/1e078f6281b8f9ce813b6f08200d9caedf1bac14/probes/P-U-CA40-WAVEFORM-SOURCE-1).
The equations, conventions and fixed thresholds are in [DERIVATION.md](DERIVATION.md),
[MODEL-INTERFACE.md](MODEL-INTERFACE.md) and [PREREG.md](PREREG.md).
This result does not modify any pinned source or threshold.

## Model and constructed pulses

Seven equal-mass ions use the declared one-dimensional Coulomb equilibrium,
seven axial harmonic modes, axial frequency 1 MHz, beatnote 1.02 MHz,
mass `6.6421562664e-26 kg`, and axial wavevector `2*pi/(397 nm)`.
Complex eta includes `exp(i Delta_k x_i)`; optical spatial phases are not
silently compensated. Every mode starts with thermal occupation 0.05.
These are model assumptions, not measured trap parameters.

Equilibrium positions in micrometres, rounded for display:

```text
[-10.0274328286006, -6.28416901309405, -3.05528743758571,
  0, 3.05528743758571, 6.28416901309405, 10.0274328286006]
```

| Mode | Frequency omega/(2*pi), MHz |
|---:|---:|
| 1 | 1.000000000000000 |
| 2 | 1.732050807568877 |
| 3 | 2.414388068731490 |
| 4 | 3.060842041247716 |
| 5 | 3.680697588590751 |
| 6 | 4.280253131107049 |
| 7 | 4.863725979908670 |

Each loop has 16 real, piecewise-constant segments of 6.25 microseconds.
Five identical 100-microsecond loops, separated by ideal instantaneous
carrier permutations, form a 500-microsecond model block. The phase is
continuous across loops and every Weyl cross term is retained; motion is
never reset. This duration excludes real shelving and carrier pulse times.

The following arrays are in **u/(2*pi), MHz**, in chronological segment
order. They are display-rounded versions of the stored binary64 values.
The retained `model.json` contains the full exported decimal values in rad/s.

```text
theta = +4*pi/5:
[ 0.130335955888312,  0.349916449600332,  0.426480119623151,
  0.211398545995102, -0.134386442908643, -0.329886579935236,
 -0.253151083765610, -0.053395025522331, -0.053395025522024,
 -0.253151083765609, -0.329886579935100, -0.134386442908927,
  0.211398545995521,  0.426480119622609,  0.349916449600977,
  0.130335955888000 ]

theta = -4*pi/5:
[ 0.106418862354754,  0.285705584709040,  0.348219559505950,
  0.172606190018094, -0.109726071157946, -0.269351264611061,
 -0.206696994352769, -0.043596855777532, -0.043596855777281,
 -0.206696994352768, -0.269351264610950, -0.109726071158178,
  0.172606190018435,  0.348219559505508,  0.285705584709567,
  0.106418862354499 ]
```

| Quantity | Positive target | Negative target |
|---|---:|---:|
| Equality-phase beta, rad | 3.769911184307752 | 2.513274122871835 |
| Peak abs(u)/(2*pi), MHz | 0.426480119623151 | 0.348219559505950 |
| RMS u/(2*pi), MHz | 0.264533786216926 | 0.215990931985986 |
| Fixed nominal raw gamma subtracted, rad | -7.322198557923424 | -4.881465705282282 |

Here beta equals minus theta modulo 2*pi. The two actual amplitude scales
have ratio sqrt(3/2); changing only the sign of a real force would not
reverse its quadratic geometric phase. Both peaks, including the 1.005
amplitude perturbation, remain below the frozen theoretical 5 MHz cap.
That cap is not an experimental optical-power or approximation certificate.

| Construction diagnostic | Recorded value |
|---|---:|
| Newton iterations | 6 |
| Equilibrium gradient infinity norm | 1.2906342661267445e-15 |
| Eigen residual infinity norm | 3.3861802251067274e-15 |
| Eigenvector orthogonality residual | 1.4432899320127035e-15 |
| Closure rank / nullity | 14 / 2 |
| Smallest normalized QR pivot | 0.13002328841928668 |
| Frozen rank tolerance / margin | 1e-10 / 1e-8 |
| Normalized null residual | 8.441653788726604e-17 |
| Unit-shape closure integral maximum, seconds | 1.4718720820255296e-21 |
| Unit-shape squared Euclidean norm | 1 |
| Pair optical phase cosine | -0.3331860985058944 |
| Projected phase eigenvalues, seconds squared | -6.414775958954749e-14; +8.528823038553136e-14 |
| Selected unit-shape pair phase, seconds squared | +8.528823038553138e-14 |

The rank and pair interaction are well separated from the frozen numerical
rejection conditions. These residuals do not constitute interval enclosures.

## All 24 jobs

G hides spectators and applies X5 only to active ions 4 and 5. E keeps the
shelved logical zero but incorrectly applies the 0..4 echo globally, exposing
the other spectator labels to the force. I is a matched-duration zero-force
idle. All endpoint label permutations are identities; coherence distinguishes
the wrong echo from an acceptable endpoint.

`d+100` increases every detuning delta by 2*pi*100 Hz; `u+0.5%` multiplies
the frozen pulse by 1.005. `Ddiff` assigns spectator D_p response
0.002*(p-2) and auxiliary response -0.004, while keeping active D response
zero. The latter is a declared differential-response perturbation, not a
measured calcium polarizability model. Neither pulse nor gamma is refitted.

The first two numerical columns are conservative half-diamond upper-bound
**estimates within the model**, evaluated with floating arithmetic and the
frozen phase convention. They are not infidelities or observed failure
probabilities. A large upper bound alone does not prove that the actual
channel error is large; a value of 1 is the capped, uninformative bound.
The frozen common-phase comparison can also make this estimate loose:
a common scalar phase is physically irrelevant to the electronic channel.

The last column is the largest directly computed trace distance among
300 source/reference Bell witnesses for that job. It is a particular-state
disturbance, not an upper bound over all source states or a full process
tomography result. Display rounding does not alter the retained data.

| Sign | Context | Arm | Gate bound | Protected-source bound | Bell trace distance |
|---|---|---|---:|---:|---:|
| + | nominal | G | 3.662774480e-15 | 0 | 0 |
| + | nominal | E | 1 | 1 | 0.999348616 |
| + | nominal | I | 0 | 0 | 0 |
| + | d+100 | G | 0.738331740 | 0 | 0 |
| + | d+100 | E | 1 | 1 | 0.848484102 |
| + | d+100 | I | 0 | 0 | 0 |
| + | u+0.5% | G | 0.111141118 | 0 | 0 |
| + | u+0.5% | E | 1 | 1 | 0.993372520 |
| + | u+0.5% | I | 0 | 0 | 0 |
| + | Ddiff | G | 0.223112238 | 0.227950581 | 0.053328809 |
| + | Ddiff | E | 1 | 1 | 0.994720921 |
| + | Ddiff | I | 0 | 0 | 0 |
| - | nominal | G | 2.732307816e-15 | 0 | 0 |
| - | nominal | E | 1 | 1 | 0.998766298 |
| - | nominal | I | 0 | 0 | 0 |
| - | d+100 | G | 0.506657619 | 0 | 0 |
| - | d+100 | E | 1 | 1 | 0.995607465 |
| - | d+100 | I | 0 | 0 | 0 |
| - | u+0.5% | G | 0.074115293 | 0 | 0 |
| - | u+0.5% | E | 1 | 1 | 0.999407385 |
| - | u+0.5% | I | 0 | 0 | 0 |
| - | Ddiff | G | 0.148913805 | 0.152150865 | 0.035561913 |
| - | Ddiff | E | 1 | 1 | 0.999997428 |
| - | Ddiff | I | 0 | 0 | 0 |

Both nominal G requirements passed: gate bound <=1e-6 and source bound
<=1e-8. Both nominal idles passed <=1e-10. Both nominal E controls exceeded
the required direct Bell trace distance of 1e-6. All 24 consistency checks
`Bell distance <= source bound + 1e-7` passed; this is a numerical consistency
gate, not an extra efficacy threshold. Stress contexts have no universal
PASS claim.

The positive-target Ddiff G witness changes ion 6 from logical 0 to 4,
with active labels (2,3). Its Bell trace distance is 0.05332880918907375,
Bell fidelity 0.9971560381104754, and relative phase -0.10670823822099962 rad.
The negative-target witness changes the same source ion/label with active
labels (0,0): distance 0.0355619129113408, fidelity 0.9987353503500862,
phase -0.07113882548067885 rad. Their Gaussian exponents are about
6.17e-31 and 3.51e-31. Thus the observed model disturbance is a coherent
phase error even though the final motion nearly closes. It cannot be
dismissed by checking endpoint populations or residual displacement alone.

## Independent numerical checks and timing

Each job has 69 frozen branch fixtures: 25 active anchors, 32 deterministic
full-register branches and 12 source variations. The separate validation
integrates all 80 absolute-time segments from endpoint sin/cos integrals;
it does not reuse the builder's factored-loop computation. Across 1,656
fixtures, maximum phase disagreement was 5.826450433232822e-13 rad and
maximum complex-alpha disagreement was 9.207177505519129e-14, below the
frozen 1e-8 and 1e-9 thresholds. All 7,200 direct Bell witnesses were
retained. Analytic resonance, circular-loop and thermal/Weyl fixtures passed.

All six scanner invocations checked scalar versus AVX512 results across
1,875,000 branches (24*78,125), then timed a separate scan. Their reported
maximum scalar/SIMD discrepancy was exactly zero. All per-case diagnostics
and witness indices were identical across the six invocations. Every
invocation exited zero, emitted empty stderr, and passed the before/after
custody checks. All 80 CPU/place/thread assignments were unique and matched
the requested map, covering CPUs 0 through 79.

Execution environment: Debian GNU/Linux 13, x86_64, Python 3.13.5,
GCC 14.2.0, two CPU packages, 40 physical cores and 80 logical threads.
AVX512/80 was fixed from the previous engineering pilot. Compilation used
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`.

| Invocation | Timed kernel, s | Scalar/SIMD validation scan, s | Subprocess wall, s |
|---|---:|---:|---:|
| Warmup | 0.012068916112 | 0.029741860926 | 0.118176644668 |
| Measured 1 | 0.012141488492 | 0.028036294505 | 0.114457646385 |
| Measured 2 | 0.012146381661 | 0.028241010383 | 0.114346241578 |
| Measured 3 | 0.012308252975 | 0.028242891654 | 0.114312563092 |
| Measured 4 | 0.012270741165 | 0.027193222195 | 0.065668407828 |
| Measured 5 | 0.012277446687 | 0.028477080166 | 0.066621679813 |

The measured kernel median was **0.012270741164684296 s**; the subprocess
wall median was 0.1143125630915165 s. Wall timing includes startup and the
validation pass and is observed through subprocess polling; it is not a
high-resolution estimate of startup overhead alone.

The complete numerical runner took **11.503348348662257 s**, including
model construction (0.5934735648334026 s), independent validation and Bell
witnesses (8.712661769241095 s), six scanner invocations and custody work.
Its external receipt measured 11.638608990237117 s. These totals exclude
compilation and the separate exact verifier, which took 9.73050557076931 s.
The 12.27 ms scan is therefore not the end-to-end simulation time.

## Custody and interpretation

An independent readback checked all 39 retained artifact hashes and byte
counts, all six raw maps, and the recorded per-fixture/per-witness summaries.
The execution archive has 655,962 bytes and SHA256
`9d43cf7865abc4c2bf2a4f98eac30e819ccea5ec9f18e14ffabb1de15d8cface`.
Artifact labels below identify execution outputs, not additional probe files.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| model.json | 1240110 | fb9fe824c7f925ad1690f7f7f4a150deafdd57c4e683007586da4bddddc87e15 |
| coefficients.txt | 261397 | a6bcaa40768e9423b329a022bff9e4bfa96433f4e95929ab41aee5142a65545a |
| independent_validation.json | 6084728 | 9890e45cebae05866fe366d5fd360a32d5b115a17381b53ca9bd4cd9e5ebf543 |
| result.json | 40519 | 9affc0a2bcb8829dd13e83a5994c7fd0f8dea647738e82fba5b4f296f338d2eb |
| metadata.json | 15258 | 0edc272bd5595905f39ca6d0f0398279b4b341a54cca7a67b2f8115c8e0b85ba |
| campaign_pins.json | 2223 | 75989b0d940d7ab6cbc2618766e9a8b69f00b3c7ec213351e776447adabe8497 |
| exact verifier stdout | 3799 | ef8c8870b9ddb100a87b6448aa2e37bcb8576e580bce0f99dd985f2cac14702c |

The compiled scanner SHA256 was
`794fc85912ef19989e1f9868487a6ef2177b140f6b066a41536abcc95556e7ba`.
Source and `SOURCE_SHA256SUMS` digests remained unchanged during execution.
The separate exact verifier does not certify these floating-point values.

Nominal G protects P=(1,2,3,6,7), including source ions (1,6,7), in the
declared endpoint model. Its zero source dependence follows from the ideal
hidden-state response and carrier contract; it is not a measured accuracy.
This auxiliary-gate result does not remove the full-contact C obstruction:
preserving every coherent source state is incompatible with retaining
distinguishable receiver records of that source under the stated unitary
contract. Classical source-label preservation is a different claim.

The calculation assumes a linear force, harmonic axial motion and a
rotating-wave description. Small final alpha does not bound intermediate
excursions, validate the Lamb-Dicke expansion, or prove harmonic/RWA accuracy
through the entire pulse. Ideal discontinuous amplitude steps do not impose
a physical bandwidth limit. Radial confinement/zigzag stability, finite
carrier errors, optical Stark calibration, scattering, heating and decay
remain outside this model. No approximation-error budget was computed.

Finally, agreement at roughly 1e-13 between two implementations is a useful
consistency check, not a 1e-13 physical-accuracy claim. Binary64/trigonometric
errors were not enclosed by interval arithmetic. The nominal 1e-15 bound
estimates must not be promoted into rigorous channel certificates, and
neither upper bounds nor Bell distances are gate infidelities.
