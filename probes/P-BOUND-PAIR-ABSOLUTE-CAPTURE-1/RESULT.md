# Absolute capture: first bounded certificate

Status: CERTIFIED

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

**NON-CANONICAL / L1. Conditional on the fixed model and the analytical
premises identified in SOURCES.md.**

Reservation: [#1814](https://github.com/mathorn1973/twist-j/issues/1814).
Prospective pin: `173ca05aab8fac006a5e4d54d640f8a9eff35d18`.

## Result

The first accepted execution of the unchanged pinned verifier enclosed the
original normalized joint bound-pair / positive pulse / record event by

\[
\boxed{
\frac{293166031669590845829}{2^{96}}
\le P_{\rm win}(0)\le
\frac{352434475368785347398}{2^{96}}.
}
\]

Its outward decimal enclosure is

```text
[0.00000000370027553796680399304109,
 0.00000000444834846832819836143547]
```

The exact raw endpoints satisfy `U/L < 1203/1000 < 10`, so the
predeclared factor-ten criterion is met. This is a bounded interval, not
a claim that a center estimate has all the displayed decimal digits.
The initial coarse absolute bracket spanning about 21 orders of magnitude
has been replaced by this complete-event enclosure for the same source
and event. No new source normalization or fitted factor was introduced.

## Complete boundary accounting observed in the run

The geometry census completed after 320 uncached model evaluations and
covered the entire integration circle for both pulse signs. It certified
six root families, three for each sign. Exactly one plus-pulse family lies
wholly in the selected outgoing momentum window; all six families remain
in the full denominator through their real coarea weights and periodic
principal-value subtraction. The continuum is also integrated for both
signs. No branch, pole, continuum region or part of the external rectangle
was discarded.

The complete uniform boundary enclosures on the original K,E rectangle are

| Function | Real part | Imaginary part |
|---|---|---|
| F1 | `[0.194310059252396773,0.201257266438878522]` | `[-0.522349346477898097,-0.512374423290279334]` |
| F2 | `[0.932192331491960723,1.008883313024726588]` | `[0.148798318546422651,0.674090864437947793]` |

F1 stopped with 95 live panels and 126 panel evaluations, meeting its
predeclared width target. F2 used the full 4096-panel budget and 8128 panel
evaluations. Its early-stop width target was not met (`target_width=0`),
but every panel had a valid bounded enclosure. The preregistration
explicitly permits that complete range sum. The actual final probability
interval, not the early-stop flag, determines CERTIFIED. There was no
outer subdivision or exceptional-set excision.

## Execution and evidence

The first process exited zero with empty stderr and no timeout. Exact
stdout is in `EXPECTED.txt`; `RUN.md` preserves its 1387 bytes, 16 lines,
SHA-256, environment, execution order and all six pinned input hashes.
The public pin readback preceded execution. No scientific rerun, altered
threshold, expanded budget or post-pin input repair produced this result.

The required unchanged PR workflow reproduces the same committed stdout
on x86_64 and aarch64. Its actual final-head checks determine whether that
repository reproducibility requirement has been satisfied. The local run
alone is not a two-architecture claim. The derivation and component review
within this continuing session are authoring review, not external
independent theorem acceptance.

## Consequence and limits

This supplies the missing absolute normalization for the already defined
capture family. Wherever the conditional finite-window predecessor gives
`R_minus(p) <= P_win(p)/P_win(0) <= R_plus(p)` with nonnegative bounds,
the same prepared family consequently satisfies

\[
 L R_-(p)\le P_{\rm win}(p)\le U R_+(p),
\]

where L,U are the exact endpoints above. This statement transfers the
predecessor's existing finite-window bounds. It does not promote the
zero-window density ratio to an exact finite-window identity and does not
extend the prepared experiment beyond its previously proved domain.

The probability is for the specific normalized input and the complete
asymptotic joint event frozen in PREREG.md. It is not a general collision
rate, an arbitrary preparation, a finite-time detector efficiency or a
particle assignment. It supplies no physical unit conversion or native
port-preparation/reset mechanism. Canon v106, the registry, frontier,
gates, workflow and predecessor probe remain unchanged.
