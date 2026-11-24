# Removing an invisible three-prime packet and the smallest normalized determinants

**NON-CANONICAL. No authority. Candidate-D, paper deductions.** The complete coupled bound is **O**. Owner 2087, draft 2089, unchanged baseline 6649670532e4d69858bc92994a55a54682f5d619. Action layer NOT_APPLICABLE.

## 1. Exact transfer for conductors with short proper divisors

Let X be a late dyadic integer, D=4X, z=D^(1/3), E=z², and w the taper of round 4. Its largest supported integer is N=2X−1+2kh≤17X/8. The inherited G7 is the round-six star core with both round-seven deletions, just as in round7/REPORT §2. For any conductor-only subset F of its conductors with

    r/P^−(r) ≤ E,                                                     (1)

let V_F contain *every* retained numerator of those conductors, with its original coefficient. Define the real function on the taper

    B_F(n) = Σ_{r∈F} A_r K_r(n),
    A_r = s(r) Σ_{m≤D/r, (m,r)=1} s(m)/m,
    K_r(n)=H(⌊n/r⌋),   H(j)=Σ_{1≤v≤j}χ₅(v) at nonnegative j.

Then, uniformly in F, for every ε>0,

    ||V_F−B_F||_w² ≪_ε X^(2+ε).                                      (2)

Condition (1) says exactly that every proper divisor is at most E. It holds for every three-prime conductor of G7, since each of its primes is at most z. It also admits conductors with more prime factors. For example, products of four distinct split primes in [X^(1/5),2X^(1/5)] have r of order X^(4/5), r/P^− of order X^(3/5), and survive the two small-divisor masks on late blocks. All three or four prime factors mentioned here are distinct.

To prove (2), first take the full, unsmoothed primitive packet W_F=Σ_F A_r Φ_r on integer time. Extend K periodically as in round 3. Its exact projection identity on split conductors is K_r=Σ_{e|r}(e/r)Φ_e. Consequently

    W_F=B_F−Σ_{e≤E} c_e Φ_e,       c_e=Σ_{h>1, eh∈F} A_{eh}/h.       (3)

Every cofactor sum in A_{eh} is still the original coprime signed sum. For each η>0 the inherited divisor bound and harmonic cofactor estimate give |A_r|≪_η X^η and |c_e|≪_η X^η after allowing for the harmonic sum over h. At fixed e the squared mass of the Fourier coefficients of Φ_e is O(1), by its centered numerator bound O(1/|a|). Distinct primitive frequencies with e≤E have circle spacing ≫E^(−2). The translated large sieve on the taper therefore bounds the squared norm of the last packet in (3) by

    O_ε(X^ε(X+E²)E)=O_ε(X^(2+ε)).

The same bound holds after multiplying every Fourier coefficient by the Jackson multiplier m_t, whose absolute value is at most one.

Write J for this Jackson average in integer time. The original high-numerator cut in each shell changes JW_F by O_ε(X^(1+ε)) in norm by round4/FINITE-TAPER §2. The height trim changes it by the same allowance by round6/MARKED-PRIME-CANCELLATION §3, equation (5), with Y=√X exp(−√log X). These estimates permit an arbitrary conductor mask, with complete numerator intervals inside each conductor before trimming. The low-conductor and two round-seven exclusions are already enforced by F. Thus these cuts produce precisely V_F.

It remains to remove J from B_F. Globally |B_F|≪_η X^(1+η) since |K_r|≤1. On 3X/8≤v≤21X/8, its successive difference is Σ_{r|v,r∈F} A_rχ₅(v/r), of size O_η(X^η) by the divisor bound with reduced input η. For n on the taper, shifts of size at most X/2 hence cost O_η(X^η|j|). The Jackson weights have absolute first moment O(√X) and total mass O(X^(−3/2)) beyond X/2, by round4/FINITE-TAPER §2. It follows that |JB_F(n)−B_F(n)|≪_η X^(1/2+η) even at the support endpoints. Summing in the taper and shrinking η proves (2). In particular, zero raw values need only hold on the original taper.

For the whole family (1) write G'=G7−V_F and D'=C_z+B_F. With complete mixed terms and the inherited restricted pair sum P', round seven and (2) give

    ||T−(G'+D')||_w² ≪_ε X^(2+ε),
    P'+2 Re⟨G',D'⟩_w+||D'||_w² = ||G'+D'||_w²+O_ε(X^(2+ε)).        (4)

