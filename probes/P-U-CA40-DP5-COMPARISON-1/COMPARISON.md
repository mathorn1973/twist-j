# Local-window DP5 / RK4 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-11.
Prepared from preserved evidence only; no new propagation.

Source pin: `09dde450cfcb9386262afbd0b790250bd3c1bb4a`. Recorded status: **COMPLETE_LOCAL_COMPARISON_COMPATIBLE**. Completed children: **6/6**.

Recorded campaign wall time: 633.937496187 s. Any saved failure remains a failure; no missing output is treated as a certificate.

| Frozen engineering decision | Saved outcome |
|---|---|
| `candidate_reference_bound_screen_pass` | `False` |
| `candidate_reference_speed_screen_pass` | `True` |
| `joint_engineering_screen_pass` | `False` |

## Scope and interpretation

A is RK4 N512, B is RK4 N256, and C is two consecutive DP5 halfsteps per N256 certificate cell. All arms retain the same pulses, exact model, seven modes, L8/G10, 120 thermal basis columns, both angles, and four 48.828125 ns windows per case. Each window starts from its own unit basis vector in the moving full-linear frame while retaining the absolute clock and full analytic linear history. Its physical initial state is U_L(t0)|n>, not the actual nonlinear state reached at t0.

These are local reset-window certificates. They cannot be summed into a full-pulse bound, and they establish neither a source/reference channel bound nor physical realization. Protected-source identity remains a conditional property of the stated dark-source model. The informative-contact full-source obstruction is unchanged.

The primary accuracy-budget screen is eps_C <= eps_A on all 2880 columns of each matched A/C pair. The speed screen is the strict inequality between exact sums of the two observed C and A program end-to-end times. These compare certificate upper bounds and measured costs, not actual integration errors. A failure does not authorize a longer run. The frozen limits are 300 s per child, 90 s per comparator, and 1800 s for the campaign including its comparisons; bounded cleanup and final preservation can extend the final wall receipt.

## Six propagation timings

| Run | Arm / method / N | Preparation s | Kernel s | Program end-to-end s | Child wall s |
|---:|---|---:|---:|---:|---:|
| 1 | A: RK4, N512 | 44.3867392633 | 69.1133024525 | 115.788455211 | 115.853204342 |
| 2 | B: RK4, N256 | 23.6070747599 | 35.1452807877 | 61.0711899828 | 61.1377523243 |
| 3 | C: DP5 two halfsteps, N256 | 27.3169687614 | 37.8779728971 | 67.4844706059 | 67.5449632145 |
| 4 | C: DP5 two halfsteps, N256 | 27.0349769853 | 37.3551042024 | 66.678616643 | 66.7152621225 |
| 5 | B: RK4, N256 | 56.0706670303 | 35.4629682805 | 93.8236964699 | 93.8932391163 |
| 6 | A: RK4, N512 | 44.7696374748 | 70.0653738305 | 117.11814918 | 117.186739709 |

Preparation includes model preparation and fixtures. Kernel time includes workspace setup, the OpenMP region and progress logging. Program end-to-end also includes artifact serialization; child wall additionally includes process overhead. A/B/C use respectively 4/2/2 certificate cells, 4/2/4 integrator substeps, and 36/18/26 right-hand-side evaluations per window.

| Arm, two-observation median | Preparation s | Kernel s | End-to-end s | Child wall s |
|---|---:|---:|---:|---:|
| A | 44.5781883691 | 69.5893381415 | 116.453302195 | 116.519972025 |
| B | 39.8388708951 | 35.3041245341 | 77.4474432264 | 77.5154957203 |
| C | 27.1759728733 | 37.6165385498 | 67.0815436244 | 67.1301126685 |
| A/C | 1.64035299037x | 1.8499665526x | 1.73599616084x | 1.73573330051x |
| B/C | 1.46595932667x | 0.938526666599x | 1.15452684959x | 1.15470528261x |
| A/B | 1.11896214344x | 1.97113903998x | 1.50364295249x | 1.50318295642x |

A median of two observations is their arithmetic mean. These are descriptive measurements of this workload, with no confidence interval or statistical-significance claim and no extrapolation to a complete trajectory.

Arm B's second preparation lasted 56.07066703028977 seconds versus 23.60707475990057 on its first observation. Both are retained; no cause is established by this panel. This variation materially affects B's end-to-end median and its B/C ratio. Its kernel timings remain close. The primary A/C observations are shown individually above.

