# RESULT C-CM-2I-QCARRIER-2, 2026-08-02

NON-CANONICAL. Recorded run of the incubation candidate.

## Recorded leg

```text
leg 1  x86_64, Ubuntu 24.04.3 LTS (WSL2), Python 3.12.3
       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
verify_cm_2i_qcarrier_2.py   exit 0, empty stderr, 11 gates,
                             11 PASS, 0 FAIL
  stdout cm_2i_qcarrier_2.stdout.txt
  sha256 84ec41562374ab4cb8f91a90314b3bec6aacd27e346366d01fe1f592c8682cde
  2270 bytes
```

One architecture recorded; incubation pins, not a public probe; the
POLICY section 4 two-architecture gate is NOT claimed.

## Per-claim outcome

```text
N1-N3   candidate-T   lift reproduced; intertwiner line unique; C pinned
N4-N5   candidate-T   cocycle mu = -phi^2 totally negative; nu^4 = 1
                      unreachable; obstruction class [-1]
N6-N8   candidate-T   explicit nu: equivariant, nu^2 = sigma-descent,
                      nu^4 = -1, nu^8 = 1 (order eight)
N9      candidate-T   the same central sign as the S spinor lift, the
                      glue phase, and the half-tick obstruction
N10-N11 candidate-T   branch swap bookkeeping; Gram transport with
                      totally positive multipliers
```

## Falsification first

Any FAIL fires F-QC2-1; F-QC2-2 and F-QC2-3 are armed as stated.
No falsifier fired. No threshold moved. PROMO deferred.
