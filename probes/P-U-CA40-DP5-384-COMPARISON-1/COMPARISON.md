# Local-window DP5/N384 versus RK4/N512 comparison

PUBLIC NON-CANONICAL. Conditional L1 numerical engineering evidence.
Original record Apache-2.0, A. M. Thorn, 2026-10-12.
Prepared from preserved evidence only; no new propagation.

Source pin: `99625cf6039a4a17334664b00630857bdfa772c3`. Recorded status: **COMPLETE_LOCAL_COMPARISON_COMPATIBLE**. Completed children: **4/4**.

Recorded campaign wall time: 494.195044437 s. Any saved failure remains a failure; no missing output is treated as a certificate.

| Frozen engineering decision | Saved outcome |
|---|---|
| `candidate_reference_bound_screen_pass` | `True` |
| `candidate_reference_speed_screen_pass` | `True` |
| `joint_engineering_screen_pass` | `True` |

## Scope and interpretation

A is inherited RK4 N512 and C is two consecutive DP5 halfsteps per N384 certificate cell. All arms retain the same pulses, exact model, seven modes, L8/G10, 120 thermal basis columns, both angles, and four 48.828125 ns windows per case. Each window starts from its own unit basis vector in the moving full-linear frame while retaining the absolute clock and full analytic linear history. Its physical initial state is U_L(t0)|n>, not the actual nonlinear state reached at t0.

These are local reset-window certificates. They cannot be summed into a full-pulse bound, and they establish neither a source/reference channel bound nor physical realization. Protected-source identity remains a conditional property of the stated dark-source model. The informative-contact full-source obstruction is unchanged.

The primary accuracy-budget screen is eps_C <= eps_A on all 2880 columns of each matched A/C pair. The speed screen is the strict inequality between exact sums of the two observed C and A program end-to-end times. These compare certificate upper bounds and measured costs, not actual integration errors. A failure does not authorize a longer run. The frozen limits are 300 s per child, 90 s per comparator, and 1200 s for the campaign including its comparisons; bounded cleanup and final preservation can extend the final wall receipt.

## Four propagation timings

| Run | Arm / method / N | Preparation s | Kernel s | Program end-to-end s | Child wall s |
|---:|---|---:|---:|---:|---:|
| 1 | A: RK4, N512 | 44.1586175635 | 69.4266897235 | 115.866608433 | 115.907129942 |
| 2 | C: DP5 two halfsteps, N384 | 39.4742563292 | 55.22248815 | 96.9872215334 | 97.0515680071 |
| 3 | C: DP5 two halfsteps, N384 | 39.2359099966 | 55.6319738775 | 97.159049144 | 97.2042618468 |
| 4 | A: RK4, N512 | 44.9557004925 | 70.1882899646 | 117.427208157 | 117.462200522 |

Preparation includes model preparation and fixtures. Kernel time includes workspace setup, the OpenMP region and progress logging. Program end-to-end also includes artifact serialization; child wall additionally includes process overhead. A/C use respectively 4/3 certificate cells, 4/6 integrator substeps, 36/39 right-hand-side evaluations and 64/48 certificate Gauss nodes per window. The two-arm comparison changes method, dense curve, substep count and certificate density together; it cannot isolate their individual effects.

| Arm, two-observation median | Preparation s | Kernel s | End-to-end s | Child wall s |
|---|---:|---:|---:|---:|
| A | 44.557159028 | 69.807489844 | 116.646908295 | 116.684665232 |
| C | 39.3550831629 | 55.4272310138 | 97.0731353387 | 97.127914927 |
| A/C | 1.13218307388x | 1.25944393337x | 1.20163944317x | 1.20135045954x |

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

## The two exposed predecessor exceptions

Both targets are window 0, column 36, occupation (0,0,0,0,0,0,3): case 0 for the positive angle and case 3 for the negative angle. They remain inside the unchanged all-2880-column screen, with no exception or tolerance.

