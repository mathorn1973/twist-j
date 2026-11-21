# Joint source and bank preparation preregistration

**NON-CANONICAL / L1. Prospective author-side finite audit.**

The analytical targets below were derived and exposed before execution.
This is not an independent acceptance test. It is a new standalone audit;
earlier verifiers, clock trajectories, field trajectories, and their sealed
outputs remain unchanged and are not imported or replayed.

## 1. Freeze and execution contract

Publicly pin verify_joint_preparation.py, this file, JOINT-CONSTRUCTION.md,
JOINT-OBSTRUCTION.md, and a source SHA-256 manifest before the first
scientific run. Record the immutable commit, source bytes and source hash.
Source inspection, hashing, and AST parsing are allowed before pin;
importing or executing the verifier is not.

After the pin and public readback, run python3 -I -B verify_joint_preparation.py
from this note directory. Use exact integers and the standard library only.
Each of x86_64 and aarch64 has a fixed 300-second wall limit and 1 GiB
memory limit. Both use identical source bytes and must exit zero, emit empty
stderr, and produce byte-identical scientific stdout.

An assertion, exception, resource limit, or architecture mismatch is a
failed gate to preserve and report. Do not alter this pin, increase its
budget, retune the preparation, or change exposed expected values after a
failure. The first successful run supplies the exact output artifact and
assertion count.

## 2. Carrier, operations, and explicit resources

Use O=Z[j], Phi_5(j)=0, rho=j^2, four integer coefficients,

\[
 Q(c)=(5\sum c_i^2-(\sum c_i)^2)/2,\qquad
 \epsilon(c)=\sum c_i\pmod5.
\]

The ordinary total contact C refuses odd coefficient differences and is
identity there. Otherwise C(s+t,s-t)=(s+rho*t,s-rho*t). The map epsilon is
reduction modulo lambda=1-j. It is invariant separately at each contacted
slot. Slot swaps preserve its multiset. No extension to a field carrier
is part of this audit.

The two contacted slots are checked for Q conservation, ring-sum
conservation and individual epsilon invariance at every audited contact.
All other slots are retained literally by the operation. Complete prepared
accounts, sums, spectator preservation and inverses are also checked.
Every refused contact is checked to be the literal identity.

The reference bank B(h) consists of two ordered copies of
(-h,-hj,-hj^2,-hj^3,-hj^4). Its account is 20 and its ring sum is zero.
It is a prepared resource. Neither this bank nor its coherence is generated
from one source pair and vacant slots.

The fixed reader D_0 acts successively on source slot p and the first bank
copy at k=0,...,4. Its five contacts have a twenty-contact literal inverse.
The second copy is retained as reference. Its output is the first index
where the two copies differ.

## 3. Main one-helper construction and declared family

The source is (p,q)=(j^r,-j^r); the helper is
(a,b)=(-j^s,+j^s). Define chronological words

\[
 A=C(p,q),\qquad K=C(p,a)C(q,b),
\]
\[
 P=A\,K\,A\,K^2\,A\,K^3\,A\,K^4\,A.
\]

P has 25 ordinary contacts. It acts on the prepared phase carrier as

\[
 (r,s)\longmapsto(s,2s-r).
\]

Its literal inverse has 100 contacts. Its compressed inverse has 40:
A^4, then K, A^4, K^2, A^4, K^3, A^4, K^4, A^4.
The compressed inverse is valid on the complete occupied carrier because
the two factors of K act on disjoint pairs and K^5=I.

The source aligns to the INITIAL helper and untouched bank phase s.
The used helper changes. The relative phase r-s is retained, not erased.
P^5=I is claimed here only on the prepared two-pair phase carrier.

For t=0,...,4 let B=C(a,b), k_t=3t mod5 represented in {0,...,4}, and

\[
 P_t=B^{k_t}P B^{5-k_t}.
\]

All five prescribed laws use the same initial source, helper and bank and
exactly 30 contact attempts. Their prepared action is

\[
 (r,s)\longmapsto(s+t,2s+t-r).
\]

The t=0 suffix is B^5, an explicit identity cycle. These are supplied
calendars and laws, not a selection by account, locality, or physical time.

Source plus used helper costs 8 on four occupied slots. Adding B(h) gives
account 28 on fourteen occupied slots, with total ring sum zero. The
twenty-two-slot interpretation with eight clock vacancies is analytical;
no native clock step or field controller is replayed in this audit.

## 4. Secondary four-helper construction

For the chronological helper phases (2,4,1,3), prepare four pairs
(-h j^k,+h j^k). Apply C(p,a_k), C(q,b_k) in that order for each helper.
There are eight contacts and a thirty-two-contact literal inverse.

This resets the source phase to h, with helper-hit counts for
delta=r-s=0,1,2,3,4 equal to (0,2,4,1,3). Changed helper suffixes retain
the old relative phase. Source plus helpers costs 20 on ten slots;
an additional untouched bank gives account 40 on twenty slots.
It is a lower contact-count alternative to the one-helper construction,
not a claimed optimum among all possible protocols.

## 5. Frozen finite inventory

1. Check the root relation, Q(1)=2, Q(lambda)=5, all main/secondary word
   lengths, and the five equal family lengths.