## Saved endpoint comparisons and repeats

| Matched runs | Arms | Compatible | Inconsistent | Unresolved | Right eps > left eps |
|---|---|---:|---:|---:|---:|
| 1/2 | A/B | 2880 | 0 | 0 | 2880 |
| 1/3 | A/C | 2880 | 0 | 0 | 2 |
| 2/3 | B/C | 2880 | 0 | 0 | 0 |
| 6/5 | A/B | 2880 | 0 | 0 | 2880 |
| 6/4 | A/C | 2880 | 0 | 0 | 2 |
| 5/4 | B/C | 2880 | 0 | 0 | 0 |

Same-arm repeat receipts: 3/3. Their preserved outcomes:

- Arm C, 3/4: all five recorded artifact comparisons agree byte for byte.
- Arm B, 2/5: all five recorded artifact comparisons agree byte for byte.
- Arm A, 1/6: all five recorded artifact comparisons agree byte for byte.

The remote runner compares actual endpoint bytes. The compact archive omits the large endpoint bodies, retaining their receipts; this local report does not independently repeat that endpoint byte comparison or recompute its distance enclosure. Raw component bodies are included and are read directly for the tables below. For saved [d_lo,d_hi] and the upward eps sum R, COMPATIBLE means d_hi <= R, INCONSISTENT means d_lo > R, and the remainder is UNRESOLVED. Compatibility is a certificate-consistency check, not a proof that the actual error is small.

## First triplet: both angles

Each angle contains 1440 local columns. Bounds/ranges are displayed outward from saved binary64 values; descriptive ratios and timings use 12 significant digits. Every decision uses the saved exact dyadic numbers. Pair ratios are columnwise ratios, not ratios of independent maxima.

| Angle | A eps max | B eps max | C eps max | C/A range | B/A range | C/B range |
|---|---:|---:|---:|---|---|---|
| +4pi/5 | 2.59954087109E-7 | 0.00000386867889589 | 2.21551915822E-7 | 0.746526504359 .. 1.00116407147 | 9.53158287316 .. 15.8981524705 | 0.0470903854857 .. 0.0974443068269 |
| -4pi/5 | 1.97516963939E-7 | 0.00000298442682176 | 1.68085522137E-7 | 0.747074629629 .. 1.00121078802 | 10.5608181897 .. 15.8751514389 | 0.0471207830028 .. 0.0859843314245 |

## First triplet: 24 window/case groups

Each eps range covers all 120 columns. Tables use the first preserved A/B/C observation; second observations enter the repeat and primary decisions above.

