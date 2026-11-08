<!-- SPDX-License-Identifier: Apache-2.0 -->

# Path phase at a common counter

NON-CANONICAL / L1 / candidate.
Owner: A. M. Thorn, common-counter path-phase review session, 2026-11-06.
Reservation: [#1922](https://github.com/mathorn1973/twist-j/issues/1922).

The question: can an arithmetic five-position phase distinguish the course of
two paths that share their start, their end and their counter? And if it can,
is that phase a function of an amplitude-squared account of the path?

The answer depends on the carrier. This note records it on the two carriers
where the question can be posed today. It supplies two short proofs and exact
finite audits. It supplies no native realization of a contact, no physical
phase, energy or action reading, no Planck normalization and no alpha value.

## What is established here

| Carrier | Statement | Status |
| --- | --- | --- |
| Unchanged origin-zero native U | From counter 3 on, the lifted fibre shift over any window is one integer for every trajectory, `t_n1 (N_n1 - N_n0)` in the notation of the registered chart. Trajectories with a common piston cut have had the same pistons throughout. The windows `1->11` and `11->21` of #1915 are successive counter windows of one trajectory. They are not two paths at a common counter. | corollary of registered [T] rows; exhaustive audit candidate-C |
| Integral relative contact | Proposition K: the half-trace `q(t)` of every admitted contact equals a residue potential difference modulo 5. | candidate-T |
| Integral relative contact | Theorem L: for every closed contact word the relative Hermitian sum `H` lies in `5 Z[phi]`; the sums of `t*g(t)` vanish exactly for the three Galois elements other than conjugation. | candidate-T, found after the first run |
| Integral relative contact | The count of state-changing contacts is path dependent at common endpoints and common word length: the fixed word of #1908 and its slot-exchanged image reach the same complete target from `I_-2` with 135 and 123 such contacts. An explicit pair of closed words at `I_1` has equal length, equal `H` and counts 27 and 35. | candidate-C |
| Integral relative contact | On the complete orbit of `I_1` (20400 states) the path-difference lattice of `(count; H)` is `Z x 5 Z[phi]`: the count is independent of the Hermitian sum. | candidate-C |
| Integral relative contact | Recon hypothesis "on closed words the count modulo 5 is a linear function of `H` modulo 5". | fired |

Details and proofs: [NATIVE.md](NATIVE.md) and [CONTACT.md](CONTACT.md).

## Reading

On the native carrier the fibre phase is a hand of the clock. On the contact
carrier a path-sensitive five-position quantity exists, and it is a count.
Up to diagonal contacts it is the exponent of the determinant of the word
matrix, and it does not change when the amplitudes are rescaled by an odd
integer. The quantities that scale with the square of the amplitudes, the
half-trace and the Hermitian sum, are endpoint functions in their
five-position reading. A relation between the two kinds would be a
normalization of amplitude, and none follows from these results.

This paragraph is an interpretation with no registered dictionary behind it.
Its factual part would be refuted by a closed contact word whose Hermitian
sum lies outside `5 Z[phi]`, or by a complete orbit with count holonomy on
which the count is a function of the Hermitian sum.

## Files

- [NATIVE.md](NATIVE.md): the corollary for native U, the reading of the
  windows of #1915, the audit.
- [CONTACT.md](CONTACT.md): setup, Proposition K, Theorem L, the finite
  results, the explicit witnesses and the fired hypothesis.
- [PROVENANCE.md](PROVENANCE.md): authority readback, inputs, custody of the
  frozen recon text, what was exposed when, the two harness errors.
- [CHECKS.md](CHECKS.md): replay record with hashes, repository checks.
- [RECON-PREREG-EXTRACT.md](RECON-PREREG-EXTRACT.md): the recon text frozen
  before the first execution, with one part outside this reservation
  omitted and marked.
- `WORD.txt`: byte-identical copy of the 322-contact word of #1908.
- `recon_native_u_2026-11-06.py`, `recon_contact_phase_2026-11-06.py`: the
  audits of the frozen clauses.
- `posthoc_contact_area_2026-11-06.py`, `check_log_coordinate_2026-11-06.py`,
  `explore_shortest_count_loop_2026-11-06.py`,
  `witness_equal_area_pair_2026-11-06.py`: written after the first run.
- `check_tick_law_2026-11-06.py`: written while the note was prepared.
- `break_recon_parts_u_k_2026-11-06.py`: separate code paths, an extract of
  the session breaker.
- `*.stdout`: exact outputs.
- `SHA256SUMS`: hashes of the other files of the content commit. `CHECKS.md`
  was appended after the checks and is not listed.

## Replay

Standard library only. Every assertion is in exact integers or Fractions.
The one float is a seeded sampling decision in
`recon_contact_phase_2026-11-06.py`; it selects which random contacts are
drawn and enters no assertion. From the repository root, with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`:

```text
N=notes/C-COMMON-COUNTER-PATH-PHASE-N
python3 $N/recon_native_u_2026-11-06.py
python3 $N/recon_contact_phase_2026-11-06.py $N/WORD.txt
python3 $N/posthoc_contact_area_2026-11-06.py $N/WORD.txt
python3 $N/check_log_coordinate_2026-11-06.py
python3 $N/explore_shortest_count_loop_2026-11-06.py
python3 $N/witness_equal_area_pair_2026-11-06.py
python3 $N/check_tick_law_2026-11-06.py
python3 $N/break_recon_parts_u_k_2026-11-06.py
```

Each prints to stdout and must reproduce the committed `.stdout` file of the
same name byte for byte. The breaker needs about two minutes, each of the
others at most about ten seconds.

## Neighbouring scopes

- [#1915](https://github.com/mathorn1973/twist-j/pull/1915) owns the native
  paired phase, its integer lift and the bounded-work boundary. This note
  compares with its pair law and changes none of its statements.
- [#1908](https://github.com/mathorn1973/twist-j/pull/1908) owns the fixed
  322-contact word, its endpoints and its counts.
- [#1916](https://github.com/mathorn1973/twist-j/issues/1916) owns the golden
  winding width and the five-sample ambiguity of prescribed smooth loops.
- [#1919](https://github.com/mathorn1973/twist-j/pull/1919) owns the
  contact-interface response boundaries and its restored-resource
  hypotheses.
- RAMIFIED-AREA-WEYL-COVARIANCE and COMMON-HISTORY-FUNDED-AREA-RECEIVER [T]
  concern an alternating area and its Weyl phase on their own carriers. The
  Hermitian sum of this note is a different quantity on a different carrier.

## Next decision

Whether the count and the Hermitian sum can be tied at all needs a carrier on
which amplitude is normalized independently of the desired answer: a contact
law, its schedule, and a response measured in the same units as `H`. That is
a new construction with its own claim, not a continuation of this note.
Independent mathematical review of Proposition K and Theorem L is the next
acceptance step here.
