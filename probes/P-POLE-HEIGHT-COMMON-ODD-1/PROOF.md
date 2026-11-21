# Exact stock exclusions before a common-word construction

NON-CANONICAL / L1 analytical candidate. The new finite audit is pending.
The proofs below do not use a reported complete stock census. No scientific
program was executed or imported while writing this document. The public
known-input witness used for the upper bound is identified explicitly.

## 1. Fixed preparation and finite neutral ball

Let O=Z[j], Phi_5(j)=0, u=1-j, p=j^2, B=1-p, and

    H(x)=x conjugate(x),       Q(x)=Tr(H(x))/2.

For a neutral stock S in uO and t=+1 or -1, the six-slot input is

    I_t(S)=(tB,-tB,u,u,S,2).

The first four required outputs are (u+tB,u-tB,0,0). Unless restoration
is explicitly required, both helper endpoints are free. The alphabet of
moves consists of all fixed-label pair contacts C, with refusal when the
difference is not in 2O and, on admission,

    C(x,y)=((x+y+p(x-y))/2,(x+y-p(x-y))/2).

It preserves the complete sum, sum H, sum Q and each slot's residue modulo
u. Since C^5=I, inverse words are also available as forward contact words.

Each S in uO has a unique integer five-coefficient representative with
sum zero. Indeed the coefficient sum is zero modulo five, so subtract
one fifth of that sum from every coefficient. In this representative,

    Q(S)=(5/2) sum a_i^2,       sum a_i=0.

Thus the complete ball V={S in uO:Q(S)<=20} lies in [-2,2]^5. Its account
shells have sizes

    Q:       0   5   10   15   20
    count:   1  20   30   60   60.

The patterns are zero; permutations of (1,-1,0,0,0); permutations of
(1,1,-1,-1,0); both signs of (2,-1,-1,0,0); and, at account20,
(2,-2,0,0,0) and both signs of (2,1,-1,-1,-1). There can be at most two
entries of magnitude two; separating zero, one and two such entries
proves this list complete. Hence |V|=171 and every neutral Q is a
nonnegative multiple of five.

## 2. A reversible alphabet obstruction

For e_a=j^a, with indices modulo five, define

    N={0} union {e_a-e_b:a!=b},       |N|=21,
    R={e_a+e_b:a,b in Z/5Z},         |R|=15.

N has Q=0 or5 and residue zero; R has Q=3 or8 and residue two.
The five-root relation is the only coefficient relation. Modulo two,
sums e_a+e_b for nonrepeated unordered pairs are distinct and nonzero:
a purported nonzero relation between two pairs has even support at most
four, whereas Phi_5 has odd support five. Doubled pairs have parity zero.

The admitted neutral pairs are equal or opposite; opposites rotate by p.
For a neutral slot followed by the unique charged slot, the nontrivial
admitted cases are

    C(0,2e_a)=(e_a-e_(a+2),e_a+e_(a+2)),
    C(e_a-e_b,e_a+e_b)=(e_a-e_(b+2),e_a+e_(b+2)).

Exchanging a,b covers the opposite orientation. Reversing the slot order
reverses the output. Every other unequal pair refuses. Therefore N^5 x R
is closed under all contacts and their inverses. No point outside it can
enter it through such a word.

If S belongs to N, the complete initial configuration is in this alphabet.
One required main output has Q=15, because Q(u+/-B)=15,5. Such a target
cannot be reached. This excludes all21 stocks in N, with arbitrary final
helpers and separately chosen words allowed for the two signs.

## 3. Nineteen translated exclusions, with two precise exceptions

The complete gated contact is translation covariant:

    C(x-u,y-u)=C(x,y)-(u,u).

Both the parity predicate and the admitted formula obey this identity.
Take S=u+n with n in N and put r=1+j=2-u. Subtract u from all six slots.
The initial first pair becomes tB-u,-tB-u; one entry has Q=15, so the
translated initial configuration is outside N^5 x R. The required first
four translated outputs, (tB,-tB,-u,-u), all lie in N.

Because the helper sum and Hermitian account are conserved, their possible
translated endpoints x,y must satisfy

    x+y=n+r,       H(x)+H(y)=H(n)+H(r),
    x mod u=0,    y mod u=2.

