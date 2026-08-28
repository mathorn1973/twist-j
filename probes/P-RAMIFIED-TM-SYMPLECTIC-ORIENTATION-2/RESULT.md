# P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2 result

Status: **candidate-T / L1 / RAMIFIED-TM-SYMPLECTIC-ORIENTATION CONFIRMED LOCALLY / PUBLIC CANON STATUS UNCHANGED.**

The first formal execution of the immutable verifier exited zero, wrote empty
stderr and produced the exact committed `EXPECTED.txt` bytes. All eight frozen
audit gates passed. No scientific falsifier fired and no equation, carrier,
threshold or interpretation moved after the pin.

## Exact result

Let

```text
Omega_k = F_(k+1) Omega_1 + F_k Omega_2,
Omega_1 = (1,0,0,1,0,1),
Omega_2 = (0,1,-1,0,1,0).
```

Relative to the fixed orientation of the integral rank-four lattice, the
symplectic orientation character is

```text
epsilon(Omega_k)=Pf(Omega_k)=(-1)^k.
```

This is inherited from the public Pfaffian pencil formula together with the
written recurrence proof in `PREREG.md`.

On `F_5^*`, let `chi_5` be the quadratic character. Since `2` is a
quadratic nonresidue,

```text
chi_5(2^k)=(-1)^k.
```

For the public ramified Thue-Morse lift

```text
Theta_n=2^s_2(n) mod 5,
theta_n=s_2(n) mod 2,
```

one therefore has for every `n>=0`

```text
epsilon(Omega_(s_2(n)))
 = chi_5(Theta_n)
 = (-1)^theta_n.
```

The real symplectic orientation character and the ramified QR/NQR character
are the same binary character of the count. They remain different carriers;
neither is identified with the other.

## Full-state factor and checkpoint no-go

The character is a function of the complete autonomous state because the
counter is part of that state:

```text
H(n,psi)=(-1)^theta_n.
```

It is not a function of the finite checkpoint alone on the full forward
carrier. The inherited theorem `CARRY-J-CHECKPOINT [T]` gives

```text
psi_4=psi_6
```

for every seed, while

```text
s_2(4)=1,  epsilon(Omega_1)=-1,  chi_5(Theta_4)=-1,
s_2(6)=2,  epsilon(Omega_2)=+1,  chi_5(Theta_6)=+1.
```

Hence no single-valued map

```text
h:F_5^6->{+1,-1}
```

realizes this character on that carrier. The missing datum is the counter, not
a hidden orientation coordinate inside the checkpoint.

## Two guards

First, direct Pfaffian reduction does not produce QR versus NQR:

```text
Pf(Omega_k) mod 5 is 1 or 4,
```

and both values are quadratic residues. The bridge passes through the
quadratic character of the ramified phase `Theta_n`.

Second, in four dimensions the Pfaffian is quadratic:

```text
Pf(-w)=Pf(w).
```

Therefore `w` and `-w` determine the same four-dimensional orientation. The
two orientation classes above are not the pair `w,-w`.

## Twenty-counter witness

For the counter prefix `n=0,...,19`, the character splits exactly ten values
`+1` and ten values `-1`. This is only a finite prefix of the counter. It is
not a map from, or statement about, a 20-checkpoint attractor.

## Scope firewall

This result supplies no action, `h`, `hbar`, `2 pi`, SI normalization, phase
law, real-place selection, P1 map, torus, decoder completion, continuum,
physical discreteness, apparatus, event stream or measure. It does not show
that spacetime is discrete and does not identify QR/NR with physical sides of
a symplectic cell.

The exact gain is narrower:

```text
one binary count character has two exact L1 realizations,
one symplectic and one ramified,
and the finite checkpoint forgets it.
```

## Pin and local run

```text
claim_issue:       639
pin_commit:        489b28ae6d91718652f576cddf8c02b645e49571
prereg_sha256:     dd1c1bfa1330e9deb5e5679d02ff100173dc1f32e32b7cf3369e22a898d00bd1
verifier_sha256:   eb1deaf17234e3ce436dc1eb9e93aa88d6b40891dc2f0613e6b2275a88870384
local_platform:    Debian GNU/Linux 13
local_architecture:x86_64
local_python:      3.13.5
local_exit:        0
local_stderr:      0 bytes
stdout_bytes:      391
stdout_lines:      9
stdout_sha256:     8445d1c0fcb96db62f033932732f448759d5cd685b5aeb13e5c976c0a1c6af8a
```

The written proof carries the universal result. The exact verifier audits the
frozen finite ranges and guards. The local lane alone does not satisfy the
public two-architecture gate. A later public row may be considered only after
byte-identical x86_64 and aarch64 workflow output plus the aggregate check.
This probe itself changes no Canon, registry or frontier file.
