# RESULT: P-KERNEL-MIRROR-TRIANGLE-CENSUS-1

Status: PASS / exact verification and two-architecture replay; PUBLIC-source, NON-CANONICAL, L1.

The first formal public-pin execution completed with **27/27 PASS**, exit
zero and empty stderr. It matches every disclosed pair/triple target and
the full group target. Independent permutation/orbit-stabilizer computation
agrees with the affine computation on all 21 records, including the full
orbit of 15625 and stabilizer order 200. No falsifier fired.

The exact transcript and source hashes are in [RUN.md](RUN.md) and
[EXPECTED.txt](EXPECTED.txt). The original supplied archive remains
unchanged; source custody and corrections are in [SOURCE.md](SOURCE.md).
This is public verification of known results, not a new blind discovery.

## Evidence and scope

- [PROOF.md](PROOF.md) is a separate candidate-T analytic argument for
  all six translations, order 3125000, transitivity, point stabilizer 200,
  and absence of three for all words and every section. It also gives
  the common linear sign character. A direct exact code audit checks the
  displayed translation and covector identities.
- [SURFACES.md](SURFACES.md) gives the precise chamber gluing, a proof that
  all links are circles, the Euler formula and simultaneous orientability.
  Its numerical counts use the census orders. No group action on the
  original 15625 cell states is substituted for the regular chamber action.
- The pair orders are 2 for ab, 5 for bc and de, and 10 for the remaining
  seven pairs. All ten literal triples have negative excess and orientable
  auxiliary surfaces, with the exact orders, chi and genera frozen in
  [PREREG.md](PREREG.md). Their intermediate linear/translation decomposition
  is checked by the affine implementation; the second implementation
  independently checks group orders and surface records.

The initial one-architecture table had candidate-C evidence. Clean public
x86_64 and aarch64 jobs subsequently reproduced the same 4342-byte stdout
and passed the aggregate check in
[run 37290826956](https://github.com/mathorn1973/twist-j/actions/runs/37290826956),
at head `afb5062fdbb5751dc1ad67ce321e56cec113ea8f`. The computation gate is
now satisfied; exact source and output identities are in RUN.md. Each
architecture also passed all 183 repository-tool tests.

The analytic arguments remain candidate-T for public review. The verified
table receives no registry status in this probe. Neither evidence route
creates a registered T here or substitutes for a later explicit Canon fold.

## Boundary retained

No P1--P5 observations, exponent-ten theorem or arbitrary-word triangle
classification is included. The all-word no-three consequence follows
from group order and is separate from the ten literal-triple table.
Independent labelled cells retain that obstruction. The CSUM comparison
in PROOF.md adds operations and exhibits `(P Q^-1)^2` of order three;
it does not derive or realize those operations from the selected U or J.

This probe changes only its own directory. Canon, registry, evidence and
dependency ledgers, gates, frontier and physical HOLD remain unchanged.
The ion-profile calibration lane is separate and still needs independent
physical inputs. The auxiliary surfaces supply no physical locality,
curvature, events, time or spacetime interpretation.
