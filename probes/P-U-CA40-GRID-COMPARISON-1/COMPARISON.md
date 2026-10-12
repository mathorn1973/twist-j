# Local-window N256 / N512 comparison

PUBLIC NON-CANONICAL. Conditional L1 engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.

The short comparison is complete: runtime improved, while the preregistered
2x local-bound-growth budget failed. No new propagation or physical experiment
is performed by this report.

Source pin: `ea8bff874876c1b6f902409888e4e98fb7716066`. Recorded campaign status: **COMPLETE_LOCAL_COMPARISON_COMPATIBLE**.
Completed propagation children: 6/6. Recorded total campaign wall time: 636.480284624 s.

## Scope

The pulses, exact model, seven modes, L8/G10 spaces and 120 thermal basis columns are fixed. Both angles use four disjoint windows per case. Each window resets its computational input to a unit thermal basis vector in the moving linear frame. Physically this corresponds to U_L(t0)|n>, not to resetting the original bath in the laboratory frame and not to the actual nonlinear state reached at that time.

Full analytic linear history is retained. N256 uses two cells and N512 four cells over the same 48.828125 ns window. These are local certificates only: the four reset windows cannot be added into a whole-pulse certificate. No final coherences or full-channel accuracy claim follow from this comparison.

## All propagation timings

| Run | N | Preparation (s) | Kernel (s) | Program end-to-end (s) | Child wall (s) |
|---:|---:|---:|---:|---:|---:|
| 1 | 512 | 44.1754015908 | 70.1913684122 | 116.650410205 | 116.716870178 |
| 2 | 256 | 23.4431394339 | 35.846228037 | 61.6014711559 | 61.6679535452 |
| 3 | 256 | 26.204867024 | 35.4757743292 | 63.9651312381 | 64.0466932636 |
| 4 | 512 | 44.995435236 | 69.3292606249 | 116.610736052 | 116.669018297 |
| 5 | 512 | 45.0427796803 | 69.8208235372 | 117.138982631 | 117.206530144 |
| 6 | 256 | 23.5466027409 | 35.3640397452 | 61.1928524785 | 61.2441373598 |

Preparation includes model preparation and fixtures. Kernel time includes the OpenMP region, workspaces and progress logging. Program end-to-end time includes final artifact serialization; child wall time additionally includes process overhead.

| Median over three children | Preparation (s) | Kernel (s) | End-to-end (s) | Child wall (s) |
|---|---:|---:|---:|---:|
| N512 | 44.995435236 | 69.8208235372 | 116.650410205 | 116.716870178 |
| N256 | 23.5466027409 | 35.4757743292 | 61.6014711559 | 61.6679535452 |
| N512/N256 ratio | 1.91090985528× | 1.96812683747× | 1.89363026591× | 1.89266650614× |

No minimum speedup was frozen for this grid comparison. Timing ratios are measurements of this bounded local workload, not forecasts for a complete trajectory.

## Consistency, repeats and the separate growth screen

- Pair 01/02: COMPATIBLE 2880, INCONSISTENT 0, UNRESOLVED 0; growth screen NOT MET (2880/2880 columns exceed 2×).
- Pair 04/03: COMPATIBLE 2880, INCONSISTENT 0, UNRESOLVED 0; growth screen NOT MET (2880/2880 columns exceed 2×).
- Pair 05/06: COMPATIBLE 2880, INCONSISTENT 0, UNRESOLVED 0; growth screen NOT MET (2880/2880 columns exceed 2×).

Same-grid repeat comparisons present: 4/4; all reported artifact comparisons are byte-identical.

For each stored, unnormalized column the comparator encloses the exact dyadic endpoint difference norm by [d_lo,d_hi]. R is the upward-rounded sum of the two local certificate radii. COMPATIBLE means d_hi<=R; INCONSISTENT means d_lo>R; otherwise the decision is UNRESOLVED. Compatibility is an integrity check, not an accuracy guarantee. The distinct engineering screen is the exact dyadic inequality eps256<=2*eps512. Ratios below are descriptive floating values. Displayed numbers use 12 significant digits; saved JSON values govern all decisions.

## First matched pair: summary by angle

Each angle combines its three cases and four reset windows: 12 groups and 1440 local columns. Maxima are taken independently; ratio ranges retain the original N256/N512 pairing of each column. These are not averages.

