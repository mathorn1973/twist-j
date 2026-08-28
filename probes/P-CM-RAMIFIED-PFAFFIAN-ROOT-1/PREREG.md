# P-CM-RAMIFIED-PFAFFIAN-ROOT-1 preregistration

Date: 2026-08-28

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. The accepted
verifier has been statically parsed but has not been imported or executed.
`PREREG.md` and `verify.py` must be committed and pushed together, then read
back byte for byte from the public remote before the first formal run.

```text
claim issue: 642
branch:      probe/P-CM-RAMIFIED-PFAFFIAN-ROOT-1
path:        probes/P-CM-RAMIFIED-PFAFFIAN-ROOT-1/
owner:       A. M. Thorn
mode:        RESULT-EXPOSED, proof-first; verifier is an exact audit
layer:       L1 exact arithmetic only
ceiling:     candidate-T
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
BASE_COMMIT:    524e9ca94124a265425be1bededbe2d054ff5485
```

The exact issue, pull-request, remote-ref, probe-path and registry searches for
this identifier were empty before issue 642 and branch creation. Issue 642
owns this one probe.

This probe is `RESULT-EXPOSED`. The candidate identities were derived in
public conversation before the pin. That derivation is provenance only, not
evidence. The verifier below is a fresh deterministic standard-library
implementation. Before the pin it was only statically parsed.

## Existing public ownership

The probe consumes only registered public facts at their current scopes.

1. `CM-ALTERNATING-PENCIL [T]` owns the marked anti-real line, the public
   forms `Omega_1,Omega_2`, the formula
   `Pf(a Omega_1+b Omega_2)=a^2-ab-b^2`, the integral unimodular Pell locus,
   the Fibonacci/Pell orbit, the Pell parameter action, and the J-pullback
   matrix `A_J=[[1,-1],[-1,2]]`.
2. `RAMIFIED-TM-LIFT [T]` owns `J_lambda=2` in `F_5^*`,
   `Theta_n=2^s_2(n)`, `theta_n=s_2(n) mod 2`, the sign quotient, and the
   chronological carry law.
3. `J-HARMONIC-SEAM [T]` owns `O_K^*=mu_10 x <phi>` and the real-unit
   classification `Z[phi]^*={+-phi^m:m in Z}`.
4. `J-GOLDEN-BRIDGE [T]` owns `J phi=zeta_5`; equivalently the residue
   calculation `phi=3 mod (1-zeta_5)` can be derived directly from
   `phi=-zeta_5^2-zeta_5^3`.

No candidate-T row is required as a theorem dependency. In particular the
additive primary-lattice seam probe is only a comparison guard and is not
used to establish any statement below.

## Field 1. Equations and carriers

Let the marked CM pencil be

```text
Omega_(a,b) = a Omega_1 + b Omega_2,
q(a,b) = Pf(Omega_(a,b)) = a^2-ab-b^2.
```

From `lambda_2=lambda_1 phi^-1`, write its normalized parameter as

```text
eta_(a,b) = a+b phi^-1 = (a-b)+b phi in Z[phi].
```

At the unique ramified prime `(1-zeta_5)`, reduction sends `zeta_5` to `1`,
so

```text
phi=-zeta_5^2-zeta_5^3 -> -2 = 3 mod 5,
eta_(a,b) -> (a-b)+3b = a+2b mod 5.
```

Freeze

```text
rho(Omega_(a,b)) := a+2b mod 5.
```

On the unimodular locus `q(a,b)=+-1`, `rho` is nonzero. Define the marked
four-phase read

```text
R(Omega_(a,b)) := rho(Omega_(a,b))^-1 in F_5^*.
```

This inverse convention is frozen because it maps the public positive Pell
generator `phi` to the public ramified generator `2`.

The carrier is L1 only:

```text
U_CM = {Omega_(a,b): a,b in Z, q(a,b)=+-1},
F_5^* = {1,2,3,4},
C2 = {+1,-1}.
```

No checkpoint, attractor, decoder, physical state, continuum carrier or
higher action layer is part of this probe.

## Frozen theorem candidate

Maximum later public row:

```text
CM-RAMIFIED-PFAFFIAN-ROOT [T ceiling; L1].
```

### S1. Ramified linear root

For all integers `a,b`,

```text
q(a,b) = (a+2b)^2 mod 5.
```

Indeed,

```text
(a+2b)^2-q(a,b) = 5b(a+b).
```

