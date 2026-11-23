# P-H3-TWO-SCALE-CLOCK-WITNESS-1

**Action layer.** L1, finite state evolution under the native H3 rules.

**Owner.** A. M. Thorn.

**Question.** Does the declared negative-bias station give both receiver cells signed unwrapped offsets of $+1/5$ turn for $q=-1$ and $-1/5$ for $q=+1$ at both B19 and B29 with five active radius-three donors and paired material stock 1,892,346? This is an open deterministic replay of an already known finite witness. The earlier concealed experiment is historical. This protocol uses public labels and fixed gains.

## Frozen carrier and panel

Use the periodic $192\times112$ four-rail H3 lattice with exact integer words in the basis $(1,j,j^2,j^3)$ and the principal embedding $j=\exp(2\pi i/5)$. The launch words, guards and readout positions appear in [verify.py](verify.py). Source sign $q$ changes the source encoding, while a second source lane stays at $+1$. The station uses bias $p$ and gain $k$ and does not depend on $q$. Both donor banks and guard compensation words are present in every mode. The three modes place the selected bank at the receiver, park both material banks, or park the source and horizontal station drive with the selected bank still at the receiver. Cross both signs of $q$ and $p$, all three modes, and gains $(4090,247,2199,430,1467,918)$, giving 72 trajectories through B29.

The C transport matches parity $(t-1)\bmod 2$ along $x$ on the CORR rail and along $y$ on the other three rails. B applies a collision to each cell. The verifier imports the public [H3 reproduction kernel](../../reproduce/h3-referenced-record/verify.py) from the v116 source tree and requires SHA-256 4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd. Sparse iteration skips only all-zero groups, which the kernel fixes. Each C/B step is reversed and checked against its input. Material and radiation sums and total Hermitian stock must be conserved on both substeps. Initial accounts must match within each gain.

## Forecast and falsifiers

The material gap is half the difference of the first two rail words. For each C and B substep read the unique signed $s\in\{-2,-1,0,1,2\}$ such that the new gap is the old gap times $j^s$ and a strictly positive real scalar. Zero and off-grid gaps fail. Positivity uses exact comparisons of rational squares in $\mathbb Q(\sqrt5)$. Accumulate C and B increments separately before subtracting the reference winding. Compare every raw gap and signed substep lift for both receiver cells and both reference cells against a closed-form forecast that does not call native evolution.

Let $\rho=j^2$, $J=1+j^2$, $S=j^2+j^3$, and $G=\rho J(1-\rho)^8$. A free clock has anchor and partner gaps $\pm\rho^{\lfloor(t+1)/2\rfloor}G$ at both substeps. Both signal-on modes first receive CORR at C9. The B9 writes multiply the two gaps by $J^{qp}$ and $J^p$. For $q=+1$ subsequent running gaps track those multiples of the free gaps. For $q=-1$ both gaps hold through B11 and stay held in the parked-bank mode. The source-off mode stays free.

For the active discordant $p=-1$ case use $\lambda=(-134-103S)/25$ at C12 and C13 and $\mu=(38-9S)/25$ from C14. The antipodal gaps at C12, C13 and C14 are $\pm(0,113,154,113)$, $\pm(-41,-154,-154,-41)$ and $\pm(56,103,56,0)$. Their signed C increments in fifth-turns are $(0,2,2)$ for the anchor and $(2,2,2)$ for the partner. From C14 the gaps are $\mu J$ times the free gaps, with the ordinary subsequent C turns and B holds. At B19 and B29 the receiver windings are $21/5,31/5$ turns at $q=-1$ and $19/5,29/5$ turns at $q=+1$, with reference windings of $20/5,30/5$. For the active discordant positive-bias comparison, C12 takes both cells to their respective $J^{-1}$ free gaps with lifts $(2,0)$. They keep that offset through B29.

Receiver B tags must agree with the write or hold at each substep. Require zero exterior B tags in the receiver column and zero CORR at either reference. The partner four-word histories in active trials with opposite $q$ must agree before their first split at C11. Source-off receivers have no first arrival through B29. The five occupied negative-bias launches have radius three. The paired stock of donor word $w$ and its opposite rail is $5\sum_i w_i^2-(\sum_i w_i)^2$. The side totals must be 727,870 and 1,164,476. Any failed comparison rejects the frozen witness. The verifier uses exact arithmetic throughout.

The output is an attainable upper bound for the stated preparation. The scoped minimum lower certificate, other repair schedules, changed lattices or launch classes, interpretation as a physical clock, and claims of new concealment or independent validation are outside this probe.
