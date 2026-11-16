# Preregistration of ordered finite-volume tests in the full Z5 measure

**NON-CANONICAL | L6 finite-volume diagnostic | unexecuted**

Test A measures the scaled electric and magnetic two-time correlations at width \(1/m\). Test B measures the transverse correlation tail at fixed nonzero longitudinal momentum. This is an L6 finite-volume diagnostic design. The finite grid can inform the next proof attempt. Inference about either ordered limit needs a separate uniform estimate on an unbounded family of sizes.

The authority is Public Canon v113, activation commit c089e7ec7ecc82f4838c27663d94c040f5cc4ea3, content commit 50d0e94d81e4954b7351bff755ed1889290bb7b8, Canon SHA-256 47114cb616069242cff36bb499e5fe9b11266a92c744ba3f15a9085c11956b34, 1555510 bytes. The existing formal production protocol under #742 has separate endpoints and dependencies. [Authority](https://github.com/mathorn1973/twist-j/blob/canon-v113/STATUS.md) Â· [Production freeze](https://github.com/mathorn1973/twist-j/blob/canon-v113/notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.md)

## 1. Fixed measure and conventions

Use the even periodic torus \(K_L=(\mathbb Z/L\mathbb Z)^4\). Sample all link fields \(a\in C^1(K_L;\mathbb Z_5)\) with density proportional to \(\prod_P W((da)_P)\), where \(W(f)=2+2\cos(2\pi f/5)\) at the fixed physical point \(t=1\). No gauge fixing, sector restriction, reweighting or coupling scan. The equivalent character measure is the complete ternary field \(n\), with weight proportional to \(2^{-|\operatorname{supp}n|}\mathbf 1_{\partial n=0\bmod5}\). All allowed integer currents and winding sectors are summed.

