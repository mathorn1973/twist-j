# Validation and review contract

**NON-CANONICAL, L1. Analytical candidate; independent mathematical
acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767.

## Immutable inputs

| Input | Revision |
| --- | --- |
| Public main and dereferenced canon-v105 tag | `892a0b11089d34e241e1eb76d2c03247022d18e6` |
| Public Canon content commit | `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc` |
| Complete forward source/filter #1746 | `01acc42b78f75095587765e9a5b91ee70dc28f37` |
| Thermal work/clock predecessor #1764 | `6670ac274888927be3429a463966da41ca8d2e8b` |
| Common-temperature endpoint #1766 | `d978a455ef01506a9b8eb68c296e6ca89703710a` |

The public Canon bytes were checked against STATUS.md: 1295029 bytes,
SHA-256 `73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.
The content commit is an ancestor of the active revision. Public main's
two architecture jobs and aggregate check, and the tag/release publication
jobs, report success at that revision. Live remote branches, claims and
registry scopes were inspected before reserving this separate candidate.

## Evidence method

The new evidence is the displayed analytical derivations in ENERGY.md,
RECORD.md and INTERFACE.md. No new scientific executable, simulator,
floating-point experiment or expanded circuit enumeration was run. The
numeric bounds are proved by the exact expressions in the text. File
hashing, whitespace checks and existing repository gates are integrity
operations, not new scientific gates or reproductions.

Same-session work separated the energy proof, record proof and an
adversarial mathematical cross-reading. These are parts of the same
working session. They do not change the candidate status of either this
result or its inputs. An independent reviewer must check the hypotheses
and proofs at the pinned final revision.

## Proof-byte manifest

These are the final UTF-8/LF bytes. VALIDATION.md is excluded from its
own manifest.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| ENERGY.md | 20703 | `a92b56cb9914116ad88b9c46f6c36261b87eed11aa6f286d0d76353091be299e` |
| INTERFACE.md | 12795 | `1f8b65a2dc22a2345490249c29b639f0154126b980c04d6ab746cc2d8c9ea49f` |
| README.md | 5905 | `bb5f862daf2d6fe759c9aafe2bab05ed22dd2fa1ef6a471c5d44b3b151fb8592` |
| RECORD.md | 19022 | `74f3593fd9c594acce32dac9f5359693543b590f17a33de6e0a02f014400c742` |

## Repository checks

Existing local checks returned:

- `python tools/check_policy.py`: POLICY PASS.
- `python tools/check_canon.py`: CANON PASS v105, 577 claims.
- `python tools/check_ledger.py`: LEDGER PASS, 577 claims, 641 items,
  1160 dependencies, 577 evidence rows, 1124 history rows, 26 gates.
- `python tools/check_gate_contract.py`: GATE CONTRACT PASS, 26 gates.
- `python tools/check_verifier.py --base 892a0b11089d34e241e1eb76d2c03247022d18e6`:
  VERIFY NOT APPLICABLE.
- `python tools/check_reproduce.py --base 892a0b11089d34e241e1eb76d2c03247022d18e6`:
  REPRODUCE NOT APPLICABLE.
- `git diff --check`: passed; the final named staged diff is checked
  again before commit.

The Windows test attempt was not a pass. Its sandboxed run encountered
temporary-directory permission failures and was stopped; a fail-fast
diagnostic identified WinError 5 in fixture setup. Outside that sandbox,
the existing suite ran 210 tests with one skipped and one error: the
symbolic-link fixture in `test_parallel_probe_replay` could not be created
because the required operating-system privilege was unavailable
(WinError 1314). No scientific assertion failed in that error, and no
test or policy was changed to suppress it.

The same existing suite subsequently passed in WSL Ubuntu 22.04 with
Python 3.10.12: `python3 -m unittest discover -s tools -p 'test_*.py'`
ran 210 tests, all successful. The printed PROBES FAIL and
REPRODUCTIONS FAIL messages are expected negative-fixture output within
the passing suite. Public CI results, including its Python 3.12 and
architecture coverage, are recorded on the draft pull request at its
actual head revision rather than inferred from these local checks.

## Decisive review obligations

1. Recompute the contact witness for arbitrary carrier-only unitary,
   including arrangement and position mixing. Distinguish operator
   conservation, mean-energy change and asymptotic scattering.
2. Check the universal exact-channel theorem's input quantifier and
   bounded-energy scope. Do not apply it to a fixed physical source
   with only arbitrary logical labels.
3. Check the total-energy direct-integral fibers, identity extensions on
   incomplete fibers, sine support, centered-translation constant,
   reference-uniform bound and conditional normalization. The battery
   is infinite dimensional despite finite capacity.
4. Check the static generator and free phases. In the combined history,
   only the archive/reference reduction is stationary on the tail;
   the complete object/carrier endpoint is not.
5. Verify that the finite predecessor's complete acceptance projector
   excludes the designated raw memory factors and commutes with its
   onsite energy. Check the identical archive spectrum and permitted
   initial fixed-charge correlations.
6. Check the full reversible writer on both pointer inputs, all failed
   states and occupied old memory. No unknown state may be cloned or
   old archive erased.
7. Derive the 65-state clock probabilities, the exact `193/2^128` bound,
   source success margins, readiness-error amplification, complete
   energy moments and the return of the record at `3*T_h`.
8. Verify the full infinite-space source word and all rejected branches
   in INTERFACE.md. It must not import #1766's thermal factors or local
   geometry, or use the old safe spectral window for the new input.
9. Check the nonzero extreme-support coefficient of every `W^n a` and
   the exact scope of the finite-invariant-carrier obstruction.
10. Confirm that only this new note directory changed and no Canon,
    registry, predecessor, scientific threshold or workflow was edited.

A counterexample within a named proposition's full hypotheses defeats
that proposition. An unavailable resource, material implementation or
unproved locality is an explicitly open interface, not evidence that a
broader class of implementations is impossible. The candidate is handed
to review, not promoted or declared independently accepted.
