# P-J-ODD-MOTOR-BRIDGE-HARDENING-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION. RESULT-EXPOSED. NO FORMAL SCIENTIFIC EXECUTION YET.**

Claim lock: issue #536.
Owner session: `chatgpt-gpt56pro-2026-08-23-odd-motor-hardening`.
Target line: PUBLIC.
Layer: **L1 exact arithmetic and exact linear algebra only**.

```text
STATE:          ACTIVE
CANON:          Public Canon v61
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v61
CONTENT_COMMIT: 76b405033b41397cd62217bf3998ac9c26111964
CANON_SHA256:   e9ee0781e489e1c3951b978be567a19c5c7370708095631f966561efe03b6cb5
CANON_BYTES:    334100
BASE_COMMIT:    94bca32b151e161322c4437e8317a03e653e35fa
```

The immutable predecessor evidence is `P-J-ODD-MOTOR-MEDIATED-BRIDGE-2`. This probe does not amend, repair, reopen, or reuse it. Public Canon v61 already registers `J-ODD-MOTOR-MEDIATED-BRIDGE [T]`. This probe supplies missing exact audit objects for two clauses and adds one finite channel classification.

A prior independent audit exposed the target statements as true before this preregistration. That exposure is discovery context only. The accepted verifier below is a fresh standard-library exact implementation. No float, tolerance, randomness, input file, environment input, network, or third-party library is admitted.

## Frozen carrier

Use exactly

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]],
D=M_J-I,
G=I-(1/5)11^T,
X^sharp=G^-1 X^T G.
```

Let `v_x=D^x e_0`, `x in F_5`. Let `rho(a,b)` be the unique rational map with `rho(a,b)v_x=v_(ax+b)`. For each token `k`, define the same stabilizer element and projectors as the predecessor:

```text
g_k=rho(2,k(1-2)),
P_k=(1/4) sum_(a in F_5^*) rho(a,k(1-a)),
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=I-P_k-R_k.
```

No alternative carrier, basis, equality, Gram form, adjoint, token action, projector, or normalization is admitted after the pin.

## H1. Exact native irreducibility and primitive sectors

Recover

```text
chi_M(x)=x^4-3x^3+4x^2-2x+1
        =(x^2-alpha_u x+alpha_u)(x^2-alpha_s x+alpha_s),
alpha_u=(3+sqrt5)/2,
alpha_s=(3-sqrt5)/2.
```

Calculate the exact discriminants in `Q(sqrt5)`:

```text
delta_u=(-5-sqrt5)/2,
delta_s=(-5+sqrt5)/2.
```

The verifier must evaluate each under both real embeddings by exact rational square comparison, not decimal approximation or a constant boolean. All four signs must be strictly negative. It must then calculate a Bezout identity for the two factors, evaluate the resulting CRT idempotents at `M_J`, and require:

```text
e_u^2=e_u,
e_s^2=e_s,
e_u e_s=0,
e_u+e_s=I,
rank(e_u)=rank(e_s)=2.
```

One factor mismatch, one nonnegative embedding value, a nontrivial gcd, an idempotent failure, or a rank other than two fires H1.

## H2. Explicit Schur complement

Set

```text
A_1=D-D^4,
H_k=g_k+g_k^-1,
L_k(z,t)=zI-(H_k+tA_1).
```

For every token, assemble the block matrices as formal Laurent matrices over `Q[z,t,z^-1]`. Require coefficient by coefficient:

```text
C L C = z C,
(C L C)^-1=z^-1 C,
P L R=0,
P L C=-t P A_1 C,
C L R=-t C A_1 R,
```

and

```text
S_PR=P L R-P L C(C L C)^-1 C L R
    =-(t^2/z)P A_1 C A_1 R.
```

The formal adjoint products must be

```text
S_PR^sharp S_PR=(5/4)(t^4/z^2)R,
S_PR S_PR^sharp=(5/4)(t^4/z^2)P.
```

This is the exact squared-magnitude statement behind `sqrt5 t^2/(2z)`. It has no physical frequency or resonance meaning.

## H3. Frozen primitive-channel census

Freeze

```text
U_c=c1 D+c2 D^2+c3 D^3+c4 D^4,
(c1,c2,c3,c4) in {-2,-1,0,1,2}^4 minus zero.
```

The box contains exactly 624 channels. A channel survives only if, for all five tokens,

```text
U_c^sharp=-U_c,
P U_c P=R U_c R=C U_c C=0,
P U_c R=R U_c P=0,
rank(P U_c C)=rank(C U_c P)=rank(R U_c C)=rank(C U_c R)=1,
B=P U_c C U_c R has rank one,
B^sharp B=(5/4)R,
B B^sharp=(5/4)P,
```

and the two normalized active rank-one lines inside `C` have squared overlap `1/5`.

The exact ordered survivor list is frozen:

```text
(-1,0,0,1),
(0,-1,1,0),
(0,1,-1,0),
(1,0,0,-1).
```

Equivalently the four channels are

```text
+/- (D-D^4),
+/- (D^2-D^3).
```

Finally require

```text
rho(2,0)(D-D^4)rho(2,0)^-1=D^2-D^3.
```

The earned uniqueness is only inside this frozen coefficient box and only up to sign and affine conjugation.

## Decision

```text
HARDENING-CERTIFIED
  carrier integrity and every H1-H3 statement pass exactly.

ROUTE-FALSIFIED
  carrier integrity passes but at least one frozen mathematical statement fails.
  Preserve the smallest exact witness and do not alter this probe.

STOP
  authority, collision, pin order, blob readback, exactness, deterministic
  execution, stderr, security, mutation, or architecture requirement fails.
```

No numerical threshold exists. Every condition is an exact equality, sign comparison, rank, finite census, or formal Laurent-polynomial identity.

## Maximum later scope and firewall

A later separately locked fold may use this evidence to harden `J-ODD-MOTOR-MEDIATED-BRIDGE [T]` and may add only the finite H3 uniqueness clause. It may not claim unrestricted channel uniqueness or choose a mediator basis.

No material, phonon, amplitudon, susceptibility, frequency, damping, temperature, light coupling, Born rule, probability, observer, decoder, apparatus, force, spacetime, SI value, or L2-L6 lift is assumed or concluded.

## Formal order

1. Commit and push this `PREREG.md` and the accepted `verify.py` together before the first scientific execution.
2. Read both files back from that exact commit and record Git blob IDs, SHA-256, bytes, lines, LF and final LF.
3. Execute the exact readback once. Require exit 0 and empty stderr. Save stdout byte for byte as `EXPECTED.txt`.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` in the result commit.
5. Open one pull request changing only this probe directory. Require byte-identical x86_64 and aarch64 output plus aggregate `check`.
6. Never amend, rebase, squash, force-push, change the box or battery, move a threshold, or reuse this identifier after the pin.
