# CLK parity produces distinct fresh words; the clock loses its clearing collision

**Finite L1 result.** One H3 clock, one receiver and identical paid stock across inputs gave two different reversible writes on the same physical \(R_0\) rail. Across all 85 fresh inputs only 44 and 4 wrote. The equal-energy CLK control removed the distinction. In an uninterrupted run the open and supported receivers lost the held word at ticks 192 and 208, respectively. Both already display the same word after different last qualified phases within the first 697 ticks. [Preregistration](PREREG.md) · [Primary output](EXPECTED.txt) · [Run records and full-period search transcripts](RUN.md).

## The phase changes an actual native collision

Read at tick one and measure the one receiver at the end of tick two. All tuples are coefficients of \(1,j,j^2,j^3\).

| Fresh input, open preparation | Initial \(R_0\) | After work transport | After work collision |
| --- | --- | --- | --- |
| Raw 44 | \((-9,0,-3,-3)\) | \((-3,2,-5,1)\) | \((-3,2,-5,1)\) |
| Raw 4 | \((-9,0,-3,-3)\) | \((-3,2,-5,1)\) | \((-5,0,-5,0)\) |
| Each of the other 83 | \((-9,0,-3,-3)\) | \((-9,0,-3,-3)\) | \((-9,0,-3,-3)\) |

At raw 44 the vertical head-minus-receiver CLK difference is \((-3,5,-1,-6)\). The contact refuses. At raw 4 the difference \((-4,2,-2,-6)\) lies in \(2O\). Transport changes the receiver CLK from \((2,-2,1,6)\) to \((2,-2,1,1)\). With CORR \((0,0,3,-1)\), the resulting radiation half-gap equals \(D=(1,-1,-1,1)\). The material half-gap is \(-\rho JD\); the norm guard therefore admits \(B_2\). That collision changes the upper material rail a second time. Rotating only the starting receiver CLK by \(\rho\) preserves its Hermitian energy and seals the edge at both targets. This control produces the same upper word for both phases. The open and sealed matter inputs and post-transport upper words agree exactly.

## The price of the open edge

At the raw-4 work cut both head and receiver CLK leave their admitted contact in the same residue class. Their horizontal CORR edges are shielded. Head CORR \((2,2,3,0)\) and receiver CORR \((0,0,3,-1)\) have different residues modulo \(2O\). Thus these two cells cannot both have integral radiation half-gaps on that cut. In the measured case the receiver takes \(B_2\) and the head takes identity. Head CLK and CORR retain the read disturbance. This incompatibility applies to the given two-site work geometry and shielded CORR edges.

At phase 44 the carrier and all paid radiation rails clear on the work tick in all three preparations. At the phase-4 work tick they clear only in the sealed control. After tick 191 neither open preparation regained the complete bare-carrier projection at any tested substep through tick 3110.

## Holding the last qualified phase

Starting once at raw zero, both active preparations wrote \((-3,2,-5,1)\) for 44 at tick 75. At tick 191 they wrote \((2,4,1,3)\) for 4 from the already-used receiver. The unassisted receiver lost that word on the collision at 192. Additional paid CLK at the neighboring site preserved it through 207; at 208 the same unsolicited change occurred. Both changed to \((3,4,3,5)\).

A counterexample also rules out an arbitrary decoder of the **held** upper rail. At tick 75 the last qualified read was 44. At tick 697 the last qualified read was 4; the projected clock did not qualify the nominal next read at 696. On both cuts, in both active preparations, the exact receiver word was \((-3,2,-5,1)\). Four integer coordinates therefore fail to identify the last phase at arbitrary later cuts. This argument needs only a finite prefix. It does not decide whether the sets of words sampled **only at future qualified completions** ever intersect in the as-yet unmeasured rest of these loaded orbits.

| Preparation | \(Q\) | First loss of hold | State-qualified raw 44 / raw 4 completions in extended search | First return of full lattice and bit |
| --- | ---: | --- | --- | --- |
| Open | 717 | Tick 192 | 1 / 1 | Greater than 100,000,000 |
| Sealed, equal energy | 717 | No loss on its full orbit | 5 / 5 | 3110 |
| Supported | 794 | Tick 208 | 1 / 1 | Greater than 100,000,000 |

The long search identified phase predecessors by the complete projected field and bit at **any** time and required the native \(B_1\) read. Each active preparation had just the two qualified events in the entire search. Their two observed endpoint classes were disjoint singletons. The sealed control traversed its complete orbit and both classes contained all five of the same ring words.

## Account, reversibility and scope

For each preparation the Python verifier checked all 85 fresh three-tick trials and every substep of the 3110-tick reference horizon, including inverse branches and recovery of the incoming full state. The open matter, radiation and Hermitian sums were \((-12,0,-4,-4),(20,6,8,17),(434,0,151,151)\). Sealing changed the radiation sum to \((23,7,8,8)\) at the same \(Q=717\). Adding the support changed radiation to \((26,5,11,18)\) and the Hermitian sum to \((487,0,180,180)\), giving \(Q=794\). All account and inverse tests passed. The separate long-cycle engine checked each new nonidentity local map for exact account conservation and inverse recovery, and performed 24,415 whole-state audits in each 100-million-tick run.

Since \(\mathrm{Tr}(z\bar z)=5\sum a_i^2-(\sum a_i)^2\ge\sum a_i^2\) in this basis, the conserved positive scalar account bounds every integer coefficient on the finite grid. Invertibility then ensures an eventual joint return; the two active periods remain unknown. A later return will repeat the measured hold failure.

The supported neighbor addresses the immediate undo for 16 further ticks. A persistent decoder still needs a native return path for the displaced radiation that lets the read head rearm while the material word stays held. A decisive next test is simultaneous integrality of the required field half-gaps on a compensated work cut, or a demonstrated delayed forward clear before the next phase read.
