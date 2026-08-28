# P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. The accepted
verifier has been statically parsed but has not been imported or executed.
`PREREG.md` and `verify.py` must be committed and pushed together, then read
back byte for byte from the public remote before the first formal run.

```text
claim issue: 639
branch:      probe/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2
path:        probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2/
owner:       A. M. Thorn
mode:        RESULT-EXPOSED, proof-first; verifier is an exact audit
layer:       L1 exact arithmetic only
ceiling:     candidate-T
```

## Authority and predecessor

```text
STATE:          ACTIVE
CANON:          Public Canon v68
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v68
TAG_TARGET:     b72505f55bcf2ef3d5985065ae52f3365966f32e
CONTENT_COMMIT: d755c5758406bfed13405dde0864c2ce81f5f581
CANON_SHA256:   63370401c2e25d94e7d8f94bdf142ba32fe3c2a5cdf81d1435114b669b0e5546
CANON_BYTES:    353145
BASE_COMMIT:    493f271285a9b2c683ff91c75c5771ef3a57b7e7
```

The exact issue, pull-request, remote-ref, probe-path and registry searches for
this identifier were empty before issue 639 and branch creation.

`P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-1`, issue 635 and pull request 638, is a
merged `ABANDONED` pin. It was never imported or executed. Its remote readback
found that `PREREG.md` named the SHA-256 and byte count of a local scratch copy
containing a leading backslash plus LF, bytes `5c 0a`, rather than the actual
pinned remote verifier. The old identifier is consumed. This successor does
not resume it. It has a new issue, branch, path, pin, accepted verifier and
metadata.

## Collision, prior exposure and adjacent ownership

No issue, pull request, remote branch, public probe path or registry row named
`P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2` existed at claim time. Issue 639 now
owns this one probe.

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

## Field 1. Equation and carriers

Let `F_0=0`, `F_1=1`, `F_(k+2)=F_(k+1)+F_k`. In upper-triangular coordinate
order `(w01,w02,w03,w12,w13,w23)`, freeze

```text
Omega_1=(1,0,0,1,0,1),
Omega_2=(0,1,-1,0,1,0),
Omega_k=F_(k+1) Omega_1+F_k Omega_2,
Pf(w)=w01 w23-w02 w13+w03 w12.
```

Relative to the fixed lattice orientation, define

```text
epsilon(Omega_k)=Pf(Omega_k) in {+1,-1}.
```

On `F_5^*`, define

```text
chi_5(1)=chi_5(4)=+1,
chi_5(2)=chi_5(3)=-1.
```

Let

```text
theta_n=s_2(n) mod 2,
Theta_n=2^s_2(n) mod 5.
```

The full autonomous carrier used in the factor statement is
`N_0 x F_5^6`. No parity function on all of `Z_2` is asserted.

## Frozen theorem candidate

The maximum later row is

```text
RAMIFIED-TM-SYMPLECTIC-ORIENTATION [T ceiling; L1].
```

S1. For every `k>=0`,

```text
Pf(Omega_k)=(-1)^k.
```

S2. For every `k>=0`,

```text
chi_5(2^k mod 5)=(-1)^k.
```

S3. For every `n>=0`,

```text
epsilon(Omega_(s_2(n)))=chi_5(Theta_n)=(-1)^theta_n.
```

The real symplectic orientation character and the ramified QR/NQR character
are therefore the same binary character of the count on two different
carriers. Neither carrier is identified with the other.

S4. The character factors through the full autonomous state by
`H(n,psi)=(-1)^theta_n`. It does not factor through the checkpoint alone on
the full forward carrier: `psi_4=psi_6`, but the two character values are
`-1` and `+1`. Hence no single-valued `h:F_5^6->{+1,-1}` realizes it there.

S5. Direct reduction of the Pfaffian is not the bridge. For every `k`,
`Pf(Omega_k) mod 5` is `1` or `4`, and both are quadratic residues.

S6. For every alternating four-dimensional form `w`, `Pf(-w)=Pf(w)`. Thus
`w` and `-w` determine the same four-dimensional orientation.

