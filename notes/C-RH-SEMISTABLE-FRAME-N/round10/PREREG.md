# Round 10 prospective exact audit

NON-CANONICAL. No Canon authority or status promotion.

- Candidate: C-RH-SEMISTABLE-FRAME-N; existing alias C-RH-BK-CONCENTRATION-N.
- Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261123-R10.
- Claim: issue #2070; draft delivery: PR #2071.
- Public authority basis: 93c36089db57032a6cbca482ff62c95884567d0f.
- Round 9 continuation basis: f35ccbafa4089260e0e2225908ebac33cb6893e0.
- Read-only external source: leanprover-community/riemann-hypothesis at 40e56bab026552e089d7afcfeff08d2defb9c005.
- Action layer: NOT_APPLICABLE (classical local algebra and representation theory).
- Status ceiling: candidate-C for these executions; candidate-D for separate paper deductions.
- This is a fresh finite audit inside the same unsealed incubation item. All round 8 and round 9 frozen files and first-run records remain unchanged.

## 1. Object and boundaries

The actual split word-prime stabilizer has the embedding
i(C) = [[C, (w-Cw)/p], [0,1]], extended by identities to ambient dimension n.
Its integral stabilizer is the subgroup Cw=w mod p. The compact orbit of an ambient spherical vector is indexed by X=F_p^k minus {0}.

A and B test the exact double-coset geometry used to derive the compact orbit Gram formula. C tests its rank and lower eigenvalue. D tests the finite permutation representation on X, including its nontrivial central characters. E tests the linear stabilizer obstruction underlying the separate twisted-Jacquet vanishing argument.

These finite checks do not compute any automorphic row, any actual period, its L-value, or the concentration defect of the actual P_u. They do not prove the cited representation theorems, the p-adic function-space argument, or the global Fourier bridge. No Lean compilation is included.

## 2. Exact domain

Use only the Python standard library, integers and fractions. No floating point, randomness, network access, external packages or third-party mathematical code.

The seven ordered triples (p,k,n) are fixed:
(2,2,3), (2,2,5), (3,2,3), (3,2,5), (2,3,4), (2,3,6), (3,3,4).

They include adjacent and positive-gap models; they are finite audit cases, not asserted parameter values of the asymptotic RH construction.

For a rational matrix whose entries have denominators prime to p, reduction mod p means exact reduction using denominator inverses. The p-valuation of zero is infinity. No numerical singular values are permitted.

## A. Compact word-prime orbit

Put w=e_1 in dimension k and enumerate all M=p^k-1 nonzero vectors x in F_p^k, using representatives 0,...,p-1.

For each x let j be its first nonzero coordinate. Define C_x over Q by taking first column x, followed, in increasing coordinate order, by all standard basis columns except e_j. Its determinant is a p-adic unit. Set
G_x = diag(i(C_x), I_(n-k-1)).

For every ordered pair (x,y) require:
- G_x and its inverse have entries of p-valuation at least -1;
- G_x^{-1}G_y has determinant of valuation zero;
- for x=y the relative matrix is the identity;
- for x!=y, both p G_x^{-1}G_y and p G_y^{-1}G_x are p-integral and have rank exactly one after reduction mod p.

The last conditions certify Smith exponents (-1,0,...,0,1). Algorithms may use a structurally equivalent exact certificate, but must test both the matrix and its inverse and distinguish the diagonal pairs.

Prospective totals: 62 orbit elements, 920 ordered pairs, of which 62 diagonal and 858 off-diagonal.

## B. Full ambient lattice neighbors

For every triple above separately, enumerate all projective covectors a in F_p^n by normalizing their first nonzero coordinate to one. Put N=(p^n-1)/(p-1).

If j is the pivot of a, define the integral n by n matrix B_a by columns:
- column j is p e_j;
- column l, l!=j, is e_l-a_l e_j.

This is a basis of the index-p lattice whose reduction is ker(a). Require det(B_a)=p, and exactly N distinct normalized covectors.

For every ordered pair (a,b) require:
- B_a^{-1}B_b has determinant of valuation zero;
- the diagonal relative matrix is identity;
- off the diagonal, p B_a^{-1}B_b and p B_b^{-1}B_a are p-integral with reduction rank one.

Prospective totals: 290 neighbors, 21,614 ordered pairs, with 290 diagonal and 21,324 off-diagonal pairs.

## C. Rational compact Gram formula

For each of the seven triples and each z in {0,1/4,1/2,3/4,1}, set
a=(N z-1)/(N-1) and G=(1-a)I_M+a J_M.

