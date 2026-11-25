# A removable divisor family and the unsigned cube-root obstruction

**NON-CANONICAL. No authority. Candidate-D, paper deductions.**
Owner issue 2087, draft 2089, same candidate C-RH-ARITHMETIC-KERNEL-N.
Use the signed star spectrum, inherited dyadic shells, finite taper and
round-six prime profile. All statements are unconditional. The signed
bound for the complete residual and the signed transfer below the cube
root have status O.

## 1. Conductors admitting a large divisor made of small primes

Fix a constant B >= 1, put y=(log X)^B and let u_y(r) be the product
of primes at most y dividing a supported conductor r. Conductors are
squarefree. Put H=R^2/X on one original shell R<r<=min(2R,4X), with
R >= X^(2/3). For any real 1<=U<=R, let V be the packet of any
subset of the actual core modes whose conductors satisfy u_y(r)>=U.
Keep the original complex coefficients. Then

    ||V||_w^2 <<_(B,eps) X^eps R^3 / [U min(U,H)]^(1/B).        (1)

The estimate includes every retained numerator and is uniform in U
and the chosen subset.

Here are the two counts used in its proof. For 1<=v<=4X the number of
y-smooth integers d in [v,yv] is at most

    O_(B,eps)(X^eps v^(1-1/B)).                                   (2)

Choose sigma=1-1/B+eta with fixed 0<eta<1/B. Rankin's bound uses
(yv)^sigma times the product of (1-p^(-sigma))^(-1) over primes at
most y. Its log is O_eta(sum_(m<=y) m^(-sigma)) =
O_(B,eta)((log X)^(1-B eta)) = o(log X). The factors y^sigma v^eta
are absorbed by choosing eta small relative to eps. This proof covers
B=1 by taking sigma=eta>0.

For each conductor with u_y(r)>=v, multiply its small prime factors
in increasing order up to the first partial product >=v. The selected
divisor belongs to [v,yv], including d=1 when v=1. An interval of
length H_0>=v contains at most H_0/d+1 <= 2H_0/v multiples of each
possible d. Thus any such interval contains at most
O_(B,eps)(X^eps H_0 v^(-1/B)) eligible conductors. Globally take
H_0=R and v=U to obtain O_(B,eps)(X^eps R U^(-1/B)) conductors
in the shell.

For a fixed nonzero signed numerator a, write V_a for its packet. A
pair within the taper strip has |a/(5r)-a/(5s)|<=64 k/X, where
k=ceil(3 log_2 X). Centered frequencies in this packet have no
wraparound for large X. Hence |s-r|<=1280 kH/|a|.
For any given r the possible s lie in an interval of length O(kH).
Take H_0=CkH and v=min(U,H) in the preceding count. This bounds the
maximum row degree of the strip by O_(B,eps)(X^eps H
min(U,H)^(-1/B)), absorbing k. Outside the strip |J_w|<=2X^(-8).
The actual coefficients have magnitude <<_eps X^eps/|a|, by the
cofactor harmonic bound, the divisor bound, the numerator kernel
bound and the Jackson multiplier bound. In the near strip use
|J_w|<=2X and multiply the global count by the row degree. The far
pairs contribute O_eps(X^(-6+eps)/a^2) even with the trivial global
count O(X), and are absorbed. The result for the squared norm of V_a
is the right side of (1) divided by a^2, with harmless epsilon
rescaling. Sum norms over a by the triangle inequality. The harmonic
sum up to 40 sqrt(X) costs only a logarithm. This proves (1).

In each original core shell one may delete the entire family

    u_y(r) min(u_y(r),H) >= (R^3/X^2)^B.                         (3)

If the root U of U min(U,H)=(R^3/X^2)^B is <=R, apply (1) at
that U (using at least one). If the root exceeds R, the admissible
portion has u_y(r)>R and u_y(r)|r<=2R, which forces u_y(r)=r.
When it is nonempty the root is at most 2R. Apply (1) at U=R;
the threshold inequality then holds to within a bounded factor
since s min(s,H) changes by at most a factor 4 from R to 2R.
The O(log X) shell norms can again be summed, so the squared error
is O_(B,eps)(X^(2+eps)). A fixed finite union of such B-families
has the same bound: assign overlapping conductors disjointly,
using the uniform subset version of (1).