| Fresh matched runs | Angle / labels | A512 eps | C384 eps | C/A | Bound screen | Distance interval | Compatibility |
|---|---|---:|---:|---|---|---|---|
| 1/2 | +4pi/5 (4,3) | 4.77705505091E-8 | 9.75550845913E-9 | 0.204215952196 .. 0.204215952196 | PASS | [2.15147373757E-8, 2.15147373758E-8] | COMPATIBLE |
| 1/2 | -4pi/5 (4,3) | 3.87953515049E-8 | 7.05981472860E-9 | 0.181975789747 .. 0.181975789747 | PASS | [1.75623748114E-8, 1.75623748115E-8] | COMPATIBLE |
| 4/3 | +4pi/5 (4,3) | 4.77705505091E-8 | 9.75550845913E-9 | 0.204215952196 .. 0.204215952196 | PASS | [2.15147373757E-8, 2.15147373758E-8] | COMPATIBLE |
| 4/3 | -4pi/5 (4,3) | 3.87953515049E-8 | 7.05981472860E-9 | 0.181975789747 .. 0.181975789747 | PASS | [1.75623748114E-8, 1.75623748115E-8] | COMPATIBLE |

For exposed context only, the preceding N256 study used source pin `09dde450cfcb9386262afbd0b790250bd3c1bb4a`. Its stored focused bounds were:

| Angle / labels | Previous A512 eps | Previous C256 eps | Previous C256/A512 |
|---|---:|---:|---|
| +4pi/5 (4,3) | 4.77705505091E-8 | 4.78261588442E-8 | 1.00116407147 .. 1.00116407147 |
| -4pi/5 (4,3) | 3.87953515049E-8 | 3.88423244518E-8 | 1.00121078802 .. 1.00121078802 |

These are previously exposed archived values, not a third arm measured in this campaign. They do not replace its fresh A observations or enter acceptance.

| Fresh runs | Case | Guard A/C | Tail A/C | Continuum A/C | Jumps A/C | Time-node A/C | Projection-node A/C | Arithmetic-node A/C |
|---|---:|---|---|---|---|---|---|---|
| 1/2 | 0 | 4.75251774519E-8 / 9.50943452706E-9 | 2.44708586415E-10 / 2.45319947557E-10 | 6.50716840341E-13 / 7.43668511657E-13 | 1.37539471500E-14 / 1.03160110025E-14 | 4.69725016573E-8 / 6.31253535945E-9 | 6.89358640802E-9 / 6.94850274046E-9 | 3.20082377417E-14 / 3.20130273593E-14 |
| 1/2 | 3 | 3.86168399025E-8 / 6.88086919851E-9 | 1.77966756030E-10 / 1.78328453362E-10 | 5.31092467674E-13 / 6.06760841217E-13 | 1.37539031488E-14 / 1.03158939907E-14 | 3.83410735496E-8 / 5.15305468756E-9 | 4.41341705825E-9 / 4.44805018252E-9 | 2.61477196628E-14 / 2.61419460510E-14 |
| 4/3 | 0 | 4.75251774519E-8 / 9.50943452706E-9 | 2.44708586415E-10 / 2.45319947557E-10 | 6.50716840341E-13 / 7.43668511657E-13 | 1.37539471500E-14 / 1.03160110025E-14 | 4.69725016573E-8 / 6.31253535945E-9 | 6.89358640802E-9 / 6.94850274046E-9 | 3.20082377417E-14 / 3.20130273593E-14 |
| 4/3 | 3 | 3.86168399025E-8 / 6.88086919851E-9 | 1.77966756030E-10 / 1.78328453362E-10 | 5.31092467674E-13 / 6.06760841217E-13 | 1.37539031488E-14 / 1.03158939907E-14 | 3.83410735496E-8 / 5.15305468756E-9 | 4.41341705825E-9 / 4.44805018252E-9 | 2.61477196628E-14 / 2.61419460510E-14 |

The separate node diagnostics have no independent continuous-time allowance. Their changes help locate a conservative bound contribution but do not identify the unknown true integration error.

## First matched pair: both angles

Each angle contains 1440 local columns. Bounds/ranges are displayed outward from saved binary64 values; descriptive ratios and timings use 12 significant digits. Every decision uses the saved exact dyadic numbers. Pair ratios are columnwise ratios, not ratios of independent maxima.

