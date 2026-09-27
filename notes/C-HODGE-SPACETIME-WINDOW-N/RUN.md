# Exact run record

PUBLIC NON-CANONICAL candidate-C reproduction. Owner: #1229.
Author: A. M. Thorn <thorn@twistj.com>.

## Public custody

pin_commit: 61c84ad6fecc35332f69ceaf7a8757d808e39d19
prereg_sha256: 1d987e7f6dae7d1f0b31990ae144a6ad5e719625503abd42d0567db56de75dfa
verifier_sha256: 86a4162ed7429db0be93b6633e70c99ecdbd7ca14cd42ae16c66188d910d7203
command: python3 notes/C-HODGE-SPACETIME-WINDOW-N/verify.py

Both complete files were publicly read back before first execution. The
first attempted remote push was denied before any scientific execution;
a properly authored public commit was then published through an authorized
Git connection. No failed scientific run or amended preregistration exists.
The second architecture obtained its input through Git at the same pin.

## First execution

platform: macOS
architecture: aarch64 (platform.machine reports arm64)
python: 3.13.13
exit_code: 0
stdout_bytes: 697
stdout_sha256: db0ab92fa432b0010d1c4ca2825d8f7d257d2f312aa65ae52cdacdb8c827c259
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Second execution

platform: Linux
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_bytes: 697
stdout_sha256: db0ab92fa432b0010d1c4ca2825d8f7d257d2f312aa65ae52cdacdb8c827c259
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Exact stdout

```text
PASS G1: real projector rank 4; rational-source rank 6, so no integer label is erased
PASS G2: 64-vertex window and covering constants; exact rounding fixtures=324
WINDOW_C0 Q5(4/5,2/5)
COVER_R Q5(10,-9/5)
PASS G3: inherited cone, future-preserving J/C5 action; geometric/order limit rests on written proof
PASS G4: direct J step has a spacelike displacement at an admitted timelike integer point
CLOCK_SEED 0,-1,1,0,-1,0
CLOCK_STEP_LENGTH_SQUARED 2
PASS G5: 40 exact integral cumulative-clock prefixes and chord identities
PASS G6: exact photon shell moments; rigorous rational null-sheet brackets=24
NON-CANONICAL: selected flat event geometry, not native physical spacetime or a massless phase
```

Both runs executed the same verifier, not independently authored proofs.
This is actual two-architecture reproduction of a noncanonical note, not a
formal public probe under the pinned Python 3.12 workflow procedure. Ordinary
notes-only CI does not run this verifier. Universal claims rest on PROOF.md.