| Angle | eps512 max | eps256 max | Paired ratio min–max | d_hi max |
|---|---:|---:|---|---:|
| +4π/5 | 2.59954087109e-07 | 3.86867889588e-06 | 9.53158287316–15.8981524705 | 2.28666585271e-06 |
| −4π/5 | 1.97516963939e-07 | 2.98442682176e-06 | 10.5608181897–15.8751514389 | 1.7229730982e-06 |

## Sampled node diagnostics by angle

These fields are diagnostic quadrature quantities. They have no separate continuous-time certificate: the continuum allowance applies to the combined defect. They must not be added again to guard or total. Each displayed maximum and paired-ratio range covers the same 1440 local columns per angle.

| Angle | Diagnostic | N512 max | N256 max | Paired ratio min–max |
|---|---|---:|---:|---|
| +4π/5 | `sampled_time_node_L2` | 2.43663982244e-07 | 3.86364324845e-06 | 15.7117240183–15.9079054894 |
| +4π/5 | `sampled_projection_node_L2` | 1.34633006367e-07 | 1.37002089678e-07 | 1.00422003112–1.05052978506 |
| +4π/5 | `sampled_arithmetic_node_L2` | 1.98175433892e-13 | 1.98188189191e-13 | 0.999929593108–1.00010727743 |
| −4π/5 | `sampled_time_node_L2` | 1.88237127716e-07 | 2.98118635797e-06 | 15.7118115569–15.8839631606 |
| −4π/5 | `sampled_projection_node_L2` | 8.52040002035e-08 | 8.63030132742e-08 | 1.00281930154–1.04790443181 |
| −4π/5 | `sampled_arithmetic_node_L2` | 1.61849684349e-13 | 1.61832022067e-13 | 0.99954247303–1.00013773072 |

## First matched pair: 24 window/case groups

Each maximum below is independently taken over all 120 columns in that group. The ratio range uses paired columns, not a ratio of the displayed maxima. Rows use pair 01/02; same-grid byte-repeat evidence is reported above.