| Angle | A eps max | C eps max | Paired C/A range |
|---|---:|---:|---|
| +4pi/5 | 2.59954087109E-7 | 1.42293424995E-7 | 0.100329984289 .. 0.777182388540 |
| -4pi/5 | 1.97516963939E-7 | 9.02059057310E-8 | 0.100159065571 .. 0.731171808534 |

## First matched pair: 24 window/case groups

Each eps range covers all 120 columns. Tables use the first preserved A/C observation; second observations enter the repeat and primary decisions above.

| Window | Case / angle / labels | A eps range | C eps range | Paired C/A |
|---:|---|---|---|---|
| 0 | 0: +4pi/5 (4,3) | 1.60928325024E-8 .. 4.77705505091E-8 | 2.01509241557E-9 .. 1.16673915329E-8 | 0.122409930607 .. 0.516905499029 |
| 0 | 1: +4pi/5 (4,4) | 3.04718118059E-8 .. 7.76886781316E-8 | 3.34320859434E-9 .. 3.20815769029E-8 | 0.107676955048 .. 0.688980988944 |
| 0 | 2: +4pi/5 (1,1) | 3.04718118059E-8 .. 7.76886781314E-8 | 3.34320859014E-9 .. 3.20815768982E-8 | 0.107676954929 .. 0.688980988856 |
| 0 | 3: -4pi/5 (4,3) | 1.31350574326E-8 .. 3.87953515049E-8 | 1.64484741507E-9 .. 7.79510068387E-9 | 0.122410274942 .. 0.441680360829 |
| 0 | 4: -4pi/5 (4,4) | 2.48738906768E-8 .. 6.30866529437E-8 | 2.73019038923E-9 .. 2.36547388287E-8 | 0.107727301611 .. 0.653629340456 |
| 0 | 5: -4pi/5 (1,1) | 2.48738906767E-8 .. 6.30866529434E-8 | 2.73019038577E-9 .. 2.36547388247E-8 | 0.107727301499 .. 0.653629340359 |
| 1 | 0: +4pi/5 (4,3) | 6.41995669719E-8 .. 1.83978255483E-7 | 7.22235458275E-9 .. 4.95016295783E-8 | 0.111040724505 .. 0.551468718021 |
| 1 | 1: +4pi/5 (4,4) | 1.03151157637E-7 .. 2.59954087109E-7 | 1.07681907885E-8 .. 1.42293424986E-7 | 0.103626371218 .. 0.777182388484 |
| 1 | 2: +4pi/5 (1,1) | 1.03151157637E-7 .. 2.59954087108E-7 | 1.07681908010E-8 .. 1.42293424995E-7 | 0.103626371312 .. 0.777182388540 |
| 1 | 3: -4pi/5 (4,3) | 4.81677172342E-8 .. 1.39302614877E-7 | 5.54099498146E-9 .. 3.71578600105E-8 | 0.113370023771 .. 0.550815985076 |
| 1 | 4: -4pi/5 (4,4) | 7.75972474196E-8 .. 1.97516963937E-7 | 8.14663335011E-9 .. 9.02059057235E-8 | 0.104049570729 .. 0.724220903725 |
| 1 | 5: -4pi/5 (1,1) | 7.75972474208E-8 .. 1.97516963939E-7 | 8.14663335944E-9 .. 9.02059057310E-8 | 0.104049570824 .. 0.724220903793 |
| 2 | 0: +4pi/5 (4,3) | 1.79528358591E-8 .. 4.04853609797E-8 | 1.93102235402E-9 .. 1.39108730305E-8 | 0.106312050745 .. 0.563022285246 |
| 2 | 1: +4pi/5 (4,4) | 1.03610939194E-7 .. 2.52635471786E-7 | 1.09462757248E-8 .. 1.31847856863E-7 | 0.104397795798 .. 0.749073454368 |
| 2 | 2: +4pi/5 (1,1) | 1.03610939194E-7 .. 2.52635471784E-7 | 1.09462757381E-8 .. 1.31847856874E-7 | 0.104397795911 .. 0.749073454416 |
| 2 | 3: -4pi/5 (4,3) | 1.36783375684E-8 .. 3.10658145296E-8 | 1.52488992925E-9 .. 9.94354648695E-9 | 0.109891727357 .. 0.535217222678 |
| 2 | 4: -4pi/5 (4,4) | 7.88544592703E-8 .. 1.88883874547E-7 | 8.39786926207E-9 .. 8.92874504481E-8 | 0.105125589955 .. 0.710708067926 |
| 2 | 5: -4pi/5 (1,1) | 7.88544592702E-8 .. 1.88883874548E-7 | 8.39786927268E-9 .. 8.92874504566E-8 | 0.105125590073 .. 0.710708067979 |
| 3 | 0: +4pi/5 (4,3) | 2.73656813362E-8 .. 6.70506945215E-8 | 2.79670865257E-9 .. 3.44665818048E-8 | 0.100329984289 .. 0.759926547275 |
| 3 | 1: +4pi/5 (4,4) | 3.08271986823E-8 .. 7.31144152422E-8 | 3.29888715124E-9 .. 3.76288472702E-8 | 0.104813637305 .. 0.733918451473 |
| 3 | 2: +4pi/5 (1,1) | 3.08271986852E-8 .. 7.31144152452E-8 | 3.29888715579E-9 .. 3.76288472735E-8 | 0.104813637403 .. 0.733918451490 |
| 3 | 3: -4pi/5 (4,3) | 2.23389858565E-8 .. 5.42283482426E-8 | 2.28434238024E-9 .. 2.56384517637E-8 | 0.100159065571 .. 0.731171808534 |
| 3 | 4: -4pi/5 (4,4) | 2.51687055057E-8 .. 5.90752357910E-8 | 2.69470882859E-9 .. 2.77133972539E-8 | 0.104562009738 .. 0.700558740796 |
| 3 | 5: -4pi/5 (1,1) | 2.51687055081E-8 .. 5.90752357935E-8 | 2.69470883227E-9 .. 2.77133972564E-8 | 0.104562009839 .. 0.700558740812 |

