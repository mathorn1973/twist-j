# Review of the first frozen execution

**PUBLIC / NON-CANONICAL. Disposition: INCONCLUSIVE_MOBILITY.**

This continues the same-session assistant review recorded in REVIEW.md;
it is not independent confirmation by another human author. The reviewed
source pin is `12942b6fc5a7540b7ff73cc65e9725ef4b4625e8`. The preserved
outputs reviewed here are published in
`8227ecf8a4d688a89ed855163f991f779132387a`.

## Custody and execution

The six prospective source and review files are unchanged between these
commits. I read RUN.md, RESULT.md, the preserved execution manifest and
the first analyzer output. I inspected existing JSON fields and checked
the analysis-file hash; I did not rerun the sampler, audit or analyzer.

The execution manifest records exit zero and empty stderr for the audit
and all 24 sampling jobs. The preserved analyzer output lists all 24 runs,
no missing runs and no execution-custody errors. Its SHA-256 is
`d5b48289d55d028b29c7635355fa487def2ced7ea9f0b4436c58686e1ee23b38`,
matching RUN.md. The audit transcript and block outputs remain engineering
records, not a formal exact-computation gate.

RUN.md records controller exit zero and discloses the custody limitation:
the first analyzer's separate process exit code was not captured. Its
preserved JSON reports INCONCLUSIVE_MOBILITY and its stderr was empty;
this review does not infer an observed process exit from those facts.
No second analyzer invocation is used to fill that missing observation.

## Mobility disposition

The preserved records support RESULT.md:

- All 24 chains have zero complete labelled-replica round trips, below
  the preregistered minimum of eight.
- Every chain has an adjacent temperature edge with zero accepted
  production exchanges, below the minimum acceptance fraction of 0.05.
- Both modes at L=8 and mode 2 at L=6 have zero target endpoint changes
  in every chain. Their endpoint-zero counts are (4096,4096,0,0), in
  cold0, hot0, cold1, hot1 order.
- Each of L=4,6,8 therefore has INCONCLUSIVE_MOBILITY. Every reported
  sum-of-squares interval is null and signed estimates are retained only
  under the NONINFERENTIAL_ESTIMATE label.

The pooled endpoint-zero fraction 1/2 in the locked groups is imposed
by the balanced initial endpoints. It provides no check of the equilibrium
normalization. Endpoint changes in some smaller-volume runs do not repair
the failed roundtrip and exchange requirements.

## Scope of the conclusion

The frozen attempt failed its mobility qualification. No full-measure
signed contrast, positive thermodynamic lower bound, decay verdict or
phase decision is supported by these trajectories. The failed transport
checks do not contradict the exact stationary-measure identities in
PROOF.md; those written results retain their candidate-T scope.

No post-observation threshold change, budget extension or retry was used
to alter this disposition. The attempt is consumed. Any successor requires
a separate prospective procedure. Public Canon v92 and the open P1 target
remain unchanged; these numerical records have ZERO scientific evidential
weight under the preregistration.
