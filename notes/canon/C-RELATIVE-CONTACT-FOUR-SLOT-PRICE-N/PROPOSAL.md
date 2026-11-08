# Four-slot price of one known-input relative-contact preparation

**Candidate:** C-RELATIVE-CONTACT-FOUR-SLOT-PRICE-N  
**Owner / reservation:** A. M. Thorn, #1846  
**Status:** NON-CANONICAL / L1 / candidate-T for the conditional mathematical assertions; local C for explicitly replayed words; H for any physical reading.  
**Licence:** SPDX-License-Identifier: Apache-2.0.

This is a **new supplied carrier and contact-application problem**, not a theorem that original native U implements the contact. The contact itself is from open NON-CANONICAL #1833, not a public Canon rule. The clock, slot frame, target word, initial funded bank, endpoint position, and target-state interpretation are extra premises.

## 1. Frozen carrier and exact law

Let O=Z[j], Phi_5(j)=0, rho=j^2, pi=1-j, and bar(j)=j^-1.
We use 26 labelled slots: 22 data and 4 auxiliary. The initial data are
(6e_1,0^16), i.e. one 6 and 21 zero entries. The auxiliary source a_0 is
prepared and is not free. Whole-slot permutations may follow contacts.

On a marked pair (x,y), the accepted C_rho^k (1<=k<=4) is

    s=(x+y)/2, t=(x-y)/2,
    (x,y) -> (s+rho^k t,s-rho^k t)                         (1)

when x-y is in 2O. The complete map is identity on the rejected complement.
Equation (1), the off-domain choice and the physically marked slots are
supplied premises inherited from #1833. Each accepted operation is exact and
reversible. All claimed words in this note use the accepted branch only.

Define

    h(z)=sum_i z_i bar(z_i) in Z[phi],
    q(z)=Tr_K/Q(z bar(z))/2 in Z_>=0,
    E(z)=sum_i q(z_i).                                      (2)

For z=sum_(k=0)^3 c_k j^k,

    q(z)=[5 sum c_k^2-(sum c_k)^2]/2.                        (3)

An accepted contact preserves the O-valued sum and h before taking traces;
all permutations preserve these accounts. E is a **positive trace account**,
not a measured Hamiltonian or a physical energy scale.

## 2. Two constructive one-shot witnesses [local C; candidate-T]

### 2.1 Signed: E_aux = 12

Put eta=1+j, and prepare the source bank

    a_0=(eta,-eta,-eta,-eta).                               (4)

A known-input word consisting of 15 power contacts C^k produces the full
multiset transition

    {6,0^21} + {eta,-eta,-eta,-eta}
      -> {-3,3,3,3,0^18} + {-2eta,0,0,0}.                 (5)

The single word is embedded as executable input data in verify.py; the
verified target uses 22 data slots plus four bank slots. A separate earlier
word uses 20 unit C^+/-1 contacts plus five final slot exchanges and also
reaches the signed target. A length in power contacts is not comparable to
a length in unit contacts.

The initial and final bank E each equal 12. They are **not the same bank
state**. The total O-valued sum, h, E and residue histogram are conserved.

### 2.2 Positive: E_aux = 27

Prepare

    a_0=(-1-j, 1+2j, 2+j^3, 2+j^2).                        (6)

A known-input word of 16 power contacts gives

    {6,0^21} + a_0
      -> {3,3,3,3,0^18}
         + (1,-1+j,-2-2j-j^3,2j+j^2+2j^3).                (7)

The initial source energies are (3,8,8,8), total 27. The last step has
the exact local form

    C_rho^4(2-rho,2+rho)=(1,3).                            (8)

All sixteen steps are replayed by verify.py with exact integer arithmetic
and the entire final auxiliary is checked. The public note does not assert
that sixteen is shortest or that the source bank can be prepared for free.

### 2.3 What the replay proves, and what it does not

The two displayed transitions are **existence witnesses on one prepared
input**. The published verify.py checks every power-contact against the
current multiset, exact admission, total accounts and the full final multiset.
It does not check any of the historical exhaustive enumeration counts.

For the signed target the lower bound four source slots is elementary:
modulo pi, rho=1, so a contact preserves the residue at every physical
slot (and a whole-slot permutation only moves it). The input data contribute
one residue 1 and zero elsewhere; the signed target data require the four
residues (2,3,3,3). These four nonzero residues must be supplied in the bank.
For positive target data, they require four residues 3.

To bound source E, q(z)=0 only at z=0; its smallest nonzero value is 2,
attained precisely at z=+/-j^r, which have residue +/-1 mod pi. Therefore
an amplitude of residue 2 or 3 has q(z)>=3, and any four-slot bank for
either target has

    E_aux >= 4*3 = 12.                                     (9)

Equation (5) attains this bound for the **signed** case. For the positive
case the 2026-11-01 author note reports an exhaustive account-and-component
exclusion of candidate energies 12, 17 and 22, while (7) reaches 27. The
sharp **positive minimum 27 remains a retrospective candidate theorem**
until that exhaustive evidence is published in full and independently
reviewed. The current small verifier proves only the **27 upper bound**.
Do not substitute a 29/29 author-reported summary for the missing original
verifier, source list and words JSON.

## 3. Invariants and exact negative results [candidate-T]

### 3.1 Every slot retains its pi residue between permutations

On the admitted branch the output satisfies

    x'-x=(rho^k-1)(x-y)/2 in (1-j)O,
    y'-y=-(rho^k-1)(x-y)/2.                                 (10)

On the refused branch the contact is identity. Thus a fixed word of
contacts and whole-slot permutations induces on the 26-position residue
vector modulo pi **one permutation fixed by the word**, independent of
which contacts accepted:

    residue(F(z))=P_sigma residue(z).                        (11)

