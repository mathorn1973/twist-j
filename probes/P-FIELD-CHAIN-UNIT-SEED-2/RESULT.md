# P-FIELD-CHAIN-UNIT-SEED-2 result

NON-CANONICAL / L1. Successor of abandoned P-FIELD-CHAIN-UNIT-SEED-1
(identifier consumed; record in PR #1552). First formal run at pin
bc1648745323a8843d2c3cb831b0f585b4e00427 passed: exit 0, empty stderr,
EXPECTED.txt SHA-256
bfaab07056c665a6d5d85d933fc4596fc06cc9d52e5f7cb3535cbda72f92645d
(local Ubuntu 22.04 x86_64 lane; see RUN.md). No frozen falsifier
fired: F-PREMISE, F-TARGET and F-CAP all negative. Candidate status:
candidate-T for the complete-bound and coset-minimum reductions
(PROOF.md), candidate-C for the finite residue table; the required
pull-request workflow supplies the second architecture against the
same EXPECTED.txt. Independent distinct-owner review (lane RB of
#1548) is still outstanding and is not replaced by this result.

## Established at this scope

1. Exactly 20 integer unit seeds H(u)=1 exist (complete by the PROOF
   section 1 bound). They are listed in EXPECTED.txt and do all lie in
   [-2,2]^4, as exposed. Shell counts for H=0..5 are 1,20,30,60,60,120,
   agreeing with the census counts disclosed in the #1323 lineage: the
   unit solutions themselves are lineage-consistent content and are not
   claimed as a new discovery here (F-INHERIT applies to the bare unit
   set; the lineage's accepted bounded census is credited).
2. New finite content: the Lu (mod 5) classification over all 25 gate
   residues. Exactly 20 residues are hit, each with multiplicity
   exactly 1; the five residues with no unit preimage are precisely
   those with last two coordinates (0,0):
   (0,0,0,0), (1,2,0,0), (2,4,0,0), (3,1,0,0), (4,3,0,0). In particular
   the zero residue has no unit preimage.
3. Coset minimum: min H on {y in L Z^4 : y = (0,0,3,1) mod 5} is
   exactly 5, attained uniquely at y = (0,0,-2,1), whose unique
   preimage is the unit seed ustar = (0,-1,-1,2), H(ustar)=1. All
   exposed targets of #1548 lane B match, including uniqueness.

## Not established

No production of a complete FIRST-WORK source by native U, no physical
least-energy selection rule, no energy-funded transport, and no Canon
or registry change. The H(w)=1 hypothesis of FIELD-CHAIN-FIRST-WORK
now has a complete residue-level seed census at this scope; which seed
(if any) a physical preparation realizes remains outside this probe.
Existence, minimum, uniqueness and physical choice of representative
remain strictly separated, as frozen.