If n=0 their total Q is3, forcing x=0 and y=r. If n!=0 their total Q is8.
A neutral nonzero value has Q>=5. A residue-two value has Q>=3: choose
its integer five-coefficient representative with sum two, for which
Q=(5 sum a_i^2-4)/2. The minimum is three, attained exactly at e_a+e_b
with a!=b. Similarly the neutral account-five values are exactly N\{0}.

Therefore, if x is nonzero, x lies in N and y in R. The only possible
escape from the alphabet has x=0 and y=n+r. Its full Hermitian budget
requires

    n conjugate(r)+conjugate(n) r=0.

For n=e_a-e_b with a!=b,

    conjugate(n)=-j^(-(a+b)) n,       conjugate(r)=j^(-1) r.

The left side is n r [j^(-1)-j^(-(a+b))], so it vanishes exactly when
a+b=1 modulo five. The four oriented solutions are

    n=+/-u,       n=+/-(j^2-j^4).

For n=+/-u, n+r is2 or2j, still in R. For the other two solutions it is
an account-eight residue-two value outside R. They identify two stocks

    E={u+(j^2-j^4),u-(j^2-j^4)},       Q(S)=10 for S in E.

For all other S in u+N every eligible translated endpoint is in N^5 x R,
so inverse closure excludes reachability. This proves unrestricted-helper
exclusion for19 of these21 stocks. It does not establish reachability of
the two exceptions. If exact helper restoration is required, the target
helpers are n,r themselves; the catalytic no-go covers all21.

Let U0=(u+N)\E and T=N union U0. The account distribution of u+N is
(1,7,6,6,1) on shells0,5,10,15,20, from

    Q(u+e_a-e_b)=10+5(delta_(a,0)-delta_(a,1)
                           -delta_(b,0)+delta_(b,1)).

N intersects u+N in its eight account-zero/five members. Removing E does
not change that intersection. Consequently |T|=21+19-8=32, with counts

    T:       Q0:1, Q5:20, Q10:4, Q15:6, Q20:1.

These32 exclusions are analytical; no stock orbit has been counted here.

## 4. A second exclusion from parity isolation

Reduce values modulo2O. The data pair alone can only rotate as
(+/-p^k B,-/+p^k B). Its five parities are the five unordered root pairs
whose indices differ by two, the diagonals of the five-cycle. The two
equal references u stay fixed and have the edge parity {0,1}. The helper
2 has parity zero. These classes are distinct by the pair-sum argument
in section2.

Define the seven allowed stock parity classes

    P={0,u} union {p^k B:k=0,...,4} modulo2O.

If S has parity outside P, it can meet neither data, reference nor helper
parity. It stays unchanged. Every cross-group contact refuses; the only
nonidentity operation is the rotation of the opposite data pair. Thus the
entire six-slot orbit consists of exactly five states. Both references
remain u and the first-four target is impossible. This proves the
exclusion for each odd sign, not merely for a common word.

This argument uses the exact six-slot preparation. Extra blanks or other
cells can create new matching pairs and are not silently included.

## 5. Exact parity-class counts and the120-stock union

In the unique zero-sum representative, the coefficient parity has even
support. It is the unique even-support representative of its class in
O/2O: adding the five-one relation changes its support parity. The16
classes consist of one support-zero, ten support-two and five support-four
classes. Their populations in V follow without a field-state search:

* Support zero: all coefficients are even, so only zero and a single2,-2
  pair fit the bound. This class has21 stocks.
* A fixed support-two class: opposite signs at those positions give two
  account-five stocks. Equal signs require one opposite doubled coefficient
  at one of the three other positions, giving six account-fifteen stocks.
  Each of the ten classes has8 stocks.
* A fixed support-four class: with zero at the fifth position, choose two
  positive signs, giving six account-ten stocks. With a doubled coefficient
  at the fifth position, the four odd signs have sum opposite to it, giving
  four possibilities for each of its signs. This gives eight account-twenty
  stocks. Each of the five classes has14 stocks.

The isolated classes are the four edge classes other than {0,1}, plus all
five support-four classes. The latter are also the singleton-root classes
when represented by odd support. The parity-isolated set I therefore has
4*8+5*14=102 stocks, with shell counts

    I:       Q5:8, Q10:30, Q15:24, Q20:40.

Its overlap with T has14 members. Explicitly, N contributes eight isolated
short roots. In U0, isolation occurs for the two orientations of each of

    {a,b}={0,2},{1,4},{2,3},{3,4},       S=u+e_a-e_b.