| Window | Case / angle / labels | A eps range | B eps range | C eps range | C/A | B/A | C/B |
|---:|---|---|---|---|---|---|---|
| 0 | 0: +4pi/5 (4,3) | 1.60928325024E-8 .. 4.77705505091E-8 | 2.53443959817E-7 .. 7.38303432446E-7 | 1.50374679512E-8 .. 4.78261588442E-8 | 0.895744007514 .. 1.00116407147 | 13.2985420039 .. 15.7604811382 | 0.0569019478033 .. 0.0689066985421 |
| 0 | 1: +4pi/5 (4,4) | 3.04718118059E-8 .. 7.76886781316E-8 | 4.82053599235E-7 .. 0.00000119044948327 | 2.50430254828E-8 .. 6.93991913309E-8 | 0.794909747198 .. 0.897570011854 | 11.2848828403 .. 15.8278525648 | 0.0502496065765 .. 0.0795373797458 |
| 0 | 2: +4pi/5 (1,1) | 3.04718118059E-8 .. 7.76886781314E-8 | 4.82053599235E-7 .. 0.00000119044948327 | 2.50430254799E-8 .. 6.93991913290E-8 | 0.794909747140 .. 0.897570011822 | 11.2848828405 .. 15.8278525648 | 0.0502496065727 .. 0.0795373797414 |
| 0 | 3: -4pi/5 (4,3) | 1.31350574326E-8 .. 3.87953515049E-8 | 2.06862941538E-7 .. 6.02606154144E-7 | 1.22745587054E-8 .. 3.88423244518E-8 | 0.895877813047 .. 1.00121078802 | 14.0132850759 .. 15.7606042682 | 0.0568950585637 .. 0.0646780619000 |
| 0 | 4: -4pi/5 (4,4) | 2.48738906768E-8 .. 6.30866529437E-8 | 3.93502247249E-7 .. 9.71748903183E-7 | 2.04512150860E-8 .. 5.63081724571E-8 | 0.795335179290 .. 0.892552859119 | 11.8445225082 .. 15.8282262037 | 0.0502662319461 .. 0.0748929264718 |
| 0 | 5: -4pi/5 (1,1) | 2.48738906767E-8 .. 6.30866529434E-8 | 3.93502247250E-7 .. 9.71748903184E-7 | 2.04512150840E-8 .. 5.63081724555E-8 | 0.795335179233 .. 0.892552859098 | 11.8445225085 .. 15.8282262037 | 0.0502662319423 .. 0.0748929264679 |
| 1 | 0: +4pi/5 (4,3) | 6.41995669719E-8 .. 1.83978255483E-7 | 0.00000101388534975 .. 0.00000283075233063 | 5.40204703316E-8 .. 1.67865374183E-7 | 0.820938395296 .. 0.912419642973 | 12.6305846133 .. 15.7960755771 | 0.0521504787849 .. 0.0695696093457 |
| 1 | 1: +4pi/5 (4,4) | 1.03151157637E-7 .. 2.59954087109E-7 | 0.00000163914381296 .. 0.00000386867889589 | 8.08034691876E-8 .. 2.18890408358E-7 | 0.774961292755 .. 0.928798486038 | 9.53158287316 .. 15.8981524705 | 0.0488293053494 .. 0.0974443068269 |
| 1 | 2: +4pi/5 (1,1) | 1.03151157637E-7 .. 2.59954087108E-7 | 0.00000163914381296 .. 0.00000386867889588 | 8.08034691808E-8 .. 2.18890408349E-7 | 0.774961292690 .. 0.928798486028 | 9.53158287322 .. 15.8981524704 | 0.0488293053456 .. 0.0974443068252 |
| 1 | 3: -4pi/5 (4,3) | 4.81677172342E-8 .. 1.39302614877E-7 | 7.60464862145E-7 .. 0.00000214579780144 | 4.14293347432E-8 .. 1.29359207749E-7 | 0.836561320882 .. 0.928620097071 | 12.7188661360 .. 15.7923422281 | 0.0531504538828 .. 0.0697168168687 |
| 1 | 4: -4pi/5 (4,4) | 7.75972474196E-8 .. 1.97516963937E-7 | 0.00000123130674614 .. 0.00000298442682176 | 6.10976753548E-8 .. 1.68085522137E-7 | 0.776193492100 .. 0.908064891338 | 10.5608181897 .. 15.8751514389 | 0.0489593712865 .. 0.0859843314245 |
| 1 | 5: -4pi/5 (1,1) | 7.75972474208E-8 .. 1.97516963939E-7 | 0.00000123130674614 .. 0.00000298442682176 | 6.10976753510E-8 .. 1.68085522132E-7 | 0.776193492072 .. 0.908064891324 | 10.5608181898 .. 15.8751514388 | 0.0489593712851 .. 0.0859843314224 |
| 2 | 0: +4pi/5 (4,3) | 1.79528358591E-8 .. 4.04853609797E-8 | 2.83923345848E-7 .. 6.22533750022E-7 | 1.44512565854E-8 .. 3.54882664487E-8 | 0.787292915094 .. 0.876570335300 | 12.7024947211 .. 15.8187595361 | 0.0498666653550 .. 0.0677342813192 |
| 2 | 1: +4pi/5 (4,4) | 1.03610939194E-7 .. 2.52635471786E-7 | 0.00000164133386743 .. 0.00000375292122609 | 8.20501457235E-8 .. 2.21551915819E-7 | 0.776837708376 .. 0.914992601200 | 10.0659795671 .. 15.8476628287 | 0.0490837124481 .. 0.0908995090945 |
| 2 | 2: +4pi/5 (1,1) | 1.03610939194E-7 .. 2.52635471784E-7 | 0.00000164133386743 .. 0.00000375292122609 | 8.20501457247E-8 .. 2.21551915822E-7 | 0.776837708396 .. 0.914992601179 | 10.0659795669 .. 15.8476628287 | 0.0490837124490 .. 0.0908995090938 |
| 2 | 3: -4pi/5 (4,3) | 1.36783375684E-8 .. 3.10658145296E-8 | 2.16125869927E-7 .. 4.78305668895E-7 | 1.14042803007E-8 .. 2.80559144672E-8 | 0.811487073418 .. 0.903555271070 | 13.0172475412 .. 15.8061591517 | 0.0514156156895 .. 0.0666529735002 |
| 2 | 4: -4pi/5 (4,4) | 7.88544592703E-8 .. 1.88883874547E-7 | 0.00000124879301319 .. 0.00000283864467172 | 6.29378554895E-8 .. 1.66742690464E-7 | 0.780835678308 .. 0.901915924686 | 10.7894450086 .. 15.8439596948 | 0.0493310964532 .. 0.0835924298211 |
| 2 | 5: -4pi/5 (1,1) | 7.88544592702E-8 .. 1.88883874548E-7 | 0.00000124879301319 .. 0.00000283864467173 | 6.29378554891E-8 .. 1.66742690466E-7 | 0.780835678324 .. 0.901915924658 | 10.7894450084 .. 15.8439596949 | 0.0493310964539 .. 0.0835924298200 |
| 3 | 0: +4pi/5 (4,3) | 2.73656813362E-8 .. 6.70506945215E-8 | 4.33782669654E-7 .. 0.00000100273714022 | 2.10008044180E-8 .. 5.51225565341E-8 | 0.746526504359 .. 0.902039057676 | 10.1473409803 .. 15.8552840288 | 0.0470903854857 .. 0.0888941309284 |
| 3 | 1: +4pi/5 (4,4) | 3.08271986823E-8 .. 7.31144152422E-8 | 4.87976306979E-7 .. 0.00000108809857472 | 2.47210508086E-8 .. 6.45921206398E-8 | 0.776333906298 .. 0.902708525171 | 10.5231951464 .. 15.8372414600 | 0.0490348977528 .. 0.0857827411364 |
| 3 | 2: +4pi/5 (1,1) | 3.08271986852E-8 .. 7.31144152452E-8 | 4.87976306982E-7 .. 0.00000108809857472 | 2.47210508135E-8 .. 6.45921206451E-8 | 0.776333906359 .. 0.902708525222 | 10.5231951458 .. 15.8372414589 | 0.0490348977598 .. 0.0857827411463 |
| 3 | 3: -4pi/5 (4,3) | 2.23389858565E-8 .. 5.42283482426E-8 | 3.54108255278E-7 .. 8.18520444518E-7 | 1.71534778277E-8 .. 4.44089556780E-8 | 0.747074629629 .. 0.890593907384 | 10.7079216259 .. 15.8556057291 | 0.0471207830028 .. 0.0831715003615 |
| 3 | 4: -4pi/5 (4,4) | 2.51687055057E-8 .. 5.90752357910E-8 | 3.98408829102E-7 .. 8.88329496015E-7 | 2.01935452563E-8 .. 5.21351943591E-8 | 0.776780943136 .. 0.895851535157 | 11.1265440715 .. 15.8375320852 | 0.0490562741669 .. 0.0800731655784 |
| 3 | 5: -4pi/5 (1,1) | 2.51687055081E-8 .. 5.90752357935E-8 | 3.98408829104E-7 .. 8.88329496017E-7 | 2.01935452604E-8 .. 5.21351943629E-8 | 0.776780943197 .. 0.895851535185 | 11.1265440708 .. 15.8375320841 | 0.0490562741739 .. 0.0800731655862 |