| Window | Case / angle / labels | eps512 max | eps256 max | eps256/eps512 range | d_lo range | d_hi range | R max | Growth failures |
|---:|---|---:|---:|---|---|---|---:|---:|
| 0 | 0: +4π/5 (4,3) | 4.7770550509e-08 | 7.38303432446e-07 | 13.2985420039–15.7604811382 | 1.30110715262e-07 to 3.49086311511e-07 | 1.30110715262e-07 to 3.49086311511e-07 | 7.86073982955e-07 | 120/120 |
| 0 | 1: +4π/5 (4,4) | 7.76886781316e-08 | 1.19044948326e-06 | 11.2848828403–15.8278525648 | 2.75867490815e-07 to 6.41840409543e-07 | 2.75867490816e-07 to 6.41840409544e-07 | 1.26813816139e-06 | 120/120 |
| 0 | 2: +4π/5 (1,1) | 7.76886781314e-08 | 1.19044948326e-06 | 11.2848828405–15.8278525648 | 2.75867490815e-07 to 6.41840409543e-07 | 2.75867490816e-07 to 6.41840409544e-07 | 1.26813816139e-06 | 120/120 |
| 0 | 3: −4π/5 (4,3) | 3.87953515048e-08 | 6.02606154144e-07 | 14.0132850759–15.7606042682 | 1.06202370424e-07 to 2.84956420958e-07 | 1.06202370424e-07 to 2.84956420959e-07 | 6.41401505649e-07 | 120/120 |
| 0 | 4: −4π/5 (4,4) | 6.30866529436e-08 | 9.71748903183e-07 | 11.8445225082–15.8282262037 | 2.25189355665e-07 to 5.23956663964e-07 | 2.25189355665e-07 to 5.23956663964e-07 | 1.03483555613e-06 | 120/120 |
| 0 | 5: −4π/5 (1,1) | 6.30866529433e-08 | 9.71748903183e-07 | 11.8445225085–15.8282262037 | 2.25189355665e-07 to 5.23956663964e-07 | 2.25189355665e-07 to 5.23956663964e-07 | 1.03483555613e-06 | 120/120 |
| 1 | 0: +4π/5 (4,3) | 1.83978255482e-07 | 2.83075233062e-06 | 12.6305846133–15.7960755771 | 5.73391286716e-07 to 1.49845785344e-06 | 5.73391286717e-07 to 1.49845785344e-06 | 3.0147305861e-06 | 120/120 |
| 1 | 1: +4π/5 (4,4) | 2.59954087109e-07 | 3.86867889588e-06 | 9.53158287316–15.8981524705 | 1.0124760825e-06 to 2.28666585271e-06 | 1.0124760825e-06 to 2.28666585271e-06 | 4.12863298299e-06 | 120/120 |
| 1 | 2: +4π/5 (1,1) | 2.59954087108e-07 | 3.86867889588e-06 | 9.53158287322–15.8981524704 | 1.0124760825e-06 to 2.28666585271e-06 | 1.0124760825e-06 to 2.28666585271e-06 | 4.12863298299e-06 | 120/120 |
| 1 | 3: −4π/5 (4,3) | 1.39302614876e-07 | 2.14579780143e-06 | 12.718866136–15.7923422281 | 4.22735674658e-07 to 1.11503274973e-06 | 4.22735674659e-07 to 1.11503274973e-06 | 2.28510041631e-06 | 120/120 |
| 1 | 4: −4π/5 (4,4) | 1.97516963937e-07 | 2.98442682176e-06 | 10.5608181897–15.8751514389 | 7.45944986545e-07 to 1.7229730982e-06 | 7.45944986546e-07 to 1.7229730982e-06 | 3.18194378569e-06 | 120/120 |
| 1 | 5: −4π/5 (1,1) | 1.97516963939e-07 | 2.98442682175e-06 | 10.5608181898–15.8751514388 | 7.45944986545e-07 to 1.7229730982e-06 | 7.45944986546e-07 to 1.7229730982e-06 | 3.18194378569e-06 | 120/120 |
| 2 | 0: +4π/5 (4,3) | 4.04853609796e-08 | 6.22533750021e-07 | 12.7024947211–15.8187595361 | 1.66330490622e-07 to 3.44958563764e-07 | 1.66330490622e-07 to 3.44958563765e-07 | 6.63019111001e-07 | 120/120 |
| 2 | 1: +4π/5 (4,4) | 2.52635471785e-07 | 3.75292122609e-06 | 10.0659795671–15.8476628287 | 9.75018704472e-07 to 2.09978700697e-06 | 9.75018704473e-07 to 2.09978700697e-06 | 4.00555669787e-06 | 120/120 |
| 2 | 2: +4π/5 (1,1) | 2.52635471784e-07 | 3.75292122609e-06 | 10.0659795669–15.8476628287 | 9.75018704472e-07 to 2.09978700697e-06 | 9.75018704473e-07 to 2.09978700697e-06 | 4.00555669787e-06 | 120/120 |
| 2 | 3: −4π/5 (4,3) | 3.10658145295e-08 | 4.78305668894e-07 | 13.0172475412–15.8061591517 | 1.23444956156e-07 to 2.5833488134e-07 | 1.23444956157e-07 to 2.5833488134e-07 | 5.09356248051e-07 | 120/120 |
| 2 | 4: −4π/5 (4,4) | 1.88883874547e-07 | 2.83864467172e-06 | 10.7894450086–15.8439596948 | 7.3613645816e-07 to 1.57057122037e-06 | 7.36136458161e-07 to 1.57057122037e-06 | 3.02752854626e-06 | 120/120 |
| 2 | 5: −4π/5 (1,1) | 1.88883874547e-07 | 2.83864467172e-06 | 10.7894450084–15.8439596949 | 7.3613645816e-07 to 1.57057122037e-06 | 7.36136458161e-07 to 1.57057122037e-06 | 3.02752854627e-06 | 120/120 |
| 3 | 0: +4π/5 (4,3) | 6.70506945215e-08 | 1.00273714022e-06 | 10.1473409803–15.8552840288 | 2.58933265204e-07 to 5.82572648202e-07 | 2.58933265204e-07 to 5.82572648202e-07 | 1.06978783474e-06 | 120/120 |
| 3 | 1: +4π/5 (4,4) | 7.31144152421e-08 | 1.08809857471e-06 | 10.5231951464–15.83724146 | 2.8444573762e-07 to 6.13003387413e-07 | 2.84445737621e-07 to 6.13003387413e-07 | 1.16121298996e-06 | 120/120 |
| 3 | 2: +4π/5 (1,1) | 7.31144152452e-08 | 1.08809857472e-06 | 10.5231951458–15.8372414589 | 2.8444573762e-07 to 6.13003387413e-07 | 2.84445737621e-07 to 6.13003387413e-07 | 1.16121298996e-06 | 120/120 |
| 3 | 3: −4π/5 (4,3) | 5.42283482425e-08 | 8.18520444517e-07 | 10.7079216259–15.8556057291 | 2.11371149316e-07 to 4.75571164768e-07 | 2.11371149316e-07 to 4.75571164768e-07 | 8.7274879276e-07 | 120/120 |
| 3 | 4: −4π/5 (4,4) | 5.9075235791e-08 | 8.88329496014e-07 | 11.1265440715–15.8375320852 | 2.32217544359e-07 to 5.00468542838e-07 | 2.32217544359e-07 to 5.00468542839e-07 | 9.47404731805e-07 | 120/120 |
| 3 | 5: −4π/5 (1,1) | 5.90752357934e-08 | 8.88329496016e-07 | 11.1265440708–15.8375320841 | 2.32217544359e-07 to 5.00468542838e-07 | 2.32217544359e-07 to 5.00468542839e-07 | 9.4740473181e-07 | 120/120 |