For B=1 a simpler form of (3) is u_(log X)(r)>=R^(3/2)/X.
Indeed R^(3/2)/X<=H and monotonicity removes the second case.
More generally put W=(R^3/X^2)^(B/2). Whenever W<=H the explicit
threshold is u_y(r)>=W. In particular 1<=B<=2 and R<=X imply
W<=R^3/X^2<=H<=R on the inherited shells. For B=2 at R of order
X^(3/4) this permits deletion when the product of prime factors at
most (log X)^2 reaches a constant times X^(1/4), with the exact
shell-dependent threshold W=R^3/X^2. Formula (3) also covers R>X.
For example take the original shell with X^(3/4)<=R<2X^(3/4)
and S=R^(3/2)/X. The product of all split primes <=log X is
X^(1/2+o(1)) by the fixed-modulus prime number theorem. Select
a product d of distinct such primes in [S,S log X], possible for
large X by the first-crossing construction. Take p<q distinct split
primes in [sqrt(6R/(5d)),sqrt(7R/(5d))]. Then r=dpq lies in the
shell, has two primes of size X^(5/16+o(1)) and has u_(log X)(r)>=S.
The shell position, the bound (log X)^2<P^+(r)<=D^(1/3) and the
numerator-one cuts all hold for sufficiently large X. The prime
number theorem on this fixed relative interval gives
>> R/[d(log X)^2] distinct conductors, at least X^(5/8-o(1)).
Their actual A_r are nonzero: every nonzero nonconstant term in its finite
inner sum has even numerator and odd denominator. After clearing a
common odd denominator, the constant term yields an odd numerator.
The original smoothing multiplier tends uniformly to one at a=1.
Thus (3) reaches polynomial largest primes and this block contains
more than X^(1/2+delta) actual nonzero conductors for each fixed
delta<1/8 when X is large. This is a cardinality statement, without
a lower estimate on the absolute total of those coefficients.

The B=2 deletion also reaches a family missed entirely by B=1.
Take the original shell with X^(7/10)<=R<2X^(7/10), so that
Z=R^3/X^2 has order X^(1/10), R<=X and the B=2 threshold is Z.
The logarithm of the product of all split primes in
(log X,(log X)^2] is (1/2+o(1))(log X)^2 by the fixed-modulus
prime number theorem. This exceeds log Z on sufficiently late
blocks. Take successive distinct primes from that interval up
to their first product d>=Z. Then Z<=d<=Z(log X)^2.
For distinct split primes p<q in
[sqrt(6R/(5d)),sqrt(7R/(5d))], r=dpq belongs to (R,2R].
Both p and q have size X^(3/10+o(1)), between (log X)^2 and
D^(1/3). Consequently u_(log X)(r)=1 while
u_((log X)^2)(r)=d>=Z. The B=1 threshold sqrt(Z) tends to
infinity, so none is deleted at B=1. The fixed-relative-interval
prime count and unique factorization yield at least a constant
times R/[d(log X)^2], hence X^(3/5-o(1)), such conductors.
Their original cofactor sums are nonzero by the same odd-denominator
argument and their numerator a=1 survives all original cuts:
r>D^(2/3), X/r has order X^(3/10), and the multiplier tends
uniformly to one. Thus the fixed union with B=1 on all shells
and B=2 on R<=X contains these additional actual nonzero modes.

Write G_new for the remaining core, and P_new for its original
restricted determinant sum. With z_0=D^(1/3) and the unmodified
two-prime profile C_(z_0), including its diagonal, this yields

    ||T-(G_new+C_(z_0))||_w^2 <<_(B,eps) X^(2+eps).
    Q_new = P_new+2 Re <G_new,C_(z_0)>_w+||C_(z_0)||_w^2.        (4)

The restricted energy identity applies since the distant-pair and
large-gcd bounds are absolute and the within-conductor bound allows
subsets. The round-six all-epsilon criterion consequently holds
with (Q_new)_+. Its proof compares approximation norms and keeps
the mixed term in (4). It assigns no separate X^(2+eps) estimate to
the difference of two signed pair sums.

## 2. The actual below-cube-root discrepancy has a large positive subtotal

Use a new threshold z=D^gamma for any fixed 0<gamma<1/3 and put
E=D/z. Fix an integer l>(1-gamma)/gamma. For 1/4<gamma<1/3 one
can take l=3. In the primitive expansion of the exact round-six
Delta_z=L_z-B_z, with its original Jackson multiplier if applied,
there is a positive real subtotal from unequal conductors, both
numerators one, of magnitude at least

    c_gamma E^3/(log X)^(2l+2).                                   (5)

