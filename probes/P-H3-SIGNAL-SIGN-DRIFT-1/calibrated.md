# A loaded narrow-band packet calibration and transfer test

This finite L1 experiment calibrates an H3 detector to one earlier public field word. It then holds the detector and the packet fixed and changes their separation. The calibration arm and the transfer arms carry different evidential roles.

## Public calibration and fixed apparatus

Take the exact post-C word $W$ of the right launch at tick 40 and distance 20 cells in [PR #2034](https://github.com/mathorn1973/twist-j/pull/2034). This is the word at right.cuts_post_C_pre_B.40 in stage 2_wave_packet in the public [EXPECTED.txt](https://github.com/mathorn1973/twist-j/blob/a8d8071e2422f0756fe6feb17f3218299925e79a/probes/P-H3-MATERIAL-FLUX-WAVE-1/EXPECTED.txt), SHA-256 30837c1d016697ee572afb5652e1c6bb18fb59820e64cc323845a75e350d00bc. In the integral basis $(1,j,j^2,j^3)$ freeze

    W = (-21386172564582355000912103625195520000,
         -26736559282320142690578810420592640000,
         -35364882103878625360276832082984960000,
           1907317838809156011152305259806720000)

On the 384 by 6 torus of the front experiment, set $m=W/(2J)$ in $\mathbb Z[j]$. Load matter $(m,-m)$ at all six sites of column $x=1$, with all CLK initially zero. All other matter is zero. The column costs $12h(m)$ in the Hermitian account and $\operatorname{Tr}(12h(m))/2$ in the scalar account. Its linear material sum is zero. Identical vertical neighbors make both material C rails constant until the first active B, including when their coefficients are even.

Use the identical right-moving compact staggered packet and translation of [the first detector protocol](light.md). Run each unchanged packet at $D=20,30,40,60$ cells to tick 80. $D=20$ is the calibration arm, $D=30$ is a new transfer distance, $D=40$ holds out the prior public field word at that distance from the apparatus design, and $D=60$ is outside the 80-tick causal cone. Every preparation has the same complete initial accounts. The fixed calibration uses one prior public word.

## Prediction and actual read

In the calibration arm, before any active B, the packet moves as in the earlier free sector. The target is on row zero with zero local CLK. If no earlier B is active, its incident CORR at tick 40 is $W=2mJ$. The receiver then has matter half-gap $m$ and radiation half-gap $-mJ$, so B1 must fire. Thus a first active B no later than tick 40 is the calibration condition. If the first branch is the nominal B1 at tick 40, it makes receiver CLK $m\rho$. The next C sends $(L/2)m\rho$ into the next vertical CLK coordinate, on row one, as the difference is even. The verifier reports the actual first B and actual separately propagated CLK before and after B. Earlier activity can select a different itinerary, and the data retain it. Transfer at 30 or 40 cells is an open measured outcome. A null at those distances leaves the calibrated positive control intact.

Record first field and every actual active B through tick 80, including other rows after the first write. Record each material Hermitian and scalar transfer against the opposite radiation transfer, the first nonzero off-target CLK at a post-C cut and the same coordinates after B, and fixed receiver and off-target words at ticks 40, 60 and 80. Read persistence only at those declared cuts. Use the same sparse, pinned native pair and site maps as the first detector protocol. Check the complete ledgers at each post-C and post-B cut, check each inverse, and reverse the full horizon back to the complete initial field and phase. Failure of the account, integer preparation or inverse is an integrity stop.