The restricted energy identity follows from the absolute far-pair and large-gcd estimates and the per-conductor large sieve. The positive-part criterion applies to (4) by comparison of norms. No separate bound of that precision for Q7 minus the new quadratic expression follows from (2).

## 2. An actual cancellation and its obstruction inside the observed times

**Candidate-D.** Take (1) only for r>N. Then B_F=0 throughout the taper, and the entire packet can simply be deleted at the precision of (2), retaining the original C_z. On late blocks every such r has exactly three prime factors: if it had at least four, then r/P^−(r)≥r^(3/4) and (1) would imply r≤D^(8/9), contradicting r>N. Conversely every three-prime G7 conductor with r>N satisfies (1).

Consider the subfamily F_out of all three-prime G7 conductors in (3X,4X]. Choose three distinct split primes from [(13X/4)^(1/3),(7X/2)^(1/3)] to see that |F_out|≫X/(log X)^3. This follows from the fixed-modulus prime number theorem in the two split classes and unique factorization. In fact every three-prime conductor in (3X,4X] with primes at most z has all its primes ≥3X/z²≫X^(1/3), so both round-seven u-factors equal one and both deletion thresholds exceed one whenever applicable. Height, numerator and Jackson conditions admit a=1, and A_r=−8 since D/r<11.

For every distinct pair r,s in this subfamily, take a=b=1. The two b(r,1) factors tend to the same nonzero τ/(2πi), and m_t tends uniformly to one. On the taper |n(1/(5r)−1/(5s))|≤17/480. Each ordered pair therefore contributes real part ≫X. These are genuine strip pairs. In the gcd test R,S>3X/2, so RS min(R,S)/X²>27X/8, whereas gcd(r,s)≤2X for distinct r,s≤4X. Therefore all survive the original cuts. Their real subtotal is

    ≫ X³/(log X)^6.                                                   (5)

Yet the entire signed, all-numerator P_{F_out} is O_ε(X^(2+ε)) in absolute value by (2), B_{F_out}=0 and the restricted energy identity. The real subtotal of all the other retained ordered pairs within this same conductor family equals minus the exact numerator-one subtotal up to O_ε(X^(2+ε)). The cancellation uses actual numerators, time phases, primality and signed cofactors.

For comparison, take F_in to be the corresponding three-prime family in [5X/4,4X/3]. Three distinct split primes from [(5X/4)^(1/3),(4X/3)^(1/3)] give |F_in|≫X/(log X)^3. Every contributing prime in that balanced construction has polynomial size, hence the products survive both round-seven cuts. All A_r=−8. At every integer n∈[3X/2,7X/4] one has ⌊n/r⌋=1 and K_r(n)=1 for all r∈F_in. The taper equals one there. Thus

    ||B_{F_in}||_w² ≫ X³/(log X)^6,
    ||V_{F_in}||_w² ≫ X³/(log X)^6,
    P_{F_in}       ≫ X³/(log X)^6.                                   (6)

The last two inequalities follow from (2) and the restricted energy identity, using e.g. a fixed ε<1 in the squared allowances. This time even all numerators within the selected family leave a signed main contribution exceeding every X^(2+ε) with fixed ε<1.

More explicitly, set H=G7+C_z−V_{F_in}. The inherited unconditional |T(n)|≪_A X/(log X)^A on the taper, together with round7/REPORT (4), implies ||G7+C_z||_w≪_A X^(3/2)/(log X)^A for every fixed A. From (6),

    2 Re⟨V_{F_in},H⟩_w=−2||V_{F_in}||_w²[1+O_A((log X)^(−A))]

for every A>0, increasing the input logarithmic exponent. This locates an actual cross cancellation but yields no fixed power saving for its residual. The coupled expression in (4) retains it.

## 3. An absolute deletion within the surviving determinant strip

**Candidate-D.** For any retained ordered unequal-conductor pair from G7, or from G' in (4), let R,S be its original shells, g=gcd(r,s), l=gcd(|a|,|b|), and L=min(R/|a|,S/|b|). The subfamily satisfying

    0 < |as−br|/(gl) ≤ X/L                                            (7)

