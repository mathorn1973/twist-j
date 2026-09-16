# Integer accumulation, growth estimates and the finite native boundary

**PROOF-FIRST / RESULT-EXPOSED / L1 MATHEMATICS.**
Public lock: [#889](https://github.com/mathorn1973/twist-j/issues/889).
Basis: Public Canon v80 and `P-BINARY-RECORD-QUADRATIC-SELECTION-1`.
The proofs and explicit witnesses below were known before the execution pin.
No historical priority or physical dimension theorem is claimed.

## 1. Exact accumulation of relational layers

Use binom(n,r)=0 for nonnegative integers n<r, and binom(n,0)=1.
Pascal's identity gives, for n,r>=0,

    binom(n+1,r+1)-binom(n,r+1)=binom(n,r).

Summing and cancelling intermediate terms proves the exact antidifference

    sum_(k=0)^(n-1) binom(k,r)=binom(n,r+1).                  (1)

No limit or integral is used. For r>=1, with (k)_r=r! binom(k,r), this yields

    sum_(k=1)^n (k)_r = r! binom(n+1,r+1).                   (2)

The r=0 version of (2) is not asserted: its left side is n, not n+1.

For a fixed positive arity m, the previous probe classifies nonnegative
integer atomic weights invariant under all injections of equality-only
carriers. With pi an equality partition of the m positions and r_pi its
number of blocks, its layer count on k labels is

    S_k = sum_pi c_pi (k)_(r_pi),       c_pi >= 0 fixed.

Thus its tagged disjoint accumulation is exactly

    V_n = sum_pi c_pi r_pi! binom(n+1,r_pi+1).                (3)

If the valuation is nonzero and R=max{r_pi:c_pi>0}, its degree is R+1 and
its leading coefficient is sum_(r_pi=R)c_pi/(R+1). This follows by expanding
each binomial polynomial; positivity forbids cancellation of the highest
degree. It is a theorem about this specified valuation and accumulation.

For binary relations the two coefficients are a on the diagonal and b on
the off-diagonal, giving

    S_k = ak+bk(k-1),
    V_n = a n(n+1)/2 + b n(n+1)(n-1)/3.                      (4)

If b>0, growth is cubic with leading coefficient b/3; if b=0<a it is
quadratic; if a=b=0 the count vanishes and normalized growth is undefined.
For a=b=1, this is the usual exact sum of squares

    sum_(k=1)^n k^2 = n(n+1)(2n+1)/6.

Full Cartesian pair incidence suffices for cubic accumulation but is not
selected by that exponent: every fixed b>0 in (4) gives exponent three.
Relabeling invariance separately at each size is weaker than injection
stability; it permits a_k,b_k varying with k, without the polynomial claim.

The counting carrier in (3) is a disjoint union with the layer index retained.
For full pairs it can be written

    {(k,i,j):1<=k<=n, 1<=i,j<=k}.

If layers overlap in another carrier and are not actual disjoint shells,
the same sum counts occurrences with multiplicity. Cardinality alone neither
supplies a metric nor identifies this constructed carrier with physical space.

## 2. A false dimension formula and its precise repairs

Write S_n=V_n-V_(n-1). The statement

    V_n ~ c n^d  implies  n S_n/V_n -> d                     (FALSE)

is false even for strictly increasing positive integer V_n, c=1 and d=3.
Set V_0=0 and, for n>=1,

    V_n=n^3+(-1)^n n^2+n.

Then V_n/n^3=1+(-1)^n/n+1/n^2 tends to one, but direct subtraction gives

    S_n = n^2-n+1             if n is odd,
          5n^2-5n+3          if n is even.

Both are positive at their allowed n, proving strict increase. Moreover,

    n S_n/V_n = 1                                  if n is odd,
                5-(10n+2)/(n^2+n+1)                 if n is even.

The even error is positive and at most 12/n; the two subsequential limits
are therefore 1 and 5. Even an O(n^2) error around n^3 is insufficient.

Here are sufficient replacements, with their proofs:

1. **Polynomial V.** For degree d>=1 and positive leading coefficient c,
   subtraction of (n-1)^j from n^j gives
   S_n=cd n^(d-1)+O(n^(d-2)), so nS_n/V_n->d. A positive constant
   polynomial gives zero. The identically zero case is undefined.
2. **Controlled local error.** For real c,d>0, write
   V_n=cn^d+e_n with e_n=o(n^d). Then nS_n/V_n->d if and only if
   e_n-e_(n-1)=o(n^(d-1)). Indeed divide S_n by cn^(d-1); the leading
   power difference tends to d and V_n/(cn^d) tends to one. The stronger
   e_n=o(n^(d-1)) is sufficient, since it controls both neighboring errors.
3. **Eventually monotone shells.** Suppose V_n~cn^d, c,d>0, and S_n is
   eventually monotone. For nondecreasing S and lambda>1, put
   m=floor(n/lambda), N=floor(lambda n). For large n,

       (V_n-V_m)/(n-m) <= S_n <= (V_N-V_n)/(N-n).

   Multiply by n/V_n and take limiting lower and upper bounds. They are
   (1-lambda^(-d))/(1-lambda^(-1)) and
   (lambda^d-1)/(lambda-1). Both tend to d as lambda decreases to one.
   For nonincreasing S the inequalities reverse; the same limiting squeeze
   applies. This proves the discrete monotone-density statement directly.

No shell regularity is needed for the macroscopic consequences of V_n~cn^d:

    log(V_n)/log(n) -> d,
    V_floor(lambda n)/V_n -> lambda^d          (lambda>1 fixed).

These follow by substitution of the asymptotic and floor(lambda n)/n->lambda.
Taking the logarithm of the second ratio and dividing by log(lambda) is
another valid exponent estimate. Logarithms are readings here; the counted
sets and (1)-(4) remain integer data.

As context only, eventual monotonicity is a standard additional hypothesis
in the [monotone density theorem, section 7](https://www.math.u-szeged.hu/~kevei/tanitas/1819regvar/RegVar_notes.pdf).
The elementary discrete proof above is self-contained; the verifier imports
no external theorem, dataset or text.

## 3. A finite semantic word carrier cannot have cubic asymptotic growth

Let a finite group G act on a finite set, with a fixed finite generating set
and exact semantic equality of elements or orbit points. Define B_n to be
the elements reached from the identity (or one pointed state) by words of
length at most n. These sets are nested and eventually constant. If the
reachable carrier has M elements, a shortest path to any of them has no
repeated vertex, so saturation occurs by n=M-1. Consequently |B_n| has
growth exponent zero and n(|B_n|-|B_(n-1)|)/|B_n| is eventually zero.

Tagged accumulation of those balls has another exact boundary: if |B_n|=M
for n>=N, then sum_(k=0)^n |B_k| = Mn+constant for n>=N. Its exponent
is one, not three. This is a new counting construction, not the original
ball volume. Counting all syntactic words instead of semantic objects is
different again: five letters have 5^n length-n words, before any equality.

The registered native generators a,b,c,d,e act on X=F5^6. The adopted
DEF-NATIVE-WORD-CURVATURE-CLASS in canon/CANON.md establishes

    Gamma=<a,b,c,d,e> <= AGL_6(F5),
    |Gamma| <= B = 5^6 product_(j=0)^5 (5^6-5^j).

Therefore the preceding argument applies to literal native word balls,
their finite commutator images and the registered finite operator class.
This is a deduction from the already registered finite carrier, not an
enumeration of Gamma or a new computation of its order. The canonical
function-space V has dimension 818; it is not identified with the distinct
three-dimensional trace-kernel W_5. The registered bridge remains open.

The complete autonomous native U state includes an unbounded counter.
This finite-space theorem is not being applied to that full state, nor to
an unspecified infinite lift or continuum limit of a geometry decoder.

## 4. Exact fired-commutator balls and a conditional cubic construction

The canonical FIRED-COMMUTATOR-NOGO theorem identifies the derived subgroup
of <b,d,e> as the 25 fiber translations, with displayed generators

    a0=(3,0), b0=(3,3), c0=(1,3)=a0+b0 in F5^2.

The names a0,b0 here denote translation vectors, not the native a,b maps.
The determinant of the first two vectors is 9=4 mod5, so their coefficients
give a bijection F5^2 -> the translation plane. Declare, for this audit,
one application of any of +/-a0,+/-b0,+/-c0 to cost one step. This symmetric
word radius is an explicit convention, not a physical distance. In basis
a0,b0 the steps are +/-e1,+/-e2,+/-(e1+e2).

First consider the **chosen** torsion-free carrier Z^2 with these six steps.
Its exact word norm is

    rho(x,y)=max(|x|,|y|,|x-y|).

Every step changes each of x,y,x-y by at most one, proving the lower bound.
For x,y of the same sign, take min(|x|,|y|) diagonal steps and then the
remaining axial steps, totaling max(|x|,|y|). For opposite signs use the
two axial directions, totaling |x|+|y|=|x-y|. This attains the bound.

For fixed integer x with |x|<=r, admissible y satisfy both |y|<=r and
|x-y|<=r, giving 2r+1-|x| choices. Hence the exact ball count is

    H_r=sum_(x=-r)^r (2r+1-|x|)=3r(r+1)+1.

Its shells have 6r members for r>=1, and its growth exponent is two. Yet
tagged accumulation of these **balls** has an exact cubic identity:

    H_r=(r+1)^3-r^3,
    sum_(r=0)^n H_r=(n+1)^3.                                 (5)

This is an exact positive example of quadratic relational growth plus one
disjoint accumulation direction producing cubic growth. It does not prove
that the resulting metric is Euclidean three-space or that the new tagged
carrier equals the native one. The balls overlap in Z^2: forgetting layer
tags leaves just B_n of size H_n, not (n+1)^3.

Now retain the native order-five relations, reducing coefficients modulo5.
Every quotient ball is the image of the corresponding integer ball, since
words lift with the same letters. At radii zero, one and two reduction is
injective on the integer ball: coordinates lie in [-2,2], where residues
are distinct. Thus the first sizes are 1,7,19. For radius three, choose
balanced coordinates x,y in [-2,2] for any residue. They have rho<=3 except
possibly (2,-2) and (-2,2), which have norm four. Replace their y coordinates
by 3 and -3 respectively; the resulting (2,3),(-2,-3) have norm three and
the same residues. Radius three therefore reaches all 25 translations.
It cannot saturate earlier since the radius-two count is 19. Thus

    |B_0|,|B_1|,|B_2|,|B_3|,... = 1,7,19,25,25,...,
    sum_(r=0)^n |B_r| = 25n-23             for n>=2.          (6)

The accumulated values agree with cubes at n=0,1,2: 1,8,27. At n=3 the
native quotient gives 52, while the chosen cover gives 64. This is an exact
finite counterexample to extending the apparent cubic prefix in the literal
native carrier. Its eventual ball and accumulation exponents are zero and
one respectively, compared with two and three for the extra infinite cover.

The cover is not forced by writing integer representatives of field elements.
In its vector lift c0=a0+b0 is represented by (6,3), whereas the displayed
residue representative is (1,3). Dropping order-five relations or choosing
a torsion-free cover changes the carrier/equality contract. The proof of (5)
is conditional on that declared choice; (6) retains the registered equality.

There is nevertheless a precise conditional link to the displayed native
maps, stronger than an arbitrary triangular analogy. Interpret the SAME
signed affine b,d,e formulas from canon/CANON.md over Z^6 instead of F5^6:

    b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
    d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
    e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).

These remain involutions. Use [u,v]=u v u^(-1) v^(-1), with the rightmost
map acting first. Direct composition gives pure translations

    t1=[d,e]=(0,0,0,0,-2,0),
    t2=[b,d]=(-5,-5,-5,-5,-2,-2),
    [b,e]=t1+t2.

The two vectors are Z-linearly independent: the piston entries force the
coefficient of t2 to vanish, and the q entry then forces that of t1 to vanish.
The linear part of each of b,d,e negates t1 and t2. Hence the translation
lattice L=Zt1+Zt2 is normal in the generated group. All three pair
commutators lie in L, so the quotient by L is abelian, giving the inclusion
of the derived subgroup in L. Conversely t1,t2 are commutators and generate
L, proving equality. Their action on every integer state is free, so each
L-orbit with these six commutator steps is the triangular lattice above.

Reduction modulo5 sends t1,t2 to a0,b0, so L maps onto the native fired
translation group with kernel exactly 5L, since a0,b0 are a field basis.
This supplies a concrete conditional lift/quotient comparison for (5)-(6).
It does not make the lift canonical: its nonzero piston translations -5
disappear natively, and it has discarded the order-five relations. The
full five-generator integer-lift class is not classified here.

### Silent spatial control, with its distinct commutator type

The current TIME-CUT-READING dictionary places its spatial channel on silent
a,c, expressly not the fired commutators. Thus the preceding positive fired
lift must not be called the spatial dimension of that dictionary.

For the displayed native a,c, with the same optional interpretation over Z,

    a(x)=(p4,p1,p4p,p1p,q,r),
    c(x)=(-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),

direct composition gives

    [a,c](x)=x+v(r),
    v(r)=(-1-r,1+r,-1+r,1-r,0,0).

Both q and r are preserved by this commutator, so its m-th power is
x+m v(r). Its displacement is nonzero over Z and over F5: simultaneous
vanishing of -1-r and -1+r would imply 2=0. It follows that the cyclic
commutator orbit has five points natively, and infinitely many in the
declared Z lift. With one application of [a,c] or its inverse costing one
step, native balls have min(2n+1,5) points; lifted balls have 2n+1 points.
Their tagged accumulations are 5n-1 for n>=1 and (n+1)^2 respectively.
Again, the literal lifted orbit does not supply a cubic count.

This is a GROUP commutator of state maps. It is not the additive Koopman
commutator T_a T_c-T_c T_a, nor its historical compression K_hist. No
equality between those different types is asserted. Other commutators,
products, projections, carriers or limits can have different growth and
need their own declared contract; this is an explicit control, not a
classification of every possible spatial realization.

## 5. What would turn a growth exponent into a geometric statement?

Even for an unbounded count V_n~cn^d, replacing its radius by
n=floor(m^alpha), alpha>0, gives V_floor(m^alpha)~cm^(alpha d).
An untyped count direction can therefore change the inferred exponent.
Conversely, radii bounded above and below by fixed positive linear multiples
preserve the logarithmic growth exponent for nested polynomial-growth balls,
by squeezing between those multiples. This is why a radius must be fixed by
the relation/metric contract rather than adjusted to produce three.

The actual spatial proposal needs a carrier, semantic equality, native
relations, an intrinsic radius or filtration, a nonduplicating counting rule,
and a stated limit regime. A cover or growing-modulus family also needs its
maps and compatibility laws. None is supplied by numerical coefficients
1/3, 1/6, a sphere/cylinder analogy, or the already declared argument/modulus
dictionary. No new necessity or physical interpretation of J's projections
is derived by these identities.

The general inference from cubic volume asymptotics to the local shell ratio
is falsified. Cubic accumulation is proved in its explicit counting class.
The literal finite native-word asymptotic route to d=3 is excluded. A
different infinite geometric realization remains a definition/bridge problem,
not a falsified physical hypothesis. Canon, Registry and all physical gates
remain unchanged. All targets and computations here are at L1.
