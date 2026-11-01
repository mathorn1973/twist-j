# Proposed Canon material: relative-contact preparation and renewal

**NON-CANONICAL / L1 / proposed text for external review.**
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

The status labels and registry rows below are proposals only. They do not
change Public Canon v106 or attest an independent mathematical review.

Proposed placement: section **2. Time, space, and the decoder**.
Proposed claim IDs: `RELATIVE-CONTACT-FOUR-SLOT-MINIMUM`,
`RELATIVE-CONTACT-RETAINED-BANK-CAPACITY`, and
`RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY`.
Proposed eventual status: `T`, conditional on acceptance of the explicit
mathematical proofs, finite computation and their stated scopes.
The external reviewer must decide that acceptance. The current working
session's source review is not independent scientific signoff.

## Proposed Canon section

### Relative-contact preparation, retained resources and a common-program boundary

All statements here are conditional L1 mathematics on a supplied contact
alphabet. Let

```text
O = Z[j],       1+j+j^2+j^3+j^4 = 0,
bar(j) = j^-1,  rho = j^2,       pi = 1-j.
```

For a marked pair of slots and k in {1,2,3,4}, define

```text
C^k(x,y) = ((x+y+rho^k(x-y))/2, (x+y-rho^k(x-y))/2)
             if x-y belongs to 2O,
           (x,y) otherwise.
```

This is a total map on O^2. In the admitted branch both halves are integral;
the new difference is rho^k(x-y), so admission is preserved. The inverse is
C^(5-k), including the refused branch. Whole-slot permutations are also
allowed. Slots, the contact, bank preparation, program and endpoint reading
are declared parts of this model.

For a complete state z, write

```text
S(z) = sum_i z_i,
h(z) = sum_i z_i bar(z_i),
q(x) = Tr_(Q(j)/Q)(x bar(x))/2,
E(z) = sum_i q(z_i).
```

The contact preserves S and h and therefore E. Indeed, with
s=(x+y)/2 and t=(x-y)/2, the pair norm is
2s bar(s)+2t bar(t); multiplication of t by rho^k leaves it unchanged.
The refused branch and permutations preserve the same accounts.

For x=sum_(i=0)^3 c_i j^i, with integer c_i,

```text
q(x) = (5 sum_i c_i^2 - (sum_i c_i)^2)/2
     >= (sum_i c_i^2)/2.
```

The numerator is even. The bound follows from
(sum_i c_i)^2 <= 4 sum_i c_i^2, and q(x)=0 iff x=0. Thus q is a
positive integer account, with finite bounded shells. It is not identified
here with a measured Hamiltonian, dissipated work or heat.

#### Four-slot known-input minima [proposed T]

The complete carrier has exactly 26 slots: 22 data slots and four auxiliary
slots. Initial data are

```text
d_in = (6,0^21).
```

The two target data states, each again occupying 22 slots, are

```text
d_plus = (3,3,3,3,0^18),
d_signed = (-3,3,3,3,0^18).
```

The initial and final auxiliary entries are arbitrary elements of O.
Every intermediate state includes all 26 slots. Final equality is complete
state equality up to the allowed whole-slot permutations, so no auxiliary
remainder or nonzero entry is discarded.

**RELATIVE-CONTACT-FOUR-SLOT-MINIMUM [proposed T].**
For this carrier, input, alphabet and equality, the least initial auxiliary
account is 27 for d_plus and 12 for d_signed. Both endpoints have the same
auxiliary account. This is a minimum of prepared auxiliary resources for
these particular known-input transitions, not a shortest-word theorem or
a common encoder for unknown inputs.

**Proof of the lower-bound reduction.** Reduction modulo pi identifies
O/(pi) with F_5. Put r(x)=sum_i c_i mod 5. On an admitted pair,

```text
x' - x = (rho^k-1)(x-y)/2 in pi O,
y' - y = -(x' - x).
```

Each slot therefore retains its residue under a contact; permutations move
residues between addresses. The complete residue histogram is invariant.
In residue order 0,1,2,3,4,

```text
H(d_in)     = (21,1,0,0,0),
H(d_plus)   = (18,0,0,4,0),
H(d_signed) = (18,0,1,3,0).
```

