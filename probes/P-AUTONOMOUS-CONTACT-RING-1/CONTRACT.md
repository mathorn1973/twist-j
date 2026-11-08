# Exact contract

NON-CANONICAL / L1 / frozen before either implementation or execution.
All indices are zero-based. Integer and rational arithmetic is exact.

## Arithmetic, accounts and maps

A canonical cell is the four-tuple (c0,c1,c2,c3) representing
c0+c1*j+c2*j^2+c3*j^3, reduced by 1+j+j^2+j^3+j^4=0.
The contact equation and matchings are exactly those in PREREG.md.
Accepted means all four coefficients of x-y are even; an accepted contact
on equal cells may leave both cells unchanged. Rejected and unchanged are
therefore different predicates.

    trace(c) = 4*c0-c1-c2-c3
    residue(c) = (c0+c1+c2+c3) mod 5
    q(c) = (5*sum(ci*ci)-(sum(ci))^2)/2
    S(z) = sum(z_i)
    h(z) = sum(z_i*conjugate(z_i))
    E(z) = sum(q(z_i)) = trace(h(z))/2

Conjugation sends j to j^4. Each division by two in an admitted contact and
each account division must be exact. The inverse contact is the same formula
with rho replaced by rho^4; its rejected branch is unchanged. Compare this
inverse with four forward contacts on the exhaustive pair inventory.

## Nine states and transition tables

For even N>=8, a nonzero odd integer a, and an even translation s, all
addresses below are taken modulo N after adding s. Put
A_k=(1+rho^k)*a, D_k=(1-rho^k)*a for k=1,2,3,4.

State 0, B, has z_1=2a, z_5=-2a and all other cells zero.
States 1,2,3,4, named L_k, have

    (z_0,z_1,z_4,z_5) = (D_k,A_k,-D_k,-A_k).

States 5,6,7,8, named R_k with state number 4+k, have

    (z_1,z_2,z_5,z_6) = (A_k,D_k,-A_k,-D_k).

Every unlisted cell is literally zero. The transition targets, ordered by
source state number 0..8, are

    bit 0: [1,2,3,4,0,5,6,7,8]
    bit 1: [5,1,2,3,4,6,7,8,0].

All nine states are distinct. On this class S=0, h=(8*a*a,0,0,0), E=16*a*a.
The four fixed receiver addresses in order are (s+0,s+2,s+4,s+6) modulo N.
Their decoded outputs are (BLANK,BLANK,BLANK,BLANK) in state 0,
(VALUE(a),BLANK,VALUE(-a),BLANK) in each L state, and
(BLANK,VALUE(a),BLANK,VALUE(-a)) in each R state. Reading the sum of the
first two receiver cells gives BLANK in state 0 and VALUE(a) otherwise.
Only the original source addresses s+1 and s+5 may depend on a initially.

The cell reader is total: ["BLANK"] for the zero cell, otherwise
["VALUE", numerator, denominator] for trace(cell)/5 in reduced form with
positive denominator. This tagged JSON-array representation is normative.

## Finite audits, order and hash rows

Each digest below starts from a fresh SHA-256 object. Feed one UTF-8 line per
row in the stated order: json.dumps(row, sort_keys=True, separators=(",",":"),
ensure_ascii=True) followed by one LF. Tuples serialize as JSON arrays;
integers serialize in ordinary decimal notation. No spaces or extra lines.

### Pairs

Use Python lexicographic product order for the 81 canonical four-tuples in
{-1,0,1}^4, with the coordinate alphabet ordered -1,0,1. For each x in that
order, then each y, let (u,v)=C(x,y). The 6561 hash rows are

    [x,y,int(accepted),u,v].

Check sum, full h, E, both labelled residues, C^5=identity, inverse(C(x,y))
=(x,y), and C^4(C(x,y))=(x,y). Check direct q against trace(z*conjugate(z))/2,
q>=0 and 2*q>=sum(ci*ci) for each cell encountered. Accepted and rejected
parity classes must remain invariant under the contact.

### Four-cell matchings

Freeze the ordered cell alphabet

    [0,1,-1,j,-j,j^2,-j^2,j^3,-j^3].

