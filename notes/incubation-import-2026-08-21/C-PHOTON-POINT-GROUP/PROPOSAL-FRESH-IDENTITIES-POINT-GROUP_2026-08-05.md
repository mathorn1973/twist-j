# PROPOSAL: fresh identities after the P-A3-FCC-POINT-GROUP-1 STOP

```text
STATUS   NON-CANONICAL proposal for an owner decision. No authority, no
         claim, no probe opened. The sealed probe stays sealed; nothing
         below reuses, renames or resumes it.
BASIS    STOP record claude/STOP-RECORD-P-A3-FCC-POINT-GROUP-1_2026-08-04.md
         (five blockers: Z3/Z4 typing, unfrozen F^-1, unfrozen D3
         generators, missing quarter-turn, undetermined K11a mutation).
RULE     a fresh identity must differ in FROZEN SCOPE, not just in name;
         a cosmetic rename would be a resume in disguise. Every option
         below changes the scope so that at least one blocker becomes
         structurally impossible, not merely patched.
```

## Design principle

The sealed probe died on one root cause: one identity carried two
ambients (Z^4 and Z^3) plus a bridge plus demos, so its preregistration
could not be self-contained. The repair is not a better patch, it is a
smaller probe: ONE AMBIENT PER IDENTITY, and the bridge itself as its own
identity whose typing is the claim rather than the plumbing.

## Option 1 (recommended): a chain of four minimal identities

```text
P-FCC-AXES-FORCED-1        ambient Z^3 only. D_3 defined directly as the
                           even-sum sublattice; generators DISPLAYED in
                           the prereg with their Gram. Claim: the norm-4
                           shell is exactly {+-2 e_i}; every isometry of
                           D_3 is a signed permutation; the point group
                           is exactly the 48 signed permutations with
                           order multiset {1:1, 2:19, 3:8, 4:12, 6:8}.
                           Kills blockers 1, 3 by construction; needs no
                           F, no quarter-turn, no A_3. The spine is the
                           axes-forced proof, which is the strongest
                           piece of the candidate record.

P-ICOSAHEDRAL-NONLIFT-1    ambient: 3x3 matrices, one displayed reduction
                           map entrywise mod 5. Claim: the finite
                           orthogonal group of the reduced form has order
                           240 with exactly 24 elements of order 5; the
                           48 displayed signed permutations reduce
                           injectively to an index-5 image containing no
                           order-5 element; hence no icosahedral subgroup
                           lifts. This is the physically loaded claim and
                           deserves its own identity.

P-A3-FCC-ISOMETRY-1        the bridge AS THE SUBJECT. Both matrices
                           DISPLAYED in the prereg: F and its exact
                           inverse (2 F^-1 is integral; display it).
                           Claim: Gram transport, bijection of the 12
                           roots onto the 12 minimal vectors, conjugation
                           carries the A_3 automorphisms onto the 48
                           signed permutations. Here the Z^4 to Z^3
                           typing is the CONTENT, so blocker 1 cannot
                           recur as plumbing and blocker 2 is the
                           displayed data itself.

P-FCC-FOURTH-ORDER-CONE-1  ambient Z^3 only. Shells at norms 2, 4, 6, 8
                           with sizes and anisotropies as frozen numbers,
                           the cone w1 = 8 w2 - 18 w3, the three
                           witnesses, the {2,6} nonexistence. Opens only
                           after P-FCC-AXES-FORCED-1, whose group it
                           cites as a displayed premise.
```

Each identity is small enough that the preregistration can display every
object it mentions, which is the whole lesson of the STOP. Each survives
or dies alone; a break in one does not seal the others.

## Option 2: one identity, one ambient, narrowest scope

```text
P-D3-SIGNED-PERMUTATION-1  Z^3 only, the content of P-FCC-AXES-FORCED-1
                           plus the order multiset and nothing else. No
                           mod 5, no bridge, no shells, no cone. Cheapest
                           possible re-entry; the rest of the content
                           waits for later identities or stays candidate.
```

## Option 3: spend no identity on the group at all

Register the point group not as its own probe but as a displayed premise
block inside the successor operator probe (the symbol expansion), with
one verification gate. The group facts stay candidate-grade until the
operator probe consumes them. Cheapest in identities, weakest in public
floor; the octahedral branch decision would carry no public row of its
own.

## Discipline for whichever option is chosen

```text
1  Quarter-turn and every expected-fail mutation: either dropped from the
   probe scope entirely, or frozen as explicit displayed data. No gate
   may consume an object the prereg does not display.
2  Pre-pin blind review: before any pin, the other model family reads the
   PREREG DRAFT alone and answers one question per gate: can I derive
   the pass and fail condition without the verifier? This is review, not
   a formal gate, so it is allowed pre-pin, and it would have caught all
   five blockers without burning an identity.
3  New registry row(s) are a separate owner decision; PHOTON_CONTINUUM
   currently has no live row and nothing here creates one.
```

No probe opens on this proposal. The decision, including the option, the
names and the ordering, is the owner's.
