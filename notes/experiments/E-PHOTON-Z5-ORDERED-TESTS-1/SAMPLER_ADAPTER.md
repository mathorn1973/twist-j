# Ordered packet sampler adapter

This adapter is part of the unexecuted NON-CANONICAL preregistration.
The exact transition source is copied byte for byte from public revision
`c089e7ec7ecc82f4838c27663d94c040f5cc4ea3`, directory
`probes/P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/`.
`prepare_capacity.py` verifies all five published source hashes and changes
five guarded blocks in a separately generated `kernel64/` copy:

1. `LineFaces` capacity `6 * 16` becomes `6 * 64`.
2. The inherited generic CLI size guard `[2,16]` becomes `[2,64]`.
3. Constructor duplicate-ID validation sorts a copied array of face IDs and
   uses adjacent_find instead of comparing every pair. The affected face
   array, its iteration order, masses, counters and updates remain untouched.
   Sorting detects a duplicate exactly when some pair was equal, with the
   same failure string. This is validation-only algorithmic equivalence.

4. The exact categorical sampler packs each original 64-bit block into an
   unsigned word in the same bit order before appending it to the unbounded
   prefix. By positional arithmetic this is the same prefix after every
   complete block, with the same 64/128/192/256-bit checks.
5. For line masses the even face weight turns f+s*delta into s*f+delta.
   Count signed residues once. For each candidate its exact mass is
   4^z * phi^(2(n-f)), with z, n, f the counts of zero, near and far
   residues. A table of exact powers and binary shifts of both coefficients
   supplies the same unnormalized masses in the original candidate order.

The upstream source and the categorical rule, random namespace, sweep order, mass,
line move, flat sheet, charge conjugation or prefix cap is edited. This is a
new capacity, validation and exact throughput adapter with a prospective pin, not a modification
or replay of the sealed historical pilot.

## Build and small integrity checks

Requirements: C++20 g++, Boost.Multiprecision headers, Python standard library.
```sh
python3 -B prepare_capacity.py
python3 -B check_capacity.py
python3 -B check_kernel_parity.py
python3 -B check_adapter_fixture.py
python3 -B check_stream_fixture.py
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -Werror line_mass_fixture.cpp -o /tmp/ordered_line_mass_fixture
/tmp/ordered_line_mass_fixture
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic -Werror ordered_sampler.cpp -o /tmp/ordered_sampler
```

The geometry check uses no states or random draws. The parity check builds
original and adapted sources separately and compares the inherited
two-cycle L3/L4 fixture bytes. The exporter check uses precisely those same
two-cycle fixture seeds and hashes. Neither script invokes a pilot or a
production schedule. These are pre-pin engineering checks, not formal receipts.

## New adapter CLI

The original ten named arguments are mandatory; duplicates and unknown options fail.
All numeric values, including the seed, are canonical unsigned decimal.
Optional --transport files|stream defaults to files; optional
--thermal-sentinels 0|1 defaults to 0. The controller freezes both explicitly.

```text
/tmp/ordered_sampler --mode run --L L --seed SEED --start hot|cold
  --thermal T --samples N --between B --chain CHAIN --output-dir NEW_DIRECTORY --t 1
```

This is a command template only. No target chain has been executed.
The driver must supply a schedule frozen before its public pin. This adapter
does not retune, extend, restart or replace a chain. An existing output
directory is rejected. Partial output remains an incomplete failed attempt.
The caller owns SHA-256 state manifests, runtime caps, immutable logs,
mixing analysis and the public execution authorization.

## Stream transport and blinded prefix replay

With --transport stream, --output-dir must be the literal `-`; no state
directory or raw state file is created. Each exported state is framed by
ASCII/LF records, with decimal byte length B owning only the seven-line state:

```text
STATE_BEGIN sample=N bytes=B
<exactly B canonical state bytes, ending in LF>
STATE_END sample=N
```

The adapter flushes and waits for exactly `ACK N\n` on stdin before writing
the sample sentinel or advancing the chain. The controller must parse and hash
all B bytes, check the closing frame and custody row, and only then ACK.
Malformed, oversized or missing ACK fails closed; an external controller
deadline owns timeout and termination. One state at a time is outstanding.
No partial state is accepted as a replay checkpoint.

With --thermal-sentinels 1, each complete thermal macrocycle emits
`THERMAL_SENTINEL macrocycle=N` followed by the identical inherited SAMPLE
line with index=N-1 and flushes stdout. --samples 0 is allowed only when
thermal>0 and thermal-sentinels=1. Such a blinded endpoint pass exports no
states but still emits UPDATE_DIAGNOSTICS, complete inherited diagnostics,
and ORDERED_STATUS GENERATION_COMPLETE_UNCLASSIFIED.