Require:
- the diagonal entries are 1 and the off-diagonal entries are a;
- the eigenvalue on constants is 1+(M-1)a;
- the eigenvalue on the sum-zero space is 1-a;
- 1+(M-1)a >= (N-M)/(N-1) > 0;
- G has exact rank M when z<1 and exact rank 1 when z=1.

Compute exact rank or a complete exact determinant/eigenspace certificate. The two implementations may use different certificates. No claim is made that every tested z is a spherical Hecke parameter of a representation.

Prospective total: 35 Gram cases.

## D. Finite compact types

Exhaust the four groups GL_k(F_p) for (p,k)=(2,2),(2,3),(3,2),(3,3), by filtering all p^(k*k) matrices with exact finite-field rank. Require respective group orders 6,168,48,11232.

For each g let chi_X(g) be its number of fixed nonzero vectors. This may be obtained by direct permutation enumeration or by p^dim ker(g-I)-1.

For p=2 define chi_aug=chi_X-1.
For p=3 define
chi_plus=(chi_X(g)+chi_X(-g))/2,
chi_minus=(chi_X(g)-chi_X(-g))/2,
chi_aug=chi_plus-1.

Require integer character values and:
- every listed nontrivial character has exact squared norm 1 under the uniform sum over the group;
- its inner product with the trivial character is zero;
- for p=3 the inner product of chi_aug and chi_minus is zero;
- at the identity the dimensions of (trivial, augmentation, minus when present) are respectively (1,2), (1,6), (1,3,4), (1,12,13).

Prospective totals: 20,292 matrices considered, 11,454 invertible matrices retained.
This is a finite representation check over characteristic zero using integer characters, not a claim of semisimplicity over F_p.

## E. Stabilizer character obstruction

Use the three fixed (p,n) cases (2,4),(3,4),(2,5).
The block dimensions are (1,n-2,1). Let n_Q be the space of strictly upper block matrices, with possible nonzero entries only in positions
(0,j), 1<=j<=n-1, and (j,n-1), 1<=j<=n-2.

Define the linear functional chi(Z)=Z_(0,1)+Z_(1,n-1).
This corresponds to a lower-block character matrix A with A_(1,0)=A_(n-1,1)=1, so A^2 e_0=e_(n-1).

Enumerate EVERY nonzero proper subspace W of F_p^n, without duplicates. For every W require a Z in n_Q with ZW contained in W and chi(Z)=1. Equivalently, require chi to be nonzero on the kernel of the linear equations defining ZW contained in W. Either direct enumeration or exact linear-system elimination is allowed.

Require 65,210,372 subspaces respectively, for a total of 647.
The two terminal coefficients in this finite-field lemma have nonzero product. This is NOT reduction modulo the word prime of the p-adic character, whose incoming coefficient has valuation one. It tests the trace-annihilator algebra over a field only; the paper proof uses the nonzero p-adic product ell(z)=-T.

## 3. Failure rule

Zero failures are required for every individual assertion and every stated count. One false assertion, mismatch, timeout, exception, nonzero exit or any stderr is a failed run, preserved verbatim. No threshold, case, file or claim changes after the execution pin. No automatic retry.

A finite success is only the declared finite result. It neither upgrades the paper deduction nor establishes a global period-rank bound.

## 4. Blind authorship and execution custody

The coordinator first publishes and reads back this contract. The developer and breaker then write separate standalone programs from it. The breaker must not read the developer's code or outputs before freezing its own code. No scientific program may be executed or imported during authorship. Static syntax checks are allowed.

Before the first execution, publish both exact programs and read them back by immutable commit. Record their SHA-256 and byte counts. That second immutable commit is the execution pin. Each first run uses a clean worktree at that pin, the repository root as cwd, PYTHONHASHSEED=0, LC_ALL=C.UTF-8, and a 240-second subprocess timeout.

Public files:
- round10/verify_r10.py
- round10/break_r10.py
- round10/verify.stdout.txt, verify.stderr.txt, verify.run.json
- round10/break.stdout.txt, break.stderr.txt, break.run.json

Record platform, architecture, Python version, command, exit code, timeout flag, stdout/stderr bytes and SHA-256, and the immutable contract/code pins. Do not expose machine names or private infrastructure. Both runs here are one x86_64 architecture. Separately authored blind code from this session is not an external independent referee or a two-architecture gate.

Paper proofs and source reading precede the finite runs and are labeled separately. The previous rounds' fixed contracts, programs and receipts are not rerun or changed.