The measured score is \(X_P=\tan(\pi(da)_P/5)=\kappa G((da)_P)\). Use positive plaquette orientations and their true centers \(c_P\). Charge conjugation gives exact zero means. Use raw second moments without empirical recentering. Time differences in the observables are Euclidean coordinate differences within one configuration. The separated identity is \(\mathbb E_n[n_P n_Q]=-\mathbb E_a[X_P X_Q]\) for \(P\ne Q\). On the diagonal the sum of covariances is \(\mathbb E_a[(1+X_P^2)/2]\), constant by symmetry. [Separated and contact identities](https://github.com/mathorn1973/twist-j/blob/canon-v113/notes/C-PHOTON-BCHI-DIRECT-BOUND-N/FULL-MEASURE.md) Â· [Finite positive transfer](https://github.com/mathorn1973/twist-j/issues/1133#issuecomment-5767009888)

## 2. Test A. Two-time amplitudes

Use time coordinate 1, electric orientation \(I=01\) with \(s_E=-1\), and magnetic orientation \(I=02\) with \(s_M=+1\). For spatial \(p\) in coordinates \(0,2,3\), define per state
\[
 F_I(t,p)=L^{-3/2}\sum_{P\parallel I,\ \text{lower time coordinate }t} X_P e^{-ip\cdot c_P^\perp}.
\]
For \(L=rm\) and \(p_k=2\pi k/L\), set
\[
 w_r(k)=r^{-3}\prod_{j=0,2,3}(1-|k_j|/r)_+,\qquad
 \widehat A_{\alpha,L}(m)=\frac{m s_\alpha}{L}
    \sum_{t=0}^{L-1}\sum_k w_r(k)\operatorname{Re}
       [F_I(t+m,p_k)\overline{F_I(t,p_k)}].
\]
Time indices are periodic. \(\mathbb E\widehat A_{\alpha,L}(m)\) is \(mC_\alpha(m)\) in the packet. The corresponding dual estimator would use \(n\) with the opposite separated signs. No contact term enters this primary estimator.

This is the triangular probability packet with continuous weight \(\varphi_m(p)=m^3\prod_j(1-m|p_j|/(2\pi))_+\) relative to Haar measure. Its width constant \(2\pi\) is a prospective design choice, broader than the exploratory packet with constant \(1/4\), so the prescribed volumes resolve nonzero momenta. On \(L=rm\), the discrete weights sum exactly to one. Keep the zero mode with weight \(r^{-3}\) and report its contribution beside the nonzero modes.

Freeze \(m=4,6,8\) and \(r=4,6,8\). The fixed-\(m\) volume rows are \(4:(16,24,32)\), \(6:(24,36,48)\), \(8:(32,48,64)\). Record \(C_\alpha(0)\) with its separate contact convention. For each saved state, the electric lag-zero estimator is \(L^{-4}\sum_{P\parallel01}(1+X_P^2)/2\) minus the raw score autocovariance averaged in the same packet. The magnetic lag-zero estimator is the raw score autocovariance. Record \(C_\alpha(2m),C_\alpha(3m)\) as checks when \(L\ge6m\). Test the expected separated nonnegativity and monotonicity up to the midpoint without modifying the data. The theoretical target is a positive eventual lower after \(L\to\infty\) at fixed \(m\) in at least one fixed channel, followed by \(m\to\infty\). The finite grid cannot identify all admissible thermodynamic profiles.

## 3. Test B. Transverse tail

Fix longitudinal axis 1 and the precise momenta \(q=\pi/4,\pi/2\). The primary transverse axis is \(i=2\) with \(I\in\{12,01,02,03\}\). These are the four orientation classes under symmetries preserving the two designated axes. Their rotations give the other transverse axes at pure axial momentum. As a secondary trace check, use all 18 transverse-axis and orientation pairs. For each pair, the two remaining transverse coordinates of the marked momentum are independently \(0,\pm 2\pi M/L\), with \(M\) defined below. These are a finite neighbourhood grid, reported separately without a primary decision.

Put \(k_0=q e_1\) for the primary grid, and include the declared offsets in the secondary grid. For each state compute
\[
 U_I(k)=\left|L^{-2}\sum_{P\parallel I}X_P e^{-ik\cdot c_P}\right|^2,\qquad
 \widehat D(R;k_0)=\sigma_{I,i}
   \left[\sum_{|j|<M}\frac{M-|j|}{M^2}\,U_I(k_0+2\pi j e_i/L)-U_I(k_0)\right],
 \quad M=\lceil L/R\rceil,
\]
with \(\sigma_{I,i}=+1\) for \(i\in I\), \(-1\) otherwise. On the character side the bracket has the opposite sign by CONTACT. Use the two terms from the same state. The FejĂ©r weights sum exactly to one and cancel the contact. Do not take absolute values or clip individual measurements.

Write \(B_L(\ell;k_0)\ge0\) for the orientation-adjusted, separated transfer coefficient and \(T_L(R)=\sum_{\min(\ell,L-\ell)\ge R}B_L(\ell;k_0)\), summing \(1\le\ell<L\). Both periodic sides are included. With \(\mathcal D_L(R)=\mathbb E\widehat D(R;k_0)\),
\[
 \mathcal D_L(R)=\sum_{\ell\ne0}B_L(\ell;k_0)
     [1-|M^{-1}\sum_{v=0}^{M-1}e^{2\pi iv\ell/L}|^2],\qquad
 T_L(R)\le\tfrac43\mathcal D_L(R).
\]
For distances at least \(R\), the modulus in the kernel is at most \(L/(2M\min(\ell,L-\ell))\le1/2\). CONTACT gives \(\sum_{\ell\ne0}B_L(\ell;k_0)\le1\) by averaging the sign-adjusted contrast over the entire transverse frequency grid. For \(r<R\), using the second moment of the difference of two uniform indices in \(0,\ldots,M-1\) gives
\[
 \mathcal D_L(R)\le T_L(r)+\pi^2(M^2-1)r^2/(3L^2).
\]
Thus vanishing of the FejĂ©r observable and of the summed tail are equivalent in the ordered limits, for the same momentum family. This uses the fully summed signed covariance. [Transfer identity](https://github.com/mathorn1973/twist-j/issues/1133) Â· [Local-limit obstruction](https://github.com/mathorn1973/twist-j/issues/1134)

Freeze \(R=4,6,8\) and the volume rows \(4:(16,24,32)\), \(6:(24,40,48)\), \(8:(32,48,64)\), equivalently \(L=8\lceil rR/8\rceil\) for \(r=4,6,8\). Both marked momenta are exactly on every tested grid. The target is \(\lim_{R\to\infty}\limsup_{L\to\infty}T_L(R;q)=0\). Identifying the full axial trace also requires uniform control in a shrinking neighbourhood of the other transverse coordinates. The secondary finite grid samples that neighbourhood.

## 4. Sampling and integrity before measurement

Reuse the accepted primal exact-weight macrocycle. The throughput adapter packs the original bit blocks without changing the prefix and computes identical exact line masses from a signed-residue histogram. The macrocycle contains a complete exact single-link sweep and an exact noncontractible-line sweep, uniform flat sheets in all four axes and a fair charge-conjugation decision. Alternate forward and reverse order in the inherited manner. Use the exact \(\mathbb Z[\varphi]\) prefix comparison, the inherited Philox namespaces and the 256-bit cap. Record a cap hit as integrity failure. Use four seeded chains per distinct \(L\), chains 1â€“2 cold and chains 3â€“4 hot. Use seeds 0xC571000000000000 + 65536 L + chain index. Reuse every saved state for all tests at its \(L\). Translated terms, momentum terms and observables are correlated components of one sample.

Use the existing sixteen mixing sentinels and production diagnostic definitions at thermal endpoints 1024, 2048, 4096, 8192 macrocycles with the last 512 observations per chain. Adopt the first passing endpoint. Apply this rule with the new phase and tail values blinded. Then record 4096 consecutive macrocycles per chain, one state after each completed macrocycle. Retain failed chains and do not replace seeds or extend the schedule. In the measured block require each primary series to pass rank-normalized split and folded \(\widehat R\le1.05\), pooled bulk ESS at least 400, pooled 5/95-percent tail ESS at least 200, and recheck inherited sentinels over all 4096 saved observations (per-chain Geyer ESS at least 128, both Rhat estimates at most 1.03, pooled bulk/tail ESS at least 800/400, hot/cold separation and per-chain half drift at most 3, unique state fraction at least 0.99). Record flux-histogram, Polyakov, and wrapping-sensitive diagnostics. The established pilot was on small volumes. The larger grid has no existing equilibrium certification. [Exact kernel and original sentinel rules](https://github.com/mathorn1973/twist-j/blob/canon-v113/notes/canon/PHOTON-PRODUCTION-PREREG-FREEZE-1.md) Â· [Pilot scope](https://github.com/mathorn1973/twist-j/blob/canon-v113/probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/RESULT.md) Â· [Rank and ESS diagnostics](https://doi.org/10.1214/20-BA1221)

The public execution pin must identify the actual sampler, saved-state schema, independent reader, transform, commands and configuration grid by immutable hashes. The independent reader must derive curvature from the saved links and compare the direct definitions with any accelerated path. Before execution require small fixtures for both signs, centering phases and cyclic indexing, \(L^{-3/2}\) and \(L^{-2}\) normalizations, exact probability weight sums, gauge and cubic transformation, and agreement of the direct FejĂ©r and separation-kernel formulas. Use constant-score, single-mode and signed shifted-slice fixtures. The exact reference reader reconstructs plaquettes from the canonical saved links and uses direct pair-distance and algebraic sums. The accelerated reader independently reconstructs plaquettes, computes normalized transforms with certified algebraic roots, and exports outward-rounded intervals. For tail values with a wide fast enclosure it reconstructs exact integer phase counts and retries the outward arithmetic on those counts. The fixture suite compares the two paths. SHA256SUMS freezes the sampler, readers, driver and analysis. The public Git commit and issue #1996 identify this preregistration. The separate pre-execution record freezes the executable, environment, wall-time budgets and resource allocation before the first scheduled run.

## 5. Errors and order of evaluation

**Arithmetic error.** Implement exact rational packet and FejĂ©r weights. Use outward interval arithmetic for algebraic scores and complex transform values. Store final per-state primary enclosures of halfwidth at most \(2^{-30}\) and compare accelerated and direct evaluation on fixtures. Add this deterministic radius separately to mean intervals. An enclosure failure is an integrity failure. Use lossless deterministic replay custody for each state. The driver accepts one framed state at a time after independent identity and length checks. It commits the state SHA-256, the arithmetic enclosures and chain identifiers to the per-state series before acknowledging receipt. Retain the executable and its digest, compiler version and digest, runtime environment, commands, full sentinel logs, thermal endpoint receipts and per-state digests. Before a completed volume is admitted to the primary scale decisions, run the independent receipt replay on its complete link-state stream. Store the replay receipt with the input measurement-file SHA-256. The replay regenerates each saved link state from the original seeds and frozen schedule, checks its length and SHA-256, and compares the thermal control prefix. Wall-time limits and the execution platform are frozen in the public execution record before starting measurements. The volume driver preserves partial records and marks a budget stop.

**Monte Carlo error.** Pool four equal chain means. For each batch length \(b=64,128,256,512\), estimate variance of each chain mean by its disjoint full batch-mean sample variance divided by the batch count. Sum the four variance estimates and divide by 16 for the pooled mean. The reported standard error is the maximum over those square roots and the sample standard deviation of the four chain means divided by two. Compute contrasts within each state before batching. Report the descriptive paired raw-state covariance matrix for primary observables evaluated on the same configurations. The primary family has \(K=90\) cells, 18 amplitude cells and 72 pure-axis tail cells. Use the nominal simultaneous halfwidth \(h=z_{1-0.01/(2K)}\widehat{\mathrm{SE}}+2^{-30}\) with the standard Gaussian quantile. Secondary-grid intervals are descriptive and cannot change a primary decision. A primary \(h>1/128\) is precision-unresolved. These are batch-based diagnostic intervals under equilibration and a large-sample approximation. [Batch-mean uncertainty](https://arxiv.org/abs/0811.1729)

**Equilibration error.** Label mixing failures separately from roundoff failures and noisy estimates. Passing diagnostics and exact transition comparisons do not bound distance from stationarity. A general minorization illustrates the gap quantitatively. Each single-link choice has probability at least \(\gamma=(W_{\min}/4)^6/5\), so a complete sweep can set every link to zero with probability at least \(\gamma^{4L^4}\). Following the sweep by the other macrocycle moves preserves a common minorization of that mass, possibly with a parity-dependent minorizing law. This yields a valid but ineffective general bound \((1-\gamma^{4L^4})^b\) on total variation after \(b\) macrocycles. An equilibrium-certified result requires an evaluated useful mixing/coupling bound or an independent exact equilibrium sampler pinned separately. Effective sample size is not a replacement for independent exact draws in a concentration argument.

**First \(L\) at fixed \(m\) or \(R\).** Report all three volume estimates before comparing scales, separately for each channel and each \(q,I\) row. A finite row is stable only if all cells pass integrity, mixing and precision and both adjacent pairs satisfy
\[
 |\widehat y_{L'}-\widehat y_L|+h_{L'}+h_L\le1/32.
\]
For a stable row report the hull of its three intervals as a finite-volume envelope. Keep unresolved rows and observed drifts visible. This envelope is a screening device. It has no certified coverage for \(L=\infty\). No fixed-ratio \(L/m\) or \(L/R\) sequence and no fitted volume exponent enters an ordered-limit inference.

**Then \(m\) and \(R\).** At \(m=6,8\), report finite-grid support at resolution \(1/64\) if stable envelopes in the same channel have lower endpoints at least \(1/64\) at both scales. Report finite-grid smallness at that resolution if both channels have stable upper endpoints below \(1/64\) at both scales. Otherwise report unresolved. For Test B report \(4/3\) times each FejĂ©r upper envelope endpoint as the diagnostic upper bound for \(T_L(R)\) on the tested volumes, capped for display at its exact ceiling one. Report finite-grid tail smallness at resolution \(1/16\) only if all primary \(q,I\) rows meet this bound at both \(R=6,8\) after their volume screen. A large FejĂ©r value at finite \(R\) can include short-distance correlations and on its own leaves the tail unresolved. Keep raw values, all flags and any budget stop. The resolutions are prospective diagnostic choices.

The finite-grid outcomes do not settle either asymptotic claim. Test A needs a lower independent of arbitrarily large \(L\) at fixed \(m\), followed by a common positive lower on eventual \(m\) in the chosen packet family. Test B needs a volume-uniform bound at fixed \(R\), followed by decay as \(R\to\infty\) at the declared \(q\)'s. A proof of trace identification requires the analogous estimate on a full transverse neighbourhood. These are the limits that any subsequent analysis must address. [Open phase gate](https://github.com/mathorn1973/twist-j/blob/canon-v113/canon/GATES.tsv#L16)
