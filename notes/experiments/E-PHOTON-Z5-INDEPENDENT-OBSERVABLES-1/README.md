# E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1

**Status:** COMPLETE PRE-PIN CANDIDATE / UNEXECUTED / ZERO-EVIDENCE / NON-CANONICAL

**Public reservation:** issue #748

**Parent:** issue #742

**Base:** `59cee594b974be6ccddf9785d35cf9da750d36a6`

This directory contains the complete pre-pin candidate for the independent
saved-state reader required by the photon production firewall. Its current
inventory is:

```text
PREREG.md                              scientific and integrity contract
README.md                              status, architecture and pin/run procedure
STATE_SCHEMA.md                        state, custody and reader-record schema
fixture_oracle.py                      independent Python fixture oracle
independent_reader.cpp                 compact production C++ reader
verify.py                              one-shot fixture gate
SOURCE_SHA256SUMS                      exact TSV source/fixture custody
fixtures/contractible_vortex.state
fixtures/contractible_vortex_cc.state
fixtures/flat_holonomy.state
fixtures/monopole_nonwrapped.state
fixtures/monopole_wrapped.state
fixtures/periodic_orientation.state
fixtures/support_winding_zero_charge.state
fixtures/wrapped_vortex_pair.state
fixtures/zero.state
```

The candidate is not yet an accepted public pin and has no formal stdout or run
result. Nothing in this directory authorizes execution of a production chain.

## Frozen architecture

The implementation candidate has two structurally independent paths:

```text
production path  compact C++ reader, 2 <= L <= 32
fixture path     independent Python oracle on small periodic lattices
```

The C++ path must be feasible at `L=32`: `O(L^4)` working memory apart from
serialized output, no dense `O(L^8)` matrices, and complete termwise
correlator work over `n=1..floor(L/2)`. It receives only a canonical state file
and the expected whole-file SHA-256 already resolved from the external
`SOURCE_SHA256SUMS` custody manifest by its caller or verifier.

The Python oracle independently reconstructs the same small-lattice fixture
answers. It must not import or reuse C++ logic, invoke the C++ reader to create
expected values, use FFI into it or accept sampler observables as truth.

Both paths implement the public equations in `PREREG.md`; neither imports the
primal sampler's observable implementation.

## What the reader returns

For each verified link state, the candidate reader returns exact Python
sort-key canonical JSON with top-level keys in this order

```text
correlator
flux
monopole
polyakov
schema
state
vortex
```

The record owns only exact reconstruction and sufficient statistics:

- independently oriented plaquette flux and exact counts;
- all four Polyakov phase histograms, which exactly determine the
  direction-wise `r,u,v` statistics;
- principal-flux monopole current and local closure;
- per-component charged vortex `H_2(T^4;F5)` wrapping;
- per-component charged monopole `H_1(T^4;Z)` wrapping and complete tails;
- exact product/left/right Z5 phase histograms for all 24 correlator terms and
  every `n=1..floor(L/2)`.

It does not choose a block length, center a correlator per configuration, run a
jackknife, apply a wrapping probability threshold or classify a phase.

## Current allowed work

Before the candidate pin, the following are permitted:

- review and correction of the pre-pin documents;
- implementation development;
- compilation and static analysis;
- explicitly non-formal development tests on synthetic states.

The following are forbidden now:

- the formal fixture gate;
- generation, opening or inspection of a production state;
- a run under any of the twenty production seeds;
- an `EXPECTED.txt`, `RUN.md` or positive reader result presented as earned;
- any phase, Canon, Registry, Gate, Frontier or production-status change.

## Frozen candidate command and environment

`SOURCE_SHA256SUMS` has magic
`TWISTJ_Z5_SOURCE_SHA256SUMS_V1` and exactly one sorted row for every listed
document, source, verifier and fixture except the manifest itself. A manifest
cannot recursively hash its own row; the public pin and readback receipt own
its exact bytes and SHA-256. File names may not be silently substituted after
the pin.

The exact formal command from the repository root is

```text
python -B notes/experiments/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1/verify.py
```

The neutral environment is exactly

```text
operating system  Windows NT 10.0.26200 x64
Python            3.12.10
CXX               unset; verifier resolves g++.exe
compiler          g++.exe MinGW-W64 x86_64-ucrt-posix-seh
                  Brecht Sanders r7, version 15.2.0
compile flags      -std=c++20 -O2 -Wall -Wextra -pedantic
bytecode policy    Python -B; no repository __pycache__
```

## Formal pin and readback protocol

The formal sequence is:

1. Commit the complete accepted candidate: final documents, C++ reader,
   independent Python oracle, fixtures, verifier and all source hashes.
2. Push the candidate to
   `experiment/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1` without amending or
   rewriting it.
3. Read back the exact commit and every pinned byte from the public remote.
4. Confirm a clean checkout and repeat every pinned SHA-256.
5. Run the exact `python -B .../verify.py` command frozen above from the
   repository root, with the frozen neutral environment.
6. Require exit zero, empty stderr and one complete ASCII/LF terminal record.
7. Save stdout byte for byte as `EXPECTED.txt` and record the neutral pin,
   command, environment, byte count and hashes in `RUN.md`.
8. Preserve either modeled terminal honestly. A fired integrity falsifier is
   not repaired and rerun under this pin.
9. Require the repository's generic changed-note checks on both `x86_64` and
   `aarch64`, plus the aggregate required context, to pass for the pull request.

The fixture gate is a pinned one-shot local execution. While this remains an
`E-...` experiment lane rather than a public `P-...` probe, the generic GitHub
jobs audit the repository and pull request; they are not represented as an
automatic replay of the formal reader gate.

A crash, nonzero exit or failure to produce a complete modeled terminal is an
abandoned pin under repository policy. The identifier is consumed; the pin is
not repaired, resumed or renamed.

## Exact terminal boundary

A completed gate emits exactly one of these two complete stdout records and no
other byte:

```text
STOP_INTEGRITY
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

or

```text
INDEPENDENT_READER_FIXTURE_PASS
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

Only the second terminal, merged after both architecture checks and publicly
read back, satisfies reader clause `F2` of the PR #768 firewall. It still does
not start production: the separate #756 execution must first return
`DUAL_CROSSCHECK_PASS`.

No reader result may contain or imply `PHOTON_EVIDENCE`, confinement,
`Z5_BROKEN_EVIDENCE`, a transition, a thermodynamic limit, pole
identification or a physical photon.

## Production firewall

The complete start condition remains

```text
F1  PR #768 freeze merged and read back          satisfied at the base
F2  #748 reader frozen and exact fixtures PASS   not yet satisfied
F3  #756 L=6,8 execution DUAL_CROSSCHECK_PASS     not yet satisfied here
```

No action in this pre-pin candidate directory changes those facts.
