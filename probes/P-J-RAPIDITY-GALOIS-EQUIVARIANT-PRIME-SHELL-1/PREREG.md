# P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / RESULT-EXPOSED /
PROOF-FIRST / NO FORMAL RUN YET**

This probe freezes one L1 arithmetic theorem package. It records no Canon,
Registry, Frontier, physical, analytic, or RH move. All formulas and finite
controls were already visible in non-canonical reconnaissance. The written
proof below is the theorem-grade evidence; the post-pin verifier is an exact
audit of that proof.

## Public identity, authority, and action layer

    probe:             P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1
    public claim lock: issue #578
    owner:             A. M. Thorn / delegated session 2026-08-26
    branch:            probe/P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1
    basis:             Public Canon v66, current public main abe931d3,
                       tag canon-v66, CONTENT_COMMIT 8f11ec18,
                       CANON SHA-256 76de4fb0..., 339260 bytes
    action layer:      L1 arithmetic only
    layer lift:        none
    authority:         none until a later sealed Canon fold

The target future row, if a later reviewed fold adopts it, is
J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL [T]. This probe itself changes no
public claim status.

## Falsifier first

The theorem package is falsified by one exact counterexample to any of the
following frozen statements:

1. the fixed eigenline is cross-labelled by the other residue root;
2. the integral two-point permutation module is a non-split sign extension
   and its sum/difference lattice has index two;
3. the odd subspace of the fixed-line algebra has rank one;
4. the Reynolds correction is unique inside the stated two-resolvent class;
5. the local product is squarefree;
6. the global group-ring lift has the stated support, augmentation,
   independent-local-relabeling invariance, involution invariance, exact
   coefficient l1 norm, or convolution formula;
7. the augmentation and constant-term readings of the partial sum are the
   stated arithmetic sums.

Two detector controls are mandatory. At p=11 the same-root label must fail:
E_4 is contained in the kernel of evaluation at phi=8 and is not contained in
the kernel of evaluation at phi=4. The unrefined scalar correction must retain
a nonzero coefficient 2-u-u^{-1} in every degree at least two. If either
control fails to fire, the detector is defective and the probe stops.

A verifier error, changed pinned byte, architecture disagreement, nonzero
exit, nonempty stderr, or stdout mismatch is an integrity STOP and is not a
mathematical counterexample. Thresholds and scope never move after the pin.

## The six frozen fields

    EQUATION
      The shell, integral extension, odd-rank-one lemma, local Reynolds
      identity, global group-ring Mobius lift, and augmentation/constant-term
      identities in the exact forms proved below.

    CODE
      probes/P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1/verify.py.
      Python standard library only; Fraction and integer modular arithmetic;
      sparse Laurent polynomials; no floating-point assertion or comparison;
      deterministic stdout; run from repository root.

    CARRIER
      F=Q(sqrt(5)), O_F=Z[phi], multiplication by phi on O_F/pO_F, split
      fixed-line pairs, the free abelian rapidity group supplied by the
      public SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T] row, and its rational
      group ring. The finite audit uses primes p<=997 and integers n<=5000.

    SYSTEMATICS
      (a) every orientation is auxiliary and every final local factor is
          invariant under independent relabelling of each split pair;
      (b) the global Galois C2 flips all pairs simultaneously and is not
          falsely used to force 2^{-|S(n)|};
      (c) Reynolds uniqueness is only inside the frozen rational span of
          the two oriented resolvents with constant coefficients;
      (d) public rapidity independence is used only to distinguish Laurent
          monomials, not to claim a Hecke character or analytic estimate;
      (e) the finite scan audits universal written proofs and is not their
          logical source;
      (f) all earlier executions were non-canonical reconnaissance and are
          not public evidence.

    THRESHOLD
      All seven printed gates must pass exactly; the two mandatory negative
      controls must fire; stdout must equal one committed EXPECTED.txt byte
      for byte; exit zero and empty stderr are required.

    LAYER
      L1 arithmetic only. No L2 manifold, L3 boundary, L4 support, L5
      stream, L6 measure, Haar, probability, physical, automorphic, zeta,
      or RH lift is made or consumed.

## 1. Fixed lines and the mandatory prime-ideal cross-label

Let

