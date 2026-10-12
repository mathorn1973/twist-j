# Continuous-prefix DP5/N384 versus RK4/N512 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.

Report from preserved first-outcome evidence only; no new propagation.

Source pin: `4c3a29e3ce4db210b754cd18e5340b805f8c5df7`. Recorded status: **COMPLETE_PREFIX_COMPARISON_COMPATIBLE**. Completed children: **4/4**.

Recorded campaign wall time: 541.435836714 s. Any saved failure remains a failure; no missing output is treated as a certificate.

| Frozen engineering decision | Saved outcome |
|---|---|
| `candidate_reference_bound_screen_pass` | `True` |
| `candidate_reference_speed_screen_pass` | `True` |
| `joint_engineering_screen_pass` | `True` |

## Scope and interpretation

A is inherited RK4 N512 and C is two consecutive DP5 halfsteps per N384 certificate cell. All arms retain the same pulses, exact model, seven modes, L8/G10, 120 thermal basis columns, both angles, and four adjacent 48.828125 ns blocks per case. Each case/batch starts once at its first active force; the state and cumulative certificate carry through all four checkpoints without a reset. The active prefix lasts 195.3125 ns. The original absolute clock and full analytic linear history remain.

Earlier active indicators vanish exactly in the declared compensated model, so this is a prefix of its initial-value problem. Cases (4,3)/(4,4) start at 100 us and (1,1) at 400 us. Checkpoint comparisons are A/C within one case, not common-time intercase coherences. No later amplitude switch is crossed.

Any completed cumulative certificates cover only the selected columns at recorded prefix endpoints. Do not sum their already cumulative values. They do not close the complete pulse, full thermal state, source/reference channel or physical realization. Protected-source identity remains conditional on the dark-source model; the informative-contact full-source obstruction is unchanged.

The primary accuracy-budget screen is eps_C <= eps_A on all 2880 columns of each matched A/C pair. The speed screen is the strict inequality between exact sums of the two observed C and A program end-to-end times. These compare certificate upper bounds and measured costs, not actual integration errors. A failure does not authorize a longer run. The frozen limits are 300 s per child, 90 s per comparator, and 1200 s for the campaign including its comparisons; bounded cleanup and final preservation can extend the final wall receipt.

## Four propagation timings

| Run | Arm / method / N | Preparation s | Kernel s | Program end-to-end s | Child wall s |
|---:|---|---:|---:|---:|---:|
| 1 | A: RK4, N512 | 76.0088607967 | 72.3735351991 | 150.672965666 | 150.75447268 |
| 2 | C: DP5 two halfsteps, N384 | 41.4000810441 | 58.7135617249 | 102.392514639 | 102.452656215 |
| 3 | C: DP5 two halfsteps, N384 | 39.1920524277 | 56.8697658759 | 98.3487901762 | 98.4454437755 |
| 4 | A: RK4, N512 | 49.1916612796 | 71.4034491573 | 122.879480569 | 122.939735424 |

| Attempt receipt | Exit code | Recorded error | Cleanup error | Wall s | Stderr bytes |
|---|---:|---|---|---:|---:|
| 01-A | 0 | False | False | 150.75447268 | 0 |
| 02-C | 0 | False | False | 102.452656215 | 0 |
| 03-C | 0 | False | False | 98.4454437755 | 0 |
| 04-A | 0 | False | False | 122.939735424 | 0 |

Preparation includes model preparation and fixtures. Kernel time includes workspace setup, the OpenMP region, progress logging and deep checkpoint snapshots. Program end-to-end also includes artifact serialization; child wall additionally includes process overhead. A/C use respectively 4/3 certificate cells, 4/6 integrator substeps, 36/39 right-hand-side evaluations and 64/48 certificate Gauss nodes per checkpoint block. Over the whole prefix these are 16/12 cells, 16/24 substeps, 144/156 RHS calls and 256/192 Gauss nodes. The two-arm comparison changes method, dense curve, substep count and certificate density together; it cannot isolate their individual effects.

| Arm, two-observation median | Preparation s | Kernel s | End-to-end s | Child wall s |
|---|---:|---:|---:|---:|
| A | 62.6002610382 | 71.8884921782 | 136.776223117 | 136.847104052 |
| C | 40.2960667359 | 57.7916638004 | 100.370652407 | 100.449049995 |
| A/C | 1.55350797507x | 1.24392494437x | 1.3627113089x | 1.36235339268x |

A median of two observations is their arithmetic mean. These are descriptive measurements of this workload, with no confidence interval or statistical-significance claim and no extrapolation to a complete trajectory.

## Saved endpoint comparisons and repeats

| Matched runs | Arms | Compatible | Inconsistent | Unresolved | Right eps > left eps |
|---|---|---:|---:|---:|---:|
| 1/2 | A/C | 2880 | 0 | 0 | 0 |
| 4/3 | A/C | 2880 | 0 | 0 | 0 |

Same-arm repeat receipts: 2/2. Their preserved outcomes:

- Arm C, 2/3: all five recorded artifact comparisons agree byte for byte.
- Arm A, 1/4: all five recorded artifact comparisons agree byte for byte.

The remote runner compares actual endpoint bytes. The compact archive omits the large endpoint bodies, retaining their receipts; this local report does not independently repeat that endpoint byte comparison or recompute its distance enclosure. Raw component bodies are included and are read directly for the tables below. For saved [d_lo,d_hi] and the upward eps sum R, COMPATIBLE means d_hi <= R, INCONSISTENT means d_lo > R, and the remainder is UNRESOLVED. Compatibility is a certificate-consistency check, not a proof that the actual error is small.

