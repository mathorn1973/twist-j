# Collatz valuation and carry: result-exposed replay specification

**Status: NON-CANONICAL reproduction proposal.** This specification and
`verify.py` describe a new integrated replay of results already derived
and inspected. They are not a blind preregistration and do not claim an
independent discovery. A public source pin must precede the first
execution of this integrated verifier. The mathematical proofs and the
finite replay have different scopes.

## 1. Definitions and arithmetic

For positive odd integers define

$$
v(n)=v_2(3n+1),\qquad T(n)=(3n+1)/2^{v(n)}.
$$

For nonnegative integers let s be binary popcount, and put

$$
c_{\rm in}(n)=2s(n)-s(3n),\qquad
c_{\rm total}(n)=2s(n)+1-s(3n+1),
$$

$$
Z(n)\iff n\mathbin{\&}(n\!\gg\!1)=0.
$$

Z(0) is admitted. This matters for the transformed power at exponent zero.
The separate statistic s(n AND 2n) counts initial overlaps, not all
propagated carries.

All arithmetic is exact Python integer arithmetic. The only imports are
`itertools.product` and `math.comb`, `math.gcd`. There is no floating
point, random input, network access, input file, environment-dependent
scientific parameter, or file write. Scientific stdout contains no time,
machine, architecture, directory, or commit identifier.

The columnwise adder independently adds n and 2n, with initial carry
zero or one. It reconstructs the sum and counts every outgoing carry.
Its results are compared with popcount defects. Small Kummer checks use
direct binomial coefficients, not the digit-sum formula to construct the
binomial valuation.

## 2. Fixed finite inventory

Every endpoint below is inclusive.

| Component | Fixed domain | Exact checks |
|:---|:---|:---|
| Carry representations | n=0,...,4095 | Both column adders; both popcount defects; c_total-c_in=v_2(3n+1); Z iff c_in=0 |
| Kummer witnesses | n=0,...,127 | c_in=v_2(binomial(3n,n)); c_total=v_2(binomial(3n+1,n)) |
| General binary tails | h=0,...,63, r=1,...,8; a=2h+1 | Both signs a*2^r +/- 1; independent column checks; closed popcount/carry formulas; the r=1 boundary |
| Actual odd inputs | All odd n=1,...,4095 | Actual T; exact inverse from output/depth; consecutive gcd and output gcd with six; one-step inputs to one; direction of the step |
| General n+1 blocks | The same 2048 odd inputs | Unique n+1=2^k u; all k prefix states and actual steps; exactly k-1 initial valuations one; exact boundary/output |
| General n-1 blocks | All odd n=3,...,4095 | Unique n-1=2^r u; all prefix states and actual steps; exactly floor((r-1)/2) initial valuations two; both boundaries; even-r common child |
| Mersenne family | k=1,...,128 | Actual prefix from 2^k-1; all tail formulas; final valuation; first-block sign relative to its start; last-prefix-state Z flags |
| Plus-one family | k=1,...,128 | Actual prefix from 2^k+1; tail carries; parity-dependent boundary; common child with 3^(q-1) |
| Step-five fixture | k=10,...,128 | First 1111 at m=5; Z positions {0,2,4} through m=5; separate exact k=10,11,12 boundary values |
| Golden powers | m=0,...,100000 | Z(3^m) and Z((3^m-1)/2), using exact repeated multiplication |
| Independent digit predicates | m=0,...,1024 | Both golden predicates compared with literal binary-string adjacency |
| Small powers and carries | m=0,...,16 | Independent column adder for 3^m |
| Admissible inverse pairs | Odd output b=1,...,255, 3 not dividing b; depth v=1,...,12 | Parity admissibility, positivity, exact actual valuation, minimal-depth preimage and its tower; 510 admissible pairs |
| Common-child towers | Odd p=1,...,255; j=0,...,6 | P_j(p)=4^j p+(4^j-1)/3; same child and valuation increased by 2j |
| Entrance divisibility | Odd d=1,...,255 | j=ord_(3d)(4); d divides A_j=(4^j-1)/3; T(A_j)=1 with depth 2j |
| Affine branch words | Length L=1,...,5; each v_i=1,...,4 | All 1364 words; closed constant compared with independent integer affine composition; positive integral candidates checked against their actual T itinerary |
| Modular offset fixture | x=0,...,4 | (3x+1)/8=x+2 modulo five: slope one does not imply a fixed point |

No adaptive search or extension beyond these domains is part of this
replay. The independent binomial and string checks deliberately have
smaller domains than the principal integer checks; their scope is not
silently enlarged.

## 3. Identities under audit

For n+1=2^k u, u odd, the audited block is

$$
T^m(n)=3^m u2^{k-m}-1\quad(0\le m\le k-1),
$$

followed by a step of depth 1+v_2(3^k u-1), with output
oddpart(3^k u-1). For a positive odd a and r>=1,

$$
s(a2^r-1)=s(a)+r-1,\quad
c_{\rm total}(a2^r-1)=c_{\rm in}(a)+r+1.
$$

The input carry is c_in(a)+r for r>=2. At r=1 it is

$$
c_{\rm in}(a)+1-v_2(3a-1)=c_{\rm in}((a-1)/2).
$$

For n>1 and n-1=2^r u, the audited block is

$$
T^m(n)=3^m u2^{r-2m}+1
\quad\left(0\le m\le\left\lfloor(r-1)/2\right\rfloor\right).
$$

For r=2q the boundary depth is 2+v_2(3^q u+1), and the output is
oddpart(3^q u+1). For r=2q+1 the depth is one and the output is
3^(q+1)u+2. For a positive odd a, plus-tail carry equals c_in(a) at
depth r>=2 and equals c_in(a)+v_2(3a+1) at r=1.

