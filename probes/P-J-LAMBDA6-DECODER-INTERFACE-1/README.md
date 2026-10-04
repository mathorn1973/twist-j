# Lambda-six scalar interface and pure-J dynamics

`P-J-LAMBDA6-DECODER-INTERFACE-1` is a fresh L1 arithmetic probe, NON-CANONICAL until a separate fold. It completes exact encoding, inverse/image recognition and forward/backward data dynamics for

`D6(alpha)=(S(alpha),S(J alpha),alpha mod (1-zeta5)^6)`

on every nonzero scalar in `Z[zeta5]` with algebraic norm at most 941. The returned inverse includes the original scalar, its unique oriented-strip representative, its signed integer J exponent, and its norm. The old rational-modulus-25 probe is unchanged.

Read [INTERFACE.md](INTERFACE.md) for exact types and exceptions, [PROOF.md](PROOF.md) for totality and scope, and [PREREG.md](PREREG.md) for the frozen tests and failure rule. [SOURCE.json](SOURCE.json) pins the public mathematical inputs and discloses the previously exposed local bundle. The residue ring has `5^6` elements and characteristic 25; its six digits require carries and do not form the additive group of `F5^6`.

From repository root, the following commands use the coefficient basis `(1,zeta5,zeta5^2,zeta5^3)` and six least-significant-first canonical lambda digits:

```text
python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-1/decoder.py encode 1 0 0 0
python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-1/decoder.py decode 2 3 1 0 0 0 0 0
python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-1/decoder.py forward 2 3 1 0 0 0 0 0
python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-1/decoder.py backward 2 3 1 0 0 0 0 0
```

The first command encodes 1; the second returns original and strip coefficients `(1,0,0,0)`, exponent 0 and norm 1. The last two apply the exact data operators corresponding to multiplication by J and J^-1. They also act on syntactically valid readings outside the scalar image; decoding such a reading rejects it. Zero is excluded from the inverse domain. A changed valid reading that is another valid image is accepted, not classified as corruption.

After the public commit-and-push freeze, run the complete gate:

```text
python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-1/verify.py
```

The coordinator wrapper validates INPUTS.sha256 and runs the author audit in primary.py and the separately frozen independent_decoder.py. Both execute on both required CI architectures against one exact EXPECTED.txt. Before that public pin, only compilation and static review are permitted. The primary audit covers all normalized arithmetic trace/residue candidates, all 15625 residue classes, every strip scalar at seven signed exponents, exact boundaries, malformed/nonimage data, both data operators, and the exposed depth-five capacity certificate. No random sampling or floating-point arithmetic is used.

Depth six is the exact first injective and first 3125-capacity depth within the original ideal-reading sequence and the inherited omitted-time reader class; PROOF.md gives the norm separation and thirty disjoint collision pairs. Exact lower-depth census counts remain in their original separate record and are not rerun here.

The residue alphabet decreases from `5^8` to `5^6`; two unbounded integer traces remain part of the full datum. This is pure-J arithmetic, not native U dynamics, a source-controlled contact, physical acquisition, a preferred dictionary, or a claim of speedup or total apparatus savings.