With exactly four auxiliary slots, a positive preparation must start with
four residues 3, while a signed preparation must start with residues
2,3,3,3. The final bank in either case has residues 0,0,0,1.
Modulo 5, the formula for q gives

```text
q(x) = 2 r(x)^2 mod 5.
```

Thus every source entry of residue 2 or 3 costs at least 3. Both auxiliary
accounts are at least 12. For the positive case the auxiliary total is
12 modulo 5, so the only totals below 27 are 12,17,22.

The positive data at both endpoints have h=36 and E=72. Their sums
are 6 and 12. Consequently an initial bank a and final bank b must satisfy

```text
S(b) = S(a)-6,       h(b) = h(a).
```

For auxiliary total at most 22 every constituent has q<=22. The inequality
above puts every coefficient in [-6,6]. Enumerating this entire box,
then every source multiset of four residue-3 entries and every target
multiset of three residue-0 entries and one residue-1 entry at each fixed
total, is therefore complete. No Galois representatives or missing
historical bank list are required.

One further invariant is the parity of the number of slots in each of
the sixteen classes of O/2O. An admitted contact removes two entries in
one common class and adds two entries in one common class; refusal and
permutation preserve these parities.

The exact finite certificate in
`probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/` gives:

| Auxiliary E | Initial banks | Final banks | Account-compatible pairs | Parity excluded | Closed target component | Closed source component | Unresolved |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 12 | 715 | 1830 | 0 | 0 | 0 | 0 | 0 |
| 17 | 5500 | 18880 | 1692 | 1584 | 108 | 0 | 0 |
| 22 | 31075 | 114985 | 70664 | 62988 | 7564 | 112 | 0 |

Here states are sorted multisets of all 26 entries, including zeros.
This quotient preserves reachability because all whole-slot permutations
are admitted. For each pair of distinct values in a common O/2O class,
the verifier includes every power C^k. Equal-value pairs and mismatched
classes are identities; reversing the orientation merely exchanges the
outputs. These are all nonidentity generator edges, and inverse edges
are included.

A component excludes the opposite endpoint only after its breadth-first
queue is exhausted. The exploration cap of 60 states is solely a stopping
rule: a 61st state returns UNKNOWN, never an exclusion. Every remaining
endpoint pair has a completely closed source or target component and
the opposite endpoint is absent. Thus the table excludes every cheaper
positive preparation. The full finite enumeration and exact replay, not
the displayed counts or their hashes alone, are the computational part of
the proof.

**Attainment.** Number slots 0 through 25, with initial 6 at slot 0,
zeros at slots 1 through 21, and the listed bank at slots 22 through 25.
A token (i,l,k) means C^k applied to those two labelled slots.
Each token below is admitted.

For the positive target use

```text
a_plus = (-1-j, 1+2j, 2+j^3, 2+j^2),
q entries = (3,8,8,8),

(1,0,3), (22,1,2), (1,2,3), (1,24,4),
(1,0,3), (3,0,1), (1,22,3), (3,1,4),
(0,22,1), (24,22,3), (22,23,3), (3,23,1),
(22,1,3), (1,3,1), (0,1,3), (0,25,4).
```

The final complete multiset equals d_plus together with

```text
b_plus = (1, -1+j, -2-2j-j^3, 2j+j^2+2j^3),
q entries = (2,5,10,10).
```

For the signed target set eta=1+j and use

```text
a_signed = (eta,-eta,-eta,-eta),
q entries = (3,3,3,3),

(0,1,3), (0,23,1), (0,1,1), (23,24,2),
(0,24,1), (22,24,2), (1,23,1), (0,25,3),
(0,1,2), (0,24,1), (23,25,3), (0,23,1),
(0,1,1), (22,23,4).
```

The final complete multiset equals d_signed together with

```text
b_signed = (-2eta,0,0,0),       E(b_signed)=12.
```

These are the 16-token positive witness and 14-token signed witness of the
pinned minimum probe. A final permutation places the target data and bank
at their designated addresses. Undo that permutation and apply the tokens
in reverse order with exponents 5-k to restore the exact original labelled
state. The verifier checks complete accounts after every token, full final
multiset equality and the labelled inverse before final rearrangement.
This establishes attainment and completes both minima.

