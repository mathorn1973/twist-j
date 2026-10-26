# Validation and separate scientific acceptance

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
Promotion dossier: PROMO-C-SOURCE-ENERGY-REFINEMENT-N.

## 1. Prospective boundary

The exact [CONTRACT.md](CONTRACT.md) was committed and pushed before
these proof files at `d69ff34274ffce191055df7fd44e092366e20819`.
Its public contents were read back and compared byte for byte. It
freezes the actual source, f(1)=0, original occupation encoding,
source energy-action tolerance <E0/1200, full-time window |s|<=3 and
receiver contrast >1/100. It permits an explicitly positive alternative
raw higher-charge completion that exactly preserves the entire code.

No scientific executable, moment enumeration, spectral numerical search,
matrix expansion or simulation was run. All new estimates and the
interaction construction are analytical. No scientific acceptance
threshold was tuned after execution. The changed boundary allowance
2^-17 is explicitly budgeted in the proof and does not change the
frozen source energy or receiver targets.

Any future scientific computation requires a separate prospective pin
of its exact executable, inputs, outputs and acceptance threshold before
execution. The repository's infrastructure tests have no independent
mathematical acceptance scope.

## 2. Authority, custody and scope

STATUS was read first. POLICY, AGENTS, CORE and FRONTIER are unchanged
from the preceding complete reads; all five normative hashes passed.
The public authority remained ACTIVE Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, also the peeled v105 tag.
The required main architecture and aggregate checks, and publication,
were successful at that authority commit.

A fresh remote scan enumerated 311 branch heads. Current issues,
branches, notes/probes and registry were checked for collisions before
the issue1782 reservation. Frozen source commits and the distinction
between their review states are recorded in [README.md](README.md).

This branch is based on public main. Its only additions are the eight
files in this directory. It changes no predecessor, canonical claim,
policy, implementation, verifier, workflow, gate, registry or ledger.
The pinned prospective contract is unchanged. All content files have
SHA-256 entries in [SHA256SUMS](SHA256SUMS); the manifest excludes itself.

## 3. Infrastructure checks

Local repository validation passed:

- `python tools/check_policy.py`: POLICY PASS.
- `python tools/check_canon.py`: CANON PASS v105, 577 claims.
- `python tools/check_ledger.py`: LEDGER PASS, 577 claims, 641 items,
  1160 dependencies, 577 evidence entries, 1124 history entries,
  26 gates and seven programs.
- `python tools/check_gate_contract.py`: GATE CONTRACT PASS, 26 gates.
- `python -m unittest discover -s tools -p 'test_*.py'`: 210 tests, OK.
- `python tools/check_verifier.py --base
  892a0b11089d34e241e1eb76d2c03247022d18e6`: VERIFY NOT APPLICABLE.
- `python tools/check_reproduce.py --base
  892a0b11089d34e241e1eb76d2c03247022d18e6`: REPRODUCE NOT APPLICABLE.

The changed-file checks concern notes only. Expected negative fixtures
inside the unit suite do not change its successful final result.
All eight files are checked for UTF-8 with LF line endings, relative
links, manifest integrity, whitespace and the declared added-only scope.
The contract is compared with its pinned commit; Canon is unchanged.
Public CI is reported in the pull-request description at its exact head,
separately from the scientific obligations below. CI success cannot
promote these notes.

## 4. Scientific review obligations

| File | Obligations | Principal failure modes |
| --- | --- | --- |
| [SHARP_SPECTRAL.md](SHARP_SPECTRAL.md) | 7 | Exterior root branch; exact pole subtraction and integral; radial real-part lower bound and measure normalization; full contact transfer; phase/source weight and reference scope. |
| [FEJER_RADIUS.md](FEJER_RADIUS.md) | 9 | Fourier signs and positivity; exact wrap error; finite-window layer-cake bound; fixed dyadic degree; finite prefix and centered tail; complete contrast and perturbation budget. |
| [FEW_BODY.md](FEW_BODY.md) | 9 | Original signed occupancy and gauge; charge-supported matrix units; Gram positivity and higher-charge completion; exact intertwining; support, norm, incidence and outside-factor scope. |
| [LOCALITY_BOUNDARY.md](LOCALITY_BOUNDARY.md) | 7 | Ancillary compression and domains; extremal path and reverse-power exclusion; physical support diameter; source-tail projection; separation of time accuracy from energy action. |

Total: **32 separate obligations**. Each file states its complete list.
Same-session authors and a separate same-session adversarial reader
checked all four files without finding a substantive mathematical
defect. A scope ambiguity between global charge ten and arbitrary
charged outside factors was clarified explicitly before publication.
This collaboration is internal author-side checking, not independent
external review or acceptance. The obligations remain open to external
scientific assessment, including the inherited conditional premises.

## 5. Boundaries that review must preserve

The following distinctions are part of the result, not optional caveats:

1. The 512*eta mass bound applies to the exact original source, not
   a newly filtered state or a generic unspecified spectral density.
2. The energy-action norm is source-specific. The infinite polynomial
   still has global norm error pi against f(U) on a full-circle spectrum.
3. The finite region is a sufficient bound, not a lower bound on the
   size needed in practice. No enormous matrix is claimed to be stored.
4. The ideal two-setting energy laws agree exactly with each other.
   They need not equal the original-Q law, and generic perturbations
   need not preserve their exact equality.
5. The all-26-label energy/time result and the 25-label fresh-write
   contrast have different stated memory scopes.
6. The ten-coordinate, twenty-qubit and seven-site bounds are per term.
   Total inventory, term count, incidence, raw norm and spatial range
   remain separately large.
7. The Gram lift exactly preserves the entire finite code, but changes
   the higher-active-charge completion. Global P_10 and the local-code
   statement tensored with arbitrary outside factors are distinguished.
8. The diameter >=2D witness concerns exact agreement on the entire
   code. It is exponentially small and is not a prepared-source witness;
   no useful lower bound for source-specific approximation follows.
9. The source-tail inequality is necessary but its relevant tail has
   not been evaluated or bounded below quantitatively here.
10. The positive two-level example rejects an inference from time
    accuracy to bare energy-action accuracy; it is not a general
    impossibility theorem for dressed or effective Hamiltonians.

No external review, empirical validation, Canon fold, thermal source,
terminal readout, renewal or native six-pentit realization is supplied
by passing these custody checks or by the internal analytical reading.
