# Independent mathematical and post-pin code review

Status: review supports candidate-T; public promotion remains a separate fold.

## Mathematical review

A separate mathematical agent reviewed both written bounds. The finite
covering beta*P subset sigma(D)+P is an actual set covering, its iteration is
valid, and planar area gives |A_n|>=phi^(2n) for all n>=0. The proof correctly
distinguishes positive real phi from sigma(phi) and does not assume that the
planar image of O is discrete.

The integral norm and four-dimensional volume packing give the upper bound.
The reviewer independently checked

    32(4phi^2+1/2)^2(4phi+1/2)^2 = 93890+41760sqrt(5).

No mathematical correction was required. The reviewer had been given the
constant-one target and a planar-covering route hint, but no author code or
proof details when first deriving the covering. This is independent
derivation with a hint, not an unhinted discovery or formal blind gate.

## Post-pin static review

A different agent read PREREG.md, PROOF.md and verify.py after the public pin.
It executed no verifier and changed no frozen file. Reviewed source SHA-256:

    3758ca321b5bdadc767bba10b3c35bece5f34e7cc2e5c74a2760954b7801026e

No blocking finding was identified:

- Exact rational-square ordering handles both signs and reflected scalar
  comparisons. Descending polynomial reduction computes the cyclotomic
  remainder correctly.
- The enumeration implements A_(n+1)=J*A_n+D. The boundary sample supplements
  the uniform analytical covering and is not used as an all-point proof.
- Fixed ASCII stdout and integer counts are independent of set iteration
  order. Only standard-library exact arithmetic is used. There is no random
  input, network, subprocess, external data or file write in the verifier.
- Assertions must remain enabled, as in the prescribed command.
- Full-alphabet cardinality remains distinct from native source completeness,
  endpoint probability, Shannon entropy and physical interpretation.

This second review is code-aware and is not described as blind confirmation.
The required architecture replays provide byte reproducibility, not a second
independent discovery of the theorem.

## Public safety

The named probe files contain original mathematical prose and Python code,
neutral platform metadata and deterministic scientific stdout only. No
credential, private infrastructure, private path, third-party code, binary
artifact or failed-run transcript is included. Apache-2.0 applies under the
repository policy. No existing probe or normative file is changed.
