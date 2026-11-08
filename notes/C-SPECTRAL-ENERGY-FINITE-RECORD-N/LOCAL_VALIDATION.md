# Locality and preparation review contract

**NON-CANONICAL, L1. New conditional analytical candidate-T; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

## Fixed inputs and unchanged reviewed material

The earlier seven files at
`d13851796d5e7a316e1f628407e1bedef04f9bad` received mathematical PASS in
[review 5642195943](https://github.com/mathorn1973/twist-j/pull/1768#pullrequestreview-5642195943),
with their stated NON-CANONICAL, L1, conditional candidate scope. That
fixed-revision review was read before this continuation. Its fifteen
obligations and acceptance do not cover the new material.

ENERGY.md, FINITE_BATTERY.md, FINITE_MODEL.md, INTERFACE.md, README.md,
RECORD.md and VALIDATION.md remain byte-identical to that revision.
Their historical status text is preserved as part of the reviewed input;
the later acceptance is recorded here with its revision and scope.

Public main and dereferenced canon-v105 remain
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The content commit is
`b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`. Canon contains 1295029 bytes
with SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.
The earlier input pins in VALIDATION.md remain in force. The additional
local history template is #1761 at
`32c17259c4baf40bb6d08b521adc642956b57e94`, specifically
`notes/C-THERMAL-REGISTER-PREPARATION-N/HAMILTONIAN.md`, Sections 3-5.
Its geometry is adapted with the changes explicitly proved in
LOCAL_HAMILTONIAN.md; it is not treated as acceptance of those changes.

## Evidence and scope

The new evidence consists of the displayed analytical arguments in
PREPARATION.md, LOCALITY.md, LOCAL_HAMILTONIAN.md and LOCAL_RESOURCES.md.
The session separated preparation, conserving local synthesis and the
autonomous clock into parallel authoring tasks and then cross-read their
interfaces. These checks belong to the same working session and are not
independent acceptance.

No new scientific executable, simulation, matrix expansion, gate-list
enumeration or physical experiment was run. Existing repository gates,
file hashing and whitespace/scope inspection are integrity operations.
No computational scientific evidence or new formal gate is inferred from
them. Canon, registry, predecessors, thresholds and workflow are unchanged.

The construction is a finite encoded device for one specified source
family's complete word. It does not prove confinement of the original
spatial carrier, reproduction of its full trajectory, preparation from
thermal resources alone, indefinite retention, a material detector or
an occurrence law. The onsite negative residual correction remains part
of the actual Hamiltonian. Energy bounds are unconditioned and include
all row-copy label defects through their conserved population.

## New proof-byte manifest

The table records final UTF-8/LF bytes. This validation file is excluded
from its own manifest. The unchanged reviewed files are additionally
checked by exact Git comparison to the reviewed revision.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREPARATION.md | 18061 | `df382743524503ae3e0e94a9d95a1f31a6f67ed4e911f62dce478b6e52d12d69` |
| LOCALITY.md | 21557 | `2de2e5e4a6cd85d17f59c450a8ad7299865da330e29cf4905e5b224ae770b88a` |
| LOCAL_HAMILTONIAN.md | 23013 | `d69b3d09dffe0af25c534a87a8b81d34c7b958d4af561e1aace1eec724069f30` |
| LOCAL_RESOURCES.md | 14284 | `d7c5026ff6c72ed74f2e19c610b949cf16367b0ebc952468a947cf3bb7375beb` |

## Repository integrity checks

The following existing local checks passed for this analytical extension:

- `python tools/check_policy.py`: POLICY PASS.
- `python tools/check_canon.py`: CANON PASS v105, 577 claims.
- `python tools/check_ledger.py`: LEDGER PASS, 577 claims, 641 items,
  1160 dependencies, 577 evidence rows, 1124 history rows, 26 gates,
  7 programs.
- `python tools/check_gate_contract.py`: GATE CONTRACT PASS, 26 gates.
- `python tools/check_verifier.py --base 892a0b11089d34e241e1eb76d2c03247022d18e6`:
  VERIFY NOT APPLICABLE.
- `python tools/check_reproduce.py --base 892a0b11089d34e241e1eb76d2c03247022d18e6`:
  REPRODUCE NOT APPLICABLE.
- The named staged diff, UTF-8/LF bytes, proof hashes, unchanged reviewed
  files and public-content scope are checked before committing.

The unchanged unit suite was not rerun locally for these prose-only
additions. The older local Linux pass and Windows fixture privilege
failure are recorded in VALIDATION.md. The reviewed revision's public
CI run 40174900100 passed 210 tests on each of x86_64 and aarch64; that
is historical evidence for its own head. The continuation's required
two-architecture CI is recorded on the draft PR at its actual new head,
including the tested tree, rather than inherited from the earlier pass.
Repository CI does not independently validate these mathematical proofs.

## Independent review obligations for this extension

1. Check the physical 2^N-qubit preparation, orthogonality of the
   Householder vectors, equal-charge property, omitted coincident
   vectors and complete raw unitary extension. No projection or
   selection may replace the displayed preparation.
2. Derive the binomial nearest-neighbor bound, including both endpoints,
   and the threshold-commutator estimate with arbitrary reference.
   Apply it once to the full compensated source word, including P_x.
3. Check the supplied common-phase qubits, sharp seeds, initial source
   and all ready program/scratch/pointer/clock/row resources. Distinguish
   input purity, mean energy, capacity, dimensional cost and couplings.
4. Verify the weighted one-hot label code, all helper/padding energies
   and the actual raw binary extensions. A rejected source history is
   an admitted code state, not an invalid input that can be deleted.
5. Check fixed-charge connectivity, boundary charges, funding-bit
   routing, transport scratch and the explicit path-length bound.
   Weighted label sites must not be routed by energy-violating SWAPs.
6. Check every selective rotation and diagonal phase with clean
   workspace, reversible copied predicates, exclusion of the target
   bits, geometric routing, cleanup, all-space conservation and gate
   counts. Dirty workspace has no promised target semantics but must
   still evolve under a complete conserving unitary.
7. Verify the pointer-free preparation/program/archive sequence, raw
   occupied-archive exchange, untouched archive prefix during the
   source program, final physical pointer location and parity padding.
8. Check the three-track row geometry, identical-spectrum vertical
   transfer, clock path length, guard scheduling, all site counts,
   seven-site support, radius four and fixed degree. Data copies and
   empty future rows are physical resources.
9. Check full-raw positivity, cursor-number and label-number
   conservation, the entire energy capacity and exact initial moments.
   Include vacuum, multiple-cursor and multiple-label sectors.
10. Check the local residual correction, free H_0 phases and the
    all-time operator inequality with d N_X. A trace-distance error
    alone does not give a size-independent defect-energy bound.
11. Verify that the final pointer remains zero at every incomplete
    prefix, the completed accepted output has exactly the clock
    weight w(t), the tail estimate, the prescribed finite window,
    conditioning error amplification and the unwanted-band effect.
    Only commutation of that effect with q_f is needed; commutation
    with r_f is not asserted.
12. Check exact record reversal at 3T_h while retaining possible charged
    free phases. A finite window is not a permanent archive or a
    measurement-modified continuation.
13. Check the thermal symmetry and full-rank purity obstructions under
    their actual hypotheses, the cold charged-zero estimate, zero-gap
    readiness limits, and the stated finite-time perturbation scope.
14. Check the separate sharp-fiber theorem, including arbitrary
    occupied-memory/archive/reference correlations and commuting band
    tests. It preserves reduced outputs exactly, not the full charged
    state or a standalone coherent spatial source.
15. Confirm all five new paths, the byte identity of the seven reviewed
    inputs, public-content safety and final CI at the claimed head.
    Do not promote this extension using the older revision's review.

A counterexample within a proposition's stated hypotheses defeats that
proposition. Resource infeasibility or an unconstructed thermal/material
interface limits its physical interpretation without establishing a
broader impossibility claim. The extension is handed to review, not
merged or promoted.