## Local component maxima

Each cell shows **N512 → N256**, with each maximum independently taken over 120 columns. Guard includes the finite-space residual; tail bounds omitted guard space; continuum is the analytic inter-node allowance; jumps account for polynomial endpoint discrepancies. Maximum norm error is a diagnostic. These quantities are neither gate infidelities nor standalone complete-pulse error components.

| Window | Case | Guard | Tail | Continuum | Jumps | Maximum norm error |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 4.75251774518e-08 → 7.38054616778e-07 | 3.14971911439e-10 → 3.19793692586e-10 | 6.50793049102e-13 → 1.03415014824e-12 | 1.375398974e-14 → 6.87738116812e-15 | 1.08608677607e-11 → 2.44429587681e-10 |
| 0 | 1 | 7.69742805466e-08 → 1.18972254887e-06 | 1.01457982472e-09 → 1.03513792872e-09 | 1.3068038198e-12 → 2.06670796062e-12 | 1.37548897277e-14 → 6.87853668653e-15 | 4.57476279081e-11 → 1.30431532241e-09 |
| 0 | 2 | 7.69742805463e-08 → 1.18972254887e-06 | 1.01457982472e-09 → 1.03513792872e-09 | 1.3068038198e-12 → 2.06670796062e-12 | 1.37548854708e-14 → 6.87855655218e-15 | 4.57487381311e-11 → 1.30431598855e-09 |
| 0 | 3 | 3.86168399024e-08 → 6.02425445055e-07 | 2.24772887572e-10 → 2.27755140757e-10 | 5.31151714513e-13 → 8.4256894507e-13 | 1.375392974e-14 → 6.87726610195e-15 | 8.0613293818e-12 → 1.63717706059e-10 |
| 0 | 4 | 6.25801927737e-08 → 9.71234482025e-07 | 7.0452071076e-10 → 7.17399305237e-10 | 1.06628965556e-12 → 1.68216408498e-12 | 1.37546825438e-14 → 6.87822770905e-15 | 3.13029602239e-11 → 8.70089778005e-10 |
| 0 | 5 | 6.25801927734e-08 → 9.71234482025e-07 | 7.04520710758e-10 → 7.17399305237e-10 | 1.06628965556e-12 → 1.68216408498e-12 | 1.37546768665e-14 → 6.87821863546e-15 | 3.13007397779e-11 → 8.70091332317e-10 |
| 1 | 0 | 1.8247530961e-07 → 2.8292136185e-06 | 2.0646965112e-09 → 2.11715971446e-09 | 1.80318272037e-12 → 3.03655184724e-12 | 1.37566562554e-14 → 6.8819619779e-15 | 2.87644352781e-10 → 8.58551763017e-09 |
| 1 | 1 | 2.55824322907e-07 → 3.86443995674e-06 | 6.46254156277e-09 → 6.65894244663e-09 | 3.8795021518e-12 → 6.49251411198e-12 | 1.37676111646e-14 → 6.8936027251e-15 | 1.00849795182e-09 → 3.08189536113e-08 |
| 1 | 2 | 2.55824322906e-07 → 3.86443995674e-06 | 6.46254156278e-09 → 6.65894244663e-09 | 3.8795021518e-12 → 6.49251411198e-12 | 1.3768074892e-14 → 6.89326615673e-15 | 1.00849906204e-09 → 3.08189491705e-08 |
| 1 | 3 | 1.38294308056e-07 → 2.14476732239e-06 | 1.37087980987e-09 → 1.40293137345e-09 | 1.4469724183e-12 → 2.40415449029e-12 | 1.37556991551e-14 → 6.88037057389e-15 | 1.45118805861e-10 → 4.27351887211e-09 |
| 1 | 4 | 1.94767923388e-07 → 2.98161020152e-06 | 4.22652278953e-09 → 4.34486783734e-09 | 3.06580154143e-12 → 5.0448547645e-12 | 1.37625873698e-14 → 6.8875185681e-15 | 4.95255392252e-10 → 1.50219121586e-08 |
| 1 | 5 | 1.9476792339e-07 → 2.98161020152e-06 | 4.22652278954e-09 → 4.34486783734e-09 | 3.06580154143e-12 → 5.0448547645e-12 | 1.37625883889e-14 → 6.88736767654e-15 | 4.95258944966e-10 → 1.50219179318e-08 |
| 2 | 0 | 4.02053530304e-08 → 6.22250069027e-07 | 3.95052937057e-10 → 4.0120293882e-10 | 7.41310808284e-13 → 1.18195349362e-12 | 1.37543102813e-14 → 6.87798358577e-15 | 2.13988826658e-11 → 5.79813308477e-10 |
| 2 | 1 | 2.48602323959e-07 → 3.7487834827e-06 | 6.03055654225e-09 → 6.20427504847e-09 | 3.62318519612e-12 → 6.11807132906e-12 | 1.3758605403e-14 → 6.88398409072e-15 | 6.46218634159e-10 → 1.96116558548e-08 |
| 2 | 2 | 2.48602323958e-07 → 3.7487834827e-06 | 6.03055654225e-09 → 6.20427504847e-09 | 3.62318519612e-12 → 6.11807132906e-12 | 1.37586123117e-14 → 6.88402148596e-15 | 6.46219966427e-10 → 1.96116527462e-08 |
| 2 | 3 | 3.08598135807e-08 → 4.78103504928e-07 | 2.74022386388e-10 → 2.77654025177e-10 | 5.94218211065e-13 → 9.41807764017e-13 | 1.37540856545e-14 → 6.87758263999e-15 | 1.16990861443e-11 → 2.82932788309e-10 |
| 2 | 4 | 1.86162713849e-07 → 2.83585744981e-06 | 3.99867420731e-09 → 4.10624539888e-09 | 2.90575352991e-12 → 4.83127940396e-12 | 1.3757247001e-14 → 6.88209521112e-15 | 3.55593554602e-10 → 1.07361575186e-08 |
| 2 | 5 | 1.8616271385e-07 → 2.83585744982e-06 | 3.99867420732e-09 → 4.10624539889e-09 | 2.90575352991e-12 → 4.83127940396e-12 | 1.37572370363e-14 → 6.88200517873e-15 | 3.55590668022e-10 → 1.07361568524e-08 |
| 3 | 0 | 6.67918116758e-08 → 1.00247510286e-06 | 3.51568895749e-10 → 3.57097771477e-10 | 6.57565730209e-13 → 1.03429368428e-12 | 1.37548956567e-14 → 6.87860433863e-15 | 4.86339857275e-11 → 1.40180955732e-09 |
| 3 | 1 | 7.24199553118e-08 → 1.08739228955e-06 | 9.99855997072e-10 → 1.01987379711e-09 | 1.30780827525e-12 → 2.07075569159e-12 | 1.37548770643e-14 → 6.8786587944e-15 | 5.14379649985e-11 → 1.48755407992e-09 |
| 3 | 2 | 7.24199553149e-08 → 1.08739228955e-06 | 9.99855997074e-10 → 1.01987379712e-09 | 1.30780827525e-12 → 2.07075569159e-12 | 1.37548235384e-14 → 6.87864086292e-15 | 5.14355225079e-11 → 1.48755296969e-09 |
| 3 | 3 | 5.4039709719e-08 → 8.18329833963e-07 | 2.49924312521e-10 → 2.53287057254e-10 | 5.36536636212e-13 → 8.42161360052e-13 | 1.37546878427e-14 → 6.87827768261e-15 | 3.32427418925e-11 → 9.35130195501e-10 |
| 3 | 4 | 5.85821237398e-08 → 8.87828898936e-07 | 6.95670170501e-10 → 7.08244903429e-10 | 1.06700438049e-12 → 1.68494437719e-12 | 1.3754627785e-14 → 6.87831388859e-15 | 3.50894868717e-11 → 9.92321558257e-10 |
| 3 | 5 | 5.85821237422e-08 → 8.87828898938e-07 | 6.95670170503e-10 → 7.08244903437e-10 | 1.06700438049e-12 → 1.68494437719e-12 | 1.37546309404e-14 → 6.87831697491e-15 | 3.50910411839e-11 → 9.9232022599e-10 |

