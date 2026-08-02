# RESULT C-CM-2I-QCARRIER-1, 2026-08-02

NON-CANONICAL. Recorded run of the incubation candidate.

## Recorded leg

```text
leg 1  x86_64, Ubuntu 24.04.3 LTS (WSL2), Python 3.12.3
       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
verify_cm_2i_qcarrier.py   exit 0, empty stderr, 10 gates,
                           10 PASS, 0 FAIL
  stdout cm_2i_qcarrier.stdout.txt
  sha256 ee7af3c974356d56b0ff20989507dab3d7ef482cbb661b44bfbd626bbc25bb60
  3073 bytes
```

One architecture recorded; incubation pins, not a public probe; the
POLICY section 4 two-architecture gate is NOT claimed.

## Per-claim outcome

```text
Q1        candidate-T   COLOR-INTEGRAL-LIFT reproduced (120, det 1)
Q2        candidate-T   Galois branches meet exactly in <S>, the geometric C4
Q3        candidate-T   sigma descends with markings intact (traces in F)
Q4        candidate-T   multiset twist-blind; tau moves all 48 golden traces
Q5        candidate-T   tau(G) a second integral model, distinct set
Q6        candidate-T   pair character Q-valued: pair is C4-closed
Q7-Q8     candidate-T   H0 Hermitian, invariant, totally positive definite
Q9        candidate-T   invariant forms exactly one F-line; H0 in it
Q10       candidate-T   descent = ker chi5; coset acts by outer 5a<->5b swap
```

## Falsification first

Any FAIL fires F-QC-1; F-QC-2 and F-QC-3 are armed as stated.
No falsifier fired. No threshold moved. PROMO deferred.
