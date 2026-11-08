# Scope freeze: C-RELATIVE-CONTACT-FOUR-SLOT-PRICE-N

NON-CANONICAL / L1. This is a notes-only retrospective reproduction contract, **not** a formal public-probe preregistration and **not** a Canon claim. Reservation: #1846. Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

## Frozen question

On O = Z[j], Phi_5(j)=0, rho=j^2, consider 26 marked slots, 22 data and 4 auxiliary. A complete pair contact C_rho^k for k in {1,2,3,4} acts on (a,b) only if a-b belongs to 2O, by preserving a+b and multiplying a-b by rho^k; otherwise it is the identity on that pair. Whole-slot permutations are allowed.

The starting full multiset is {6} + 21 zeros + four explicitly named auxiliary values. Two different final full multisets are tested: four data values (3,3,3,-3) or (3,3,3,3), plus a named final four-slot auxiliary multiset, plus zeros. These are **known-input single-shot** claims, not a multi-input device.

## Code, carrier, accounting, failures

- Arithmetic: only integer coefficient vectors of length 4 in the basis (1,j,j^2,j^3), using j^4=-(1+j+j^2+j^3).
- Account: q(z)=(5 sum c_i^2 - (sum c_i)^2)/2, with total energy sum q. This is the positive trace account of #1833, not SI energy.
- Check each declared pair is present in the current multiset; contact acceptance; exact contact output; total O-valued sum; and total positive trace account after every power-contact step.
- Check final full multiset including the entire changed auxiliary. Check the modulo-(1-j) histogram of the auxiliaries changes and hence a reset with retained data and unchanged other resources is forbidden.
- Power contacts C^k count as one word token, while counting C^+1 or C^-1 would give a different length.
- Falsify a word on the first absent input pair, failed admission, inaccurate calculated successor, broken account, or wrong final state.
- This small verifier does **not** establish the exhaustive lower-bound censuses at energies 17/22, the 130/130 or 294 stored-word inventories, minimum word length, canonical realization, or physical occurrence.

## Provenance and scope separation

Historical 2026-11-01 author note SHA-256 `b8df2422572f4c4a1aa6a0905dc4512857823aae495b2d7201ea767b52db8781` (16001 bytes), received with this task. Its declared `verify_katedrala_pruzkum4_2026-11-01.py` and `words_katedrala_2026-11-01.json` are not in the accessible payload. The executable witness words in this note are transcribed from its published text. Any local replay is reproduction of these supplied witnesses and is not prospective discovery or independent authorship.

Dependency #1833 is an **open NON-CANONICAL proposal**; this document does not import it as Canon. Existing #1845 studies a different Gram/occupied-record scope.

**No L1-to-L2/L3/L4/L5/L6 lift is made.** No public T, no registry row, no Canon edit, no official probe gate, no threshold, no expected output pin and no architecture-grade proof are claimed.
