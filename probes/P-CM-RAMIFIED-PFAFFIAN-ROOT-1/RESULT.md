# P-CM-RAMIFIED-PFAFFIAN-ROOT-1 result

Status: **candidate-T / L1 / CM-RAMIFIED-PFAFFIAN-ROOT CONFIRMED LOCALLY /
PUBLIC CANON STATUS UNCHANGED.**

The accepted immutable verifier was read back from the public pin before
execution. It exited zero, wrote empty stderr and produced the exact committed
`EXPECTED.txt` bytes. All ten frozen audit gates passed. No scientific
falsifier fired and no equation, carrier, marking, threshold or interpretation
moved after the pin.

## Exact result

For the public marked CM pencil

```text
Omega_(a,b)=a Omega_1+b Omega_2,
q(a,b)=Pf(Omega_(a,b))=a^2-ab-b^2,
eta_(a,b)=(a-b)+b phi,
```

reduction at the unique ramified prime `(1-zeta_5)` gives

```text
phi -> 3,
rho(Omega_(a,b))=a+2b mod 5,
q(a,b)=rho(Omega_(a,b))^2 mod 5.
```

The identity is integral:

```text
(a+2b)^2-q(a,b)=5b(a+b).
```

Among rational primes, five is the unique prime at which this binary norm form
becomes the square of a nonzero linear form. For odd primes the obstruction is
the discriminant `5`; in characteristic two the cross term survives while a
linear square has none.

## Marked C4 phase and its C2 quotient

On the unimodular locus `q(a,b)=+-1`, `rho` is nonzero. Define the frozen
marked phase

```text
R(Omega)=rho(Omega)^-1 in F_5^*.
```

Then exactly

```text
Pf(Omega) mod 5 = R(Omega)^2,
chi_5(R(Omega)) = Pf(Omega) in {+1,-1}.
```

Thus the four-dimensional orientation is the quadratic `C4 -> C2` quotient of
the marked ramified phase. Direct Pfaffian reduction is not the QR/NQR bridge:
`Pf mod 5` is always `1` or `4`, both quadratic residues.

The marking is load-bearing. `R` is relative to the public
`lambda_1,Omega_1,Omega_2` choice. No unmarked or Galois-invariant phase
selector is claimed.

## Exact unit quotient

Using the public real-unit classification `Z[phi]^*={+-phi^k}` and
`phi -> 3 mod 5`, residue inversion gives

```text
R(phi)=2,
im R=F_5^*,
ker R=<-phi^2>.
```

Hence

```text
1 -> <-phi^2> -> Z[phi]^* -> F_5^* -> 1
```

is exact.

The ramified four-phase carrier is therefore a finite quotient of the marked
real Pell-unit axis.

## Pell orbit and Thue-Morse composition

For the public Fibonacci/Pell orbit

```text
Omega_k=F_(k+1) Omega_1+F_k Omega_2,
```

the normalized parameter is `eta_k=phi^k`, including `eta_0=1`. Therefore

```text
R(Omega_k)=2^k mod 5.
```

Composing with the public `RAMIFIED-TM-LIFT [T]` at `k=s_2(n)` gives for every
`n>=0`

```text
R(Omega_(s_2(n)))=Theta_n,
Pf(Omega_(s_2(n)))=Theta_n^2=(-1)^theta_n.
```

The previously exposed binary symplectic-orientation seam is thus the C2
quotient of this marked C4 lift. The real alternating form and the ramified
phase remain different carriers.

## Dynamical intertwining

Let the public Pell shift be

```text
S(a,b)=(a+b,a).
```

It multiplies the normalized parameter by `phi`. On the unimodular locus,

```text
Pf(S Omega)=-Pf(Omega),
R(S Omega)=2 R(Omega).
```

For `Omega_hat_n=Omega_(s_2(n))`, the all-index identity

```text
s_2(n+1)-s_2(n)=1-nu_2(n+1)
```

therefore yields

```text
Omega_hat_(n+1)=S^(1-nu_2(n+1)) Omega_hat_n,
R(Omega_hat_(n+1))
 =2^(1-nu_2(n+1)) R(Omega_hat_n).
```

This is exactly the chronological multiplier of the public ramified
Thue-Morse lift after the marked CM phase map.

The public J-pullback satisfies

```text
A_J=S^-2.
```

Consequently

```text
Pf(P_J Omega)=Pf(Omega),
R(P_J Omega)=-R(Omega).
```

One J-pullback preserves the C2 orientation but applies the half-turn on the
marked C4 phase.

Finally,

```text
Pf(-Omega)=Pf(Omega),
R(-Omega)=-R(Omega).
```

So negation reverses the marked full phase, not the four-dimensional
orientation.

## Prime-five meaning

The new five-specific statement is narrow and exact. The same quadratic form
has discriminant five, and exactly at the ramified prime five its two
conjugate linear factors collapse to one repeated line. The finite
`F_5^* ~= C4` phase is the residue-inverse of that marked line. No wider
physical selection of `p=5` is inferred from this theorem alone.

## Scope firewall

This is L1 exact arithmetic only. It supplies no action, `h`, `hbar`, `2 pi`,
SI normalization, physical `U(1)`, electromagnetic phase, checkpoint
coordinate, 20-state attractor map, P1 map, torus, decoder completion,
continuum geometry, apparatus, L5 event stream or L6 measure.

The additive index-five primary-lattice seam from
`P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1` is a different comparison object.
It is not a dependency and is not identified with this multiplicative C4
quotient.

## Proof and audit status

The written proof in `PREREG.md` carries the universal statements. The exact
verifier audits the frozen residue classes, exponent classes, Pell ranges,
large Thue-Morse prefix, intertwining signs and guards. The bounded audits are
not substituted for proof.

Local evidence:

```text
pin_commit:       b714703b519f28eca9b0cc017431d74f9a3ce723
prereg_sha256:    29158586aa9b5dad6a591fc1ee354d1142f3b92ce26e7d18271e1b5288e35f83
verifier_sha256:  0ede3dd26e96ff0465dcb566a1a6b1a9174109274ab2b2e73fcfc20cbdd1a458
local_platform:   Debian GNU/Linux 13
local_arch:       x86_64
local_python:     3.13.5
local_exit:       0
local_stderr:     0 bytes
stdout_bytes:     786
stdout_lines:     11
stdout_sha256:    d4ade9939ad8b203b52d404a212a0f30b5ec6a13e1a0ed5fb3bdc1f95e478294
```

The local lane alone does not satisfy the public two-architecture gate. A
later public row may be considered only after byte-identical x86_64 and
aarch64 workflow output plus the aggregate check. This probe itself changes no
Canon, registry or frontier file.
