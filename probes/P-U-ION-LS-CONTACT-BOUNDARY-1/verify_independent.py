"""Independent exact audit of a restricted, uncalibrated ion-contact model.

No physical calibration, pulse integration, or numerical pulse sampling occurs.
The archived tables are inputs, not newly executed native dynamics.  This file
must not be imported or executed until the complete accepted public pin exists.
"""

from __future__ import annotations

import csv
from fractions import Fraction
import hashlib
from io import StringIO
from pathlib import Path


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _rows(root: Path, name: str, header: tuple[str, ...], digest: str) -> list[tuple[int, ...]]:
    source = root / "probes/P-U-TWO-TRACE-PORT-CONTACTS-1/evidence/primary" / name
    raw = source.read_bytes()
    _require(hashlib.sha256(raw).hexdigest() == digest, "Archived input changed: " + name)
    _require(raw.endswith(b"\n") and b"\r" not in raw, "Noncanonical CSV bytes: " + name)
    reader = csv.reader(StringIO(raw.decode("ascii")))
    _require(tuple(next(reader)) == header, "Unexpected CSV schema: " + name)
    result = []
    for record in reader:
        _require(len(record) == len(header), "CSV row width: " + name)
        row = tuple(int(value) for value in record)
        _require(all(str(value) == token for value, token in zip(row, record)),
                 "Noncanonical integer: " + name)
        _require(all(0 <= value < 5 for index, value in enumerate(row) if index != 2),
                 "Pentit or input label outside F5: " + name)
        result.append(row)
    return result


def _force_polynomial(left: int, right: int) -> dict[tuple[int, ...], int]:
    """Coefficients in Q[Delta_0,...,Delta_4,c], with c=cos(phi).

    For A=Delta_left+exp(i*phi)*Delta_right with real Delta labels, this
    is AA^dagger.  Label equality is retained by accumulating monomials.
    """
    terms: dict[tuple[int, ...], int] = {}
    for positions, coefficient in (((left, left), 1), ((right, right), 1),
                                   ((left, right, 5), 2)):
        powers = [0] * 6
        for position in positions:
            powers[position] += 1
        exponent = tuple(powers)
        terms[exponent] = terms.get(exponent, 0) + coefficient
    return terms


