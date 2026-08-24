# P-J-ODD-MOTOR-MEDIATED-BRIDGE-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION. RESULT-EXPOSED. NO SCIENTIFIC RESULT YET.**

Claim lock: issue #526.

Owner session: `chatgpt-gpt56sol-2026-08-22-odd-motor-bridge`.

Target line: PUBLIC. Action layer: **L1 exact arithmetic, finite representation theory, and exact linear algebra only**.

Base frozen for the pin:

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

The accepted verifier is standard-library only. It uses `Fraction` and exact finite matrices. No float, tolerance, randomness, network, external data, environment input, generated file input, or third-party library is admitted.

## 1. Result exposure and independence boundary

This is not blind discovery. Before this public claim, a non-canonical one-platform SymPy incubation and a separate augmentation-carrier breaker produced the candidate formulas and negative controls. They have no public authority and are not evidence for this probe.

The accepted public `verify.py` is a fresh implementation over `fractions.Fraction`. It reconstructs the public `M_J`, the five-point affine simplex, all projectors, block products, character sums, and the determinant directly. It imports no incubation output and reads no incubation file.

The scientific content below is frozen before the first formal execution. Both `MEDIATED-BRIDGE-CERTIFIED` and `ROUTE-FALSIFIED` remain valid exit-zero scientific routes. An integrity/protocol failure is `STOP` and exits nonzero.

## 2. Frozen carrier and notation

Use the public integer step matrix

```text
M_J = [[1,0,-1,1],
       [0,1,-1,0],
       [1,0,0,0],
       [0,1,-1,1]].
```

Define

```text
D = M_J - I,
A = D - D^-1 = D - D^4,
S = D + D^-1 = D + D^4.
```

The verifier must first recover `D^5=I` and the public affine simplex

```text
v_x = D^x e_0,   x in F_5.
```

For `a in F_5^*`, `b in F_5`, define the unique rational linear action

```text
rho(a,b) v_x = v_(a x+b).
```

The Gram is frozen as

```text
G = I_4 - (1/5) 11^T,
X^sharp = G^-1 X^T G.
```

For token `k in F_5`, its multiplier stabilizer is

```text
h_(a,k) = rho(a, k(1-a)),
g_k = h_(2,k).
```

Define the exact projectors

```text
P_k = (1/4) sum_(a in F_5^*) h_(a,k),
R_k = (1/4)(I - g_k + g_k^2 - g_k^3),
C_k = I - P_k - R_k.
```

No other sector decomposition is admitted after the pin.

## 3. Frozen theorem route G1: native two-sector no-go

The characteristic polynomial is

```text
chi_M(x) = x^4 - 3x^3 + 4x^2 - 2x + 1.
```

In `Q(sqrt(5))`, put

```text
alpha_u = phi^2    = (3+sqrt(5))/2,
alpha_s = phi^-2   = (3-sqrt(5))/2.
```

Then

```text
chi_M(x)
 = (x^2 - alpha_u x + alpha_u)
   (x^2 - alpha_s x + alpha_s).
```

The discriminants are

```text
Delta_u = (-5-sqrt(5))/2,
Delta_s = (-5+sqrt(5))/2.
```

Both are negative in both real embeddings because `sqrt(5)<3<5`; therefore neither is a square in the real field `Q(sqrt(5))`. The two quadratics are distinct irreducibles. By CRT,

```text
Q(sqrt(5))[M_J] ~= K_u x K_s
```

with `K_u,K_s` fields. A field has only idempotents `0,1`, hence the product has exactly four idempotents and exactly two primitive nonzero ones. Therefore the native four-dimensional real carrier has exactly two primitive rank-two invariant sectors. A third native invariant mediator does not exist.

This is a no-go for the naive native-carrier route only. It is not a no-go for derived affine projectors.

## 4. Frozen theorem route G2-G4: odd-motor mediated block

For each token, verify exact ranks

