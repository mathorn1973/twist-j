# P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2 result

Status: `PILOT_READY_FOR_PRODUCTION_PREREG / ZERO_PILOT_ONLY / PUBLIC REPLAY PENDING`.

## Recorded decision

```text
kernel audit:       PASS
pin/reference:      PASS
raw custody:        PASS
analyzer custody:   PASS
mixing failures:    NONE
wrapper terminal:   PILOT_READY_FOR_PRODUCTION_PREREG
evidence weight:    ZERO_PILOT_ONLY
```

One authorized execution completed all eight frozen chains, 4,096 samples and
439,418,880 exact heat-bath decisions. The eight raw logs total 2,978,050 bytes.
Every process exit was zero, every captured stderr was empty, and every raw
byte count and SHA-256 matches `PILOT_RUNS.tsv`. The final and authoritative
line of `EXPECTED.txt` is exactly:

```text
RESULT PILOT_READY_FOR_PRODUCTION_PREREG
```

## Integrity result

The independent exact-local audit covered 15,625 environments, 78,125 positive
candidate masses and 390,625 detailed-balance pairs. The nondyadic witness is
`4096/4740 = 1024/1185`. The fourteen-file pin, independent reference fixture,
raw custody and analyzer replay all passed.

Every chain reported the exact scheduled local, line, flat-sheet and charge
counts. The smallest selected-nonzero line count was 1,638, every flat-sheet
cache identity passed, bit-cap exhaustion was zero, and the largest prefix used
64 bits against the frozen 256-bit cap.

## Mixing result

All sixteen registered metrics passed every frozen gate at both `L=6` and
`L=8`. The worst observed values were:

| Gate | Worst observed | Frozen threshold |
| --- | ---: | ---: |
| Within-chain variance | about `4.173e-7` | `> 0` |
| Per-chain Geyer ESS | `295.825504349` | `>= 64` |
| Rank-normalized split Rhat | `1.00205751313` | `<= 1.05` |
| Folded split Rhat | `1.00350941353` | `<= 1.05` |
| Pooled bulk ESS | `1514.46534639` | `>= 400` |
| Pooled tail ESS | `1644.2918081` | `>= 200` |
| Hot/cold z | `1.89742442296` | `<= 4` |
| Half-drift z | `2.55823710191` | `<= 4` |
| Distinct state-hash fraction | `1` | `>= 0.99` |

The analyzer therefore emitted `PILOT_FAILURES NONE`. This is an engineering
mixing/readiness result for the frozen finite volumes, not phase evidence.

## Authorized consequence and scope firewall

This terminal authorizes only drafting the separate production preregistration
reserved by issue #757. It does not start that production run and supplies no
thermodynamic limit, photon phase, massless pole, polarization, causal cone,
Born selection, continuum limit, SI quantity, contraction/expansion law,
matter/light split, or visible/invisible sector.

The independent dual/Ward obligation #756 and reader obligation #748 remain
open. No Canon, Registry, Frontier, program-status or authority movement is
made by this pilot. Required clean GitHub x86_64 and aarch64 byte-identity
replays, review and merge remain pending.
