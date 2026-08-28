# P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No
scientific result is earned by this file. The accepted `verify.py` may be
read, parsed, compiled and inspected statically before the pin, but it has not
been imported or executed. This file and `verify.py` must be committed
together, pushed, and read back byte for byte from the public remote before the
first formal scientific execution.

Public claim lock: issue 635, opened before this file was committed.

```text
branch:  probe/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1
path:    probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; verifier is an exact audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v68
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v68
TAG_TARGET:     b72505f55bcf2ef3d5985065ae52f3365966f32e
CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581
CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546
CANON_BYTES:    353145
BASE_COMMIT:    0a7f87495d7df37a6acbfe8ac906593e844472cf
ACTION_LAYER:   L1 exact arithmetic only
```

Immediately before issue lock and branch creation, `STATUS.md`, `POLICY.md`,
`AGENTS.md`, `canon/CORE.md`, `canon/FRONTIER.md`, the registry, the annotated
tag, release assets, current `main`, exact remote branch name, public probes,
and open and closed issues and pull requests were read from the public remote.
The declared content commit is an ancestor of current `main`; the v68 tag,
Canon hash and byte count match the active authority; the required publication
and current-main architecture checks are successful.

This probe changes exactly its own directory. It changes no Canon, registry,
frontier, dependency, evidence, gate, release, workflow or decoder file.

## Collision, prior exposure and adjacent ownership

No issue, pull request, remote branch, public probe path or registry row named
`P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1` or
`RAMIFIED-TM-SYMPLECTIC-ORIENTATION` existed at claim time. Issue 635 now owns
this one probe.

This probe is `RESULT-EXPOSED`. The main identity was derived in public
conversation before the pin. That derivation is provenance only, not evidence.
The verifier below is a fresh deterministic standard-library implementation.
It has been statically parsed but never imported or executed.

Existing public claims retain ownership:

1. `CM-ALTERNATING-PENCIL [T]` owns the integral alternating forms
   `Omega_1`, `Omega_2`, the formula
   `Pf(a Omega_1+b Omega_2)=a^2-ab-b^2`, and the Fibonacci/Pell unimodular
   orbit with Pfaffian `(-1)^k`.
2. `RAMIFIED-TM-LIFT [T]` owns `J_lambda=2` in `F_5^*`,
   `Theta_n=2^s_2(n)`, `q(Theta_n)=theta_n`, and
   `Theta_n^2=(-1)^theta_n`.
3. `CARRY-J-CHECKPOINT [T]` owns the universal collision
   `psi_4=psi_6` for every seed and the phase values
   `Theta_4=2`, `Theta_6=4`.
4. This probe earns only the exact character-level composition, the resulting
   binary checkpoint no-go, and the direct-reduction and negation guards. It
   does not re-earn its dependencies.

## Field 1. Frozen equation and carriers

Let

```text
F_0 = 0,  F_1 = 1,  F_(k+2) = F_(k+1)+F_k.
```

Use the public alternating forms in upper-triangular coordinate order
`(w01,w02,w03,w12,w13,w23)`:

```text
Omega_1 = (1,0, 0,1,0,1),
Omega_2 = (0,1,-1,0,1,0).
```

For `k>=0`, define

```text
Omega_k = F_(k+1) Omega_1 + F_k Omega_2.
```

For `w=(w01,w02,w03,w12,w13,w23)`, use

```text
Pf(w) = w01 w23 - w02 w13 + w03 w12.
```

Every `Omega_k` is unimodular. Relative to the fixed lattice orientation,
define its symplectic orientation character by

```text
epsilon(Omega_k) = Pf(Omega_k) in {+1,-1}.
```

This is the sign of `(1/2) Omega_k wedge Omega_k` relative to the fixed
oriented lattice volume. It is not the sign of the two-form itself.

On `F_5^*={1,2,3,4}`, define the quadratic character

```text
chi_5(1)=chi_5(4)=+1,
chi_5(2)=chi_5(3)=-1.
```

Let `s_2(n)` be the binary digit sum,

```text
theta_n = s_2(n) mod 2,
Theta_n = 2^s_2(n) mod 5.
```