Thus the marked Pfaffian norm form acquires the linear root
`rho=a+2b` at the ramified prime five.

### S2. Prime uniqueness

Among rational primes `ell`, five is the unique prime for which `q mod ell`
is the square of a nonzero linear form.

For odd `ell`, the discriminant of

```text
q(a,b)=a^2-ab-b^2
```

is

```text
(-1)^2-4(1)(-1)=5.
```

A nonzero square of a linear form has discriminant zero, so such a square is
possible only when `ell|5`, hence `ell=5`; S1 supplies the witness. At
`ell=2`, the reduction `a^2+ab+b^2` has a nonzero cross term, while every
linear square `(ua+vb)^2` in characteristic two has zero cross term.

### S3. Pfaffian is the C2 quotient of the marked C4 phase

On `U_CM`,

```text
Pf(Omega) mod 5 = R(Omega)^2,
chi_5(R(Omega)) = Pf(Omega) in {+1,-1},
```

identifying `-1` with `4 mod 5`.

Proof: S1 gives `Pf=rho^2`. Since `rho in F_5^*`, `rho^4=1`, hence
`R^2=rho^-2=rho^2`. Euler's quadratic-character exponent on `F_5^*` is
also `x^2`.

### S4. Exact unit quotient

The marked phase extends to the real unit group as the residue-inverse
homomorphism

```text
R : Z[phi]^* -> F_5^*.
```

It obeys

```text
R(phi)=2,
im R=F_5^*,
ker R=<-phi^2>.
```

Therefore

```text
1 -> <-phi^2> -> Z[phi]^* -> F_5^* -> 1
```

is exact.

Proof: every real unit is `+-phi^k`. Since `phi -> 3`, the inverse residue is
`+-2^k`. The image is all four nonzero residues. It equals one exactly for
`phi^(4m)` or `-phi^(4m+2)`, which are precisely the powers of `-phi^2`.

### S5. Full Pell C4 phase

For

```text
Omega_k=F_(k+1) Omega_1+F_k Omega_2,  k>=0,
```

the normalized parameter is

```text
eta_0=1,
eta_k=F_(k-1)+F_k phi=phi^k for k>=1.
```

Hence

```text
R(Omega_k)=2^k mod 5.
```

### S6. Composition with the public Thue-Morse lift

For every `n>=0`,

```text
R(Omega_(s_2(n))) = 2^s_2(n) = Theta_n,
Pf(Omega_(s_2(n))) = Theta_n^2 = (-1)^theta_n.
```

The second line is the C2 quotient of the first. The real form and the
ramified phase remain different carriers.

### S7. Pell-shift intertwining and chronological law

Let the public Pell shift be

```text
S(a,b)=(a+b,a).
```

It multiplies the normalized parameter by `phi`, so on `U_CM`

```text
Pf(S Omega)=-Pf(Omega),
R(S Omega)=2 R(Omega).
```

Set `Omega_hat_n=Omega_(s_2(n))`. The exact bit-count identity

```text
s_2(n+1)-s_2(n)=1-nu_2(n+1)
```

gives

```text
Omega_hat_(n+1)=S^(1-nu_2(n+1)) Omega_hat_n,
R(Omega_hat_(n+1))
 = 2^(1-nu_2(n+1)) R(Omega_hat_n).
```

This is exactly the public `RAMIFIED-TM-LIFT` chronological multiplier after
the marked CM phase map.

### S8. J-pullback half-turn

The public J-pullback matrix is

```text
A_J=[[1,-1],[-1,2]]=S^-2.
```

Therefore on `U_CM`

```text
Pf(P_J Omega)=Pf(Omega),
R(P_J Omega)=-R(Omega).
```

So one J-pullback preserves the C2 orientation while applying the half-turn
on the marked C4 phase.

### S9. Direct Pfaffian reduction guard

For every unimodular form,

```text
Pf(Omega) mod 5 in {1,4},
```

and both residues are quadratic residues. QR/NQR is therefore not obtained by
applying the quadratic character to the direct Pfaffian residue. It is the
C2 quotient of the marked phase `R`.

### S10. Negation guard

Because the Pfaffian has degree two,

```text
Pf(-Omega)=Pf(Omega).
```

But the marked residue root is linear, hence

```text
R(-Omega)=-R(Omega).
```

Thus `Omega` and `-Omega` are opposite marked C4 phases with the same
four-dimensional orientation.

