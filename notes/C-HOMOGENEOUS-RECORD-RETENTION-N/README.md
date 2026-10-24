# C-HOMOGENEOUS-RECORD-RETENTION-N

**PUBLIC, NON-CANONICAL. L1 analytical package: how long the receiver of the
v105 homogeneous capture-current-record law holds a written record.**

License: Apache-2.0.
Authority basis: `mathorn1973/twist-j` main
`892a0b11089d34e241e1eb76d2c03247022d18e6` (Public Canon v105, tag
`canon-v105`).

## Question

Public Canon v105 (`HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T]`) proves an
asymptotic joint capture-and-record event with weight above $2/10^{28}$ and a
coherent transfer of old memory into the outgoing pulse. It leaves open "a
quantitative finite-interval or future-uniform retention bound". This package
asks, on the same unchanged law, how long the receiver holds the record once it
is written, and with what error, without confusing one successful capture with
a durable memory.

## Answers

1. **The record is exactly where the carrier is** (Theorem 1). For every
   one-carrier state and every time, the memory is $d_1$ exactly on the
   component whose carrier is right of the receiver, and holds its old value on
   the rest. The wrong-memory probability equals
   $(1-\|\phi_1\|^2)\,\|\mathbf 1_{c<z}U^n\chi\|^2$, uniformly over coded
   memory and reference inputs; its per-step change is a quarter of the carrier
   current through the receiver cut. The receiver adds no decay of its own.
2. **Leftward crossings un-write exactly** (Theorem 2); contacts beyond the
   receiver do not.
3. **No uniform modulus over the success sector** (Theorem 3): translated
   success states can delay the write arbitrarily.
4. **No exact permanent retention for the free surrogate** (Theorem 4): a
   nonzero right-moving pulse is never entirely beyond the receiver, at any
   time. An exact witness has zero wrong-memory weight at $n = 0,1,2$ and a
   nonzero weight at $n = 3$ (corrected wording, R2).
5. **An eternal record exists outside the success sector** (Proposition 5):
   a parked dark token right of the receiver holds $d_1$ for all past and future
   times, with no write event and no capture herald. This is an existence
   example, not a classification; permanence of a captured record stays open
   (corrected wording, R2).
6. **Future-uniform bound for a declared ideal success family** (Theorem 6):
   for smooth product states of a bound pair and a right-moving pulse inside the
   v105 event $Q_{\rm full}$, the wrong-memory amplitude is at most
   $\varepsilon(T)$ for all $n\ge T$, with an explicit computable modulus. The
   frozen check is $T = 10^6$ macrosteps against $1/100$; see `RESULT.md`.
7. **Not achieved:** the same bound for the actual normalized v105 selected
   component. No free-tail bound relative to the fixed receiver and the stated
   time origin is certified for it; the minimal missing premise is stated in
   `PROOF.md` §7 (corrected, R3).

## Files

| File | Role |
|---|---|
| [PROTOCOL.md](PROTOCOL.md) | preregistration frozen before formal execution |
| [PROOF.md](PROOF.md) | theorems and proofs |
| [INTERFACE.md](INTERFACE.md) | typed success-state and retention contract |
| [RESULT.md](RESULT.md) | outcome of the pinned run (added after execution) |
| [SOURCES.tsv](SOURCES.tsv) | public inputs with commit, blob and SHA-256 |
| [`../../reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/`](../../reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/) | exact standard-library verifier and run record |

## Scope

L1 only. No Canon file changes, no new claim status, no detector, preparation,
occurrence or many-carrier statement, and no lock, archive or reset added to the
law.
