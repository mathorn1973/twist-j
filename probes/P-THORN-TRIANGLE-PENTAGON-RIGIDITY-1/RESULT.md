# P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1 result

Status: **candidate-T / L1 / THORN-TRIANGLE-PENTAGON-RIGIDITY CONFIRMED / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable public verifier exited zero,
wrote empty stderr, and produced the exact committed `EXPECTED.txt` bytes.
All twelve frozen gates passed. No scientific falsifier fired and no equation,
carrier, threshold, branch rule, or interpretation moved after the pin.

## Result

Let `z` be any complex unit-circle point and put

```text
J_z = 1 + z^2,
N_z = J_z conjugate(J_z),
S_z = (1-z)(1-conjugate(z)),
t_z = z + conjugate(z).
```

No root-of-unity, order, orientation, fifth root, extremal, or Hurwitz premise
is used. Unit modulus gives `conjugate(z)=z^-1`, hence exactly

```text
N_z = t_z^2,
S_z = 2-t_z.
```

Therefore

```text
S_z = 1+N_z
iff t_z^2+t_z-1 = 0.
```

Multiplication by `z^2` gives the exact Laurent-polynomial identity

```text
z^2 (S_z-(1+N_z)) = -Phi_5(z).
```

Consequently the full Thorn closure is equivalent to

```text
Phi_5(z)=z^4+z^3+z^2+z+1=0,
```

and therefore to `z` having exact order five. The pentagon is forced by the
closure equation itself. It is not selected by a minimum, a scan, or a prior
root-of-unity assumption.

## Scale and branch theorem

On the closure locus,

```text
N_z^2-3N_z+1=0,
N_z in {phi^-2,phi^2}.
```

The conjugate pair `{zeta_5,zeta_5^-1}` is the contracting branch with
`N_z=phi^-2`. The other conjugate pair is the expanding branch with
`N_z=phi^2`. Nothing in the theorem chooses an orientation inside either
pair.

The same quadratic gives

```text
N_z^-1 = 3-N_z,
S_z+N_z^-1 = 4,
S_z^2 = 5N_z,
disc(x^2-3x+1) = 5.
```

Writing `rho^2=N_z` and `s^2=S_z`, the exact double-right-triangle form is

```text
1+rho^2 = s^2,
s^2+rho^-2 = 2^2.
```

The first relation is load-bearing. The frozen primitive-third-root control
has `N=1` and `S=3`, so it satisfies the weaker second relation
`S+N^-1=4` while failing `S=1+N`. The weak scalar triangle alone does not
select five.

## Principal public specialization

At the already-public principal branch `z=zeta_5`, inherited public theorems
give

```text
N_z = J Jbar = phi^-2,
S_z = s_J^2 = 3-phi.
```

The new exact reduction then gives

```text
s_J^4 = 5 phi^-2 = 5 J Jbar.
```

This is the literal golden ramified chord squared. Together with the existing
public scalar definitions it permits only the derived rewriting

```text
script-Q = 2 pi phi^-2 = s_J^4 (2 pi/5).
```

That rewriting is not a physical mechanism or an independently earned bridge.

## Relation to the primary lattice seam

The polynomial `x^2-3x+1` is the same quadratic already present in
`CM-ALTERNATING-PENCIL [T]` and in the candidate-T source package
`P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1`. Its discriminant is five, matching
the source package's independently computed integral primary index five.
This probe does not re-earn or strengthen the source split, bases, quotient,
projector, no-retraction theorem, or promotion package. It also does not
select `Omega_1` as an action unit.

## Proof grade

The universal statement is carried by the written Laurent-polynomial proof in
`PREREG.md`. The verifier is an exact audit using only integers, `Fraction`,
ordinary and Laurent polynomials, exact `Q(sqrt5)` pairs, and exact Gaussian
rationals. Its controls include `z=i`, `z=-1`, the exact rational unit-circle
point `(3+4i)/5`, and the primitive-third-root weak-triangle breaker.

The local x86_64 execution is reproduction, not the two-architecture gate.
The pull-request workflow must reproduce the same `EXPECTED.txt` bytes on
GitHub-hosted x86_64 and native aarch64 and pass aggregate `check`.

## Physical and status boundary

This result is L1 exact algebra only. It creates no action carrier, vacuum
mechanism, phase law, `h`, `hbar`, SI normalization, decoder field, time
orientation, physical continuum, entropy-area identification, or lift to
L2-L6. It changes no Canon, Registry, Frontier, dependency, gate, release, or
existing public status. Public Canon v68 remains authoritative and unchanged.