```text
rank(P_k), rank(R_k), rank(C_k) = 1,1,2,
P_k + R_k + C_k = I,
```

and pairwise `G`-orthogonality.

The odd channel must satisfy

```text
A^sharp = -A,
PAP = RAR = CAC = 0,
PAR = RAP = 0,
rank(PAC)=rank(CAP)=rank(RAC)=rank(CAR)=1.
```

This gives the complete block graph

```text
P <-> C <-> R
```

with no direct `P <-> R` block.

Define

```text
B_k = P_k A C_k A R_k.
```

The frozen positive route requires for every token

```text
rank(B_k)=1,
B_k^sharp B_k = (5/4) R_k,
B_k B_k^sharp = (5/4) P_k.
```

Thus the normalized second-order amplitude has squared magnitude `5/4` and magnitude `sqrt(5)/2`.

For the two active lines in `C_k`, define

```text
U_P = C_k A P_k,
U_R = C_k A R_k,
L_P = (2/5) U_P U_P^sharp,
L_R = (2/5) U_R U_R^sharp.
```

The frozen angle statement is

```text
tr(L_P L_R) = 1/5.
```

No geometric or material reading is attached to this `1/5`.

## 5. Frozen negative controls G5

For each token and each control operator

```text
D, D^2, D^3, D^4, S=D+D^-1,
```

consider every ordered distinct pair `X,Y` among `P,R,C`, with `Z` the third sector. The odd-channel phenomenon is declared specific only if no control satisfies simultaneously

```text
X U Y = 0,
X U Z U Y != 0.
```

One exact counterexample in the control family falsifies the specificity clause. The control list and test are frozen and may not be reduced after the run.

## 6. Frozen Schur/resolvent theorem G6

Set

```text
H_k = g_k + g_k^-1 = g_k + g_k^3.
```

The projectors must satisfy

```text
H_k P_k =  2 P_k,
H_k R_k = -2 R_k,
H_k C_k =  0.
```

For formal variables `z,t`, define

```text
L_k(z,t) = zI - (H_k + tA).
```

Since `CAC=0` and `H_k|_C=0`, the `C` block is exactly `z I_C`; for `z != 0` its elimination is exact. The induced `P-R` map is `-(t^2/z) P A C A R` up to the orientation convention of one-dimensional normalized bases. Since `B_k^sharp B_k=(5/4)R_k`, its orientation-independent magnitude is

```text
sqrt(5) t^2 / (2 z).
```

The pole at `z=0` is an algebraic resolvent pole of the eliminated mediator block. It is not a physical resonance claim.

At token `k=2`, the verifier independently computes the full bivariate determinant by the 24-term Leibniz formula and must obtain exactly

```text
det L_2(z,t) = z^4 + (5t^2-4)z^2 + 5t^4.
```

The full determinant is regular as a polynomial; the Schur pole says only that elimination of `C` fails at its eigenvalue.

`t` is a formal insertion counter. It is not a fitted or physical coupling.

## 7. Frozen quadratic lift G7-G8

Let `G_aff = AGL_1(F_5)`. On the four-dimensional augmentation/simplex carrier, the character is

```text
chi_V(g) = #Fix_F5(g) - 1.
```

The symmetric-square character is

```text
chi_Sym2(g) = (chi_V(g)^2 + chi_V(g^2))/2.
```

Let `epsilon(a)=+1` for `a in {1,4}` and `-1` for `a in {2,3}`. Exact character inner products over all 20 affine elements must give

```text
Sym^2(V) ~= 1 + epsilon + 2V,
dim End_G(Sym^2 V) = <chi_Sym2,chi_Sym2> = 6.
```

The two explicit motor-invariant scalar forms are frozen as

```text
q_+ = (5/2) G,

q_- = [[ 0, 1,-1,-1],
       [ 1, 0, 1,-1],
       [-1, 1, 0, 1],
       [-1,-1, 1, 0]].
```

