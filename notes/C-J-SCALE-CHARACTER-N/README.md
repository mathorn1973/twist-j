# J, scale branches and arithmetic characters

**PUBLIC line. NON-CANONICAL. All new derivations: candidate-D. No authority.**

Owner: ChatGPT-Astra-Sol-20261124-J-Scale-Character.
Author: A. M. Thorn <thorn@twistj.com>.
[Claim #2077](https://github.com/mathorn1973/twist-j/issues/2077).
Action layer: NOT_APPLICABLE, pure arithmetic.

The question is what the squared moduli of
$J_n=1+(J-1)^n$, $J=1+\zeta_5^2$, read from integer indices.
The investigation treats this as standalone arithmetic. The supplied note's
five-value identity is correct. It admits an integer-coordinate extraction
and fits a sharp classification of prime cyclotomic scale branches.

## The result

Write $A_q(n)=|1+\zeta_q^{2n}|^2$ for an odd prime $q$.
At five, with $t=j+j^{-1}$ and $A_5(n)=u_n+v_nt$,

$$
\chi_5(n)=\frac{A_5(2n)-A_5(n)}{A_5(2)-A_5(1)}=-v_n.
$$

The ratio is unchanged by replacing the primitive root $j$ by any of its
conjugates. The character and its multiplication law are derived from the
Galois action after the integer coordinate is extracted.

For arbitrary nonzero labels $a,b$ with $a\ne\pm b\pmod q$, the normalized
gap

$$
U(n)=\frac{A_q(bn)-A_q(an)}{A_q(b)-A_q(a)}
$$

is multiplicative on $\mathbb F_q^\times$ **if and only if $q=5$**.
This is stronger than uniqueness of the involution given by doubling.
For larger primes the general identity retains an automorphism:

$$
U(sn)=U(s)\,\sigma_s(U(n)).
$$

The positive scale products are also classified. Set

$$
G=\mathbb F_q^\times/\{\pm1\},\qquad
d=\min\{r>0:2^r\equiv\pm1\pmod q\}.
$$

A product of exactly $r>0$ nonzero-index squared moduli can equal one
exactly when $d\mid r$. This part is elementary: reduction at
$\zeta_q=1$ gives $4^r=1$ in $\mathbb F_q$, and
$A_q(g)=B(2g)/B(g)$, $B(g)=|1-\zeta_q^{2g}|^2$, telescopes around a
doubling cycle.

The full relation statement uses the classical Franz independence lemma:

$$
\prod_{g\in G}A_q(g)^{z_g}=1
\quad\Longleftrightarrow\quad
z_{2g}=z_g\ \text{for every }g,\qquad z_g\in\mathbb Z.
$$

Thus each relation uses a constant exponent on each cycle.
The generated group has rank
$(q-1)/2-(q-1)/(2d)$. At $q=5$ one two-cycle gives the familiar pair
$\varphi^{-2},\varphi^2$. Among odd prime conductors, no other case
has two distinct reciprocal branch values.

## Information, binary inputs and Thue-Morse

For the original fivefold reader, all multiplication probes $A_5(kn)$
together retain exactly the information in $\chi_5(n)$. A second probe
at any known nonzero additive shift recovers the full residue:

$$
n\equiv(2h)^{-1}\bigl(\chi_5(n+h)-\chi_5(n)-h^2\bigr)\pmod5.
$$

These observations remain periodic modulo five. Reading binary digits from
left to right requires exactly five states for $\chi_5(n)$, two for
$t(n)=(-1)^{s_2(n)}$, and ten for their joint output.

The already-recorded composition
$\chi_5(2^{s_2(n)})=t(n)$ and the direct comparison have different inputs.
The existing four-bit block identity specializes to

$$
\sum_{0\le n<16^m}t(n)\chi_5(n+h)=5^m\chi_5(h).
$$

For the shift matching the first four signs, $h=1$, the mean equals
$(5/16)^m$. The direct correlation tends to zero for all lengths, uniformly
in the integer shift, by an elementary aligned-block decomposition.

## General-prime boundary

The special role of five concerns a **raw difference of two branches**.
For every $q\equiv1\pmod4$, an alternating rational linear combination
of all $(q-1)/2$ branches gives the quadratic sign; its square is $q$.
The homogeneous linear combination is unique up to scalar and uses every
branch. For $q\equiv3\pmod4$, the real branch group has odd order and
admits no nontrivial sign character. This explains precisely what is
special about the single comparison at five.

## Evidence and reading order

1. [PROOF.md](PROOF.md): integer extraction, arbitrary-gap rigidity, exact
   product lengths, the full relation lattice, and general linear readers.
2. [OBSERVATION.md](OBSERVATION.md): information retained, exact additive
   inverse, minimal automata and the Thue-Morse specialization.
3. [SOURCE.md](SOURCE.md): pinned inherited statements and classical sources.
4. [REVIEW.md](REVIEW.md): same-session mathematical review and scope limits.
5. [SCOPE.md](SCOPE.md): ownership, prospective boundaries and exposure.
6. [PROMO-C-J-SCALE-CHARACTER-N.md](PROMO-C-J-SCALE-CHARACTER-N.md):
   review package and proposed next disposition.

The Gauss sum, the quadratic character, the two moduli and the basic
Thue-Morse block are credited to their earlier sources. No historical
priority or new public theorem status is asserted. The package contains
paper derivations and source review. No new scientific program was run;
repository checks and CI do not constitute numerical evidence for these
statements. No Canon status changes.
