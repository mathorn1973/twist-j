# Review response for the proposed common ENC4 closure

NON-CANONICAL. This response accompanies
[PR #1985](https://github.com/mathorn1973/twist-j/pull/1985).
The independent review returned a scoped PASS with seven nonblocking
observations on head 9b9d6bc4ca6d45a1c167eb1619911a720f12b244.
This supplemental material was developed after that review.
Its fixtures are a separate audit and were not part of the
reviewed head. The original scientific pin, proof and run records
remain unchanged.

- **N1.** The general claim rests on the written all-input
  argument. There is no Lean formalization. A finite reproduction
  tests its implementations on specified inputs.
- **N2.** The generator and checker share the auxiliary spectral
  routines. The supplement tests the observable quotient against
  directly derived dimensions and averaging matrices, and checks a
  size-two Jordan chain via its nilpotent part and nullities. This
  adds independent fixture expectations and does not replace the
  shared auxiliary implementation.
- **N3.** The supplement checks all admitted reduction forms on
  explicit fixtures, including initialized MSD blocking. An MSD
  transient example separates a strictly positive finite tail
  from an exact zero family. A two-dimensional box gives (3/4,1/4)
  when normalizing the mean, versus (1/2,1/2) when averaging the
  pointwise normalized values.
- **N4.** The supplement compares the complete set G against a
  separate pointwise oracle on the 192-case permutation surface
  and against the full four-vector set in a two-active-axis
  product. These comparisons remain bounded.
- **N5.** The supplemental entrypoint refuses to run with Python
  optimization enabled. The original assertion-based probe must
  continue to run without optimization, as recorded in its RUN.md.
- **N6.** The independent review did not perform online readback
  of the public issue pin or hosted receipts. Git records the later
  result commit at 2026-11-13 13:47:35 UTC, while RUN.md gives the
  exact-command Linux run start as 13:47:36.426317 UTC, a difference
  of 1.426317 seconds. The Linux run and Windows Git commit used
  different environments. Clock skew is possible, and the cause
  has not been established. The scientific source pin is recorded
  earlier, at 13:42:46 UTC. The original Git and run metadata are
  retained.
- **N7.** The modulus is an effective sufficient side-length bound.
  Its parameters are not canonical and can produce large bounds.
  There is no claim that the returned bound is the least valid one.

The [supplemental reproduction](../../reproduce/metro-enc4-review/README.md)
audits only common ENC4 fixtures. The scoped theorem and adoption
still require the separate reviewed Canon fold. The remaining
encoding obligation, reduction-equivalence classification, and
broader METRO obligations retain their existing status.