For every affine element `rho(a,b)` require

```text
rho^T q_+ rho = q_+,
rho^T q_- rho = epsilon(a) q_-.
```

Pairwise direct Hom spaces between the three irreducible types are zero:

```text
<1,epsilon>=<1,V>=<epsilon,V>=0.
```

The complete ordered triple census within `{1,epsilon,V}` is frozen. In particular,

```text
dim(1*epsilon*epsilon)^G = 1,
dim(1*V*V)^G = 1,
dim(epsilon*V*V)^G = 1,
dim(V*V*V)^G = 3,
```

with the ten permutations of the first three patterns plus `1*1*1` and `V*V*V` giving the exact nonzero ordered list implemented by the verifier.

The multiplicity two of `V` is a nonselection boundary. The affine action determines the isotypic component but not a unique splitting into two copies. No physical mediator basis is selected.

## 8. Decision and falsifiers

```text
MEDIATED-BRIDGE-CERTIFIED
  carrier integrity passes and every frozen statement G1-G8 passes exactly.

ROUTE-FALSIFIED
  carrier integrity passes but at least one frozen scientific clause G1-G8
  fails. Preserve the first failing exact witness; do not modify this probe.

STOP
  authority, collision, carrier construction, exact arithmetic, pin/readback,
  deterministic execution, stderr, security, or architecture requirements fail.
```

Scientific falsifiers include:

```text
F1 native factorization or irreducibility fails;
F2 a third primitive native invariant sector exists;
F3 an odd-channel diagonal or direct P-R block is nonzero;
F4 any required P/R-C block loses rank one;
F5 B_k vanishes, changes rank, or violates either 5/4 projector identity;
F6 the active-line overlap differs from 1/5;
F7 a frozen raw/even control exhibits the same mediated pattern;
F8 H_k sector eigenvalues differ from +2,-2,0;
F9 the exact determinant differs from z^4+(5t^2-4)z^2+5t^4;
F10 the Sym^2 decomposition, q_- character, direct-Hom zeros, triple census,
    or End dimension differs from the frozen statement.
```

No numerical threshold exists. Every decision is exact equality, rank, finite character sum, or exact polynomial identity.

## 9. Maximum later status and scope

If the written proof remains valid and the exact audit passes on the required two architectures, a later separate Canon fold may propose theorem rows at **T, L1 only** for the algebraic statements. The probe PR itself changes no Canon, Registry, Frontier, Evidence, Gate, dependency, status, tag, or release file.

The word `resonance` is not part of the proposed public theorem scope. A physical resonance requires a separately typed frequency/susceptibility bridge and is absent here.

## 10. Hard firewall

No phonon, amplitudon, ferroaxial order, material, susceptibility, frequency, damping, temperature, laser coupling, light control, quantum-state control, Born rule, probability, observer, decoder, force, spacetime, SI value, or L2-L6 lift is assumed or concluded.

This probe establishes at most an exact L1 statement of the form:

```text
one frozen odd motor channel has a symmetry-forbidden direct P-R block,
an active rank-one second-order P-C-R block of exact norm, and exact
representation-theoretic controls.
```

Nothing more.

## 11. Formal order

1. Commit and push exactly this `PREREG.md` and accepted `verify.py` before any formal scientific execution.
2. Read both files back from GitHub; record the pin commit, blob IDs, SHA-256, bytes and line counts.
3. From a clean local copy of those exact bytes, execute exactly once:

```text
python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-1/verify.py
```

4. Require exit code 0 and empty stderr. Save stdout byte-for-byte as `EXPECTED.txt`.
5. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` in the result commit.
6. Open one PR changing only `probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-1/`.
7. Require GitHub x86_64 and aarch64 jobs and aggregate `check` with the same verifier hash and byte-identical stdout.
8. Never amend, rebase, squash, force-push, move a threshold, change a gate, repair the verifier, or reuse the probe identifier after the pin.
