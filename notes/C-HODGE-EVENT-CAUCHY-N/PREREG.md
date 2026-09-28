# C-HODGE-EVENT-CAUCHY-N: prospective contract

Status: PUBLIC NON-CANONICAL incubation. No Canon authority.
Owner: A. M. Thorn / hodge-event-cauchy-20260927; issue #1239.
Date: 2026-09-27.
Basis: Public Canon v92, main ad8a572128f594a3550cbf5e3adef2516fea3d88.

## Scope and distinct predecessor

C-HODGE-SPACETIME-WINDOW-N provides a chosen flat Lorentz event set M.
C-HODGE-WINDOW-FIELD-OPERATOR-N provides consistency on ALL events but no
finite-scale stability. This candidate does NOT change that operator or
claim its missing stability. It selects a marked SUBCARRIER of actual M
and transports a separately chosen stable scalar Cauchy problem onto it.
Neither the selected chart E+ nor its physical Galois equivalence is derived.

The exact anchor is probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py, SHA256
02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9.
Other checked mathematical sources, not new Canon authorities:
notes/C-HODGE-SPACETIME-WINDOW-N/verify.py, SHA256
86a4162ed7429db0be93b6633e70c99ecdbd7ca14cd42ae16c66188d910d7203;
notes/C-HODGE-WINDOW-FIELD-OPERATOR-N/verify.py, SHA256
6e835c99c88e2fa057e372a22c06711476e3956d79be3d2ddd7fe18816d0e300.
The two note proofs, their input definitions, and their nonclaims are retained.

## G1: actual events and injective marked grid

F=Q(sqrt5), positive real embedding. In the inherited E+ basis set

    t=(0,0,0,1), s1=(1,-1,0,0), s2=(1,1,-2,0), s3=(1,1,1,0),
    ct=-g(t,t)=(2+sqrt5)/8,
    (a1,a2,a3)=(g(si,si))=(2sqrt5/5,6sqrt5/5,3sqrt5/2).

The four vectors are g-orthogonal. Retain Pi, N=I-Pi, c0 and R from the
window construction, with c0=(4+2sqrt5)/5 and R=10-9sqrt5/5.
For n>=3, delta=1/n, H=n^4, freeze

    y_n(m,z)=delta*(m*t+sum z_i*s_i),        (m,z) in Z x Z^3,
    w_n(m,z)=rnd(H*i*y_n(m,z)) in Z^6,
    e_n(m,z)=Pi*w_n(m,z)/H in M/H.

Here i is the E inclusion and rnd rounds ambient coordinates to nearest
integers, ties toward +infinity. Prove total admission, injection, local
finiteness, covering at O(1/n), spacelike same-m slices, and future timelike
same-z consecutive events. The norm is the inherited ||.||_*.
No surjection onto M/H is asserted. Event equality is literal equality of
projected coordinates and the labels are recoverable by injection.

## G2: selected scalar law and exact coefficients

Define the scalar field ONLY on Gamma_n=image(e_n), retaining (m,z) as the
chosen chart. Values are in F for exact arithmetic, and real or complex
extensions are specified for estimates/modes. Nothing assigns values to
M/H minus Gamma_n. The Hilbert norm is pulled from counting Z^3, not a
claim about the physical measure of all windowed events.

    alpha_i=ct/a_i,
    K=sum_i alpha_i*(2I-shift_i-shift_-i),
    f_(m+1)-2f_m+f_(m-1)+K f_m=delta^2 j_m.

Prove alpha=((5+2sqrt5)/16,(5+2sqrt5)/48,(5+2sqrt5)/60),
A=sum alpha=1/2+sqrt5/5<1, and 0<=K<=4A I on l2(Z^3).
These are metric-derived weights conditional on the chosen rectangular
stencil; they are not a uniqueness theorem among physical dynamics.

## G3: finite-scale existence, stability, energy and retarded response

