# Three-step local receiver event record

PUBLIC / NON-CANONICAL / candidate-T by conditional proof / L1.
Authority remains Public Canon v95. Reservation
[#1313](https://github.com/mathorn1973/twist-j/issues/1313).

This candidate adds a receiver-only cyclic permutation of three existing
matter-register arrangements to the first-delivery family of
[#1312](https://github.com/mathorn1973/twist-j/pull/1312).
For every N>=2 and every integer H(w)=1 in the declared preparation, the
fixed local reader first sees an event at N, stays 1 at N,N+1,N+2, then
first resets at N+3. Initial energy remains 41 and the full carrier has
32N-1 coordinates. Every single cut keeps the prepared receiver unchanged
for all time. This is a new five-layer law with an explicit stored phase
mechanism; it is not permanent, robust or optimal memory.

Read [PROOF.md](PROOF.md) for the universal result, [PREREG.md](PREREG.md)
for the prospective scope and resource contract, and REVIEW.md for static
adversarial review. Post-pin receipts belong in RUN.md and RESULT.md once
execution exists. The source pin alone is not a completed computation.

The two full-state adapters reuse hash-checked local arithmetic from #1310.
A separate closed-state oracle checks the complete prepared trajectory;
matched K=identity controls expose the old one-step record and target-cell
reset. No native-memory reader is assumed to compose with this carrier.

From a clean pinned checkout:

```text
python3 tools/check_reproduce.py --base 04fa72ca2506398bf47a64fe33aa024625bd4f9b
```

The [reproduction entry](../../reproduce/field-receiver-bounded-record-n/README.md)
uses the unchanged repository runner and two-architecture PR workflow.
This draft is stacked on #1312 at 04fa72ca2506398bf47a64fe33aa024625bd4f9b;
all dependencies remain noncanonical. No merge or promotion is authorized.
