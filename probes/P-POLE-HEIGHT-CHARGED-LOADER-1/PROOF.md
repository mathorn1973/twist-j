# Exact constraints for a charged unknown-input loader

NON-CANONICAL L1 analytical candidate. These proofs classify possible
endpoints and exclude restricted routes. They do not establish that a
common loading word exists. No scientific program was executed or
imported to prepare this document.

## 1. Carrier, inputs and goal

Let O=Z[j], Phi_5(j)=0, u=1-j, p=j^2 and
Q(x)=Tr(x conjugate(x))/2. The integral contact fixes (x,y) unless x-y
belongs to 2O. On admission it acts as

    C(x,y)=((x+y+p(x-y))/2, (x+y-p(x-y))/2).

It preserves the pair sum and Hermitian account, and C^5=I. The six-slot
input for t in {-2,-1,0,1,2} is

    I_t=(T_t,-T_t,u,u,0,2),       T_t=tB,       B=1-p.

One common finite word must put the first four slots at

    (u+T_t,u-T_t,0,0).

The final helpers may depend on t, but every helper value must be
reported. Only fixed-label contacts are admitted in this probe; there
are no supplied slot swaps, resets or external input-dependent choices.
The parity predicate inside C remains part of the operation.

The initial sum is 2u+2 and total Q is 10t^2+18. The first four desired
outputs have sum 2u and Q equal to 10t^2+10, exactly the initial account
of the four main slots. Each individual embedding's corresponding
Hermitian account also agrees. These budgets permit the target but do
not prove its reachability.

## 2. Exactly five possible helper endpoints

Every contact preserves each labeled slot modulo u, because p-1 is
-u(1+j) and 2 is invertible modulo u. Thus slots 1 through 5 remain
neutral modulo u and slot 6 retains residue 2.

Let final helper values be h5,h6. Their sum must be 2 and their total
Q must be 8. Write h5=1-z,h6=1+z with z=1-h5 in O. Polarization gives

    Q(1-z)+Q(1+z)=4+2Q(z),       hence Q(z)=2.

Here Q(1)=2. The integral vectors of account two are exactly

    z in {+j^r,-j^r : r=0,1,2,3,4}.

An elementary proof uses five coefficients a0,...,a4 with a4=0:

    2Q(z)=5 sum a_i^2-(sum a_i)^2
         =sum_(i<j)(a_i-a_j)^2.

If the largest and smallest coefficients differ by at least two, their
pair contributes at least four, and each of the other three coefficients
contributes at least two through its pairs with those extremes. The sum
is at least ten, contradicting 2Q=4. The range is therefore one. If m
coefficients take its higher value, the sum is m(5-m), equal to four
only for m=1 or 4. Subtracting a common coefficient does not change the
field element, and leaves one signed fifth root of unity.

Since h5 is neutral, z is 1 modulo u. This excludes the negative roots.
Using p to order the same five positive roots, all eligible endpoints are

    G_(t,k)=(u+T_t,u-T_t,0,0,1-p^k,1+p^k),       k=0,...,4.

Each candidate also satisfies the complete Hermitian budget because
p^k conjugate(p^k)=1. This is a complete necessary endpoint list, not a
reachability theorem. A simultaneous five-input search has 5^5 possible
helper-phase assignments.

Only k=0 restores the original ordered helper pair (0,2). For k!=0 the
helper has changed its exact state. Equal sum, Q and residues do not make
it a returned catalyst. A claimed loader must preserve and disclose that
phase resource, including any dependence on t.

## 3. One source family suffices

The other supplied family is A_t=t(j-j^3)=jT_t. The admitted contact on
an antisymmetric pair multiplies both signed entries by p. Therefore

    C_12^2(A_t,-A_t)=(T_t,-T_t),       since p^2 j=1.

After any B-family loader, applying C_12^3 to its first two outputs gives
(u+A_t,u-A_t), because their center is u and p^3=j. Hence prepend
C_12^2 and append C_12^3 to obtain an A-family loader from the same word.
The helpers are unaffected by this wrapper. Its forward elementary cost
is five additional contacts. This reduction does not equate the two
native piston charts or construct their interface to the O slots.

## 4. A uniform admission pattern cannot load the bias

Suppose a word, even with fixed permutations and any fixed auxiliary
constants, has the same admitted/refused decision at each elementary
contact for all five t. Under that assumption its slot values are affine
functions a_i t+b_i. Initially the only nonzero coefficients are B,-B,
and both corresponding intercepts are zero.