Freeze arbitrary finitely supported F-valued two-slice data (f0,f1) and
finite forcing prefixes. Prove unique all-time continuation, exact reverse
step, finite stencil support, and the conserved energy in the unforced case

    E(f_m,f_(m+1))=1/2||f_(m+1)-f_m||^2
                     +1/2<f_(m+1),K f_m>.

For a=(f_(m+1)+f_m)/2 and v=f_(m+1)-f_m prove

    E=1/2<v,(I-K/4)v>+1/2<a,Ka> >=(1-A)||v||^2/2.

Prove strict positivity for every nonzero finite-support pair, and source
work E_m-E_(m-1)=delta^2<j_m,f_(m+1)-f_(m-1)>/2.
For G0=0,G1=I,G_(r+1)=(2I-K)G_r-G_(r-1), prove the exact Duhamel formula,
retarded support and ||G_r||<=r. A zero-frequency double root is allowed;
no spectral gap or uniform-in-time bound on unweighted position is claimed.

## G4: convergence and local D3 comparison

For each fixed macroscopic time T, sampled C4 solutions of

    f_tautau=sum_i alpha_i f_xixi

with uniformly compact spatial support and bounded derivatives are the
reference class. Norm: ||f||_delta^2=delta^3 sum_z |f(z)|^2.
Prove unscaled local defect O(delta^4), then O(delta^2) finite-time solution
error for exact initial two-slice samples. Include the O(delta^4) event
rounding error. This is a conditional numerical/mathematical convergence
statement on this precise class, not a native evolution or quantum limit.

For a fixed bounded lifted physical momentum set, initialize the new exact
recurrence by the two initial slices of a principal D3 plane wave, using
the same limiting orthonormal Hodge frame and epsilon=delta. Prove uniform
finite-time O(delta^2) mode agreement with the D3 wave after the actual
event sampling error is included. No exact finite-scale D3 equality, global
torus map, action, Hilbert-space or measure equivalence is asserted.

## G5: group velocity versus microscopic support

The exact selected grid dispersion is

    sin^2(omega/2)=sum_i alpha_i sin^2(theta_i/2).

Prove real branches, the zero-mode convention, and the orthonormal Hodge
frame group-speed bound sum_i alpha_i sin^2(theta_i)/sin^2(omega)<=1 away
from the zero mode. Verify the underlying polynomial inequality with
u_i=sin^2(theta_i/2) in [0,1].

Do NOT identify that bound with front support. The one-step impulse reaches
neighboring sites with nonzero alpha_i although ideal displacement t+s_i
is spacelike. Seek an exact rounded-event witness too. A negative strict
microscopic-cone result is retained, not reinterpreted as physical causality.

## Candidate layer bridges and choices

CB-EVENT-MESH: L1 integer labels -> selected L2 affine events.
CB-EVENT-SCALAR-EVOLUTION: L2 marked Gamma_n -> L5 scalar histories.
They are candidate-D dictionaries only, not existing public GATES.tsv rows.
The chart sign, window, frame/stencil, rounding, scaling H=n^4, active
subcarrier, counting norm and initial data are explicit choices.
No L6 measure, native Omega/U identification, physical E+ selector or
Galois equivalence, full-M dynamics, exact finite-scale J/C5 symmetry,
physical photon, polarization, massless phase, SI or nonflat gravity claim.

## Prospective audit and failure rules

Commit and publicly read back PREREG.md, model.py and verify.py before first
scientific execution. Standard-library exact arithmetic only. The audit
checks the anchor hash, orthogonality/coefficients/CFL margin, finite
admission/injection/causal slice witnesses, independent finite sparse and
periodic-matrix wave steps, energy, inverse, source work, Green recursion,
finite support, the group-speed polynomial and Taylor moment identities.
All-integer/all-time conclusions require the written proof; finite cases are
corroboration. No blind independent-agent claim is made.
Mathematical counterexample fires its frozen clause; code/integrity failure
is STOP, not a physical falsification. Thresholds and classes remain fixed.
Only this candidate directory may be added. No Canon, gate, Registry,
Frontier, workflow, tool or existing-note edits. Promotion is a later fold.
