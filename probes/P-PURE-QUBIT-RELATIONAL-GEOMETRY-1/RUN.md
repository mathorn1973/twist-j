# P-PURE-QUBIT-RELATIONAL-GEOMETRY-1 run record

Status: `VERIFIER TRANSCRIPT PASS / SCIENTIFIC FALSIFIER FIRED / PROBE CLOSED / CANON UNCHANGED`

## Authority and immutable initial pin

```text
public base:          64d92817e2f63912d20240e92c780e2ec389c526
preparation commit:   ad20a51455054bee98b11850a3bb3e32e6c68924
initial pin commit:   6cc6d2d8175dfeed2a59e8c910d07e33fe35be32
claim lock:           issue #428
branch:               probe/P-PURE-QUBIT-RELATIONAL-GEOMETRY-1
formal run UTC:       2026-08-19T07:01:51Z
```

The public remote was read at the exact pin before execution. Both returned
UTF-8 contents were byte-identical to the local files:

```text
file         bytes  SHA-256
PREREG.md    16217  38d7da88b9c433b26c35f549f79966bbbeef76b5843c608dac19c271a03ddd3c
verify.py     9790  725b227e97b4c79a135151eb291f3a8a89c06cbb1adcdd1c494c5f08623cc90b

Git blob PREREG.md  b50d339f45763262515d5e874cd4301ced214b59
Git blob verify.py  73b6c49259606667e727b90704e5cd22d8d6156e
```

No formal verifier gate ran before that readback. The only pre-pin check was
`ast.parse` on `verify.py`, without import, compilation or execution.

## Accepted command and environment

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-PURE-QUBIT-RELATIONAL-GEOMETRY-1/verify.py

platform:       Ubuntu 24.04
architecture:   x86_64
Python:         3.12.13
arguments:      none
stdin:          none
```

## Local exact result

```text
exit code:       0
stdout bytes:    1469
stdout SHA-256:  26560ebffd68dc7b079bdd479bd1053a1e9f3a26327672c8696c6169d49f995e
stderr bytes:    0
stderr SHA-256:  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
EXPECTED bytes:  1469
byte comparison: stdout == EXPECTED.txt
last line:       RESULT PASS
```

All 16 gates passed. The exact audits covered 2,401 Gaussian-rational `2 x 2`
matrices and 69,888 Gaussian-rational two-row matrices across `n=2,3,4`.

## Post-run adversarial audit and STOP

At `2026-08-19T07:04:07Z`, before any result files were pushed, the independent
static science audit fired the frozen R1 falsifier. `PREREG.md` declares the
unhalved ambient tensor wedge

```text
u wedge v = u tensor v - v tensor u
```

but then states

```text
det(A A^dagger) = sum_(i<j) |u_i v_j-u_j v_i|^2 = ||u wedge v||^2.
```

With that declared convention, the last term is twice the minors sum. The
correct identity is

```text
det(A A^dagger)
  = sum_(i<j) |u_i v_j-u_j v_i|^2
  = (1/2) ||u wedge v||_tensor^2.
```

The verifier variable named `wedge_norm` computes only the minors sum, so its
PASS transcript does not audit the frozen equality. Additional integrity
defects were retained: the local-phase witness is unnormalized, breaker gate
labels do not match B1-B3, and the interpreter guard is broader than the
declared workflow environment.

No threshold, equation or code was changed after the pin. No rerun is
permitted under this probe identifier. A corrected attack requires a new
claim lock, branch, path, preregistration and verifier.

## Public workflow

Not used as scientific rescue. The repository workflow may reproduce the
verifier transcript, but byte agreement cannot repair a false frozen equation.
