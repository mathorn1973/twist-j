# P-RELATIVE-CONTACT-WORKBANK-REUSE-1

NON-CANONICAL / L1 / prospective composition with disclosed source exposure.
Owner: A. M. Thorn, workbank-reuse continuation, 2026-11-03.
Reservation: https://github.com/mathorn1973/twist-j/issues/1878.
Base: ACTIVE Public Canon v108, main
17de90b58f814238e151aac77badde6654b52627.

## 1. Question, action layer and exposure

Can the actual v108 apparatus write its two records, copy them into fresh
permanent banks, and reverse its work to restore the entire active input,
clock, controls and the SAME two workbanks, then repeat this for three
independent prepared inputs under one fixed complete program?

This is an L1 exact finite composition claim. The v108 proofs, word, code and
outputs and the supplied C-BANK-COPY-WORD-1 package were read before design.
The copy word and its five successful cases are known results. The present
three-use composition has not been executed before this pin. There is no
blind-discovery or independent-author claim. PROVENANCE.md records the source
and corrections without importing the private working archive.

All scientific source in this directory is committed, pushed and publicly
read back byte for byte BEFORE verify.py executes. Only static inspection,
hashing and AST parsing occur before the pin. After a completed run add only
EXPECTED.txt, RUN.md and RESULT.md. Do not modify the frozen source or
thresholds to rescue a failure; follow the repository's abandoned-pin rules.

## 2. Equation, code and complete alphabet

O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2. For four integer coefficients,

    Q(a) = (5 sum_i a_i^2 - (sum_i a_i)^2)/2.
    C(a,b) = (a,b)                         if a-b is not in 2O;
    C(a,b) = ((a+b+rho(a-b))/2,
              (a+b-rho(a-b))/2)           otherwise.

The contact is total and bijective; C^5=id and C^-1=C^4. Diagonal and refused
pairs are fixed. The other primitive SWAP(i,j) exchanges complete slots and
is its own inverse. Contacts preserve Q, sum and each labelled residue
modulo (1-j); swaps preserve Q and sum and transport residues. Swapped pairs
in the admitted program have equal residues, a separately checked property.
The parity guard is part of the law; global O-linearity is not asserted.

All words act chronologically left to right, with zero-based addresses in
code and the following construction. S is the actual 535-contact v108 word,
built from its fixed blocks and checked contact by contact against the
unchanged WORD535.txt (one-based fixture), SHA-256
ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b.
Let W=S^10. Reverse a literal contact word by reversing its order and replacing
each contact by four identical contacts. No inverse shortening is used in
the counted program.

The six-slot copier, written ONE-BASED for comparison with its source, is

    W6 = C14 C14 C45 C14 C14 C14 C16 C16 C16 C16 C14 C16.

For source bank at a and target bank at t, K(a,t) concatenates W6 for p=0..4,
with q=(p+1) mod5 and six-slot address list
(a+2p,a+2p+1,a+2q,a+2q+1,t+2p,t+2p+1).
Thus K has 60 contacts. Its source contains exactly one marked pair, its
target is blank. Two K operations cost 120 contacts per experiment.

For stage h=0,1,2, permanent targets start at t_h=31+20h and t_h+10.
The identical cycle pattern is

    W K(11,t_h) K(21,t_h+10) W^-1.

Between stages h=0 and h=1, execute five swaps (i,91+5h+i), i=0..4.
The whole fixed word has 80610 contacts and ten swaps. Its literal inverse
has 322440 contacts and ten swaps. No input chooses any edge, stage count,
next input, primitive or archive address. The program is a supplied finite
schedule; no autonomous controller or native-U identification is asserted.

## 3. Carrier, data and common preparation

Carrier O^101. Slots 0..30 are the SAME v108 active apparatus at every stage:
active input 0..4, controls 5..10, workbanks 11..20 and 21..30. Permanent archives
occupy 31..90, and two queued five-slot inputs occupy 91..95 and 96..100.
Set u=1-rho, w=1+rho, b=1+rho^2, F=C01 C12,
Y_n=F^n(0,2,0) of period9, X_r=(rho^r w,-rho^r w).
Each input I_(n,r)=(Y_n,X_r), (n,r) in {0,1} times Z/5, has account 14.
All 1000 ordered triples of these inputs are admitted independently.

Controls are (0,u,0,0,w,0), account 8. A blank bank is M_empty=(-b,b)^5,
account 30. A marked bank M[p] rotates only pair p by rho. Blank is distinct
from every marked bank, including M[0]. Initially all eight banks are blank.
The 86 designated auxiliary slots are identical in all preparations and have
account 248. Fifteen input-system slots have account 42; twelve of those slots
vary across the input family. Complete account 290 and ring sum 8 are fixed.
The queued inputs are explicit data, not input-dependent auxiliary donors.

