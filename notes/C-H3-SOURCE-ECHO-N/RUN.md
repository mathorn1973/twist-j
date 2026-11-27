# Informal exact audit

NON-CANONICAL. Issue #2117 froze A and B before calculation;
comment 7220694517 froze C before its late capture test.
The earlier #2116 recovery failure remains unchanged.
No thresholds or input families altered after computation.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The public Apache-2.0 source is imported unchanged and not copied
into this package. The alternate implementation uses its own
five-power cyclic arithmetic and independent local updates.
Memoization and precomputed matching edges in the primary audit
preserve the pinned local primitives and geometry exactly.

Initial execution: Linux aarch64, Python 3.11.2. Primary A,
B and C and alternate A, B and C all exited zero with empty
stderr. The three complete stdout pairs matched byte for byte.
All executed sources archived unchanged. The alternate algorithm
was written after the primary results and is result-exposed, not
blind independent review.

Exact executed source and original transcript SHA-256 values:
```text
2c2904a0fbb87db1d0eab0426ca7e4ba14f63f974dc7f76dee35eb6f5d6e3be5  verify.py
cccfce70e2c4add51ba9b5ee3731dede6c981c941599a9fc086eb3c0caa2dbca  raw_echo.py
546cc8a2731cdd9323c306ddf4a1e3581582da98ee8f245e14a0f697e3003d50  capture.py
75108c251aa0ef1f680493b811220a8ffe985634a637bfabbe0dd058868fe9a9  break.py
43647c0ba596797653ee940b2b6519fbd074fe4ab7515b33e2db10c01257985b  A.txt
83a3879a57fa20e6975f2dad47294f357854ff0d7caf673081e14d55dc2c3488  B.txt
d1ee6ba309418adcb85fb3105a592226357e2cb0fa388658703be493dcb92aab  C full stdout (regenerable)
```
Original C stdout: 17,448 lines, 853,921 bytes. The compact
C_SUMMARY.txt is obtained by the documented grep filter.
Its per-stock summaries retain all negative outcomes; the
unchanged exact full stdout hash covers every candidate line.
No formal scientific gate or registry/Canon change.

Compact summary SHA-256: 3509f3baeced4cfdc78fe4deebc38554ce32c4c1f0bc3ce1f448a63930e44caf

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 1538d88b873e41a24c6c980a79905ff05e476f3c and the immutable
public H3 source at the base were fetched as raw files. All eight
executed script, transcript and source SHA-256 values were checked
before execution. Primary A, B and C and alternate A, B and C passed
with empty stderr. Both full transcript pairs for A and B, and the
complete 853921-byte C transcript, match byte for byte and all
recorded hashes agree. The compact C summary also matches. This is
cross-architecture reproduction, not blind independent review or the
formal public scientific gate.