## Local components

Each entry is the independent maximum **A / B / C** over the 120 columns. Guard already includes arithmetic balls; tail bounds omitted guard space; continuum covers inter-node defect; jumps cover stored polynomial endpoint discrepancies. These maxima are neither additive across columns nor infidelities.

| Window | Case | Guard | Tail | Continuum | Jumps |
|---:|---:|---|---|---|---|
| 0 | 0 | 4.75251774519E-8 / 7.38054616778E-7 / 4.75780852280E-8 | 3.14971911439E-10 / 3.19793692587E-10 / 3.19455320382E-10 | 6.50793049103E-13 / 1.03415014825E-12 / 1.03337116020E-12 | 1.37539897400E-14 / 6.87738116813E-15 / 6.87839739599E-15 |
| 0 | 1 | 7.69742805466E-8 / 0.00000118972254887 / 6.86743246055E-8 | 1.01457982473E-9 / 1.03513792873E-9 / 1.03405099662E-9 | 1.30680381981E-12 / 2.06670796062E-12 / 2.06540953888E-12 | 1.37548897277E-14 / 6.87853668653E-15 / 6.88030490602E-15 |
| 0 | 2 | 7.69742805464E-8 / 0.00000118972254887 / 6.86743246034E-8 | 1.01457982473E-9 / 1.03513792873E-9 / 1.03405099662E-9 | 1.30680381981E-12 / 2.06670796062E-12 / 2.06540953888E-12 | 1.37548854708E-14 / 6.87855655219E-15 / 6.88031327945E-15 |
| 0 | 3 | 3.86168399025E-8 / 6.02425445056E-7 / 3.86621104156E-8 | 2.24772887573E-10 / 2.27755140758E-10 / 2.27529267098E-10 | 5.31151714514E-13 / 8.42568945071E-13 / 8.41946119128E-13 | 1.37539297400E-14 / 6.87726610195E-15 / 6.87787092013E-15 |
| 0 | 4 | 6.25801927737E-8 / 9.71234482025E-7 / 5.57951371852E-8 | 7.04520710760E-10 / 7.17399305238E-10 / 7.16669033050E-10 | 1.06628965557E-12 / 1.68216408498E-12 / 1.68114309520E-12 | 1.37546825439E-14 / 6.87822770906E-15 / 6.87969403283E-15 |
| 0 | 5 | 6.25801927735E-8 / 9.71234482026E-7 / 5.57951371834E-8 | 7.04520710758E-10 / 7.17399305237E-10 / 7.16669033049E-10 | 1.06628965557E-12 / 1.68216408498E-12 / 1.68114309520E-12 | 1.37546768666E-14 / 6.87821863546E-15 / 6.87979827807E-15 |
| 1 | 0 | 1.82475309610E-7 / 0.00000282921361851 / 1.66331889695E-7 | 2.06469651121E-9 / 2.11715971447E-9 / 2.11471758367E-9 | 1.80318272037E-12 / 3.03655184724E-12 / 3.03266057612E-12 | 1.37566562554E-14 / 6.88196197790E-15 / 6.88987981118E-15 |
| 1 | 1 | 2.55824322907E-7 / 0.00000386443995675 / 2.14664906986E-7 | 6.46254156277E-9 / 6.65894244664E-9 / 6.65248205423E-9 | 3.87950215181E-12 / 6.49251411199E-12 / 6.48801489355E-12 | 1.37676111646E-14 / 6.89360272510E-15 / 6.90964118308E-15 |
| 1 | 2 | 2.55824322906E-7 / 0.00000386443995675 / 2.14664906982E-7 | 6.46254156278E-9 / 6.65894244664E-9 / 6.65248205422E-9 | 3.87950215181E-12 / 6.49251411199E-12 / 6.48801489355E-12 | 1.37680748921E-14 / 6.89326615673E-15 / 6.90636367393E-15 |
| 1 | 3 | 1.38294308056E-7 / 0.00000214476732239 / 1.28332275099E-7 | 1.37087980988E-9 / 1.40293137345E-9 / 1.40129047294E-9 | 1.44697241831E-12 / 2.40415449030E-12 / 2.40136995014E-12 | 1.37556991552E-14 / 6.88037057389E-15 / 6.88513857461E-15 |
| 1 | 4 | 1.94767923388E-7 / 0.00000298161020153 / 1.65278077258E-7 | 4.22652278954E-9 / 4.34486783734E-9 / 4.34036465275E-9 | 3.06580154144E-12 / 5.04485476451E-12 / 5.04124402807E-12 | 1.37625873698E-14 / 6.88751856811E-15 / 6.89666393062E-15 |
| 1 | 5 | 1.94767923390E-7 / 0.00000298161020153 / 1.65278077255E-7 | 4.22652278954E-9 / 4.34486783734E-9 / 4.34036465275E-9 | 3.06580154144E-12 / 5.04485476451E-12 / 5.04124402807E-12 | 1.37625883889E-14 / 6.88736767655E-15 / 6.89512611671E-15 |
| 2 | 0 | 4.02053530305E-8 / 6.22250069027E-7 / 3.52052730265E-8 | 3.95052937057E-10 / 4.01202938821E-10 / 4.00800732043E-10 | 7.41310808284E-13 / 1.18195349363E-12 / 1.18128352248E-12 | 1.37543102814E-14 / 6.87798358578E-15 / 6.88094086806E-15 |
| 2 | 1 | 2.48602323960E-7 / 0.00000374878348271 / 2.17427940228E-7 | 6.03055654225E-9 / 6.20427504847E-9 / 6.19692828148E-9 | 3.62318519612E-12 / 6.11807132907E-12 / 6.11239605139E-12 | 1.37586054031E-14 / 6.88398409073E-15 / 6.89424880431E-15 |
| 2 | 2 | 2.48602323958E-7 / 0.00000374878348271 / 2.17427940229E-7 | 6.03055654226E-9 / 6.20427504848E-9 / 6.19692828149E-9 | 3.62318519612E-12 / 6.11807132907E-12 / 6.11239605139E-12 | 1.37586123118E-14 / 6.88402148597E-15 / 6.89300206210E-15 |
| 2 | 3 | 3.08598135807E-8 / 4.78103504929E-7 / 2.78541958040E-8 | 2.74022386388E-10 / 2.77654025178E-10 / 2.77394116100E-10 | 5.94218211065E-13 / 9.41807764018E-13 / 9.41300931408E-13 | 1.37540856545E-14 / 6.87758264000E-15 / 6.87913099783E-15 |
| 2 | 4 | 1.86162713849E-7 / 0.00000283585744982 / 1.63964630891E-7 | 3.99867420732E-9 / 4.10624539889E-9 / 4.10141247137E-9 | 2.90575352992E-12 / 4.83127940396E-12 / 4.82729977493E-12 | 1.37572470011E-14 / 6.88209521112E-15 / 6.88849948539E-15 |
| 2 | 5 | 1.86162713850E-7 / 0.00000283585744982 / 1.63964630892E-7 | 3.99867420732E-9 / 4.10624539889E-9 / 4.10141247138E-9 | 2.90575352992E-12 / 4.83127940396E-12 / 4.82729977493E-12 | 1.37572370364E-14 / 6.88200517874E-15 / 6.88927069369E-15 |
| 3 | 0 | 6.67918116759E-8 / 0.00000100247510287 / 5.48609175246E-8 | 3.51568895750E-10 / 3.57097771478E-10 / 3.56895549830E-10 | 6.57565730210E-13 / 1.03429368429E-12 / 1.03325714078E-12 | 1.37548956567E-14 / 6.87860433864E-15 / 6.88073327018E-15 |
| 3 | 1 | 7.24199553119E-8 / 0.00000108739228955 / 6.38596561141E-8 | 9.99855997073E-10 / 1.01987379712E-9 / 1.01880203935E-9 | 1.30780827525E-12 / 2.07075569160E-12 / 2.06953888686E-12 | 1.37548770643E-14 / 6.87865879441E-15 / 6.88087295130E-15 |
| 3 | 2 | 7.24199553149E-8 / 0.00000108739228956 / 6.38596561190E-8 | 9.99855997074E-10 / 1.01987379713E-9 / 1.01880203936E-9 | 1.30780827525E-12 / 2.07075569160E-12 / 2.06953888686E-12 | 1.37548235385E-14 / 6.87864086292E-15 / 6.88075429160E-15 |
| 3 | 3 | 5.40397097191E-8 / 8.18329833964E-7 / 4.42186120410E-8 | 2.49924312522E-10 / 2.53287057254E-10 / 2.53150496434E-10 | 5.36536636212E-13 / 8.42161360052E-13 / 8.41332260207E-13 | 1.37546878427E-14 / 6.87827768262E-15 / 6.88011818665E-15 |
| 3 | 4 | 5.85821237398E-8 / 8.87828898936E-7 / 5.16170136135E-8 | 6.95670170502E-10 / 7.08244903430E-10 / 7.07526196611E-10 | 1.06700438049E-12 / 1.68494437719E-12 / 1.68398749700E-12 | 1.37546277851E-14 / 6.87831388860E-15 / 6.88012267910E-15 |
| 3 | 5 | 5.85821237423E-8 / 8.87828898938E-7 / 5.16170136175E-8 | 6.95670170503E-10 / 7.08244903437E-10 / 7.07526196619E-10 | 1.06700438049E-12 / 1.68494437719E-12 / 1.68398749700E-12 | 1.37546309405E-14 / 6.87831697491E-15 / 6.88015021239E-15 |