Take its fourth Cartesian power in lexicographic alphabet-index order. For
each complete state z, process bit 0 and then bit 1. The 13122 hash rows are

    [z,bit,K_bit(z)].

Check complete-state S,h,E, every labelled residue and exact one-step inverse.
Contacts are evaluated from the old array and assigned to disjoint targets.

### Nine-state class

Loop in this exact order: N in (8,10,12); s in range(0,N,2); a in
range(-15,16,2); state number in range(9); bit in (0,1). Construct states from
the formulas above, independently of the implementation of K_bit. Require
K_bit(z) to equal the formula state indicated by the frozen table. Check
the nine states are distinct, their complete accounts and fixed readers,
all conservation laws, and exact inverse. The 4320 hash rows are

    [N,s,a,state_number,bit,z,K_bit(z)].

### Continuing primary histories

Loop over a in (-1,1). Start at n=3 in the N=8, s=0 state B. Visit every
boundary n in range(3,260), including both endpoints. The expected abstract
state follows the frozen transition tables using b_n, starting at state 0.
At each boundary compare all eight cells with that formula state; check
accounts, residues, the four fixed receivers and their fixed sum reading.
Hash the 514 rows

    [a,n,state_number,z,[reader(z_0),reader(z_2),reader(z_4),reader(z_6)]].

After hashing boundary 259 do not take another forward step. Recover all
256 previous steps in reverse order using the previous clock bit, compare
every recovered array with its stored complete forward boundary and finish
at exactly n=3,B. Explicitly assert z_2 and z_6 are zero at n=3 and n=10,
and read VALUE(a),VALUE(-a) respectively at each n=4..9. Assert the complete
ring at n=10 equals B, without asserting equality of the full clock state.

### Controls

First control: N=8, n=3, all cells zero. Apply the continuing law for 256
ticks, checking that every boundary remains zero. Hash one row

    ["zero",initial_array,final_array].

Second control: N=8, s=0, a=2. Apply bit 1 once and bit 0 once, in that
order. After the second step require z_3=(1-rho)^2, nonzero, and require
the array to differ from each of the nine formula states for a=2. This is
an intended negative control on extending the odd-a theorem to even a,
not a failed prediction of the admitted family. Check conservation and
inverse for these two transitions. Hash the second row

    ["even",initial_array,after_bit_1,after_bit_0].

### Clock

Compute b_n for n=1..8192 from valuation parity; compare each bit with
parity(popcount(n-1)) XOR parity(popcount(n)). Hash the ASCII 8192-bit word
and one LF, without JSON. This audit word is not stored or used as a contact
program by the evolution. For each length ell=1..64, count all distinct
length-ell substrings in this exact prefix and require the count <=4*ell.
These finite counts are witnesses; the infinite factor bound is a proof
obligation, not inferred from their stability.

## Exact report interface

Each implementation's audit() returns precisely this dictionary, replacing
angle-bracketed descriptions by the computed values:

    {
      "probe": "P-AUTONOMOUS-CONTACT-RING-1",
      "pair_cases": 6561,
      "pair_sha256": "<pair digest>",
      "ring_cases": 13122,
      "ring_sha256": "<four-cell digest>",
      "orbit_cases": 4320,
      "orbit_sha256": "<nine-state digest>",
      "trajectory_boundaries": 514,
      "trajectory_sha256": "<primary-history digest>",
      "control_cases": 2,
      "control_sha256": "<control digest>",
      "even_control_z3": [<four canonical coefficients>],
      "clock_length": 8192,
      "clock_sha256": "<ASCII clock digest>",
      "factor_counts": [<64 integer counts, lengths 1..64>],
      "orbit_transition": [[1,2,3,4,0,5,6,7,8],[5,1,2,3,4,6,7,8,0]],
      "primary_read_window": [4,5,6,7,8,9],
      "erased_boundary": 10,
      "primary_account": 16,
      "native_bit_match": true
    }

The primary verifier compares its report for exact equality with the
independent breaker's report, then emits exactly

    {"independent_match":true,"report":<report>,"status":"PASS"}

using the same sorted-key compact JSON convention and one LF. The breaker
entry point emits its report alone with that convention. Assertion failures
are never caught and converted into a success marker.
