# Frozen finite audit results

NON-CANONICAL. No authority. Status: **candidate-C**, one x86_64 lane.
No Canon status change. This is not a test of actual automorphic matrices.

## Custody and method

The preregistration was published as commit
3418bd94e0ac8e4ff47393e4706291729845ff23 and read back byte for byte.
Both programs were frozen, published together as commit
72ff97914a1b56ad616d8e603d9776364ae90968, and read back byte for byte
before either program was executed.

The development implementation uses reduced row-echelon bases and
intersection ranks. The blind opposition implementation grows subspaces as
sets of field points and counts preimages and kernel intersections.
The opponent received the frozen contract, not the development program.
These are separate implementations in one session. They are not external
independent review and do not satisfy a two-architecture gate.

Both first runs completed under the frozen 180-second budget, exit code 0,
with empty stderr and no failed contract assertions. No program was repaired
or rerun. Python was 3.12.14 on x86_64; the prescribed hash-seed, bytecode
and UTF-8 environment settings were applied. Runtime values in the JSON
records are measured metadata, not floating-point scientific assertions.

## Results

| Domain | Frozen cases | Result |
|---|---:|---|
| A: kernel formula, all target and source subspaces | 6,291 map families | Both pass |
| B: Kronecker rank upper certificates | 25,164 at l=1 and 960 at l=2 | Both pass |
| C: genuine finite group average over Q | One fixed model and matching witnesses | Exact defect 1/6; certificate rank 5 of 6 |
| D: block budgets, all target subspaces | 1,146 block families | Both pass |
| E: normalized relative trace bound | 7,168 grid cases, plus fixed fixtures | Both pass; sharp fixture 1/3; joint/marginal counterexample 1/2 |

The opposition log records 100,424 target-subspace visits and 120,468
source-subspace pairs in A. In D it records 39,154 target-subspace visits
and 8,748 visits in positive-rank blocks. These are exhaustive within the
stated domains, not arbitrary-dimensional proofs.

## Output-label erratum, retained without changing the frozen files

The development stdout calls 615 cases "zero-defect" and 146 cases
"balanced zero-defect". That wording is too broad. The counters in both
programs mean:

- 615 families in which every positive-rank **reduced block** has e_alpha=0;
- 146 of those families also have p=q.

The checked conclusions are respectively eps=B and eps=kappa. Neither
counter asserts eps=0 for the full family. The all-zero family illustrates
the distinction: the local conditions are vacuous but its full defect is 1.
The opposition stdout's "semistable" shorthand refers to the same local
condition and must be read with this scope.

This reporting defect was found by the root's post-run code inspection.
The mathematical assertions implement the preregistered conditional
equalities correctly. All program bytes and first-run stdout are preserved;
the correction is made here, not by silently changing the frozen result.

## Hashes

| File | SHA-256 |
|---|---|
| PREREG.md | 7fa50924f322f4ff4c8a412fe3ac8fced9de2abf59b348a6c3a99613d27625d0 |
| verify.py | 19a1a8fdbefab7a7fe68062ca974e2a4bfb07f926f385b053f07463177deb805 |
| break.py | 81f0baf5e2480ca50ed6e3b4f4889538b7ebfef66f8982ef6f612703137f0bd5 |
| verify.stdout.txt | 70fb78fdc3bbbb3a6c250e7d9a2fa7fe07e32328a65e4084facce7cbdb76f4ae |
| break.stdout.txt | 719131ee7c3559722877a2b7f0e544afb2d42d846855a86c3a09252e115ad5c2 |
| Each empty stderr file | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

Measured first-run elapsed times: development 3.224 seconds; opposition
1.520 seconds. See the unrounded run JSON records and separate stdout files.
