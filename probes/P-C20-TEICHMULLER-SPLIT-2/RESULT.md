# P-C20-TEICHMULLER-SPLIT-2 result

Status: SCIENTIFIC RESULT; FORMAL AARCH64 LEG PASS;
X86_64 REPRODUCTION PENDING; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 6/6 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier fired in the formal aarch64 leg. The frozen proof
establishes the exact C_4 x C_5 split of the J-cycle in R=A_4, the complete
fourth- and eighth-root census in R, the C_4 two-primary subgroup throughout
the declared tower A_m, and the independently reconstructed reduced public
J-STEP operator. The finite verifier exhausts every claim in R and audits the
exact determinant and unit-group facts used by the all-m proof.

This is a transparent proof-first protocol repair with a disclosed known
predecessor result, not blind discovery. It records a scientific result but
does not register a Canon claim or change any existing status.

## Immutable pin and formal leg

```text
public lock:          issue 126
base commit:          633940a0187f7bdac83eae5639844622ad955d9f
preregistration pin: 338a90c6b82a8934a0f7f28090dee51bce6c791c
PREREG.md SHA-256:    b5054f27c7c018f0f8b305b9d26c8f64e34f528e8729eb48d1b8ebfade28733c
verify.py SHA-256:    5ba3680f2cca840ab458e72e8a2f0febb99c732fcacaeadd68c71c020baacd41

run started:          2026-07-23T05:27:59Z
run finished:         2026-07-23T05:33:23Z
platform:             Ubuntu 24.04.4 LTS
architecture:         aarch64
Python:               CPython 3.12.3
checkout:             clean before and after; detached at the exact public pin
deterministic runs:   1
exit/stderr:          0 / 0 bytes
stdout SHA-256:       4cbf934b2220c5a5c3de8169a448baac1396236ebc37c286536c3886bb8d86e8
stdout bytes/lines:   724 / 7
result:               6/6 ALL PASS
```

`EXPECTED.txt` is the exact ASCII, LF-only stdout of this formal leg and has
a final LF. `PREREG.md` and `verify.py` remain byte-identical to the public
pin. The complete neutral return is preserved in issue comment 5054847202.

## Proof and audit verdict

The exact identity `(5)=(lambda)^4` makes A_m a finite local ring with residue
field F_5 and gives `|A_m|=5^m`. In R, the freshman's-dream calculation gives
`J^5=2`, hence J has exact order 20. The elements `t=J^5` and `u=J^16`
have coprime orders 4 and 5, multiply to J, and generate the internal direct
product `<J>=<t> x <u>`.

For every m, the kernel of `A_m^* -> F_5^*` is a 5-group. Therefore the
two-primary subgroup maps isomorphically to the cyclic group F_5^* and is
C_4; no A_m contains an element of order 8. In R the four scalar lifts are
the complete fourth- and eighth-root sets.

The matrix audit constructs M_R from the four reduced public `step(e_i)`
columns and independently from multiplication by J. It checks all 625
vectors, all four basis columns for every exponent `0<=k<20`, the full cycle
and split, and both declared nilpotency indices in Mat_4(F_5). All six frozen
gates pass. The all-m statement rests on the proof above, not on extrapolation
from the finite depth audit.

## Scope firewall

The earned result is confined to exact L1 algebraic state and carrier
arithmetic in the declared cyclotomic quotients. `J-STEP [T]` is its only
claim premise. `FIB-ROOT-TIES [T]` is comparison only.

No time quantum, chronological process, phase, tick, clock, decoder,
quadratic-floor statement, physical carrier, SI scale, uniqueness, or lift
to L2-L6 is earned. `TIME-QUANTUM-TOWER`, `RAMIFIED-TM-LIFT`,
`PENTIT-ROOT-FACTS`, C8, and all decoder and metrology rows are not premises.
No Canon, registry, frontier, dependency, gate, or status change is made.

## Two-architecture gate

PENDING. The formal aarch64 leg uses the pinned verifier, exits zero, writes
empty stderr, and produces the 724-byte transcript in `EXPECTED.txt`. The
required GitHub x86_64 check must reproduce the same verifier hash and exact
stdout before this computation gate can close. Any discrepancy is preserved
as a first-class failure.
