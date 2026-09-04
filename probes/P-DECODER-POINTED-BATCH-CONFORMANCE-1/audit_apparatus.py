"""Finite exact audit of the explicitly selected atomic batch model.

Nothing is evaluated at import time.  run_checks is called only by the
pinned verifier.  The explicit Cartesian enumeration is independent of
PairBank's rank/unrank implementation.  These checks are not evidence of a
physical apparatus, self-location, a temporal ensemble, or an L6 measure.
"""

from fractions import Fraction
from itertools import product
from typing import Callable

from apparatus import (
    CONTEXT_ID, READY_STATE_ID, BatchRecord, Controller, PairBank,
    append_history, centered_head, context_of, emit, mix_a, passive_read,
    persist, prepare, ready_select, reset, step, terminal, zero_support,
)
from kernel import u_step


# Literal rows in the marked basis e_0,...,e_4, independently written from
# A e_j = e_j + e_(j+2) - e_(j+3) - e_(j+4), indices modulo five.
A_REFERENCE = (
    (1, -1, -1, 1, 0),
    (0, 1, -1, -1, 1),
    (1, 0, 1, -1, -1),
    (-1, 1, 0, 1, -1),
    (-1, -1, 1, 0, 1),
)


def _center_reference(v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(v[j] * (5 * int(k == j) - 1) for j in range(4))
                 for k in range(5))


def _mix_reference(a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * a[j] for j in range(5)) for row in A_REFERENCE)


def _unit_tuple(unit: object) -> tuple:
    return (unit.source_id, unit.relative_cut, unit.cell, unit.tag,
            unit.sign, unit.ordinal)


def _pair_tuple(pair: object) -> tuple:
    return _unit_tuple(pair.system), _unit_tuple(pair.record)


def _enumerate_pairs(source_id: tuple, cut: int, a: tuple[int, ...]) -> tuple:
    """Explicit nested-loop product; no rank, inverse, counts or bank helper."""
    rows = []
    for cell in range(5):
        value = a[cell]
        sign = 1 if value > 0 else -1
        for system_ordinal in range(1, abs(value) + 1):
            for record_ordinal in range(1, abs(value) + 1):
                rows.append((
                    (source_id, cut, cell, "S", sign, system_ordinal),
                    (source_id, cut, cell, "R", sign, record_ordinal),
                ))
    return tuple(rows)


def _raises_value_error(operation: Callable[[], object]) -> bool:
    try:
        operation()
    except ValueError:
        return True
    return False


def _batch_checks() -> bool:
    ok = True
    seen = 0
    largest_bank = 0
    for column in range(5):
        basis = tuple(int(row == column) for row in range(5))
        ok = (mix_a(basis) == _mix_reference(basis)) and ok

    for v in product(range(-2, 3), repeat=4):
        seen += 1
        point = tuple(value % 5 for value in v) + (0, 0)
        source_id = (0, point)
        a_ref = _center_reference(v)
        support, controller = prepare(source_id, v)
        event = emit(support)
        bank = event.pair_bank
        expected = _enumerate_pairs(source_id, 0, a_ref)
        expected_counts = tuple(sum(pair[0][2] == cell for pair in expected)
                                for cell in range(5))
        largest_bank = max(largest_bank, len(expected))
        m_ref = sum(value * value for value in v) - Fraction(sum(v) ** 2, 5)

        ok = (controller == Controller(0)) and ok
        ok = (centered_head(v) == a_ref == support.a == event.a) and ok
        ok = (sum(a_ref) == 0) and ok
        ok = (sum(value * value for value in a_ref) == 25 * m_ref) and ok
        ok = (mix_a(a_ref) == _mix_reference(a_ref)) and ok
        ok = (event.counts == bank.counts == expected_counts) and ok
        ok = (event.total_count == bank.total_count == len(expected)) and ok
        ok = (event.source_id == source_id and event.relative_cut == 0
              and event.absolute_counter == 0
              and event.provenance_checkpoint == source_id) and ok
        ok = (context_of(source_id) == CONTEXT_ID == event.context_id) and ok
        ok = (ready_select(source_id) == READY_STATE_ID) and ok

        for cell, (system, record) in enumerate(bank.fibers):
            value = a_ref[cell]
            sign = (value > 0) - (value < 0)
            ok = (system.tag == "S" and record.tag == "R"
                  and system.cell == cell == record.cell
                  and system.size == abs(value) == record.size
                  and system.sign == sign == record.sign
                  and system.source_id == source_id == record.source_id
                  and system.relative_cut == 0 == record.relative_cut) and ok
            for ordinal in range(1, abs(value) + 1):
                ok = (_unit_tuple(system.unit_at(ordinal))
                      == (source_id, 0, cell, "S", sign, ordinal)) and ok
                ok = (_unit_tuple(record.unit_at(ordinal))
                      == (source_id, 0, cell, "R", sign, ordinal)) and ok

        for index, expected_pair in enumerate(expected):
            actual = event.pair_at(index)
            ok = (_pair_tuple(actual) == expected_pair) and ok
            ok = (bank.index_of(actual) == index) and ok
            ok = (bank.pair_at(bank.index_of(actual)) == actual) and ok
        ok = _raises_value_error(lambda: event.pair_at(len(expected))) and ok
        ok = _raises_value_error(lambda: event.pair_at(-1)) and ok
        ok = _raises_value_error(lambda: event.pair_at(True)) and ok

        if expected:
            ratio_ref = tuple(Fraction(count, len(expected))
                              for count in expected_counts)
            ok = (event.ratio == ratio_ref and event.outcome == "BATCH_EVENT") and ok
            # This is a finite-bank identity check, not an invented U checkpoint.
            next_bank = PairBank(source_id, 1, _mix_reference(a_ref))
            next_pair = next_bank.pair_at(0)
            ok = (next_pair.system.relative_cut == 1
                  and next_pair.record.relative_cut == 1) and ok
            ok = _raises_value_error(lambda: bank.index_of(next_pair)) and ok
            ok = _raises_value_error(lambda: next_bank.index_of(event.pair_at(0))) and ok
        else:
            ok = (event.ratio == "ZERO_DENOMINATOR"
                  and event.outcome == "ZERO_EVENT") and ok

    # q(d)=25*m <= 25*sum(v_i^2) <= 400; (2,2,-2,-2) attains 400.
    return ok and seen == 625 and largest_bank == 400


