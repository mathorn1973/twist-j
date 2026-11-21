# Local prospective audit specification

Candidate: C-UNWRAPPED-KINEMATIC-REFERENCE-N
Owner: ChatGPT-unwrapped-reference-review-20261030
Author: A. M. Thorn
Date: 2026-10-30
Status: NON-CANONICAL. Local draft only. No public reservation, public pin,
formal probe, independent review, promotion, or GitHub write is claimed.
Authority reference: public mathorn1973/twist-j main
at a193e389fb1ddb0bdc89165b015c95a17eb1e425, Public Canon v106.

## Scope frozen before this local execution

L1 state/operator mathematics in an explicitly declared comparison model,
plus an exact comparison of two integer lattice automorphisms. There is
no transport from native U, no L1-L6 lift, and no physical-admission claim.
The analytical reference uses m>0, hbar=c=1, H_m=L2(R,deta),
E=m cosh(eta), P=m sinh(eta), K=i d/deta,
X={E^-1,K}/2 and D={tanh(eta),K}/2.
The written proof, not finite tests, is the basis of analytical candidate-T.
All test fixtures and the conclusions were analytically exposed before the
pin. This is not a blind prediction or independent confirmation.

## Exact finite audit

The accompanying standard-library Python program will:
1. Use Fraction pairs for Q(sqrt(5)), with no floating-point arithmetic.
2. Check golden frames and their metric transfer on every ordered pair
   n,n' in [-8,8], with the exact matrices S_r and G_r.
3. Check Dirac diagonalization and v^2+q^2=1 on all 17 rungs, m=2.
4. Audit the momentum translation and mass-change Jacobian coefficients
   on all ordered pairs of those rungs. This is only an algebraic fixture
   check, not numerical integration and not a proof of self-adjointness.
5. Audit the exact common-rapidity comoving clock identity for m1=2,m2=4
   on all ordered pairs of those rungs. No same-momentum clock claim.
6. Check the exact 8/5 norm factor of the submitted incorrect mass map
   at tau=log(2), by change of variables, with rational arithmetic.
7. Verify M_J from multiplication by J in Z[j]/Phi5 and the unimodular
   matrix Q given in PROOF.md, with its integer inverse.
8. Verify Q^-1 M_J^5 Q=diag(-F^5,F^-5) and
   Q^-1 M_J^10 Q=diag(F^10,F^-10), F=((0,1),(1,1)).
9. Check unequal characteristic polynomials for positive block lengths
   1,...,9, and equality at 10. The proof of all block lengths is analytic.

## Failure and limits

An exact failed identity rejects that particular statement at its frozen
scope. The audit must not be silently changed after a failure. A software
or custody defect is an integrity failure, not a physical falsification.
There are no adjustable numerical thresholds.
Unitarity, domains, all-parameter statements, the clock cosine bound,
and Fourier asymptotics must be proved in PROOF.md; passing the finite
fixtures alone establishes none of them.

## Custody and later public work

Freeze PREREG.md, PROOF.md and verify.py by SHA-256 before executing verify.py.
Record actual stdout, architecture, Python version, exit code and stderr.
The one local architecture does not meet a public two-architecture gate.
A subsequent public submission needs a collision/reservation recheck,
public Git custody, independent review and the repository's required checks.
No existing pin or public probe is reused. No Canon file is modified.