The additional saved-data comparison with predecessor window zero reports **FIRST_CHECKPOINT_BYTE_AUDIT_PASS**. It is not an acceptance criterion and changes neither the fresh A/C observations nor campaign disposition. Endpoint inheritance is a recorded remote byte comparison; endpoint payloads are not locally replayed.

## Previously exposed column at every checkpoint

Both targets are column 36, occupation (0,0,0,0,0,0,3), at every checkpoint: case 0 for the positive angle and case 3 for the negative angle. They remain inside the unchanged all-2880-column screen, with no exception or tolerance.

| Fresh matched runs | Checkpoint | Angle / labels | A512 eps | C384 eps | C/A | Bound screen | Distance interval | Compatibility |
|---|---:|---|---:|---:|---|---|---|---|
| 1/2 | 1 | +4pi/5 (4,3) | 4.77705505091E-8 | 9.75550845913E-9 | 0.204215952196 .. 0.204215952197 | PASS | [2.15147373757E-8, 2.15147373758E-8] | COMPATIBLE |
| 1/2 | 1 | -4pi/5 (4,3) | 3.87953515049E-8 | 7.05981472860E-9 | 0.181975789746 .. 0.181975789747 | PASS | [1.75623748114E-8, 1.75623748115E-8] | COMPATIBLE |
| 1/2 | 2 | +4pi/5 (4,3) | 1.06544871996E-7 | 2.05459961163E-8 | 0.192838901878 .. 0.192838901879 | PASS | [1.52900283753E-8, 1.52900283754E-8] | COMPATIBLE |
| 1/2 | 2 | -4pi/5 (4,3) | 8.66002967813E-8 | 1.51589473532E-8 | 0.175044981560 .. 0.175044981561 | PASS | [1.24748779210E-8, 1.24748779211E-8] | COMPATIBLE |
| 1/2 | 3 | +4pi/5 (4,3) | 1.80631233632E-7 | 3.76220724534E-8 | 0.208281102314 .. 0.208281102315 | PASS | [2.83543453686E-8, 2.83543453688E-8] | COMPATIBLE |
| 1/2 | 3 | -4pi/5 (4,3) | 1.46850169688E-7 | 2.83332198599E-8 | 0.192939646717 .. 0.192939646718 | PASS | [2.31435309222E-8, 2.31435309223E-8] | COMPATIBLE |
| 1/2 | 4 | +4pi/5 (4,3) | 2.68646870171E-7 | 6.39523286466E-8 | 0.238053503493 .. 0.238053503494 | PASS | [2.29042403087E-8, 2.29042403089E-8] | COMPATIBLE |
| 1/2 | 4 | -4pi/5 (4,3) | 2.18124876765E-7 | 4.79843688136E-8 | 0.219985769277 .. 0.219985769278 | PASS | [1.86927079659E-8, 1.86927079660E-8] | COMPATIBLE |
| 4/3 | 1 | +4pi/5 (4,3) | 4.77705505091E-8 | 9.75550845913E-9 | 0.204215952196 .. 0.204215952197 | PASS | [2.15147373757E-8, 2.15147373758E-8] | COMPATIBLE |
| 4/3 | 1 | -4pi/5 (4,3) | 3.87953515049E-8 | 7.05981472860E-9 | 0.181975789746 .. 0.181975789747 | PASS | [1.75623748114E-8, 1.75623748115E-8] | COMPATIBLE |
| 4/3 | 2 | +4pi/5 (4,3) | 1.06544871996E-7 | 2.05459961163E-8 | 0.192838901878 .. 0.192838901879 | PASS | [1.52900283753E-8, 1.52900283754E-8] | COMPATIBLE |
| 4/3 | 2 | -4pi/5 (4,3) | 8.66002967813E-8 | 1.51589473532E-8 | 0.175044981560 .. 0.175044981561 | PASS | [1.24748779210E-8, 1.24748779211E-8] | COMPATIBLE |
| 4/3 | 3 | +4pi/5 (4,3) | 1.80631233632E-7 | 3.76220724534E-8 | 0.208281102314 .. 0.208281102315 | PASS | [2.83543453686E-8, 2.83543453688E-8] | COMPATIBLE |
| 4/3 | 3 | -4pi/5 (4,3) | 1.46850169688E-7 | 2.83332198599E-8 | 0.192939646717 .. 0.192939646718 | PASS | [2.31435309222E-8, 2.31435309223E-8] | COMPATIBLE |
| 4/3 | 4 | +4pi/5 (4,3) | 2.68646870171E-7 | 6.39523286466E-8 | 0.238053503493 .. 0.238053503494 | PASS | [2.29042403087E-8, 2.29042403089E-8] | COMPATIBLE |
| 4/3 | 4 | -4pi/5 (4,3) | 2.18124876765E-7 | 4.79843688136E-8 | 0.219985769277 .. 0.219985769278 | PASS | [1.86927079659E-8, 1.86927079660E-8] | COMPATIBLE |

