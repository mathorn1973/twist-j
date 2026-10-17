# P-FIELD-CHAIN-UNIT-SEED-2

Status: preregistered public probe candidate, RESULT-EXPOSED.
Action layer: L1 only.
Owner: A. M. Thorn / Muse-20261016-field-chain-unit-seed session.
Public lock: #1553. Parent program: #1548 lane B (DISPATCH_RELEASED;
body read back at 13858 UTF-8 bytes, SHA-256
c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87).
Branch: probe/P-FIELD-CHAIN-UNIT-SEED-2.

## Predecessor

P-FIELD-CHAIN-UNIT-SEED-1 (public lock #1549) is ABANDONED. Its pin
066ef45911f6215f7574daba80fd53616ee1c66d was read back before
execution; its single formal run exited 1 on a verifier fixture defect
(a cancelled polynomial coefficient left an explicit zero entry and
broke a dictionary equality for the sum-of-squares identity) before
any enumeration ran. It produced no scientific conclusion, no
EXPECTED.txt and no RUN.md; its abandonment record is PR #1552 and the
identifier is consumed. This successor changes no scientific equation,
domain, shell cap, threshold or falsifier from #1549. Verifier changes
are fixture-level only: zero-coefficient cleaning in the two
polynomial-dictionary comparisons, correct x/Lx pairing in the
minimizer report, and the new identifier in banners.
Source: public main a632c6a162dc87e60104d7a478e7650a6d5c4a1b.
Authority: Public Canon v102 ACTIVE, peeled tag canon-v102 at the same
commit, content b04e22dd3ed8e4240cff347364f24670d4183a4d, CANON.md
1024033 bytes SHA-256
c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1
(all recomputed this session). The immutable canon-v102 release is
published, closing the release-publication condition noted as open in
#1548. Collision scan this session: no branch, probe directory, issue
or registry entry for P-FIELD-CHAIN-UNIT-SEED-2 other than #1548/#1553
and the abandoned predecessor lane.

This probe is result-exposed and proof-first, not blind discovery: the
assignment in #1548 publishes its targets. No part of the supplied
historical exploratory program `v103_kontrola.py` was available or used.

## Lineage (inherited, not new ownership)

Canon v102 supplies, as proved theorems used here only as definitions
and audited premises: the matrices B_f, A_f, L, Vinv=5L^-1 of shared
proof section 2; H(y)=y^t B_f y/2 positive definite and integral;
L=(I-A_f)(I-A_f^2); H(Lx)=5H(x); det L=25; the image criterion
a+2b=c+2d=0 (mod 5) with exactly 25 image residues; and the Hraw
completed-square certificate.

#1323 (C-FIELD-J-ENERGY-READOUT-N, notes, v96 basis) already earned an
accepted scoped containing box, norm bound and complete H<=5 census
(mathematical statement B ACCEPT; its Python contract REJECT and the
successor acceptance at 3f53cff429c67fbdfa95941b3024279d9fd59638 are
preserved unchanged). The integer solutions of H(u)=1 therefore sit
inside existing lineage evidence. The only new scope claimed here is:
a self-contained completeness bound for H(u)=1 at the literal v102
B_f coordinates, the Lu (mod 5) classification of all unit seeds over
the 25 gate residues with multiplicities, and the exact minimum of H
on the displayed coset class with attainment/uniqueness. If the result
finds any of this already present in the lineage notes, RESULT.md must
report inheritance instead of novelty.

## 1. Equation (frozen targets)

For y=(a,b,c,d) in Z^4, with Canon
B_f=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]]:

    H(y) = 2a^2 - 2ab + 3b^2 + c^2 + d^2 + 2ac - ad - bc + 3bd.

G1 UNIT CLASSIFICATION. Classify every u in Z^4 with H(u)=1.
Completeness rests on the polynomial identity (Canon Hraw certificate
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2 at the P embedding
E=(a-b,-a,b,b), M=(c,d)):

    4H(y) = (2a-2b+c-d)^2 + (2a+c)^2 + 2(2b+d)^2 + c^2 + (c+d)^2.  (*)

For H(y)<=k every squared form is <=4k and 2(2b+d)^2<=4k; with
s=floor(sqrt(4k)) and t=floor(sqrt(2k)) this gives the frozen complete
box |a|<=s, |b|<=(t+2s)/2 floor, |c|<=s, |d|<=2s. For k=1 the box is
a,b,c in [-2,2], d in [-4,4]. The exposed [-2,2]^4 box is a hypothesis
about the output, not an input bound.