S7. The finite counter prefix `n=0,...,19` contains ten values of each
character. This is not a 20-checkpoint-attractor statement.

## Written proof

For S1, put

```text
D_k=F_(k+1)^2-F_(k+1)F_k-F_k^2.
```

The public Pfaffian formula gives `Pf(Omega_k)=D_k`. With
`a=F_(k+1)`, `b=F_k`,

```text
D_(k+1)=(a+b)^2-(a+b)a-a^2=-D_k,
D_0=1,
```

so `D_k=(-1)^k`.

For S2, the nonzero squares modulo five are `1,4`, hence `chi_5(2)=-1` and
multiplicativity gives `chi_5(2^k)=(-1)^k`.

S3 follows by substituting `k=s_2(n)` and using the public ramified lift. S4
uses the public collision at times four and six. S5 follows from
`+1 mod 5=1`, `-1 mod 5=4`. S6 follows because the four-dimensional
Pfaffian is homogeneous of degree two. S7 follows because every positive
power-of-two Thue-Morse block is balanced: the first sixteen split 8/8 and
the following four, the complement of the first four, split 2/2.

The written proof, not the finite audit ranges, carries the universal claim.

## Field 2. Accepted code

```text
file:    probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2/verify.py
sha256:  eb1deaf17234e3ce436dc1eb9e93aa88d6b40891dc2f0613e6b2275a88870384
bytes:   4753
lines:   154
LF:      yes, including final LF
runtime: Python standard library only
```

The code uses integers only, reads no files, opens no network, starts no
subprocess, and writes fixed stdout. Before the pin it was only statically
parsed.

Run from repository root with

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2/verify.py
```

## Field 3. Audit carrier

```text
G1  all a,b in [-32,32] for the Pfaffian pencil formula;
G2  all k in [0,2048] for the Fibonacci/Pell sign;
G3  all k in [0,4096] for the ramified character;
G4  all n in [0,2^18) for the composed character;
G5  exact times 4 and 6 for the opposite-character collision;
G6  all k in [0,2048] for direct Pfaffian reduction;
G7  all k in [0,256] for the negation guard;
G8  the exact prefix n in [0,20) for the ten/ten count.
```

These ranges audit the implementation. They are not substituted for proof.

## Field 4. Systematics and scope

The proof has no approximation. The risks are a misstated dependency, carrier
or sign convention, an incorrect composition, or an implementation defect. A
failure is recorded; no threshold moves.

No action, `h`, `hbar`, `2 pi`, phase law, SI normalization, real-place
selection, decoder completion, P1 map, torus, continuum, physical discreteness,
L5 event or L6 measure is included. QR/NR is not identified with `+w/-w`.

## Field 5. Falsifiers and stop conditions

```text
F1  Any inherited dependency is false or misstated at the used scope.
F2  The all-index Pell/Pfaffian sign proof fails.
F3  The all-index quadratic-character proof fails.
F4  The composed identity fails for some n>=0.
F5  A checkpoint-only factor exists despite the inherited collision and
    opposite character values.
F6  A direct Pfaffian residue 1 or 4 is a nonresidue modulo five.
F7  Pf(-w) differs from Pf(w) in four dimensions.
F8  The first twenty counter values do not split ten and ten.
```

Formal execution passes only if the pinned script exits zero, writes empty
stderr, emits all eight PASS lines and `RESULT 8/8 ALL PASS`, and matches one
committed `EXPECTED.txt` byte for byte on both required architectures.

STOP on authority drift, collision, pre-pin import or execution, post-pin
mutation, hidden floating point, bounded search substituted for proof,
architecture-dependent stdout, nonempty stderr, or expansion beyond L1.

## Formal order

1. Commit and push this file and `verify.py` together.
2. Read both remote blobs back byte for byte and verify SHA-256, bytes, LF and
   final LF.
3. Only then execute the pinned verifier formally.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after the run.
5. Open one probe-only pull request and require x86_64, aarch64 and aggregate
   checks.
6. Never amend, rebase, squash, force-push, rename, resume or reuse the branch
   after the pin. A Canon fold, if earned, is separate.