The public sign quotient `q:F_5^* -> F_2` obeys

```text
chi_5(x)=(-1)^q(x).
```

The full autonomous state carrier used here is only

```text
Omega_aut = N_0 x F_5^6.
```

No parity function on all of `Z_2` is asserted.

## Frozen theorem candidate

The maximum later claim is

```text
RAMIFIED-TM-SYMPLECTIC-ORIENTATION [T ceiling; L1].
```

It contains exactly the following parts.

### S1. Pell orientation character

For every `k>=0`,

```text
Pf(Omega_k)=(-1)^k.
```

### S2. Ramified QR/NQR character

For every `k>=0`,

```text
chi_5(2^k mod 5)=(-1)^k.
```

### S3. Character seam

For every `n>=0`,

```text
epsilon(Omega_(s_2(n)))
 = chi_5(Theta_n)
 = (-1)^theta_n.
```

Thus the real symplectic orientation character and the ramified QR/NQR
character are the same binary character of the count. They live on different
carriers. Neither carrier is identified with the other.

### S4. Full-state factor and checkpoint no-go

The character factors through the full autonomous state:

```text
H(n,psi)=(-1)^theta_n.
```

It does not factor through the checkpoint alone on the full forward carrier.
The inherited theorem gives `psi_4=psi_6` for every seed, while

```text
s_2(4)=1,  epsilon(Omega_1)=-1,
s_2(6)=2,  epsilon(Omega_2)=+1.
```

Equivalently,

```text
chi_5(Theta_4)=chi_5(2)=-1,
chi_5(Theta_6)=chi_5(4)=+1.
```

Hence no single-valued map

```text
h:F_5^6 -> {+1,-1}
```

can realize the character on the full forward carrier.

### S5. Direct-reduction guard

For every `k>=0`,

```text
Pf(Omega_k) mod 5 is 1 or 4.
```

Both values are quadratic residues. Therefore QR/NR is not obtained by
reducing the Pfaffian modulo five. The bridge in S3 passes through the
quadratic character of the ramified phase `Theta_n`.

### S6. Negation guard

For every alternating form `w` in four dimensions,

```text
Pf(-w)=Pf(w).
```

Consequently `w` and `-w` determine the same four-dimensional orientation.
The two orientation classes in S1 are not the pair `w,-w`.

### S7. Twenty-counter witness

For the finite counter prefix `n=0,...,19`, exactly ten values have character
`+1` and ten have character `-1`.

This is a counter-prefix witness only. It is not a statement about a
20-checkpoint attractor, P1 support, a torus, physical action or physical
orientation.

## Written all-index proof

### Proof of S1

`CM-ALTERNATING-PENCIL [T]` gives

```text
Pf(a Omega_1+b Omega_2)=a^2-ab-b^2.
```

Set

```text
D_k=F_(k+1)^2-F_(k+1)F_k-F_k^2.
```

Then `D_0=1`. With `a=F_(k+1)` and `b=F_k`,

```text
D_(k+1)
 =(a+b)^2-(a+b)a-a^2
 =-(a^2-ab-b^2)
 =-D_k.
```

Thus `D_k=(-1)^k`, proving S1.

### Proof of S2

The nonzero squares modulo five are `1` and `4`, so `chi_5(2)=-1`.
Multiplicativity gives

```text
chi_5(2^k)=chi_5(2)^k=(-1)^k.
```

### Proof of S3

Substitute `k=s_2(n)` into S1 and S2 and use the inherited exact identity

```text
Theta_n=2^s_2(n) mod 5
```

and `theta_n=s_2(n) mod 2`.

### Proof of S4

`H(n,psi)=(-1)^theta_n` is a total function on the stated full autonomous
carrier because `n` is part of that carrier. For checkpoint factorization,
`CARRY-J-CHECKPOINT [T]` gives the same checkpoint at times four and six for
every seed. S3 gives opposite character values there. A function cannot assign
two values to one argument, proving the no-go.

### Proof of S5

By S1, `Pf(Omega_k)` is `+1` or `-1`. Modulo five these are `1` and `4`, both
squares.