Here and below l can be fixed as a function of gamma. These pairs
may also obey the original star numerator and height cuts, taper
strip and small-gcd cutoff. This matches the power E^3 of the
previous upper bound for absolute pair majorization and precludes
pushing this majorization to O_eps(X^(2+eps)) for every epsilon
at any fixed gamma<1/3. It gives no lower bound for the signed
squared norm of Delta_z. For an explicit absolute upper comparison,
the primitive frequencies have circle spacing >>E^(-2), so a taper
strip has at most O(1+kE^2/X) neighbors per row. Using
2|c_i c_j|<=|c_i|^2+|c_j|^2 and the round-six squared coefficient
mass gives O((XE+E^3)(1+log X)^6) in absolute value summed over
the near pairs. The absolute far contribution is negligible by the
taper tail and the harmonic bound on the sum of absolute coefficients.

To prove (5), take r to be a product of l distinct split primes
in [(3E/5)^(1/l),(2E/3)^(1/l)]. Fixed-modulus prime counting gives
N >>_gamma E/(log X)^l distinct r by unique factorization. In
particular 3E/5<=r<=2E/3 and P^+(r)=o(z) because
(1-gamma)/l<gamma. Round six writes Delta_z as a polynomial in
K_e with e<=E. Only e=r can contribute to its primitive coefficient
at any chosen r>E/2. Since 3z/2<=D/r<=5z/3<z^2, the coefficient is

    D_r = -2s(r) sum_(z<p<=D/r, split prime) 1/p.                  (6)

The prime sum is bounded above and below by positive constants
times 1/log X uniformly here, by the fixed-modulus prime number
theorem on [z,3z/2] and [z,5z/3]. The D_r have a common sign and
|D_r| is comparable to 1/log X, with constants depending on gamma
and l. The true normalized b(r,1) tends uniformly to the same
nonzero complex number tau/(2 pi i). The multiplier m_t(1/(5r))
tends uniformly to one since r/sqrt(X) tends to infinity. All
chosen r have r>X^(2/3), P^+(r)>(log X)^2 and h=X/r of order
X^gamma, below the original star cutoff. The power numerator cap
allows a=1 in every occupied shell.

Partition [3E/5,2E/3] into O(X/E) bins of width at most
c E^2/X, for a sufficiently small absolute constant c. Within a bin,
|n(1/(5r)-1/(5s))|<=1/40 on the taper support. Every ordered
distinct pair there contributes real part >>_gamma X/(log X)^2,
using the common sign, the asymptotic for b, nonnegative w, and
sum w>=X. The bins contain at least N^2/O(X/E)-N such ordered
distinct pairs by Cauchy-Schwarz. Its first term dominates N because
E^2/[X(log X)^l] tends to infinity. This gives (5). The same-bin
frequencies obey the taper strip with room to spare. The large-gcd
bound in FINITE-TAPER section 3 uses only |D_r|<<_eps X^eps, the
harmonic numerator weights, the strip and the shell upper limits
for the actual counting argument. These all hold here. Thus
deleting the large-gcd pairs costs O_eps(X^(2+eps)) in absolute
value. Choose eps<1-3gamma to preserve (5), since
E^3=(4X)^(3-3gamma). The same estimates hold if the optional
smoothing is omitted. Contributions outside the positive subtotal
are still coupled in the signed discrepancy.

## Inputs and checks

The inherited objects were read in round6/CUBE-ROOT-TRANSFER.md,
round6/MARKED-PRIME-CANCELLATION.md, round6/REVIEW-CUBE-ROOT.md,
round5/NUMERATOR-ESTIMATE.md, round5/SMOOTH-SUPPORT.md,
round4/FINITE-TAPER.md and the preceding split-prime tail. Round five's
positive-frequency bins in NUMERATOR-ESTIMATE section 3 underlie the
count in (5). The new coefficient identification (6) is specific
to the primitive-versus-raw discrepancy. Neighboring draft 2093,
content eac05e3cde56d0fb3e429b91aa7129087e5da4db, studies different
balanced coefficients and supplied no coefficient bound for (1) or
(6). The only external arithmetic input beyond inherited elementary
estimates is the classical fixed-modulus prime number theorem already
cited in round5/SMOOTH-SUPPORT.md. Yamada, [Explicit formulae for
primes in arithmetic progressions, I, Introduction](https://arxiv.org/html/1306.5322v4#S1), gives this
for each of the two split residue classes at the fixed modulus five
for all sufficiently large arguments. Removing higher prime powers
costs O(sqrt(x) log^2 x), and partial summation gives the asserted
fixed-relative-interval counts. No science code or numerical
experiment, independent review, RH assumption or physical result.