G2 GATE RESIDUES. For each of the 25 residues r in F5^4 with
r0+2r1=r2+2r3=0, list exactly the units u with Lu=r (mod 5) and the
multiplicity, including residues with none. The verifier also checks
exactly that the mod-5 image of L equals this 25-element criterion set.

G3 COSET MINIMUM. Decide min H(y) over
{y in L Z^4 : y=(0,0,3,1) mod 5}, attainment and uniqueness. Proof
route, frozen: H(Lx)=5H(x) and L is injective (det L=25), H is a
nonnegative integer form with H(x)=0 only at x=0 (from (*)), so the
coset minimum is 5 times the least shell k>=1 containing an x with
Lx=(0,0,3,1) (mod 5); minimizers correspond bijectively. The verifier
searches shells k=1..5 in the complete boxes of G1. If no shell up to
the frozen cap 5 attains the class, the run records
NONE_WITHIN_CAP5 as a retained negative disposition; the cap is not
raised after this pin.

Exposed targets to prove or refute (not asserted by the verifier;
RESULT.md compares): 20 units; 20 distinct image residues; 5 residues
without a unit preimage; ustar=(0,-1,-1,2) with L ustar=(0,0,-2,1) a
unit preimage of (0,0,3,1), unique; coset minimum 5.

## 2. Code

`verify.py` in this directory, Python standard library only, exact
integer arithmetic (matrix products, Bareiss determinant, polynomial
coefficient dictionaries, integer square-root bounds). It asserts only
internal consistency and audited inherited premises (matrix identities,
SOS identity (*), H(Lx)=5H(x) and H>=0 on the enumeration box, zero set
{0} in the box, image-mod-5 criterion, gate count 25); the scientific
classification is printed as a deterministic table and compared with
the exposed targets in RESULT.md. A mismatch with an exposed target is
a retained result, not a verifier failure; an assertion failure is a
fired premise falsifier and is preserved, never repaired by editing
this pin. Frozen commit and SHA-256 of both files are recorded in
#1553 and in the metadata receipt on #1548 after public readback, and
no formal gate execution happens before that readback.

Run, from the repository root, in a Linux environment:

    PYTHONHASHSEED=0 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 \
    python3 probes/P-FIELD-CHAIN-UNIT-SEED-2/verify.py

stdout must match the later EXPECTED.txt byte for byte; the required
pull-request workflow reruns the same head on x86_64 and aarch64.

## 3. Carrier and data

Carrier: Z^4 with the displayed quadratic form and matrix L; finite
enumeration domains are exactly the G1 boxes for shells k<=5
(a,b,c,d ranges printed by the verifier). No external data, fixtures,
randomness, floating point, or third-party material. Inputs are only
the Canon v102 definitions above, this preregistration, and the
exposed targets of #1548/#1553.

## 4. Systematics

Result-exposed confirmatory audit: targets were public before this
pin, so no blind-discovery claim is made. Transcription is guarded
three ways (polynomial vs B_f coefficients; SOS coefficient identity;
matrix identity recomputation). The unit census of the #1323 lineage
is a known cross-check, credited, not imported as code. The verifier
author is the probe owner; the distinct-owner reviewer lane RB of
#1548 must freeze its own derivation before reading this probe's
proof, verifier or outputs beyond the pinned specification.

## 5. Failure threshold (falsifiers)

- F-PREMISE: any asserted identity in verify.py fails (exit nonzero).
  Scientific conclusion: an inherited premise or its transcription is
  false at this scope; preserve stdout/stderr record per POLICY, do
  not repair under this identifier.
- F-TARGET: the printed classification differs from any exposed target
  (counts, residue coverage, ustar, uniqueness, minimum). Conclusion:
  that exposed hypothesis is refuted at this scope; the computed
  classification is the retained result.
- F-CAP: no minimizer within shell cap 5. Conclusion: coset minimum,
  if attained, exceeds 25, or is unattained; G3 stays open at this
  scope and no larger search is run under this identifier.
- F-INHERIT: any of G1-G3 found already completely present in the
  cited lineage. Conclusion: NO_NEW_CLAIM for that part.
Custody/runtime failures (hash mismatch, environment defect) are STOP,
not scientific results.

## 6. Action layer

L1 only. This is finite integer lattice arithmetic about the selected
field cell. It supplies no native-U production of a source, no contact
or energy-funded transport, no physical selection of a least-energy
representative, and no Canon, registry, frontier or gate change. The
FIRST-WORK hypothesis H(w)=1 is addressed only as a mathematical seed
existence/classification question. Status remains NON-CANONICAL
candidate scope until any separately reviewed promotion.
