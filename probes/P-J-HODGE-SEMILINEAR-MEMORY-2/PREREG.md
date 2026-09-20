# PREREG: P-J-HODGE-SEMILINEAR-MEMORY-2

**FORMAL PUBLIC PROBE / NO CANON PROMOTION.**

Owner: A. M. Thorn / J-Hodge semilinear memory successor session 2026-09-19.
Action layer: L1.
Issue lock: #1071.
Branch: `probe/P-J-HODGE-SEMILINEAR-MEMORY-2`.
Authority: Public Canon v89; base main
`08d7984d97c85d89d0b22a400762a5140fcb3bb5`.

Predecessor: P-J-HODGE-SEMILINEAR-MEMORY-1 (#1070) is ABANDONED after a
nonzero first run caused by a defective basis-normalization assertion in G7.
That identifier is consumed and is not resumed. This successor preserves the
mathematical target and freezes the normalization formula below before
execution.

Let V=A4 tensor Q in the marked root basis, C the marked five-cycle,
M=I+C^2, W=Lambda^2 V, L=Lambda^2 M, K=sqrt(5)*,
F=Q(sqrt(5)) with automorphism sigma, and
P_+/-=(I +/- K/sqrt(5))/2. Let E_J=im P_+ + im(P_- L P_+).
Let A_c=Lambda^2 C and T=(I+A_c+...+A_c^4)/5, R=I-T.

Frozen targets:
G1. K L K^-1 T=L^-1 T and (KL-LK)R=0.
G2. For every rational substrate w, its plus coordinate x evolves in the
frozen sigma-conjugate Hodge bases as x'=A x+B sigma(x), rank_F(B)=1.
G3. This map is Q-linear/semilinear and not F-linear.
G4. E_J is an exact four-dimensional F-linear predictive realization with
present output x; the present/next observability rank is four, so four is
minimal among F-linear exact realizations of this frozen output.
G5. The one-dimensional visible primary axis output y obeys
y_(n+2)=3 y_(n+1)-y_n.
G6. Present triple x_n plus one previous axial scalar y_(n-1) has full
observation rank four and determines the E_J state uniquely and F-linearly.
G7. For the deterministic sigma-conjugate primary basis from the first
nonzero rational column of T, let the boost matrix be [[3/2,b],[c,3/2]].
Freeze bc=5/4 and the pre-run normalization
    target=-sqrt(5)/2,
    r=target/b,
    h_-'=r h_-.
The normalized basis (h_+,h_-') must give exactly
    1/2 [[3,-sqrt(5)],[-sqrt(5),3]].
Thus self coefficient is L_2/2 and normalized conjugate coupling is
-sqrt(5)F_2/2. No post-run basis fitting is permitted.
G8. P_-=sigma(P_+) entrywise; the hidden rank-one primary channel is exactly
the Galois-conjugate Hodge component.
G9. The accepted arbitrary A5/J future-word minimum remains six; four is
fixed-J only.
G10. No native-U intertwiner or physical-time theorem is asserted.

PROOF.md owns universal semilinear/minimality arguments. verify.py is exact
standard-library Fraction/Q(sqrt5) arithmetic and audits G1-G8. No floating
point, randomness, network input, external package or tolerance. Static syntax
compilation only is allowed before pin.

The negative-norm coordinate is not identified with physical time. "Time is a
counter" remains a reading. No physical dimension, observer, decoder,
occurrence law, measure, SI, Canon promotion or L2-L6 lift.
