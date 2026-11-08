# Complete integer carrier and a supplied positive one-stroke law

**NON-CANONICAL / L1 / conditional analytical proposal.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: [#1806](https://github.com/mathorn1973/twist-j/issues/1806).

The construction below retains both outputs. It does not prepare a physical
coherent state from a native point, choose an observed history, or identify
an integer norm account with a continuous-time generator. The formulas are
self-contained proofs, not a new numerical experiment or a formal replay.

## 1. One complete contact on an integer congruence lattice

Let C be the five-cycle on column vectors, C e_k=e_(k+1 mod5), R=C^2,
and let A4={x in Z^5: sum_k x_k=0}. Use the Euclidean form on A4.
Define on two copies of its rational extension

```text
M = ((I,I),(I,-I)),       M^-1=M/2,
D = diag(I,R),
L = M(A4 direct-sum A4),
V = M D M^-1 = (1/2)((I+R,I-R),(I-R,I+R)).
```

Equivalently L consists of pairs (u,v) in A4 direct-sum A4 such that
u and v have the same componentwise parity. Indeed
(u+v)/2 and (u-v)/2 are then integral zero-sum vectors, and the converse
follows from u=a+b, v=a-b. Thus no division with rounding occurs.

D and its inverse preserve A4 direct-sum A4. Consequently V is a bijection
of L with inverse M diag(I,R^-1) M^-1. Since M^T M=2I and D^T D=I,
V^T V=I. In particular the nonnegative integer account

```text
E(u,v)=||u||^2+||v||^2
```

is preserved on every admitted state, including occupied second ports.
Also V^5=I. This is a complete reversible integer model on a declared
congruence lattice, not a stochastic update of a single path bit.

For any x in A4, the ready state (2x,0) belongs to L and

```text
V(2x,0) = ((I+R)x,(I-R)x).
```

Both outputs have integer coefficients. Their full account is

```text
||(I+R)x||^2 + ||(I-R)x||^2 = 4||x||^2.
```

After normalizing the input by its norm 2||x|| for x!=0, the two branch
operators are exactly K0=(I+R)/2 and K1=(I-R)/2. Normalization and the
interpretation of squared norms as probabilities are declared reading
operations; the integer system itself has retained both vectors.

The factor two in this preparation is explicit. An arbitrary primitive
(x,0) need not belong to L. This construction supplies neither a machine
that loads (2x,0) nor free production of its integer account from x.
The relation M^-1(2x,0)=(x,x) makes the correlated two-path preparation
visible in the diagonal coordinates; a change of coordinates has not
derived its preparation from native U.

The projection (u,v)->(u,0) does not in general preserve L. Thus retaining
only the no-click output is not an integer bijection on this full carrier.
One cannot repeatedly discard the second port and reuse the first under
the same lattice theorem; fresh records and their complete outputs must
be included, as in Section 2.

The method of conjugating a root-phase operation into a congruence lattice
has a predecessor in C-INTEGER-CYCLOTOMIC-PHASE-WORK-CONTACT-N at
c5f5697470d506b3105fb0fb2bcb4310da39b056. Its four-slot lattice, trace
account and physical boundary remain distinct. No novelty or acceptance
of that general method is reclaimed here.

## 2. A finite complete record bank

Fix an integer N>=1. Give each of the 2^N record addresses h in {0,1}^N
one copy of A4. Let

```text
H2=((1,1),(1,-1)),
M_N=H2^(tensor N) tensor I5,
L_N=M_N(A4^(direct-sum 2^N)),
M_N^-1=2^-N M_N.
```

For j=1,...,N let D_j apply R to the data vector at address b precisely
when b_j=1 and act as I otherwise. Each D_j is an integer permutation,
preserves the zero-sum condition in every slot, and has order five.
Define V_j=M_N D_j M_N^-1. Then each V_j is an orthogonal bijection of
L_N. The V_j commute. In the port coordinates each V_j is the complete
two-port V of Section 1 on bit j and the data, with other bits untouched.

For any x in A4 the state with 2^N x at address 0^N and zero elsewhere
belongs to L_N: its inverse image under M_N is the bank with x in every
address. Successive V_1,...,V_N give the full final bank

```text
y_h = product_(j=1..N) (I+(-1)^h_j R) x.
```

Every coefficient is integral. The formula follows by the two-port block
identity at each fresh bit; the factors commute because each is a
polynomial in R. Orthogonality gives the exact full account

```text
sum_h ||y_h||^2 = 4^N ||x||^2.
```

Dividing by the initial norm 2^N||x|| gives precisely the complete
history amplitudes in PROOF.md, including every failed branch. The
no-click output alone is y_(0^N)=(I+R)^N x. No output is deleted or reset.

This explicit bank has 5*2^N scalar coordinates with a zero-sum condition
in each slot, hence rational dimension 4*2^N. Its ready account is
4^N||x||^2. These are costs of this particular integer-coordinate
realization, not lower bounds on every device or intrinsic physical
energies. The quantum tensor description uses N record qubits and one
five-level register; tensor dimension and number of registers are distinct.
An unknown occupied bank would require a named export/preparation
operation. It is not covered by assuming this ready bank.

The complete product has fifth power I. After five repetitions of that
whole product on the same bank, the original state returns. A stable
archive therefore needs isolation, a stopped interaction or a separate
retention construction. Repeated readout into fresh ports cannot be
replaced by indefinitely reusing this same closed bank.

## 3. An optional positive static generator, with its exact scope

This paragraph adds a standard complex-Hilbert comparison. It is not the
integer automaton's time law. Set hbar=1 and fix a nominated duration tau>0.
Let P_k be the spectral projectors of R with R P_k=zeta5^(2k) P_k.
Choose n_k in {0,1,2,3,4} satisfying n_k=-2k mod5; in k order 0,...,4
these are (0,3,1,4,2). Then

```text
H_R = (2*pi/(5*tau)) sum_k n_k P_k >= 0,
exp(-i*tau*H_R)=R.
```

For the N supplied binary path registers define

```text
H_N = sum_(j=1..N) ((I-X_j)/2) tensor H_R.
```

Each term is positive, all terms commute, and

```text
exp(-i*tau*H_N) = product_j V_j,
||H_N|| <= 8*pi*N/(5*tau).
```

Indeed exponentiating one term gives P_(+,j) tensor I plus
P_(-,j) tensor R, whose path blocks are the V of Section 1. This proves
one common positive time-independent law for the supplied full record
bank at one nominated time, uniformly on all inputs and passive references.
The preparation |0>^(tensor N) tensor rho has mean generator energy
N Tr(H_R rho)/2. This is the mean generator energy of the supplied ready
state, not a derived preparation-work or fuel cost.

Each term touches one binary register and the same five-level register.
The central register has incidence N. This is locality on a declared
register graph, not a proof of bounded spatial range or bounded incidence
independent of N. The spectral couplings and nominated duration are
supplied. All N commuting contacts run during the same interval; the
construction does not produce N separately timed trials or a self-stopping
clock. The full evolution returns after 5*tau. Continuous evolution need
not preserve L_N between the nominated integer steps.

The quadratic integer account of Sections 1-2 is not identified with H_N
or with a pre-existing physical spectral energy. An additive fuel, clock
and source account would require its own complete conserving construction.

## 4. Preparation and occurrence are still separate

There are two equivalent mathematical descriptions of the mixing step:
prepare a balanced path state, apply a controlled permutation and recombine;
or supply the complete rational V directly. The latter removes a visible
Hadamard symbol from the formula, but still supplies a mixing contact and
the lattice/reading in which its halves are exact. It is not a native
preparation theorem. NATIVE.md states the missing actual-U equalities.

Nor does this integer completion choose one history. It produces the
complete bank. With a declared Born interpretation, PROOF.md gives its
normalized history probabilities. Without such an occurrence reading,
these remain exact quadratic weights of a complete deterministic state.
