# Independent review of affine numerator synthesis and division recording

Status: NON-CANONICAL / L1. Candidate-T symbolic review and candidate-C finite
runtime evidence. No public Canon promotion or physical apparatus closure.

Reviewer: independent child session `/root/synthesis_breaker`.

## Verdict

The direct two-contact affine synthesis, the bounded fixed-word cascade and
the current-state reader satisfy the frozen contract. No preregistered
falsifier fired. The independent implementation agrees with the author's
complete q=3 current-state fingerprint and all reported counts.

This is a direct algebraic construction on the supplied coherent source
E_q(n), not an enumeration of individual n values. The same contact word
works for every supplied gain q and every positive n whose depth is at most
the declared D. The choice q=3 and the input loading interface remain
premises. The output is not a renewed E_q(m).

## Independence, pin and execution

The breaker read PREREG.md only, used the basis `(1,rho,rho^2,rho^3)`, and
froze before either author code or author output was opened. The source
uses cyclic length-five convolution for general multiplication, a separate
rho matrix for primitive contacts, and a Gram account expression. It reads
no source/reference leftovers to decode the output.

The common public source pin was
`0fde5621d9954ce86526eb1657e9afa1f1120fc6`. Frozen source hashes are:

| Source | SHA-256 |
|---|---|
| PREREG.md | fc85714e88ad9940ff31cdc6165fa541104543f0841c83f5b2ce1a7491574419 |
| verify.py | a0d55f34a913063e443f035affae4e99da5796f290e29077b317fe599f3ab679 |
| blindbreak.py | afee2a28b67f357c03ab9f23e38484d6fe52de6d59ed97a81c5f57e8d1b612e7 |
| BREAK-SCOPE.md | 0181746faa4ffae392dcbf5a7c173bbe999ef84b123da7b59c49fc20fe5e1a65 |

Only syntax compilation preceded the freeze. Public byte-identical readback
and explicit run authorization preceded the first scientific execution.
The breaker completed its own execution before reading verify.py or
EXPECTED.txt. Neither frozen implementation was changed after execution.

The exact independent command was

    python blindbreak.py --boundaries-out break-boundaries.json

Run environment: Linux, x86_64, Python 3.12.14, LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, TZ=UTC. The run started at
`2026-11-02T22:36:35.848412Z`, exited zero, and wrote zero stderr bytes.
Engineering elapsed time was 2.0311542300041765 seconds. This runtime is
metadata, not an exact scientific quantity.

The 993-byte stdout in BREAK-EXPECTED.txt has SHA-256
`5d42fc7742bc32e0cf2b7b21c166d136b26910efbe156ecac70283005e30d72a`.
Empty stderr has SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The neutral run metadata needed for replay is stated in this review.

## What the independent execution checked

| Exact audit | Cases |
|---|---:|
| q=3, odd n through 4095 | 2048 |
| q=1..9, odd n through 127 | 576 |
| Two occupied prior archives | 225 |
| Expected outside-depth saturation | 1 |
| Full native inverse replays | 2850 |

The independent lane checked both synthesis prefixes separately, complete
final-state formulas, actual accepted/refused contact prefixes, complete
sum and account, both labelled residues at every distinct primitive pair,
the output-only reader and arithmetic inverse, occupied archives, and full
native inverse restoration. Each native inverse uses reversed edges and
four contacts per edge. Every encountered distinct primitive pair also
passes C^5=id and its four-contact inverse. Matrix multiplication by rho
agrees with independent cyclic convolution on every encountered difference.

There were 213,750 primitive word applications and 48,772 distinct ordered
primitive pairs. These counts agree with the author. The 576 general-gain
cases include 256 depth-zero cases. The q=3 depth counts are

    1:1024, 2:512, 3:256, 4:128, 5:64, 6:32,
    7:16, 8:8, 9:4, 10:2, 11:1, 12:1.

Both compilers use the identical 15-edge word, with SHA-256
`eb37b5b2b6918571a3498b6d0badc9188d61f4511cf891dd90d17d4b7bdcc0db`.
Both complete canonical q=3 current-state fingerprints are
`e7aa8abf1acff43fcda83141b41ee238d854386d17e716d12c0d0a1a2c9e630e`.
The independent canonical payload is 449,224 bytes. No JSON regrouping,
basis ambiguity or stdout rewriting was needed in this comparison.
COMPARISON.json records the post-execution comparison.

The q=3,n=5461 witness returns DEPTH_LIMIT, not an arithmetic success.
All thirteen cascade records are nonzero, the active value remains even,
the full state accounts are retained, and the native inverse succeeds.

## Independent algebraic review

For the declared source

    a=2(q-1)un, b=2((q-1)u+2)n, c=2J,