These give eight stocks: two at Q5, four at Q10 and two at Q15. The two
account-five stocks are already in N. Thus

    |T intersect I|=8+8-2=14,
    overlap shells: Q5:8, Q10:4, Q15:2.

Consequently the analytically excluded union has size32+102-14=120 and
shell counts

    T union I: Q0:1, Q5:20, Q10:30, Q15:28, Q20:41.

The residual51 stocks have Q15:32 and Q20:19. The latter are precisely
all doubled nonzero short roots except2u. This is a finite classification
of proven obstructions, not an assertion that the residual stocks work.
A report of nine successful stocks would leave42 residual failures only
if that separate census and its success definition were established.
The present proof does not adopt that reported census or classify those
42 by assertion.

## 6. Four more exclusions from a product of two five-cycles

Four members of the residual account-twenty shell admit another exact
argument. Put

    d in {+/-(j-j^3), +/-(j^2-j^3)},       S=2d.

The data pair cycles as (t p^l B,-t p^l B). Independently, after k
contacts on the helper pair (2d,2), its values are

    (1+d+p^k(d-1), 1+d-p^k(d-1)).

Modulo two both helper values have the common parity

    r_k=(1+d)(1+p^k).

Changing d to -d does not change these parities. Direct expansion in
O/2O gives the following ordered lists for k=0,1,2,3,4:

| d | r_0,r_1,r_2,r_3,r_4 |
|---|---|
| j-j^3 | 0, j+j^2, 1, j, 1+j^4 |
| j^2-j^3 | 0, j^3+j^4, j^2, j^3, j+j^2 |

Every nonzero entry is either a singleton-root class or an edge class
other than u={0,1}. None is in the five diagonal data classes. Therefore
no helper value can contact a data or reference value; data cannot contact
the references either. The reference pair is equal and remains fixed.
The only nonidentity contacts are the two disjoint edges12 and56.

Each has a genuine five-cycle: B is nonzero and d-1 is nonzero. Their
Cartesian product contains exactly25 distinct states, every one reachable
by suitable powers of those two commuting contacts. It is closed under
all15 edges because every other edge either refuses or fixes the equal
reference pair. Both references remain u, so neither odd input reaches
the required first-four target, with arbitrary final helpers allowed.
This orbit size follows from the displayed product, not a reported census.

These four stocks are outside T union I. Their parity is zero, so they
are not in I; the only account-twenty stock in T is2u, which is not one
of them. The enlarged proven exclusion therefore has124 members and
shell counts

    Q0:1, Q5:20, Q10:30, Q15:28, Q20:45.

Its residual47 stocks have Q15:32 and Q20:15. Relative to the separately
reported nine-success census, these four would explain four of the earlier
42 failures and leave38 without an explanation from these criteria. That
last comparison remains conditional on the reported census; the124-member
exclusion and47-member residual do not depend on it.

## 7. A sharp stock-account bound for a specified odd input

Every neutral stock of Q<15 is in the excluded union: the complete lower
shells are Q0,Q5,Q10, and every member has just been excluded even with
unrestricted helper endpoints. Hence Q(S)>=15 is necessary for either
known odd input in this exact six-slot contract.

The bound is attained. For X=1+j-2j^3, Q(X)=15, the public
[PR1900 transition certificate](https://github.com/mathorn1973/twist-j/blob/61743a5fe30bdaf93c1d667b311d0d93e45f823d/probes/P-POLE-HEIGHT-NEUTRAL-STOCK-1/RESULT.md)
supplies the chronological word

    45 56 16 16 16 25 25 25 25 26 26 26 26 36 36 46
    56 56 56 56 26 26 26 26 46 12 12

and its complete intermediate-state certificate for

    (B,-B,u,u,X,2) -> (u+B,u-B,0,0,X,2).

Relabeling1 and2 throughout gives a separate negative-input word. This
establishes sharpness at Q15 for an individually specified odd input,
with exact helper return. The source is an existing exact witness, not a
newly executed search in this proof.

The result is not a minimum over helper counts, nonneutral stocks,
encodings, operation alphabets or physical resources. It also does not
show that every account-fifteen stock succeeds. A common word for unknown
sign or all five input amplitudes requires its own exact transition
certificate; pointwise witnesses cannot simply be substituted for it.
The new common-word audit remains separate from this stock exclusion.