## Written proof ownership

The displayed derivations carry the universal quantifiers. The verifier below
audits exact algebra, finite residue classes, finite exponent representatives,
and large deterministic prefixes. No bounded scan is promoted into an
all-index or all-prime proof.

## Field 2. Accepted code

```text
file:    probes/P-CM-RAMIFIED-PFAFFIAN-ROOT-1/verify.py
sha256:  0ede3dd26e96ff0465dcb566a1a6b1a9174109274ab2b2e73fcfc20cbdd1a458
bytes:   6036
lines:   211
LF:      yes, including final LF
runtime: Python standard library only
```

The code uses integer arithmetic only, reads no files, opens no network,
starts no subprocess, and writes fixed stdout. Before the pin it was only
statically parsed.

Run from repository root with

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-CM-RAMIFIED-PFAFFIAN-ROOT-1/verify.py
```

## Field 3. Audit carrier

```text
G1   all 25 residue pairs in F_5^2 for q=rho^2;
G2   symbolic discriminant 5, characteristic-two guard, prime audit <=997;
G3   complete C2 x Z/4 exponent classes for the real-unit quotient;
G4   exact Fibonacci coefficient recurrence through k=1024;
G5   Pell phase, Pfaffian and chi_5 through k=4096;
G6   composed TM/C4/C2 identity for all n<2^18;
G7   chronological carry identity for all n<2^18;
G8   every unimodular pair in [-50,50]^2 for Pell shift;
G9   every unimodular pair in [-50,50]^2 for J-pullback;
G10  every unimodular pair in [-100,100]^2 for direct-Pf and negation guards.
```

These finite ranges audit the implementation and sign conventions only.

## Field 4. Systematics and scope

There is no approximation or fitted parameter. The only material risks are a
misstated public dependency, a marking/sign convention error, a false
discriminant argument, a bad unit-kernel classification, a wrong Pell
intertwiner, or an implementation defect.

The word `marked` is load-bearing. `R` is defined relative to the public
`lambda_1,Omega_1,Omega_2` marking. This probe does not prove an unmarked or
Galois-invariant phase selector.

The additive index-five primary-lattice seam is not this object. It is not a
dependency and no equality with it is claimed.

## Field 5. Falsifiers and stop conditions

```text
F1   Any inherited public dependency is false or misstated at the used scope.
F2   Some integers a,b violate q(a,b)=(a+2b)^2 mod 5.
F3   Some rational prime ell!=5 makes q mod ell a nonzero linear square,
     or ell=5 fails to do so.
F4   R is ill-defined on a unimodular form, or Pf!=R^2 or chi_5(R).
F5   R(phi)!=2, im R!=F_5^*, or ker R!=<-phi^2>.
F6   Some Pell rung has eta_k!=phi^k or R(Omega_k)!=2^k.
F7   Some n>=0 violates R(Omega_s2(n))=Theta_n or its C2 quotient.
F8   The Pell-shift or chronological intertwining law fails.
F9   J-pullback fails to preserve Pfaffian or fails to send R to -R.
F10  Direct Pfaffian reduction gives NQR, or -Omega changes orientation.
```

Formal execution passes only if the pinned script exits zero, writes empty
stderr, emits ten `G* PASS` lines plus the final `ALL PASS` line, and matches
one committed `EXPECTED.txt` byte for byte on both required architectures.

STOP on authority drift, collision, pre-pin import or execution, post-pin
mutation, hidden floating point, bounded search substituted for proof,
architecture-dependent stdout, nonempty stderr, or expansion beyond L1.

## Field 6. Action layer and firewall

Action layer: `L1`.

No action, `h`, `hbar`, `2 pi`, SI normalization, physical phase law,
electromagnetism, checkpoint coordinate, attractor map, decoder completion,
P1 map, torus, L2 geometry, continuum, apparatus, L5 event stream or L6
measure is claimed. No cross-layer gate is opened or implied.

## Formal order

1. Commit and push this file and `verify.py` together.
2. Read both remote blobs back byte for byte and verify SHA-256, bytes, LF and
   final LF.
3. Only then execute the pinned verifier formally.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after the run.
5. Open one probe-only pull request and require byte-identical x86_64,
   aarch64 and aggregate checks.
6. Never amend, rebase, squash, force-push, rename, resume or reuse the branch
   after the pin. A Canon fold, if earned, is separate.
