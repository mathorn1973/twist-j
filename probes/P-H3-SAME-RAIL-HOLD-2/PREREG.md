# Holding a 44-to-4 transition on one native H3 matter rail

**Prospective finite L1 probe.** In the Q706 predecessor the same rail held its first word through tick 190. The ensuing work at 191 transported on both radiation edges, the inverse collision failed, and an unsolicited upper-rail contact followed at 193. That completed public record includes its original thresholds, retained counterexamples and incorrect transient prediction. This new probe changes the paid stock using bare inputs and exact pre-transport parity on both radiation edges. Its decorated trajectory has not been evaluated before this pin. [Public claim #2007](https://github.com/mathorn1973/twist-j/issues/2007) · [Completed Q706 experiment](https://github.com/mathorn1973/twist-j/blob/cd45ae66e915131e6456c9c5972d8448498f5836/probes/P-H3-SAME-RAIL-HOLD-1/RESULT.md).

Authority at claim: ACTIVE, Public Canon v113, main c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, annotated tag object 3a91e2bee83a3045b17f3aa2895f69deef62d89c, content commit 50d0e94d81e4954b7351bff755ed1889290bb7b8. The Canon has 1555510 bytes and SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34.

## 1. Native equation and observable

Use \(O=\mathbb Z[j]\), \(j=\zeta_5\), \(\rho=j^2,\ J=1+\rho,\ h(z)=z\bar z\). A full H3 state comprises four \(O\)-valued rails \((R_0,R_2,K,U)\) at each of 32 sites and a matching bit \(b\). Every forward tick transports by \(C_b\), scatters by \(B\), then toggles the bit. The first three rails match vertically and CORR (\(U\)) horizontally in disjoint pairs starting at index \(b\bmod2\). On the periodic \(8\times4\) lattice the admitted pair has \(u-v\in2O\); the outputs are \(m\pm\rho e\), where \(m=(u+v)/2,\ e=(u-v)/2\). Inadmissible pairs are unchanged.

For the local collision let \(d=(R_0-R_2)/2,\ f=(K-U)/2\). For integral gaps, branch 1 applies \((d,f)\mapsto(Jd,J^{-1}f)\) when \(d\ne0,\ h(f)=h(J)h(d)\). Otherwise branch 2 applies \((d,f)\mapsto(J^{-1}d,Jf)\) when \(f\ne0,\ h(d)=h(J)h(f)\). Collision preserves both midpoints and otherwise applies identity. The observable is the single physical rail \(R_0(1,1)\) in the ordered reporting basis \(1,j,j^2,j^3\). The scalar \(\mathrm{Tr}(R_0)/2\) is also reported. A write is an actual change on that rail, detected across each substep.

## 2. Code

Freeze this file together with the standalone Python standard-library verifier **verify.py**. Run `python3 probes/P-H3-SAME-RAIL-HOLD-2/verify.py` from the repository root after a public readback of the commit and both file hashes. The native transition receives only the whole field and the current bit. The expected event times, target labels, word count and bare references are used by the verifier to prepare or score, and never passed to the native rule as control inputs.

## 3. Carrier and initial stock

Bare rank zero starts at bit zero. Initialize \((R_0,R_2,K)=(2J,-2J,1)\) throughout column zero. Put CORR triples \((-3,-3,5)\) in columns 0,1,2 on rows 0 and 1 and put \(U=J-\rho^2-2\rho J(2+\rho+\rho^2)\) at \((0,2),(0,3)\). All other entries start at zero. Generate the 85 ready triples by iterating the left then right pair contacts on the initial triple. Identify each ready state by its full bare field and next bit zero over the 622-tick orbit. The marked cuts 44 and 4 are at ticks 74 and 190.

Set \(D=(1,-1,-1,1),\ g=JD=(3,0,1,1)\). At \((1,0)\) put \((D,-D,K_H)\) with \(K_H=(0,2,-1,1)\). At \((1,1)\) put \((-3g,0,1)\). Both sites retain their bare CORR. For fresh trials add this same stock to the predecessor of each ready state, including the wrap at rank 0. Each trial advances two ticks. For uninterrupted operation add the stock once at bare rank zero. Evolve that state forward for 3110 ticks.

## 4. Predicted dynamics and controls

Use \(n\) only in the external comparison with the measured trajectory. After \(n\) completed transfers, the predicted head midpoint and half-gap and the passive upper rail are
\[
 M_n=(\rho^n-1)g,\qquad D_n=\rho^nD,\qquad
 P_n=-g-2\rho^n g.
\]
The passive lower rail remains zero and its CLK remains one. At either marked read, expect \(B_1\) to change the head gap to \(JD_n\). The CLK increment and CORR decrement are the same \(\delta\) at that read, with \(\delta_{44}=(-1,1,1,-1)\) and \(\delta_4=(-2,-2,0,-1)\). During the next tick, expect only the upper lane to work at the receiver. The post-transport head gap is \(J D_{n+1}\), so the inverse branch \(B_2\) clears the radiation defect in that same forward tick. Outside these transient cuts the decorated clock agrees with the bare clock once the known funded rails are accounted for.

The full ring accounts over all rails are predicted to be matter \((-9,0,-3,-3)\), radiation \((19,8,7,11)\), Hermitian \((380,0,144,144)\), and scalar \(Q=\mathrm{Tr}(\sum h)/2=616\). Test them at every transport and collision. Undo each collision, compare its exchanged tags, then use inverse transport and the recovered matching bit to reconstruct the complete incoming state. Compare the full 32-cell field at both forward substeps with the bare field plus the specified stocks and transient. These checks account for all 128 rails.

At each work tick compare the actual incoming differences along the head-minus-passive CLK edge and head-minus-left-neighbor CORR edge. At raw 44 they must be ((-2,3,0,0)) and ((0,1,0,-6)); at raw 4 they must be ((-3,0,-1,0)) and ((5,4,9,2)). Require each difference to lie outside (2O). The hypothesized shielding is thus directly falsifiable at the cut where the predecessor failed.

## 5. Decision criteria and falsifiers

1. **Fresh selection.** Only raw ranks 44 and 4 may change \(R_0\), on the second transport. Require no change at the other 83 inputs. The predicted fresh target word is \(P_1=(-3,2,-5,1)\) for both ranks. Independently ask whether the observed two fresh target words are different. Coincidence falsifies fresh phase identification.
2. **Hold and forward handoff.** In one uninterrupted run require exactly 10 transfers at \(75+622k\) (raw 44) and \(191+622k\) (raw 4), for \(0\le k<5\). Require the stipulated reads on the preceding ticks and the forward clears on the write ticks. In particular \(P_1\) must survive every intervening substep including tick 77 and the next read at 190. At 191 require \(P_2=(3,4,3,5)\). For each later interval require the corresponding \(P_n\) until the next work transport; the expected half-traces for \(n=0,1,2,3,4\pmod5\) are \(-15,-5,0,0,-5\).
3. **Full return.** Require at tick 3110 literal equality with the initial state, including all funding and the bit. Require no repeated full state and bit before that tick. Any unequal ledger, failed inverse, extra write, lost hold, incorrect clock projection or earlier repeat falsifies its corresponding test.
4. **Stable phase identification.** Collect the exact \(R_0\) immediately after each qualified write in the uninterrupted run. The two phase classes must both be represented and disjoint for the rail alone to determine the phase. Any shared ring value falsifies this interpretation, including for any scalar function of that rail. The rotor formula predicts that both target classes visit all five ring values. Report the phase tests separately. Disjoint sets support a positive stream decoder verdict only if the stipulated hold and schedule also pass; partial coverage is insufficient.

All comparisons are exact. Preserve failed gates in the public result. A scientific counterexample is a normal verifier outcome.

## 6. Action layer

This experiment tests a reversible conditional advance and an absolute phase identifier as separate finite L1 assertions. It assumes the declared paid preparation. The held output, clock recovery and joint renewal have separate witnesses. No Canon promotion or physical interpretation is proposed.
