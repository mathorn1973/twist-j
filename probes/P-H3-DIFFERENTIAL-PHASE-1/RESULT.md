# Signed writes, differential holds and the reach of the point emitter

Status: CANDIDATE / NON-CANONICAL

All six stages completed from the [public preregistration pin](https://github.com/mathorn1973/twist-j/commit/aa1842905d0a7236e6fcc72b426468cd685ac9a8). The complete output is preserved. The fixed-source fixtures failed the direct signed Coulomb-phase criterion. They distinguish a signed local write, a retained offset, and an increment during a measured hold. The codes \(q,p\) refer to prepared orientations. Their identification as physical charges remains open.

## Two distances on one H3 path

One source on a common horizontal rail reached simultaneous receivers at \(r\) and \(2r\) at exactly those ticks for \(r=1,2,3,4\), including the equal-stock free-path controls. We scored 32 loaded histories, paired with 32 parked-source and 32 free-path histories. With fixed launch amplitude, the closer probe changed the field on the farther probe at tick 2 for \(r=1\). For \(r=2,3,4\) the fixed drive gave zero endpoint and hold phase contrast throughout the tested sign choices. The far-calibrated drives produced additional contrasts. The null-corrected differential was even under either sign reversal in every radius/drive group. None of the 32 loaded histories gave the preregistered nondegenerate near-phase-equals-twice-far-phase relation during the subsequent \(2r\)-tick hold. The test uses phase modulo a full turn in both embeddings. The mixed material column has no measured continuous phase lift. [Shared path and controls](native_read.md)

## An opposite phase write can survive without growing

With a fixed CLK bias at each odd matter anchor, the independent free-flight pilot read \((r,2r)\) at all four ranges. Let \(N=\#B1-\#B2\). The simultaneous native gap phase relative to its resting reference in the principal embedding is \(2\pi N/5\). All 32 loaded bias cases had common scalar stock \(Q=12347232\) and matched complete \(M,U,H,Q\); each returned to its exact preparation under inversion.

The table shows the signed integer \(N_r-N_{2r}\) **added during the common interval from \(2r\) to \(4r\)**. The far and near cuts see the same elapsed hold time. Each entry covers all four sign combinations.

| Launch | \(r=1\) | \(r=2\) | \(r=3\) | \(r=4\) |
| --- | ---: | ---: | ---: | ---: |
| Same unsigned amplitude at every distance | 0 | 0 | 0 | 0 |
| Amplitude compensated separately for each path | 0 | 0 | 0 | \(-qp\) |

With compensation the first contact selected B1 for \(qp=+1\) and B2 for \(qp=-1\) on both probes at every distance. The fixed launch also produced a signed offset at \(r=4\): it already equaled \(-qp\) at \(2r\) and still equaled \(-qp\) at \(4r\). At \(r=1,3\) the compensated run also retained that offset. This is an example of a usable sign-sensitive detector and of the distinction between a stored phase and a sustained rate. [Anchored apparatus](anchored.md)

## Autonomous stationary source and exact return

The other apparatus initializes a material emitter once, then advances only H3. All 16 loaded runs have the same complete budget with \(Q=660\). At one bond from the source the first nonzero CORR arrives at tick 2. The local matter phase shift is \(qp\,2\pi/5\) against the co-evolved resting reference. An inverse branch at tick 3 cancels it. The signed write recurs at ticks 12, 22 and 32, with the corresponding restorations observed at 13 and 23. The more distant receivers record no CORR through tick 32. A hold timed from actual arrival at the far receiver is therefore undefined. Full source-site words in the near and far arrangements never diverge on those 32 cuts. An active receiver changes its own radiative stock as required by the collision; the experiment did not detect a changed source trajectory.

The isolated emitter returns exactly to its complete initial state and matching bit at tick 10. At both native substeps the union of occupied sites consists of the origin, its western CORR neighbor and its southern CLK neighbor. No occupied site reaches the simulation boundary. Locality and determinism extend this exact ten-tick solution to the infinite grid and every later period. A passive field read at two or more bonds is therefore silent for this emitter indefinitely. General multisite sources are outside this conclusion. [Emitter and recurrence tests](anchored.md)

## What bounds phase accumulation

**Secondary candidate T, algebraic consequence.** This bound follows from the frozen anchor identity and conserved native account. It was not a numerical pass criterion. Assume a nonzero antipodal material half-gap \(d\) at an odd, isolated anchor, with material C refused on every step. Its word after any evolution is \(g_t=dJ^{N_t}\). Let \(H_i\) be the finite, conserved total Hermitian stock in each of the two complex embeddings, and let \(A_i=H_i/(2|\sigma_i(d)|^2)\ge1\). The two material rails contribute \(2|\sigma_i(d)|^2|\sigma_i(J)|^{2N_t}\le H_i\) because every word contributes a nonnegative squared modulus. Order the embeddings so that \(|\sigma_1(J)|=\varphi^{-1}\) and \(|\sigma_2(J)|=\varphi\). Then for every tick
\[
 -\frac{\log A_1}{2\log\varphi}\ \le N_t\le\
 \frac{\log A_2}{2\log\varphi}.
\]
Consequently the difference of two such signed counts is bounded for all time and its average rate tends to zero, for arbitrary incident radiation consistent with the hypotheses. Individual B1 and B2 counts and the sum of absolute phase changes can grow without bound. A fixed nonzero per-window secular rate for all repeated windows would violate the bound. Any return of the anchor word itself restores the exact net exponent, since \(J\) has infinite order.

This explains a limitation that measuring for more ticks cannot remove on this readout. Admitted material C provides a concrete way outside its hypotheses. The exact cold alternating material mode rotates by \(\rho\) at every C while both Hermitian weights stay constant. It supplies a candidate clock for a later **loaded-versus-free rate** comparison, with a separate task of obtaining repeated signed changes in its tick count. [Earlier explicit material transfer](https://github.com/mathorn1973/twist-j/blob/1d90710e4209a3c121f619e424853141c4c6fd83/probes/P-H3-PHASE-D3-FLUX-2/matter.md)

## Phase, work and the independent scalar clocks

- The fixed-reference local H3 control changes the received material gap ratio from 1 to \(J\) with both arms at scalar material \(Q=10\). The active arm exchanges nonzero full Hermitian stock with radiation. In the separate cold C control, an equal-site-weight encoding produces the ratios 1 and \(\rho\). The following C reads the distinction into local material weights \((16,16)\) and \((6,26)\). All three global radiation-affine controls preserve the material history under their stated simultaneous transforms. [Exact controls](quadrature.md)
- In grounded scalar \(D_3\) boxes with 4,631 and 6,083 sites, exact first-hit times and amplitudes agree with weighted shortest walks at every tested endpoint. At \(r^2=26\), the two equal-radius directions take 3 and 4 ticks from source activation to the doubled endpoint in both boxes. At \(r^2=50\), they take 5 and 6. The long-wavelength characteristic has unit speed in the same coordinates. A timing choice changes the work-times-time comparator. The fixed-source differences \(G(x)-G(2x)\) are negative for the shortest sampled axial and face-diagonal pairs, and positive for the other eight samples in each box. Thus the sampled near field also fails strict radial monotonicity. These are grounded, finite-distance observations. The Coulomb tail established in the predecessor is asymptotic.
- Interpreting static scalar work times ticks as a phase requires an action scale and a source assignment. No H3 experiment here measured the physical \(\alpha\). [Scalar protocols](d3_read.md) · [Exact scientific output](EXPECTED.txt) · [Local execution and hashes](RUN.md)
