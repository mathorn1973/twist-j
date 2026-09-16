"""Bounded software regression checks; never a physical #539 verifier.

The complete implementation and this scope must be reviewed and publicly
committed before their first execution. No external measurement is consumed.
"""

import ast
from dataclasses import FrozenInstanceError, fields, is_dataclass, replace
from fractions import Fraction as F
import inspect
from pathlib import Path
import unittest

import adapter as a


E0 = (0, (1, 0, 0, 0, 0, 0))
E1 = (0, (0, 1, 0, 0, 0, 0))
NEG_E0 = (0, (4, 0, 0, 0, 0, 0))
TWO_E0 = (0, (2, 0, 0, 0, 0, 0))
ZERO = (0, (0, 0, 0, 0, 0, 0))
ORIGIN = (0, 0, 0)


def context(n=1, q=F(1, 16), gamma=None):
    gamma = ((ORIGIN, F(1)),) if gamma is None else gamma
    return a.ContextKey(a.core.Context(gamma, q, n))


def forged(value, **changes):
    """Fresh malformed fixture; never mutate or alias-write the original."""
    result = object.__new__(type(value))
    for item in fields(value):
        object.__setattr__(result, item.name, changes.get(item.name, getattr(value, item.name)))
    return result


class Session:
    """Mutable test driver, outside the immutable implementation carriers."""

    def __init__(self, plan, ctx):
        self.plan, self.context = plan, ctx
        self.ready = a.ready_select(plan, ctx)
        self.apparatus = self.ready.custody
        self.journal, self.history = (), ()
        self.positions = [a.ProtocolPosition(self.apparatus, self.journal)]
        self.reset_ready = None
        self.first_completed = None

    def admin(self, kind):
        old = self.apparatus
        if kind == "PREPARE":
            carrier, self.apparatus = a.prepare(self.plan, self.context, self.ready)
            assert carrier == a.support(self.apparatus)
        else:
            self.first_completed = old
            self.ready, self.apparatus = a.reset(old, self.context)
            self.reset_ready = self.ready
        self.journal = a.journal_append(self.journal, kind, old, self.apparatus)
        self.positions.append(a.ProtocolPosition(self.apparatus, self.journal))

    def tick(self):
        old = self.apparatus
        output = a.step(a.support(old), old, self.context)
        event = a.emit(output)
        position = a.ProtocolPosition(old, self.journal)
        assert a.admissible_append(position, self.history, event)
        assert a.admissible_extension(position, self.history, event)
        self.history = a.append(self.history, event)
        self.apparatus = a.persist(old, output.outcome, event)
        assert self.apparatus == output.next_apparatus
        self.journal = a.journal_append(self.journal, "STEP", old, self.apparatus)
        self.positions.append(a.ProtocolPosition(self.apparatus, self.journal))

    def complete(self):
        self.admin("PREPARE")
        for _ in range(self.context.core_context.horizon):
            self.tick()
        self.admin("RESET")
        self.admin("PREPARE")
        for _ in range(self.context.core_context.horizon):
            self.tick()
        return self


class AdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rich = Session((E0, TWO_E0), context(n=2)).complete()
        cls.empty = Session((E0, E1), context(gamma=())).complete()
        cls.subthreshold = Session((E0, E1), context(q=F(100))).complete()
        cls.n0 = Session((E0, E1), context(n=0)).complete()

    def test_two_exposures_match_unchanged_core_and_retain_both_banks(self):
        run = self.rich
        n = run.context.core_context.horizon
        for i, head in enumerate(run.plan):
            reference = a.core.run(head, run.context.core_context)
            self.assertEqual(run.apparatus.banks[i], reference)
            events = tuple(e.delta.core_event for e in run.history if e.delta.index == i)
            self.assertEqual(events, reference.history)
            self.assertEqual(len(events), n)
        self.assertEqual(tuple(e.delta.index for e in run.history), (0, 0, 1, 1))
        self.assertEqual(run.positions[-1].action_index, 2 * n + 3)
        self.assertEqual(len(run.journal), 2 * n + 3)

    def test_old_residual_signed_tape_and_records_survive_reset_and_prepare1(self):
        run = self.rich
        old = run.first_completed.banks[0]
        self.assertNotEqual(old.pair.current, ())
        self.assertNotEqual(old.apparatus.tape, ())
        self.assertTrue(any(v < 0 for row in old.apparatus.tape for _, v in row))
        after_reset = run.reset_ready.custody
        prepare1 = next(entry for entry in run.journal
                        if entry.kind == "PREPARE" and entry.before.index == 1)
        for state in (after_reset, prepare1.after, run.apparatus):
            self.assertEqual(state.banks[0], old)
            self.assertEqual(state.banks[0].pair, old.pair)
            self.assertEqual(state.banks[0].apparatus.tape, old.apparatus.tape)
            self.assertEqual(state.banks[0].history, old.history)
        self.assertEqual(run.reset_ready.selection.index, 1)
        self.assertIsInstance(after_reset.banks[1], a.Unprepared)
        self.assertEqual(a.reset(run.first_completed, run.context)[1], after_reset)
        # Full second-exposure session records carry the first bank's custody.
        for event in run.history[2:]:
            self.assertEqual(event.delta.before.banks[0], old)
            self.assertEqual(event.delta.after.banks[0], old)

    def test_joint_energy_account_and_resource_consumption(self):
        for run in (self.rich, self.empty, self.subthreshold, self.n0):
            for position in run.positions:
                measured, introduced, used_slots = F(0), F(0), 0
                for bank in position.apparatus.banks:
                    if type(bank) is a.Unprepared:
                        continue
                    measured += a.core.wave.energy(bank.pair)
                    measured += sum((v for _, v in bank.apparatus.heat), F(0))
                    introduced += a.core.wave.qdd_mass(a.core.signed_head(bank.source)) / 2
                    used_slots += bank.tick * len(bank.context.gamma)
                self.assertEqual(measured, introduced)
                self.assertLessEqual(used_slots, 2 * run.context.core_context.horizon
                                     * len(run.context.core_context.gamma))
            reset = next(entry for entry in run.journal if entry.kind == "RESET")
            self.assertEqual(reset.before.banks, reset.after.banks)

    def test_n0_has_four_distinct_administrative_positions_and_no_events(self):
        run = self.n0
        self.assertEqual(run.history, ())
        self.assertEqual(tuple(p.action_index for p in run.positions), (0, 1, 2, 3))
        self.assertEqual(len(set(run.positions)), 4)
        self.assertEqual(tuple(e.kind for e in run.journal), ("PREPARE", "RESET", "PREPARE"))
        self.assertEqual(tuple(p.apparatus.phase for p in run.positions),
                         ("READY", "COMPLETE", "READY", "COMPLETE"))
        for p in run.positions:
            with self.assertRaises(a.DomainError):
                a.step(a.support(p.apparatus), p.apparatus, run.context)
        with self.assertRaises(a.DomainError):
            a.ProtocolPosition(run.apparatus, ())

    def test_zero_crossing_empty_ports_and_multiple_crossings_are_events(self):
        for run in (self.empty, self.subthreshold):
            self.assertEqual(len(run.history), 2)
            for event in run.history:
                self.assertEqual(event.delta.core_event.crossings, ())
                self.assertEqual(event.delta.core_event.outcome, "NO_CROSSINGS")
        self.assertEqual(self.empty.apparatus.banks[0].apparatus.tape, ((),))
        multiplicities = [sum(c.count for c in event.delta.core_event.crossings)
                          for event in self.rich.history]
        self.assertTrue(any(count > 1 for count in multiplicities))

    def test_append_totality_is_separate_from_protocol_admission(self):
        events = self.rich.history
        e0, e1 = events[:2]
        self.assertEqual(a.append((e1, e0, e0), e1), (e1, e0, e0, e1))
        self.assertEqual(a.append(events, e0), events + (e0,))
        foreign = self.subthreshold.history[0]
        self.assertEqual(a.append(events, foreign), events + (foreign,))
        position = self.rich.positions[1]  # immediately after preparation 0
        self.assertTrue(a.admissible_append(position, (), e0))
        self.assertFalse(a.admissible_append(position, (), e1))
        self.assertFalse(a.admissible_append(position, (e0,), e0))
        self.assertFalse(a.admissible_append(position, (), foreign))
        self.assertFalse(a.admissible_append(self.rich.positions[-1], events, e0))
        history = ()
        for event in events:
            history = a.append(history, event)
        self.assertEqual(history, events)

    def test_journal_rejects_skips_duplicates_forged_actions_and_wrong_history(self):
        run = self.rich
        with self.assertRaises(a.DomainError):
            a.ProtocolPosition(run.apparatus, run.journal[1:])
        with self.assertRaises(a.DomainError):
            a.ProtocolPosition(run.apparatus, (run.journal[0],) * len(run.journal))
        first = run.journal[0]
        with self.assertRaises(a.DomainError):
            a.JournalEntry("RESET", first.before, first.after)
        with self.assertRaises(a.DomainError):
            a.journal_append((first,), "PREPARE", first.before, first.after)
        after_first_step = run.positions[2]
        self.assertTrue(a.admissible_append(after_first_step, run.history[:1], run.history[1]))
        self.assertFalse(a.admissible_append(after_first_step, (), run.history[1]))
        self.assertFalse(a.admissible_append(after_first_step, run.history[1:2], run.history[1]))
        self.assertFalse(a.admissible_append(forged(after_first_step, journal=()),
                                            run.history[:1], run.history[1]))

    def test_reset_domain_incomplete_ready_exhausted_and_context_mismatch(self):
        run = self.rich
        for position in (run.positions[0], run.positions[1], run.positions[2],
                         run.positions[4], run.positions[-1]):
            with self.assertRaises(a.DomainError):
                a.reset(position.apparatus, run.context)
        self.assertEqual(a.reset(run.first_completed, run.context)[0], run.reset_ready)
        with self.assertRaises(a.DomainError):
            a.reset(run.first_completed, context(n=2, q=F(1, 8)))
        with self.assertRaises(a.DomainError):
            a.reset(self.n0.apparatus, self.n0.context)

    def test_bad_heads_contexts_tokens_support_and_persist_are_rejected(self):
        ctx = self.rich.context
        malformed = ([E0, E1], (E0,), ((True, E0[1]), E1), (E0, (0, [1] * 6)))
        for plan in malformed:
            self.assertEqual(a.ready_request(plan, ctx)[0], "INVALID_REQUEST")
        for plan in ((ZERO, E0), (E0, ZERO)):
            self.assertEqual(a.ready_request(plan, ctx),
                             ("REJECTED", "ZERO_AMPLITUDE_SESSION_PLAN"))
        self.assertEqual(a.ready_request((E0, E1), None)[0], "INVALID_REQUEST")
        for invalid in (forged(ctx, profile="OTHER"),
                        forged(ctx, core_context=forged(ctx.core_context, horizon=True)),
                        forged(ctx, core_context=forged(ctx.core_context, quantum=1))):
            self.assertEqual(a.ready_request((E0, E1), invalid)[0], "INVALID_REQUEST")
        ready = a.ready_select((E0, E1), ctx)
        with self.assertRaises(a.DomainError):
            a.prepare((E1, E0), ctx, ready)
        with self.assertRaises(a.DomainError):
            a.prepare(ready.selection.plan, ctx,
                      forged(ready, selection=forged(ready.selection, index=1)))
        with self.assertRaises(a.DomainError):
            a.prepare(ready.selection.plan, ctx,
                      forged(ready, custody=forged(ready.custody, index=True)))
        before = self.rich.positions[1].apparatus
        with self.assertRaises(a.DomainError):
            a.step(a.support(ready.custody), before, ctx)
        event = self.rich.history[0]
        with self.assertRaises(a.DomainError):
            a.persist(before, "NO_CROSSINGS", event)
        with self.assertRaises(a.DomainError):
            a.persist(event.delta.after, event.delta.core_event.outcome, event)
        with self.assertRaises(TypeError):
            a.emit(event)

    def test_forged_event_cannot_erase_archive_or_signed_information(self):
        event = self.rich.history[2]
        old = event.delta.after.banks[0]
        broken = forged(old, history=old.history[:-1])
        after = forged(event.delta.after, banks=(broken, event.delta.after.banks[1]))
        bad_event = forged(event, delta=forged(event.delta, after=after))
        with self.assertRaises((TypeError, ValueError)):
            a.append((), bad_event)
        signed = self.rich.history[0]
        outgoing = tuple((site, -value) for site, value in signed.delta.core_event.outgoing)
        bad_core = forged(signed.delta.core_event, outgoing=outgoing)
        with self.assertRaises((TypeError, ValueError)):
            a.reread(forged(signed, delta=forged(signed.delta, core_event=bad_core)))

    def test_missing_declared_fields_are_rejected_before_core_validation(self):
        incomplete_event = object.__new__(a.EventRecord)
        position = self.rich.positions[1]
        self.assertFalse(a.admissible_extension(position, (), incomplete_event))
        with self.assertRaises(TypeError):
            a.append((), incomplete_event)
        incomplete_context = object.__new__(a.ContextKey)
        self.assertEqual(a.ready_request((E0, E1), incomplete_context)[0], "INVALID_REQUEST")
        nested_context = forged(self.rich.context, core_context=object.__new__(a.core.Context))
        self.assertEqual(a.ready_request((E0, E1), nested_context)[0], "INVALID_REQUEST")
        broken_bank = object.__new__(a.core.CompleteState)
        broken_apparatus = forged(position.apparatus,
                                  banks=(broken_bank, position.apparatus.banks[1]))
        with self.assertRaises(TypeError):
            a.support(broken_apparatus)
        broken_event = forged(self.rich.history[0], delta=forged(
            self.rich.history[0].delta, core_event=object.__new__(a.core.Event)))
        self.assertFalse(a.admissible_extension(position, (), broken_event))

    def test_passive_rereads_and_immutable_nested_carriers(self):
        run = self.rich
        event = run.history[0]
        before = (run.apparatus, run.history, run.journal)
        for _ in range(4):
            self.assertIs(a.reread(event), event)
        self.assertEqual((run.apparatus, run.history, run.journal), before)
        with self.assertRaises(FrozenInstanceError):
            run.apparatus.index = 0
        with self.assertRaises(FrozenInstanceError):
            run.reset_ready.selection.index = 0

        def check(value):
            if type(value) is tuple:
                for child in value:
                    check(child)
            elif is_dataclass(value):
                self.assertTrue(type(value).__dataclass_params__.frozen)
                for item in fields(value):
                    check(getattr(value, item.name))
            else:
                self.assertIn(type(value), (int, bool, str, F, type(None)))

        check((run.apparatus, run.history, run.journal, run.reset_ready, a.support(run.apparatus)))

    def test_new_bank_core_generation_is_independent_of_inactive_bank_data(self):
        # Different first-source schedules produce distinct retained custody.
        # They keep the new-bank head and complete context fixed. This finite
        # check complements, and does not replace, the structural argument.
        ctx = context()
        left = Session((E0, TWO_E0), ctx).complete()
        right = Session((E1, TWO_E0), ctx).complete()
        opposite = Session((NEG_E0, TWO_E0), ctx).complete()
        for other in (right, opposite):
            self.assertNotEqual(left.apparatus.banks[0], other.apparatus.banks[0])
            self.assertEqual(left.apparatus.banks[1], other.apparatus.banks[1])
            self.assertEqual(left.history[-1].delta.core_event, other.history[-1].delta.core_event)
            self.assertNotEqual(left.history[-1], other.history[-1])
        # Guard the dependency boundary of actual generation, not validators
        # which deliberately inspect/replay retained histories for coherence.
        tree = ast.parse(Path(a.__file__).read_text(encoding="utf-8"))
        functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
        allowed = {
            "_prepare_bank": ({"head", "context", "core"}, {"prepare"}),
            "_step_bank": ({"bank", "event", "core"}, {"step", "emit", "append"}),
        }
        for name, (names, calls) in allowed.items():
            fn = functions[name]
            loaded = {node.id for node in ast.walk(fn)
                      if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load)}
            self.assertLessEqual(loaded, names)
            for node in ast.walk(fn):
                if isinstance(node, ast.Call):
                    self.assertIsInstance(node.func, ast.Attribute)
                    self.assertIsInstance(node.func.value, ast.Name)
                    self.assertEqual(node.func.value.id, "core")
                    self.assertIn(node.func.attr, calls)
        self.assertEqual(tuple(inspect.signature(a._prepare_bank).parameters), ("head", "context"))
        self.assertEqual(tuple(inspect.signature(a._step_bank).parameters), ("bank",))
        self.assertEqual(tuple(inspect.signature(a._selection).parameters), ("plan", "context", "index"))


if __name__ == "__main__":
    unittest.main()
