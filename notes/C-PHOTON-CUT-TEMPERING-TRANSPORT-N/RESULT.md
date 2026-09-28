# Result: fixture type error prevented production

**PUBLIC / NON-CANONICAL. FAIL_IMPLEMENTATION_ANALYZER_TESTS.**

The first frozen invocation at `42efd804047ab89aa80e79d37276366d5cfa8596`
passed the sampler implementation audit, then failed the analyzer-fixture
suite. Eleven tests passed; one errored. The controller stopped exactly
as preregistered, before any of the twenty production jobs or the production
analyzer started. This is neither a transport failure nor a result about
signed cancellation.

The recursive no-interval guard in
`test_complete_synthetic_transport_fixture` calls `key.lower()` on every
dictionary key. The result includes integer replica labels in
`roundtrips_by_replica`, so it raises
`AttributeError: 'int' object has no attribute 'lower'`. Its preceding
synthetic qualification assertions had completed. This is a fixture key-type
handling defect; the static review missed it. No lattice observation is
available from which to assess the proposed sampler.

RUN.md and the eight preserved ENGINEERING files record the complete actual
attempt. The seven frozen files, thresholds, budget and seeds remain
unchanged. No test was removed, no failure relabeled, and no job retried.
The identifier is consumed and must not be reused or resumed. A corrected
successor can change the fixture guard to handle integer keys, with a new
identifier, review and public pin before execution.

The finite stationary-law proofs retain their candidate-T scope after
review. This failed engineering attempt has ZERO scientific evidential
weight and provides no signed contrast, sector-polarization lower bound,
mixing theorem, phase or P1 conclusion. Public Canon v92 is unchanged.