Tokens count powers C^k. They are not all single applications of C or
C^-1, and no minimal length in either metric is claimed.

#### Retained outputs require changing auxiliary resources [proposed T]

**RELATIVE-CONTACT-RETAINED-BANK-CAPACITY [proposed T].**
The two preparations above cannot restore their initial bank while keeping
their prepared data unchanged and restoring every other resource to its
initial exact state. For N disjoint known-input loads of d_in and N retained
outputs of the stated signed or positive type, count every auxiliary slot
whose state may change, including spent banks and archives. Suppose all
operations belong to the same contact/permutation alphabet and no uncounted
external state exchanges residues. Then

```text
L_aux >= 4N,       E_aux(initial) >= 12N.
```

For the signed target these bounds are attained simultaneously by N disjoint
copies of the signed word, with all N inputs and sites prepared in advance.
For the positive target independent copies give E_aux(initial)<=27N with
4N auxiliary slots. No claim that 27N is the positive many-output minimum
is made.

**Proof.** In a positive preparation the initial bank histogram is
(0,0,0,4,0), and its final histogram is (3,1,0,0,0). For a signed preparation
the initial histogram is (0,0,1,3,0), with the same final histogram.
If final data stay fixed and every other resource returns exactly, total
histogram conservation would require the bank histograms to be equal,
which they are not.

For N loads the initial data contain no residue-2 or residue-3 entries.
The retained signed outputs contain N residue-2 and 3N residue-3 entries;
the positive outputs contain 4N residue-3 entries. Conservation therefore
requires the initial changing auxiliary supply to contain at least those
entries. Resources that return to their original state cancel from the
histogram equation. There must be at least 4N changing auxiliary slots.
Each required residue costs at least 3, proving E_aux>=12N. Disjoint
witness copies establish the stated upper bounds and signed equality.

The bank keeps its trace account while changing the residues needed for
another retained preparation. Inverting the whole word restores the bank
while undoing the output. Swapping in a fresh bank transfers the spent
state into another resource. Neither operation supplies clean bank renewal
under the retained-output contract. No energetic dissipation follows.

#### One fixed program preserves input residue distance [proposed T]

**RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY [proposed T].**
For any finite number of slots m, let F be one fixed finite word of the
declared marked contacts and whole-slot permutations on O^m. Its contact
admission may depend on the current input, as the defined law requires,
but its sequence of marked operations and permutations is fixed.
There is a single permutation sigma of the m residues, independent of
the input, such that for all z,w in O^m,

```text
r(F(z)) = P_sigma r(z),
r(F(z)-F(w)) = P_sigma r(z-w).
```

In particular the Hamming distance between the complete residue vectors of
two inputs is exactly preserved.

**Proof.** Each admitted or refused contact is the identity on the residue
vector at its marked addresses. Each whole-slot permutation acts by its
fixed permutation matrix. Composing them proves the first equation; taking
the difference proves the second and preserves its support cardinality.

If two source inputs are given the same initial bank, additional identical
auxiliary entries add zero coordinates to their residue difference.
Consequently no fixed word with that common bank can produce prescribed
data outputs whose residue difference already has more nonzero coordinates
than the complete initial difference. Allowing more unchanged common-bank
slots or a larger initial trace account cannot change this obstruction.
The conclusion is a necessary condition, not a classification of all
possible encoders. A program chosen separately for each input or a
state-dependent permutation controller has a different contract and
requires its own complete state and resource accounting.

These results do not compose the preparation words with a phase response
or occupied-record apparatus. They supply no autonomous controller, common
unknown-input instrument, native-U implementation, physical event, measured
energy scale or cross-layer lift. Those claims require their own compatible
carrier, interfaces and evidence.

## Proposed registry rows

The following is a proposed six-column TSV block only. Do not insert it
into the live registry before external review and the separate sealed fold.
The proposed T statuses have not been earned by this document.

