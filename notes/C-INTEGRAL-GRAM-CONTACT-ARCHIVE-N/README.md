# Integral contact, complete quadratic reading and two-use archive

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1844](https://github.com/mathorn1973/twist-j/issues/1844).
Status before execution: **NON-CANONICAL / L1 / analytical proposal**.
No Public Canon status is created by this directory.

## The concrete unification

For the specified integer contact of #1833, the complete unnormalized
Hermitian record G=z*z^dagger contains the information that decides whether
the contact is integral. It then evolves by the same selected contact matrix.
Consequently one can run the record forward or backward without choosing
a hidden representative z. This is proved on the exact image of O^N,
O=Z[zeta_5], including occupied and refused states.

The admission condition is

    z_i-z_j in 2O
      iff G_ii+G_jj-G_ij-G_ji == 0 in O_F/(2)=F4.

The scalar binary trace is insufficient. Retaining the full relative norm
is essential to this particular factor. Normalizing away the overall scale
also fails for this same contact.

This closes a narrow connection between a declared integer dynamics and its
quadratic reading. It does not select the dynamics from J or implement it
with the original native U.

## One complete apparatus example

Seven O-valued slots contain two independently chosen source/reference pairs,
the same reusable receiver, an archive for its arbitrary old content, and
an archive for the first output. A fourteen-state cyclic cursor applies six
specified pair operations, holds the final state for two ticks, and reverses
the operations. All primitive data operations conserve both the full
Hermitian account and the O-valued sum.

From

    (S1,S2,L1,L2,R,A0,A1)=(2u1,2u2,2v1,2v2,m,0,0)

the actual state at ticks 6,7,8 is

    (a1,a2,0,0,b2,m,b1),
    a_k=(1+rho)u_k+(1-rho)v_k,
    b_k=(1-rho)u_k+(1+rho)v_k, rho=j^2.

The old content m and both new relative records coexist. No intermediate
reset, erasure or source-dependent precomputed archive is used. All source
and reference inputs are present at the common origin. Every complete state,
including unprepared occupied archives, returns after fourteen ticks.
The storage is therefore finite-window storage, not a permanent archive.

The final record reader receives only the cursor and the current Gram
matrix. During the declared window it returns the principal 3-by-3 record
on (A0,A1,R). Recorded zero is a valid record in that window. It does not
recover absolute scalar phases from the phase-blind Gram alone.

## What is inherited, and what is being tested here

The contact, its integral domain and its complete identity refusal branch
are inherited from #1833. The residue fields are the accepted
J-BINARY-NORM-DESCENT theorem. Quadratic congruence reading, occupied-memory
export and two-use apparatuses have existing predecessors. REFERENCES.md
identifies them; this candidate makes no first-construction claim.

The new narrow question is exact state-dependent contact admission and full
forward/backward Gram continuation for that specific contact, followed by
its explicitly stated continuing apparatus example. The written proof
contains the universal statements. The finite programs audit only their
frozen inventories.

## Evidence layout

- PREREG.md freezes the complete domain, equations, systematics, falsifiers,
  seven audit inventories, negative controls and comparable certificate streams.
- PROOF.md gives the analytical argument and its scope boundaries.
- REFERENCES.md attributes the exact dependencies and nearby work.
- verify.py is the builder's independent integer-state/Gram implementation.
- break.py was written from the frozen preregistration alone, without reading
  verify.py or PROOF.md. Both sources require a public pin and readback before
  execution or comparison.
- PREPARATION.md records the actual local source revisions, static checks,
  implementation provenance and pending public pin. No scientific run has
  occurred at this preparation stage.
- RUN.md, RESULT.md and recorded stdout are added only after actual execution.
- The PROMO document describes a possible later review, not a requested fold.

## Limits retained explicitly

The carrier consists of integer configurations, not an undeclared space of
quantum amplitudes or mixed density matrices. The slot graph, contact,
program cursor, reference phases, initial blanks and read window are supplied.
There is no physical construction that acquires the global Gram matrix.
Adding a fresh reference with a fixed absolute phase after discarding the
old common phase needs another preparation interface and is not an operation
on the old Gram record alone.

The conserved positive integer account is not identified with a Hamiltonian,
an SI energy, a relativistic clock or the energy of another TWIST-J model.
No Born occurrence, native U/W bridge, photon/electron identification, spatial
dimension, infinite fresh-input supply or public claim promotion follows.
