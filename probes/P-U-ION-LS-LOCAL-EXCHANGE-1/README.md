# P-U-ION-LS-LOCAL-EXCHANGE-1

**NON-CANONICAL.** A prospective exact local construction audit for the
actual ion contact families `|s,1> -> |1,s>` and `|s,4> -> |4,s>` from
[#1363](https://github.com/mathorn1973/twist-j/pull/1363).
Reservation: [#1364](https://github.com/mathorn1973/twist-j/issues/1364).

The candidate uses a single fixed light-shift profile, one scalar intensity,
completed motional loops, and explicit 729 nm star-transition pulses.
Twenty predetermined permutations turn the same fixed-profile loops into
an equality phase. Three rotated equality phases yield each embedded pair
exchange; four such blocks and an explicit phase correction implement the
required local family. No arbitrary U(5) primitive, independent five-level
shift controls or direct D-D drive is assumed.

- [PREREG.md](PREREG.md): frozen target, execution and failure conditions.
- [MODEL.md](MODEL.md): admitted controls, phase frame, inherited motion,
  parameter conditions, finite time/drive-energy account and physical limits.
- [PROOF.md](PROOF.md): finite constructive derivation and compilation.
- [SOURCES.md](SOURCES.md): independent physical provenance.
- [verify.py](verify.py), [verify_independent.py](verify_independent.py):
  separate exact code paths, run only after the public preregistration pin.
- [REVIEW-PREREG.md](REVIEW-PREREG.md): static preregistration review.

The mandatory task is a local basis-label exchange. The candidate also
preserves coherence on each actual five-dimensional input subspace in its
fixed interaction frame, but is not required to realize full SWAP on all
25 pair inputs. Its bounds are 240 closed LS loops and at most 2923 star
carrier pulses per contact; they are not optimality claims.

Even a successful exact audit supplies only conditional reachability in
the frozen ideal model. It does not calibrate an actual device, bound its
physical error, prepare the inherited inputs, implement the conjugated
native evolution, protect the archive, or close the finite source/controller
account of the whole two-contact history. Canon v97, #1359's physical HOLD,
and #1361's same-dictionary exclusion remain unchanged.