## Node diagnostics by angle

Time/projection node diagnostics have no independent continuum allowance. Arithmetic-node diagnostics are already included in guard and must not be added again. The maximum norm error is diagnostic, not the vector-error bound.

| Angle | Diagnostic | A max | B max | C max |
|---|---|---:|---:|---:|
| +4pi/5 | `sampled_time_node_L2` | 2.43663982245E-7 | 0.00000386364324845 | 2.04227206176E-7 |
| +4pi/5 | `sampled_projection_node_L2` | 1.34633006367E-7 | 1.37002089679E-7 | 1.36887870390E-7 |
| +4pi/5 | `sampled_arithmetic_node_L2` | 1.98175433893E-13 | 1.98188189191E-13 | 1.98188160390E-13 |
| +4pi/5 | `maximum_norm_error` | 1.00849906204E-9 | 3.08189536114E-8 | 1.00131014591E-11 |
| -4pi/5 | `sampled_time_node_L2` | 1.88237127716E-7 | 0.00000298118635797 | 1.57538861024E-7 |
| -4pi/5 | `sampled_projection_node_L2` | 8.52040002036E-8 | 8.63030132743E-8 | 8.62390521188E-8 |
| -4pi/5 | `sampled_arithmetic_node_L2` | 1.61849684349E-13 | 1.61832022067E-13 | 1.61832000743E-13 |
| -4pi/5 | `maximum_norm_error` | 4.95258944966E-10 | 1.50219179318E-8 | 6.05737682236E-12 |

