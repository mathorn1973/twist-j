# RESULT — C-CURRENT-PRIME-GATE-N

**Verdict:** PASS at the frozen NON-CANONICAL scope.
**Scientific ceiling:** candidate-T for the written theorem package; candidate-C for the finite audit.
**Canon:** unchanged.

## Result

The frozen theorem package survives.

1. In a \(D\)-dimensional hypercubic plaquette carrier, one edge has exactly
   \(2(D-1)\) incident plaquettes.

2. For a ternary plaquette chain \(n_p\in\{-1,0,1\}\) with
   \(\partial n\equiv0\pmod p\), the current
   \(j=\partial n/p\) is unit-capacity whenever \(p>D-1\), and identically zero
   whenever \(p>2(D-1)\).

3. Hence the local nontrivial unit-current window is
   \[
   D-1<p\le2(D-1).
   \]
   At \(D=4\), its unique odd prime is
   \[
   \boxed{p=5}.
   \]

4. At \(D=4,p=5\), every charged edge has exactly five occupied plaquette
   incidences out of six, all with the same boundary sign. There are twelve
   local charged incidence words: six possible missing plaquettes times two
   current signs.

5. The already public \(n_D\) construction realizes nonzero unit current
   globally for every stated separation \(D\ge3\). The frozen finite audit
   reproduced the formula for \(D=3,\ldots,12\).

6. Every finite divergence-free unit current decomposes into edge-disjoint
   oriented simple cycles.

7. For every exact augmented surface component \(K\),
   \(J_K=\partial\eta_K/5\) has zero total homology on \(T^4\). Individual
   winding cycles may occur in a chosen decomposition, but their winding
   vectors sum to zero within \(K\).

## What failed to appear

No theorem of probabilistic independence between cycles appears. Neutral
matched surfaces can connect several current loops into one augmented
component. The exact covariance therefore remains a component sum, not an
Euler product.

No physical selection theorem for \(p=5\) is claimed. The result says that the
already selected \(p=5\) is uniquely compatible, among odd primes, with the
four-dimensional ternary **nonzero unit-current** window.

## Prime relation

The strongest exact relation found here is local and structural:

\[
\boxed{
D=4
\quad\Longrightarrow\quad
2(D-1)=6
\quad\Longrightarrow\quad
3<p\le6
\quad\Longrightarrow\quad
p=5
}
\]

for odd prime \(p\) under the frozen ternary current carrier.

Primitive current cycles can later be organized with dynamical-zeta or Möbius
language only if a multiplicative activity or determinant law is proved.
Nothing here supplies such a law for the interacting full current measure.

Issue #1193 is separate arithmetic Möbius/divisor work and is not evidence for
this result.

## Remaining target

The photon program now has a better structural reduction:

\[
\text{whole augmented component}
\to
\text{unit current cycle system with zero total winding}
\to
\text{bound the component functional without splitting its neutral weight}.
\]

The next quantitative target is a uniform bound on the whole-component current
moment, not another isolated loop geometry.

Full \(\Xi_L\), \(P1\), the positive \(b-25\chi\) margin, the massless phase
and the physical photon remain open.