Prefix replay starts a fresh process with the identical seed, initial state
rule and macrocycle order. The coordinator compares sentinel fingerprints at
matching prefix endpoints before accepting later states. Increasing a frozen
endpoint is not continuation from a saved field: it repeats the prefix cost.
The complete prefix endpoint and replay schedule must be pinned in advance;
no endpoint may be chosen after inspecting phase or packet measurements.

Replay custody must retain exact source hashes, compiler binary and version,
compile flags, executable byte count and SHA-256, runtime/library versions,
environment, command arguments, seed/start/counter schedule, stdout/stderr
logs and exit status, plus every state byte count/SHA-256 and reader receipt.
State hashes alone do not reconstruct states. Reconstruction requires running
the identical deterministic prefix again and verifying each state hash before
use. No raw-state persistence is claimed for stream transport.

`--mode synthetic-zero` requires cold, T=0, N=1, B=1; it exports a constructed
zero field with MACROCYCLE=0, invokes no kernel, and prints SYNTHETIC_ONLY.
`--upstream-self-test` alone runs the inherited small integrity checks.

The state schema is exactly seven LF-terminated lines:

```text
TWISTJ_Z5_ORDERED_LINK_STATE_V1
L=<2..64>
CHAIN=<identifier>
SAMPLE=<zero-based sample>
MACROCYCLE=<completed macrocycles>
LINKS=<4*L^4 digits, original site-major/direction-major order>
END
```

For genuine scheduled exports, sample s has MACROCYCLE=T+(s+1)B.
Only links are exported. No cached observables are inputs to the independent
reader. The adapter preserves the sixteen inherited sampler sentinels:
logw; polyakov_radius_mean; polyakov_radius_0..3; vortex_density;
monopole_density; score_mean; flux_asym_14; flux_asym_23;
flux_fraction_0..4. Exact flux counts, state/cache fingerprints and original
update/prefix diagnostics accompany them. Fingerprints are not custody hashes.
Sentinel numerical values are engineering floating-point diagnostics; kernel
categorical decisions remain exact algebraic decisions.

## Capacity and runtime audit

At L<=64, V=L^4, 6V<2^31 and 4V<2^32. Thus inherited signed site/face
arithmetic and Philox uint32 ordinals fit. The adapter checks the total
macrocycle count against uint32 and bounds worst-case diagnostic bit counts
and uniform-rejection counters before constructing a lattice.
Line masses use unbounded cpp_int coefficients. The only size-dependent
fixed line array found is the explicitly enlarged one.

At L=64 the three coordinate/neighbor arrays plus links and flux require
58L^4=973078528 bytes before other allocations. The inherited pairwise
constructor check would perform
4L^3*(6L)*(6L-1)/2=77108084736 comparisons. The guarded sort replacement
instead validates 4L^3 arrays of 6L IDs with O(L log L) work per array.
One macrocycle makes 4L^4 local and 4L^3 line categorical decisions;
line mass reconstruction processes 6L faces once and forms five exact masses.
The update work therefore grows at least as L^4, with increasing integer
operand sizes, and the new constructor validation grows as O(L^4 log L).
Two target-size engineering fixtures at L=64 used a cold start and a single
macrocycle at the inherited fixture seed. They emitted sentinels and counters
with zero saved states. Baseline wall time was 115.43 s and the combined
exact-throughput build took 62.05 s. Their ASCII transcripts have the same
SHA-256 after substituting the common chain label in the ORDERED_RUN header;
the rest of the transcript was byte-identical. The state fingerprint, cache
fingerprint and exact update counters were included. The normalized digest is
c55679e04994841d27ec8f8987f63b8dd062cab1431a78ef992ec6698406944c.
These are single-cycle checks and timing estimates. The measured workload uses
long equilibrated prefixes and separate costs for state streaming and replay.

The saved payload alone has 4L^4 bytes. L64 is 67108864 bytes per state,
requiring external manifest custody under public file-size policy.
The original #742 production firewall and its F3 requirement remain separate
and unchanged. This adapter emits no phase classifier or Canon conclusion.

For L={16,24,32,36,40,48,64}, four chains with 1024 thermal plus 4096
measurement macrocycles require exactly 2318763294720 local-plus-line
categorical decisions before any replay. Four times 4096 saved states per
size would require 1820009168896 payload bytes (1695.015625 GiB), before
headers and manifests. L64 alone contributes one TiB. A controller that ever
spools states must reserve this full declared amount plus bounded overhead
before starting, or fail closed. Streaming must bound simultaneously resident
state buffers and worker count; one L64 payload is 67108864 bytes, besides
the sampler and reader working arrays. These are exact counts, not measured
execution times or a prediction of mixing.
