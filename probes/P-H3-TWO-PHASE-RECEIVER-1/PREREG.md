# Two material values at the same two-tick latency

**Prospective L1 preregistration.** Public claim [#2003](https://github.com/mathorn1973/twist-j/issues/2003). This probe uses the 85 prepared cuts and the bare kernel from the [single-symbol experiment](https://github.com/mathorn1973/twist-j/tree/0c901277f99793cd2e2ca2b67bdad23943fae51e/probes/P-H3-SINGLE-PHASE-RECEIVER-1). Its fresh two-symbol stock, decorated trajectories and uninterrupted test are frozen here before execution. Bare input cuts were examined to design the stock. The predicted symbols are algebraic consequences checked against the full dynamics below.

Public main at claim is c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, ACTIVE Canon v113. Tag canon-v113 has object 3a91e2bee83a3045b17f3aa2895f69deef62d89c and points to that main commit. The content commit is 50d0e94d81e4954b7351bff755ed1889290bb7b8. The Canon has 1555510 bytes and SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34.

## 1. Equation and readout

Each cell on an \(8\times4\) torus carries \((R_0,R_2,K,U)\) (matter, CLK and CORR) in \(O=\mathbb Z[j]\), with \(j=\zeta_5,\ \rho=j^2,\ J=1+\rho\). At each tick H3 applies \(C_b\), then \(B\), and toggles the matching bit \(b\). The first three rails match vertically and \(U\) matches horizontally, starting at index \(b\bmod 2\) along each direction. For an admitted pair \(u-v\in2O\), \(C(u,v)=(m+\rho e,m-\rho e)\) with \(m=(u+v)/2,\ e=(u-v)/2\). Other pairs stay fixed.

At a site set \(d=(R_0-R_2)/2,\ f=(K-U)/2,\ h(z)=z\bar z\). For integral half-gaps, \(B_1\) sends \((d,f)\) to \((Jd,J^{-1}f)\) when \(d\ne0\) and \(h(f)=h(J)h(d)\). Otherwise \(B_2\) sends them to \((J^{-1}d,Jf)\) when \(f\ne0\) and \(h(d)=h(J)h(f)\). Both midpoints stay fixed. If neither branch applies, the site stays fixed. These unchanged maps perform every step. Raw rank is used solely to prepare and score trials.

One passive cell supplies one material observable \(S=R_0+R_2\). Its scalar readout is \(\mathrm{Tr}_{\mathbb Q(j)/\mathbb Q}(S)/2\) on the three declared fresh outcomes. Also inspect the actual rail that changes and the substep on which it changes.

## 2. Code

The accepted exact Python program is in this directory at **verify.py**. Run from the repository root with `python3 probes/P-H3-TWO-PHASE-RECEIVER-1/verify.py` after the preregistration commit and both file hashes have been read back publicly. All initial data and the native update are included. All reported four-tuples here use the ordered basis \(1,j,j^2,j^3\).

## 3. Carrier and paid initial conditions

Start bare rank zero at bit zero. Set \(R_0=2J,\ R_2=-2J,\ K=1\) in column zero at all four rows. The \(U\) triples in columns 0, 1 and 2 of rows 0 and 1 are \((-3,-3,5)\). At \((0,2),(0,3)\) put \(U=J-\rho^2-2\rho J(2+\rho+\rho^2)\). All other entries are zero. Iterate left-pair then right-pair \(C\) on the triple to define raw ready ranks 0 through 84. Locate their full bare ready cuts with next bit zero in the 622-tick bare orbit. Rank 44 is at tick 74 and rank 4 at 190. Each fresh trial starts on the predecessor, including the periodic wrap for rank zero.

Load two sites, keeping all CORR entries. Let \(D=(-2,-1,-2,0)\). The head at \((1,0)\) receives \((D,-D,K_H)\) with \(K_H=(-6,0,1,-3)\). The single passive cell at \((1,1)\) receives \((-3JD,3J^{-1}D,1)\). Its initial matter sum is \((-6,-3,9,0)\). Every fresh trial uses exactly this stock. An additional uninterrupted trajectory starts with the same stock at raw zero and receives no further preparation.

## 4. Systematics and predicted write

For raw 4 put \(g=JD,\ \epsilon=+1\), and for raw 44 put \(g=J^{-1}D,\ \epsilon=-1\). At tick one expect head branch 1 or 2 respectively, leaving the passive cell's matter intact. The chosen head rail becomes \(\epsilon g\) and its opposite passive rail partner on the same lane starts at \(-3\epsilon g\). At tick two the vertical contact changes that head rail by \(2\epsilon(\rho-1)g\) and the passive rail by its negative. The other matter rail at each site stays fixed during this transport. The head half-gap becomes \(\rho g\), so \(h(\rho g)=h(g)\). With the radiation half-gap retained, the inverse collision branch clears the read on the same tick. The head CLK and the whole CORR projection then coincide with their funded or bare references as appropriate. Its final matter midpoint is \(\epsilon(\rho-1)g\) and its half-gap is \(\rho D\). The changed midpoint explicitly pays the receiver's material increment.

Compare the entire clock outside the six prepared entries with the corresponding bare state, including every CORR, all otherwise untouched rails and the matching bit. Check the prepared sites separately, including funded CLK and both material pairs. Allow only the predicted transient radiation defect between read and clear. Test each transport/collision account in the full ring
\[
  \sum(R_0+R_2)=(-6,-3,9,0),\quad \sum(K+U)=(13,6,9,7),\quad
  \sum h(z)=(465,0,109,109),\quad \tfrac12\mathrm{Tr}\sum h(z)=821.
\]
The sums range over all cells, with \(h\) summed over all four rails. Recover each input bit and full state by undoing the collision and applying inverse transport with \(\rho^{-1}\); compare all coordinates. Inverse execution is a check only.

## 5. Failure thresholds

**Fresh trials.** All 85 run exactly two ticks, first bit one, then bit zero. The only expected transfers are \(R_0\) for raw 4 and \(R_2\) for raw 44, both at tick-two transport and retained after its collision. Require scalar levels \(-20,0,-15\) for raw 4, raw 44, and every other rank respectively. No other input may write or scatter at the prepared sites. Check the forward reset \(B_1,B_2\) at rank 4 and \(B_2,B_1\) at rank 44, including full clock recovery on exit. Every stated equality is exact.

**Uninterrupted operation.** Independently score 3110 forward ticks starting at raw zero. Require only lower-lane writes at \(75+622k\) and upper-lane writes at \(191+622k\), \(0\le k<5\), preceded by their corresponding native reads and followed by the appropriate same-tick clears. Require the bare-clock projection throughout up to the declared read transient, full accounts and inverses throughout and return of the complete augmented state including bit at tick 3110. At each scheduled completion also compare all six funded entries with the fresh output for that label, and require the corresponding passive pair to hold until the next scheduled write. Record concrete departures, including earlier joint returns when present. A missing or extra event falsifies sustained addressing even if the carrier later returns. Report the controlled and uninterrupted findings separately. Continue measurement through the horizon after an observed failure. Retain well-formed counterexamples as experiment outcomes.

## 6. Action layer

This is a finite L1 test of exchange between prepared sites in the specified H3 lattice. Clock restoration refers to the underlying 85-state carrier. A retained material output can coexist with a changed funded head. Full-circuit restoration requires literal equality of every coordinate and the matching bit. Continuous addressing is a separate empirical question. No physical dictionary or Canon status is proposed.