| Fresh runs | Checkpoint | Case | Guard A/C | Tail A/C | Continuum A/C | Jumps A/C | Time-node A/C | Projection-node A/C | Arithmetic-node A/C |
|---|---:|---:|---|---|---|---|---|---|---|
| 1/2 | 1 | 0 | 4.75251774519E-8 / 9.50943452706E-9 | 2.44708586415E-10 / 2.45319947557E-10 | 6.50716840341E-13 / 7.43668511657E-13 | 1.37539471500E-14 / 1.03160110025E-14 | 4.69725016573E-8 / 6.31253535945E-9 | 6.89358640802E-9 / 6.94850274046E-9 | 3.20082377417E-14 / 3.20130273593E-14 |
| 1/2 | 1 | 3 | 3.86168399025E-8 / 6.88086919851E-9 | 1.77966756030E-10 / 1.78328453362E-10 | 5.31092467674E-13 / 6.06760841217E-13 | 1.37539031488E-14 / 1.03158939907E-14 | 3.83410735496E-8 / 5.15305468756E-9 | 4.41341705825E-9 / 4.44805018252E-9 | 2.61477196628E-14 / 2.61419460510E-14 |
| 1/2 | 2 | 0 | 1.05969405409E-7 / 1.99697784398E-8 | 5.74135281140E-10 / 5.74706395592E-10 | 1.30379678122E-12 / 1.49064834033E-12 | 2.75081772920E-14 / 2.06325991765E-14 | 1.04919318107E-7 / 1.35019582573E-8 | 1.44720642652E-8 / 1.45345169580E-8 | 6.40612833924E-14 / 6.40667501046E-14 |
| 1/2 | 2 | 3 | 8.61878577601E-8 / 1.47460293717E-8 | 4.11347507968E-10 / 4.11681296377E-10 | 1.06400524164E-12 / 1.21605276331E-12 | 2.75080228537E-14 / 2.06323525007E-14 | 8.56219256333E-8 / 1.10207185600E-8 | 9.61437776415E-9 / 9.65720582977E-9 | 5.23287903092E-14 / 5.23189486819E-14 |
| 1/2 | 3 | 0 | 1.79695586187E-7 / 3.66856261302E-8 | 9.33647026019E-10 / 9.34174467219E-10 | 1.95915707432E-12 / 2.24090581961E-12 | 4.12626591533E-14 / 3.09501520907E-14 | 1.77202041589E-7 / 2.19086333887E-8 | 2.88711760262E-8 / 2.89459815968E-8 | 9.60663404036E-14 / 9.60703746018E-14 |
| 1/2 | 3 | 3 | 1.46185450557E-7 / 2.76679782744E-8 | 6.63079160487E-10 / 6.63382728307E-10 | 1.59870794936E-12 / 1.82790772629E-12 | 4.12623983163E-14 / 3.09494610339E-14 | 1.44604121409E-7 / 1.78834494481E-8 | 2.05276730199E-8 / 2.05790582252E-8 | 7.84514645849E-14 / 7.84444022258E-14 |
| 1/2 | 4 | 0 | 2.67327177321E-7 / 6.26317912766E-8 | 1.31702180569E-9 / 1.31750273941E-9 | 2.61602651023E-12 / 2.99336266012E-12 | 5.50173834298E-14 / 4.12679471552E-14 | 2.61425935839E-7 / 3.13765163499E-8 | 5.30127530365E-8 / 5.30935161225E-8 | 1.27903838557E-13 / 1.27905902574E-13 |
| 1/2 | 4 | 3 | 2.17193051910E-7 / 4.70519791361E-8 | 9.29635210034E-10 / 9.29906879333E-10 | 2.13462800843E-12 / 2.44153112694E-12 | 5.50169392964E-14 / 4.12669711270E-14 | 2.13344280809E-7 / 2.56147434582E-8 | 3.82921918308E-8 / 3.83474360985E-8 | 1.04466280509E-13 / 1.04448220293E-13 |
| 4/3 | 1 | 0 | 4.75251774519E-8 / 9.50943452706E-9 | 2.44708586415E-10 / 2.45319947557E-10 | 6.50716840341E-13 / 7.43668511657E-13 | 1.37539471500E-14 / 1.03160110025E-14 | 4.69725016573E-8 / 6.31253535945E-9 | 6.89358640802E-9 / 6.94850274046E-9 | 3.20082377417E-14 / 3.20130273593E-14 |
| 4/3 | 1 | 3 | 3.86168399025E-8 / 6.88086919851E-9 | 1.77966756030E-10 / 1.78328453362E-10 | 5.31092467674E-13 / 6.06760841217E-13 | 1.37539031488E-14 / 1.03158939907E-14 | 3.83410735496E-8 / 5.15305468756E-9 | 4.41341705825E-9 / 4.44805018252E-9 | 2.61477196628E-14 / 2.61419460510E-14 |
| 4/3 | 2 | 0 | 1.05969405409E-7 / 1.99697784398E-8 | 5.74135281140E-10 / 5.74706395592E-10 | 1.30379678122E-12 / 1.49064834033E-12 | 2.75081772920E-14 / 2.06325991765E-14 | 1.04919318107E-7 / 1.35019582573E-8 | 1.44720642652E-8 / 1.45345169580E-8 | 6.40612833924E-14 / 6.40667501046E-14 |
| 4/3 | 2 | 3 | 8.61878577601E-8 / 1.47460293717E-8 | 4.11347507968E-10 / 4.11681296377E-10 | 1.06400524164E-12 / 1.21605276331E-12 | 2.75080228537E-14 / 2.06323525007E-14 | 8.56219256333E-8 / 1.10207185600E-8 | 9.61437776415E-9 / 9.65720582977E-9 | 5.23287903092E-14 / 5.23189486819E-14 |
| 4/3 | 3 | 0 | 1.79695586187E-7 / 3.66856261302E-8 | 9.33647026019E-10 / 9.34174467219E-10 | 1.95915707432E-12 / 2.24090581961E-12 | 4.12626591533E-14 / 3.09501520907E-14 | 1.77202041589E-7 / 2.19086333887E-8 | 2.88711760262E-8 / 2.89459815968E-8 | 9.60663404036E-14 / 9.60703746018E-14 |
| 4/3 | 3 | 3 | 1.46185450557E-7 / 2.76679782744E-8 | 6.63079160487E-10 / 6.63382728307E-10 | 1.59870794936E-12 / 1.82790772629E-12 | 4.12623983163E-14 / 3.09494610339E-14 | 1.44604121409E-7 / 1.78834494481E-8 | 2.05276730199E-8 / 2.05790582252E-8 | 7.84514645849E-14 / 7.84444022258E-14 |
| 4/3 | 4 | 0 | 2.67327177321E-7 / 6.26317912766E-8 | 1.31702180569E-9 / 1.31750273941E-9 | 2.61602651023E-12 / 2.99336266012E-12 | 5.50173834298E-14 / 4.12679471552E-14 | 2.61425935839E-7 / 3.13765163499E-8 | 5.30127530365E-8 / 5.30935161225E-8 | 1.27903838557E-13 / 1.27905902574E-13 |
| 4/3 | 4 | 3 | 2.17193051910E-7 / 4.70519791361E-8 | 9.29635210034E-10 / 9.29906879333E-10 | 2.13462800843E-12 / 2.44153112694E-12 | 5.50169392964E-14 / 4.12669711270E-14 | 2.13344280809E-7 / 2.56147434582E-8 | 3.82921918308E-8 / 3.83474360985E-8 | 1.04466280509E-13 / 1.04448220293E-13 |