## Local components

Each entry is the independent maximum **A / C** over the 120 columns. Guard already includes arithmetic balls; tail bounds omitted guard space; continuum covers inter-node defect; jumps cover stored polynomial endpoint discrepancies. These maxima are neither additive across columns nor infidelities.

| Window | Case | Guard | Tail | Continuum | Jumps |
|---:|---:|---|---|---|---|
| 0 | 0 | 4.75251774519E-8 / 1.13587621162E-8 | 3.14971911439E-10 / 3.16184908904E-10 | 6.50793049103E-13 / 7.43668511657E-13 | 1.37539897400E-14 / 1.03162339784E-14 |
| 0 | 1 | 7.69742805466E-8 / 3.10600530343E-8 | 1.01457982473E-9 / 1.02002282648E-9 | 1.30680381981E-12 / 1.49134521772E-12 | 1.37548897277E-14 / 1.03177422975E-14 |
| 0 | 2 | 7.69742805464E-8 / 3.10600530296E-8 | 1.01457982473E-9 / 1.02002282647E-9 | 1.30680381981E-12 / 1.49134521772E-12 | 1.37548854708E-14 / 1.03176998208E-14 |
| 0 | 3 | 3.86168399025E-8 / 7.57450015414E-9 | 2.24772887573E-10 / 2.25511574950E-10 | 5.31151714514E-13 / 6.06760841217E-13 | 1.37539297400E-14 / 1.03159398800E-14 |
| 0 | 4 | 6.25801927737E-8 / 2.29456218635E-8 | 7.04520710760E-10 / 7.07890870697E-10 | 1.06628965557E-12 / 1.21630403643E-12 | 1.37546825439E-14 / 1.03173833733E-14 |
| 0 | 5 | 6.25801927735E-8 / 2.29456218597E-8 | 7.04520710758E-10 / 7.07890870691E-10 | 1.06628965557E-12 / 1.21630403643E-12 | 1.37546768666E-14 / 1.03174885166E-14 |
| 1 | 0 | 1.82475309610E-7 / 4.74830129824E-8 | 2.06469651121E-9 / 2.07891947743E-9 | 1.80318272037E-12 / 2.09275882519E-12 | 1.37566562554E-14 / 1.03220607625E-14 |
| 1 | 1 | 2.55824322907E-7 / 1.35772826972E-7 | 6.46254156277E-9 / 6.51609592460E-9 | 3.87950215181E-12 / 4.49270439347E-12 | 1.37676111646E-14 / 1.03386862301E-14 |
| 1 | 2 | 2.55824322906E-7 / 1.35772826982E-7 | 6.46254156278E-9 / 6.51609592461E-9 | 3.87950215181E-12 / 4.49270439347E-12 | 1.37680748921E-14 / 1.03374014483E-14 |
| 1 | 3 | 1.38294308056E-7 / 3.58178291833E-8 | 1.37087980988E-9 / 1.37951003039E-9 | 1.44697241831E-12 / 1.67361873372E-12 | 1.37556991552E-14 / 1.03205815765E-14 |
| 1 | 4 | 1.94767923388E-7 / 8.59436766706E-8 | 4.22652278954E-9 / 4.25868377057E-9 | 3.06580154144E-12 / 3.53528871352E-12 | 1.37625873698E-14 / 1.03296202587E-14 |
| 1 | 5 | 1.94767923390E-7 / 8.59436766786E-8 | 4.22652278954E-9 / 4.25868377058E-9 | 3.06580154144E-12 / 3.53528871352E-12 | 1.37625883889E-14 / 1.03299638391E-14 |
| 2 | 0 | 4.02053530305E-8 / 1.35133686375E-8 | 3.95052937057E-10 / 3.96645349361E-10 | 7.41310808284E-13 / 8.49121438270E-13 | 1.37543102814E-14 / 1.03177839700E-14 |
| 2 | 1 | 2.48602323960E-7 / 1.25765866586E-7 | 6.03055654225E-9 / 6.07777610702E-9 | 3.62318519612E-12 / 4.20737931792E-12 | 1.37586054031E-14 / 1.03261640916E-14 |
| 2 | 2 | 2.48602323958E-7 / 1.25765866596E-7 | 6.03055654226E-9 / 6.07777610704E-9 | 3.62318519612E-12 / 4.20737931792E-12 | 1.37586123118E-14 / 1.03259671823E-14 |
| 2 | 3 | 3.08598135807E-8 / 9.66790959521E-9 | 2.74022386388E-10 / 2.74947300887E-10 | 5.94218211065E-13 / 6.79563101896E-13 | 1.37540856545E-14 / 1.03166822135E-14 |
| 2 | 4 | 1.86162713849E-7 / 8.52562513006E-8 | 3.99867420732E-9 / 4.02783036791E-9 | 2.90575352992E-12 / 3.36143610730E-12 | 1.37572470011E-14 / 1.03231253549E-14 |
| 2 | 5 | 1.86162713850E-7 / 8.52562513087E-8 | 3.99867420732E-9 / 4.02783036793E-9 | 2.90575352992E-12 / 3.36143610730E-12 | 1.37572370364E-14 / 1.03228894280E-14 |
| 3 | 0 | 6.67918116759E-8 / 3.41128201757E-8 | 3.51568895750E-10 / 3.53002764097E-10 | 6.57565730210E-13 / 7.49656379509E-13 | 1.37548956567E-14 / 1.03181592107E-14 |
| 3 | 1 | 7.24199553119E-8 / 3.66221910576E-8 | 9.99855997073E-10 / 1.00515401462E-9 | 1.30780827525E-12 / 1.49333259693E-12 | 1.37548770643E-14 / 1.03180082554E-14 |
| 3 | 2 | 7.24199553149E-8 / 3.66221910608E-8 | 9.99855997074E-10 / 1.00515401462E-9 | 1.30780827525E-12 / 1.49333259693E-12 | 1.37548235385E-14 / 1.03180589737E-14 |
| 3 | 3 | 5.40397097191E-8 / 2.53870446609E-8 | 2.49924312522E-10 / 2.50786267344E-10 | 5.36536636212E-13 / 6.11420390156E-13 | 1.37546878427E-14 / 1.03174032008E-14 |
| 3 | 4 | 5.85821237398E-8 / 2.70132112420E-8 | 6.95670170502E-10 / 6.98959130258E-10 | 1.06700438049E-12 / 1.21772830119E-12 | 1.37546277851E-14 / 1.03174517024E-14 |
| 3 | 5 | 5.85821237423E-8 / 2.70132112446E-8 | 6.95670170503E-10 / 6.98959130261E-10 | 1.06700438049E-12 / 1.21772830119E-12 | 1.37546309405E-14 / 1.03176145270E-14 |

