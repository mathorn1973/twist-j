# Does read-head CLK parity write the phase into one material rail?

**Prospective finite L1 experiment.** A prepared single-clock circuit on the native H3 lattice advances one physical receiver rail on raw 44 and raw 4 but its old word classes coincide. This experiment couples CLK selectively into a receiver collision. Bare cuts, the old orbit and local guard algebra were available during design. The new decorated trajectories, including the control and extra support, are prospective. [Claim #2009](https://github.com/mathorn1973/twist-j/issues/2009) · [Q616 antecedent](https://github.com/mathorn1973/twist-j/blob/3e37eb39385a60b594e8d941416f4f93186ccd73/probes/P-H3-SAME-RAIL-HOLD-2/RESULT.md).

Public authority at claim is ACTIVE Canon v113. The main commit is c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, the annotated tag object is 3a91e2bee83a3045b17f3aa2895f69deef62d89c and the content commit is 50d0e94d81e4954b7351bff755ed1889290bb7b8. The declared Canon has 1555510 bytes and SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34.

## 1. Equation and measurement

Work in \(O=\mathbb Z[j]\), \(j=\zeta_5,\ \rho=j^2,\ J=1+\rho,\ h(z)=z\bar z\). Each of 32 sites on an \(8\times4\) torus has four ordered rails \((R_0,R_2,K,U)\), with \(K=\mathrm{CLK},\,U=\mathrm{CORR}\). One forward H3 tick with bit \(b\) applies matching \(C_b\), collision \(B\), and flips the bit. The first three rails pair vertically, the fourth horizontally, with pairs beginning at index \(b\bmod2\). For \(u-v\in2O\), let \(m=(u+v)/2,\ e=(u-v)/2\). The pair becomes \((m+\rho e,m-\rho e)\). Other pairs stay unchanged.

The local collision preserves the two midpoints. With integral \(d=(R_0-R_2)/2,\ f=(K-U)/2\), branch 1 applies \((d,f)\mapsto(Jd,J^{-1}f)\) if \(d\ne0,\ h(f)=h(J)h(d)\). Otherwise branch 2 applies \((d,f)\mapsto(J^{-1}d,Jf)\) if \(f\ne0,\ h(d)=h(J)h(f)\). Other inputs stay unchanged. All reported four-tuples use the ordered basis \(1,j,j^2,j^3\). The output is \(R_0(1,1)\) at the end of the work tick. Observe it before transport, after transport, and after collision. Timing and raw labels are scoring information only.

## 2. Code and finite limits

Freeze **verify.py**, **period.cpp** and this preregistration on the public branch before executing the new preparations. Run the primary verifier from the repository root with `python3 probes/P-H3-CLK-TO-RAIL-1/verify.py`. It reconstructs all 85 bare inputs, tests fresh trials and observes all 3110 reference ticks for each of three fixed preparations.

The companion long-cycle engine uses a separate four-coefficient implementation and exact complete-state comparison. Compile with `g++ -std=c++20 -O3 period.cpp -o period` from the probe directory. Run separately with arguments `active 100000000`, `control 100000000` and `antenna 100000000`. Each run stops on the first full-field-plus-bit return or at that tick bound. At every bit-one cut, compare the full clock projection with the two original raw predecessors regardless of reference time. Count a read only when the native head takes branch 1. Record receiver words on the following work tick, separately counting actual changes; count additional changes and losses of hold on other substeps. Report disjointness of word classes only over the observed coverage. The Python and C++ clocks use independent ring representations; the long engine is a separately runnable supplement. An incomplete orbit gives a lower bound. A counterexample inside a prefix suffices to falsify a universal hold or decoder requirement. Preserve all three outcomes and any fired falsifiers.

## 3. Equal-input preparations and control

Start the bare clock at raw zero with next bit zero. Put \((2J,-2J,1)\) on the first three rails throughout column zero. Put CORR triples \((-3,-3,5)\) at columns 0,1,2 in rows 0 and 1. At \((0,2),(0,3)\) put \(U=J-\rho^2-2\rho J(2+\rho+\rho^2)\). Other entries are zero. Generate ready triples by alternating the left and right pair contacts on this triple and locate all 85 complete ready states with bit zero in a 622-tick bare orbit. The predecessors entering ranks 44 and 4 are at ticks 73 and 189 respectively. Load the same stock in all 85 fresh trials of a given preparation. For each separate uninterrupted run load the stock only at raw zero.

Let \(D=(1,-1,-1,1),\ g=JD=(3,0,1,1)\). At the head \((1,0)\) set \((R_0,R_2,K)=(D,-D,(0,2,-1,1))\). At the receiver \((1,1)\) set \((R_0,R_2)=(-3g,-g)\). All preparations keep the initial bare CORR entries.

| Preparation | Initial receiver CLK | Additional stock |
| --- | --- | --- |
| Open (C++ active) | \(k=(2,-2,1,6)\) | None |
| Sealed (C++ control) | \(\rho k=(5,-1,1,-3)\) | None |
| Supported (C++ antenna) | \(k\) | \(K=(6,-1,3,1)\) at \((1,2)\) |

Open and sealed have identical matter stock and identical Hermitian energy. Their radiation sums are accounted for separately. The supported preparation pays for its extra CLK cell explicitly.

## 4. Causal prediction and audit

During a read the two target head CLK values are \(T_{44}=(-1,3,0,0)\) and \(T_4=(-2,0,-1,0)\). At the next even matching their differences from \(k\) are \((-3,5,-1,-6)\) and \((-4,2,-2,-6)\). Only the second difference admits a CLK transport. The passive CORR on those cuts is \(U_{44}=(-2,0,-1,-5)\) or \(U_4=(0,0,3,-1)\).

The common upper matter contact on either fresh target writes \(w=(-3,2,-5,1)\) at its transport substep. The lower rail there remains \(-g\). On raw 4 in the open preparation the transported receiver CLK must be \((2,-2,1,1)\), so \(f=D\) and \(d=-\rho g\). This admits receiver \(B_2\), giving a different final word \(v=(-5,0,-5,0)\). At raw 44 the blocked CLK edge must leave the common word \(w\). Full-rail control measurements must show that the sealed CLK rotation closes both target edges and gives \(w\) for both. Require the same pre-transport and post-transport upper words in the active and sealed comparisons. The support tests the separate prediction that the phase-specific word can survive the next tick. Its added CLK has the phase-4 post-collision receiver residue.

Measure the complete matter sum, radiation sum, total Hermitian sum and half its field trace, counting all 128 rails. The predicted tuples are:

| Preparation | Matter | Radiation | Hermitian sum | \(Q\) |
| --- | --- | --- | --- | ---: |
| Open | \((-12,0,-4,-4)\) | \((20,6,8,17)\) | \((434,0,151,151)\) | 717 |
| Sealed | \((-12,0,-4,-4)\) | \((23,7,8,8)\) | \((434,0,151,151)\) | 717 |
| Supported | \((-12,0,-4,-4)\) | \((26,5,11,18)\) | \((487,0,180,180)\) | 794 |

For each fresh preparation and all 3110 reference ticks, compare exact native accounts at every \(C,B\) substep. Undo the collision, compare the inverse branch tags, use the toggled bit to select inverse transport, and recover the incoming complete field. The long engine checks local conservation and the inverse on each new nonidentity map before caching it, then additionally audits whole-state accounts and the inverse at least every 4096 ticks and at its endpoint. All checks are exact.

## 5. Decision criteria

* **Fresh selection and actual writes.** Over all 85 inputs require no earlier receiver write, no work write among the 83 controls, and a nonzero transport and net work change at each target. Compare final upper rails literally. Require \(w,v\) for open/supported (44,4 respectively) and \(w,w\) for sealed. Inspect the read and work branches separately. Check third-tick retention of each target as a separate predicate; preserve any undo. Compare the two active outcomes with the closed interventions to identify the CLK cause.
* **Clock restoration.** Test the complete bare carrier outside the six explicitly replaced stock entries (seven for supported), including all CORR and the matching bit. Also test all radiation rails against the bare reference with the paid CLK values installed. Report the exact work-cut comparison and first later equality, if any, rather than inferring uninterrupted recovery from equality at a later boundary. Full renewal requires literal equality of all rails and matching bit.
* **Reference-cycle operation.** In each of five consecutive 622-tick reference laps require the native read at both expected cuts and the completed work on the following tick. Qualify a phase only if the incoming carrier and bit match the full bare predecessor and the actual head takes \(B_1\). Within a qualified work tick allow both transport and collision to change the observed rail. Elsewhere require the last completed word to hold on every substep. Require all ten samples, nonempty disjoint ring-word classes for 44 and 4, and full renewal for a reusable clock-synchronous decoder. Missing or additional writes, overlap, a loss of hold, or a missed return falsify the corresponding claim.
* **Intrinsic loaded cycle.** Analyze actual state-qualified reads anywhere in the C++ orbit. On a completed cycle classify overlap of the words after all such reads and of words after actual net writes. Require both classes represented, a genuine write after each read, hold until the next qualified work, and full return for a persistent intrinsic phase register. Subsets of nominally scheduled samples or disjoint observed subsets before an uncompleted return do not establish it.

## 6. Action layer

This is an L1 finite test of a funded native circuit. Fresh transduction, retention, word separation, clock recovery, and periodic operation have separate criteria. No external schedule supplies an edge to the network, and no Canon status change is requested.
