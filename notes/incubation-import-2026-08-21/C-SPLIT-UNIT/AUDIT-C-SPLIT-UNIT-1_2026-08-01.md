# AUDIT C-SPLIT-UNIT-1, external review accepted

NON-CANONICAL. Audit record for the incubation candidate C-SPLIT-UNIT-1.
No authority, no Canon change. Date 2026-08-01, same day as the runs.

An independent external review (relayed by the owner; seat and model family
not verifiable from this session) audited the candidate against Public Canon
v30. Verdict accepted in full. This record pins what was corrected, what was
re-verified, and what stands. The RESULT file and every frozen pin are
untouched; where this audit re-grades a label, this audit supersedes the
RESULT prose.

## 1. What the audit hit, and the acceptance

All four findings are prose-layer. No frozen gate fired; the 38 + 8 gates,
the SHA-256 pins, and the two-architecture byte identity stand as run. Each
auditor identity below was re-verified here in exact arithmetic before
acceptance.

```text
FINDING 1   chi5 is not conjugation. ACCEPTED.
            c = sigma_(-1) = sigma_4 generates <c> = {1,4} = squares =
            ker chi5, and chi5(c) = +1. Conjugation generates the KERNEL
            of the bit; the bit is the unique nontrivial character of the
            quotient G/<c> ~ C_2. They are canonically linked at p = 5
            (squares = {+-1} iff (p-1)/2 = 2 iff p = 5) but not identical.
            The phase doublet is c-odd; c-oddness alone already forces its
            trivial and chi5 components to vanish. The rev 1 sentence "the
            bit operator is epsilon = complex conjugation" was wrong as a
            label; the I3 gate computation (the c-grading algebra) is
            correct and untouched.

FINDING 2   the pure sector holds the LOG modulus, not the raw modulus.
            ACCEPTED, with one clarification. Exactly
              (|sigma_a(J)|)_a = (sqrt5/2) . 1 - (1/2) . chi5,
            re-verified here: trivial component sqrt5/2 (half the Gauss
            sum), chi5 component -1/2. Purity holds only for the
            logarithmic image log|sigma_a(J)| = -(ln phi) chi5(a). The
            same centering applies to the registered Li_2 face:
              (Re Li_2(sigma_a(J)))_a = (pi^2/20) . 1 - (pi^2/25) . chi5,
            re-verified: mean pi^2/20 (the registered orbit sum pi^2/5
            over 4), centered part pure chi5. Clarification: the frozen
            layer never asserted raw-modulus purity (gates C1..C4 are the
            multiplicative products, T6 of the candidate doc carried the
            log explicitly); the loose phrasing lived in the session
            summary. Corrected everywhere in rev 2.

FINDING 3   uniqueness of J needs the class condition 1 + eta. ACCEPTED.
            The theorem stands within the class: for eta in mu_10 the
            norms of 1 + eta are 16, 0, 1, 5 by type, so the units in the
            class are exactly the one Galois orbit {1 + zeta^k}. What the
            field does not force is the class itself: U = mu_10 x <phi>
            gives the torsor mu_10 . phi^{+-1} of twenty minimal-quantum
            units, and J is one of them. Sharpening recorded here: even
            exceptionality does not select the orbit, because phi is
            itself an exceptional unit (1 - phi = -phi^-1, re-verified);
            the selecting property is "u - 1 pure phase". Hence:
            within the class, unique orbit and minimal quantum ln phi
            [candidate-T]; "the field forces its first word" [D], valid
            only relative to the premise "distinction is sizeless".

FINDING 4   the three zeros are not one C_4 theorem. ACCEPTED.
            sum chi5 = 0 and the unit log sum are the same trivial
            projection in the same C_4 module. Tr[P,Q] = 0 is trace
            cyclicity and End(V) = k I + sl(V), a different module with
            no canonical morphism to the C_4 datum. The instances are
            individually T; the unification "zero scalar projection of a
            nontrivial object" is a [D] reading pattern, not a theorem.
```

Also accepted: "the bit generates the scale" is [D] (the identity
ln phi = (sqrt5/2) L(1, chi5) is classical [T, literature]; the scale is
dimensionless arithmetic only, METRO-EDGE-SCALE [O] untouched), and the
p = 5 sector census is mathematics, not an independent physical selection
of p = 5; Canon section 16 is untouched and no such reading is registered.

## 2. The surviving skeleton (auditor's formulation, adopted)

```text
The logarithmic image of J carries the single quadratic bit and the
principal argument carries the single phase pair. Within the class
1 + mu_10, J is the unique Galois orbit of units and realizes the
minimal logarithmic quantum ln phi.
```

candidate-T at L1, on the frozen pins. Everything ontological around it is
[D]; the completeness claim stays [H] with its falsifier; bit-to-driver,
decoder, curvature, and measure remain the open Canon rows they were.

## 3. Re-grading table (supersedes RESULT prose where they differ)

```text
T1 size character (log form)      candidate-T   unchanged
   raw modulus decomposition      candidate-T   new line, covered by frozen
                                                gates plus one-step arithmetic
T4 orbit within 1 + mu_10         candidate-T   scope now explicit
   "field forces its first word"  D             demoted from the rev 1 gloss
T5 bit uniqueness and census      candidate-T   conjugation relation corrected
T6 two sectors (log, Arg)         candidate-T   unchanged; Li_2 face holds
                                                after centering
T7 Gauss sum, L(1, chi5)          T literature  identity; "generates the
                                  D             scale" reading
T8 three zeros                    T each        instances
                                  D             unification
census p = 5 physical reading     none          not claimed, not registered
```

## 4. Artifact location, corrected process

The rev 1 bundle lived only in the claude.ai project lane (claude/ paths of
the project, per the project contract). That lane is invisible to non-Claude
seats and is not a durable handoff; the working agreement is explicit that
the only shared bus is git. Accepted. The bundle now also lives in public
git under notes/C-SPLIT-UNIT-1/ on branch notes/c-split-unit-1 (this
directory), NON-CANONICAL, touching no canon file, README with reproduction
commands and the hash manifest included. The claude/ prefix inside the
project is the incubation lane of the project contract, not a repository
directory; the repository home of a non-authoritative candidate is notes/,
as the audit states.

## 5. Standing note on the audit itself

The audit hit only the narrative layer while all 46 frozen gates survived.
That is the gate design rule doing its job on the computations and a
reminder that it does not cover prose: labels and glosses need the same
adversarial pass as gates. If the auditing seat was a non-Claude family
seat, this pass partially satisfies the cross-family break requirement of
the working agreement for the algebraic block; the owner can record the
seat. PROMO stays deferred either way.
