# P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-2 result

Status: **WARD_ENGINE_QUALIFICATION_PASS / ZERO_ENGINEERING_ONLY / non-canonical**.

## Recorded decision

```text
source manifest and exact fixture custody:                 PASS
legacy guards at L6/L8 with zero random-bit consumption:   PASS
ExactUInt KAT spans, width-overflow and sum-overflow:       PASS
full small-span table/selection audit:                      PASS
old/new choice, draw, bit-count and successor-bit parity:  PASS
exact weights, interval partition and detailed balance:    PASS
synthetic failing spec, two return codes and pipe custody:  PASS
bounded stderr prefixes, byte counts and SHA-256:           PASS
at least two queued futures cancelled before start:        PASS
dequeued queued wrappers starting a child:                  0
running sibling engine and reader killed and reaped:       PASS
all futures completed:                                      PASS
reader-spawn and thread-start fault cleanup:                PASS
surviving child PIDs:                                        0
exact fixture stdout, empty stderr and exit code:           PASS
terminal:                                    WARD_ENGINE_QUALIFICATION_PASS
evidence weight:                             ZERO_ENGINEERING_ONLY
production firewall F3:                     NOT SATISFIED
production issue #742:                      FORBIDDEN
```

The deterministic verifier completed once at the public source pin. The
authoritative terminal in `EXPECTED.txt` is exactly:

```text
TERMINAL WARD_ENGINE_QUALIFICATION_PASS
```

The old implementation failures were reproduced without consuming a random
bit: `orbit_integer_weight_overflow` at the exact synthetic spreads 72 and
128, `bitstream_bits_width_exceeds_63` at a representable total requiring 64
bits, and `orbit_weight_sum_overflow` above the uint64 total. The qualified
path samples every such table with a repository-owned standard-C++17
`ExactUInt` and unbiased bounded rejection. It imports no Boost or other
third-party integer dependency.

Whenever the inherited sampler could complete, the new dispatcher calls the
whole old uint64 implementation. The exhaustive small envelope and frozen
known-answer tests preserve selected index, draw, consumed-bit count and
following stream bits. This qualification therefore changes no formerly
executable mobility transition and does not itself require a new mobility
qualification.

The supervisor result is likewise engineering-only. It preserves the failing
specification, both child return codes, bounded stderr prefixes, complete
stderr byte counts and hashes, and pipe custody. One integrated failure
decision cancels queued work, terminates and reaps a running sibling, waits for
all futures and leaves no surviving direct child.

## Consequence and boundary

This local PASS is only the technical prerequisite for the required public
two-architecture replay and a separate governance decision on retaining the
#772 sector-umbrella wrapper. It does not itself make that decision and does
not reserve or authorize CROSSCHECK-3. Any later cross-check requires a fresh
identifier, sources, paths, seeds, receipt and one-shot execution after the
separate governance readback.

No Ward observable or residual was evaluated. F3 remains unsatisfied and
production #742 remains forbidden. No Canon, Registry, Frontier, program
status, phase, photon, propagator, polarization, Born selection, matter/light
split, contraction/expansion or cosmological claim changes. Public Canon
remains v74.
