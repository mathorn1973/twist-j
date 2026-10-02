# RESULT, ADDENDUM 1: C-NATIVE-FIBRE-PENTIT-WIGNER-N

**NON-CANONICAL. Candidate labels only. Action layer L1. No registry, frontier
or Canon row is changed.** Date 2026-10-02. Authority: Public Canon v97, tag
`canon-v97`, main `738e0421bd15aaea5bb6ef2a56f1cab752d44de5`.

This record extends, and does not replace,
`RESULT-C-NATIVE-FIBRE-PENTIT-WIGNER-N_2026-10-02`. The base preregistration,
verifier, stdout and result are untouched; both pins were re-hashed after the
addendum run and are intact.

Outcome in one sentence: the declared QDD reading leaves point counting
through its **measurement** as well as through its preparations, and the
frozen class of line preparations, line readers and the update U1 is an exact
counting contract that consumes one fresh uniformly counted pentit per
reading. Outcome for occurrence: `STOP_APPLICABILITY / H_NOT_TESTED` of
`C-OCCURRENCE-CYCLE-COUNT-N` is unchanged.

## 1. Custody

```text
PIN ADDENDUM 1 recorded 2026-10-02T17:10:53Z, before the first execution
  f5c518380864989d07fc37c381e12bec984b1408b73ff6d6b5319a55324a7d17  ADDENDUM-1-PREREG
  cd609366fb656ca79fd91e7a7090ea35f0974e85bfe5f3616866df27dfe4b346  addendum verifier
First execution of the pinned addendum verifier
  exit 0, stderr empty, 12 of 12 checks PASS, under 1 second
  stdout 2436 bytes
  fc5432d288f340038d64edb5ceab9aeec71c3b400cc378c8556878089b549bed  stdout
  platform Ubuntu 24.04, architecture x86_64, CPython 3.12.3
  rerun on the same architecture: byte-identical (reproduced, not a second leg)
Breaker, written after the first run, independent code path
  6bac007185d0c4424f761b337a8f30a43209d93b250033c69207a4e6935bc816  breaker
  6e3aa7f8eac8d2df31f6c60f4e2b5cfa78c11a4092501b4a5defa1a12a733bd6  breaker stdout
  exit 0, stderr empty, 11 of 11 checks PASS, 1403 bytes
Base pin, unchanged
  cbda8c9f0fbc7da3b5baeed685d9e8592ecffaa6b70617633a271056ca94757c  PREREG
  ddf883612cd6fff00b227d8fca76668fc876ef1873f819da724ee0e66426dd63  verifier
```

The addendum verifier was edited once before its pin (a vacuous comparison in
the U0 control was written out explicitly). It was not executed before the pin.

## 2. Results by claim

| Claim | Content | Label |
| --- | --- | --- |
| B7.1 | dual uniqueness: `xi_E(u) = Tr(E A_u)` is the only function on the 25 points whose line averages are `Tr(Pi_L E)`; an effect is a point reader on line preparations exactly when `0 <= xi_E <= 1` | candidate-T |
| B7.2 | LOW response: 1 once, 3/4 four times, -1/4 four times, (1+sqrt5)/8 eight times, (1-sqrt5)/8 eight times; twelve negative values; LOW is no point reader, deterministic or stochastic | candidate-C |
| B7.3 | control: `f` is a line state of direction (1,0) and `|<l,f>|^2 = 1/4`, not a multiple of 1/5 | candidate-T |
| B7.4 | LOW probability on the 30 line states: 4/5 and 1/20 x4 on basis states, 0 and 1/4 x4 on Fourier states; exactly two multiples of 1/5 | candidate-C |
| B7.5 | acceptance `I - |+><+|` is a deterministic point reader: the indicator of the complement of the line `r=0` | candidate-T |
| B7.6 | HIGH has response values outside [0,1] and is no point reader | candidate-C |
| B8.1 | `Pi_M Pi_L Pi_M = (|L cap M|/5) Pi_M` for all 900 pairs | candidate-T |
| B8.2 | with U1, counting 125 microstates returns the two-round law in all 1080 scenarios, repeated and changed context | candidate-T |
| B8.3 | with U1 the final point is uniform on the last outcome line | candidate-T |
| B8.4 | necessity: every reading consumes at least one uniformly counted five-valued coordinate; no function of the point alone can serve | candidate-T |
| B8.5 | control: U0 returns the first outcome with count 1 where the law gives 1/5, in all 900 three-round scenarios; U1 gives 1/5 | candidate-T |
| C2 | applicability | disposition unchanged |

No falsifier fired in the pinned run or in the breaker.

## 3. Found, not seen before the freeze

1. LOW probability on the twenty remaining line states:
   `(3-sqrt5)/10` twice, `(3+sqrt5)/10` twice, `(7-sqrt5)/40` eight times,
   `(7+sqrt5)/40` eight times. The predicted candidates `(17+-sqrt5)/40` do
   not occur.
2. HIGH response: `-1` once, `1/4` eight times, `(7-sqrt5)/8` eight times,
   `(7+sqrt5)/8` eight times. One value below 0, eight above 1.
3. Breaker searches: none of the 50 native fibre maps used as a fixed update,
   and none of the 3125 outcome-indexed shifts along the reading direction,
   reproduces the two-round law. This agrees with B8.4 and adds nothing beyond it.

## 4. What this adds to the base result

1. The boundary of counting is two-sided. Preparations: every real sum-zero
   state has a negative Wigner function (base B3). Readers: LOW and HIGH are
   not point readers even on nonnegative line preparations (B7). Acceptance
   is a point reader (B7.5). The split lies between acceptance and LOW/HIGH.
2. The class in which counting is exact is now frozen with its state change:
   line preparations, line readers, update U1. In that class repeated and
   changed context are reproduced exactly by counting (B8.2).
3. The price is explicit: one fresh uniformly counted pentit per reading
   (B8.4). A reading that leaves the point in place is refuted on three
   rounds (B8.5).

## 5. What is not claimed

No occurrence law. The counts of B8 are ensemble counts over `(u,t1,t2)`, not
frequencies along one trajectory. No native source or renewal of the fresh
coordinate is exhibited; the five-to-one merge of the native law is not
identified with one. U1 is one admissible update; uniqueness is not claimed.
No statement about larger carriers, contextual apparatus or other readings.
No complete apparatus class for `QDD-INSTRUMENT-CLASS-COMPLETENESS`: B7 and
B3 show that such a class must classify readers as well as preparations.

## 6. Delta for PROMO-C-NATIVE-FIBRE-PENTIT-WIGNER-N

Two statements are added to section 2 of the proposal; everything else stands.

**S7, reader boundary.** `xi_E(u) = Tr(E A_u)` is the unique point response
with the line averages of `E`. For the LOW projector of the declared reading
it takes twelve negative values, and on the Fourier line state the LOW
probability is `1/4`. The acceptance projector has a 0/1 response. Proposed
status: T for uniqueness and for the control value; C, conditional on the
declared reading, for the LOW and HIGH tables.

**S8, counting contract with state change.** For line preparations, line
readers and the update `u -> u + t delta` with one fresh uniformly counted
`t` per reading, counting returns the two-round law
`Tr(Pi_L Pi_M1) Tr(Pi_M1 Pi_M2)` in all 1080 scenarios; at least one such
coordinate per reading is necessary; the non-disturbing reading fails on
three rounds. Proposed status: T. Scope note for the row: ensemble count at
L1, no event contract, no native source of the coordinate.

Dependency edges: `S7 -> S4`, `S8 -> S4`. Falsifiers as in the addendum.
Additional pins: the four hashes of section 1. No H or O row closes.
