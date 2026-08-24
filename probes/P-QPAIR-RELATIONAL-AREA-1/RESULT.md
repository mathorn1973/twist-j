# P-QPAIR-RELATIONAL-AREA-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`a7564e7f47ee4d7ff39b952554f5af3bf673bf22` (base `91e11e4`, Public Canon
v52, claim lock #424) was executed exactly once on native Linux/aarch64
after public remote readback. The verifier exited zero, wrote no stderr,
and produced the exact 4526-byte output recorded in `EXPECTED.txt` with
SHA-256 `cf07f330d7f39d2487171f59dd260b5dcbf8934d92f67f9858d2b1d06040f7fa`.
All fifty gates passed: the environment integrity gate, the generic
partial-trace, trace, determinant, norm, discriminant and Pythagorean
identities in eight variables, the kappa coefficient `(ad-bc)/2` on the
sixteen-dimensional reordered space with the slot comparison
`4 N(kappa_coef) = det rho_V`, the `zeta_5` phase witness, the generic and
exact local characters with local-unitary and scalar invariance of `A`, the
five integral area witnesses with their exact values, embedding order,
bounds and Galois-class indexing, the two discriminant witnesses, and the
14640-state pentit audit family (every area in `K+`, no bound violation).
No counterexample was emitted; no falsifier fired.

## Verdict

```text
QPAIR-DET-AREA-SLOT-COMPARISON  proposed [T]  written proof R1; 50/50 gates PASS
QPAIR-DET-AREA-PLACE-PAIR       proposed [T]  written proof R2; witnesses,
                                              bounds and pentit audit PASS
pentit REPORT lines             audit output only; no row, no status
QUADRATIC-DECODER-DATA          [O] / STOP, untouched
QDD-INSTRUMENT-APPARATUS        [O], untouched
```

For every field of characteristic not two with involution `c` and
two-dimensional `V, W`, the two typed slots carry two determinant forms: the
typed partial traces of `H(x)` are `X c(X)^T` and `X^T c(X)`, both with
determinant `N(D) = D c(D)`, while the antisymmetric line of the symmetric
slot carries `D/2`; the comparison `4 N(kappa_coef) = det rho_V` holds, the
discriminant identity `n^2 - 4 N(D) = (p-q)^2 + 4 z c(z)` holds, and on
`n != 0` the Pythagorean identity `beta_B + 4 A = 1` holds in `Fix(c)`. The
Hermitian form is invariant under the phase `u^2` (with `u c(u) = 1`) that
the symmetric form retains. No necessity, minimality, or informational
independence of the two slots is asserted.

For `K = Q(zeta_5)` and nonzero integral `x`, `n(x) != 0`, the area
`A = N(D)/n^2` lies in `K+ = Q(phi)`, its two real embeddings are indexed by
`F_5^x/{+-1}`, agree iff `A` is rational, and lie in `[0, 1/4]`. Exact
witnesses: `(1,0,0,1)` with `A = 1/4`, `(1,0,0,phi)` with `A = 1/5`,
`(1,zeta,0,1)` with `A = 1/9` (embedding-blind); `(1,1,0,phi)` with
`A = (10 + 3 phi)/121`, embeddings `(23 +- 3 sqrt5)/242`, and
`(1,1,1,1+zeta)` with `A = (26 - 9 phi)/361` (embedding-split, opposite
orders). The discriminant `6 + 3 phi` of `(1,1,0,phi)` has norm 45, not a
rational square, so the local eigenvalues leave `K+` while `N(D) = 1 + phi`
is integral; `(2,0,0,1)` has discriminant 9 and weights 4 and 1.

REPORT-only audit output over the pentit family `(mu_10 union {0})^4` minus
zero: 6640 embedding-blind and 8000 embedding-split areas, 1200 at `1/4`,
1440 at `0`, seven distinct values. These reports agree with the drafting
expectations exposed in `PREREG.md`; they are not fields of either target
row.

## Evidence

```text
PREREG.md    sha256 ca2c2ac707b900ace4b1b9e06d44a7fa2e760eeab720c04445ea1c0f8a04cfea  25543 B
verify.py    sha256 2b26d98781cd8e49118981ba6a1046ebc7c37e818f886adcd72a69a2abb340b2  24364 B
EXPECTED.txt sha256 cf07f330d7f39d2487171f59dd260b5dcbf8934d92f67f9858d2b1d06040f7fa   4526 B
```

The accepted local leg is the single formal execution on Linux/aarch64,
CPython 3.12.3, deterministic environment, exit zero, empty stderr, with the
raw stdout returned on issue #424 before this record was written. The
first clean GitHub Linux/x86_64 pull-request replay (pull request #426)
used the identical pinned verifier at tested merge commit
`c2ec4c00754fdbdd237b1c51f3e40acdf8a40a0b`: workflow run `32219985004`, job
`95968516655`, exit zero, empty stderr, `EXPECTED.txt` reproduced byte for
byte; the parallel GitHub Linux/aarch64 job `95968516518` replayed
identically and the aggregate check job `95968564806` passed. The
two-architecture computation gate is PASS.

## Scope firewall

The kappa line is a direction in the quadratic target, not a Bell state and
not the two-qubit singlet. "Area" names `A(x)`, an element of `Fix(c)`;
"embedding" means a real embedding of `K+`, and no gate depends on which
embedding is called principal. `F_5^x/{+-1}` is used as an index set only;
no edge to `QUBIT-FROM-F5` and no "hence a qubit" sentence is created.
`QPAIR-TRANSPOSE-FIBER-REDUNDANCY` is a wording precedent on its registered
`K^2` carrier, not a premise, and is not widened to the composite carrier.
The probe touches no rational `V_eff` or `QDD` object, states no bridge
between carriers, creates no `BELL-CAUSAL-ACCOUNTING` row, and makes no
mixed-state, CHSH, decoder, instrument, event-stream, measure, L2 to L6, or
physical statement. Issues #419 and #422 are non-canonical lineage, not
evidence or dependencies.

## Recorded decision

```text
run integrity:       PASS
counterexample:      NONE
result:              PASS
architecture gate:   PASS (local aarch64, GitHub x86_64, GitHub aarch64)
scope:               R1 and R2 of PREREG.md, layer L1, integral QPAIR carrier
status discipline:   the probe result stands at its evidential grade; the
                     registry rows QPAIR-DET-AREA-SLOT-COMPARISON and
                     QPAIR-DET-AREA-PLACE-PAIR and the Canon fold are a
                     separate sealed integer-versioned step and are not
                     made by this probe
```
