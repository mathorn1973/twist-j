# Retained contact context: analytical proof

**NON-CANONICAL / conditional candidate-T / L1.** The exact carrier, three
completed contacts, observation domain and source bindings are those of
CONTRACT.md and README.md. All statements below are exact and conditional
on those already proved complete old-model laws. No program was executed
to establish this note. N_0 includes zero.

## 1. Universal receiver-gain identity

Write Z=T X. Immediately after Ghat let the source and receiver stocks be
s and t, and let the initial link stock be u. G preserves each cell energy.
The two actual stock swaps send

    (source stock, receiver stock, eta)=(s,t,u) -> (u,s,t).

F then preserves each cell energy. Consequently

    E_R(Z)=E_R(X)-t+s,
    r_R(Z)=s,             eta(Z)=t,
    E_R(X)=E_R(Z)-r_R(Z)+eta(Z).                    (1)

This uses occupied stocks; it does not assume a successful G reaction,
an integral split, Gauss admissibility, or a clean pointer/link.

For a final state Y and label k, apply (1) to Z=S_k Y. Since S_k preserves
E_R and eta and is its own inverse, X=F_k^-1 Y=T^-1 S_k Y satisfies

    g_k(Y)=E_R(Y)-E_R(X)
          =r_R(S_k Y)-eta(Y)
          =r_R(Y)-eta(Y)-lambda_k(Y).              (2)

In particular a refused contact contributes effective price zero even
when its unfunded raw proposal has nonzero price. Equation (2) proves C1
on the entire carrier, including every refused branch.

## 2. Exact one-step fibres and the sharp minimum

At fixed Y, the three histories have the unique predecessors F_k^-1 Y.
By (2), two of their gains agree if and only if their effective prices
agree. The exhaustive partitions of Kctx are therefore

    {012}, {01|2}, {02|1}, {12|0}, {0|1|2}.        (3)

Here, for example, {01|2} means lambda_0=lambda_1!=lambda_2. This is a
classification by the exact complete-contact rule, not by raw proposal
prices. It includes identities, nonidentity zero-price contacts, and
equal nonzero prices without requiring any of these to be conflated at
the state level.

Let q1(Y) be the number of blocks. Any adequate supplementary code must
take different values on histories with different gains: otherwise the
same reading input (Y,code) would have two different required outputs.
Thus its alphabet has at least q1(Y) values. Conversely sort the distinct
integer gains increasingly and encode their rank at Y. This uses exactly
q1(Y) values and reads the gain. A common three-value alphabet, with code
k itself, works for every Y. Recovering k is unnecessary for gain reading
when two gains agree; a bijection on labelled histories is a different,
stronger requirement.

The following explicit final state proves that the common bound three
is sharp even within the Gauss sector. Set v=(1,0,0,0), let the source be
the all-zero cell, and set eta=p=0. The receiver is

    m=(0,0,0), b=(5v,10v,-15v),
    E=(-1,-1,7,-8), M=(0,0), r=0.                 (4)

Denote this whole old state by Y*. Its split is y=0, sigma=(-1,7).
Its charges satisfy DE=(5,10,-15)=rho, so its defect vanishes.
Zero matter is neither the reactive R triple nor the AM triple; G is
therefore the complete identity on this receiver and the three contact
images. The contacts do not change matter or y. Their acceptance bits
all equal zero, so each funded proposal below is actually committed:

| k | n | E after S_k | b coefficients after S_k, in units v | raw/effective price | stock |
|---|---:|---|---|---:|---:|
| 0 (01) | -1 | (1,1,8,-7) | (10,5,-15) | 0 | 0 |
| 1 (02) | -4 | (-5,-5,-5,0) | (-15,10,5) | -40 | 40 |
| 2 (12) | -5 | (4,4,-3,7) | (5,-15,10) | -25 | 25 |

For transparency, E.v_01=5, E.v_02=35, E.v_12=40 and the vector squared
norms are 10,15,15. These give prices 10-10=0,240-280=-40,375-400=-25.
The first contact changes state despite having zero price.

