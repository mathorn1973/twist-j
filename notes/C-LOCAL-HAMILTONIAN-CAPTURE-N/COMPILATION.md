# Exact compilation into a finite nearest-neighbour qubit circuit

**NON-CANONICAL, L1, conditional candidate-T.**
This is an analytical construction under [claim #1749](https://github.com/mathorn1973/twist-j/issues/1749).
No scientific program, synthesis table or numerical simulation was executed.
The algorithm below defines a finite coefficient table; its possibly enormous
entries and gate list have not been generated.

## 1. Fixed finite target and observable checkpoints

The source/filter input is [PR #1746 at 01acc42b][filter]. Its clock and
battery extension is [PR #1748 at ecb34609][extension], in particular its
[CLOCK.md][clock] and [ENERGY.md][energy]. Those unmerged candidate premises
retain their original status. Public authority is main/canon-v105
`892a0b11089d34e241e1eb76d2c03247022d18e6`.

Use precisely the finite coordinate completion and full all-state laws of
those inputs. The following notation makes the carrier size explicit:

    D = 327680,       B_work = 2D+3,
    T = H+1,         s = 99,
    L_prog = T+5D+8, M = L_prog+H+1,
    R_box = |s|+T+D+H+3,       N_box = 2R_box+1,
    d_data = 12 N_box^3 26^2 5^(D+1) 2^B_work.

The finite coordinate representatives are [-R_box,R_box]. The strict unused
margin in CLOCK.md identifies the original infinite target word and this
finite word on the stated initialized source throughout L_prog+H ticks.
This comparison includes every rejected history. It does not identify their
infinite-time spectra or prescribe native particle positions for this compiler.

On the full clock/data carrier define the selected integer account

    N_S = c+(R-s)^2+r^2+(x-s)^2+I_pulse
          +sum_pentits [a!=0]+sum_bits b.

An explicit upper bound is

    q_max = (M-1)+2(R_box+|s|)^2+R_box^2+1+(D+1)+B_work.

Fix an integer Q>=q_max, let L_bat=Q 5^22, and use the battery with
L_bat+2Q basis levels. Its full energy-sector unitary is Gamma(U_clock),
including identity on the incomplete edge sectors, as defined in ENERGY.md.
Write this unitary as U_funded. The complete target dimension is

    d = M d_data (L_bat+2Q).                                  (C1)

The hardwired word is not an additional program register in this dimension.
All source-loader, filter, predicate, occupied-memory, clock and battery
factors are counted. A passive reference is arbitrary and external to d.

Fix h in {0,...,H} and put t_ticks=L_prog+h. The default h=0 endpoint is the
completed instrument before release. A separate choice h>0 includes that
many native target release steps. The bound-band leakage threshold is
inherited only at h=0; later contact need not preserve binding. The release
family retains the finite memory guarantee at its selected endpoints.
Rather than hide
this chronology in one unexplained matrix, compile the explicit word

    P_B, U_funded, U_funded, ..., U_funded                     (C2)

with t_ticks funded ticks, a total of nu=1+L_prog+h named macros. Each member is
synthesized separately, so every original tick boundary remains an identifiable
clean-workspace circuit checkpoint. These are circuit-prefix checkpoints,
not deterministic intermediate times of an autonomous history Hamiltonian.
The prepared input has the prescribed source/coin basis state, clock and
work registers zero, arbitrary logical labels and old memory, and battery
basis level zero. The source loader itself is already in U_clock's schedule.

## 2. A finite explicit battery-ready prefix

Let the desired battery vector be

    b = (1/sqrt(L_bat)) sum_(n=Q)^(Q+L_bat-1) |n>.

Let S_B exchange battery basis levels 0 and Q, fixing all other levels.
For j=1,...,L_bat-1, put a_j=Q+j-1, b_j=Q+j and

    c_j = 1/sqrt(L_bat-j+1),
    s_j = sqrt((L_bat-j)/(L_bat-j+1)).

Define a total two-level rotation R_j by

    R_j |a_j> = c_j |a_j>+s_j |b_j>,
    R_j |b_j> = -s_j |a_j>+c_j |b_j>,

and identity on every other battery level. The ready prefix is exactly

    P_b = R_(L_bat-1)...R_1 S_B,
    P_B = I_(clock,data) tensor P_b.                          (C3)

After j rotations the first j levels beginning at Q have amplitude
1/sqrt(L_bat), and the remaining amplitude is
sqrt((L_bat-j)/L_bat) at Q+j. Induction using the displayed c_j,s_j proves
P_b|0>=b. The word defines a unique full-state algebraic unitary, including
unused battery inputs; it is not merely a state-preparation prescription.

This supplies an explicit preparation prefix from a basis state. Its
compilation, storage and time are counted in (C2), not omitted as a free
initial state. Although it is one named macro, it has L_bat defined factors;
the generic compilation bound below depends on d>=L_bat and does not treat
this matrix as a single physical site or elementary gate. The circuit starts
with basis-zero storage, not a claim of a physically cost-free ready state.

In particular P_B does not conserve the old account epsilon(N_S+n): the
battery's mean energy rises from zero to epsilon[Q+(L_bat-1)/2]. Thus including
(C3) does not prove preparation under that same old conserved energy law.
A Hamiltonian realization must state its own complete initial state and
energy account. The compiler must not relabel this increase as zero work.

Every matrix in (C2) has algebraic complex entries. The source uses rational
numbers, roots of unity and positive square roots; the clock is a finite
controlled permutation of those operations; the energy sectors use integer
diagonal projectors and copies of those matrices; and (C3) is algebraic.
This is an exact finite algebraic description, without rounded angles.

## 3. Deterministic two-level decomposition

Let A be any one of the d-dimensional unitaries in (C2). The procedure below
also applies to the full total-state matrix, including inputs outside the
initialized source or ready clock domain. Choose a fixed ordering of the
mixed-radix basis. For columns c=0,...,d-2, successively eliminate entries
in rows j=d-1,...,c+1 by a two-row unitary on rows j-1,j.

For the current entries a=A_(j-1,c), b=A_(j,c), skip the step when both are
zero. Otherwise let r=sqrt(|a|^2+|b|^2)>0 and multiply those rows by

    Z(a,b) = [[conjugate(a)/r, conjugate(b)/r],
              [-b/r,                    a/r]].               (C4)

Direct multiplication gives Z(a,b)(a,b)^T=(r,0)^T and Z*Z=I. Previously
eliminated columns stay zero because both affected rows are below their
pivots. The final matrix is upper triangular and unitary, hence diagonal:
its first column has only one unit-modulus entry, orthogonality forces the
rest of its first row to vanish, and induction finishes the claim.

Consequently A is a product of at most d(d-1)/2 inverse two-level rotations
and d one-coordinate phase gates. Its product order is the reverse of the
elimination order, with the final diagonal included. All coefficients remain
algebraic. Choosing the positive real root in (C4), the fixed row order and
skipping exactly the zero pairs makes the procedure deterministic. Exact
zero comparison and arithmetic of algebraic numbers define it; no floating
point search or numerical tolerance is needed for this existence proof.

The total number of these factors is at most d^2. A one-coordinate phase
can be implemented by the controlled gate construction below. Inverses of
intermediate rotations are permitted here. This is not a query algorithm
restricted to calls of the original W or T_R.

## 4. Binary encoding, Gray paths and clean controls

Encode each target register separately in binary. The internal object coin
and carrier arrangement together have twelve values. The two logical labels
have separate 26-value registers. A sufficient number of data-code qubits is

    n = ceil(log_2 12) + 3 ceil(log_2 N_box)
        + 2 ceil(log_2 26) + 3(D+1) + B_work
        + ceil(log_2 M) + ceil(log_2(L_bat+2Q)).              (C4a)

In particular n>=2. The d valid codewords form a specified tensor-product
subset C of {0,1}^n, generally not an interval of integer codes. Fix their
order by the original mixed-radix basis order. Extend every target matrix
by identity on the orthogonal complement of span(C), including invalid
codes in any individual register. QR in Section 3 acts on the d valid
basis vectors; the following Gray construction uses their actual n-bit
strings and therefore does not require a contiguous encoding.

Within each known register, assign code zero to its specified ready basis
state, and enumerate the remaining basis states in fixed lexicographic
order. Thus R=s, r=0, x=s, the source coin/standing-token configuration,
every auxiliary zero, the target clock c=0 and battery level zero all have
zero codes. The two unknown logical labels keep their own five-qubit blocks,
with valid values 0,...,25 in each. Arbitrary logical/reference Xi occupies
these ten qubits on the 676-dimensional valid subspace; every other data-code
qubit and every clean work qubit starts at zero. An initializer must exclude
these ten unknown qubits from its blank-register penalty. Unused label codes
26,...,31 have no source-family promise. The encoded battery and target
clock remain separate factors. Any additional local Hamiltonian clock is
separately counted and initialized, for example in its zero domain wall.

For a two-level rotation on distinct strings x,y, let
x=g_0,g_1,...,g_h=y be the Gray path obtained by flipping their differing
bits in increasing position order. Its length satisfies 1<=h<=n. Adjacent
path strings differ in one bit. Transpositions along g_h,...,g_1 move y to
g_1 while fixing x=g_0. A rotation on the pair g_0,g_1, followed by the
inverse transpositions, therefore realizes the desired two-level rotation
on x,y and is identity on every other basis string. This uses at most
2(h-1)+1<=2n-1 multi-controlled single-qubit gates.

A transposition of two strings differing in one bit is an X on that bit
controlled on the other n-1 matching bit values. The central rotation is
similarly one single-qubit unitary controlled on those n-1 values. Negative
controls are converted to positive ones by conjugating their bits with X.
A phase on exactly one binary string is obtained by the same construction,
using a controlled diagonal single-qubit unitary with the other target-bit
value assigned phase one.

For m=n-1 positive controls, compute their conjunction into at most m-1=n-2
clean ancillas using an AND ladder of Toffoli gates. Apply one controlled
single-qubit unitary from the last conjunction bit to the data target, then
reverse the entire AND ladder. For m=1 the ordinary controlled gate suffices.
Every control and work qubit is restored, for arbitrary data superpositions
and arbitrary passive reference correlations.

A Toffoli has a five two-qubit-gate realization: with controls a,b and target
t, apply controlled-S from b to t, CNOT(a,b), controlled-S* from b to t,
CNOT(a,b), and controlled-S from a to t, where

    S = (I+X)/2 + i(I-X)/2,       S^2=X.

For the four basis values of a,b, the net power of S is respectively 0,0,0,2.
The controls are restored. This proves the construction directly, including
its phases; all matrices used are algebraic. General controlled single-qubit
unitaries are allowed elementary two-qubit matrices in this finite catalogue.
No claim of exact compilation into one fixed discrete universal gate set is
made. That different demand could require approximation.

Counting the X conjugations, AND computation and uncomputation, and final
controlled gate, fewer than 12n one- or two-qubit gates suffice for each
multi-controlled operation. At most n-2 work qubits are simultaneously needed.

## 5. Nearest-neighbour geometry and an explicit finite bound

Place the n data-code qubits and at most n-2 work qubits on one line. Its
width w is at most 2n. For any intended two-qubit gate, move one operand by
adjacent SWAPs until the operands are neighbours, apply the gate, then reverse
the SWAPs. This restores every wire position and costs at most
2(w-2)+1<4n nearest-neighbour gates. One-qubit gates need no routing.

Thus a two-level factor costs at most

    (2n)(12n)(4n) = 96 n^3

nearest-neighbour one- or two-qubit gates. One-coordinate phases satisfy the
same bound. The looser uniform bound

    G_one <= 128 n^3 d^2                                    (C5)

therefore suffices for each named unitary A, including the battery-ready
prefix. Compiling (C2) separately at every tick gives

    G_total <= 128 nu n^3 d^2,          w<=2n.                (C6)

These are finite upper bounds, not efficiency claims. They deliberately
allow an exponential cost in the binary description size. The gate matrices,
wire addresses and exact algebraic coefficients are determined by (C1)-(C4)
and the fixed routing rule. There is no large target matrix hidden inside a
single site's Hilbert space: each circuit site is a qubit, and every gate
acts on at most two adjacent sites.

For clean work qubits, the product for each named unitary is exactly
(A on valid codes, identity on invalid codes) tensor I_work on the initialized work subspace.
This includes arbitrary encoded inputs and arbitrary reference entanglement.
The work returns to zero at every named checkpoint, so no fresh work bank or
reset is assumed between compiled ticks. Invalid codes may be used at
intermediate Gray-path or routing stages, but are fixed by each completed
named matrix. On dirty workspace the same gate word is still a total unitary;
the clean-workspace target identity is not asserted there.

## 6. What this local compilation proves, and what it does not

No deterministic intermediate physical checkpoints are inferred from this
word. In a history-Hamiltonian realization, intermediate amplitudes may
contain multiple prefix states coherently; only an independently proved
endpoint identity supplies the selected physical output time.

The result is exact geometric locality for a *simulator circuit* of finite
width and finite length. It proves that the finite source, predicates,
controlled walk steps and complete battery-sector law can be represented by
an explicit sequence of bounded-dimensional local gates. It also retains
all initialized output histories, correlations and specified checkpoints.

The simulator line is not identified with the original particles' spatial
coordinates. Generic QR factors need not preserve the old energy account,
old propagation cones, holding semantics or clock values between named
checkpoints. Reaching the same target checkpoint does not prove those
intermediate properties. The compiled primitives are not claimed to be the
original forward-only controlled W queries. In particular an autonomy or
Hamiltonian construction must account for its own additional clock and
routing resources.

Finally, a nearest-neighbour data circuit plus an abstract Feynman clock is
not by itself a geometrically local Hamiltonian proof: clock-edge terms can
still couple to distant reused data wires. A further local layout or a local
Hamiltonian-computer construction is required. Hermiticity also supplies
reverse terms for every nonzero forward history hop. Neither problem is
removed by the finite compilation theorem above.

[filter]: https://github.com/mathorn1973/twist-j/blob/01acc42b78f75095587765e9a5b91ee70dc28f37/notes/C-FORWARD-ONLY-CAPTURE-FILTER-N/PROOF.md
[extension]: https://github.com/mathorn1973/twist-j/tree/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N
[clock]: https://github.com/mathorn1973/twist-j/blob/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N/CLOCK.md
[energy]: https://github.com/mathorn1973/twist-j/blob/ecb3460977cd2ee8a120797ffa53ba88cbe14171/notes/C-FORWARD-AUTONOMOUS-CLOCK-N/ENERGY.md
