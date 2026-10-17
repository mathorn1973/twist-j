# P-FIELD-CHAIN-UNIT-SEED-2 proof

NON-CANONICAL / L1. Candidate-T for the two universal reductions
(complete bound, coset minimum); the finite residue table is a
candidate-C exact computation audited against them. Definitions are
the literal Canon v102 ones restated in PREREG.md.

## 1. Complete bound for bounded-energy shells

Canon gives 4*Hraw(E,M) = ||2E + CM||^2 + M0^2 + (M0+M1)^2 and
Hraw(P y) = H(y) for P(a,b,c,d) = (a-b, -a, b, b, c, d). Substituting
E = (a-b, -a, b, b), M = (c, d) and
CM = (c-d, -c, d, d) gives the polynomial identity

    4H(y) = (2a-2b+c-d)^2 + (2a+c)^2 + 2(2b+d)^2 + c^2 + (c+d)^2,

which the verifier also checks by exact coefficient expansion. Every
term is a nonnegative integer square (with weight 2 on the third), so
H(y) >= 0, and H(y) = 0 forces c = 0, then a = 0 from (2a+c)^2, then
d = 0 from (c+d)^2, then b = 0 from (2b+d)^2: the zero set is {0}.
H is integer-valued by its displayed polynomial.

If H(y) <= k, each squared linear form is <= 4k and 2(2b+d)^2 <= 4k.
With s = floor(sqrt(4k)) and t = floor(sqrt(2k)):

    |c| <= s,  |c+d| <= s  hence  |d| <= 2s,
    |2a+c| <= s            hence  |a| <= s,
    |2b+d| <= t            hence  |b| <= (t + 2s)/2 floor.

So every integer point of shell <= k lies in that finite box, for every
k, with the bound derived before enumeration and independent of any
point it finds. For k = 1 the box is a,b,c in [-2,2], d in [-4,4].
Enumerating the k = 5 box and bucketing by H therefore enumerates
every shell 0..5 completely. This replaces any assumed search box;
that the found units happen to lie in [-2,2]^4 is an output, checked
against the exposed target, not a premise.

## 2. Coset minimum reduction

Let ybar = (0,0,3,1) and consider
C = {y in L Z^4 : y = ybar (mod 5)}. Every y in C is y = Lx for a
unique x in Z^4 (L is injective, det L = 25), and the Canon adjoint
identity gives H(Lx) = 5 H(x) (independently rechecked by the verifier
on the whole enumeration box, and the matrix identities
L = (I-A_f)(I-A_f^2), Vinv*L = 5I exactly). Lx = ybar (mod 5) forces
x != 0, so H(x) >= 1 by section 1, and H(y) >= 5 on C, with equality
iff some unit seed x (H(x)=1) satisfies Lx = ybar (mod 5). Minimizers
of H on C correspond bijectively to least-shell preimages. The
verifier searches shells 1..5 in the complete boxes of section 1; the
first nonempty shell gives the exact minimum 5k and all minimizers,
not a lower bound from sampling. The frozen outcome is k=1 with the
single minimizer recorded in EXPECTED.txt, hence minimum 5, attained,
unique. No statement is made if the cap had been exhausted; that
branch was frozen in PREREG.md and did not occur.

## 3. Residue classification

The 25 gate residues are the mod-5 image of L; the verifier proves the
equality with the criterion set {r0+2r1 = r2+2r3 = 0} by exhausting all
625 residue classes of x. The unit list of section 1 is complete, so
grouping its Lu (mod 5) values over the 25 gate residues is the
complete classification: every multiplicity in EXPECTED.txt is exact,
including the five residues of multiplicity zero. No analytic shortcut
is claimed for the table itself; its completeness is sections 1 and
the finite residue exhaustion.