The b energy is 6(25+100+225)=2100. Hraw in (4) is 115; after the three
contacts it is respectively 115,75,90. Thus all three receiver energies
including stock equal 2215. Each contact preserves Gauss defect. Since
the static fields have y=0, F and F^-1 fix them. T^-1 moves the contact's
receiver stock into the source and sets the receiver stock to zero;
all G steps remain identities and p stays zero. The three predecessors
therefore have receiver energies

    2215, 2175, 2190,

and give distinct gains

    g_0(Y*)=0,              g_1(Y*)=40,           g_2(Y*)=25.          (5)

Their source energies are respectively 0,40,25, so every predecessor
and Y* has total energy 2216, including the constant pointer energy 1.
All predecessor and final cells are Gauss states. This proves C2, while
making no assertion that every narrower preparation class contains (4).

## 3. Entire archive fibres

For known horizon n, let A_n(Y) be the set of distinct ordered gain
archives obtained from all words ending at Y. At horizon zero

    A_0(Y)={()}.

For n>=1 the exact backward recursion is

    A_n(Y) = union over k in Kctx of
             { (a,g_k(Y)) : a in A_(n-1)(F_k^-1 Y) }.                (6)

Proof: the last label k determines the unique penultimate state
F_k^-1 Y and the last gain (2). Every preceding word contributes precisely
one archive in its A_(n-1). Conversely appending k to each such preceding
word gives a valid history ending at Y. Equal tuples from different
branches are counted once, as the target is the archive rather than the
labelled word. This proves (6) by induction.

Two histories belong to the same observation-fibre block exactly when
their archive tuples agree component by component. The same factorization
and pigeonhole argument as above yields the exact local code minimum

    q_n(Y)=|A_n(Y)|,             1<=q_n(Y)<=3^n.                     (7)

Lexicographic rank among A_n(Y) attains that minimum abstractly. This is
not an efficient implementation claim and does not assert equality
q_n=3^n for every n. A known fixed word already determines all predecessors
by successive complete inverses, and therefore needs no extra word code.
Equations (6)-(7) prove C3.

## 4. Finite energy shells and unbounded archive capacity

The shell argument needs the complete finite-dimensional integer carrier,
nonnegative stocks, finite pointer, and the bound positive definite
quadratic forms. These premises are explicit, rather than inferred from
a finite census. For M=(u,w), directly expanding gives

    4Hraw(E,M)=||2E+CM||^2 + u^2 + (u+w)^2.                         (8)

This vanishes only when E=M=0. For z=(a,b,c,d), direct expansion of the
bound K gives

    4Q(z)=9(a+b+c+d)^2+(a-b+c-d)^2
           +14((a-c)^2+(b-d)^2).                                  (9)

All terms can vanish only when a=b=c=d=0. These are positive definite
quadratic forms on finite-dimensional real spaces. Hence their sublevel
sets are bounded and contain finitely many integer vectors. For fixed
Htot=H, (8)-(9) bound every matter, b and field coordinate; nonnegative
cell stocks and eta are bounded as well, and p has five possibilities.
Thus the complete shell Omega_H is finite. The assertion does not require
fixing Gauss defect, reaction status or other invariant sectors.

Each F_k is a complete energy-preserving bijection and therefore a
permutation of Omega_H. For H=2216 this shell contains Y*. There exists
a common positive integer L such that all three permutations satisfy

    F_0^L=F_1^L=F_2^L=id on Omega_2216.                             (10)

For example take a common multiple of their finite permutation orders.
No value, short recurrence time or computational bound for L is claimed.

For each k, the length-L constant word k^L is a loop from Y* back to Y*.
Its last gain is g_k(Y*), because its final state is Y* and last law is
F_k. By (5) the three last gains differ. Concatenate m independently
selected such loops. All 3^m resulting histories have the same fixed
initial state Y*, the same final state Y*, the same known horizon mL,
and the same total energy. Their gain archives are pairwise distinct:
at the last step of the first differing block their gains are distinct.
Consequently

    q_(mL)(Y*) >= 3^m,             m>=1.                            (11)