### Proof of S6

The Pfaffian of a four by four alternating matrix is homogeneous of degree
two. Therefore

```text
Pf(-w)=(-1)^2 Pf(w)=Pf(w).
```

### Proof of S7

Every Thue-Morse block of length `2^m`, `m>=1`, is balanced because its second
half is the complement of its first half. The first sixteen values therefore
split eight and eight. The next four are the complement of the first four,
which themselves split two and two. The total is ten and ten.

The proof above, not the finite verifier ranges, is the proposed theorem
basis.

## Field 2. Accepted code

```text
file:    probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1/verify.py
sha256:  da26458e9ffd6a25eb4165e0860aa1eddc1ce885dedf25f6e40bb7559ed9d626
bytes:   4755
runtime: Python standard library only
```

The code is deterministic, uses integers only, reads no files, opens no
network, starts no subprocess, and writes only its fixed stdout. It was
statically parsed before pinning and was not imported or executed.

Run from repository root with

```text
LC_ALL=C LANG=C PYTHONDWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1/verify.py
```

## Field 3. Frozen audit carrier

The finite audit is fixed as follows:

```text
G1  all a,b in [-32,32] for the Pfaffian pencil formula;
G2  all k in [0,2048] for the Fibonacci/Pell sign;
G3  all k in [0,4096] for the ramified quadratic character;
G4  all n in [0,2^18) for the composed character;
G5  exact times 4 and 6 for the opposite-character collision witness;
G6  all k in [0,2048] for direct Pfaffian reduction;
G7  all k in [0,256] for the four-dimensional negation guard;
G8  the exact prefix n in [0,20) for the ten/ten count.
```

These ranges audit implementation and frozen formulas. They do not establish
the universal statements.

## Field 4. Systematics and scope

The written proof has no numerical approximation. The main risks are a
misstated dependency, a carrier mismatch, a sign convention mismatch, an
incorrect composition, or implementation error.

A failure in an inherited claim is not repaired here. It fires F1 and stops
this candidate. A code or text defect found after the pin leaves both pinned
files unchanged and requires a new identifier. A result record may report a
failure but may not move a threshold.

No claim is made that a checkpoint or a 20-state support alone carries the
orientation character. No action, `h`, `hbar`, `2 pi`, phase law, SI
normalization, real-place selection, decoder completion, probability, torus,
continuum, space, physical discreteness, or L2-L6 lift is included.

## Field 5. Frozen thresholds and falsifiers

```text
F1  Any inherited dependency is false or misstated at the used scope.
F2  The all-index Pell/Pfaffian sign proof has a gap or counterexample.
F3  The all-index quadratic-character proof has a gap or counterexample.
F4  The composed identity fails for some n>=0.
F5  The full-state factor is ill typed, or a checkpoint-only factor exists
    despite the inherited collision and opposite character values.
F6  A direct Pfaffian residue 1 or 4 is a quadratic nonresidue modulo five.
F7  Pf(-w) differs from Pf(w) for a four-dimensional alternating form.
F8  The first twenty counter values do not split ten and ten.
```

Formal execution passes only if the pinned script exits zero, writes empty
stderr, emits all eight PASS lines and `RESULT 8/8 ALL PASS`, and matches the
one committed `EXPECTED.txt` byte for byte on the required x86_64 and aarch64
workflow jobs.

STOP on authority drift, collision, pre-pin execution or import, post-pin
mutation, hidden floating point, bounded search substituted for proof,
architecture-dependent stdout, nonempty stderr, or any expansion beyond L1.

## Formal order

1. Commit and push this file and the accepted `verify.py` together.
2. Read both remote blobs back byte for byte. Record the commit, SHA-256,
   byte count, LF line endings and final LF.
3. Only then execute the pinned script formally on Linux.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after the run.
5. Open one probe-only pull request. Require byte-identical x86_64 and aarch64
   output plus aggregate `check`.
6. Never amend, rebase, squash, force-push, rename, resume or reuse the branch
   after the pin. A Canon fold, if earned, is a separate transaction.
