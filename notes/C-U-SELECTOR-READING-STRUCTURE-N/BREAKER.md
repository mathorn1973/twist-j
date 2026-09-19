# Independent breaker record

Status: NON-CANONICAL. L1 candidate audit PASS. No public status promotion.

The frozen contract is `PREREG.md`, publicly pinned at
`c083513a8f00ea1f66a72c54e7e1c8e24bb3342e`. Both implementation sources were
publicly pinned and remotely byte-read-back by the coordinating session at
`b13fb785c43143115087b01de9c9495b5b264b76` before this run. The breaker source
hash was supplied to that session before execution; static compilation alone
preceded the public source pin. The source was unchanged before and after
execution.

## Independence and exposure

The breaker was independently implemented from the frozen contract and the
canonical native coordinate formulas. It did not open the builder's
`verify.py`, `PROOF.md`, `SELECTOR.md`, execution outputs, or the verifier for
`P-U-J-HODGE-SEPARABLE-COUNTER-READ-1`. No builder result comparison occurred
before this record was written and hashed.

The prior prediction of thirteen components, one size 625 and twelve size
1250, all five trace values in each component, and the proposed
`F_5^2/{+/-1}` classification had already been disclosed. This is an
implementation-independent adversarial check, not blind discovery.

## Frozen source and execution

```text
source: break.py
source bytes: 15915
source SHA256: 91fc6713d17025a3deeaf82cf606138381ed0f7bbb897cc1eca3d8432a1e446f
source pin: b13fb785c43143115087b01de9c9495b5b264b76
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
Python: 3.12.14
LC_ALL=C
LANG=C
TZ=UTC
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
timeout: 120 seconds
scientific executions: 1
exit code: 0
stderr bytes: 0
stderr SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout: BREAKER-EXPECTED.txt
stdout bytes: 967
stdout SHA256: 6e83664aa0536bf21c0d373b9780e347b03e00199702a5d0590c836683351b5b
```

From the repository root, the scientific command was equivalent to:

```sh
env LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 -B notes/C-U-SELECTOR-READING-STRUCTURE-N/break.py
```

A standard-library subprocess wrapper imposed the 120-second timeout and
captured stdout, stderr, and exit code before evaluating success. It wrote
`BREAKER-EXPECTED.txt` only after exit zero and empty stderr were established.
All scientific arithmetic uses exact integers, including modular arithmetic;
there are no third-party dependencies or floating-point comparisons.

## Attacks and results

- The native graph was constructed from all 15625 six-tuples and their two
  selected transitions. The graph traversal uses adjacency sets and BFS,
  never the proposed invariant. Its complete vertex-set partition equals the
  explicit Q-fibre partition. Merely obtaining thirteen components would not
  have passed this test. The size histogram is one 625 and twelve 1250.
- All five native generator trace laws and involutions were checked on the
  full carrier. Every selected edge preserves Q. All 25 oriented kappa
  values have 625 preimages, 125 on each initial trace sheet. The sign-class
  sizes and every individual trace-sheet intersection agree with the frozen
  targets.
- A separate restricted BFS recovers the registered 313 terminal R fibres
  exactly. Every terminal edge reverses the oriented V value.
- The H bridge uses a trace-three seed x and the undirected path
  `d(x), x, a(x), d(a(x))`. The G bridge uses a trace-zero seed x and the path
  `e(c(x)), c(x), x, a(x), c(a(x)), e(c(a(x)))`. Every consecutive pair is
  checked against actual selected graph edges. The latter uses
  `k=1+2*r(x)`; its terminal starting coordinate is `s=r(x)+1`, so this is
  exactly `k=2*s-1`. Every oriented terminal V admits all five k values.
- All 9375 transient states have the explicit checked escape into X14.
  Every `G_k H` displacement agrees with the contract, and their exact
  additive closure equals the complete 25-element kernel of the two-sum
  projection.
- All 25 two-coordinate values were checked for quadratic collisions.
  Equality occurs exactly up to simultaneous sign. The thirteen image
  matrices have rank at most one; the twelve nonzero members give six
  projective directions with two matrices in each direction.
- The trace tables and the three-step reset were checked on all heads.
  The four terminal-sheet/control-bit cases verify the induction step for
  the registered all-n trace law. This is not an extrapolation from a finite
  time prefix. The Q-versus-initial-trace incidence relation contains every
  one of the 65 pairs.
- The distinct-Q heads `(0,0,0,0,0,0)` and `(0,0,0,0,1,4)` have the same
  initial trace. Closed deterministic trace evolution therefore gives the
  same complete trace and selector histories for them. At n=3 every head
  has the same current trace and index. These are direct information-loss
  witnesses for the frozen selector-only reading class.
- Selector augmentation one differs from the `I+C^2` sum augmentation two
  over both integers and F_5. On the augmentation lattice the exact J
  matrix and its exterior square both have determinant one. A deliberately
  chosen assignment of six coordinate vectors and zero supplies a
  nonconstant six-spanning source map with seven output values; it is a
  choice, not a preferred native amplitude assignment.

No scientific violation, code failure, or integrity failure occurred. No
threshold or frozen source was changed after execution. The finite audit is
one-architecture candidate-C evidence and does not satisfy a formal public
two-architecture gate. The all-n reader obstruction still uses mathematical
induction and injectivity of the target iterate, and the connectivity claim
uses the explicit bridge and kernel argument. No physical selector,
preparation, occurrence law, characteristic-zero source lift, or L2-L6 claim
follows from this record.