A supplementary alphabet of fixed finite cardinality N cannot read all
these archives once 3^m>N. This proves C4 even under the stronger
fixed-initial-state restriction. It does not prohibit reading only the
last gain, a single fixed horizon, or using memory of unbounded capacity.
Finite energy shells for the old carrier do not themselves make an
unbounded auxiliary memory physically available.

## 5. Bijective occupied-memory extension and repetition

Adjoin two nonnegative integer registers (a,b), with every occupied value
admitted. Euclidean division determines unique k in {0,1,2} and q>=0 with
b=3q+k. Define on the whole extended carrier

    Bctx(X,a,b)=(F_k X, 3a+k, q).                                  (12)

Given any output (Y,a',b'), uniquely write a'=3a+k and set

    Bctx^-1(Y,a',b')=(F_k^-1 Y, a, 3b'+k).                         (13)

Composing (13) after (12) recovers X by F_k^-1 F_k, recovers a from
floor((3a+k)/3), and recovers b from 3floor(b/3)+(b mod3).
Conversely composing (12) after (13) recovers Y by F_k F_k^-1 and
recovers both output integers by the same division identities. Hence
Bctx is globally onto and one-to-one, with no clean-register premise,
including a=0 or b=0 and all refused-contact states.

Let k_j be the digit selected at step j. Induction yields

    a_n=3^n a_0 + sum_(j=1)^n k_j 3^(n-j),
    b_n=floor(b_0/3^n).                                           (14)

The residue a_n mod3^n gives exactly the last n digits, in their order
(k_1,...,k_n), even when a_0 was occupied. Reading the final digit first
and applying (13) repeatedly reconstructs every old predecessor and
every gain; thus the full archive is an exact function of the final
extended state and n. No register is reset between steps and no fresh
clean bits are supplied.

Any prescribed finite word of length n can be supplied by taking

    b_0=sum_(j=1)^n k_j 3^(j-1) + 3^n t,           t in N_0,         (15)

with arbitrary occupied a_0 and arbitrary remaining input t. This is
preloaded finite-word selection. A fixed finite integer b_0 eventually
has only zero digits left, so it does not encode an arbitrary infinite
input stream. That stronger contract needs a different infinite carrier.
Two integer registers are a fixed register count with unbounded capacity,
fully consistent with the finite-alphabet no-go (11). C5 follows.

For comparison, the simpler map (X,k)->(F_k X,k) is also a bijection.
Repeating it applies the same retained k each time. Treating a newly
chosen k as freely inserted and its predecessor label as silently
overwritten would change this map and lose its inversion guarantee.

## 6. Scope of energy, source and next-step compatibility

Every old-state component of (12) preserves the bound Htot. No physical
controller energy or cost of arbitrary integer capacity has been derived.
A constant bookkeeping energy on the added registers can make an
abstract extended conserved quantity, but does not supply a physical
memory, preparation procedure, coupling, readability or work reservoir.

A proposed next K/T3 composition must specify its complete carrier,
equality and reader, its exact order with (12), and both inverse
identities on all occupied helper states. A restricted set is admissible
only with an explicit invariant-domain proof. A controller that changes
a or b must be included in the inverse and archive analysis; discarding
one register does not preserve these claims. Static-contact commutation
with G and F is not commutation with the stock swaps, T, or a controller.

The source bridge remains conditional: this note proves no independently
admitted native source law U, no operational encoder from native source
states, and no physical readout/cost model. A time-dependent reader that
inserts the intended target does not establish source selection. The old
G/F/stock alphabet preserves the node-charge labels and cannot by itself
implement a charge-changing static contact on the same carrier; that
requires an admitted new coupling. The source notes' obstruction to an
instantaneous onto image of an unbounded-energy target remains in force.

All conclusions are on the frozen three-contact family and its literal
coordinate equality. No metric/Hilbert representation, photon claim,
hardware feasibility or canonical promotion follows.
