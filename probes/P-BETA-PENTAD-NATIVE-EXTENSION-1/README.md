# Intrinsic bracket pentad and native symmetry extension

**Formal L1 revalidation; NON-CANONICAL. No authority or status promotion.**
Original analytical work and integration: A. M. Thorn, Apache-2.0.
Issue: [#1481](https://github.com/mathorn1973/twist-j/issues/1481).
Authority: Public Canon v101 at `5f54015ed8361e3a64cb10894397020ddfadd104`.

The supplied bracket/pentad/counter package joins two existing mathematical
carriers through an explicit common five-element set and classifies an exact
symmetry-extension problem for the unchanged native machine. This package
preserves the useful new construction, credits existing results and supplies
a prospective public revalidation of the result-exposed targets.

## Mathematical content

1. For `beta(x,y)=B^-1(x cross y)` on `F5^3`, the fifteen projective directions
   of nonzero square **B-norm** partition intrinsically into five orthogonal
   triples. `Aut(beta)` acts faithfully as the full permutation group of that
   pentad. Its even-subset quadratic space is explicitly the four-bit carry
   form `e2`.
2. One signed integral permutation action `sgn(sigma) P_sigma` on `A4`
   realizes both the residual characteristic-five Lie action and the binary
   quadratic action. This extends the comparison diagram to all `S5`; it
   does not assert full `S5` commutation of the inherited integral Hodge
   operator with odd orientation-reversing permutations.
3. The homogeneous image of words in all five original generators on each
   same-base fiber is exactly `C2^3`, with bracket subgroup `C2^2`. The
   displayed missing involution `T` is outside that image. Adding `T` to
   `<A,Phi>` generates all 120 bracket automorphisms; adding it only to
   `<Phi>` generates order 12.
4. Every prescribed active-fiber `C in GL3(F5)` has a unique base-preserving
   full-state symmetry extension when the existing counter may be read.
   Across all five sheets, a single checkpoint-only extension of that same
   action exists precisely for the four `C_lambda`; only identity belongs
   to `SO(B,5)`. At most 24 externally supplied time contexts suffice to
   evaluate the whole linear lift action; this is an upper bound and
   supplies no autonomous context updater. These are different classes.

See [GEOMETRY_PROOF.md](GEOMETRY_PROOF.md) and
[NATIVE_PROOF.md](NATIVE_PROOF.md), with same-session reviews in
[GEOMETRY_REVIEW.md](GEOMETRY_REVIEW.md) and
[NATIVE_REVIEW.md](NATIVE_REVIEW.md). [IMPACT.md](IMPACT.md) records the
concrete consequences and remaining dependency. [PREREG.md](PREREG.md)
freezes the accepted checks and failure semantics.

## Attribution and result exposure

`Aut(beta)=SO(B,5)`, Killing `=2B`, the binary carry pentad, the `A4` residual
isometry and marked `A5` action are inherited. The universal sharp nine-step
sheet bound is also already in `TM-SHEET-SYNCHRONIZING-GRAPH`; the supplied
argument/witness is an exposition and input to the chart construction, not a
new synchronization theorem. [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json)
records exact current registry owners and the incoming archive hashes.

The submitted proofs and three exploratory JSON outputs were exposed before
this public pin. They are not blind predictions or retrospectively
preregistered runs. The original three audit implementations are retained
byte-identical after static review; their old output files are not formal
inputs or expected results. The new `verify.py` executes those pinned sources,
checks their semantic certificates and independently solves the finite-field
linear constraints for the complete checkpoint-only matrix class.

No scientific execution is asserted by the source-preparation text. The
first formal stdout, neutral execution record and conservative conclusion
belong in separately committed `EXPECTED.txt`, `RUN.md` and `RESULT.md`
after complete-source publication and immutable-ref readback.

## Revalidation

After that gate, from the repository root:

```sh
python3 -B probes/P-BETA-PENTAD-NATIVE-EXTENSION-1/verify.py
```

The verifier uses exact integers and the standard library. It refuses
optimized Python, performs no network or subprocess calls and writes only
stdout. Supplied output JSONs and the live numerical campaign are not read.
The finite `n=0..31` chart checks and `n=0..4095` entrance census are bounded
audits; the written proofs establish arbitrary-counter claims. Public CI
will replay this accepted verifier on x86_64 and aarch64 against the same
newly captured output. Successful execution is not asserted until recorded.

## Boundary

The bridge transfers structures and actions between carriers of sizes 125
and 16; it is not a state bijection. It chooses no five-cycle, orientation,
native bit encoding, physical gate or decoder. A commuting symmetry is not
an original generator word. The time window used to evaluate an extension
is supplied by the existing counter; autonomous context updating is a
separate question. Neither native `U` nor a lossy context update is made
reversible by this symmetry construction. Canon, live physical obligations,
the running DP5 attempt and the deferred ion experiment remain unchanged.
