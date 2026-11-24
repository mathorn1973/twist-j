# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL. Standalone exact H3 recurrent worker check."""

from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import product
from struct import Struct
from sys import flags, stdout


def normalized(coefficients):
    return tuple(value - coefficients[-1] for value in coefficients)


def constant(n):
    return n, 0, 0, 0, 0


def add(*values):
    return tuple(map(sum, zip(*values)))


def scale(n, value):
    return tuple(n * term for term in value)


def subtract(a, b):
    return add(a, scale(-1, b))


def power(k):
    return normalized(tuple(int(i == k % 5) for i in range(5)))


@cache
def multiply(a, b):
    return normalized(tuple(sum(a[i] * b[(k - i) % 5] for i in range(5))
                            for k in range(5)))


@cache
def norm(a):
    return multiply(a, normalized((a[0], *reversed(a[1:]))))


def trace_half(a):
    twice = 5 * a[0] - sum(a)
    assert twice % 2 == 0
    return twice // 2


def even(a):
    return all(value % 2 == 0 for value in a)


def half(a):
    assert even(a)
    return tuple(value // 2 for value in a)


ZERO, ONE = constant(0), constant(1)
RHO = power(1)
J = add(ONE, RHO)
INV_J = scale(-1, add(power(1), power(3)))
THETA = norm(J)
FUND = constant(1025)
OFFSET = add(constant(-2), *(scale(2 * k, power(k)) for k in range(1, 5)))
MARKERS = tuple(
    subtract(add(constant(-1), RHO, power(2)),
             scale(2, multiply(J, power(1 + 3 * i))))
    for i in range(5)
)


@cache
def contact(a, b, exponent=1):
    delta = subtract(a, b)
    if not even(delta):
        return a, b
    midpoint = half(add(a, b))
    difference = multiply(power(exponent), half(delta))
    return add(midpoint, difference), subtract(midpoint, difference)


@cache
def scatter(cell):
    r0, r2, clk, corr = cell
    matter_gap, field_gap = subtract(r0, r2), subtract(clk, corr)
    if not even(matter_gap) or not even(field_gap):
        return cell, 0
    d, f = half(matter_gap), half(field_gap)
    if d != ZERO and norm(f) == multiply(THETA, norm(d)):
        matter_unit, field_unit, tag = J, INV_J, 1
    elif f != ZERO and norm(d) == multiply(THETA, norm(f)):
        matter_unit, field_unit, tag = INV_J, J, 2
    else:
        return cell, 0
    d, f = multiply(matter_unit, d), multiply(field_unit, f)
    m, a = half(add(r0, r2)), half(add(clk, corr))
    return (add(m, d), subtract(m, d), add(a, f), subtract(a, f)), tag


def transport(field, height, bit, exponent=1):
    after = [list(cell) for cell in field]
    for x, y in product(range(8), range(bit, height, 2)):
        left, right = x * height + y, x * height + (y + 1) % height
        for lane in range(3):
            after[left][lane], after[right][lane] = contact(
                field[left][lane], field[right][lane], exponent
            )
    for x, y in product(range(bit, 8, 2), range(height)):
        left, right = x * height + y, ((x + 1) % 8) * height + y
        after[left][3], after[right][3] = contact(field[left][3], field[right][3], exponent)
    return tuple(map(tuple, after))


def scatter_field(field):
    outputs, tags = zip(*(scatter(cell) for cell in field))
    return outputs, tags


def account(field):
    matter = add(*(value for cell in field for value in cell[:2]))
    radiation = add(*(value for cell in field for value in cell[2:]))
    quadratic = add(*(norm(value) for cell in field for value in cell))
    return matter, radiation, quadratic, trace_half(quadratic)


def clock_ready_fields():
    d = add(constant(2), RHO, power(2))
    k = subtract(J, power(2))
    receiver_stock = subtract(k, scale(2, multiply(multiply(RHO, J), d)))
    paid = scale(2, J)
    triple = constant(-3), constant(-3), constant(5)
    initial = triple
    fields = []
    for _ in range(85):
        field = [(ZERO,) * 4] * 32
        for y in range(4):
            field[y] = paid, scale(-1, paid), ONE, triple[0] if y < 2 else receiver_stock
        for x, y in product((1, 2), (0, 1)):
            field[4 * x + y] = ZERO, ZERO, ZERO, triple[x]
        fields.append(tuple(field))
        left, middle = contact(*triple[:2])
        middle, right = contact(middle, triple[2])
        triple = left, middle, right
    assert len(set(fields)) == 85 and triple == initial
    assert {account(field)[-1] for field in fields} == {446}
    return tuple(fields)


def port(y):
    return (y // 4 + (y % 4 == 3)) % 5


def worker_field(clock, offset):
    field = [clock[4 * x + y % 4] for x, y in product(range(8), range(20))]
    for y in range(20):
        i = port(y)
        source = y % 4 < 2
        center = add(offset, power(i), constant(0 if source else 4))
        d = multiply(J, FUND) if source else FUND
        clk = add(MARKERS[i], scale(2, FUND)) if source else ZERO
        field[20 + y] = add(center, d), subtract(center, d), clk, field[20 + y][3]
    return tuple(field)


def label(rank):
    if rank == 0:
        return 0
    block, offset = divmod(rank - 1, 21)
    return 21 * ((2 * (block + 1)) % 5 - 1) + offset + 1


def j_coefficients(value):
    # rho = j², so rho² = j⁴ = -1-j-j²-j³.
    c0, c1, c2, c3, c4 = value
    return c0 - c2, c3 - c2, c1 - c2, c4 - c2


CARRIER_PERIOD = 622
PERIOD = 5 * CARRIER_PERIOD
PASSIVE_ROWS = tuple(y for y in range(20) if y % 4 >= 2)
BASE_ACCOUNT = ((80, 0, 0, 0), (20570, 20, 40, 40),
                (105002830, 0, 21013020, 21013020), 188992640)
SCALAR_ACCOUNT = ((-160, 80, -80, 160), (20570, 20, 40, 40),
                  (105005070, 0, 21013820, 21013820), 188996320)
BASE_TRANSFERS = {-60: 18, -40: 54, -20: 72, 0: 162, 20: 72, 40: 54, 60: 18}
SCALAR_TRANSFERS = {-180: 18, -160: 54, -140: 18, 20: 72, 40: 216, 60: 72}
BASE_TRACE = "be7255f4b7404dfd3b6d9b0f20fab59ed1fabb558db3b3bd7121eda27d5b0c46"
SCALAR_TRACE = "0b6d9cee7dadab88d034f459fcb2a037b8eb64d0c30f55421818bcd30cea0d9a"


def passive_snapshot(field):
    return tuple(field[20 + y][:2] for y in PASSIVE_ROWS)


def native_step(field, height, bit):
    return scatter_field(transport(field, height, bit))[0]


def expected_signature(phase):
    index = (phase + 20) // 21
    return index, 4 + 2 * (21 * index - phase)


def verify_carrier_observables(ready):
    ready_ranks = {field: rank for rank, field in enumerate(ready)}
    clock = ready[0]
    arrival_times = {}
    pre_middle_hits, post_middle_hits = [], []
    target = ready[44][4][3]
    assert j_coefficients(target) == (-2, 0, -1, -5)
    peer = ready[4][4][3]
    assert peer != target and even(subtract(peer, target))
    reads = [set(), set(), set()]
    outgoing_reads = [set(), set(), set()]
    middle_residues = Counter()
    source_slots = (0, 4, 8)
    for t in range(CARRIER_PERIOD):
        if clock[4][3] == target:
            pre_middle_hits.append(t)
        post = transport(clock, 4, t % 2)
        difference = subtract(target, post[4][3])
        if even(difference):
            assert trace_half(norm(half(difference))) < 722
        if post[4][3] == target:
            post_middle_hits.append(t + 1)
        if t == 74:
            left = clock[0][3]
            assert clock[4][3] == target
            assert post[4][3] == target and post[0][3] == left
            for middle in (target, subtract(target, multiply(FUND, RHO))):
                assert not even(subtract(left, middle))
        if t % 2 == 0 and clock in ready_ranks:
            rank = ready_ranks[clock]
            assert rank not in arrival_times
            arrival_times[rank] = t
            for slot, bare, outgoing in zip(source_slots, reads, outgoing_reads):
                bare.add(clock[slot][3])
                outgoing.add(post[slot][3])
            residue = tuple(value % 2 for value in clock[4][3])
            middle_residues[residue] += 1
            assert even(subtract(post[4][3], post[8][3]))
        clock, _ = scatter_field(post)
    assert clock == ready[0]
    assert arrival_times[44] == 74
    assert pre_middle_hits == post_middle_hits == [74, 75]
    assert tuple(map(len, reads)) == tuple(map(len, outgoing_reads)) == (11, 85, 45)
    assert len(middle_residues) == 15 and max(middle_residues.values()) == 21

    ordered = sorted((t, label(rank)) for rank, t in arrival_times.items())
    assert [phase for _, phase in ordered] == list(range(85))
    times = [t for t, _ in ordered] + [CARRIER_PERIOD]
    lengths = [after - before for before, after in zip(times, times[1:])]
    special_lengths = {0: 72, 21: 72, 42: 174, 63: 72, 84: 72}
    assert lengths == [special_lengths.get(phase, 2) for phase in range(85)]
    print("carrier period=622 special_ready_returns=(72, 72, 174, 72, 72) other_ready_returns=2")
    print("carrier bare_CORR=(11, 85, 45) outgoing_post_transport_CORR=(11, 85, 45)")
    print("carrier middle_residues=15 largest_class=21 outgoing_right_guard=85/85")
    print("carrier raw_rank_44=74 target_in_j=(-2, 0, -1, -5) target_complete_and_post_transport_ticks=(74, 75)")
    print("carrier raw_rank_4_same_residue=True target_following_left_guard_refuses=True")


def verify_capacity():
    values = [2, 3]
    while len(values) <= 42:
        values.append(3 * values[-1] - values[-2])
    for budget in (BASE_ACCOUNT[-1], SCALAR_ACCOUNT[-1]):
        assert budget**2 < 4 * (values[39] + 2)
        assert 2 * FUND[0]**2 * values[4] <= budget < 2 * FUND[0]**2 * values[5]
    assert 2 * values[42] == 717780700011756164
    assert 2 * FUND[0]**2 * values[5] == 258453750
    print("capacity isolated_span_bound=38 minimum_Q_for_85=717780700011756164 funded_exponents=-4..4")


def verify_orbit(name, ready, offset, expected_account, expected_transfers, expected_trace):
    ready_labels = {field: label(rank) for rank, field in enumerate(ready)}
    projected_middle = {field[4][3] for field in ready}
    assert len(projected_middle) == 85

    clock = ready[0]
    full = initial = worker_field(clock, offset)
    complete_account = account(initial)
    *ring_accounts, scalar_account = complete_account
    assert (*map(j_coefficients, ring_accounts), scalar_account) == expected_account

    starts, work, snapshots = [], [], []
    seen, clock_seen = set(), set()
    source_middle = {i: set() for i in (0, 1, 4)}
    ordinary_marks = []
    blank_difference = multiply(J, FUND)
    corr_write = multiply(RHO, FUND)
    moves, transfers, source_events, turn_counts = (Counter() for _ in range(4))
    trace = sha256()
    pack_values = Struct("<2560i")
    for t in range(PERIOD):
        bit = t % 2
        if t < CARRIER_PERIOD:
            assert (clock, bit) not in clock_seen
            clock_seen.add((clock, bit))
        if t % CARRIER_PERIOD == 0:
            assert clock == ready[0]
        assert (full, bit) not in seen
        seen.add((full, bit))
        snapshots.append(passive_snapshot(full))
        if bit == 0 and clock in ready_labels:
            starts.append((t, ready_labels[clock]))
            # Keep the measured coordinates distinct from the projection.
            assert full[20][3] == clock[4][3]
            rank = ready.index(clock)
            for i in source_middle:
                expected_corr = clock[4][3]
                if (rank, i) in ((15, 1), (19, 4)):
                    expected_corr = subtract(expected_corr, corr_write)
                actual_corr = full[20 + 4 * i][3]
                assert actual_corr == expected_corr
                if t < CARRIER_PERIOD:
                    source_middle[i].add(actual_corr)

        if offset == OFFSET and bit == 0:
            expected_d = FUND if t % CARRIER_PERIOD == 212 else blank_difference
            assert half(subtract(*full[25][:2])) == expected_d

        clock, clock_tags = scatter_field(transport(clock, 4, bit))
        post = transport(full, 20, bit)
        after, tags = scatter_field(post)
        assert account(post) == account(after) == complete_account
        if offset == OFFSET:
            seam = slice(5 * 20, 7 * 20)
            assert full[seam] == post[seam] == after[seam] == ((ZERO,) * 4,) * 40
        recovered, inverse_tags = scatter_field(after)
        assert recovered == post
        assert inverse_tags == tuple(3 - tag if tag else 0 for tag in tags)
        assert transport(recovered, 20, bit, exponent=-1) == full

        for x, y in product(range(8), range(20)):
            slot, clock_slot = 20 * x + y, 4 * x + y % 4
            if x != 1:
                assert after[slot] == clock[clock_slot]
                assert tags[slot] == clock_tags[clock_slot]
            elif y in PASSIVE_ROWS:
                assert after[slot][2:] == clock[clock_slot][2:]
                assert tags[slot] == 0
            else:
                r0, r2, clk, corr = after[slot]
                d_written = half(subtract(r0, r2))
                assert d_written in (FUND, blank_difference)
                expected_clk = add(MARKERS[port(y)], scale(2, FUND))
                if d_written == FUND:
                    corr = add(corr, corr_write)
                    clk = subtract(clk, corr_write)
                assert corr == clock[clock_slot][3] and clk == expected_clk
                if tags[slot]:
                    source_events[(port(y), tags[slot])] += 1
                if bit == 1 and y % 4 == 0 and tags[slot] == 2:
                    ordinary_marks.append((t + 1, port(y)))

        for i in range(5):
            sites = (20 + 4 * i + 2, 20 + (4 * i - 1) % 20)
            changes = tuple(post[slot][:2] != full[slot][:2] for slot in sites)
            if not any(changes):
                continue
            assert bit == 1 and all(changes)
            work.append((t + 1, i))
            moves[i] += 1
            turn_counts[t // CARRIER_PERIOD, i] += 1
            center = add(offset, power(i), constant(2), scale(2, power(moves[i])))
            for slot in sites:
                assert after[slot][:2] == (add(center, FUND), subtract(center, FUND))
                previous = add(*(norm(value) for value in full[slot][:2]))
                current = add(*(norm(value) for value in post[slot][:2]))
                transfers[trace_half(subtract(current, previous))] += 1

        trace.update(bytes((1 - bit,)))
        trace.update(pack_values.pack(*(coefficient for cell in after for value in cell
                                        for coefficient in j_coefficients(value))))
        full = after

    assert full == initial and clock == ready[0]
    assert trace.hexdigest() == expected_trace
    assert moves == {i: 45 for i in range(5)}
    assert turn_counts == {key: 9 for key in product(range(5), repeat=2)}
    assert transfers == expected_transfers
    assert sum(amount * count for amount, count in transfers.items()) == 0
    assert source_events == {
        (i, tag): 2 * (50 if i in (1, 4) else 45)
        for i, tag in product(range(5), (1, 2))
    }
    assert [phase for _, phase in starts] == list(range(85)) * 5
    assert source_middle[0] == projected_middle
    assert all(len(values) == 85 for values in source_middle.values())
    assert ordinary_marks == [(lap * CARRIER_PERIOD + tick, i)
                              for lap in range(5) for tick, i in ((212, 1), (220, 4))]
    if offset == OFFSET:
        assert 311 * scalar_account == 58777855520
        assert 311 * 8 == 2488

    repeated_work = work + [(t + PERIOD, i) for t, i in work]
    signatures = set()
    for t, phase in starts:
        tick, i = next((tick, i) for tick, i in repeated_work if tick > t)
        signature = (i, tick - t)
        assert signature == expected_signature(phase)
        signatures.add(signature)
    assert len(signatures) == 85
    assert max(delay for _, delay in signatures) == 44

    first_lap_origins = [t for t, _ in starts[:85]]
    sizes = [len({snapshots[(t + delay) % PERIOD] for t in first_lap_origins})
             for delay in range(PERIOD)]
    assert (max(sizes), sizes.index(max(sizes)), sizes[44]) == (21, 34, 21)
    print(f"{name} accounts={expected_account}")
    print(f"{name} period={PERIOD} ready={len(starts)} work={len(work)} inverse_substeps={2 * PERIOD}")
    print(f"{name} receiver_site_scalar_changes={sorted(transfers.items())}")
    print(f"{name} first_work_signatures={len(signatures)} max_delay=44")
    print(f"{name} projected_middle_CORR=85 actual_middle_CORR_at_(1,0)=85")
    print(f"{name} passive_common_time_max=21 first_delay=34 count_at_44=21")
    print(f"{name} ordinary_marks={ordinary_marks[:2]} actual_middle_CORR_ports_0_1_4=(85, 85, 85)")
    if offset == OFFSET:
        print("translated seam_columns=(5, 6) marker_cut=212 spatial_tiles=311 spatial_Q=58777855520")
    print(f"{name} trace_sha256={trace.hexdigest()}")


def first_work(field):
    """Observe the first passive transport after a bit-zero cut."""
    for elapsed in range(1, 45):
        after = native_step(field, 20, (elapsed - 1) % 2)
        moved = {port(y) for y in PASSIVE_ROWS if after[20 + y][:2] != field[20 + y][:2]}
        if moved:
            assert len(moved) == 1
            return moved.pop(), elapsed
        field = after
    raise AssertionError("No passive work in 44 ticks")


def verify_loading(ready, offset):
    mismatches = []
    for rank, clock in enumerate(ready):
        expected = expected_signature(label(rank))
        direct = first_work(worker_field(clock, offset))
        if direct != expected:
            mismatches.append((rank, direct, expected))

        unscattered, _ = scatter_field(clock)
        predecessor = transport(unscattered, 4, 1, exponent=-1)
        assert native_step(predecessor, 4, 1) == clock
        blank = worker_field(predecessor, offset)
        loaded = native_step(blank, 20, 1)
        assert passive_snapshot(loaded) == passive_snapshot(blank)
        assert first_work(loaded) == expected
    assert mismatches == [(15, (1, 2), (2, 16)), (19, (4, 2), (2, 8))]
    print(f"loading predecessor=85/85 direct=83/85 mismatches={mismatches}")


def verify():
    if flags.optimize:
        raise SystemExit("Run without -O or PYTHONOPTIMIZE so all exact checks execute.")
    ready = clock_ready_fields()
    verify_carrier_observables(ready)
    verify_capacity()
    verify_orbit("base", ready, ZERO, BASE_ACCOUNT, BASE_TRANSFERS, BASE_TRACE)
    verify_orbit("translated", ready, OFFSET, SCALAR_ACCOUNT, SCALAR_TRANSFERS, SCALAR_TRACE)
    verify_loading(ready, OFFSET)
    print("PASS")


if __name__ == "__main__":
    stdout.reconfigure(newline="\n")
    verify()
