# P-J-ODD-MOTOR-MEDIATED-BRIDGE-2 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION. RESULT-EXPOSED. NO SCIENTIFIC RESULT YET.**

Claim lock: issue #527.
Owner session: `chatgpt-gpt56sol-2026-08-22-odd-motor-bridge`.
Target line: PUBLIC. Layer: **L1 exact arithmetic, finite representation theory, exact linear algebra only**.

```text
STATE:          ACTIVE
CANON:          Public Canon v60
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v60
CONTENT_COMMIT: 18b21bdaf2c2236c9444b120900277ccfb63e050
CANON_SHA256:   9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0
CANON_BYTES:    329876
BASE_COMMIT:    7a0fb56e44e652879aec1cc188a8867c63f39577
```

The predecessor `P-J-ODD-MOTOR-MEDIATED-BRIDGE-1` stopped before execution because its pushed verifier blob did not match the accepted local bytes. It produced no scientific result and is not repaired here.

The candidate formulas were exposed by non-canonical one-platform work. That work is discovery context only. The accepted public verifier is a fresh standard-library exact audit. No float, tolerance, randomness, external data, environment input, network, or third-party library is admitted.

## Frozen carrier

Use the public integer step matrix

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]].
```

Set `D=M_J-I`, `A=D-D^-1=D-D^4`, `S=D+D^-1=D+D^4`. The verifier first recovers `D^5=I`.

Let `v_x=D^x e_0`, `x in F_5`. For `a in F_5^*`, `b in F_5`, let the unique rational map `rho(a,b)` satisfy `rho(a,b)v_x=v_(ax+b)`. Freeze

```text
G = I_4 - (1/5) 11^T,
X^sharp = G^-1 X^T G.
```

For token `k in F_5`, define

```text
h_(a,k)=rho(a,k(1-a)),
g_k=h_(2,k),
P_k=(1/4) sum_(a in F_5^*) h_(a,k),
R_k=(1/4)(I-g_k+g_k^2-g_k^3),
C_k=I-P_k-R_k.
```

No alternative sector decomposition is admitted after the pin.

## G1. Native two-sector no-go

The exact characteristic polynomial is

```text
chi_M(x)=x^4-3x^3+4x^2-2x+1.
```

Over `Q(sqrt5)`, with `alpha_u=(3+sqrt5)/2=phi^2` and `alpha_s=(3-sqrt5)/2=phi^-2`, prove

```text
chi_M=(x^2-alpha_u x+alpha_u)(x^2-alpha_s x+alpha_s).
```

The discriminants are `(-5-sqrt5)/2` and `(-5+sqrt5)/2`. Both are negative under both real embeddings because `sqrt5<3<5`, hence neither is a square in the real field. The factors are distinct irreducibles. CRT gives a product of two fields, so the generated algebra has exactly four idempotents and exactly two primitive nonzero idempotents. Therefore the native real carrier has exactly two primitive rank-two invariant sectors. The naive third-native-sector mediator route is closed negative.

## G2-G4. Odd-channel mediated block

For every token require exact ranks `(rank P,rank R,rank C)=(1,1,2)`, `P+R+C=I`, pairwise G-orthogonality, and

```text
A^sharp=-A,
PAP=RAR=CAC=0,
PAR=RAP=0,
rank(PAC)=rank(CAP)=rank(RAC)=rank(CAR)=1.
```

Thus the odd block graph is exactly `P <-> C <-> R` with no direct `P <-> R` block.

Define `B_k=P_k A C_k A R_k`. The positive route requires

```text
rank(B_k)=1,
B_k^sharp B_k=(5/4)R_k,
B_k B_k^sharp=(5/4)P_k.
```

Hence the normalized second-order magnitude is `sqrt5/2`.

For `U_P=C A P`, `U_R=C A R`, define `L_P=(2/5)U_P U_P^sharp` and `L_R=(2/5)U_R U_R^sharp`. Require

```text
tr(L_P L_R)=1/5.
```

No material or geometric reading is attached to this fraction.

## G5. Frozen negative controls

For each token and each `U` in

```text
D, D^2, D^3, D^4, S=D+D^-1
```

test every ordered distinct sector pair `X,Y` among `P,R,C`, with `Z` the third sector. No control may satisfy simultaneously

```text
X U Y = 0,
X U Z U Y != 0.
```

One exact witness falsifies specificity. The control family may not be reduced after the run.

## G6. Exact Schur/resolvent audit

Set `H_k=g_k+g_k^-1`. Require

```text
H_k P_k=2P_k,
H_k R_k=-2R_k,
H_k C_k=0.
```

For formal `z,t`, let `L_k(z,t)=zI-(H_k+tA)`. Since the C-block is `z I_C`, exact elimination for `z!=0` induces the P-R map `-(t^2/z) P A C A R` up to one-dimensional orientation. Its orientation-independent magnitude is therefore

```text
sqrt5 t^2/(2z).
```

The pole at `z=0` is an algebraic resolvent pole of the eliminated block, not a physical resonance claim.

At token `k=2`, independently evaluate the complete 24-term determinant and require

```text
det L_2(z,t)=z^4+(5t^2-4)z^2+5t^4.
```

`t` is a formal insertion counter, not a physical coupling.

## G7-G8. Minimal quadratic lift

For `G_aff=AGL_1(F_5)`, use the augmentation character

```text
chi_V(g)=#Fix_F5(g)-1,
chi_Sym2(g)=(chi_V(g)^2+chi_V(g^2))/2.
```

With quadratic multiplier character `epsilon(a)=+1` for `a in {1,4}` and `-1` for `a in {2,3}`, exact character inner products over all 20 elements must give

```text
Sym^2(V) ~= 1 + epsilon + 2V,
dim End_G(Sym^2 V)=6,
<1,epsilon>=<1,V>=<epsilon,V>=0.
```

Freeze the two explicit forms

```text
q_+=(5/2)G,
q_-=[[0,1,-1,-1],[1,0,1,-1],[-1,1,0,1],[-1,-1,1,0]].
```

For every affine `rho(a,b)` require `rho^T q_+ rho=q_+` and `rho^T q_- rho=epsilon(a)q_-`.

The complete nonzero ordered trilinear census within `{1,epsilon,V}` is frozen: `1*1*1` has dimension 1; each permutation of `1*epsilon*epsilon`, `1*V*V`, and `epsilon*V*V` has dimension 1; `V*V*V` has dimension 3; all other ordered triples vanish. Multiplicity two of V is a nonselection boundary, not a selected mediator basis.

## Decision

```text
MEDIATED-BRIDGE-CERTIFIED
  carrier integrity and every frozen G1-G8 statement pass exactly.

