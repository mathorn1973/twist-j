# PREREG: P-A4-RAMIFIED-HODGE-TRACEKERNEL-1

Status: FORMAL PREREGISTRATION PIN.
Owner: connected GitHub account, explicitly authorized by the author in chat on 2026-09-19
Action layer: L1
Authority basis: Public Canon v89
Issue lock: #1048

## Equation / decision target

Let V=A4 in the marked augmentation-root basis with Gram H=I_4+11^T, det H=5, and W=Lambda^2 V. The marked orientation defines the Hodge star. Set K=sqrt(5)*star.

Frozen targets:
- K is integral and K^2=5 I_6.
- Modulo five, Kbar^2=0, rank Kbar=3, and im Kbar=ker Kbar=ell wedge Vbar for ell=(1,1,1,1).
- For Hbar=H mod 5, ker Hbar=<ell> and im Hbar=W_5=ker(sum:F_5^4->F_5).
- Hbar induces an isometry Vbar/<ell> -> (W_5,g_5), where g_5 is the public TRACEKERNEL-RESIDUAL-FORM carrier.
- The alternating quotient home map induced by Kbar, transported to the public difference basis b1=(1,-1,0,0), b2=(0,1,-1,0), b3=(0,0,1,-1), equals -beta_public for the frozen root orientation, with beta_public(x,y)=B^-1(x cross y), B=[[2,4,0],[4,2,4],[0,4,2]] mod 5.
- The marked A5 action is equivariant for the transported bracket.

The minus comparison scalar is frozen before execution and may not be changed after the run.

## Code

verify.py is Python standard-library only. Integer identities are exact over Z and ramified statements use exact F_5 elimination. No floating point, randomness, external package, network data or tolerance is admitted.

The committed verifier audits the integral/nilpotent carrier and public residual Gram. The quotient isometry, frozen bracket scalar and A5 equivariance remain theorem-grade proof obligations and must be supplied before any T conclusion.

## Carrier / data

The carrier is generated from the marked A4 Gram and orientation. The public W_5 basis and residual Gram are reconstructed from their definitions. No copied numerical table is evidence.

## Failure threshold

No tolerance. Any exact failure of integrality, K^2=5I, the rank/image/kernel statement, quotient isometry, frozen bracket scalar or A5 equivariance fires the corresponding target. Integrity mismatch or changed authority is STOP.

## Explicit nonclaims

A positive result is L1 algebra only. It does not close TRACEKERNEL-CURVATURE-FORCING [O], select a physical spatial commutator, derive physical dimension or time, or supply a decoder, probability, measure, SI quantity or L2-L6 lift.
