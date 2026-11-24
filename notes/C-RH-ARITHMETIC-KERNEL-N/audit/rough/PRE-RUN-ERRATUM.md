# Pre-run fixture correction

The frozen PREREG.md initially gave d=11*19 at N=1000 as the control for dropping the outer cutoff. Its floor quotient is 4, with residue kernel zero, and d actually belongs to the outer range. Do not use that fixture.

The corrected outer-cut fixture is the split prime d=19 at N=6*19. Its cube exceeds N, so it meets the least-prime condition. Its cube is at most N^2, since 19<36, so it lies outside the outer tail. Its floor quotient is 6 and its kernel weight is +1. Its signed contribution would be -2 under the omitted outer cut.

Use d=11*19 for the separate N=11^3 least-prime equality witness. Its cube exceeds N^2, its smallest-prime cube equals N, and floor(N/d)=6. The wrong nonstrict condition would admit a signed +4 contribution. These are support-level controls. The universal domain and every mathematical target remain as originally frozen. This correction was written before any checker was written or executed.