## Node diagnostics by angle

Time/projection node diagnostics have no independent continuum allowance. Arithmetic-node diagnostics are already included in guard and must not be added again. The maximum norm error is diagnostic, not the vector-error bound.

| Angle | Diagnostic | A max | C max |
|---|---|---:|---:|
| +4pi/5 | `sampled_time_node_L2` | 2.43663982245E-7 | 2.73053180256E-8 |
| +4pi/5 | `sampled_projection_node_L2` | 1.34633006367E-7 | 1.35206853600E-7 |
| +4pi/5 | `sampled_arithmetic_node_L2` | 1.98175433893E-13 | 1.98179099766E-13 |
| +4pi/5 | `maximum_norm_error` | 1.00849906204E-9 | 2.93298718646E-12 |
| -4pi/5 | `sampled_time_node_L2` | 1.88237127716E-7 | 2.10430518980E-8 |
| -4pi/5 | `sampled_projection_node_L2` | 8.52040002036E-8 | 8.54586216744E-8 |
| -4pi/5 | `sampled_arithmetic_node_L2` | 1.61849684349E-13 | 1.61832563321E-13 |
| -4pi/5 | `maximum_norm_error` | 4.95258944966E-10 | 2.82596168689E-12 |

## Decision and limits on any next test

The frozen local cost/bound condition is met on this panel, including the two focused states. This supports retaining N384 as a local candidate in a separately preregistered study. It does not establish accumulated errors, full-pulse feasibility or authorize a long run.

