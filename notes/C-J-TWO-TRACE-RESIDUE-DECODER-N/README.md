# Exact scalar inversion from two traces and a residue

PUBLIC / NON-CANONICAL. No authority. Action layer: L1 only.
Author: A. M. Thorn. Issue: #1281. License: Apache-2.0.

This prospective incubation package develops the scalar-reader construction
proposed after Public Canon v93. It is not a physical apparatus and changes
no Canon claim, status or scope. It is one named item with one owner.

The data are S(alpha)=Tr(alpha*bar(alpha))/2, S(J alpha), and alpha mod25 O,
for nonzero alpha in O=Z[zeta_5] with N(alpha)<=941. The supplied inverse is
integer-only, normalizes the J orbit, reconstructs the small representative,
and rejects readings outside the exact image. Its first two data entries are
unbounded integers, not finite pointer states.

PREREG.md fixes the prospective audit before computation. PROOF.md contains
candidate-T universal derivations. decoder.py is the implementation;
verify.py audits it, while break.py uses a separate same-author cyclic-ring
implementation and larger complete box without importing either file.
Independent agent confirmation and a formal two-architecture scientific gate
are not claimed. A notes PR's repository checks do not provide that gate.

The primary proof establishes sufficiency of modulus 25, not its minimality.
The mod5 full-domain collision is known before this audit. A separate complete
census determines whether mod5 nevertheless has enough distinct observed
orbit classes for a 3125-label codebook at the same norm bound.

Run from the repository root with Python's standard library:

    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/verify.py
    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/break.py

Result and neutral run records are added after the frozen execution. Only the
later public fold can promote a reviewed, properly evidenced theorem.