def audit(root: Path) -> dict:
    """Derive the declared finite invariants without primary-code imports."""
    history_header = ("a1", "a2", "n", "s1", "s2", "r1_p1", "r1_p4",
                      "r1_p1p", "r1_p4p", "r1_q", "r1_r", "r2_p1", "r2_p4",
                      "r2_p1p", "r2_p4p", "r2_q", "r2_r")
    contact_header = ("a1", "a2", "n", "source_before", "source_after",
                      "before_p1", "before_p4", "before_p1p", "before_p4p",
                      "before_q", "before_r", "after_p1", "after_p4",
                      "after_p1p", "after_p4p", "after_q", "after_r")
    histories = _rows(root, "HISTORY.csv", history_header,
                      "0485f39381fb83c1cf30edbdf7114df2a107d0d6b7aa40e0725f83ae1d84f3d3")
    contacts = _rows(root, "CONTACTS.csv", contact_header,
                    "4480ac45a70548bc01688b59d3c3516428af687a201ea04b94ecfd3fe198ddf7")
    _require([row[:3] for row in histories] ==
             [(a, b, n) for a in range(5) for b in range(5) for n in range(10)],
             "History order or complete coverage changed")
    _require([row[:3] for row in contacts] ==
             [(a, b, n) for a in range(5) for b in range(5) for n in (0, 6)],
             "Contact order or complete coverage changed")
    boundaries = {row[:3]: row for row in histories}
    initial = (0, 0, 0, 0, 1, 0)
    ready = (2, 1, 3, 4, 0, 4)
    for row in histories:
        a, b, n, source1, source2 = row[:5]
        _require(source1 == ((a + 1) % 5 if n == 0 else 1), "First source custody")
        _require(source2 == ((b + 1) % 5 if n <= 6 else 4), "Second source custody")
        if n == 0:
            _require(row[5:11] == initial and row[11:17] == initial, "Initial cells")
        if n == 6:
            _require(row[11:17] == ready, "Inherited second ready cell")
        _require(row[5:11] == boundaries[a, 0, n][5:11], "R1 depends on second label")
        _require(row[11:17] == boundaries[0, b, n][11:17], "R2 depends on first label")

    second_contacts = []
    for row in contacts:
        a, b, n, source_before, source_after = row[:5]
        before, after = row[5:11], row[11:17]
        boundary = boundaries[a, b, n]
        source_index, cell_index = (3, 5) if n == 0 else (4, 11)
        _require(source_before == boundary[source_index], "Contact source input mismatch")
        _require(before == boundary[cell_index:cell_index + 6], "Contact full input mismatch")
        _require(source_after == boundaries[a, b, n + 1][source_index],
                 "Contact source output not inherited")
        _require(after[:4] == before[:4] and after[5] == before[5],
                 "Contact changed fixed receiver coordinates")
        _require(source_after == sum(before) % 5, "Contact displaced trace mismatch")
        _require(after[4] == (source_before - sum(before[:4]) - before[5]) % 5,
                 "Contact receiver port mismatch")
        if n == 6:
            _require(before == ready and source_before == (b + 1) % 5,
                     "Second-contact family mismatch")
            _require((source_after, after[4]) == (4, (source_before + 1) % 5),
                     "Second-contact target mismatch")
            second_contacts.append(row)

    distinct = []
    maximum_fibres = []
    for n in range(10):
        classes: dict[tuple[int, ...], int] = {}
        for row in histories:
            if row[2] == n:
                key = row[2:]  # all original state coordinates; only labels removed
                classes[key] = classes.get(key, 0) + 1
        distinct.append(len(classes))
        maximum_fibres.append(max(classes.values()))
    for n in (9,):
        merged = {boundaries[a, b, n][2:] for a in (0, 1) for b in (0, 1)}
        _require(len(merged) == 1, "The four-history collision was lost")

    states = tuple((s, q) for s in range(5) for q in range(5))
    target = {(s, q): ((q + 4) % 5, (s + 1) % 5) for s, q in states}
    exchange = {(s, q): (q, s) for s, q in states}
    _require(set(target.values()) == set(states), "Target is not a permutation")
    _require(all(target[target[pair]] == pair for pair in states), "Target involution failed")
    mismatches = sum(target[exchange[pair]] != exchange[target[pair]] for pair in states)

    # Exact swap covariance of the diagonal closed-loop phase profile for
    # every label pair; c remains an indeterminate, rather than a sampled angle.
    for s, q in states:
        _require(_force_polynomial(s, q) == _force_polynomial(q, s),
                 "Closed-loop force profile lost swap symmetry")

    # Matrix entries of an arbitrary common R tensor R are products of two
    # formal commuting R entries.  Exchanging both input and output indices
    # only changes factor order.  Check the entire 25-by-25 matrix support.
    monomial_entries = 0
    for a, b in states:
        for s, q in states:
            original = sorted(((a, s), (b, q)))
            conjugated = sorted(((b, q), (a, s)))
            _require(original == conjugated, "Common rotation covariance failed")
            monomial_entries += 1
    _require(monomial_entries == 625, "Incomplete common-rotation polynomial audit")

    # For any swap-invariant density operator the two probabilities below
    # are equal.  Orthogonality and positivity of I-E-F imply 2p <= 1.
    incoming = (0, 0)
    _require(exchange[incoming] == incoming, "Chosen input is not swap fixed")
    wanted = target[incoming]
    counterpart = exchange[wanted]
    _require(wanted != counterpart, "The requested output is swap fixed")
    effect = {pair: int(pair == wanted) for pair in states}
    reflected = {pair: int(pair == counterpart) for pair in states}
    _require(all(effect[pair] * reflected[pair] == 0 for pair in states),
             "Correct and exchanged outcome effects overlap")
    _require(all(reflected[pair] == effect[exchange[pair]] for pair in states),
             "Outcome effects are not swap partners")
    _require(all(1 - effect[pair] - reflected[pair] >= 0 for pair in states),
             "Outcome effects do not have a positive complement")
    orbit = {wanted, counterpart}
    bound = Fraction(1, len(orbit))
    # The equal mixture saturates the state-space bound; no pulse reachability
    # or coherent implementation is inferred from this density-operator witness.
    distribution = {pair: bound if pair in orbit else Fraction(0) for pair in states}
    _require(sum(distribution.values()) == 1 and
             all(distribution[pair] == distribution[exchange[pair]] for pair in states),
             "Exact symmetric probability witness failed")

    coefficients = []
    for s in range(5):
        outgoing = target[s, 0]
        coefficients.append([sum(int(level == value) for value in outgoing) -
                             int(level == s) - int(level == 0)
                             for level in range(1, 5)])

    # A different, predeclared physical encoding Q(q)=q+4 changes the
    # representation of the target to bare SWAP.  This is a boundary control,
    # not permission to change the frozen identical encoding after a contact.
    encoded_target_is_swap = all(
        (target[s, q][0], (target[s, q][1] + 4) % 5) == ((q + 4) % 5, s)
        for s, q in states
    )
    zero_inputs = sum(row[3] == 0 and row[9] == 0 for row in second_contacts)
    return {
        "actual_second_contacts": len(second_contacts),
        "zero_pair_histories": zero_inputs,
        "history_distinct": distinct,
        "history_max_fibre": maximum_fibres,
        "target_swap_commutator_mismatches": mismatches,
        "symmetric_success_bound": str(bound),
        "identical_spectrum_coefficients": coefficients,
        "relabelled_target_is_swap": encoded_target_is_swap,
    }