The separate node diagnostics have no independent continuous-time allowance. Their changes help locate a conservative bound contribution but do not identify the unknown true integration error.

## Cumulative growth in every recorded observation

At each checkpoint and angle, eps max is over its three cases and 120 columns. Growth ratios are exact rational quotients of each saved binary64 E_k and that same column's E_1, then displayed with outward decimal endpoints. The saved growth files are checked against every raw component row. A zero denominator is reported separately; no growth threshold or fitted law is introduced. The increase from a previous cumulative upper bound is diagnostic and is not a separately certified interval error.

| Run / arm | Checkpoint | Angle | Cumulative eps max | Columnwise E_k/E_1 range | Increase from previous range |
|---|---:|---|---:|---|---|
| 1 / A | 1 | +4pi/5 | 7.76886781316E-8 | 1 .. 1 | 1.60928325024E-8 .. 7.76886781316E-8 |
| 1 / A | 1 | -4pi/5 | 6.30866529437E-8 | 1 .. 1 | 1.31350574326E-8 .. 6.30866529437E-8 |
| 1 / A | 2 | +4pi/5 | 1.63623597316E-7 | 1.92465695608 .. 2.24104412196 | 1.97001699155E-8 .. 8.59349191841E-8 |
| 1 / A | 2 | -4pi/5 | 1.32804315924E-7 | 1.91856229821 .. 2.23223384819 | 1.60729376471E-8 .. 6.97176629803E-8 |
| 1 / A | 3 | +4pi/5 | 2.56765051404E-7 | 2.74143956543 .. 3.78122570721 | 2.44315297188E-8 .. 9.31414540903E-8 |
| 1 / A | 3 | -4pi/5 | 2.08205643353E-7 | 2.73173298283 .. 3.78525168588 | 1.99354573032E-8 .. 7.54013274305E-8 |
| 1 / A | 4 | +4pi/5 | 3.54859488296E-7 | 3.51888070025 .. 6.03647693196 | 2.83850467709E-8 .. 9.80944368920E-8 |
| 1 / A | 4 | -4pi/5 | 2.87089347057E-7 | 3.50106649963 .. 5.98037250180 | 2.31671616601E-8 .. 7.88837037039E-8 |
| 2 / C | 1 | +4pi/5 | 3.20815769029E-8 | 1 .. 1 | 2.01509241557E-9 .. 3.20815769029E-8 |
| 2 / C | 1 | -4pi/5 | 2.36547388287E-8 | 1 .. 1 | 1.64484741507E-9 .. 2.36547388287E-8 |
| 2 / C | 2 | +4pi/5 | 7.92298882066E-8 | 1.98314875724 .. 2.46963821178 | 2.30055176799E-9 .. 4.71483113037E-8 |
| 2 / C | 2 | -4pi/5 | 5.63306947788E-8 | 1.95978914356 .. 2.38187455498 | 1.87740254559E-9 .. 3.26759559503E-8 |
| 2 / C | 3 | +4pi/5 | 1.36881558088E-7 | 2.80192797945 .. 4.32356810739 | 2.69444675196E-9 .. 5.76516698855E-8 |
| 2 / C | 3 | -4pi/5 | 9.55585319953E-8 | 2.71859659670 .. 4.33976630374 | 2.19952832447E-9 .. 3.92278372204E-8 |
| 2 / C | 4 | +4pi/5 | 2.07737693882E-7 | 3.64252172663 .. 7.66316600217 | 3.03690230690E-9 .. 7.08561357958E-8 |
| 2 / C | 4 | -4pi/5 | 1.43477444429E-7 | 3.49196474496 .. 8.12491163591 | 2.47999220144E-9 .. 4.79189124337E-8 |
| 3 / C | 1 | +4pi/5 | 3.20815769029E-8 | 1 .. 1 | 2.01509241557E-9 .. 3.20815769029E-8 |
| 3 / C | 1 | -4pi/5 | 2.36547388287E-8 | 1 .. 1 | 1.64484741507E-9 .. 2.36547388287E-8 |
| 3 / C | 2 | +4pi/5 | 7.92298882066E-8 | 1.98314875724 .. 2.46963821178 | 2.30055176799E-9 .. 4.71483113037E-8 |
| 3 / C | 2 | -4pi/5 | 5.63306947788E-8 | 1.95978914356 .. 2.38187455498 | 1.87740254559E-9 .. 3.26759559503E-8 |
| 3 / C | 3 | +4pi/5 | 1.36881558088E-7 | 2.80192797945 .. 4.32356810739 | 2.69444675196E-9 .. 5.76516698855E-8 |
| 3 / C | 3 | -4pi/5 | 9.55585319953E-8 | 2.71859659670 .. 4.33976630374 | 2.19952832447E-9 .. 3.92278372204E-8 |
| 3 / C | 4 | +4pi/5 | 2.07737693882E-7 | 3.64252172663 .. 7.66316600217 | 3.03690230690E-9 .. 7.08561357958E-8 |
| 3 / C | 4 | -4pi/5 | 1.43477444429E-7 | 3.49196474496 .. 8.12491163591 | 2.47999220144E-9 .. 4.79189124337E-8 |
| 4 / A | 1 | +4pi/5 | 7.76886781316E-8 | 1 .. 1 | 1.60928325024E-8 .. 7.76886781316E-8 |
| 4 / A | 1 | -4pi/5 | 6.30866529437E-8 | 1 .. 1 | 1.31350574326E-8 .. 6.30866529437E-8 |
| 4 / A | 2 | +4pi/5 | 1.63623597316E-7 | 1.92465695608 .. 2.24104412196 | 1.97001699155E-8 .. 8.59349191841E-8 |
| 4 / A | 2 | -4pi/5 | 1.32804315924E-7 | 1.91856229821 .. 2.23223384819 | 1.60729376471E-8 .. 6.97176629803E-8 |
| 4 / A | 3 | +4pi/5 | 2.56765051404E-7 | 2.74143956543 .. 3.78122570721 | 2.44315297188E-8 .. 9.31414540903E-8 |
| 4 / A | 3 | -4pi/5 | 2.08205643353E-7 | 2.73173298283 .. 3.78525168588 | 1.99354573032E-8 .. 7.54013274305E-8 |
| 4 / A | 4 | +4pi/5 | 3.54859488296E-7 | 3.51888070025 .. 6.03647693196 | 2.83850467709E-8 .. 9.80944368920E-8 |
| 4 / A | 4 | -4pi/5 | 2.87089347057E-7 | 3.50106649963 .. 5.98037250180 | 2.31671616601E-8 .. 7.88837037039E-8 |

