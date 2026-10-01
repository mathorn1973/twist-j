# Replay the known finite-chain first-delivery audit

NON-CANONICAL / candidate-T by conditional proof / L1. Public authority is v95.
Reservation #1311; stacked dependency #1310 at
dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2.

The complete known proof and prospective replay protocol are in
notes/C-FIELD-FINITE-CHAIN-FIRST-DELIVERY-N/. The original Windows audit ran
before any public pin. Its exact sources and historical report are preserved;
new public runs establish reproducibility, not blind discovery or new
implementation independence.

verify.py validates literal SHA-256 hashes of the protocol, historical
package and inherited local-arithmetic/proof files. It then calls the
unchanged audit.py main once. That program evolves both generic-N full-state
representations, checks their equality against the closed formula, layer
invariants, both inverse identities, all declared cuts and occupied contents.
The predecessor's main routines are not executed. Assertions must be enabled.

EXPECTED.txt contains the seven already exposed local stdout lines with LF
endings,554 bytes, SHA-256
c77b74b795dfe030c8b3dde34a8ff3755e9659d0e03da8f14b5245600640a394.
The original LOCAL AUDIT PASS line is retained verbatim. The surrounding
repository runner's REPRODUCE PASS receipt is the new replay evidence.

From a clean public-pinned checkout:

```text
python3 tools/check_reproduce.py --base dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2
```

The existing runner enforces120 seconds, exit0, empty stderr and exact stdout;
the existing workflow runs it on x86_64 and aarch64. No tools or workflow are
changed. Only Python standard library and exact public files in this checkout
are needed. Scientific programs write no files and use no network.

The theorem covers all N>=2 and integer H(w)=1 by induction. The finite audit
retains its original scope and cannot substitute for that proof. Target return
at N+1 is an analytical conclusion, while connected execution ends at N.
