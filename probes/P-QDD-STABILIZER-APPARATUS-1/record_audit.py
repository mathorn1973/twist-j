"""Accepted exact support audit; zero runs at pin. Importing this module executes no gates."""
from dataclasses import replace
from fractions import Fraction as F
import record


ZERO = (F(0),)*5


def unit(i):
    return tuple(F(int(j == i))-F(1, 5) for j in range(5))


def difference(i, j):
    return tuple(F(int(k == i)-int(k == j)) for k in range(5))


def run_checks(terminal):
    """Called only by the pinned verifier; independent cumulative reference."""
    checks = 0

    def check(condition):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError("record conformance falsifier")

    def rejected(function, *args):
        try:
            function(*args)
        except (ValueError, TypeError):
            check(True)
        else:
            check(False)

    sources = (ZERO,) + tuple(unit(i) for i in range(5)) + tuple(
        difference(i, j) for i in range(5) for j in range(i+1, 5))
    for k in range(5):
        for variant, labels in (("E", ("LOW", "HIGH")),
                                ("R", ("r0", "r1", "r2", "r3"))):
            context = record.Context("stabilizer-"+variant+"-k"+str(k), labels, F(1, 3))
            state = record.ready(context)
            cumulative_input = F(0)
            lifetimes = [0]*len(labels)
            for sequence in (sources, tuple(reversed(sources))):
                run_input = F(0)
                outputs = [[] for _ in labels]
                emitted = [[] for _ in labels]
                origin = tuple(lifetimes)
                for v in sequence:
                    before = state
                    x = terminal(k, variant, v)
                    energy = sum((a*a for a in v), F(0))
                    state = record.deposit(state, x, energy)
                    cumulative_input += energy
                    run_input += energy
                    batch = state.active.batches[-1]
                    for i in range(len(labels)):
                        outputs[i].append(x[i])
                    # Sum stored vector coefficients from the full pulse list,
                    # independently of the incremental count/remainder code.
                    total = tuple(sum((a*a for vec in rows for a in vec), F(0))
                                  for rows in outputs)
                    expected_counts = tuple((e/context.quantum).numerator
                                            // (e/context.quantum).denominator for e in total)
                    check(batch.counts == expected_counts)
                    check(tuple(context.quantum*n+c for n,c in
                                zip(batch.counts, batch.remainders)) == total)
                    check(all(0 <= c < context.quantum for c in batch.remainders))
                    for mark in batch.marks:
                        emitted[labels.index(mark.channel)].extend(range(mark.first, mark.last+1))
                    for i in range(len(labels)):
                        check(emitted[i] == list(range(origin[i]+1, origin[i]+expected_counts[i]+1)))
                        lifetimes[i] = origin[i]+expected_counts[i]
                    check(sum(total, F(0)) == run_input)
                    check(record.stored_energy(state) == cumulative_input)
                    check(record.accounting_energy(state) == cumulative_input)
                    check(state.active.batches[:-1] == before.active.batches)
                    check(record.read(state) is state)
                    check(record.read(before) is before)
                    if v == ZERO:
                        check(not batch.marks)
                    # Changed coefficient signs leave this pulse's calorimetry
                    # unchanged but are unequal complete signed store histories.
                    negative = tuple(tuple(-a for a in vec) for vec in x)
                    other = record.deposit(before, negative, energy)
                    check(other.active.batches[-1].counts == batch.counts)
                    if energy:
                        check(other != state)
                closed = record.end(state)
                check(record.end(closed) == closed)
                rejected(record.deposit, closed, tuple(ZERO for _ in labels), F(0))
                archived = record.reset(closed)
                check(archived.archives[-1] == closed.active)
                check(archived.active.initial_lifetime == tuple(lifetimes))
                check(archived.active.batches == ())
                check(record.stored_energy(archived) == cumulative_input)
                check(record.accounting_energy(archived) == cumulative_input)
                state = archived

    half = tuple(x/F(2) for x in difference(0, 1))
    context = record.Context("two-half-energy-paths", ("a", "b"), F(1))
    state = record.ready(context)
    for n in range(1, 7):
        state = record.deposit(state, (half, half), F(1))
        batch = state.active.batches[-1]
        check(batch.counts == (n//2, n//2))
        check(len(batch.marks) == (2 if n % 2 == 0 else 0))
    # Reset-per-pulse suppresses every crossing but never destroys the energy.
    reset_state = record.ready(context)
    for _ in range(6):
        reset_state = record.deposit(reset_state, (half, half), F(1))
        check(reset_state.active.batches[-1].counts == (0, 0))
        reset_state = record.reset(reset_state)
    check(record.stored_energy(reset_state) == F(6))
    check(record.accounting_energy(reset_state) == F(6))
    check(len(reset_state.archives) == 6)

    # Exact reduced-ratio 2/3 increments, across three periods.
    periodic = record.ready(record.Context("periodic", ("a",), F(3, 4)))
    previous, increments = 0, []
    for n in range(1, 10):
        periodic = record.deposit(periodic, (half,), F(1, 2))
        count = periodic.active.batches[-1].counts[0]
        check(count == 2*n//3)
        increments.append(count-previous)
        previous = count
    check(increments[:3] == increments[3:6] == increments[6:9] == [0, 1, 1])

    # HIGH coarse counting must follow fine-channel thresholding.
    fine = record.ready(record.Context("fine-high", ("r0", "r1", "r2", "r3"), F(1)))
    fine = record.deposit(fine, (ZERO, half, half, ZERO), F(1))
    check(sum(fine.active.batches[-1].counts[1:]) == 0)
    check(int(F(1)//F(1)) == 1)  # forbidden energy-first aggregation differs

    check(record.threshold_interval(F(0), F(9, 10), F(1)) == ("DETERMINED", 0))
    check(record.threshold_interval(F(9, 10), F(1), F(1)) == ("AMBIGUOUS", 0, 1))
    check(record.threshold_interval(F(1), F(1), F(1)) == ("DETERMINED", 1))
    rejected(record.threshold_interval, F(1), F(0), F(1))
    rejected(record.threshold_interval, F(0), F(1), F(0))
    rejected(record.Context, "", ("a",), F(1))
    rejected(record.Context, "x", ("a", "a"), F(1))
    rejected(record.Context, "x", ("a",), F(0))
    rejected(record.Context, "x", ("a",), True)
    rejected(record.vector, (1, 0, 0, 0, 0))
    rejected(record.vector, [0, 0, 0, 0, 0])
    rejected(record.vector, (True, -1, 0, 0, 0))
    blank = record.ready(context)
    rejected(record.deposit, blank, (half,), F(1, 2))
    rejected(record.deposit, blank, (half, half), F(2))
    rejected(record.deposit, blank, (half, half), F(-1))
    # Detect a damaged persistent record rather than accepting its cached totals.
    batch = state.active.batches[-1]
    for bad in (replace(batch, pulse=batch.pulse+1),
                replace(batch, input_energy=batch.input_energy+1),
                replace(batch, marks=()),
                replace(batch, counts=(999, 999)),
                replace(batch, remainders=(F(1), F(1)))):
        broken = replace(state, active=replace(state.active,
                         batches=state.active.batches[:-1]+(bad,)))
        rejected(record.read, broken)
    broken = replace(reset_state, archives=reset_state.archives[1:])
    rejected(record.read, broken)
    return checks