Continuity evidence is conditional on the reviewed harness plus its actual recorded assertions: 90 initializations, 270 state/certificate carry checks and one polynomial-start/monotonicity check per certified cell. The renderer also checks all 21,600 saved first-ten-component monotonicity comparisons per completed child. Endpoint norm intervals are not required to be monotone. A monotone budget alone would not exclude a reset of the numerical state.

## First matched pair: both angles

Each angle contains 1440 checkpoint columns. Bounds/ranges and rational ratio ranges are displayed outward from saved binary64 values; decimal displays and descriptive timings use 12 significant digits. Every decision uses the saved exact dyadic numbers. Pair ratios are columnwise ratios, not ratios of independent maxima.

| Angle | A eps max | C eps max | Paired C/A range |
|---|---:|---:|---|
| +4pi/5 | 3.54859488296E-7 | 2.07737693882E-7 | 0.107676954929 .. 0.829375647215 |
| -4pi/5 | 2.87089347057E-7 | 1.43477444429E-7 | 0.107727301499 .. 0.785417659126 |

## First matched pair: 24 checkpoint/case groups

Each eps range covers all 120 columns. Tables use the first preserved A/C observation; second observations enter the repeat and primary decisions above.

| Checkpoint | Case / angle / labels | A eps range | C eps range | Paired C/A |
|---:|---|---|---|---|
| 1 | 0: +4pi/5 (4,3) | 1.60928325024E-8 .. 4.77705505091E-8 | 2.01509241557E-9 .. 1.16673915329E-8 | 0.122409930607 .. 0.516905499029 |
| 1 | 1: +4pi/5 (4,4) | 3.04718118059E-8 .. 7.76886781316E-8 | 3.34320859434E-9 .. 3.20815769029E-8 | 0.107676955047 .. 0.688980988944 |
| 1 | 2: +4pi/5 (1,1) | 3.04718118059E-8 .. 7.76886781314E-8 | 3.34320859014E-9 .. 3.20815768982E-8 | 0.107676954929 .. 0.688980988856 |
| 1 | 3: -4pi/5 (4,3) | 1.31350574326E-8 .. 3.87953515049E-8 | 1.64484741507E-9 .. 7.79510068387E-9 | 0.122410274942 .. 0.441680360830 |
| 1 | 4: -4pi/5 (4,4) | 2.48738906768E-8 .. 6.30866529437E-8 | 2.73019038923E-9 .. 2.36547388287E-8 | 0.107727301610 .. 0.653629340456 |
| 1 | 5: -4pi/5 (1,1) | 2.48738906767E-8 .. 6.30866529434E-8 | 2.73019038577E-9 .. 2.36547388247E-8 | 0.107727301499 .. 0.653629340360 |
| 2 | 0: +4pi/5 (4,3) | 3.57930024179E-8 .. 1.06544871996E-7 | 4.31564418356E-9 .. 2.43378505087E-8 | 0.118284613707 .. 0.512281130454 |
| 2 | 1: +4pi/5 (4,4) | 6.11887007822E-8 .. 1.63623597314E-7 | 6.76364370776E-9 .. 7.92298882066E-8 | 0.109005261497 .. 0.759259383035 |
| 2 | 2: +4pi/5 (1,1) | 6.11887007844E-8 .. 1.63623597316E-7 | 6.76364370236E-9 .. 7.92298882018E-8 | 0.109005261410 .. 0.759259382979 |
| 2 | 3: -4pi/5 (4,3) | 2.92079950797E-8 .. 8.66002967813E-8 | 3.52224996067E-9 .. 1.62103306893E-8 | 0.118299991526 .. 0.430147915748 |
| 2 | 4: -4pi/5 (4,4) | 4.99424093494E-8 .. 1.32804315923E-7 | 5.52268777193E-9 .. 5.63306947788E-8 | 0.109048980502 .. 0.715551724755 |
| 2 | 5: -4pi/5 (1,1) | 4.99424093512E-8 .. 1.32804315924E-7 | 5.52268776729E-9 .. 5.63306947749E-8 | 0.109048980423 .. 0.715551724694 |
| 3 | 0: +4pi/5 (4,3) | 6.02245321368E-8 .. 1.80631233632E-7 | 7.01009093553E-9 .. 4.63624005213E-8 | 0.114456674520 .. 0.555062769643 |
| 3 | 1: +4pi/5 (4,4) | 9.26288533253E-8 .. 2.56765051404E-7 | 1.02607465496E-8 .. 1.36881558087E-7 | 0.109449235934 .. 0.798889851123 |
| 3 | 2: +4pi/5 (1,1) | 9.26288533236E-8 .. 2.56765051402E-7 | 1.02607465494E-8 .. 1.36881558088E-7 | 0.109449235929 .. 0.798889851135 |
| 3 | 3: -4pi/5 (4,3) | 4.91434523830E-8 .. 1.46850169688E-7 | 5.72177828514E-9 .. 3.26209564069E-8 | 0.114486957459 .. 0.490498685508 |
| 3 | 4: -4pi/5 (4,4) | 7.56004633423E-8 .. 2.08205643353E-7 | 8.37778831507E-9 .. 9.55585319946E-8 | 0.109478464124 .. 0.753590880857 |
| 3 | 5: -4pi/5 (1,1) | 7.56004633408E-8 .. 2.08205643351E-7 | 8.37778831458E-9 .. 9.55585319953E-8 | 0.109478464119 .. 0.753590880869 |
| 4 | 0: +4pi/5 (4,3) | 8.86095789077E-8 .. 2.68646870171E-7 | 1.00469932424E-8 .. 8.61137214582E-8 | 0.111538388652 .. 0.650889875135 |
| 4 | 1: +4pi/5 (4,4) | 1.24960739973E-7 .. 3.54859488296E-7 | 1.38045276622E-8 .. 2.07737693882E-7 | 0.109144018605 .. 0.829375647210 |
| 4 | 2: +4pi/5 (1,1) | 1.24960739968E-7 .. 3.54859488291E-7 | 1.38045276582E-8 .. 2.07737693880E-7 | 0.109144018573 .. 0.829375647215 |
| 4 | 3: -4pi/5 (4,3) | 7.23106140431E-8 .. 2.18124876765E-7 | 8.20177048658E-9 .. 6.13436974934E-8 | 0.111577723304 .. 0.593271329756 |
| 4 | 4: -4pi/5 (4,4) | 1.01992639870E-7 .. 2.87089347057E-7 | 1.12718753307E-8 .. 1.43477444429E-7 | 0.109166058213 .. 0.785417659122 |
| 4 | 5: -4pi/5 (1,1) | 1.01992639866E-7 .. 2.87089347053E-7 | 1.12718753268E-8 .. 1.43477444426E-7 | 0.109166058179 .. 0.785417659126 |

