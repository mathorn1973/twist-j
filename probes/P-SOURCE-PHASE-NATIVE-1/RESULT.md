# Result: P-SOURCE-PHASE-NATIVE-1

**PASS for the preregistered finite exact audit. NON-CANONICAL, L1.
Candidate: C-SOURCE-PHASE-NATIVE-1. Independent theorem-grade review:
PENDING.**

The first accepted execution at pin
`751b7f219ccc65f7dba5b04ba248ab0df93bd526` passed every registered assertion,
returned exit 0 and emitted no stderr. The platform was Ubuntu 24.04.1 LTS,
x86_64, CPython 3.12.3. The fifteen output groups are recorded verbatim in
[EXPECTED.txt](EXPECTED.txt); the hashes and execution provenance are in
[RUN.md](RUN.md). No total count of atomic comparisons is claimed.

The exact checks cover the two residue places, raw coefficient updates,
native preparation and charts, the all-tick factor on the registered finite
fixtures, residue propagation, the formal inverse prefix, and the specified
normalization controls. The complete computational scope and bounds remain
those of [PREREG.md](PREREG.md). The all-time arguments are submitted
separately in the [proposal](../../notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md).

The registered negative controls were reproduced:

- The four-point Frobenius profile is a characteristic-five statement.
  For the characteristic-zero comparison convolution, the coefficient
  of the fifth power at (3,0) is 25600, and only its residue is zero.
- The unit impulse has no finite-support preimage under B. The displayed
  inverse belongs to the specified one-sided formal-series completion;
  it is not a finite-support inverse.
- On all bilateral infinite fields, the nonzero field (-1)^R is in ker(B).
  Thus finite-support injectivity does not extend to arbitrary fields.
- Positive rescaling can change raw residues, and normalizing each port
  separately changes coherent weights. The initial global normalization
  is fixed and does not define a residue map on normalized rays.
- The wrong residue place annihilates the full-phase numerator.

No unexpected falsifier fired in the registered finite domain. This is not
a claim that unrestricted counterexamples have been excluded. In
particular the full spectral-energy and spatial-operator proofs are not
certified solely by this finite verifier.

At this recorded stage the finite audit supplies at most candidate-C
evidence from one architecture. Required two-architecture CI replay is a
reproducibility gate, not a T promotion. The submitted theorem statements
still require independent reading against their frozen inputs. No Canon
entry, version, release or Frontier status has changed.
