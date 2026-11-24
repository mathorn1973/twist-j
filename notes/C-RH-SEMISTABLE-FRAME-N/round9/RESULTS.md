# Round 9 first-run results

NON-CANONICAL. No authority. **candidate-C**, one x86_64 architecture.

Both independently authored programs completed their first scientific run with exit code zero, empty stderr and no timeout. All preregistered subtests A-D passed. There were no scientific reruns, case changes or frozen program edits.

## Immutable inputs

- Preregistration public pin: d598aedb1658f00af9196aedba8944dd6205f533.
- Execution public pin: b83250a7db82d2a27de932617fb39f61cf6af823.
- PREREG.md SHA-256: 4da279d9c4ea6457b04e465c165bed937358c43c536178cbc6905e8e18f65f59.
- verify_r9.py SHA-256: 73f36c06df3084af2bfd012a85b1e3bf9a2e938959e3be7752863f2e8eb5f37d.
- break_r9.py SHA-256: 4abf263516945c9b3bc131299b18f9cbd98e03194ce7fe27942697964ae71b14.

The contract and both programs were publicly read back before execution. The blind author had not read the verifier or its output before freezing.

## A. Incidence family

Both implementations agree on every individual source count and every distinct pair, not only the totals.

| t | m | D | d | R | pair intersection | exact defect |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 11 | 2420 | 880 | 9680 | 320 | 7/44 |
| 2 | 17 | 9248 | 2176 | 36992 | 512 | 13/68 |
| 2 | 29 | 47096 | 6496 | 188384 | 896 | 25/116 |
| 3 | 19 | 12996 | 6156 | 116964 | 2916 | 5/57 |
| 3 | 37 | 98568 | 23976 | 887112 | 5832 | 14/111 |
| 4 | 37 | 98568 | 42624 | 1577088 | 18432 | 21/296 |
| 4 | 67 | 592548 | 141504 | 9480768 | 33792 | 51/536 |
| 5 | 53 | 292136 | 137800 | 7303400 | 65000 | 14/265 |

Totals: **34,134 atom labels; 270 source counts; 5,689 unordered distinct-word pairs**. All match the contract. Atom multiplicities are positive integer coordinate counts, not approximations.

The finite runs check the coordinate witness and the matching spectral upper certificate. They do not enumerate all complex subspaces. The projection-trace proof in PROOF.md establishes the maximum over all such subspaces.

## B. Literal group averaging

For N=(Z/2)^11 and Gamma=C_11, the semidirect group has order 22,528.

Both implementations verify orthogonality of the eleven characters, the full cyclic orbit, the stated translation laws, the averaged squared norm 1/11 and the coefficient 1/11 in every active character projection. Thus those full projections are injective on the chosen target factor.

The implementations deliberately use different mechanisms. The development program directly sums each full Fourier projection. The opposition program uses an independently implemented integer Walsh transform and literal rotation/translation checks. Operation counts in their stdout therefore differ; the mathematical quantities agree.

Other N-characters are outside the designated orbit and vanish on the model target. No broader injectivity assertion is made.

## C. Nontrivial Hecke corner

Both programs verify the regular S_3 model:

- projector rank 3;
- orthogonal surviving block ranks 1 and 2;
- commuting corner with span dimension 2;
- exact source and target weights 1/3 and 2/3;
- zero individual-kernel and target-span budgets;
- in all eight incidence families, each block has the original defect and the weighted sum has that same defect.

This finite example is the nontrivial generic corner of GL_2(F_2). The proof of persistence under arbitrary regular finite-group factors is separate.

## D. Local lattice normal form

| k | p | all matrices modulo p squared | determinant unit | integral ambient stabilizer |
|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 2 | 2 |
| 1 | 3 | 9 | 6 | 3 |
| 1 | 5 | 25 | 20 | 5 |
| 2 | 2 | 256 | 96 | 32 |
| 2 | 3 | 6561 | 3888 | 486 |
| **Total** | | **6855** | **4012** | **528** |

Both independently verify Gz=z, ell G=ell, determinant preservation, and the biconditional between p-integrality of G and its inverse and the distinguished-column congruence on C. These tests include residue characteristic two.

This audit checks the lattice normal form. It does not compute local irreducible representations or establish the classical newform theorems by finite testing.

## Outputs and execution metadata

| Program | Exit | Elapsed nanoseconds | stdout SHA-256 |
|---|---:|---:|---|
| verify_r9.py | 0 | 4909722359 | 0cb0452c896eb12ddff1cceb8acde56a0766724bad2d81fa104c34972e2779a9 |
| break_r9.py | 0 | 1031044409 | 15001949264b65a0789d9bb93e61da7b72fa7d028bbadac51b59cd51bf955bcb |

Both empty stderr files have SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
The full stdout, stderr and record JSON files retain the actual results.

The development driver's first attempted launch was stopped before program execution by an invalid 65-character hash transcription. CUSTODY.md preserves the error, the comparison with the unchanged author and public commits, and the correction of only that driver literal. The scientific program then executed exactly once. The opposition program also executed exactly once.

These are two separately authored implementations in one session and one architecture. They are not an external independent review, a two-architecture validation, a Lean proof, or a validation of RH.