## First matched pair: growth by case and checkpoint

Each range covers the same 120 initial columns within that case. The table displays E_k/E_1; the final checkpoint therefore also gives E_4/E_1 without an additional extrapolation.

| Checkpoint | Case / angle / labels | A growth range | C growth range |
|---:|---|---|---|
| 1 | 0: +4pi/5 (4,3) | 1 .. 1 | 1 .. 1 |
| 1 | 1: +4pi/5 (4,4) | 1 .. 1 | 1 .. 1 |
| 1 | 2: +4pi/5 (1,1) | 1 .. 1 | 1 .. 1 |
| 1 | 3: -4pi/5 (4,3) | 1 .. 1 | 1 .. 1 |
| 1 | 4: -4pi/5 (4,4) | 1 .. 1 | 1 .. 1 |
| 1 | 5: -4pi/5 (1,1) | 1 .. 1 | 1 .. 1 |
| 2 | 0: +4pi/5 (4,3) | 2.16671558117 .. 2.23210928252 | 2.07706191238 .. 2.28579017248 |
| 2 | 1: +4pi/5 (4,4) | 1.92465695608 .. 2.24104412189 | 1.98314875724 .. 2.46963821157 |
| 2 | 2: +4pi/5 (1,1) | 1.92465695613 .. 2.24104412196 | 1.98314875791 .. 2.46963821178 |
| 2 | 3: -4pi/5 (4,3) | 2.16551616308 .. 2.23223384819 | 2.07955372825 .. 2.23997013016 |
| 2 | 4: -4pi/5 (4,4) | 1.91856229821 .. 2.17529146765 | 1.95978914356 .. 2.38187455474 |
| 2 | 5: -4pi/5 (1,1) | 1.91856229826 .. 2.17529146773 | 1.95978914377 .. 2.38187455498 |
| 3 | 0: +4pi/5 (4,3) | 3.65061898472 .. 3.78122570721 | 3.43254177510 .. 4.12502533232 |
| 3 | 1: +4pi/5 (4,4) | 2.74143956544 .. 3.67967589323 | 2.80192797945 .. 4.32356810652 |
| 3 | 2: +4pi/5 (1,1) | 2.74143956543 .. 3.67967589327 | 2.80192798011 .. 4.32356810739 |
| 3 | 3: -4pi/5 (4,3) | 3.64870607374 .. 3.78525168588 | 3.43248660910 .. 4.33976630374 |
| 3 | 4: -4pi/5 (4,4) | 2.73173298285 .. 3.50386380086 | 2.71859659670 .. 4.15346232945 |
| 3 | 5: -4pi/5 (1,1) | 2.73173298283 .. 3.50386380090 | 2.71859659742 .. 4.15346233075 |
| 4 | 0: +4pi/5 (4,3) | 5.32411567610 .. 6.03647693196 | 4.89355945768 .. 7.66316600217 |
| 4 | 1: +4pi/5 (4,4) | 3.51888070031 .. 5.37917357933 | 3.64252172663 .. 6.79886635234 |
| 4 | 2: +4pi/5 (1,1) | 3.51888070025 .. 5.37917357933 | 3.64252172730 .. 6.79886635398 |
| 4 | 3: -4pi/5 (4,3) | 5.32027778037 .. 5.98037250180 | 4.87101963887 .. 8.12491163591 |
| 4 | 4: -4pi/5 (4,4) | 3.50106649970 .. 5.04773273920 | 3.49196474496 .. 6.52032153355 |
| 4 | 5: -4pi/5 (1,1) | 3.50106649963 .. 5.04773273919 | 3.49196474567 .. 6.52032153530 |

