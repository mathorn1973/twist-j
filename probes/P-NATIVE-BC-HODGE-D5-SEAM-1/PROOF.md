# Proof: the canonical native bc sector is not the ramified Hodge D5 module

**L1 exact negative result.**

Use the frozen matrices and composition convention of PREREG.md.

## 1. Native order-five word

The linear parts of b and c differ only by the r-dependent piston shear in c.
Multiplying them in the frozen order gives

    P_n = B_n C_n = I + N_n,

where

    N_n x = r(x) * (0,1,0,-1,0,0)^T.

Thus N_n has rank one and N_n^2=0. It is nonzero, so in characteristic five

    (I+N_n)^k = I + k N_n

for 1 <= k < 5, while (I+N_n)^5=I. Hence P_n has exact order five and
unipotent Jordan type

    J_2(1) + J_1(1) + J_1(1) + J_1(1) + J_1(1).

Equivalently the exact rank sequence of (P_n-I)^k is

    1,0,0,0,0.

This is already a complete similarity invariant sufficient for the decision.

## 2. Hodge marked five-cycle

On the marked augmentation A4 carrier in characteristic five, take the same
coordinate five-cycle C_4 and A_h=Lambda^2 C_4. Direct exact elimination gives

    rank((A_h-I)^k) = 4,3,2,1,0,   k=1,...,5.

Therefore A_h has unipotent Jordan type J_5(1)+J_1(1). Its inverse has the
same Jordan block sizes and the same rank sequence.

## 3. No simultaneous D5 intertwiner

Any invertible simultaneous intertwiner for either frozen orientation would
conjugate the product B_n C_n to A_h or A_h^-1. Similar matrices have equal
rank sequences for every polynomial, in particular for powers of X-I.

The sequences

    native: 1,0,0,0,0
    Hodge:  4,3,2,1,0

are unequal. Hence neither orientation admits an invertible intertwiner.

The verifier independently solves both complete 72-equation intertwiner
systems. Each solution vector space has F_5-dimension eight, but exhaustive
projective enumeration finds zero invertible solutions. This finite census is
an audit of the preceding one-line similarity obstruction.

## 4. Consequences and boundary

Because the D5 representations are not equivalent, there is no transported
Hodge Kbar or wedge metric in the frozen comparison class. The zero counts of
transported projective lines are absence, not a claim of nonunique structure.
The separately computed 11-dimensional native invariant symmetric-form space
does not repair the missing representation equivalence.

This does not contradict the common group presentation b^2=c^2=(bc)^5=1.
In characteristic five, many inequivalent modules realize the same abstract
D5 relation. Here the native product is a rank-one transvection while the
Hodge product carries a length-five unipotent chain.

The result concerns only this canonical pair of native LINEAR PARTS and the
marked Hodge D5 normalizer. Affine translations, selector dynamics, other
native words and enlarged/history-dependent readings remain outside scope.
FIRED-COMMUTATOR-NOGO is unchanged.
