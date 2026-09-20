# Independent mathematical break review

P-ENTROPY-MEASURABLE-OBSTRUCTION-1. Candidate-T, NON-CANONICAL.
A. M. Thorn; original text Apache-2.0.

This review was completed before the public pin. The reviewer read the
public generator formulas and the proof in
`probes/P-ENTROPY-LAW-REDUCTION-1/PREREG.md`, independently checked the
proposed all-measurable argument, and authored `break.py` without reading or
importing the accepted `verify.py`. No scientific code was executed for this
review. A subsequent formal run record must name the public pin and cannot
be inferred from the review verdict below.

## Scope and verdict before execution

The reviewed argument excludes every measurable solution of the forced
native r-coordinate equation on the frozen product source. It does not
assume a finite cylinder, a continuous reader, a particular initial orbit,
or the uniform target pushforward. Consequently, if its stated premises
hold, it excludes the entire registered measurable equivariant class and
hence also the smaller class satisfying Law_W.

Verdict of this written break review: the all-measurable argument survives.
This is a mathematical review, not a formal finite-audit PASS and not a
Canon promotion. The finite audit below cannot establish its universal
quantifier.

## 1. Forced coordinate and tower signs

The existing public law-reduction proof forces

    z(P(kappa,y)) = 4 + 2 kappa[-1] (mod 5).

Thus the four driver pairs select e,b,b,d respectively. Their r maps are
`1-r,-r,-r,1-r`, giving

    r(S kappa,J y) = 1_{kappa[-1]=kappa[0]} - r(kappa,y).

Use the aligned two-level tower `kappa=mu(b)`, with `mu(0)=01`,
`mu(1)=10`. Its three relevant bits are

    kappa[-1]=1-b[-1], kappa[0]=b[0], kappa[1]=1-b[0].

Writing `d=b[-1] xor b[0]`, the first equality indicator is d and the
second is zero. Therefore two steps give `r'=r-d`. With `q=-r`, the
induced equation on the normalized even tower is exactly

    q(S b,J^2 y) = q(b,y)+d (mod 5).

The tower is the usual recognizable TM substitution tower. Its two
levels partition the TM system and have probability one half. Pulling the
normalized aligned-level probability back by mu gives the unique TM
probability, so the induced source remains the product of TM probability
and additive Haar probability. No conditioning correlates the two factors.
Almost-everywhere equations are restricted to a common invariant conull
set before this induction.

## 2. The auxiliary clock is explicit

Adjoin an independent uniform `u in Z/5`, advanced by one at each induced
step. This is a proof enlargement of the source, not an assertion that the
original source supplied a clock. Existence on the original source would
imply existence on this enlarged source by ignoring u.

Define beta uniquely by

    beta mod 5 = 3q-2u,       beta mod 2 = b[-1].

Both congruences then give

    beta' = beta+3d-2 (mod 10).

The modulo-five clock term is essential. Omitting it would identify a
different cocycle. The CRT signs and all 100 local cases are audited in
`break.py`; the displayed calculation establishes them without execution.

## 3. Exact identification with the substitution extension

Let B(n) be the alternating sum of the binary digits of n, with the units
digit positive. Its base-four recurrence is

    B(4n+i)=B(n)+(0,1,-1,0)[i].

Thus B modulo ten is the one-sided fixed point starting in zero of

    sigma(j)=(j,j+1,j-1,j),       j in Z/10.

Incrementing an integer changes its trailing block of ones. If that block
has even length, B increases by one and binary digit parity flips. If it
has odd length, B decreases by two and binary digit parity is unchanged.
Consequently, for every n,

    B(n+1)-B(n)=3(theta(n) xor theta(n+1))-2.

Reduction modulo two sends sigma to the square of the TM substitution.
Hence its two-sided subshift projects onto the TM subshift. The local
increment relation above holds on the entire substitution subshift,
because it holds on every legal adjacent pair. Conversely, over any TM
point this relation determines a lift from its initial letter. There are
at most five initial letters of its prescribed parity. At least one lift
exists by the onto projection. Adding 2 to every letter preserves the
substitution language and supplies all five distinct lifts. Therefore
there are exactly five lifts, not merely five observed in a finite orbit.