## Build, exact gate, and evidence custody

| Recorded separate stage | Wall seconds | Exit code | Standard output bytes | Standard error bytes |
|---|---:|---:|---:|---:|
| build_baseline | 13.9874552432 | 0 | 0 | 0 |
| build_candidate | 14.3892581146 | 0 | 0 | 0 |
| build_comparator | 14.239051871 | 0 | 0 | 0 |
| exact | 0.215001258999 | 0 | 1219 | 0 |

The saved exact gate reports **PASS**; stdout SHA-256 `dad43eb4277ebc1941f300ca94e923acfa61ef501da0ec095fc2e16c483a7a18`. This supports the listed algebraic fixtures, not an independent numerical replay or complete trajectory certificate. Any later CI exact replay has the same limited role.

Frozen sources are identified by the public pin. Completed child records passed the runner's source/input/binary custody checks; the recorded campaign status governs any later failure. This renderer authenticates every included archive member against the preserved manifest, but does not reconstruct the remote machine state or certify the solver implementation independently.

| Endpoint artifact | Bytes | SHA-256 | Local payload |
|---|---:|---|---|
| 01-A | 296524800 | `9a566df1502760cfb2a62ea2088a7978ef6fdfac346a2af2d00622f673db76f9` | remote receipt only |
| 02-C | 296524800 | `b04c2232c4800be5e53a68202a3af76f2cc1f7cace4c42d6432e5fdcf5ba8fa1` | remote receipt only |
| 03-C | 296524800 | `b04c2232c4800be5e53a68202a3af76f2cc1f7cace4c42d6432e5fdcf5ba8fa1` | remote receipt only |
| 04-A | 296524800 | `9a566df1502760cfb2a62ea2088a7978ef6fdfac346a2af2d00622f673db76f9` | remote receipt only |

| Report evidence | Bytes | SHA-256 |
|---|---:|---|
| remote-export.json | 33032 | `39a575407b495f415a9ad5aa0fa43a85d4b2d2e14442e074f2c320c27ec9fbde` |
| compact-evidence.zip | 1215623 | `fe70179d0f33457fd13e12f8d4afd89cffa651f087bc264c8e9aefcc1cd26c10` |

Report preparation is saved-output postprocessing in the same assistant session. It performs no scientific propagation, does not fit phases or normalize states, and is not an independent laboratory or numerical replication.
