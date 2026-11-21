# Odd-head blocks: exact bounded replay specification

**Status: NON-CANONICAL reproduction proposal.** The analytical identities
and explicit witnesses were derived before this integrated replay was
written. This is not a blind discovery experiment. The code and this
specification must be publicly pinned and read back before the first
execution of this verifier. No numerical search is authorized before
that pin.

`PROOF.md` supplies the integer identities and constructions.
`MEASURE.md` supplies the local Haar product laws, exceptional-set
analysis, coefficient expectations and logarithmic cocycle. Infinite
expectations, independence of an infinite code, almost-sure limits and
statements quantified over all positive inputs are proved there, not
inferred from the finite checks below.

## 1. Conventions and independent representations

For positive odd n, let T(n) be the odd part of 3n+1. Write

$$
n+1=2^k u,\quad
t=v_2(3^k u-1),\quad
m=B(n)=T^k(n),\quad
m+1=2^{k'}u'.
$$

Each call to the verifier's block routine computes B by exactly k actual
accelerated steps. Each such step performs the addition and then counts
successive integer divisions by two. The closed block formula does not
produce this actual endpoint. Independently, valuations used in the
closed formulas are extracted from the least significant one bit.

The actual valuation word must be k-1 copies of one followed by t+1.
The endpoint, head equation and inverse must satisfy

$$
m=\frac{3^k u-1}{2^t},\qquad
2^{t+k'}u'=3^k u+2^t-1,\qquad
u=\frac{2^{t+k'}u'-2^t+1}{3^k}.
$$

Both branch coefficients and positive affine corrections are checked
with cleared integer denominators:

$$
2^{k+t}m=3^k n+3^k-2^k,\qquad
2^{t+k'}u'=3^k u+2^t-1.
$$

The signs of m-n and u'-u are compared with the corresponding exact
cleared numerators. Rational products and partial expectations use
`fractions.Fraction`. All other arithmetic is integer arithmetic.
The only imports are `Counter`, `Fraction` and `product` from the Python
standard library. There is no floating point, randomness, input file,
network access or scientific dependence on the runtime environment.

## 2. Fixed inventory

All bounds are inclusive. No adaptive expansion is part of this replay.

### A. All small odd inputs and their joint cylinders

For every odd n from 1 through 65535, check the actual block, its entire
valuation word, both heads, the inverse, both affine identities and
their signs. This is 32768 starting values.

Put s(x)=popcount(x) and c_in(x)=2s(x)-s(3x). For every one of these
inputs also check

$$
3\mid u'\iff t\text{ is even},\qquad
s(3^k u)=s(u')+k',
$$

$$
c_{\rm in}(3^k u)
=c_{\rm in}(u')+k'+1
 -\mathbf1_{t\ge2}v_2(3m+1),
$$

$$
s(u')\equiv c_{\rm in}(3^{k-1}u)+k'\pmod2.
$$

Count joint cells with k,t,k' each in 1,...,4 and u' in each of the eight
odd residue classes modulo 16. For every cell, the required exact count
among odd representatives modulo 2^16 is

$$
2^{16-k-t-k'-4}.
$$

There are 512 cells. The largest required modulus is exactly 2^16, so
even the smallest cells have one representative in the declared input
range. Cells with a larger depth in any of the three coordinates are
outside this census, but their starting inputs still receive the block
and carry checks.

### B. Conditional head cylinders

For each fixed k=1,...,8 and every odd u=1,...,4095, construct
n=2^k u-1 and compute its actual block. Count t,k'=1,...,4 together
with each odd u' residue modulo 16. Each cell must have exactly

$$
2^{12-t-k'-4}
$$

representatives. This gives 16384 starting heads and 1024 conditional
cells. No distribution of k is assumed in this check.

### C. Integer inverse triples

For every k,t,k'=1,...,6 and every odd u'=1,...,255, test whether

$$
3^k\mid2^{t+k'}u'-2^t+1.
$$

If divisible, reconstruct the positive odd u and n and require the actual
block to have exactly that triple and target head. Independently compute
the unique admissible odd residue of u' modulo 2*3^k. Its arithmetic
progression gives the count of admissible u' in [1,255]; compare this
count with the explicit enumeration for each triple.

There are 27648 candidate triples-with-target-head. The aggregate number
of valid inputs is printed from the run. No uncomputed aggregate count
is prescribed or guessed in this specification.

### D. Fibers with fixed block output

For each k=1,...,6, construct the exact residue cycle of two modulo 3^k.
Require its length to be D=2*3^(k-1), with every unit residue appearing
once. For each positive odd m<=63 not divisible by three, find the
unique least positive t_0<=D satisfying

$$
2^{t_0}m\equiv-1\pmod{3^k}.
$$

For t=t_0+jD, j=0,1,2, reconstruct u=(2^t m+1)/3^k and n=2^k u-1,
then require the actual block to output m with depths k,t. There are
126 fixed-output targets and 378 explicitly reconstructed inputs.

### E. Arbitrarily long growth construction, finite audited range

For every R=1,...,128, construct all R+1 states

$$
u_j=9^j2^{3(R-j)+1}-1,\qquad n_j=4u_j-1,
\qquad0\le j\le R.
$$

Check by actual block iteration that the first R blocks all have
(k,t,k')=(2,1,2), with both node and head increasing strictly. Their
affine rules are

$$
n'=(9n+5)/8,\qquad u'=(9u+1)/8.
$$

At j=R check the next block has k=2, t=3 and

$$
k' =1+v_2(R+1),\quad
m=\frac{9^{R+1}-5}{4},\quad
u'=\frac{9^{R+1}-1}{2^{3+v_2(R+1)}}.
$$

Both node and head must then decrease. Thus the audit covers exactly R
growth blocks followed by their specified contracting boundary, not an
unbounded positive orbit. For every j=0,...,R check

$$
v_2(u_j+1)=3(R-j)+1,\quad v_3(u_j+1)=2j,
$$

$$
v_2(n_j+5)=3(R-j)+3,\quad v_3(n_j+5)=2j.
$$

Also require the boundary head to equal the actual Mersenne block
output B(2^(2(R+1))-1), computed by its own 2(R+1) actual odd steps.
For the already included R=6, check the exact comparison
u_boundary=597871>u_0=524287: contraction from the preceding head is
not necessarily descent below the original head. At every growth block
and boundary, check the normalized scalar product formula for the node
and head coefficients using their exact two- and three-adic valuations.

Print the known small rows (R, start n, after-R n, start u, after-R u):

| R | Start n | After-R n | Start u | After-R u |
|---:|---:|---:|---:|---:|
| 1 | 59 | 67 | 15 | 17 |
| 2 | 507 | 643 | 127 | 161 |
| 4 | 32763 | 52483 | 8191 | 13121 |

### F. Finite words and their exact cylinders

Enumerate all 819 words of lengths one through three over the nine
symbols (k,t) with k,t in {1,2,3}. For a prefix of j blocks set

$$
L_j=\sum_{i<j}k_i,\quad D_j=\sum_{i<j}(k_i+t_i),\quad C_0=0,
$$

$$
C_{j+1}=3^{k_j}C_j+(3^{k_j}-2^{k_j})2^{D_j}.
$$

Here L is the number of accelerated odd steps, not the number of blocks.
Independently compose the elementary odd-step affine maps using
`Fraction`, expanding each block into k-1 depths one and a depth t+1.
Require the resulting coefficients to be 3^L/2^D and C/2^D.

Compute the unique odd cylinder representative

$$
r=(2^D-C)(3^L)^{-1}\pmod{2^{D+1}},\qquad0<r<2^{D+1}.
$$

For n=r+j*2^(D+1), j=0,1,2,3, require every actual block to match the
declared word and require the endpoint to satisfy the composition
identity. Also require r+2^D not to realize the same whole word. This
last check tests the necessary highest bit of the word cylinder.

### G. Sixteen-block traces

For each odd start n=1,...,1023, follow exactly sixteen blocks, including
fixed-point repetitions. There are 512 traces and 8192 blocks; no early
stopping rule or adaptive extension is used. At each prefix check

$$
2^{D_N}n_N=3^{L_N}n_0+C_N,
$$

$$
n_N<n_0\iff(2^{D_N}-3^{L_N})n_0>C_N,
$$

and the exact coefficient and actual-size identities

$$
\prod_{i<N}a_i=2^{k_0-k_N}\prod_{i<N}A_i,
\qquad
\frac{u_N}{u_0}=2^{k_0-k_N}\frac{n_N+1}{n_0+1}.
$$

Accumulate the head affine correction separately and require it to be
positive and to reproduce u_N exactly. Require the node affine
correction to be positive as well. No claim is made that all these
traces descend within sixteen blocks; the check is the equivalence
with the exact affine inequality.

### H. Exact finite moment sums

For M=1,...,64, independently sum the one-dimensional rational series
and compare with

$$
\sum_{r=1}^M2^{-r}=1-2^{-M},\quad
\sum_{r=1}^M r2^{-r}=2-(M+2)2^{-M},\quad
\sum_{r=1}^M4^{-r}=(1-4^{-M})/3,
$$

$$
\sum_{r=1}^M(3/4)^r=3(1-(3/4)^M),\quad
\sum_{r=1}^M(3/2)^r=3((3/2)^M-1).
$$

The rectangular partial sums for the coefficient first moments must be

$$
E_A(M)=(1-(3/4)^M)(1-4^{-M}),
$$

$$
E_a(M)=\frac{((3/2)^M-1)(1-4^{-M})^2}{3}.
$$

For M=1,...,6, independently enumerate all pairs (k,t) and triples
(k,t,k') in [1,M] to cross-check these products. These are
**unnormalized rectangular partial sums**, not expectations conditional
on all depths being at most M. Infinite expectations and the logarithmic
drift are proof-only; no floating logarithm or numerical limiting test
is part of the verifier.

### I. A head alone does not determine the next head

For u=1 and each odd k=1,...,31, require the actual block to have

$$
t=1,\quad m=(3^k-1)/2,\quad k'=1,\quad u'=(3^k+1)/4.
$$

The first three output heads are 1,7,61. This is a concrete finite
witness that retaining u without k does not define the same autonomous
transition.

## 3. Execution and preservation contract

Run only the publicly pinned source, with Python >=3.12, assertions
enabled, and no arguments:

```text
python3 verify.py
```

The precise interpreter version must be recorded. Do not use `-O` or
`-OO`; disabled assertions are rejected. No timing or machine data are
printed in scientific stdout. Success requires exit zero and empty
stderr. Preserve the actual first stdout before adopting it as
`EXPECTED.txt`; no expected file is fabricated from the known formulas.

The neutral record binds the public pin, verifier/specification hashes,
command, exact Python version, operating system, architecture, exit
code, byte counts and stdout/stderr hashes. This notes-only verifier is
not selected by the repository CI selectors for `probes/` and
`reproduce/`. Green required architecture jobs are repository-integrity
checks and must not be reported as scientific execution of this file.

Separately recorded scientific reproductions are allowed. Each must use
the same pinned verifier bytes and compare against the same expected
stdout. A claim of two-architecture scientific reproduction requires
successful such records on two distinct architectures; same-architecture
agreement or unrelated CI success cannot supply that claim.

Any failed assertion, unexpected stderr, nonzero exit or byte mismatch
must be retained. A source or scope change requires a new explicit pin
and new run evidence. No failure is silently converted into a passing
expectation. These finite checks establish no canonical promotion,
global Collatz convergence or divergent positive integer orbit.
