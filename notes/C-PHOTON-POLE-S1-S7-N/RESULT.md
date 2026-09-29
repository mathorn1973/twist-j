# Result and limits: finite S2 component

**PUBLIC; NON-CANONICAL.** C-PHOTON-POLE-S1-S7-N under #744.  
**Written mathematical status:** candidate-T, conditional finite L4 algebra.  
**Finite audit:** candidate-C, six groups passed on one local architecture.  
**Formal independent acceptance / public two-architecture scientific acceptance:** NOT DONE.  
**Canon:** v91 unchanged. No S3-S7 or parent-gate closure.

## Outcome

TRANSFER.md proves an exact positive-transfer support description for every
spatial N>=2 in the explicitly selected fixed-weight model. The positive
support is M times the span of gauge-closed modulo-five ternary Fourier
fields. The normalized temporal insertion is supported within that
subspace and is bounded uniformly in N. One common unitary sends all scaled
electric insertions to the constrained values -1,0,1 and sends the transfer
to the explicit matrix (21). A 13-link finite witness separates modulo-five
Gauss closure from a real divergence-free law. The proposed S1-S7 draft's
normalized/unnormalized partition notation is corrected explicitly.

These claims concern the supplied transfer construction, not a derived
native U dynamics. No photon spectrum was computed or inferred from the
three electric values. The rank-two matrix in the audit is the separately
specified target only.

## Preregistration and exact audit receipt

Scope: #744 comment 5753406017. Source pin: comment 5753438626.
Before execution the complete audit source was stored in the repository as
Git blob `85722bf7076c94ab6413e158654417dc6529e229` and fetched back.
It matches the 7761-byte local source by Git object identity. Its SHA-256 is
`fca9dfcb45bf0ee15bce97ed95f3c24a53905cb6ed5e3fdf5d072fb04354b767`.

Command: `python -I audit.py` (executed using the absolute file path).
Environment: Linux, x86_64, Python 3.13.5.
Exit: 0; stderr: 0 bytes.
Stdout: 481 bytes, seven lines; SHA-256
`09e285cda424443e6efaab7123323a2db8f02319bb93e4da48cef4464e164dec`.

```text
PASS G1: five exact W, G and scaled-insertion Fourier identities
PASS G2: complete one-link kernel eigenvectors, support and order bounds
PASS G3: all 729 star labels; gauge projection is mod five only
PASS G4: N=3 edge-disjoint 13-link junction with boundary -5,+5
PASS G5: five rational directions of TARGET rank-two EM projector only
PASS G6: forbidden-charge, absent-gauge and wrong-sign controls detected
ALL 6 EXACT AUDIT GROUPS PASS; no many-link spectrum or phase computed
```

The source was unchanged after execution. This is a nonformal incubation
run, NOT a repository runner invocation, a P-probe, a canonical benchmark,
or the pinned Python 3.12 two-architecture procedure. No such evidence is
claimed for this note. The output is retained here instead of presenting
an unauthenticated second-architecture transcript.

## Same-agent falsification pass

This pass is not independent or blind confirmation. In addition to the
exact programmed mutations, the written argument was checked against:

- noncommutation of M and K: the proof keeps M S instead of incorrectly
  identifying the range with the undressed Fourier support;
- singular transfer: all inverse square roots stay on the positive support;
- an insertion at forbidden Fourier charge +/-2: it violates support and
  the Loewner bound, so the WG support identity is essential;
- gauge projection: the local sum tests all 729 star fields, not only real
  divergence-zero fields, and the junction realizes the extra allowed case;
- normalized trace: Lambda_N^m is retained in the finite partition identity;
- limit exchange: a finite Perron vector is not substituted for the
  prescribed simultaneous infinite-volume/time limit;
- target versus result: no finite-target projector identity is reported as
  an actual residue or a massless-phase computation.

No failed candidate predicate was altered. All-N support, unitary
conjugacy, partition normalization and norm sharpness are written proofs;
the finite program audits premises and witnesses, not those full matrices.

## Additional mathematical review

Two separate AI review passes checked the finite proof and its agreement with
the S1-S7 contract. No error was found in the stated finite theorem. This is
not blind external peer review, formal verification or public acceptance.
The summary above corrects support equality to support inclusion: if
`A=Lambda_N^(-1/2)L^(1/2)M:H_+ -> S`, then A is invertible and
`-i*kappa*D_l=A^* Q_l A`. Since `Q_l chi_0=0`, the nonzero vector
`A^(-1)chi_0` lies in `ker D_l` inside `H_+`. Thus D_l annihilates the
transfer kernel but also has additional zero directions. Equations (9)-(14)
of TRANSFER.md already give the correct statement; its source is unchanged.

A local replay of the unchanged audit passed all six groups on Windows,
AMD64, Python 3.12.10, with exit 0 and empty stderr. Its 488-byte CRLF stdout
has SHA-256 `100c495785a977a390db886733c5bb3481e2af1b0521226bb1afb17e80b84c0e`.
Replacing CRLF by LF gives the original 481 bytes and hash recorded above.
The raw byte streams differ, and both runs use the x86_64 architecture;
this is not a formal two-architecture result.

DYNAMICS.md adds a separate written finite extension: a four-plaquette
transition out of the real-Gauss subspace, its finite ground-state
consequence and the preserved global modulo-five flux sectors. The original
audit does not test these new propositions; their evidence is the displayed
proof, subject to separate review.

## What remains

Formal mathematical review should first inspect equations (5),
(8)-(14), and the state/volume-limit boundary. A later public formal probe
can audit the proof in the repository's required environment after a new
prospective pin. The massless phase, infinite-volume reconstruction,
scaling measure, positive massless spectral atom, its actual rank-two
residue, normalization to D3, locality and effective remainders remain open.
No detector, source-to-QDD map, one-photon preparation or SI scale is supplied.
