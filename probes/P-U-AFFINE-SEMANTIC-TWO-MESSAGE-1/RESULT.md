# Result: affine reading with a different preparation

PUBLIC / NON-CANONICAL / L1 / candidate-T. Issue #1542.
Author A. M. Thorn, Apache-2.0.

The open existence question under a common semantic blank, with arbitrary
joint preparation at absolute n=0, has an affirmative witness. All arithmetic
below is in F5. On the original unchanged native U, prepare

    r0=3(1+mu-lambda),
    E(lambda,mu)=(3mu,3,3mu,2,2-mu-r0,r0).

Use the fixed affine pair and fixed decoder

    X=a+b+c-d-1, H=2a+b+d+q+r-2,
    delta(X,H)=BLANK if H=0, otherwise PRESENT(H^2 X).

The actual first selected generators are g2,g2,g4. The raw observations are
(mu,0),(-lambda,3),(mu,0),(-mu,3); decoded meanings are BLANK,lambda,BLANK,mu.
For all later times the invariant 2ACz=mu, together with B=D=0, C^2=4 and
z^2=1, gives H^2 X=mu and H nonzero. This includes mu=0 and uses no division
by A. PROOF.md supplies the universal algebraic proof and exact support.

## Frozen falsification result

Public pin: 20c19576bba5382a45cb7acdfa9a76d3bf41ca67.
All six preregistered falsifiers survived the first default run, exit 0,
empty stderr; exact stdout is EXPECTED.txt and its receipt is RUN.md.

| Falsifier | First-run result |
|---|---|
| F1 actual dynamics and semantic prefix | PASS: 25 preparations, 225 checkpoints, 200 transitions |
| F2 exact tail and both controls | PASS: 100 states, 200 edges, actual cover at times 3,4,7,8 |
| F3 disjoint support and all meanings | PASS: 25 blank + 25 first + 100 tail = 150 states |
| F4 arbitrary-decoder separation | PASS: 9375 cross-label pairs; 25 codes; fibres 20x5 and 5x10 |
| F5 affine formulas and ranks | PASS: rank 2 for reader and preparation; all 15625 native points |
| F6 separately authored matrix implementation | PASS: exact agreement on all 150 labelled rows and 200 tail edges |

The six semantic classes each contain 25 states. Their raw image sizes are
5 for BLANK and 4 for each present message. The canonical sorted row digest is
47cea3f3a2775ada1a221f558cccfc4d38cbbae14a28d645e59e66fc8ffc6cb2.
The primary and separate implementations both know the formula and target;
this internal authoring-session check is not an external blind audit.
Required public architecture replays are pending when this receipt is written.

## Exact scope

For this alternative preparation family the minimum observation degree is 1:
the displayed pair is affine, while constant observations cannot produce six
meanings. The minimum number of F5 coordinates is 2: one coordinate has only
five values for six distinct meanings. No exhaustive row-space search is
claimed or needed for this affirmative witness.

This does not alter the fixed original 550-state family's affine impossibility
or degree-2 minimum in #1536/#1541. The contract here only equates decoded
BLANK meanings. In particular the second message is already present in the
initial raw pair (mu,0); the common-raw-ready obstruction in #1520/#1524 is
not contradicted. The reader accesses all six native coordinates. Preparation
and observation are affine; the arbitrary permitted decoder is nonlinear.

This is mathematical existence, with both messages in the joint preparation.
It establishes no physical detector, disjoint-sector transfer, new information,
later insertion, source clearing or energy law. The reported third audit of
#1541 was unavailable in this session and is not evidence for this result.
No old verifier, old proof, Canon v101 or required workflow is changed.
No merge, Canon promotion or release is authorized by this record.
