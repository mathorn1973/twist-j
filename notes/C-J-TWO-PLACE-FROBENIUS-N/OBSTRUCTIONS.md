# What the defect does not establish

NON-CANONICAL. New statements: candidate-D, L1.
All counterexamples below are proved algebraically, not reported as a
finite computational census.

## 1. A composite passes the entire Frobenius law

Let

\[
N=252601=41\cdot61\cdot101.
\]

Each prime factor is one modulo five, so the cyclotomic polynomial
splits completely and without repeated roots at all three factors.
Consequently

\[
\mathcal O/N\mathcal O\simeq
\mathbb F_{41}^4\times\mathbb F_{61}^4\times\mathbb F_{101}^4.
\]

Moreover \(40,60,100\) all divide \(N-1=252600\).
Every component therefore satisfies \(x^N=x\), including zero.
Thus

\[
x^N=x\quad\hbox{for every }x\in\mathcal O/N\mathcal O.       \tag{1.1}
\]

For \(5\nmid n\), let \(\sigma_n(j)=j^n\).
The correct universal prime identity is \(x^p=\sigma_p(x)\)
modulo a prime \(p\ne5\), not generally \(x^p=x\) on this extension.
Here \(N=1\bmod5\), so \(\sigma_N\) is the identity. Equation (1.1)
therefore passes the correctly twisted Frobenius law as well:

\[
x^N=\sigma_N(x)\quad\hbox{for every }x.
\]

All additive Frobenius identities follow. In particular
\((x+y)^N=x^N+y^N\) holds for every pair. Testing additional elements
or every additive relation in this same quotient cannot reject this
composite by failure of that law.

This does not show that the complete ring, its characteristic, or a
different decoder is unable to recognize compositeness.
It disproves sufficiency of this universal Frobenius property.
In the special factorization of PROOF.md it also implies
\(N\mid F_{(N-1)/2}\).

## 2. Exact universal criteria

For any integer \(N>1\) with \(5\nmid N\), put
\(f_p=\operatorname{ord}_5(p)\) for each prime divisor \(p\) of \(N\).
Then

\[
x^N=x\ \hbox{for all }x\in\mathcal O/N\mathcal O
\]

holds if and only if \(N\) is squarefree and

\[
p^{f_p}-1\mid N-1\quad\hbox{for every }p\mid N.             \tag{2.1}
\]

Necessity of squarefreeness follows already in the integer subring.
If \(p^2\mid N\), the integer \(N/p\) is a nonzero square-zero class
modulo \(N\), contradicting \(x^N=x\). The embedding of
\(\mathbb Z/N\) in \(\mathcal O/N\mathcal O\) is injective because the
integral basis contains one.
For squarefree \(N\), Chinese remaindering and unramified cyclotomic
splitting give products of fields \(\mathbb F_{p^{f_p}}\).
The cyclic multiplicative group of each field gives exactly (2.1).

There is also an exact criterion for the weaker condition that the
power map \(x\mapsto x^N\) be additive on the whole quotient.
It holds if and only if \(N\) is squarefree and, for every \(p\mid N\),

\[
N\equiv p^{a_p}\pmod{p^{f_p}-1}
\quad\hbox{for some }0\le a_p<f_p.                         \tag{2.2}
\]

An additive power map is unital and multiplicative and fixes the integer
subring, which again forces squarefreeness. In every residue field it
is a unital endomorphism, hence a Frobenius power, giving (2.2).
Conversely these Frobenius powers are additive.
On \(\mathcal O/N\mathcal O\), a unital endomorphism with the value
\(j^N\) at the generator is exactly \(\sigma_N\). Thus universal
additivity is equivalent to the correctly twisted universal identity.

The identity criterion (2.1) alone is not a necessary prime condition
at nonsplit primes. The distinction from (2.2) is essential.

## 3. The one-relation detector is not unique to one marked generator

In \(\mathbb F_{16}\), the eight unit exponents modulo fifteen split as
\(\langle2\rangle\) and \(-\langle2\rangle\).
Inside the first subgroup, the power map is Frobenius and preserves
every sum. Outside it, undoing Frobenius reduces the one-relation test

\[
(1+a)^n=1+a^n
\]

to inversion. For \(a\ne0,1\), inversion passes iff

\[
(1+a)^{-1}=1+a^{-1}
\quad\Longleftrightarrow\quad a^2+a+1=0.
\]

The values \(a=0,1\) pass as well.
The complete blind set is therefore the subfield \(\mathbb F_4\).
Every \(a\) outside that subfield detects the nongenuine coset.

At \(\mathbb F_5\), the nonidentity unit exponent is three.
Its relation defect is \(3a(a+1)\), which vanishes exactly at
\(a=0,-1\).

Hence the reduced product one-relation detector works for every \(a\)
with \(a_2\notin\mathbb F_4\) and \(a_5\notin\{0,-1\}\).
The marked value \(a=j^2\) satisfies both conditions.
This explains the exact mechanism without claiming a uniqueness
principle for \(J\).

## 4. The full residual is richer than the two flags

For unit exponents modulo fifteen, the nonzero defect at two equals
\(j^{n\bmod5}\). Indeed, in (3.2) of PROOF.md both
\(\phi^{-n}\) and \(h_a\) belong to the two-element set
\(\{\phi,\phi^{-1}\}\) in \(\mathbb F_4\). When they differ, their
sum is one. The full binary residual therefore has five possible
values: zero and four nontrivial fifth roots. The ramified field residual
has two values on odd exponents. Chinese remaindering gives ten
possible pairs of numerical residuals in the reduced two-place ring,
not merely the four pairs of zero/nonzero flags.

Both versions remain periodic modulo sixty. Neither retains a full
unbounded carry history. The all-sixty result uses the thicker
nilpotent quotient at five.

## 5. Equal finite readings, arbitrarily different ordinary carries

For \(k\ge2\), take

\[
n=2^{4k+1}-1,\qquad m=2^{4k}+15.
\]

Both have binary length \(4k+1\), and both are \(31\bmod60\).
Thus they have identical full defect residues modulo ten, even when
the bit length is supplied as additional context.
Yet addition of one propagates through \(4k+1\) trailing ones in \(n\)
and through exactly four trailing ones in \(m\).

Their binomial carry patterns also differ. In characteristic two,

\[
(1+T)^e=\prod_{i:e_i=1}(1+T^{2^i}),
\]

so the number of odd binomial coefficients in row \(e\) is
\(2^{s_2(e)}\). The two rows above therefore have respectively
\(2^{4k+1}\) and \(32\) odd entries.
These entries are also precisely the carry-free splits of \(e\)
into two nonnegative summands.

These are ordinary binary and binomial carries, explicitly named.
No equality with a physical or otherwise unnamed TWIST-J carry variable
is assumed. Growing precision, the unrestricted integer defect, and a
retained transition trace are different inputs from a terminal residue.