This gives a topological identification with the skew extension whose
coordinate beta has parity `b[-1]` and increment `3d-2`; the index shift by
one is explicit and harmless. For the modulo-five fiber coordinate t the
map is

    E(b,t)=(S b,t+3d-2).

The substitution is primitive: in five substitution levels the allowed
increments 0,+1,-1 reach every residue modulo ten from every letter. It is
aperiodic because it has the aperiodic TM system as a factor. Its unique
invariant probability is invariant under the commuting vertical addition
of 2. On each five-point fiber that action is transitive. The conditional
fiber probability is therefore uniform. In the displayed coordinates the
invariant measure is exactly `m_TM times uniform(Z/5)`. This justifies the
measure identification used by the spectral argument.

No assertion about exceptional fibers of the dyadic odometer is needed.
The exact five-point count is over TM itself. The dyadic factor needed
below is already a factor of TM.

## 4. Main spectral argument: repeated words

The main argument does not require a classification of substitution
spectra. Set `L=4^k`. In `sigma^(k+1)(0)`, the first and fourth blocks are
the identical word `sigma^k(0)`, each of length L, separated by `3L`.

Write nu for the unique substitution probability. For every positive
integer N, the probability

    (1/4^N) sum_{i=0}^{4^N-1} (S^i sigma^N)_* nu

is shift invariant: the sum telescopes under shift, using
`S^(4^N) sigma^N = sigma^N S` and invariance of nu. Uniqueness therefore
identifies it with nu. Vertical addition of 1 commutes with substitution
and preserves its language, so uniqueness also gives `nu[x[0]=0]=1/10`.

Let A be the event that the radius-m window agrees with its translate by
`3L`. For `x[0]=0`, each shift `i=m,...,L-1-m` in the averaged measure
puts both windows inside the two identical blocks. Hence, for `L>2m`,

    nu(A) >= (L-2m)/(40L).

This bound does not require that these events for different i are
disjoint: it sums separate positive contributions in the measure identity.

Suppose `F o S = eta F` is a nonzero measurable eigenfunction. Ergodicity
allows normalization to `|F|=1` almost everywhere. Choose a radius-m
cylinder function g with `||F-g||_2<epsilon`. On A the two values of g
agree. The triangle-square bound and invariance of nu therefore give

    |eta^(3L)-1|^2 nu(A) <= 4 ||F-g||_2^2.

For any fixed epsilon and its corresponding m, the lower bound on nu(A)
tends to `1/40` as k grows. Then epsilon can be made arbitrarily small.
It follows that `eta^(3*4^k)` tends to one. This is a statement about
every measurable eigenfunction, obtained from L2 approximation; no finite
coding radius is assumed for F.

Only a restricted set of eigenvalues will arise from the auxiliary
source in Section 6. If the order of eta divides `2*5^a`, its powers
lie in a finite set. Convergence to one forces exact equality for all
sufficiently large k. Since 3 and 4 are coprime to 5, the order of eta
then divides 2. Thus only `eta=1` or `eta=-1` is possible in the
source-required set.

Both eigenvalues already occur in the TM base: the constant function
gives 1 and the two-level substitution tower gives -1. Pullback to the
five-point extension preserves these eigenfunctions in the fiber constant
sector. Ergodicity makes each eigenspace one dimensional. Consequently no
nontrivial fiber-character sector contains an eigenfunction with order
dividing `2*5^a`. This is exactly the exclusion needed below.

## 5. Independent height and spectral crosscheck

The return of the initial symbol occurs at 3 because B(3)=0. It also
occurs at

    N=1+4+...+4^9=349525,

because B(N)=10, hence zero modulo ten. Since N is 1 modulo 3,
`gcd(3,N)=1`. These two returns force substitution height one. An extension
of the one-sided fixed point to the two-sided language suffices for these
return witnesses; the illegal boundary pair 00 need not be introduced.

The external spectral theorem is Dekking's classification for primitive
aperiodic constant-length substitution systems, including measurable
eigenfunctions. A primary source is:

[F. M. Dekking, The Spectrum of Dynamical Systems Arising from Substitutions
of Constant Length, prepublication version](https://www.numdam.org/item/PSMIR_1976___2_A6_0.pdf).
Use Section 2, Theorem 13, and Section 3, Theorem 7 and its proof
(printed pages 22-23 for the latter). The proof establishes that every
L2 eigenfunction lies in the odometer-times-height factor. The published
article is [Z. Wahrscheinlichkeitstheorie verw. Gebiete 41, 221-239
(1978)](https://doi.org/10.1007/BF00534241).

As an independent crosscheck, for length four and height one every
eigenvalue is dyadic. TM already
has the full dyadic eigenvalue group. Pulling its eigenfunctions back to
the five-point extension supplies each such eigenvalue in the fiber
constant sector. Ergodicity of the extension makes each eigenspace one
dimensional. Therefore every nontrivial fiber-character sector has no
eigenfunctions. This uses the measurable theorem, not just a maximal
topological factor claim.

This classification is stronger than the main argument requires and is
not needed for its conclusion. Section 4 of `PROOF.md` supplies a direct
uniform-word-frequency proof of unique ergodicity: the primitive
stochastic incidence matrix contracts letterwise oscillations, the
normalized boundary errors are summable, and decomposition into large
substitution blocks makes the resulting word frequencies uniform over
the subshift. This argument also survived the written break review. The
cited primary source states the corresponding standard fact in Section 1.7.

## 6. Pure point auxiliary factor and the contradiction

Multiplication by the unit J preserves each finite quotient of
`O_(K,lambda)` and its uniform probability. Functions on these finite
quotients form nested finite-dimensional invariant spaces whose union is
dense in L2 of additive Haar probability. Each restriction is a permutation
unitary. Thus J, J squared, and the product of J squared with the auxiliary
five-cycle all have complete countable eigenbases. Ergodicity of this
auxiliary factor is not required.

At depth m the residue ring has `5^m` elements and its unit group has
`4*5^(m-1)` elements. Lagrange's theorem gives the order of J squared
dividing `2*5^(m-1)`. Multiplication by J squared on the additive quotient
therefore has order dividing that number, including on nonunits. Adding
the auxiliary five-cycle only raises the power of five in this bound.
Every auxiliary eigenvalue has order dividing `2*5^a` for some finite a.
The countable eigenbasis can be chosen from finite-level invariant
spaces; no uniform finite depth is imposed on the assumed reader.

Put `omega=exp(2 pi i/5)`, `c(b)=3d-2`, and let

    f(b,y,u)=omega^(beta(b,y,u) mod 5).

An assumed solution gives `f(Sb,J^2 y,u+1)=omega^c(b) f(b,y,u)` and
`|f|=1`. Expand f in an orthonormal eigenbasis of the auxiliary factor.
At least one coefficient h in L2(TM) is nonzero. If its auxiliary
eigenvalue is lambda, then

    h(Sb)=lambda^(-1) omega^c(b) h(b).

On the five-point extension the function

    H(b,t)=h(b) omega^(-t)

therefore satisfies `H o E=lambda^(-1) H`. It is a nonzero eigenfunction
in a nontrivial fiber-character sector. Its eigenvalue has the restricted
order just proved, so it contradicts Section 4. This
argument applies to every measurable initial solution, independently of
any finite coding radius and independently of a target pushforward law.

## Finite break audit and limits

`break.py` independently audits affine generator-index compositions,
the four driver-pair cases, all tower and CRT cases, exact adjacent-pair
language closure, primitivity by graph reachability, the two sparse height
witnesses, and the five initial letters with their transitive vertical
action. It does not import or execute the accepted verifier.

These finite checks audit explicit premises. They do not prove
recognizability, unique ergodicity, the measurable repeated-word
inequality, L2 density of finite quotient functions, or the final
all-measurable quantifier. Those steps are the written proof. The named
external spectral theorem is an independent crosscheck, not a necessary
premise of the main argument. No empirical approximation to a spectrum
or a large finite search is substituted for these steps.
