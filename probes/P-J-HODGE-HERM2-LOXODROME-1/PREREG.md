# PREREG: P-J-HODGE-HERM2-LOXODROME-1

**FORMAL PUBLIC PROBE PREREGISTRATION / NO CANON STATUS.**

Owner: A. M. Thorn / J-Hodge loxodrome session 2026-09-19
Action layer: L1
Authority basis: Public Canon v89
Issue lock: #1051
Branch: `probe/P-J-HODGE-HERM2-LOXODROME-1`

## Equation / decision target

Use the marked augmentation-root carrier `V=A4 tensor Q` with
`H=I+11^T`, marked five-cycle `C`, `M=I+C^2`,
`W=Lambda^2 V`, `L=Lambda^2 M`, and the natural symmetric wedge pairing
`beta` on `W`.  With the marked orientation let `W_+` and `W_-`
be the two real Hodge eigenspaces.

Define

```text
E_J = W_+ + im(P_- L P_+).
```

The frozen exact targets are:

```text
dim E_J = 4,
L(E_J) = E_J,
signature(beta|E_J) = (3,1),
L|E_J preserves beta,
char_(E_J)(X) = (X^2-3X+1)(X^2-phi X+1).
```

Here `phi=(1+sqrt(5))/2`.  The boost factor has roots
`phi^2,phi^-2`.  The phase factor has roots
`zeta_10,zeta_10^-1`, where `zeta_10=-zeta_5^3`.

Define the algebraic loxodromic multiplier

```text
a_H = -J^-2.
```

The preregistered identity is

```text
a_H = phi^2 zeta_10.
```

For the normalized diagonal Hermitian action associated with
`diag(a_H,1)`, the modulus pair is `phi^2,phi^-2` and the phase pair is
`zeta_10,zeta_10^-1`; hence its two exact characteristic factors are the
same two displayed factors.  The claim is this exact algebraic loxodromic
comparison, not a canonical carrier identification.

In standard real Lorentz notation the exact pair corresponds to rapidity
`2 log(phi)` and rotation angle `pi/5`.  The verifier proves the
algebraic pair; no floating approximation to either transcendental quantity
is an input or acceptance criterion.

## Code and exact carrier

`verify.py` is Python standard-library only.  It uses `Fraction`, an exact
two-component implementation of `Q(sqrt(5))`, and an exact degree-four
implementation of `Q(zeta_5)`.  No floating point, randomness, external
package, network input or tolerance is admitted.

The four-dimensional carrier is reconstructed from the marked A4 matrices.
The first three basis vectors are a deterministic column basis of `P_+`;
the fourth is the first nonzero column of `P_- L P_+`.  This is only a
coordinate certificate for the coordinate-free space `E_J`.

## Systematics and controls

1. The Hodge orientation is frozen by the marked A4 root basis.
2. The verifier reconstructs the Hodge projectors and cross rank rather than
   importing the result of P-J-HODGE-PREDICTIVE-CLOSURE-1.
3. The wedge-pairing Gram is checked in the deterministic basis.  Its plus
   block is exactly `sqrt(5)/10 * [[3,1,1],[1,3,1],[1,1,3]]`; the fourth
   vector is beta-orthogonal to that block and has squared value
   `-(2+sqrt(5))/8`.  This is the exact signature certificate.
4. Invariance and beta preservation are checked as matrix identities.
5. The two characteristic factors are certified by exact annihilating
   factors of rank two each, with product zero.
6. The cyclotomic identities `zeta_10^10=1`, `zeta_10^5=-1`,
   `zeta_10+zeta_10^-1=phi`, and
   `-J^-2=phi^2 zeta_10` are checked independently.

## Failure threshold

There is no numerical tolerance.  The probe fires on any exact failure of:

- four-dimensionality or L-invariance of `E_J`;
- nondegeneracy or signature certificate `(3,1)`;
- beta preservation;
- either frozen characteristic factor or its rank-two certificate;
- the exact cyclotomic identity for `a_H`;
- the normalized Herm2 modulus/phase factor comparison.

Changed preregistration or verifier bytes after the pin, or an authority
mismatch, is STOP rather than a scientific result.

## Explicit nonclaims

No physical spatial dimension or physical time is derived.  No canonical
intertwiner with an already adopted physical Herm2 carrier is asserted.
No native-U bridge, decoder selection, probability, measure, SI quantity,
curvature selection or L2-L6 lift follows from this probe alone.
