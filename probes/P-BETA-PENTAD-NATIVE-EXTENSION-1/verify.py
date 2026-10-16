#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact aggregate audit for the bracket/pentad/native-extension probe.

Only the three hash-bound source helpers are read and executed. Their supplied
output files are never inputs. This aggregate shares their submitted formulas;
it is not a blind independent reproduction. Its additional classifier uses
independently assembled linear equations and complete F_5 row elimination.

The native helper checks all checkpoints for each generator and each proposed
lambda extension. Its full-counter chart checks are restricted to n=0..31,
and its entrance census to n=0..4095. The additional active-chart check below
exhausts both selector bits and counter parities. Universal entrance, extension
uniqueness, and the necessity of the classifier conditions remain proof claims.
No finite time census is described as a proof for every integer counter.
"""

import sys

# Keep execution read-only even outside the repository runner's environment.
sys.dont_write_bytecode = True

from contextlib import redirect_stderr, redirect_stdout
from hashlib import sha256
from io import StringIO
from itertools import product
import json
from pathlib import Path
import runpy


SOURCE_HASHES = {
    "signed_a4_audit.py":
        "9092a1dc10fac13c11754e9ce0212d3a990c7748324102afbd042bc6e493ad42",
    "independent_geometry_audit.py":
        "080ac4616bbb390d39edc5f7ed9b98c546ceff4c8caa2fee76d5f2362604e35a",
    "native_fiber_audit.py":
        "cff091a505a2e04cd18b7b691bf03f51782218899fcf31ee417a0858d81c17ac",
}
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
B = ((2, 4, 0), (4, 2, 4), (0, 4, 2))
A = ((4, 1, 0), (0, 1, 0), (0, 1, 4))
P = ((0, 4, 1), (0, 4, 0), (1, 4, 0))
T = ((1, 0, 0), (3, 4, 0), (4, 0, 4))
STAR = (1, 4, 3)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mv(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) % 5
                 for row in matrix)


def mm(left, right):
    return tuple(tuple(sum(a * b for a, b in zip(row, column)) % 5
                       for column in zip(*right)) for row in left)


def determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return (a * (e * i - f * h) - b * (d * i - f * g)
            + c * (d * h - e * g)) % 5


def orthogonal(matrix):
    return mm(tuple(zip(*matrix)), mm(B, matrix)) == B


def matrix(flat):
    return tuple(tuple(flat[3 * i:3 * i + 3]) for i in range(3))


def json_value(value):
    return json.loads(json.dumps(value, allow_nan=False))


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key in helper stdout")
        result[key] = value
    return result


def run_helper(directory, name):
    path = directory / name
    require(sha256(path.read_bytes()).hexdigest() == SOURCE_HASHES[name],
            "helper source hash mismatch: " + name)
    stdout, stderr = StringIO(), StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        namespace = runpy.run_path(str(path), run_name="__hash_bound_helper__")
    require(not stderr.getvalue(), "helper wrote stderr: " + name)
    require(sha256(path.read_bytes()).hexdigest() == SOURCE_HASHES[name],
            "helper source changed during execution: " + name)
    text = stdout.getvalue()
    report = json.loads(text, object_pairs_hook=unique_object)
    require(type(report) is dict, "helper stdout is not a JSON object: " + name)
    return namespace, report, sha256(text.encode("utf-8")).hexdigest()


def expect_counts(report, expected, label):
    for key, value in expected.items():
        require(type(report.get(key)) is int and report[key] == value,
                label + ": incorrect count " + key)


def helper_semantics(signed, geometry, native, reports):
    sr, gr, nr = (reports[name] for name in
                  ("signed_a4_audit.py", "independent_geometry_audit.py",
                   "native_fiber_audit.py"))
    expect_counts(sr, {
        "signed_s5_matrices": 120, "homomorphism_pairs": 14400,
        "projective_directions": 31, "square_directions": 15,
        "frame_permutations": 120, "binary_states": 16,
        "binary_isometries": 120, "native_tangent_group": 8,
        "native_bracket_group": 4, "native_plus_T_group": 120,
        "active_phi_plus_T_group": 12, "fivecycles": 24,
    }, "signed A4")
    require(sr.get("carry_basis_matches_registered_tau15") is True,
            "signed A4: carry basis result missing")
    require(sr.get("missing_transposition_matrix") == json_value(T),
            "signed A4: incorrect target transposition")
    expect_counts(gr, {
        "det_R": 2, "SO_count": 120, "distinct_frame_actions": 120,
        "square_determinant_PGL_subgroup_size": 60,
        "binary_state_count": 16, "binary_orthogonal_group_count": 120,
        "A4_signed_S5_count": 120,
    }, "geometry")
    census = gr.get("projective_line_census")
    require(type(census) is dict, "geometry: missing projective census")
    expect_counts(census, {
        "total": 31, "isotropic": 6, "square_norm": 15, "nonsquare_norm": 10,
    }, "geometry projective census")
    require(gr.get("element_order_census") ==
            {"1": 1, "2": 25, "3": 20, "4": 30, "5": 24, "6": 20},
            "geometry: incorrect element order census")
    require(gr.get("all_assertions_passed") is True,
            "geometry: assertion completion marker missing")
    require(gr.get("B") == json_value(B)
            and gr.get("A4_signed_transposition_01") == json_value(T),
            "geometry: form or target binding mismatch")
    expect_counts(nr, {
        "checkpoint_generator_decompositions": 78125,
        "checkpoint_extensions": 125000,
        "full_counter_chart_affine_basis_checks": 16000,
        "bounded_entrance_cases": 20480, "maximum_entrance": 9,
    }, "native fiber")
    witness = {"n": 14, "z": 0,
               "driver": "".join(str(n.bit_count() % 2) for n in range(14, 23))}
    require(witness["driver"] == "101001011" and nr.get("sharp_witness") == witness,
            "native fiber: incorrect sharp entrance witness")
    require(signed["B"] == geometry["B"] == B
            and signed["A"] == native["A"] == A
            and signed["PHI"] == native["P"] == P
            and native["STAR"] == STAR, "helper coordinate bindings disagree")
    require(set(signed["MATS"].values()) == geometry["so"],
            "signed A4 image does not equal independent SO enumeration")
    require(signed["FRAMES"] == tuple(geometry["coordinate_frames"]),
            "common five-coordinate frame labels disagree")
    require(sr["intrinsic_frames"] == json_value(
        [[list(v) for v in sorted(f)] for f in signed["FRAMES"]]),
        "signed A4: emitted frames disagree with checked frames")


def row_reduce(equations, variables):
    rows = [[value % 5 for value in row] for row in equations]
    pivots = []
    rank = 0
    for column in range(variables):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, 5)
        rows[rank] = [inverse * value % 5 for value in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [(a - coefficient * b) % 5
                           for a, b in zip(rows[i], rows[rank])]
        pivots.append(column)
        rank += 1
    require(not any(not any(row[:variables]) and row[variables] for row in rows),
            "classifier linear constraints are inconsistent")
    return rows[:rank], pivots


def classifier():
    # Nine row-major unknowns C_ij. Assemble CA-AC=0 directly, then Cv_r=v_r
    # for every r in F_5. This exhausts the solution space of these necessary
    # proof conditions; it does not search only the supplied C_lambda family.
    fixed_vectors = [((2 + r) % 5, 0, (1 - r) % 5) for r in range(5)]
    equations = []
    for i, j in product(range(3), repeat=2):
        coefficients = [((A[c][j] if r == i else 0)
                         - (A[i][r] if c == j else 0)) % 5
                        for r, c in product(range(3), repeat=2)]
        equations.append(coefficients + [0])
    for vector in fixed_vectors:
        for i in range(3):
            coefficients = [vector[c] if r == i else 0
                            for r, c in product(range(3), repeat=2)]
            equations.append(coefficients + [vector[i]])
    reduced, pivots = row_reduce(equations, 9)
    free = [i for i in range(9) if i not in pivots]
    require(len(pivots) == 8 and len(free) == 1,
            "classifier must have affine dimension one")
    origin = [0] * 9
    for row, pivot in zip(reduced, pivots):
        origin[pivot] = row[9]
    directions = []
    for column in free:
        vector = [0] * 9
        vector[column] = 1
        for row, pivot in zip(reduced, pivots):
            vector[pivot] = -row[column] % 5
        directions.append(vector)
    solutions = set()
    for parameters in product(range(5), repeat=len(free)):
        flat = tuple((origin[i] + sum(t * v[i] for t, v in
                                     zip(parameters, directions))) % 5
                     for i in range(9))
        require(all(sum(a * b for a, b in zip(row[:9], flat)) % 5 == row[9]
                    for row in equations), "RREF candidate violates an original equation")
        candidate = matrix(flat)
        require(mm(candidate, A) == mm(A, candidate)
                and all(mv(candidate, v) == v for v in fixed_vectors),
                "classifier candidate fails direct matrix conditions")
        solutions.add(candidate)
    projector = tuple(tuple(3 * (I[i][j] + A[i][j]) % 5 for j in range(3))
                      for i in range(3))
    require(mm(projector, projector) == projector, "invalid eigenspace projector")
    family = {lam: tuple(tuple((I[i][j] + (lam - 1) * projector[i][j]) % 5
                               for j in range(3)) for i in range(3))
              for lam in range(5)}
    require(len(solutions) == 5 and solutions == set(family.values()),
            "complete affine solution space is not the C_lambda family")
    require(all(determinant(candidate) == lam for lam, candidate in family.items()),
            "C_lambda determinant does not equal lambda")
    invertible = [lam for lam, candidate in family.items() if determinant(candidate)]
    isometries = [lam for lam, candidate in family.items() if orthogonal(candidate)]
    special = [lam for lam in isometries if determinant(family[lam]) == 1]
    require(invertible == [1, 2, 3, 4] and isometries == [1, 4] and special == [1],
            "incorrect GL/O/SO classifier intersection")
    require(family[1] == I and family[4] ==
            tuple(tuple(-x % 5 for x in row) for row in A),
            "orthogonal classifier representatives are not I and -A")
    return {
        "field": 5, "unknown_order": "row-major C00,C01,...,C22",
        "equation_count": len(equations), "fixed_vectors": fixed_vectors,
        "rref_augmented_nonzero_rows": reduced, "pivot_columns": pivots,
        "free_columns": free, "affine_origin": matrix(origin),
        "affine_direction_basis": [matrix(v) for v in directions],
        "affine_solution_count": len(solutions), "projector_E_plus": projector,
        "family_by_lambda": {str(lam): candidate for lam, candidate in family.items()},
        "determinants_by_lambda": {str(lam): determinant(candidate)
                                   for lam, candidate in family.items()},
        "singular_lambdas": [lam for lam in family if lam not in invertible],
        "invertible_lambdas": invertible, "orthogonal_lambdas": isometries,
        "special_orthogonal_lambdas": special,
    }


def active_chart(parity, z, w):
    require(z in (1, 4), "active chart requested outside active sheets")
    centered = tuple((a - b) % 5 for a, b in zip(w, STAR))
    if z == 4:
        centered = mv(P, centered)
    return tuple((-a if parity else a) % 5 for a in centered)


def additional_native_checks(native):
    count = 0
    for checkpoint in product(range(5), repeat=6):
        s, q, r, w = native["unpack"](checkpoint)
        z = (s + q + r) % 5
        if z not in (1, 4):
            continue
        for bit, parity in product(range(2), repeat=2):
            generator = (sum(checkpoint) + 2 * bit) % 5
            nxt = native["literal"](generator, checkpoint)
            ns, nq, nr, nw = native["unpack"](nxt)
            require(active_chart(parity, z, w) ==
                    active_chart(1 - parity, (ns + nq + nr) % 5, nw),
                    "active invariant fails a selector-bit/parity edge")
            count += 1
    require(count == 25000, "incomplete active checkpoint/bit/parity census")
    require(mm(P, P) == I and mm(A, A) == I, "native involution premise fails")
    # The proof forces Phi_0(w)=o_r+PCP(w-o_r). At r=0 and w=0,
    # the a self-loop requires its value to be fixed by A. P and T both fail.
    obstructions = {}
    center = (4, 4, 1)
    for name, candidate in (("P", P), ("T", T)):
        image = mv(mm(P, mm(candidate, P)), center)
        value = tuple((a - b) % 5 for a, b in zip(center, image))
        after_a = mv(A, value)
        require(after_a != value, "missing checkpoint-only obstruction: " + name)
        require(not (mm(candidate, A) == mm(A, candidate)
                     and all(mv(candidate, ((2 + r) % 5, 0, (1 - r) % 5)) ==
                             ((2 + r) % 5, 0, (1 - r) % 5) for r in range(5))),
                "obstructed matrix unexpectedly satisfies classifier conditions")
        obstructions[name] = {
            "forced_phi0_at_zero": value, "a_of_forced_phi0_at_zero": after_a,
            "piston_outputs": [native["pack"](0, 0, 0, v)[:4]
                               for v in (value, after_a)],
        }
    require(obstructions["P"]["forced_phi0_at_zero"] == (2, 3, 1)
            and obstructions["T"]["piston_outputs"] ==
            [(1, 3, 0, 1), (3, 1, 1, 0)], "checkpoint obstruction binding fails")
    return {"active_checkpoint_selector_bit_counter_parity_checks": count,
            "checkpoint_only_obstructions": obstructions}


def time_context_certificate():
    # In the Thue--Morse fixed point, a length-nine window meets at most two
    # consecutive length-sixteen mu^4 blocks. All four adjacent letter pairs
    # occur, so the union below is the complete factor set (TM-SHEET premise).
    # For LINEAR C the scalar counter sign cancels from K^-1 C K. These words
    # suffice as externally supplied evaluation contexts, with no context
    # update, occupied-memory continuation, or minimality claim.
    def substitute(word):
        return "".join("01" if bit == "0" else "10" for bit in word)

    prefix = "0"
    for _ in range(3):
        prefix = substitute(prefix)
    pairs = {prefix[i:i + 2] for i in range(len(prefix) - 1)}
    require(pairs == {"00", "01", "10", "11"}, "adjacent-pair coverage fails")
    blocks, factors = {}, set()
    for pair in sorted(pairs):
        block = pair
        for _ in range(4):
            block = substitute(block)
        require(len(block) == 32, "incorrect substitution block length")
        blocks[pair] = block
        factors.update(block[i:i + 9] for i in range(len(block) - 8))
    require(len(factors) == 24, "incorrect length-nine Thue--Morse factor count")
    sheet_maps = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    entrance_steps = {}
    for word in sorted(factors):
        by_sheet = []
        for initial_sheet in range(5):
            sheet, steps = initial_sheet, 0
            while sheet not in (1, 4) and steps < len(word):
                sheet = sheet_maps[int(word[steps])][sheet]
                steps += 1
            require(sheet in (1, 4), "admitted time factor fails nine-step entrance")
            by_sheet.append(steps)
        entrance_steps[word] = by_sheet
    maximum = max(max(steps) for steps in entrance_steps.values())
    require(maximum == 9 and entrance_steps["101001011"][0] == 9,
            "factor entrance maximum or sharp witness fails")
    return {
        "substitution": {"0": "01", "1": "10"},
        "substitution_power": 4, "adjacent_pairs_witness_prefix": prefix,
        "pair_blocks": blocks, "factor_length": 9,
        "factor_count": len(factors), "factors": sorted(factors),
        "entrance_steps_by_factor_and_initial_sheet": entrance_steps,
        "factor_sheet_cases": len(factors) * 5, "maximum_entrance": maximum,
        "sharp_factor": "101001011", "sharp_initial_sheet": 0,
        "linear_lift_evaluation_context_upper_bound": len(factors),
        "context_update_or_minimality_claim": False,
    }


def target_generation_certificate(geometry):
    def generated(generators):
        found, pending = {I}, [I]
        while pending:
            current = pending.pop()
            for generator in generators:
                candidate = mm(generator, current)
                if candidate not in found:
                    found.add(candidate)
                    pending.append(candidate)
        return found

    minus_identity = tuple(tuple(-value % 5 for value in row) for row in I)
    bracket_group = generated((A, P, T))
    full_group = generated((A, P, minus_identity, T))
    negative_so = {tuple(tuple(-value % 5 for value in row) for row in candidate)
                   for candidate in geometry["so"]}
    require(len(bracket_group) == 120 and bracket_group == geometry["so"],
            "<A,P,T> is not the complete bracket-preserving SO group")
    require(len(full_group) == 240 and full_group == bracket_group | negative_so
            and all(orthogonal(candidate) for candidate in full_group),
            "<A,P,-I,T> is not the 240-element orthogonal group")
    return {
        # The frozen helper's native_plus_T_group field means <A,P,T>,
        # adjoining T to the bracket-preserving native four subgroup.
        "signed_helper_native_plus_T_group_means": "order of <A,P,T>",
        "bracket_preserving_generators": {"A": A, "P": P, "T": T},
        "bracket_preserving_group_order": len(bracket_group),
        "full_native_extra_generator": minus_identity,
        "full_native_homogeneous_plus_T_group_order": len(full_group),
        "full_group_determinant_one_count":
            sum(determinant(candidate) == 1 for candidate in full_group),
        "full_group_determinant_minus_one_count":
            sum(determinant(candidate) == 4 for candidate in full_group),
    }


def main():
    require(sys.flags.optimize == 0 and __debug__,
            "optimized Python disables assertions in the hash-bound helpers")
    require(len(sys.argv) == 1, "this verifier accepts no arguments")
    directory = Path(__file__).resolve().parent
    # Verify every source before executing any helper, then verify each again
    # immediately before and after its execution in run_helper.
    for name, digest in SOURCE_HASHES.items():
        require(sha256((directory / name).read_bytes()).hexdigest() == digest,
                "helper source hash mismatch: " + name)
    namespaces, reports, output_hashes = {}, {}, {}
    for name in SOURCE_HASHES:
        namespaces[name], reports[name], output_hashes[name] = run_helper(directory, name)
    signed = namespaces["signed_a4_audit.py"]
    geometry = namespaces["independent_geometry_audit.py"]
    native = namespaces["native_fiber_audit.py"]
    helper_semantics(signed, geometry, native, reports)
    certificate = classifier()
    controls = additional_native_checks(native)
    time_context = time_context_certificate()
    target_generation = target_generation_certificate(geometry)
    result = {
        "probe": "P-BETA-PENTAD-NATIVE-EXTENSION-1",
        "status": "PASS exact finite audit; universal claims require the proof",
        "helper_source_sha256": SOURCE_HASHES,
        "helper_stdout_sha256": output_hashes, "helper_reports": reports,
        "checkpoint_only_linear_constraint_certificate": certificate,
        "additional_native_controls": controls,
        "finite_time_context_certificate": time_context,
        "target_generation_certificate": target_generation,
        "finite_counter_coverage": {
            "chart_counter_min_inclusive": 0, "chart_counter_max_inclusive": 31,
            "chart_vectors_per_base": 4, "entrance_counter_min_inclusive": 0,
            "entrance_counter_max_inclusive": 4095,
            "universal_counter_claim_verified_by_finite_census": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False))


if __name__ == "__main__":
    main()