For any two inputs under the same word,

    residue(F(z)-F(w))=P_sigma residue(z-w).                  (12)

This is not a statement that physical slot addresses are fixed under
permutations. Only the residue multiset is absolutely invariant.

### 3.2 The mod-2 class-parity invariant

In an accepted contact x-y belongs to 2O. Hence x and y have the same
class in O/2O=F_16. The outputs also have the same class (their difference
is rho^k(x-y)). Therefore both inputs from one F_16 class are replaced
by two outputs from one (possibly different) class. For each r in F_16,

    epsilon_r(z)=#{i:z_i mod 2=r} mod 2                     (13)

is invariant under each contact and every slot permutation. This gives
sixteen exact parity constraints. They do not classify contact-connected
components by themselves. An author-reported separate mod-4 additive
classification is not promoted by this note.

### 3.3 No clean self-reset while retaining the changed data

Suppose the word completes (5) or (7), we keep the prepared output unchanged,
and an additional program restores a_0 from a_E while all other sources and
archives return to their original exact states. Then total pi-residue
histogram conservation implies

    H(a_0)=H(a_E).                                          (14)

This fails in both witnesses. Thus **clean auxiliary restoration with
retained final data and unchanged other resources is impossible** for these
closed-resource conditions. Running the inverse word restores the bank only
while undoing the prepared data, which is allowed and does not contradict
the no-go.

An extra changing bank can exchange its ready copy with a_E, but it is
spent as a ready supply and must itself be accounted for. No energetic
dissipation has been derived.

### 3.4 Fixed-program two-input boundary

A different target demands that the *same* word with the *same* initial
bank handle input 6e_1 and 6e_2 and yield the corresponding six-coordinate
data columns 6U_Be_1 and 6U_Be_2 of the original book's fixed matrix U_B.

The source-residue difference has two nonzero positions, namely 1 and -1.
The target data difference is

    6U_B(e_1-e_2)=(3,0,6,3,-3,-3)
                 =(3,0,1,3,2,2) mod 5,                   (15)

which has **five** nonzero positions already in the data. Equation (12)
forbids any fixed-word realization with the same initial bank, regardless
of the number of additional source slots or their funded trace account.

This is a no-go for the **specified target and gate alphabet**, not for
every possible physical or quantum reading, not for a target-dependent
program, and not for a newly prepared source at each input.

## 4. Multi-output capacity [candidate-T, typed scope]

For N *retained* known-input outputs, consider all changing auxiliary
slots, including spent banks and any archives. At fixed total residue
histogram, the N signed targets require N copies of residues (2,3,3,3);
the N positive targets require 4N copies of residue 3. These residues
are absent from each original known-input data load. Consequently the
initial total auxiliary supply needs at least 4N such nonzero positions:

    L_aux >= 4N, E_aux >= 12N.                             (16)

For the signed case, N disjoint copies of the exhibited one-shot
construction attain both (L_aux,E_aux)=(4N,12N), when the N known
inputs and sites are prepared in advance. A *ready bank remaining
untouched after N retained outputs*, indefinite autonomous use, or a
single shared input-independent loader would be different contracts.

For the positive case, N copies of the exhibited word give E_aux=27N,
but (16) does not prove that 27N is the global N-shot minimum.

## 5. Status and cross-layer exclusions

- CONDITIONAL MATHEMATICS: exact contact law, one-shot transition words,
  permutation-of-residues invariant, F_16 class parities, and a scoped
  closed-source reset no-go.
- RETROSPECTIVE AUTHOR CENSUS: energy-17/22 exhaustive counts, all 130
  mixed pairs with words, 294 positive words, and 245 unsearched
  positive classes. These are not reproduced by the attached mini-verifier.
- OPEN: unrestricted multi-input preparation, source-independent selector,
  initial loading and renewal of an occupied archive, native U realization,
  L1-L5/L6 readout and physical occurrence.

The exact contact itself is openly marked as an added **L1** mechanism
in #1833. No logical step here derives it solely from J. Neither the
amplitude port nor q has been identified with a physical detector or
Hamiltonian. No Canon text, public registry row, release or tag is modified.

## 6. Falsification and promotion gates

First falsifiers: a failed exact word step, any missing pair, any violation
of (1)/(2), or a full residue-bank reset counterexample with retained data
and unchanged external resources. The asserted sharp positive minimum 27
must be downgraded on any cheaper admitted **fully accounted** word. A
verified match of the entire declared 12/17/22 enumeration is required for
its computation-grade closure.

Future formal-public test must be new and prospectively pinned under
\`probes/P-...\` with PREREG and verifier before execution. It must freeze
the accepted alphabet, output equality, bank funding, token-length
convention, and the exhaustive finite source domain. The public pinned
two-architecture jobs and independent mathematical breaker apply as in
POLICY.md. The same complete apparatus-family context and separate
declared cross-layer gate are needed before making any physical reading
claim. This notes candidate is not such a gate.

## Evidence pointers

- Authority: Public Canon v106, main a193e389fb1ddb0bdc89165b015c95a17eb1e425, status and source pin per STATUS.md.
- Parent contact: #1832 / draft PR #1833, pinned head d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0.
- Independent neighboring notes: #1844 / draft PR #1845, a full Gram record and occupied two-use archive; it is **not** reused here as proof of a preparation.
- User-supplied 2026-11-01 Průzkum 4 note, source SHA-256 b8df2422572f4c4a1aa6a0905dc4512857823aae495b2d7201ea767b52db8781, 16001 bytes.
- The historical \`verify_katedrala_pruzkum4_2026-11-01.py\` (declared 29/29 on one architecture) and \`words_katedrala_2026-11-01.json\` are **not supplied** as accessible payload in this session.
