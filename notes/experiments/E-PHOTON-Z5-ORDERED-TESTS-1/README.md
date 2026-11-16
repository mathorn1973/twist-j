# Ordered Z5 tests

This is the unexecuted NON-CANONICAL preregistration for issue #1996. PREREG.md specifies the
probability measure, observables, simultaneous error budget and volume-first
decision rule. SHA256SUMS identifies the proposed source bytes for this package.

The two readers derive plaquette scores separately from canonical link-state
bytes. reference_reader.py uses cyclotomic coefficients and direct periodic
pair-distance sums on fixtures. ordered_reader.py is the accelerated interval
reader. A contact, sign, phase, schema, replay or precision failure prevents a
measurement from being admitted.

The C++ adapter inherits the exact macrocycle. Its capacity adaptations and
streaming protocol are documented in SAMPLER_ADAPTER.md. The checked public
diagnostics dependency is analyze_pilot.py at
c089e7ec7ecc82f4838c27663d94c040f5cc4ea3 in
probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2. The required SHA-256 is
d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce.

## Local checks

Run the reader suite and the analysis fixtures with Python and NumPy.

    python3 -B -m unittest -v test_reference_reader test_ordered_reader
    python3 -B verify_analysis.py
    python3 -B check_registered_reader.py new-unused-L16-fixture.state

On a C++20 host with Boost.Multiprecision, materialize the SHA-checked kernel
sources from the declared Git pin, then run the parity, capacity, stream and
controller fixtures. SHA256SUMS includes these materialized inputs and outputs.

    python3 -B materialize_upstream.py
    sha256sum -c SHA256SUMS
    python3 -B check_capacity.py
    python3 -B check_kernel_parity.py
    python3 -B check_adapter_fixture.py
    python3 -B check_stream_fixture.py
    python3 -B check_driver_fixture.py

check_reader_capacity.py constructs non-Gibbs fields for operational checks
on the registered sides. Its output measures software behavior on those
fields. The fixture commands produce no phase or tail estimates.

## Execution and custody

After the public preregistration commit and execution record are pinned,
build the sampler using the recipe in SAMPLER_ADAPTER.md and retain the
compiler and sampler digests. The volume driver is run once per registered
volume. It records the executable, settings, protocol logs and per-state
SHA-256 and enclosures. The execution record fixes platform availability,
longdouble precision and the wall-time budgets. The output directory for
each volume is new. Before a volume is admitted to a primary decision, replay each of its saved
states under the same executable and settings. Supply the resulting
replay-receipt.json to the primary analyzer using --replay-receipt.
No thermal endpoint is chosen from a measured observable.

    python3 -B run_ordered_volume.py --help
    python3 -B replay_ordered_volume.py --help
    python3 -B analyze_ordered.py --help
    python3 -B analyze_descriptive.py --help

The primary analyzer consumes each volume's receipts and measurement file.
Repeated --thermal-receipts options supply the distinct volume receipts.
The descriptive analyzer takes one complete volume file and reports
secondary means and standard errors, packet checks and paired primary
covariance. The estimates and diagnostics remain finite-volume results.

For a chain accepted at thermal endpoint T, the driver and complete digest
replay execute the sum of the candidate endpoints through T plus 2(T+4096)
macrocycles. For the first endpoint, that is 11,264 per chain. For the last
endpoint, it is 39,936. The four serial chains at L=64 therefore need at least
45,056 macrocycles for an admitted volume. A single cold engineering
macrocycle took 62.05 s after the exact-throughput changes. At that timing,
the earliest serial L=64 workload projects about 32 days for the sampler
alone. An execution allocation must include state reading, uncertainty in
the macrocycle timing and the later possible thermal endpoints.

Uncompressed link payload for the saved states would total 1,820,009,168,896
bytes. Streaming caps the number of raw states held by each worker.
