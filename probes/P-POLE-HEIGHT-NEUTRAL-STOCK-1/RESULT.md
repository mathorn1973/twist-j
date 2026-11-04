# Exact witnesses, neutral-stock construction and orientation obstruction

NON-CANONICAL / L1. Analytical candidate-T with exact computational audits;
no Canon promotion. The first prospective run completed with all fixed
audits passing and a found catalytic X word. All source bytes remain at
pin d321ff7aca4106bf0dc516f08d105da2cfa1b6bf.

## 1. The supplied witnesses

For source (B,-B,u,u,0,2,-2), W17 reaches

    (u+B,u-B,0,0,-B,1+p,-2p).

W20 reaches

    (u+B,u-B,0,0,0,2,-2).

Every requested contact admits for t=+1. Both arithmetic routes agree at
every step and the literal reversed C^4 word restores the complete source.
This verifies reachability and W20's helper restoration. It does not
establish17/20 minimality. Both unchanged words fail the first-four target
for every other tested t in {-2,-1,0,2}; their full endpoints are retained
in EXPECTED.txt. These are known-input witnesses, not common encoders.

## 2. One nonneutral helper and neutral stock X suffice

Let X=1+j-2j^3. The new search independently finds the chronological word

    45 56 16 16 16 25 25 25 25 26 26 26 26 36 36 46
    56 56 56 56 26 26 26 26 46 12 12

which performs exactly

    (B,-B,u,u,X,2) -> (u+B,u-B,0,0,X,2).

All27 contacts admit and change the state. Both helpers return exactly.
Total Q=43 is preserved at every step, as are the full Hermitian account,
slot sum and marked residues. Independent quotient arithmetic agrees with
the power-basis route after every step. The full108-contact literal inverse
restores the complete initial state.

The search completed forward/backward balls through radii14 and13,
containing1690 and1453 states, after18870 and16200 candidate edges.
No state or depth cap was reached. There was no intersection in earlier
complete balls. The first complete-layer intersection has distance27:
this certifies the shortest forward-elementary contact word for this
specific source and this complete catalytic endpoint, using the15 edges.
It is not a minimum over other stocks, helper counts, endpoints or gate
alphabets. The second arithmetic audits all encountered pair cycles and
the witness, not a separately generated second breadth-first search.

The reported27 agrees with this new result. None of the other four inputs
passes the first-four or helper-return target when given this unchanged
word. A common five-input word remains open; input-specific success does
not settle it. The first contact45 is the constructive identity
C(u,X)=(2(1-j^3),0), with the reference and its consumed state fully present.

### A direct transition certificate for the27-word

Put D=1-j^3 and A=j-j^3. The grouped chronological program is

    C45 C56 C16^3 C25^4 C26^4 C36^2 C46 C56^4 C26^4 C46 C12^2.

The following full states permit direct checking without repeating the
search. Every displayed grouped pair has even difference. For an admitted
pair with center s and half-difference d, C^k gives (s+p^k d,s-p^k d).
The table was also checked analytically after the actual run; it is a
post-run explanation, not an additional preregistered prediction.

| Completed group | Complete state |
|---|---|
| Start | (B,-B,u,u,X,2) |
| C45 | (B,-B,u,2D,0,2) |
| C56 | (B,-B,u,2D,B,1+p) |
| C16^3 | (D,-B,u,2D,B,1+j^3) |
| C25^4 | (D,D,u,2D,-D,1+j^3) |
| C26^4 | (D,u,u,2D,-D,1+j) |
| C36^2 | (D,u,0,2D,-D,2) |
| C46 | (D,u,0,D,-D,3-j^3) |
| C56^4 | (D,u,0,D,X,1-j+2j^3) |
| C26^4 | (D,1-2j+j^3,0,D,X,1+j^3) |
| C46 | (D,1-2j+j^3,0,0,X,2) |
| C12^2 | (u+B,u-B,0,0,X,2) |

Before the final group the first pair has center u and half-difference A;
p^2 A=B. The helper restoration is already complete at that boundary.
Renaming every slot label1 with2 and2 with1 gives a separate valid
negative-input word, by contact covariance under that permutation. This
analytical relabeling does not supply one common unknown-sign program.

## 3. Why 2u fails despite producing account15

PROOF.md proves an odd-input no-go for stock2u without using its reported
11080-state orbit. Conservation classifies every eligible pair of helper
endpoints as (2-j-p^k,2-j+p^k). Translating all six slots by-u puts every
such target in N^5 x R, a reversible closed alphabet, while the initial
state has a translated account15 value outside it. This excludes even
input-specific words and unrestricted final helpers in the stated six-slot
preparation. The corresponding catalytic theorem excludes every stock in
u+N, and any finite number of restored helpers meeting its hypotheses.

Yet C^3(2u,2)=(u+B,2-j+j^2), with accounts15 and13. Thus an explanation
based solely on the impossibility of creating a local account15 is false.
Orientation and the complete endpoint constraints matter. X escapes the
translated trap, and its actual successful word above proves sufficiency
for this particular known-input preparation. No universal rule saying
that every stock outside the trap succeeds has been established.

The audit checks1071 ordered local pairs through five powers in each of
the unshifted and shifted alphabets, including explicit translation
covariance. Exactly20 of the225 R*R pairs escape (N union R)^2, matching
the disclosed review comparison. This verifies one way an extra
nonneutral helper can escape the original alphabet, not its necessity.

The21 excluded catalytic stocks have Q-counts (0:1,5:7,10:6,15:6,20:1).
The complete neutral Q<=20 ball contains171 elements, with Q-counts
(0:1,5:20,10:30,15:60,20:60). The review reported142 tested preparations;
that statement is not relabeled as a complete-ball census. This probe
does not audit its claimed absence of Q10 successes or its34-contact word.

## 4. Remaining boundary

The frozen source/limits were not changed after public readback. No
scientific falsifier fired, no search limit was reached, and no failed
run was discarded. Static crossreviews were author-session checks.
Required CI reproduction and independent mathematical acceptance remain
distinct; actual architecture-check results accompany the PR handoff.

No sealed predecessor is edited. This construction uses declared slots,
prepared stocks and a supplied control word. It does not yet implement the
native-machine preparation, an autonomous common selector, physical
energy readout, Planck normalization or electromagnetic alpha.
