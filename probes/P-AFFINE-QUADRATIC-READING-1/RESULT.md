# P-AFFINE-QUADRATIC-READING-1 result

Date: 2026-08-21

```text
DECISION:   AFFINE-QUADRATIC-READING-CONFIRMED
CHECKS:     33 of 33 PASS, exit 0, empty stderr
PIN:        98f0ce2ba7cc530819ccc7c59d8876ce82effc48
CLAIM LOCK: issue 495
LAYER:      L1 state only
BASIS:      Public Canon v59, tag canon-v59, content 5da6b883,
            CANON_SHA256 7fdea700...87f641, CANON_BYTES 314310
```

No threshold moved after the pin. No falsifier fired. Nothing in this
directory changes `canon/`, the registry, the frontier, or any live `H` or `O`
row; a fold is a separate later act.

## 1. What was asked

Let `M_J = m_J` be the full step for `J = 1 + zeta_5^2` and
`D_J := M_J - I = m_{zeta_5^2}` the motor, `u: zeta_5 -> zeta_5^2` the Galois
generator, `c = u^2`, `K = Q(zeta_5)`, `K+ = Q(sqrt5)`, and
`G = <D_J, u> = AGL_1(F_5)` of order 20 acting on `V = K` as the augmentation
of the five points. At which degree does an invariant scalar reading of `V`
first exist, and how many are there at that degree?

## 2. What was found

```text
AFFINE-READING-DEGREE-CENSUS         earned status T, scope L1
  (V*)^G = 0 and (Lambda^2 V*)^G = 0, while (Sym^2 V*)^G has dimension one.
  Degree two is therefore the first degree carrying a nonzero G-invariant
  scalar reading of V, and it carries exactly one line.

AFFINE-QUADRATIC-FORM-UNIQUENESS     earned status T, scope L1
  that line is Q . q_+ with q_+(x) = Tr_{K+/Q}(x c(x)), whose Gram has leading
  minors 2, 15/4, 25/4, 125/16 and is therefore positive definite. Rational
  invariance under the motor and under the Galois generator fix the LINE;
  adding q != 0 and q >= 0 as a fourth premise fixes the RAY Q_{>0} . q_+.
```

Both rows rest on a written proof plus an exact machine audit, which is why
they are `T` rather than `C`. The written step is that each census number is
the dimension of the rational solution space of an invariance system, and the
rank of a rational matrix is unchanged by extension of scalars; with `G` finite
and characteristic zero, Maschke turns `dim End_{Q[G]}(V) = 1` into
irreducibility of `V_L` for every characteristic-zero `L`. The verifier audits
the ranks; it does not carry the universal quantifier by itself.

Consequence recorded in the same scope: no nonzero lossy `G`-equivariant linear
reading of `V` exists over any field of characteristic zero. The affine linear
wall does not fall anywhere.

## 3. The controls, which are the interesting half

Under the motor alone the same census returns symmetric dimension two,
alternating dimension two, and endomorphism dimension four; and over
`K+ = Q(phi)` the motor even admits a lossy equivariant idempotent

```text
E = (D_J + phi I)(D_J^2 + psi D_J + I)/sqrt5,   psi = 1 - phi,
```

of rank two, with `u E u^-1 = I - E`. So the compression wall of the motor
alone falls exactly at the adjunction of `phi`, and it is the Galois generator
that restores it over every field, removes the second symmetric channel, and
removes both alternating channels. The uniqueness is a property of the full
affine structure, not of the motor.

## 4. Target comparison, made last

With `P(e_x) = zeta_5^x` the augmentation intertwiner, `J = I + T^2` on the
augmentation is `M_J`, and

```text
P^T Gram(q_+) P = (5 I_5 - 11^T)/2.
```

The unique invariant is the Euclidean form of the five points read in
`J`-coordinates. As matrices, `5 I_4 - 11^T = 2 Gram(q_+)` and
`I_4 - (1/5)11^T = (2/5) Gram(q_+)`, so both frozen public constants are
positive rational multiples of it. Whether the carrier basis of any other
public row equals this frozen `zeta`-power basis is not asserted here.

## 5. Scope, stated as a firewall

```text
MAY      the exact identities, the census dimensions, the two rows of section
         2 at status T and scope L1, the controls of section 3, and the matrix
         identities of section 4.
MAY NOT  any physical reading. The identification of q_+ with a Born square is
         NOT part of this probe. No effect selection, no normalization to total
         probability one, no apparatus, no instrument, no pointer, no
         post-state law, no realized-event stream, no measure.
```

`READING-SPLIT [D]` is unchanged: no totality, uniqueness or completeness of
the decoder is claimed. `QDD-J-AFFINE-APPARATUS-NONSELECTION [T]`,
`QDD-INSTRUMENT-NONSELECTION [T]`, `QDD-J-CENTRALIZER-NONSELECTION [T]` and
`QDD-RECORD-COMPLETE-LUEDER-SELECTION [T]` are untouched and uncontradicted:
they are `L4` apparatus and support statements, and deriving that a form is the
unique invariant of its degree is not selecting an apparatus. `SAMPLING NOT
PROVIDED`.

No layer lift is performed or named anywhere in this probe.

## 6. Disclosure

RESULT-EXPOSED, not blind, as preregistered. The statement was derived in
non-canonical incubation work on the same date and exercised there by a
separate implementation with a different structure and different check labels.
Those runs are discovery context and are not evidence. The accepted verifier
was written fresh, pinned before any execution, read back from the public
remote, and run exactly once.
