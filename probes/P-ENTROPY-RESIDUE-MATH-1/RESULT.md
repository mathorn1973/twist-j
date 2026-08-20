# P-ENTROPY-RESIDUE-MATH-1 result

Status: `PROVED AND AUDITED / CANON UNCHANGED`

## Disposition

```text
toral entropy:  h_top = h_Haar = 2 log phi, carried by the exact Z[phi]
                factorization of the characteristic polynomial (complex
                pairs of squared moduli phi^2 and 2 - phi) plus the
                imported entropy formula; fixed-point table decided by
                two independent exact paths for n = 1..15, witness
                #Fix(T^15) = 1860496.
driver:         the Thue-Morse driver has entropy rate 0; exact factor
                counts to L = 20 with a stabilization witness,
                p(20) = 60.
residue:        R(q) = 2 log phi - h(q) lies in [log(phi^2/2), 2 log phi]
                with the strictly positive floor phi^2 - 2 = 1/phi and
                the exact split identity 2 log phi = log 2 +
                log(phi^2/2); deterministic reads attain the ceiling;
                floor attainability is not claimed.
integrity:      no STOP. One formal execution, exit zero, empty stderr,
                8/8 gates PASS, stdout equal to EXPECTED.txt.
```

## Proposed registry consequence (a later sealed fold, not this probe)

J-TORAL-ENTROPY [T], TM-ENTROPY-ZERO [T], BINARY-READ-RELATIVE-ENTROPY
[T]; exact row texts frozen in PREREG.md. This gives the entropy rate
2 log phi its first public canon anchor. ENTROPY-LAYER-BRIDGE [O] is
untouched: the identification of the toral rate with the declared
architecture's tick remains exactly as open as that row states, and this
probe must never be cited as closing or weakening it. The incubation
lane's canonicity hypothesis (a saturating binary read) is not carried.

## Evidence boundary

Local formal leg x86_64 (Ubuntu 24.04.4 LTS, CPython 3.11.15); the
pull-request workflow supplies the x86_64 and aarch64 replays against
EXPECTED.txt, completing the repository two-architecture computation
gate. Universal statements carry labeled imports: the entropy formula
for hyperbolic toral automorphisms and the equality of topological and
Haar entropy; the exact Thue-Morse complexity formula (Brlek; de Luca
and Varricchio); entropy monotonicity under factors. Everything else is
exact arithmetic audited by the verifier. No physical reading is added
anywhere.
