# Run custody

PUBLIC NON-CANONICAL candidate-C corroboration of candidate-T proofs.
Owner #1223. This is not a formal public probe or an independent-agent test.

## Frozen Git basis

pin_commit: 57ad7319ff06d3523eb84706a348727912264626
basis_main: 09ace5f4664392e007a353e822350c9e4d094783
prereg_blob: 199027171530a35ae5bbd91fb9b8253851d8caae
verifier_blob: 2d2ed82eb3dbff1936a2ebf1a3600cdcad5f7292

The preregistration and complete audit were committed before execution and
read back from that immutable commit through the public GitHub connector.
The source and both execution copies agree with the pinned Git blobs.
Author and committer of the pin: A. M. Thorn <thorn@twistj.com>.

PREREG.md SHA-256: 1321ed7937248cd99f51eb2ed0d9bcab7d1e3e2203c05a8f86550abe7f36b91f; bytes: 5774
verify.py SHA-256: babc344f3956f24a4a37b97b40a592f047443fe79657ba5c958d25124b27e23b; bytes: 7343

The inherited source is probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py,
SHA-256 02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9.
The audit rejects a different inherited-source hash before running it.

## Exact executions

Command from repository root on both architectures:

    python3 notes/C-HODGE-RANK4-SEAM-CANONICITY-N/verify.py

| Field | First execution | Second execution |
|---|---|---|
| Operating system | Linux | Darwin |
| Architecture | x86_64 | aarch64 (platform reports arm64) |
| Python | 3.13.5 | 3.9.6 |
| Exit code | 0 | 0 |
| Stdout bytes | 697 | 697 |
| Stderr bytes | 0 | 0 |

Both stdout SHA-256 values:

    c366bc20879d7e5470d8bf0b94604e0b8556f194fab5b7427decc3041cd7735d

Both stderr SHA-256 values:

    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Exact stdout (identical in both executions):

```text
PASS anchors: exact hash-pinned marked A4/J-Hodge reproduction
PASS blocked class: dim_F Hom(L^10,B^10)=12; maximum rank 4
PASS C5 map test: joint blocked/C5 Hom dimension 0
PASS C5 image test: two real-irreducible rotating target planes; no invariant rank-four image
PASS kernel test: periodic source splits into two inequivalent C5/Hodge planes
PASS target forms: exact block matrices; nondegenerate pencil restriction is (2,2), otherwise (1,1,2 zero)
PASS witnesses: same Hodge kernel, different images, h ranks 4/2 and wedge ranks 2/4
PASS direct quotient: rank-four orthogonal J/C5 projection onto E survives; Galois changes chart
NON-CANONICAL L1: no physical spacetime or photon conclusion
```

The code was unchanged between these executions. A separately authored
proof-aware review is recorded, but no blind second-agent confirmation is
claimed. Ordinary PR CI checks repository policy and the unchanged Canon;
its changed-public-probe selector does NOT execute this notes directory.
The two scientific executions above, not a green notes-only CI badge,
supply the recorded cross-architecture reproduction.