## Cumulative components

Each entry is the independent maximum **A / C** over the 120 columns. Guard already includes arithmetic balls; tail bounds omitted guard space; continuum covers inter-node defect; jumps cover stored polynomial endpoint discrepancies. These maxima are neither additive across columns nor infidelities.

| Checkpoint | Case | Guard | Tail | Continuum | Jumps |
|---:|---:|---|---|---|---|
| 1 | 0 | 4.75251774519E-8 / 1.13587621162E-8 | 3.14971911439E-10 / 3.16184908904E-10 | 6.50793049103E-13 / 7.43668511657E-13 | 1.37539897400E-14 / 1.03162339784E-14 |
| 1 | 1 | 7.69742805466E-8 / 3.10600530343E-8 | 1.01457982473E-9 / 1.02002282648E-9 | 1.30680381981E-12 / 1.49134521772E-12 | 1.37548897277E-14 / 1.03177422975E-14 |
| 1 | 2 | 7.69742805464E-8 / 3.10600530296E-8 | 1.01457982473E-9 / 1.02002282647E-9 | 1.30680381981E-12 / 1.49134521772E-12 | 1.37548854708E-14 / 1.03176998208E-14 |
| 1 | 3 | 3.86168399025E-8 / 7.57450015414E-9 | 2.24772887573E-10 / 2.25511574950E-10 | 5.31151714514E-13 / 6.06760841217E-13 | 1.37539297400E-14 / 1.03159398800E-14 |
| 1 | 4 | 6.25801927737E-8 / 2.29456218635E-8 | 7.04520710760E-10 / 7.07890870697E-10 | 1.06628965557E-12 / 1.21630403643E-12 | 1.37546825439E-14 / 1.03173833733E-14 |
| 1 | 5 | 6.25801927735E-8 / 2.29456218597E-8 | 7.04520710758E-10 / 7.07890870691E-10 | 1.06628965557E-12 / 1.21630403643E-12 | 1.37546768666E-14 / 1.03174885166E-14 |
| 2 | 0 | 1.05969405409E-7 / 2.35286952065E-8 | 8.79225597059E-10 / 8.80503427924E-10 | 1.30392986240E-12 / 1.49064834033E-12 | 2.75082607451E-14 / 2.06327381751E-14 |
| 2 | 1 | 1.61918221113E-7 / 7.63178320686E-8 | 2.90343294848E-9 / 2.90905270456E-9 | 2.61430371591E-12 / 2.98363307744E-12 | 2.75098250414E-14 / 2.06353653739E-14 |
| 2 | 2 | 1.61918221115E-7 / 7.63178320639E-8 | 2.90343294848E-9 / 2.90905270455E-9 | 2.61430371591E-12 / 2.98363307744E-12 | 2.75098075585E-14 / 2.06353814238E-14 |
| 2 | 3 | 8.61878577601E-8 / 1.56432074224E-8 | 6.14097497028E-10 / 6.14872709347E-10 | 1.06410640626E-12 / 1.21605276331E-12 | 2.75080933364E-14 / 2.06323952748E-14 |
| 2 | 4 | 1.31616780523E-7 / 5.43626711978E-8 | 1.96212044967E-9 / 1.96557051155E-9 | 2.13299552431E-12 / 2.43324905588E-12 | 2.75093910393E-14 / 2.06343798778E-14 |
| 2 | 5 | 1.31616780524E-7 / 5.43626711940E-8 | 1.96212044966E-9 / 1.96557051154E-9 | 2.13299552431E-12 / 2.43324905588E-12 | 2.75093763977E-14 / 2.06345420151E-14 |
| 3 | 0 | 1.79695586187E-7 / 4.49696173826E-8 | 1.57135169467E-9 / 1.57265275758E-9 | 1.95933638922E-12 / 2.24090581961E-12 | 4.12628394467E-14 / 3.09501520907E-14 |
| 3 | 1 | 2.54075729922E-7 / 1.31832870920E-7 | 5.03857090256E-9 / 5.04418085929E-9 | 3.92224614591E-12 / 4.47803076653E-12 | 4.12647444239E-14 / 3.09533709531E-14 |
| 3 | 2 | 2.54075729920E-7 / 1.31832870921E-7 | 5.03857090256E-9 / 5.04418085928E-9 | 3.92224614591E-12 / 4.47803076653E-12 | 4.12647424887E-14 / 3.09526650357E-14 |
| 3 | 3 | 1.46185450557E-7 / 3.16563820622E-8 | 1.08057303233E-9 / 1.08135706231E-9 | 1.59884070052E-12 / 1.82790772629E-12 | 4.12625207327E-14 / 3.09494610339E-14 |
| 3 | 4 | 2.06344569185E-7 / 9.21998365251E-8 | 3.35158155742E-9 / 3.35501510204E-9 | 3.20002123457E-12 / 3.65175340021E-12 | 4.12640824311E-14 / 3.09513472452E-14 |
| 3 | 5 | 2.06344569183E-7 / 9.21998365259E-8 | 3.35158155742E-9 / 3.35501510203E-9 | 3.20002123457E-12 / 3.65175340021E-12 | 4.12640687459E-14 / 3.09513445297E-14 |
| 4 | 0 | 2.67327177321E-7 / 8.40681094080E-8 | 2.36604600350E-9 / 2.36735432127E-9 | 2.61624688842E-12 / 2.99336266012E-12 | 5.50176558603E-14 / 4.12679471552E-14 |
| 4 | 1 | 3.51108678851E-7 / 2.00272916930E-7 | 7.45309361556E-9 / 7.45876833759E-9 | 5.22995144413E-12 / 5.97280910598E-12 | 5.50196228366E-14 / 4.12711182839E-14 |
| 4 | 2 | 3.51108678846E-7 / 2.00272916928E-7 | 7.45309361555E-9 / 7.45876833759E-9 | 5.22995144413E-12 / 5.97280910598E-12 | 5.50196429410E-14 / 4.12705328618E-14 |
| 4 | 3 | 2.17193051910E-7 / 5.99410886017E-8 | 1.60650799724E-9 / 1.60729225008E-9 | 2.13478707680E-12 / 2.44153112694E-12 | 5.50171381011E-14 / 4.12669711270E-14 |
| 4 | 4 | 2.84509133118E-7 / 1.38575004469E-7 | 4.89407544384E-9 / 4.89753264908E-9 | 4.26697303022E-12 / 4.87063186326E-12 | 5.50187461719E-14 / 4.12687711941E-14 |
| 4 | 5 | 2.84509133113E-7 / 1.38575004467E-7 | 4.89407544383E-9 / 4.89753264908E-9 | 4.26697303022E-12 / 4.87063186326E-12 | 5.50187303546E-14 / 4.12689596956E-14 |

