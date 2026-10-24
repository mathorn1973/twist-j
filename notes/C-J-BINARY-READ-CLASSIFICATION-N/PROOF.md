# Complete binary classification of periodic J-world readers

**Proposed analytical candidate-T, conditional on the exact finite audit;
NON-CANONICAL; L1.**

This proof is self-contained. Lemmas 1, 2, the construction in Lemma 4 and
the shape of Lemma 5 restate the arguments of draft pull request #1727
(PROOF.md, sections 2, 3, 4 and 6), specialized to two letters. Credit
belongs there, and no logical dependence on an unmerged branch remains.

## 1. Setting

O=Z[zeta_5] in the basis (1,z,z^2,z^3) with z=zeta_5. Every unit of modulus
exponent one has the form u=eps*zeta^a*phi^k with eps in {1,-1} and k in
{1,-1}. The two frozen units are:

- J=zeta*phi^-1 (eps=1, a=1, k=-1),
- phi^-1 (eps=1, a=0, k=-1).

No complex embedding of such u has modulus one: the moduli are
phi,phi,phi^-1,phi^-1. So u^n-1 is nonzero, R_n(u)=O/(u^n-1) is finite with
F_n=|N(u^n-1)| elements, T(x)=u*x is a permutation of R_n(u), and T^n=I.

A binary reader is a nonempty T-invariant S and a map f:S->{0,1} such that,
for x uniform on S, the n-word (f(x),...,f(T^(n-1)x)) is uniform on
{0,1}^n.

## 2. Lemma 1, fixed points

For d|n write u^n-1=(u^d-1)b with b in O. The kernel of multiplication by
u^d-1 on O/(u^n-1)O is bO/(u^n-1)O. The map y mod (u^d-1) -> b*y mod (u^n-1)
is an isomorphism onto it, because O is an integral domain. Hence
#Fix(T^d)=F_d. The number of states of exact period d is
P_d=sum_(e|d) mu(d/e)F_e, and the number of d-cycles is C_d=P_d/d.

## 3. Lemma 2, cycle criterion

S is a union of T-cycles. Take a cycle of length e. Its labels form a cyclic
sequence s of length e. Since e|n and T^e=I on the cycle, the n-word started
at T^j x is s rotated by j and repeated n/e times. If s has least period d,
then d|e, and the e starting points give each of the d rotations of one
necklace of least period d exactly e/d times.

Uniformity means every word has the same count c>=1, so |S|=c*2^n. A reader
therefore exists exactly when some c>=1 admits integers y(eta,e)>=0, for
necklaces eta of least period d and cycle lengths e with d|e|n, such that

```text
sum_e (e/d)*y(eta,e) = c       for every necklace eta,
sum_eta y(eta,e)    <= C_e     for every e|n.
```

Necessity follows from the cycle decomposition. Sufficiency: allot distinct
cycles as prescribed and label each by repeating its necklace word.

## 4. Lemma 3, three exclusions

- **L0.** |S|=c*2^n<=F_n with c>=1. If F_n<2^n there is no reader.
- **L1.** Let n be prime, F_1=1 and floor(F_n/2^n)<n. The constant words 0^n
  and 1^n are necklaces of least period one. Only cycles whose length
  divides n can serve them, so lengths 1 and n. A fixed point contributes one
  preimage and an n-cycle contributes n. There is a single fixed point, so at
  least one constant word receives none. Its count c is then a positive
  multiple of n, so c>=n, contradicting c<=floor(F_n/2^n)<n.
- **L2.** Let floor(F_n/2^n)=1 and F_1<2. Then c=1. A cycle of length e
  labelled by a constant contributes e preimages to that constant word, so
  each of the two constant words needs its own fixed point. That requires two
  distinct fixed points, but F_1<2.

## 5. Lemma 4, constructions

- **E1.** If P_n>=n*2^n, take c=n. Each necklace of least period d receives d
  cycles of length n, each giving n/d preimages per word. The number of
  n-cycles used is sum_(d|n) d*B_d=sum_(d|n) W_d=2^n<=P_n/n=C_n.
- **CERT.** The four assignments of PREREG section 3 satisfy Lemma 2. The
  audit checks this exactly.

## 6. Lemma 5, tail for modulus exponent one

Let u=eps*zeta^a*phi^k with k=+/-1 and rho=phi^2. Write
F_n=|s1^n-1|^2*|s2^n-1|^2 with |s1|=phi^(+/-1) and |s2|=phi^(-/+1). The
triangle inequality gives

```text
rho^n*(1-phi^-n)^4 <= F_n <= rho^n*(1+phi^-n)^4.
```

- For n>=2 we have phi^-n<1/2. Since rho>5/2 (because sqrt5>2),
  F_n>=rho^n/16>(5/2)^n/16.
- For every d>=1 we have F_d<=16*rho^d<16*3^d (because rho<3).
- A proper divisor of n is at most n/2, and there are fewer than n of them.

Hence, for n>=2,

```text
P_n >= F_n - sum_(d|n, d<n) F_d > (5/2)^n/16 - 16*n*3^(n/2).
```

Two integer inequalities finish the bound:

```text
(A)  25^n >= 512^2 * n^2 * 12^n   <=>   (5/2)^n >= 512*n*3^(n/2)
(B)  5^n  >= 32 * n * 4^n         <=>   (5/2)^n/32 >= n*2^n
```

(A) makes the subtracted term at most (5/2)^n/32. Under (A) and (B),
P_n>(5/2)^n/32>=n*2^n.

Both hold at n=31; the audit checks them as integers. The ratio
(25/12)^n/n^2 is nondecreasing for n>=3, because (1+1/n)^2<=25/12 there.
The ratio (5/4)^n/n is nondecreasing for n>=4. So (A) and (B) hold for every
n>=31. Therefore P_n>=n*2^n for every n>=31 and every unit of modulus
exponent one, and by E1 a binary reader exists there.

(B) fails at n=30, so 31 is the first horizon this argument reaches. It is a
sufficient onset, not a minimal one.

## 7. Theorem and proof

**Theorem.** A binary reader on R_n(u) exists exactly when n is not in
{1,5} for u=J, and when n is not in {1,2,3,4,5,7} for u=phi^-1.

**Proof.** For n>=31, Lemma 5 and E1 apply. For n<=30, the exact audit
computes F_d and P_n. For each n it applies one rule of Lemmas 3 and 4 to
these exact integers, in the frozen decision of PREREG section 2:

- the excluded horizons are decided by L0, L1 or L2;
- every other horizon is decided by E1 or CERT.

The theorem is therefore conditional only on the correctness of that finite
integer audit. break.py rechecks the audit by code-distinct paths:

- an independent count by traces and Newton identities;
- explicit quotient enumeration with exhaustive assignment search for n<=8;
- direct realization on the enumerated quotient for every positive n<=12.

## 8. Reading, not a further claim

J=zeta*phi^-1 and phi^-1 share the modulus exponent, the growth rate and the
tail. They differ only in their finite exceptions. The phase is invisible
to the exponent and visible to finite arithmetic.

## 9. Scope

The scope is a preparation-capacity statement for freely selected S and f
with a uniform start on S. It supplies no native-U sampler, Born occurrence,
apparatus, self-location, physical tick or layer lift.