For a contact to admit for both t=0 and t=1, its coefficient difference
and intercept difference must both belong to 2O. A variable slot with
coefficient +/-p^r B cannot therefore contact a constant slot on a common
admitted branch: p^r B is not divisible by two. A common refused contact
changes nothing. Contacting the two variable slots merely rotates their
opposite coefficients by p; their zero intercepts remain zero. Fixed
permutations only move these two slots.

Induction gives exactly two variable slots, with coefficients +/-p^r B
and intercept zero, throughout the word. Neither required output u+T_t
nor u-T_t has zero intercept. Consequently a successful common loader
must have different contact admission histories for some inputs. This
argument respects the nonlinear predicate: it excludes uniform branch
histories rather than replacing the actual contact by an always-admitted
linear map.

## 5. Why one isolated charged helper is insufficient

Consider the five-slot input (T_t,-T_t,u,u,2), with odd t=+1 or -1.
Modulo two, O is F16: Phi_5 is irreducible over F2 since 2 has order
four modulo five. The fifth-power map is its norm to F4. For residues
of the data and reference,

    norm(B)=p+p^(-1)=j^2+j^3,
    norm(u)=j+j^(-1)=1+j^2+j^3.

They are distinct and nonzero. Multiplication by p preserves this norm.
Thus no data value +/-p^r T_t can share parity with u. Neither can it
share parity with the even helper 2.

The two data slots can only rotate as an antisymmetric pair; the equal
references remain fixed; all cross-group contacts refuse. No zero can
be produced and the required reference clearing is impossible. Fixed
permutations merely move these isolated values and do not fix the defect.

With the additional blank, however,

    C_56(0,2)=(1-p,1+p),
    C_56^3(0,2)=(u,1+j).

These give helpers matching the data parity or reference parity,
respectively. Before the first admitted C_56, an odd six-slot input has
only the isolated behavior above, plus an untouched blank. Therefore
any successful odd-input trajectory must include an admitted C_56.
This opens an interaction route; it does not yet supply a loading word.

## 6. Forward-contact lower bounds with fixed labels

There is exactly one nonneutral slot throughout: slot 6 has residue 2.
For a neutral slot i define its leading residue r_i=x_i/u modulo u,
identified with F5. A contact between neutral slots leaves each r_i
unchanged. On an admitted forward contact between neutral i and slot 6,

    (x_i'-x_i)/u = -(1+j)(x_i-x_6)/2 = 2 modulo u.

This formula is independent of whether the neutral slot is written first
or second. Refusal contributes zero. Let n_i count admitted elementary
forward contacts between slot i and slot 6 during one successful run.
The required leading changes in main slots are

    (+1,+1,-1,-1),

because B/u=1+j=2 modulo u. Hence

    n1,n2 = 3 modulo 5,       n3,n4 = 2 modulo 5.

At least ten charged-to-main contacts are necessary. For odd inputs, the
preceding parity argument also requires n5>=1, so at least eleven
forward contacts are needed in total.

The helper phase sharpens the bound. Since p=1-2u modulo u^2,

    (1-p^k)/u=2k modulo u,       so n5=k modulo 5.

For final phases k=1,2,3,4 the odd-input lower bounds are respectively
11,12,13,14. For k=0, n5 must be a positive multiple of five, giving at
least 15. These are necessary bounds, not demonstrated achievable
lengths. Additional neutral-neutral or refused contacts only increase
the word length.

The cost convention is essential: one forward C counts one. A macro
C^r costs r for r=1,2,3,4; C^(-1)=C^4 costs four. These numbers do not
bound a different alphabet that prices an inverse as one, or supplies
slot permutations. No physical time, electrical charge, energy unit or
action normalization follows from these arithmetic contact counts.

## 7. A universal bound on the B-loader stock

For the B-family funding contract let I(v)=Q(v_2-v_3) and define B_load
as max(0,I(prefix)-I(initial)) over every forward elementary prefix and
all five inputs. The initial and loaded interactions are

    I(initial)=5+5t^2+5t,       I(loaded)=5+5t^2-5t.

The endpoint t=-2 therefore requires B_load>=20. At every prefix the
site-account sum remains 10t^2+18. Positivity and polarization give

    Q(x-y)=2Q(x)+2Q(y)-Q(x+y)<=2[Q(x)+Q(y)],
    I(prefix)<=2(10t^2+18).

Consequently

    I(prefix)-I(initial)<=15t^2-5t+31<=101,
    20<=B_load<=101.

This is a conservative universal interval for any successful word in
this six-slot B contract. The exact stock is obtained from its actual
prefixes. The bound neither gives a loading word nor funds an untested
A-family schedule or a different continuous interpolation.
