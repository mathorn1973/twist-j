# A closed alphabet excludes the odd one-charge loader

NON-CANONICAL L1 analytical candidate. This is a local closure proof for
the declared integral contact. The proof was derived before the prospective audit; no orbit census is
used as a premise. The proof establishes
no orbit cardinality, radius or shortest loading word. In particular, a
separately reported count of 1,480 states is not verified by this argument.

## 1. The contact and its finite alphabets

Let O=Z[j], Phi_5(j)=0, u=1-j, p=j^2, B=1-p and

    Q(x)=Tr(x conjugate(x))/2.

The contact C is identity when x-y is not in 2O. Otherwise

    C(x,y)=((x+y+p(x-y))/2, (x+y-p(x-y))/2).

It conserves the pair sum and Hermitian account, hence Q(x)+Q(y), and
satisfies C^5=I. Write e_a=j^a with indices modulo five and define

    N={0} union {e_a-e_b : a!=b},
    R={e_a+e_b : a,b in Z/5Z}.

N contains 21 elements, including 20 nonzero oriented differences.
R contains 15 elements, corresponding to unordered pairs with repetition.
These counts are exact: among five formal coefficients the only rational
relation is a multiple of (1,1,1,1,1). Equality between two listed
differences, or between two listed sums, has coefficient sum zero, so
that multiple must be zero. Thus only the stated identical pairs agree.

Every N element is neutral modulo u; every R element has residue two.
Using Tr(1)=4 and Tr(j^r)=-1 for r nonzero modulo five gives

    Q(0)=0,       Q(e_a-e_b)=5 for a!=b,
    Q(2e_a)=8,    Q(e_a+e_b)=3 for a!=b.

These are arithmetic residues and accounts, not physical electric charges
or calibrated energies.

## 2. The parity classification is exact

Modulo two, Phi_5 remains irreducible, since two has order four modulo
five, so O/2O is F16. The following elementary relation argument also
shows the exact parity distinctions directly.

For unordered pairs {a,b} and {c,d} with a!=b and c!=d, equality

    e_a+e_b=e_c+e_d modulo 2O

would give a relation with zero, two or four nonzero coefficients among
the five roots. A nonzero polynomial of degree at most four divisible by
Phi_5 over F2 must equal Phi_5 itself, whose coefficient vector has odd
weight five. Therefore the even-weight relation must be zero, and the
unordered pairs must coincide. Likewise e_a+e_b is nonzero for a!=b.

Consequently, two nonzero neutral differences have the same parity
exactly when they are equal or opposite. Zero has different parity from
all of them. A charged value 2e_a has zero parity. A charged value
e_a+e_b with a!=b shares parity with precisely the two neutral values
+(e_a-e_b) and -(e_a-e_b).

## 3. Complete local closure

For two neutral slots, equal values remain fixed. An admitted opposite
pair satisfies

    C(d,-d)=(pd,-pd),

which remains in N x N. Every other unequal neutral pair refuses.
This includes a zero paired with a nonzero neutral difference.

For a neutral slot followed by the unique charged slot, the complete
nontrivial admitted cases are

    C(0,2e_a)=(e_a-e_(a+2), e_a+e_(a+2)),
    C(e_a-e_b,e_a+e_b)=(e_a-e_(b+2), e_a+e_(b+2)).

The second formula also covers a zero output when b+2=a. For the opposite
neutral orientation, exchange a and b. Both formulas follow immediately
by taking the pair center and half-difference. Their outputs remain in
N x R. All other neutral/charged pairs refuse.

The reversed slot order has the reversed output, because C commutes with
exchanging its two arguments. Thus the result holds regardless of the
index order used to name a contact. There is no charged/charged pair when
only one slot belongs to R.

Induction now proves closure: any finite carrier with all but one slots
in N and the remaining slot in R stays in this alphabet under every
contact sequence. Contact powers and inverses preserve it as well, since
C^(-1)=C^4. Whole-slot permutations merely move its entries and preserve
the same property. The sequence may be selected separately for a known
input or adapted to intermediate states; no allowed local step escapes
the alphabet.

## 4. The odd target is outside that alphabet

For t=+1 or -1, the input

    (tB,-tB,u,u,0,2)

has five entries in N and one in R. The same is true after adding any
finite number of blank slots, or indeed any additional helper values
chosen from N.

The desired first two slots are u+tB and u-tB. Since

    Q(u)=Q(B)=5,       Tr(B conjugate(u))=5,
    Q(u+tB)=10+5t,     Q(u-tB)=10-5t,

one required slot has Q=15. Neither N nor R contains an element with
that account. Therefore no contact sequence can reach the target, even
if the final helpers are unrestricted and a different sequence may be
chosen for each odd input. A common word for all five t is consequently
excluded in this preparation contract.

The A-family has the same obstruction: A=j-j^3 belongs to N and
Tr(A conjugate(u))=-5, so u+A and u-A again have accounts 5 and 15.

This proof includes arbitrarily many extra blank or short-root neutral
helpers, such as u. It does not include arbitrary neutral elements of O:
for example 2u has Q=20 and is outside N. Nor does the closure table cover
two charged helpers and their mutual contacts. These exclusions identify
where the proof stops; they do not prove that any such added resource is
sufficient for a loader.

## 5. The special six-slot occupancy consequence

The unaugmented odd input has total Q=28. A reachable charged slot has
Q=8 or Q=3, while each occupied neutral slot has Q=5. Thus there are
exactly four occupied neutral slots in the first case and five in the
second. Including the charged slot, at least five of the six slots are
nonzero. In particular, the two original reference positions 3 and 4 can
never both be zero.

That occupancy argument is specific to the six-slot, total-28 contract.
With more blanks it does not by itself forbid those two positions from
clearing. The Q=15 target obstruction in section 4 still applies.

## 6. Why orbit finiteness needs an argument

The equation C^5=I makes each contact individually invertible with finite
order. It does not by itself make the group generated by different
contacts finite, nor prove that a search has exhausted an orbit.

For this integral carrier, positive Q supplies an independent finiteness
argument. In the power basis x=sum_(i=0)^3 a_i j^i,

    Q(x)=[5 sum a_i^2-(sum a_i)^2]/2 >= (sum a_i^2)/2.

At fixed total Q=E and a fixed finite number of slots, every integer
coefficient has absolute value at most floor(sqrt(2E)). The invariant
account shell is therefore finite. For the six-slot odd input E=28,
this bound is seven. The explicit closed alphabets above give a second,
stronger structural finite container, without identifying its entire
reachable subset.

An exhaustive orbit census would additionally require a complete queue
traversal, canonical state encoding and demonstrated closure under every
allowed generator. Such execution is recorded separately from this proof. The analytical obstruction
does not depend on such a census or on any reported shortest path.
