# P-J-ODD-MOTOR-BRIDGE-HARDENING-1 result

Status: **candidate-T / L1 / HARDENING-CERTIFIED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable verifier exited zero, wrote empty
stderr, and matched the committed `EXPECTED.txt` bytes. All frozen H1-H3
statements passed exactly.

## H1. Native two-sector evidence hardened

The verifier calculated rather than assumed

```text
chi_M(x) = (x^2-alpha_u x+alpha_u)(x^2-alpha_s x+alpha_s),
delta_u = (-5-sqrt5)/2,
delta_s = (-5+sqrt5)/2.
```

The four exact real-embedding signs are

```text
-1 -1 -1 -1.
```

A polynomial extended-gcd calculation produced complementary CRT idempotents
in the generated algebra. They are orthogonal, sum to the identity, and have
ranks

```text
2 2.
```

Thus the two quadratic factors are distinct irreducibles over `Q(sqrt5)` and
the native generated algebra has exactly two primitive nonzero rank-two
sectors. The predecessor theorem's native third-sector exclusion now has an
explicit exact computational audit.

## H2. Schur elimination calculated explicitly

For all five tokens the verifier assembled

```text
L_k(z,t)=zI-(H_k+tA_1)
```

as a formal Laurent matrix and calculated the `C`-block inverse and Schur
complement coefficient by coefficient. It obtained

```text
S_PR = -(t^2/z) P A_1 C A_1 R,
S_PR^sharp S_PR = (5/4)(t^4/z^2) R,
S_PR S_PR^sharp = (5/4)(t^4/z^2) P.
```

Result:

```text
explicit Schur tokens 5/5 PASS.
```

This is the exact algebraic source of the orientation-independent magnitude
`sqrt5 t^2/(2z)`. It is not a physical frequency or resonance statement.

## H3. Finite primitive-channel classification

The complete frozen box

```text
(c1,c2,c3,c4) in {-2,-1,0,1,2}^4 minus zero
```

contains 624 channels. The full projector, rank, norm and active-line battery
left exactly four ordered survivors:

```text
(-1,0,0,1)
(0,-1,1,0)
(0,1,-1,0)
(1,0,0,-1)
```

Equivalently:

```text
+/- (D-D^4),
+/- (D^2-D^3).
```

The exact conjugacy

```text
rho(2,0)(D-D^4)rho(2,0)^-1 = D^2-D^3
```

also passed. Therefore the frozen coefficient box contains one primitive odd
channel up to sign and affine conjugation.

This is a finite classification in the preregistered box. It is not an
unrestricted uniqueness theorem and it does not select a physical mediator
basis.

## Scientific routing

```text
H1  PASS
H2  PASS
H3  PASS
DECISION  HARDENING-CERTIFIED
```

The maximum later public use is:

1. add this probe as supplementary exact evidence for the existing
   `J-ODD-MOTOR-MEDIATED-BRIDGE [T]` clauses;
2. add the finite-box uniqueness clause at L1 if a separately locked Canon
   fold accepts it.

No Canon, Registry, Frontier, dependency, gate, status, tag or release file is
changed by this probe. No material, phonon, amplitudon, susceptibility,
frequency, damping, temperature, light coupling, Born rule, probability,
observer, decoder, apparatus, force, spacetime, SI value or L2-L6 lift is
assumed or concluded.