ROUTE-FALSIFIED
  carrier integrity passes but at least one frozen scientific statement fails.
  Preserve the failing witness and do not modify this probe.

STOP
  authority, collision, blob/pin/readback, exactness, deterministic execution,
  stderr, security, mutation, or architecture requirement fails.
```

No numerical threshold exists. Every decision is an exact equality, rank, finite character sum, or exact polynomial identity.

## Maximum scope and firewall

A later separately locked fold may propose T only at **L1** if the written proof survives and the required two-architecture audit is byte-identical. This probe PR changes no Canon, Registry, Frontier, Evidence, Gate, dependency, status, tag, or release file.

No phonon, amplitudon, ferroaxial order, material, susceptibility, frequency, damping, temperature, laser/light coupling, quantum-state control, Born rule, probability, observer, decoder, force, spacetime, SI value, or L2-L6 lift is assumed or concluded. The word `resonance` is outside the scientific scope.

## Formal order

1. Before pinning, create both Git blobs and require their Git blob SHAs to equal local `git hash-object` exactly.
2. Commit and push this `PREREG.md` and the accepted `verify.py` together in one pin commit.
3. Read both files back from that commit and record blob IDs, SHA-256, bytes, lines, LF and final LF.
4. From exact readback bytes execute once: `python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-2/verify.py`.
5. Require exit 0 and empty stderr. Save stdout byte-for-byte as `EXPECTED.txt`.
6. Add only `EXPECTED.txt`, `RUN.md`, `RESULT.md` in the result commit.
7. Open one PR changing only this probe directory and require x86_64 plus aarch64 byte identity and aggregate `check`.
8. Never amend, rebase, squash, force-push, move a threshold, change a gate, repair the verifier, or reuse this identifier after the pin.