```tsv
claim_id	status	scope	canon_section	evidence	falsifier
RELATIVE-CONTACT-FOUR-SLOT-MINIMUM	T	at L1 on O^26 with O=Z[j], rho=j^2, the declared total relative contact, arbitrary whole-slot permutations, initial data (6,0^21), exactly four arbitrary auxiliary slots and complete endpoint equality, the least initial auxiliary positive trace account is 27 for (3,3,3,3,0^18) and 12 for (-3,3,3,3,0^18); complete endpoint accounts and inverse witnesses attain both; no shortest length, common unknown-input encoder, native realization or physical energy interpretation is asserted	2. Time, space, and the decoder	probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/PROOF.md; probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/RESULT.md	fires on an admitted fully accounted positive four-slot word below 27, a signed word below 12, a failed displayed attainment or inverse, or a missing endpoint or generator invalidating the complete finite exclusion; changed carriers, alphabets and resource contracts are outside scope
RELATIVE-CONTACT-RETAINED-BANK-CAPACITY	T	at L1 in the same declared contact/permutation alphabet, the stated used banks cannot return to their initial states while prepared output data stay fixed and every other resource returns exactly; for N disjoint known-input loads and N retained signed or positive outputs, all changing auxiliary resources satisfy L_aux>=4N and E_aux(initial)>=12N; signed disjoint copies attain both, while positive copies give only the upper bound 27N; initial loads and sites are supplied and no clean or autonomous renewal is asserted	2. Time, space, and the decoder	inline; probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/PROOF.md	fires on a complete closed-resource bank reset preserving the prepared output, a fully accounted retained-output construction violating either lower bound, or failure of disjoint witness attainment; uncounted exchanges, undoing data and different output contracts do not satisfy the hypotheses
RELATIVE-CONTACT-FIXED-WORD-RESIDUE-BOUNDARY	T	at L1 for every fixed finite word of the declared marked relative contacts and whole-slot permutations on O^m, the complete residue vector modulo 1-j changes by one input-independent permutation, so pairwise residue Hamming distance is preserved; a common initial auxiliary bank of any size or trace account cannot realize prescribed outputs whose data residue distance exceeds the complete input distance; this is a necessary fixed-word condition, not an encoder classification or a theorem about state-dependent controllers	2. Time, space, and the decoder	inline; probes/P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1/PROOF.md	fires on an admitted fixed word and two complete inputs whose residue difference is not transported by the word's fixed permutation, or a common-bank realization of the stated distance-increasing target; input-specific programs and separately accounted adaptive controls change the scope
```

## Review inputs and provenance

This section is release-proposal metadata, not proposed normative Canon prose.

- Public authority inspected: main
  `a193e389fb1ddb0bdc89165b015c95a17eb1e425`, Public Canon v106.
- Parent contact proposal: PR #1833, head
  `d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0`.
- Resource-boundary proposal: PR #1847, head
  `12062dc44287bd3f97b4fdc0ca4a931a56a16bcd`.
- Complete finite minimum probe: PR #1849, head
  `c9af56ae7f9ede45da9ff709f8663aaa1ae95105`; prospective source pin
  `ed90ffd1826190b1fe04af0cf172d2886be21067`.
- Its original PREREG.md, PROOF.md and verify.py are unchanged between that
  pin and the inspected head.
- Exact verifier SHA-256:
  `461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f`.
- Exact EXPECTED.txt SHA-256:
  `95ee2135ecb491ab7f0702d603ea94013d00beb28e70668a3c418c0f21478178`,
  1755 bytes.
- The 14-token eta witness here is from PR #1849. PR #1847 describes that
  eta transition but its 15-token mini-verifier uses a different signed
  bank and endpoint. This proposal does not attribute the eta transition
  to that different 15-token replay.
- The book-specific U_B two-column example is omitted because its exact
  matrix is not defined in that proposal. The general residue-distance
  theorem is self-contained and does not need that example.
- The supplied later summary's shortest-word catalogues, 130/294 pair
  inventories and energy-27 completion counts are not prerequisites here
  and are not promoted. No claim is made to reproduce its missing source
  or fixture files.
- External review must address the finite bound, complete bank enumeration,
  all-slot quotient and generator set, closed-component certificates,
  witness transcriptions, residue proofs and precise resource scope.
  The reviewer should record the exact reviewed proposal revision.