has absolute total O_ε(X^(2+ε)). This is a bound on the additive difference of pair sums, leaving the mixed and profile terms unchanged.

Indeed fix R,S,a,b,g. Put u=r/g, v=s/g, a₀=a/l, b₀=b/l. The reduced determinant m=a₀v−b₀u is an integer. For each nonzero m, solutions in the shells lie on one progression of at most 1+lL/g points, since its signed steps are (a₀,b₀). The number of possible m is at most twice min(1280k RS/(Xgl),X/L), with no unit endpoint term since m=0 is excluded. For the contribution of the 1 in the progression count use the first bound. For the lL/g in that count use the second. Multiply by O_ε(X^(1+ε)/|ab|), the absolute bound for a single weighted summand. Summing g≤4X gives for fixed shells and numerators

    ≪_ε X^ε log(2X) [k RS/(l|ab|)+X² l/|ab|].

The harmonic numerator sum of 1/|ab| costs O(log²X). For the second term sum first at fixed gcd l and write |a|=li, |b|=lj. Dropping (i,j)=1 gives Σ_{a,b} l/|ab|≪(log X)^3 since l,i,j≤40√X. The signs cost a factor four and the shell pairs cost logarithms. Since RS≤16X² this proves (7) after ε rescaling. The result holds without replacing any original weights in the surviving pair sum.

Condition (7) removes polynomially many genuine pairs even after the full transfer (1). Take the original shell with X^(9/10)≤R<2X^(9/10) and conductors made from four distinct split primes in [(6R/5)^(1/4),(7R/5)^(1/4)]. There are ≫R/(log X)^4 such conductors in [6R/5,7R/5]. They survive both small-prime masks, have P⁺≤z and r/P^− of order X^(27/40)>E on late blocks. For a=1 they pass the height and numerator cuts, and the multiplier tends uniformly to one. Their A_r are nonzero: after clearing the positive odd common denominator in its cofactor sum, the unit term has odd numerator and every other term even numerator. Partition the conductor interval into O(R²/X) bins of length at most X/R. Cauchy–Schwarz for occupancies and subtraction of the diagonal give ≫X/(log X)^8 unequal ordered pairs in common bins, since R=o(X/(log X)^8). A shared prime would divide a nonzero difference at most X/R, less than the size of every prime factor, so each pair has g=1. With a=b=1 the determinant is at most X/R, within (7), well inside the original strip O(kR²/X) and at g=1 below its actual cutoff R³/X². All these summands are nonzero since the phase oscillation on the taper is o(1). This witnesses arithmetic support, without a lower bound on the sum of their magnitudes.

Let P'' be P' with (7) removed. With D' and G' as in (4), its original mixed term is still 2 Re⟨G',D'⟩_w. The desired all-ε bound for the resulting complete expression, equivalent to that for Q7, is **O**. In particular (6) obstructs paying for every three-prime contribution separately, and four-prime conductors in the last construction have a proper divisor above E. On such conductors equation (3) has longer secondary denominators if used without (1), so its target-scale large-sieve estimate no longer follows by that proof.

## Read, run and attribution

Read the baseline POLICY and AGENTS, candidate FOUNDATION, round4/FINITE-TAPER, round5/NUMERATOR-ESTIMATE, SMOOTH-SUPPORT and FULL-ESTIMATE, round6/CUBE-ROOT-TRANSFER and MARKED-PRIME-CANCELLATION, and round7/REPORT and SMOOTH-DIVISOR-AND-TRANSFER. The exact primitive expansion and finite large-sieve budgets are those of this candidate. The neighboring draft 2093 at ceb77e3632ec4617c54d8e1fd504d3b1c99dd106 was consulted in FULL-COUPLED-ENERGY and LOW-FREQUENCY-PAIRS. Its Möbius coefficients are distinct. The only external counting input for (5)–(7) is the fixed-modulus prime number theorem, previously used in round seven: Tomohiro Yamada, [Explicit formulae for primes in arithmetic progressions, I, §1, Theorem 1.2 (4)](https://arxiv.org/html/1306.5322v4#S1). At fixed modulus five the theorem applies for large arguments, and removal of higher prime powers and partial summation give the fixed-ratio interval counts. No science code, numerical experiment, external confirmation, or two-architecture check. No proof or disproof of RH.