The exact common-child relation and its general prefix consequence are

$$
T(P_j(p))=T(p),\qquad v(P_j(p))=v(p)+2j,
$$

$$
T^q(2^{2q}u+1)=T(3^{q-1}u).
$$

The affine return of a branch word has

$$
2^K n_L=3^L n_0+C,\qquad
C=\sum_{i=1}^L3^{L-i}2^{v_1+\cdots+v_{i-1}}.
$$

For a positive integral cycle candidate the replay requires
D=2^K-3^L>0, D dividing C, and the actual itinerary from n_0=C/D
having exactly the specified valuations and returning to n_0. It does
not substitute a homogeneous congruence for the affine return.

Universal validity of these identities comes from the accompanying
proofs. A passing finite replay cannot supply that universal quantifier.
The proof's affine-center identity and logarithmic cycle inequality are
analytical statements; this integer replay does not numerically evaluate
rational centers or logarithms.

## 4. Known results being reproduced

These expectations were known before this integrated code was written.

- In the fixed exponent interval 0<=m<=100000, Z(3^m) holds exactly at
  m=0,2,4. For the transformed powers, with k=m+1, Z((3^(k-1)-1)/2)
  holds exactly at k=1,2,3,5,8 in 1<=k<=100001. Neither list is asserted
  to be exhaustive beyond its stated interval.
- The finite Mersenne last-prefix-state list for k<=128 is {1,2,3,5,8}.
  The case k=1 is the fixed point one. The first complete Mersenne block
  decreases its starting value at k=2,4,8, equals it at k=1, and increases
  it at the other tested k. The global version of this last sign
  classification has a separate proof; it is not inferred from k<=128.
- At 3,27,243, total input carry is respectively 2,5,6, whereas initial
  overlap count is respectively 1,2,4.
- At step five of the plus-one family, k=10,11,12 give states 61,487,973
  and input carries 4,7,6. The separated upper-block interpretation is
  therefore not extended across the two lower boundary cases.
- Among the 1364 declared branch words, the only positive integral
  cycles are the five repetitions of the fixed point one, with all
  valuations two. This is a finite word-box result, not a general cycle
  exclusion or a new lower bound on nontrivial cycle length.

The following fixed illustrations are also checked:

1. 13 is not Z but T(13)=5; Z is a proper subset of the contracting odd
   states above one.
2. 55 -> 83 -> 125 shows recurrence of a prime factor after one absent
   step, despite coprimality of consecutive nodes.
3. 255 -> 383 -> 575 -> 863 -> 1295 -> 1943 -> 2915 -> 4373 -> 205 has
   its first Z state at index seven. The final depth is six;
   (3^7-1)/2=1093 is golden although 3^7 is not.
4. 257 -> 193 -> 145 -> 109 -> 41 -> 31 -> 47 -> 71 -> 107 -> 161 -> 121
   is an exact path, with T(109)=T(27)=41.
5. The accelerated and ordinary orbits of 27 are followed to their first
   hit of one, with separate fixed caps of 1000 steps. They have 41 and
   111 steps and maxima 3077 and 9232. The ordinary orbit's odd
   subsequence must equal the accelerated orbit exactly.

The last two fixtures are supplementary arithmetic illustrations; they
add no claim about all starting values. The proof's elementary base
F(9)=3^9-1-36(2^9-1)=1286 is checked as well.

## 5. Public pin and execution contract

Before execution, publish and read back the exact source and this
specification at a full commit pin. Record their SHA-256 values. The
pin must identify the same bytes that will execute. Prior local
derivations and earlier separate audits remain result exposure; they
must not be described as a blinded validation of this integrated replay.

Run the pinned file with Python >=3.12, assertions enabled, and no
arguments. Record the exact Python version used. From the repository root:

```text
python3 -I notes/C-COLLATZ-BLOCK-CARRY-PRIME-N/verify.py
```

The command is independent of the current working directory when the
corresponding path to the pinned file is supplied. Do not use `-O` or
`-OO`; the verifier explicitly rejects disabled assertions. Success is
exit zero, empty stderr, and the complete stable scientific stdout. The
actual first stdout is retained and only then becomes `EXPECTED.txt`.
No expected-output file is fabricated from the anticipated results.

The neutral run record binds the public source pin, command, Python
version, operating system, architecture, exit code, byte counts and
SHA-256 of stdout/stderr.

This notes-only verifier is not selected by the current CI selectors for
`probes/` and `reproduce/`. The required architecture jobs check repository
integrity; their success must not be presented as scientific execution of
this verifier or as its two-architecture replay.

Scientific reproductions may instead be performed and recorded
separately. Each must identify the exact public source pin and verifier
hash, execute those bytes, and compare its stdout byte for byte with the
same retained `EXPECTED.txt`, with exit zero and empty stderr. A claim of
two-architecture scientific replay requires such successful recorded
executions on two distinct architectures. Same-architecture agreement is
a reproduction only, and repository CI success cannot supply a missing
scientific execution. None of these records grants canonical promotion.

Any failed assertion, cap, nonzero exit, unexpected stderr or byte
mismatch is preserved as a failed replay. It is not silently repaired or
converted into a passing expected output. Any source or scope change
requires a new explicit pin and new run evidence. Mathematical
interpretation of a failure must distinguish a false proposition from an
implementation error.

This replay makes no claim of Collatz convergence, no global
classification of golden exponents, no physical realization, no new
canonical status and no cross-layer inference.