No input or bank is assigned a new value during evolution. Each cycle copies
before reversing W. The inverse restores the active prepared input as well
as the controls and workbanks. The five swaps park that actual restored input
in the cartridge just emptied. After three stages the core holds input 3,
cartridge 91 holds input 1 and cartridge 96 holds input 2, all in their original
preparations. All three two-bank permanent records remain on the carrier.

## 4. Predictions and retention

For input(n,r), W ends with records

    (M[-r], M[-r-Delta_n]), Delta_0=1, Delta_1=8,

indices modulo5. Source becomes Y_(n+10), clock X_(r+10), and controls are
ready. The copy restores each workbank at the 12-contact module boundaries;
it need NOT preserve that bank at every internal contact. Permanent targets
are required blank and the copier is NOT an involution. Its declared inverse
has 240 contacts per bank.

After both copies and W^-1 the complete first 31 slots equal their prepared
stage input. Previously completed permanent archives are never addressed by
any subsequent primitive. Each new archive is untouched from its completed
copy onward through all later forward operations. The final reader must
parse the six actual permanent banks, recover all three(n,r) pairs using
(pa-pb) mod5 in {1,3}, and distinguish all 1000 preparations without reading
workbanks, source, cartridges or original input labels.

The whole-state inverse deliberately removes the records and restores every
coordinate, including the original input order and six blank archive banks.
It is not a retention-preserving reset. The forward checkpoint count of
fresh permanent pairs of banks is3,2,1,0; this refers to the chosen retained
history protocol, not a globally monotone function of a reversible state.

## 5. Accepted verifier, exhaustive inventory and systematics

verify.py uses only the Python standard library, exact integers, assertions,
fixed words and deterministic output. It reads only WORD535.txt beside it;
no network, randomness, floats, external data, file writes or scientific
imports from other probes. It crosschecks four-coefficient polynomial and
five-coefficient cyclic contact arithmetic and conservation on every distinct
pair-map entry. Caching exact local maps is permitted; no whole-word,
checkpoint or endpoint oracle replaces any trajectory operation.

The finite inventory comprises the three local copying cases, every one of
the five marked-bank inputs and their inverses, blank/occupied-target and
non-involution boundaries as specified in code, diagonal/refused contact
controls, and the source nine-cycle. The main exhaustive audit traverses all
1000 full forward trajectories and all 1000 full literal inverses. These main
trajectories contain 403050000 contacts and 20000 swaps in total; auxiliary
local/copy/source audits are reported separately. All101-coordinate cycle,
loading and final endpoints are checked against closed formulas, as are
workbank recovery, the actual six-bank decoder and record injectivity.
Fixed word support and whole-state checkpoints certify untouched archives;
local contact certificates establish per-operation invariants. The executable
also fixes all additional checkpoint and local-audit tests before pinning.

Output fingerprints, serialized as specified by verify.py, are not known in
advance. A first completed Linux run supplies exact EXPECTED.txt. Normal
repository changed-verifier checks and two-architecture CI must reproduce the
same source/output bytes under the unchanged 600-second limit. Every required
architecture and aggregate job must pass. Timing is operational metadata,
not a printed scientific value or a gate threshold moved after execution.

## 6. Failure threshold, scope and proposed decision

Tolerance is zero. A missing case, changed word, incorrect complete endpoint,
loss of common preparation, wrong copy or inverse, failed workspace recovery,
changed protected archive, hidden state replacement, wrong resource/operation
count, arithmetic disagreement, invariant failure or decoder collision fires
the corresponding falsifier. No input may be removed. Reproduction requires
exit 0, empty stderr and byte-identical output. Nonzero/timeout is not a pass.

A successful run supports a NON-CANONICAL L1 candidate-C finite witness.
PROOF.md supplies candidate-T copying and arbitrary SPECIFIED FINITE horizon
arguments, requiring independent mathematical acceptance. The construction
uses 26+25k slots and account 68+74k for k>=1, with 2k fresh permanent banks;
it does not claim one fixed finite carrier works for unbounded history.
Capacity 5^b>=10^k is restricted to b five-symbol banks and distinguishable
ordered histories. Neither this capacity inequality nor the copier's length
is an attained global minimum.

No Canon/release change follows automatically. No retained-archive
regeneration, raw preparation, autonomous input selection, contact-only
loader, Collatz completion, physical time/energy, temperature or second-law
claim is made. The existing v108 finite theorem is not reopened.