the first difference a-b=-4n is even. Its first output is 2qun and its
second is 2[q-(q-2)rho]n. Both 2qun and c are even, so the second contact
is also admitted. It gives

    active=uJ(qn+1), leftover=q*u^2*n+J^2.

The separate source slot stays 2[q-(q-2)rho]n. These identities use only
J+u=2 and the literal contact formula. They do not require any finite table.
The supplied gain enters through E_q and is not selected by the contacts.

Both J and u are units modulo two. J is an integral unit with inverse
-rho-rho^3, whereas u has norm five and is not an integral unit. Thus the
active value has exactly the divisibility of qn+1. Each accepted fresh-zero
contact lowers that divisibility by one, multiplies the remaining active
value by J, and leaves a nonzero stored value. Every later fresh-zero
contact is refused once the active value is odd.

The formula after s successful cascade contacts is therefore

    active=u*J^(s+1)*(qn+1)/2^s,
    record_s=u^2*J^s*(qn+1)/2^s.

The fixed thirteen-port cascade gives exactly the positive prefix and zero
tail stated in the contract when v<=12. The present records supply the
depth; no hidden counter is needed by the mathematical reader. Normalizing
the active value by J^(-(v+1)) yields u*m, whose constant j coefficient is
m. This does not divide by u. It is an explicit depth-dependent reading,
not a Q-preserving contact operation that has physically renewed a port.

The source account is

    [40q(q-1)+32]*n^2+12.

It includes both n-dependent source ports and the common reference. For
q=3 this is 272n^2+12. The unchanged old archive values add their own
unchanged accounts. No account of the prior constant-energy binary code
is silently transferred to this different loading interface.

## Raw-source and fixed-family boundaries

One raw scalar n plus fixed common references cannot produce an unbounded
raw scalar 3n+1 under these conservative contacts. Positivity already gives
the necessary extra account 2(3n+1)^2-2n^2, unbounded with n.

There is a stronger finite-family statement independent of how large the
common references are. Fix one enabled/refused itinerary of a contact word.
It is a linear Q-isometry. For two distinct raw inputs n,n' on that same
itinerary, their input-state difference has account 2(n-n')^2. Two pure
output scalars 3n+1 and 3n'+1 would already require 18(n-n')^2 in one
output slot. Nonnegative account in the remaining difference slots makes
this impossible. Thus one itinerary can realize at most one such raw
input. A fixed L-contact word has at most 2^L itineraries; common fixed
permutations do not change the argument.

Labelled residues provide a separate obstruction. Contacts preserve each
fixed slot's coefficient sum modulo five. Fixed slot permutations only
permute the initial labels. A raw output slot inherited from a raw n slot
or from a common reference cannot have residue 3n+1 for every n. Allowing
state-dependent external port selection or a new residue-bearing input
chart changes these hypotheses and must be declared separately.

The present result pays for its escape explicitly: two n-dependent source
ports, a larger input-dependent account, a fixed residue-neutral numerator
code uJ, and a specified depth-dependent output reading. It does not prove
that this source chart can be loaded from a single raw n at no cost.

## Strict reload obstruction

The actual output retains n-dependent source/reference leftovers. For q=3,
slot 1 is 2(3-rho)n, whose constant coefficient is 6n. Thus the old n is
still present in a reported source leftover. Source cleaning is not part
of this result.

Suppose a proposed next step demands a fresh E_3(m), while all other final
accounts are nonnegative. If the complete initial system is E_3(n) plus
an additional account B, conservation requires

    272*(m^2-n^2)<=B.

Any old archive restored exactly cancels from the two sides. Retained new
records can only increase the final requirement. On n congruent to 3
modulo four, m=(3n+1)/2 and therefore

    B>=68*(5n^2+6n+1).

This is unbounded. Already 3->5 requires the source account to rise from
2460 to 6812, a gap of 4352 before accounting for new stored records.
Thus neither B=0 nor one common finite B can supply this exact reload for
the full growing family. This is a symbolic boundary, not an extra executed
test or a changed threshold. Another encoding or an explicitly funded
bounded source family requires its own complete resource contract.

## Remaining scope

The positive theorem is infinite only conditionally: n is unbounded, but
the supplied gain, loading interface and depth cap are fixed. The full
unbounded depth family cannot fit one fixed finite cascade. Saturation is
flagged rather than silently interpreted as a normalized odd part.

All executions use 15 primitive contacts irrespective of depth. The number
of accepted divisions is an internal activity count; its identification
with an elapsed physical interval needs a separate operational statement.
Similarly Q is a mathematical conserved account, not yet measured energy.

The current result constructs a one-pass numerator and depth record from
E_q(n). It does not provide source renewal, a repeated autonomous Collatz
map, a native-U bridge, choice of q=3, an occurrence law or convergence.
Two independent implementations here remain one x86_64 architecture;
ordinary repository CI does not replay this notes-only science or provide
the public two-architecture scientific gate.
