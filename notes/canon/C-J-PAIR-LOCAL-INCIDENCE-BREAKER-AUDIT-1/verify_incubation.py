"""Post-exposure incubation audit; independent convolution code path.

No public formal claim, no blind confirmation, and no physical simulation.
Root first freezes PREREG + this file + compared source snapshots by SHA-256.
"""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


def emit(name, **fields):
    print(json.dumps(dict(check=name, **fields), sort_keys=True, separators=(",", ":")))


def demand(condition, name):
    if not condition:
        raise AssertionError(name)


def norm(v):
    return sum(x * x for x in v)


def convolve(v):
    """Distribute source columns, independently of model's row-shift code."""
    out = [0] * 5
    arrivals = [[] for _ in range(5)]
    for source, coefficient in enumerate(v):
        for offset, multiplier in ((0, 1), (2, 1), (3, -1), (4, -1)):
            target = (source + offset) % 5
            contribution = multiplier * coefficient
            out[target] += contribution
            arrivals[target].append(contribution)
    return tuple(out), arrivals


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    sign = 1
    result = Fraction(1)
    for column in range(len(a)):
        pivot = next((i for i in range(column, len(a)) if a[i][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            sign = -sign
        value = a[column][column]
        result *= value
        for row in range(column + 1, len(a)):
            ratio = a[row][column] / value
            for j in range(column, len(a)):
                a[row][j] -= ratio * a[column][j]
    return sign * result


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


print("INCUBATION C-J-PAIR-LOCAL-INCIDENCE-BREAKER-AUDIT-1")
print("MODE POST-EXPOSURE REPRODUCTION; L1; NO PHYSICAL STATUS MOVE")

left = (-3, 0, -1, 1, 3)
right = (-3, 0, 1, -1, 3)
for scale in (1, 5):
    x = tuple(scale * z for z in left)
    y = tuple(scale * z for z in right)
    ax, _ = convolve(x)
    ay, _ = convolve(y)
    demand(tuple(map(abs, x)) == tuple(map(abs, y)), "B1 equal input magnitude")
    demand(tuple(map(abs, ax)) != tuple(map(abs, ay)), "B1 output magnitude split")
    supported = all((z - x[0]) % 5 == 0 for z in x)
    demand(supported == (scale == 5), "B1 stated lattice scope")
    emit("B1", scale=scale, x=x, y=y, ax=ax, ay=ay,
         abs_ax=list(map(abs, ax)), abs_ay=list(map(abs, ay)), supported=supported)

seed = (4, -1, -1, -1, -1)
orbits = [seed]
for n in range(4):
    current = orbits[-1]
    following, terms = convolve(current)
    pre = tuple(sum(abs(z) for z in cell) for cell in terms)
    positive = tuple(sum(max(z, 0) for z in cell) for cell in terms)
    negative = tuple(sum(max(-z, 0) for z in cell) for cell in terms)
    demand(tuple(p - m for p, m in zip(positive, negative)) == following,
           "B2 signed reduction")
    demand(norm(pre) == norm(current) + 3 * sum(map(abs, current)) ** 2,
           "B2 raw norm identity")
    demand(norm(following) == 5 * norm(current), "A norm identity")
    if n < 3:
        demand(norm(pre) == (212, 1300, 5300)[n], "B2 supplied raw total")
        demand(norm(following) == (100, 500, 2500)[n], "B2 supplied net total")
    emit("B2", step=n + 1, a=current, next=following, positive=positive,
         negative=negative, raw_magnitude=pre, raw_pairs=norm(pre),
         reduced_pairs=norm(following), ratio=str(Fraction(norm(pre), norm(following))))
    orbits.append(following)

_, first_terms = convolve(seed)
cell = first_terms[1]
positive = sum(max(z, 0) for z in cell)
negative = sum(max(-z, 0) for z in cell)
demand(sorted(cell) == [-1, -1, 1, 1], "B3 arrival witness")
demand((positive + negative) ** 2 == 16, "B3 unsigned raw count")
demand((positive - negative) ** 2 == 0, "B3 signed pair sum")
emit("B3_RAW", contributions=cell, positive=positive, negative=negative,
     unsigned_pairs=16, signed_pair_sum=0, reduced_units=0)

columns = []
for j in range(5):
    e = tuple(int(i == j) for i in range(5))
    columns.append(convolve(e)[0])
matrix = transpose(columns)
gram = multiply(transpose(matrix), matrix)
demand(gram == [[5 * int(i == j) - 1 for j in range(5)] for i in range(5)],
       "Exact full-register Gram identity")
basis_columns = []
for j in range(4):
    f = tuple(int(i == j) - int(i == 4) for i in range(5))
    af, _ = convolve(f)
    demand(sum(af) == 0, "A4 invariant")
    basis_columns.append(af[:4])
restricted = transpose(basis_columns)
det = determinant(restricted)
demand(det == 25, "B4 determinant")
# On V, A^{-1}=g^{-2} A/5, with g^{-2}v row k = v_(k+2).
target = (1, 0, 0, 0, -1)
atarget, _ = convolve(target)
inverse_target = tuple(Fraction(atarget[(k + 2) % 5], 5) for k in range(5))
demand(any(x.denominator != 1 for x in inverse_target), "B4 non-surjective witness")
demand(convolve(inverse_target)[0] == target, "B4 exact inverse")
emit("B4", restricted_matrix=restricted, determinant=str(det), index=25,
     target=target, inverse_target=[str(x) for x in inverse_target],
     injective=True, same_lattice_surjective=False)

# Universal no-go certificate: a nonnegative separately additive signed-pair
# kernel has ++,-- unit entries equal to 1. At p=m=1 its count is >=2,
# whereas dependence on the reduced zero state demands 0.
emit("RAW_POSITIVE_PAIR_NOGO", pure_plus_calibration=1, pure_minus_calibration=1,
     null_pair_minimum_count=2, required_zero_count=0,
     conclusion="No nonnegative separately additive raw signed-pair kernel fits all three inputs")

# Compare with the frozen candidate only after all independent calculations.
model_path = Path(__file__).parent / "source" / "candidate_model.py"
spec = importlib.util.spec_from_file_location("frozen_candidate_model", model_path)
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)
for n, a in enumerate(orbits):
    bank = model.prepare_blank(seed, n, "audit-cut-" + str(n), max_units=512)
    demand(bank.coefficients == a, "Model signed state vs independent convolution")
    active = model.toggle_same_cell(bank)
    counts, ratios = model.census(active)
    demand(counts == tuple(z * z for z in a), "Model reduced-input counts")
    demand(sum(counts) == 20 * 5 ** n, "Model expected norm total")
    demand(model.toggle_same_cell(active) == bank, "Model fixed-input involution")
    if n == 1:
        demand(counts[1] == 0, "Actual model dark cell")
    emit("MODEL", n=n, signed_state=a, bank_sites=len(bank.addresses), counts=counts,
         ratios=[str(r) for r in ratios], actual_cell_1_count=counts[1],
         fixed_input_involution=True)

for raw in (left, right):
    prepared = tuple(5 * x for x in raw)
    bank = model.prepare_blank(prepared, 1, "supported-B1", max_units=128)
    demand(bank.coefficients == convolve(prepared)[0], "Scaled B1 model state")
emit("MODEL_B1", signed_preparation_retained=True, signed_cut_state_retained=True)
print("AUDIT PASS: supplied numeric witnesses reproduced; raw-arrival extension fails; reduced-input snapshot survives")
print("PHYSICAL COINCIDENCE-RECORD-FREQUENCY: UNTESTED STOP")