def _persist_zero_checks() -> bool:
    ok = True
    for initial_counter in (0, 7):
        for piston in ((0, 0, 0, 0), (1, 1, 1, 1), (1, 3, 2, 4)):
            source_id = (initial_counter, piston + (0, 0))
            v = tuple(value if value <= 2 else value - 5 for value in piston)
            support, controller = prepare(source_id, v, source_id)
            checkpoint_ref = source_id
            a_ref = _center_reference(v)
            history = ()
            zero_case = piston == (0, 0, 0, 0)

            for cut in range(3):
                next_checkpoint = u_step(checkpoint_ref)
                before = (support, controller, history)
                next_support, next_controller, event = step(
                    support, controller, next_checkpoint)
                ok = (event == emit(support)) and ok
                ok = (next_controller == persist(controller, event)) and ok
                ok = (event.source_id == source_id
                      and event.relative_cut == cut
                      and event.absolute_counter == initial_counter + cut
                      and event.provenance_checkpoint == checkpoint_ref
                      and event.a == a_ref) and ok
                ok = (next_support.source_id == source_id
                      and next_support.relative_cut == cut + 1
                      and next_support.checkpoint == next_checkpoint
                      and next_support.a == _mix_reference(a_ref)) and ok
                ok = (event.counts == tuple(value * value for value in a_ref)) and ok
                ok = (next_controller.next_cut == cut + 1
                      and next_controller.cache == event and terminal(event)) and ok

                if zero_case:
                    ok = (event.outcome == "ZERO_EVENT"
                          and event.total_count == 0
                          and event.ratio == "ZERO_DENOMINATOR"
                          and zero_support(support) == event) and ok
                    ok = _raises_value_error(lambda: passive_read(event, 0)) and ok
                else:
                    expected_total = sum(value * value for value in a_ref)
                    ok = (event.outcome == "BATCH_EVENT"
                          and event.total_count == expected_total
                          and event.ratio == tuple(Fraction(value * value, expected_total)
                                                   for value in a_ref)) and ok
                    ok = (passive_read(event, 0) == event.pair_at(0)) and ok
                    ok = (passive_read(event, expected_total - 1)
                          == event.pair_at(expected_total - 1)) and ok
                    ok = _raises_value_error(lambda: zero_support(support)) and ok
                ok = ((support, controller, history) == before) and ok

                # The actual next support supplies a legitimate next-cut record;
                # it is deliberately too early to append it to this prefix.
                gap_event = emit(next_support)
                ok = _raises_value_error(lambda: append_history(history, gap_event)) and ok
                new_history = append_history(history, event)
                ok = (new_history == history + (event,)
                      and len(new_history) == cut + 1) and ok
                ok = _raises_value_error(lambda: append_history(new_history, event)) and ok
                ok = _raises_value_error(lambda: step(support, controller, checkpoint_ref)) and ok
                ok = _raises_value_error(lambda: step(support, Controller(cut + 1),
                                                      next_checkpoint)) and ok

                ready, cleared = reset(next_controller)
                ok = (ready == READY_STATE_ID and cleared.next_cut == cut + 1
                      and cleared.cache is None) and ok
                ok = (reset(cleared) == (READY_STATE_ID, cleared)) and ok
                next_next_checkpoint = u_step(next_checkpoint)
                ok = (step(next_support, cleared, next_next_checkpoint)
                      == step(next_support, next_controller, next_next_checkpoint)) and ok
                ok = (new_history[-1] == event and len(history) == cut) and ok

                support, controller = next_support, cleared
                history = new_history
                checkpoint_ref = next_checkpoint
                a_ref = _mix_reference(a_ref)

            ok = (tuple(event.relative_cut for event in history) == (0, 1, 2)) and ok
            if zero_case:
                ok = (all(event.outcome == "ZERO_EVENT" for event in history)) and ok
    return ok


def run_checks() -> list[tuple[str, bool]]:
    return [("G07_BATCH", _batch_checks()),
            ("G08_PERSIST_ZERO", _persist_zero_checks())]
