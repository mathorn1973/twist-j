# PREREG: P-A4-RAMIFIED-HODGE-TRACEKERNEL-1

**FORMAL PUBLIC PROBE PREREGISTRATION / NO CANON STATUS.**
Owner: A. M. Thorn / ramified Hodge seam session 2026-09-19
Action layer: L1
Authority basis: Public Canon v89
Issue lock: #1048

## Equation / decision target

Let `V=A4` in the marked augmentation-root basis, with Gram

```
H = I_4 + 11^T,        det H = 5,
```

and let `W=Lambda^2 V`.  The marked orientation defines the real Hodge star.
Set

```
K = sqrt(5) * star  on W.
```

The first exact target is

```
K in M_6(Z),          K^2 = 5 I_6.
```

Reduce modulo five.  Put `Vbar=V/5V`, `ell=(1,1,1,1)`, and let `Kbar` be the
reduction of `K`.  The ramified target is

```
Kbar^2 = 0,
rank Kbar = 3,
im Kbar = ker Kbar = ell wedge Vbar.
```

For `Hbar=H mod 5`, the target is

```
ker Hbar = <ell>,
im Hbar = W_5 = ker(sum:F_5^4 -> F_5),
```

and the induced map `Vbar/<ell> -> W_5` is an isometry from the quotient
residual form to the public `g_5` of TRACEKERNEL-RESIDUAL-FORM.

Use `Kbar` to define the alternating quotient home map
`Lambda^2(Vbar/<ell>) -> Vbar/<ell>`.  Transport it through the preceding
isometry to the public difference basis

```
b1=(1,-1,0,0), b2=(0,1,-1,0), b3=(0,0,1,-1).
```

With the marked root orientation frozen above, the transported bracket is
preregistered to equal `- beta_public`, where

```
beta_public(x,y) = B^-1 (x cross y),
B = [[2,4,0],[4,2,4],[0,4,2]] mod 5.
```

The minus sign is part of the preregistration and may not be changed after
execution.  Reversing the four-dimensional orientation would reverse it, but
that is not an after-the-fact repair.

## Code

`verify.py` is Python standard-library only.  Universal integer identities are
checked over `Z`; the ramified statements use exact Gaussian elimination in
`F_5`.  No floating point, randomness, external package, network source or
numerical tolerance is used.

## Carrier / data

The carrier is entirely generated from the marked `A4` Gram and orientation.
The public `W_5` difference basis and residual Gram are reconstructed exactly
inside the verifier.  No copied table or external data file is used.

## Systematics and controls

1. `K` is constructed from the induced bivector Gram and wedge pairing, not
   from a target hard-coded nilpotent matrix.
2. `im Kbar = ker Kbar` is certified by nilpotence, exact rank and the
   independently constructed subspace `ell wedge Vbar`.
3. The quotient-to-`W_5` map is checked metrically, not by equal dimension.
4. The bracket comparison is checked on a basis after both maps are built from
   their own definitions.
5. The marked five-cycle and three-cycle generate an exact 60-element `A5`;
   bracket equivariance and residual-metric preservation are checked on both
   generators.
6. The public bracket's volume-sign freedom is kept explicit.  This probe does
   not infer a physical orientation.

## Failure threshold

No tolerance.  The probe fires on any exact failure of:

- integrality of `K` or `K^2=5I`;
- `Kbar^2=0`, rank three, or the stated image/kernel identity;
- the `Hbar` kernel/image classification;
- the quotient residual isometry;
- the frozen comparison scalar `-1` against the public bracket;
- the two-generator `A5` equivariance checks.

An integrity mismatch or changed authority/pin is STOP.

## Explicit nonclaims

A positive result is an L1 ramified carrier bridge only.  It does not close
TRACEKERNEL-CURVATURE-FORCING [O], select the physical spatial commutator,
derive physical dimension or time, or supply any decoder, probability,
measure, SI quantity or L2-L6 lift.