## Build, exact gate, and evidence custody

| Recorded separate stage | Wall seconds | Exit code | Standard output bytes | Standard error bytes |
|---|---:|---:|---:|---:|
| build_baseline | 13.9879290275 | 0 | 0 | 0 |
| build_candidate | 14.4395253342 | 0 | 0 | 0 |
| build_comparator | 14.1890581902 | 0 | 0 | 0 |
| exact | 0.215265857056 | 0 | 963 | 0 |

The saved exact gate reports **PASS**; stdout SHA-256 `621c571e28fcba8f228f8deaf0755407cd9fe7825e128ac5a97a20211226cee7`. This supports the listed algebraic fixtures, not an independent numerical replay or complete trajectory certificate. Any later CI exact replay has the same limited role.

Frozen sources are identified by the public pin. Completed child records passed the runner's source/input/binary custody checks; the recorded campaign status governs any later failure. This renderer authenticates every included archive member against the preserved manifest, but does not reconstruct the remote machine state or certify the solver implementation independently.

| Endpoint artifact | Bytes | SHA-256 | Local payload |
|---|---:|---|---|
| 01-A | 296524800 | `9a566df1502760cfb2a62ea2088a7978ef6fdfac346a2af2d00622f673db76f9` | remote receipt only |
| 02-B | 296524800 | `3df30d25d94054c3c56f24288d8af67c8843df5224651647a75481ee5178e83f` | remote receipt only |
| 03-C | 296524800 | `29a2fd0179d4df76acf64d6cb607bddaa10e210c90145647c8a3ed4efd65b4aa` | remote receipt only |
| 04-C | 296524800 | `29a2fd0179d4df76acf64d6cb607bddaa10e210c90145647c8a3ed4efd65b4aa` | remote receipt only |
| 05-B | 296524800 | `3df30d25d94054c3c56f24288d8af67c8843df5224651647a75481ee5178e83f` | remote receipt only |
| 06-A | 296524800 | `9a566df1502760cfb2a62ea2088a7978ef6fdfac346a2af2d00622f673db76f9` | remote receipt only |

| Report evidence | Bytes | SHA-256 |
|---|---:|---|
| remote-export.json | 47820 | `8ef3298a947a6f3128e01fe0dd2cd06cc978dd19ab768cd2e3191a2c9631b029` |
| compact-evidence.zip | 2250558 | `18e9af0675fab714842c099e1f8999da39a95b5a0d47d6e427984a8a23909316` |

Report preparation is saved-output postprocessing in the same assistant session. It performs no scientific propagation, does not fit phases or normalize states, and is not an independent laboratory or numerical replication.