## Node diagnostics by angle

Time/projection node diagnostics have no independent continuum allowance. Arithmetic-node diagnostics are already included in guard and must not be added again. The maximum norm error is diagnostic, not the vector-error bound.

| Angle | Diagnostic | A max | C max |
|---|---|---:|---:|
| +4pi/5 | `sampled_time_node_L2` | 3.40092714330E-7 | 3.94845659278E-8 |
| +4pi/5 | `sampled_projection_node_L2` | 1.99656624639E-7 | 1.99709056478E-7 |
| +4pi/5 | `sampled_arithmetic_node_L2` | 3.12812469024E-13 | 3.12813570162E-13 |
| +4pi/5 | `maximum_norm_error` | 2.27369012507E-10 | 2.82573964228E-12 |
| -4pi/5 | `sampled_time_node_L2` | 2.77579945203E-7 | 3.22414294190E-8 |
| -4pi/5 | `sampled_projection_node_L2` | 1.38016119295E-7 | 1.38043529663E-7 |
| -4pi/5 | `sampled_arithmetic_node_L2` | 2.55461920834E-13 | 2.55456165225E-13 |
| -4pi/5 | `maximum_norm_error` | 1.52296175671E-10 | 2.82596168689E-12 |

## Decision and limits on any next test

The frozen short-prefix cost/bound condition is met on this panel, including the two focused states through all checkpoints. This supports retaining N384 for this short continuous workload. It establishes only the recorded cumulative column bounds; it does not establish full-pulse feasibility or authorize a long run.

## Build, exact gate, and evidence custody

| Recorded separate stage | Wall seconds | Exit code | Standard output bytes | Standard error bytes |
|---|---:|---:|---:|---:|
| build_baseline | 13.8878587075 | 0 | 0 | 0 |
| build_candidate | 14.4392668698 | 0 | 0 | 0 |
| build_comparator | 14.1388129201 | 0 | 0 | 0 |
| exact | 0.215289261192 | 0 | 1536 | 0 |

The saved exact gate reports **PASS**; stdout SHA-256 `8853daa287401d818bcff8c8d347d0aa32c3c0c9f64d65e914a0ab4bbc96c6e2`. This supports the listed algebraic fixtures, not an independent numerical replay or complete trajectory certificate. Any later CI exact replay has the same limited role.

Frozen sources are identified by the public pin. Completed child records passed the runner's source/input/binary custody checks; the recorded campaign status governs any later failure. This renderer authenticates every included archive member against the preserved manifest, but does not reconstruct the remote machine state or certify the solver implementation independently.

| Endpoint artifact | Bytes | SHA-256 | Local payload |
|---|---:|---|---|
| 01-A | 296524800 | `9207c3f50d6ec71cc92bf781829cbc4b1dead2f5b7e6524ab5eac295a98d753a` | remote receipt only |
| 02-C | 296524800 | `af7ab91796afb9293088423959bc0aedff87312cb1e32ed676b57ea2e6c5934e` | remote receipt only |
| 03-C | 296524800 | `af7ab91796afb9293088423959bc0aedff87312cb1e32ed676b57ea2e6c5934e` | remote receipt only |
| 04-A | 296524800 | `9207c3f50d6ec71cc92bf781829cbc4b1dead2f5b7e6524ab5eac295a98d753a` | remote receipt only |

| Report evidence | Bytes | SHA-256 |
|---|---:|---|
| remote-export.json | 34374 | `c4ca081271252f406ca8969e22497d573aa3282550343317945534528f4436cb` |
| compact-evidence.zip | 1772745 | `d5ca6c0cc49387d154644df2c85326f586a9706c632737657a5a94931df01a34` |

Report preparation is saved-output postprocessing in the same assistant session. It performs no scientific propagation, does not fit phases or normalize states, and is not an independent laboratory or numerical replication.
