# C-J-ZERO-ROOT-N: prospective arithmetic audit

NON-CANONICAL / NO AUTHORITY. Public claim reservation: #2097.
Owner: A. M. Thorn / codex-zero-root-20261125.
Package: PROMO-C-J-ZERO-ROOT-N. Action layer: L1 arithmetic; no layer lift.
Basis: Public Canon v117, main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

## Frozen definitions

O = Z[j] = Z[X]/(1+X+X^2+X^3+X^4), J=1+j^2,
rho=j^2, ell=1-j, Delta=J-conjugate(J)=j^2-j^3,
s=sqrt(5)=-1-2j^2-2j^3. Here s is the named algebraic element.
R4=O/(5)=O/(ell^4); the last equality is an equality of ideals.
All state equalities are exact ring or quotient equalities. Phase indices are
cyclic in F5. No measurement, occurrence or physical equality is supplied.

For x in O and k=0,...,4 define D_k=2 Tr_(Q(j)/Q)(rho^k x).
L_k=(D_k-D_0)/5 is asserted to be an integer.
r_k=L_k mod5, r_0=0, and q_k=r_(k+1)-r_k.
For x in ell^2 R4, x=s(a+b Delta), a,b in F5. For an integral
representative of this class set F_k=D_k/5 mod5, if divisible.

The supplied conversation did not explicitly define Delta. This package fixes
the definition above. Any different original convention requires a separate
comparison, not silent substitution.

## Exposed proposed statements and audit questions

1. Exact integral identity 10x=sum D_k rho^(-k), and
   2x=sum_(k=1)^4 L_k rho^(-k).
2. If x=sum_(i=0)^4 n_i rho^i, coefficients considered modulo common
   integer shifts, then D_k=10n_(-k)-2sum n_i and
   L_k=2(n_(-k)-n_0). Hence the relative reader needs no trace oracle
   as an algebraic map. Its native implementation is a separate question.
3. The map x mod5 -> (r_1,...,r_4) is bijective on all 625 residues.
   Adding 5y changes no r. It generally changes F by a common offset.
4. On ell^2 R4, F_k=c+2bk+3ak^2. Any three distinct phases determine
   a,b,c; second cyclic difference is a and third is zero.
   With arbitrary lift offsets these words are RS[5,3,3].
5. The square-zero set is exactly ell^2 R4 and has 25 elements.
   The ideal sizes for r=0,...,4 are 625,125,25,5,1.
6. The interpolating polynomial for r has zero constant and degree
   <=4-r on ell^r R4. For nonzero states the degree is exactly
   4 minus ell-adic order. Puncturing the anchored zero gives
   [4,4-r,r+1] generalized Reed-Solomon words for r=0,...,3.
7. Adjacent differences q on ell^r R4 form RS[5,4-r,r+2]
   for r=0,...,3. For r=2, q_k=a k+(3a+2b).
   These distances concern independently observed q symbols.
   Errors propagated from a common source F are correlated and must
   not be credited with independent-symbol correction guarantees.
8. Raw quadratic F words admit recovery from any three coordinates
   and unique correction of any one changed coordinate. Adjacent
   linear q words admit recovery from any two coordinates and unique
   correction of any one changed coordinate. Anchored r words on
   ell^2 have distance three. A bad common anchor changes four r
   coordinates; preserve this control.
9. Hermitian pair H(x)=(x+bar(x),Jx+bar(J)bar(x)) on R_m=O/ell^m:
   proposed kernel ell^(m-1)R_m for even m, and zero for odd m.
   Prove this all-depth statement symbolically. Finite m=4 audit
   is supplementary, not a proof for all m.
   Proposed exact witness for x=ell*s:
   Delta*(x-bar(x))=5.
10. For purely declared multiplication by rho and J, verify
    q_k(rho*x)=q_(k+1)(x), q(J*x)=(I+T)q(x).
    Four consecutive q_0(J^n x) readings recover all x by binomial
    inversion; two suffice on ell^2. Neither the sensor nor this
    evolution is identified with the unchanged native U by this identity.

## Exact finite audit

The main new verifier uses four integral polynomial coordinates and exact
arithmetic only. Audit all 625 states in {0,...,4}^4, all five phases,
all four unit-coordinate lift directions and scalar lifts 0,...,4;
all 25 square-zero states, all 125 raw (a,b,c) words, all ten
three-phase sets, all ten two-phase sets for adjacent words;
all one-symbol substitutions (five positions, four nonzero errors)
for every raw and adjacent codeword; all five ideal layers and the
complete nonzero-word minimum distances. For code linearity, minimum
nonzero weight gives pair distance. Explicitly check inverse reconstruction,
cyclic finite differences, native augmentation identity, and J-intertwining.
The bound and exact formula, not numerical approximation, decide a claim.

A separate same-session checker may use five coefficients/cyclic convolution
and a different interpolation/decoding route. It must be written without
reading verify.py and frozen before comparison. This is a separate
implementation by a helper, not independent external review.

No original opponent script is available at preregistration. No claim to have
replayed or independently confirmed that audit is made.

## Failure and execution

A single exact counterexample rejects the corresponding proposed statement.
Record any wrong scope, coefficient, sign, distance or error model. Do not
modify frozen code to erase a failed result; a repaired successor must retain
the failed source and output with explicit cause. Theoretical extensions
found later are separately labeled and are not retroactive preregistration.

Commit and push this file before new arithmetic execution. Freeze each new
executable source by Git commit and SHA-256 before executing it. Static
syntax inspection is allowed. Record command, environment, stdout, stderr,
exit and hashes. Repository policy/Canon/ledger/gate checks use their existing
runners. This note does not run a sealed public probe or create a two-
architecture computation-grade public T claim. Written proofs are at most
candidate-T, finite audits candidate-C. Promotion is a later public fold.

## Original audit custody

The owner requested the original audit, authorship, four caveats and scripts
to be preserved under this directory. Retrieval currently supplies only a
contextual summary, not the original file or script bytes. That intake is
blocked pending source recovery. No reconstructed note may be attributed to
the unknown original auditor. The new audit and its provenance remain separate.