## Report inputs

This renderer reads the preserved JSON evidence only. It does not import the scientific source, propagate a state, or recompute the interval endpoint norm. It checks inventories, saved comparisons, total-bound agreement, exact dyadic growth decisions and timing medians. It is postprocessing in the same assistant session, not an independent scientific replication.

| File under comparison/ | Bytes | SHA-256 |
|---|---:|---|
| summary.json | 6106 | `4866798b288cdb756b207bf5defbe7018e0047227dc047cc2fd320f7a70d7a11` |
| compare-01-02.json | 612511 | `f16a189f4fc595c9c5dd7cca70d72bdafdd58d7bdf5d7d6bde18b5d3fd9e7ac1` |
| compare-01-02-screen.json | 149893 | `79ed8d15130848b62e4c118406a0fd61b44b1e95e5bff92bbfbe689da408456e` |

Protected-source preservation remains conditional on the stated zero-response model. This local numerical comparison supplies no physical admission and does not remove the full-source obstruction for an informative contact.

## Runtime and evidence custody

The public source pin is `ea8bff874876c1b6f902409888e4e98fb7716066`.
All thirteen sources plus SOURCE_SHA256SUMS were publicly compared byte for
byte before execution, at 2026-10-11T16:05:12.942240 UTC. The unchanged input
JSON has SHA-256 `ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`.
Its exact-decimal serialized input has 3918 bytes and SHA-256
`720f167680bbb51549165a10ba04ce9688de43cc67bb4087cd4ce5be20ebb471`.