\[
F=\mathbb Q(\sqrt5),\qquad O_F=\mathbb Z[\varphi],\qquad
A=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

For a split rational prime p not equal to 5, let t and \bar t=1-t be the two
roots of X^2-X-1 modulo p, and define

\[
\mathfrak p_a=(p,\varphi-a).
\]

In the basis (1,\varphi), multiplication by \varphi is A and

\[
A(1,t)=t(1,t).
\]

Thus E_t=F_p(1,t). Evaluation at \varphi=\bar t sends this vector to

\[
1+t\bar t=1+t(1-t)=1+t-t^2=0.
\]

Both E_t and \mathfrak p_{\bar t}/pO_F are one-dimensional, hence

\[
\boxed{E_t=\mathfrak p_{\bar t}/pO_F.}
\]

This is the cross-label. At p=11, the roots are 4 and 8:
1+4*8=0 modulo 11 while 1+4*4 is nonzero modulo 11. Therefore the
same-root label is explicitly false.

Attach to the cross-labelled ideal its oriented rapidity r and put
c_t=2t-1. The unordered two-point shell is

\[
\mathscr S_p=
\{(E_t,\mathfrak p_{\bar t},r_{\mathfrak p_{\bar t}},c_t):
t\in\{r,\bar r\}\}.
\]

Branch exchange acts without choosing an orientation:

\[
(E_t,\mathfrak p_{\bar t},r,c)
\longleftrightarrow
(E_{\bar t},\mathfrak p_t,-r,-c).
\]

## 2. Finite-phi odd rank one

Let

\[
B_p=\mathbb F_p[t]/(t^2-t-1),\qquad \iota(t)=1-t,\qquad c=2t-1.
\]

For p not equal to 2 or 5,

\[
c^2=4t^2-4t+1=5.
\]

Every element of B_p has the form a+bt. The invariant and anti-invariant
conditions under \iota show directly that

\[
B_p^+=\mathbb F_p,\qquad B_p^-=\mathbb F_p c.
\]

The word subspace is essential: B_p^- is not an algebra because the product
of two odd elements is even. Consequently finite A-dynamics supplies exactly
one algebraic odd direction. The verifier audits equivalent representatives:
the eigenvector wedge, tangent-multiplier difference, Lefschetz weight, and
the restriction of 2A-I.

At p=5 the roots merge and c=0. At p=2 there is no fixed line over F_2 and
sign oddness collapses after extension because -1=1.

## 3. Integral sign extension and the forced local half

For one split pair let

\[
M_p=\mathbb Z e_{\mathfrak p}\oplus\mathbb Z e_{\bar{\mathfrak p}},
\]

with the involution exchanging the basis vectors. The sum map gives

\[
0\longrightarrow\mathbb Z_{\rm sgn}
\longrightarrow M_p
\longrightarrow\mathbb Z_{\rm triv}
\longrightarrow0.
\]

Its kernel is generated by e_{\mathfrak p}-e_{\bar{\mathfrak p}}. An
equivariant section of 1 would have to be an invariant vector
a(e_{\mathfrak p}+e_{\bar{\mathfrak p}}) with sum 2a=1, impossible over
Z. The change-of-basis matrix with columns (1,1) and (1,-1) has determinant
-2, so the sum/difference lattice has index two. After inverting 2 there is
one normalized invariant section,

\[
1\longmapsto\frac12(e_{\mathfrak p}+e_{\bar{\mathfrak p}}).
\]

The half is therefore forced locally. Globally, the factor
2^{-|S(n)|} is forced by local Euler multiplicativity and independent
relabeling of every split pair, an action of (C_2)^{S(n)}. The single global
Galois involution only flips all pairs simultaneously and by itself does not
force the product of local halves.

## 4. The frozen Reynolds correction

Let Gamma be the free abelian group generated by one auxiliary orientation at
each split rational prime, as supplied by the public rapidity-independence
theorem. Put

\[
R=\mathbb Q[\Gamma],\qquad u_p=[r_{\mathfrak p}],\qquad u_p^*=u_p^{-1}.
\]

The oriented split ideal-Mobius factor is

\[
\widetilde B_p(T)=(1-u_pT)(1-u_p^{-1}T).
\]

Freeze the correction class to

\[
a(1-u_pT)^{-1}+b(1-u_p^{-1}T)^{-1},
\qquad a,b\in\mathbb Q.
\]

Independent relabeling u_p<->u_p^{-1} forces a=b. Scalar augmentation u_p->1
must give (1-T)^{-1}, so a+b=1. Therefore a=b=1/2 uniquely in this class:

\[
\widetilde C_p(T)=
\frac12\left((1-u_pT)^{-1}+(1-u_p^{-1}T)^{-1}\right).
\]

Direct cancellation gives the universal formal identity

\[
\boxed{
\widetilde B_p(T)\widetilde C_p(T)
=1-\frac{u_p+u_p^{-1}}2T.
}
\]

No uniqueness is asserted among all symmetric formal series.

For comparison, the unrefined scalar correction leaves a tail:

\[
\frac{(1-uT)(1-u^{-1}T)}{1-T}
=(1-T)+(2-u-u^{-1})\frac{T}{1-T}.
\]

The coefficient 2-u-u^{-1} is nonzero in Q[Gamma], although augmentation
kills it. Thus scalar correction is not a squarefree refined lift.

## 5. Global group-ring Mobius lift

Define the local factors

\[
\sum_{k\ge0}\widetilde\mu(p^k)T^k=
\begin{cases}
1-\dfrac{u_p+u_p^{-1}}2T,&p\text{ split},\\
1-T,&p\text{ inert or }p=5.
\end{cases}
\]

For squarefree n let S(n) be its split prime divisors. Multiplication of the
local factors gives

\[
\boxed{
\widetilde\mu(n)=
\frac{\mu(n)}{2^{|S(n)|}}
\sum_{\varepsilon_p\in\{\pm1\}}
\prod_{p\in S(n)}u_p^{\varepsilon_p},
}
\]

and \widetilde\mu(n)=0 when n is not squarefree. This formula is invariant
under independently replacing any u_p by u_p^{-1}. It is therefore
orientation-free before scalarization.

Rapidity independence makes the generators u_p free, so the
2^{|S(n)|} Laurent monomials above are distinct. Consequently

\[
\operatorname{aug}\widetilde\mu(n)=\mu(n),\qquad
\widetilde\mu(n)^*=\widetilde\mu(n),\qquad
\|\widetilde\mu(n)\|_1=|\mu(n)|.
\]

For an independent convolution construction, let \widetilde b have local
factors

\[
(1-u_pT)(1-u_p^{-1}T),\quad 1-T^2,\quad 1-T
\]

at split, inert, and ramified primes respectively. Let the Reynolds correction
have prime-power coefficients

\[
\widetilde c(p^k)=
\begin{cases}
(u_p^k+u_p^{-k})/2,&p\text{ split},\\
(-1)^k,&p\text{ inert},\\
0,&p=5,\ k\ge1.
\end{cases}
\]

Then local multiplication proves

\[
\widetilde\mu=\widetilde b*\widetilde c.
\]

The notation correction is deliberate: \widetilde c is not claimed to be a
completely multiplicative character.

## 6. Augmentation and constant-term readings

Let

\[
P_N=\sum_{n\le N}\widetilde\mu(n).
\]

Augmentation commutes with the finite sum, hence

\[
\boxed{\operatorname{aug}P_N=M(N).}
\]

If n has a split prime divisor, every monomial of \widetilde\mu(n) contains
that free generator with exponent +1 or -1 and cannot be the identity.
If n has no split prime divisor, \widetilde\mu(n)=\mu(n) is scalar. Therefore

\[
\boxed{
\operatorname{CT}P_N=
\sum_{\substack{n\le N\\
n\text{ has no split prime divisor}}}\mu(n).
}
\]

This probe calls the second functional the constant term only. No Haar,
measure, probabilistic, physical, asymptotic, or uniform-in-N interpretation
is part of the claim.

## Exact verifier gates

The sealed invocation will be

    python3 probes/P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1/verify.py

The accepted verifier prints seven gates:

1. fixed-line census and mandatory cross-label for primes p<=997;
2. finite-phi odd-rank-one identities on every oriented split line;
3. integral sign extension and forced local denominator two;
4. unique Reynolds correction in the frozen class and local product through
   degree eight;
5. global lift through n<=5000 and independent convolution through n<=2000;
6. augmentation and constant term at four checkpoints through N=5000;
7. the scalar-correction tail breaker in degrees two through eight.

The universal conclusions follow from the written proofs, not extrapolation
from these bounds. The formal time budget is 120 seconds. The exact success
line is RESULT 7/7 ALL PASS.

## Disclosure and formal-run boundary

A larger internal non-canonical program was executed before this public lock.
It included these formulas, extra analytic experiments, a first expected-output
census typo, and its mechanical successor. None of that output is public
evidence and none is imported here. The accepted public verifier is a reduced,
newly named audit whose result is exposed by the proofs above.

Before the immutable public pin, static syntax inspection is permitted but no
formal gate execution is. The first accepted formal run occurs only after
PREREG.md and verify.py are committed, pushed, and read back from the remote
pin. Any post-pin change to either file consumes this probe identity and
requires a fresh successor.

## Non-claims

This probe does not select one orientation, derive a second odd direction,
use J residue orders as a universal selector, identify a Haar mean, construct
a Hecke character, invoke automorphic induction or Selberg-Delange, assert an
L-function, estimate any summatory function, mention zeta zeros as evidence,
prove or disprove RH, or move any result from L1 to L2-L6.

The wider arithmetic-analytic synthesis, fired J-order selector route, fixed
nonzero-mode analysis, and the open trivial-character transfer problem belong
to a separate NON-CANONICAL Note and are not dependencies of this probe.