2. For all 25 source/helper phase pairs (r,s), check the exact main map,
   Q=8, zero sum, Q=2 at every output slot, unchanged relative phase,
   literal inverse, compressed inverse, and P^5=I on this prepared carrier.
   Append the same B(j^s), check that the bank is untouched by P and the
   complete account is 28. Apply D_0 and check reading zero, untouched
   second bank copy, and the unique match of the used negative helper
   against bank reference k=s-r mod5. Reverse the reader and main word
   literally and recover every initial slot.
   For the fixed input (r,s)=(2,0), the first source output is 1 and the
   second is j^3; this is not permanent locking to the initial frame.
   Separately test all 125 triples of source phase r, helper phase s and
   INDEPENDENT bank phase v. Check the reset source is j^s, the bank is
   untouched, complete Q=28 and sum zero, the reader reports s-v mod5,
   second-copy preservation and full reader/reset reversal. This tests
   the coherent donor-bank premise rather than assuming every bank aligns.
3. For all 125 triples (r,s,t), use the identical initial state for every
   t. Check the exact P_t phase map, Q=8, zero sum, retained relative
   phase and its 120-contact literal inverse. With the unchanged bank,
   check complete Q=28, D_0 reading t, untouched second bank copy,
   and the helper reference index s+t-r mod5. Reverse reader and law
   completely. The same reference bank distinguishes the actual laws.
4. For all 25 source/bank phases in the secondary construction, check
   output source +/-h, Q=20, zero sum, every slot Q=2, twice the declared
   helper-hit count in accepted ordinary contacts, changed helper count,
   distinct retained helper records at each fixed s, and complete inverse.
   Append the untouched bank, check Q=40 and D_0 reading zero. Compare
   negative helper slots with the untouched corresponding bank twins to
   retain the changed-helper record. Reverse reader and secondary word.
   At fixed (r,s)=(2,0), a second application returns the source phase
   to j^2; do not claim a persistent reset.
5. Enumerate all 5^5=3125 balanced unit configurations of one source and
   four independent helper phases. Use the SAME secondary word.
   Decode the resulting balanced unit phases; check 3125 distinct outputs,
   each complete inverse, and uniform output source counts
   (625,625,625,625,625). There are 625 source-phase-zero inputs and
   625 such outputs. Report their intersection as a computed output,
   with no preregistered target for that intersection.
   This finite permutation does not align independent helpers
   unconditionally or erase their phase information.
6. Form the 81 ring elements with coefficients in {-1,0,1}^4.
   For all 6561 ordered pairs, apply C five times, checking the contact
   invariants at each step and the exact fifth-power identity.
   This audit is confined to O.
7. Check the twelve-slot funded obstruction seed

   (1,-1,lambda,-lambda,lambda,-lambda,0,0,0,0,0,0).

   It has Q=24, sum zero and epsilon histogram (10,1,0,0,1), in residue
   order 0,1,2,3,4. For all 25 target source/bank phase pairs, check the
   twelve-slot target (j^r,-j^r,B(j^s)) has Q=24, sum zero, and histogram
   (0,1,0,0,11). The unequal histograms obstruct all words of these
   contacts and slot swaps. Four potential bank ports initially hold
   lambda funding; the example is not an entirely blank bank with
   uncounted energy.
8. For all 25 canonical phase preparations, for both main-plus-bank and
   secondary-plus-bank protocols, and for all ten scalars +/-j^k,
   check complete-state simultaneous covariance of reset and composed
   reset-plus-reader. Check the invariant reading zero and complete
   inverse of the rotated composed output. This rotates the complete
   marked preparation, not the source alone.
9. Use 32 fixed raw ten-slot states. Enumerate the 81 coefficient-box
   elements in itertools.product order; fixture number n has slot k
   equal to elements[(11n+7k+k^2) mod81], n=0,...,31, k=0,...,9.
   Check literal inverse of the main word, secondary word and each of
   the five family words, retaining unused slots. Also check the
   compressed main inverse. No phase-carrier hypothesis is imposed.
10. For all 25 source/helper phases, separately test the two whole-slot
    swaps (p,b), (q,a). They produce source phase s and helper phase r,
    with Q=8, zero sum and exact inverse. This is a distinct swap-based
    donor protocol, not a smaller ordinary-contact count or a free
    coherent donor preparation.

## 6. Deterministic stdout and claim limits

Record main rows (r,s,new source phase,new helper phase); independent
bank rows (r,s,v,reader index); family rows
(r,s,t,new source phase,new helper phase,reader index,helper-match index);
secondary rows (r,s,changed-helper count,changed-helper indices); and every
independent-input/output phase tuple in lexicographic input order.
Hash each complete record list as ASCII JSON using sort_keys=True,
separators=(",",":") and a single trailing LF, with SHA-256.

Scientific stdout contains status, the exact main map and relative-phase
qualification, contact/inverse counts, declared accounts, case counts and
record digests; the independent source marginal and alignment intersection;
the two residue histograms; covariance/raw/donor fixture counts; the
assertion count and PASS. There are no timings, hostnames, paths, random
values, or floating point values in scientific stdout.

The analytic residue obstruction and general bijection statements are not
proved by finite examples alone; their proofs are in the pinned companion
notes. The finite audit checks the stated instances and exact protocols.
A coherent donor/helper and reference bank are initial resources.
Old information is retained, and both main and secondary repeated words
are reversible, not attractors. No creation of bank residues from one
pair and blanks, unrestricted cloning, physical phase selection, preferred
P_t, shared field-action controller, or electromagnetic coupling is claimed.