Execution used Debian GNU/Linux 13, x86_64, Python 3.13.5, GNU C++ 14.2.0,
MPFR 4.2.2 and GMP 6.3.0. Both binaries used the frozen flags
`-O3 -std=c++20 -fopenmp -ffp-contract=off -fno-fast-math -fno-tree-vectorize`.
The explicit AVX-512 implementation processes eight thermal lanes.
Every child verified all eighty distinct worker/CPU/place assignments,
both SMT siblings of forty physical cores on two packages, singleton places,
disabled dynamic teams/nested parallelism and zero observed start/end
migrations. This panel is not a new AVX2/AVX512 or forty/eighty-thread test.

The 340392-byte benchmark binary has SHA-256
`44b377f6258e8c86ff8f8ba59edfb1c3dbcdb2801a8729d51b01906f731b19c2`;
the 365816-byte comparator has SHA-256
`1575609fb574d56374dee84c6e92f26164345b4c8157b3d4cce4fd50e42f3f2e`.
All runtime directed-arithmetic/underflow, displacement, adjoint and ball
enclosure fixtures passed. Every attempted child and comparator exited zero
with empty stderr. Source, serialized-input, executable and comparison
artifact custody passed. No normalization or phase fitting was used.

The private compact archive has 1816976 bytes and SHA-256
`f352ff3f8472e1c52e749b22c16f3ccdd0710a69325e48577e4428fee2e85d9f`.
Its manifest binds 120 records: 114 are included, together with the manifest;
six 296524800-byte endpoint files remain separately retained. All six raw
component files are included. All compact entries were checked by byte count
and SHA-256 after transfer. Local output-only review rechecked components,
screen decisions, classifications and available repeated payload bytes.
It did not independently repropagate states or recompute the full endpoint
distance intervals. Endpoint byte-repeat checks were performed by the pinned
remote runner and their receipts are retained. This is a same-session audit,
not an independent external replication.

The runner's 636.4802846238017-second wall time includes preparation,
propagation, serialization, validation, custody and the three endpoint
comparisons. Program timings in the table omit the runner's validation and
custody work. Three repetitions provide no confidence interval or forecast
for a complete campaign. No observation or warmup was discarded.

Post-run checks at 2026-10-11T16:17:11.305861 UTC found no live campaign
process, clean pinned sources and unchanged binaries. No full trajectory,
retry or longer successor run was started. The local result remains sealed
with the negative engineering screen explicitly retained.
