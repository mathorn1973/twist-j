# PREREG-BREAKER-MACKEY4-SOURCE-1

Independent source-side breaker draft for the residual source gates of the
archived candidate `C-ENTROPY-MACKEY-OBSTRUCTION-4-N`.

```text
STATUS:        NON-CANONICAL PREREGISTRATION DRAFT; NOT FROZEN
AUTHORITY:     NONE
CLAIMED GATES: E1, E2, E3, E5, E13 only
TARGET GATE:   PREREG-BREAKER-MACKEY4-2 and its common-cocycle decision are
               disjoint and excluded
DRAFTED:       2026-08-02
OPENED:        NONE
PUBLIC BASIS:  Public Canon v30
MAIN:          b8d4d585820d04ebd008444661f3a71d6e24f423
TAG:           canon-v30
CONTENT:       857223fcd5e7bc8c8e68f1df768d6e8222b24ee0
CANON SHA256:  2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a
CANON BYTES:   157167
ARCHIVE BASIS: notes/entropy-selection-recon-breaker-m2 at
               88026bbb109ec33cff7f96e8b2cc746cf2cc1751
INTENDED CODE: mackey4_source.py, absent while this draft is unfrozen
CEILING:       breaker agreement at incubation candidate grade only
COMPUTATION UNDER THIS DRAFT: NONE
```

This draft replaces none of the archived instruments. The owner retired
`PREREG-BREAKER-MACKEY4-1` in full, so its source calculations have discovery
value but zero breaker credit. If frozen, this document opens a fresh
source-side decision surface on Public Canon v30.

A successful run would not establish the target common cocycle, produce a
Mackey obstruction by itself, establish `A_A = empty`, close
`ENTROPY-LAYER-BRIDGE [O]`, or change a public claim or status.

## Independence fence

The sessions writing and reviewing this preregistration have read the archived
primary and retired breaker and are disqualified from implementing the
instrument.

The implementing session must be a clean named session. At authoring and run
time it may read only:

```text
this preregistration;
STATUS.md, POLICY.md and AGENTS.md;
the pinned Public Canon v30 normative files.
```

It must not read or import:

```text
the branch notes/entropy-selection-recon-breaker-m2;
mackey4_verify.py, mackey4_break.py, their stdout or result records;
PREREG-BREAKER-MACKEY4-1 or PREREG-BREAKER-MACKEY4-2;
any target-side successor implementation;
the verifier sources or outputs of P-ENTROPY-BRIDGE-3,
P-ENTROPY-MIRROR-1 or P-ENTROPY-RG-RETURN-1.
```

The proposed comparison values below may be used only after the instrument has
constructed the quotient permutation, living maps, cycles and certificates.
They may not be installed as working objects.

## Field 1. Exact decision surface

Notation is typed before any formula:

```text
s_TM      dyadic Thue-Morse factor/substitution level;
r_collar  collar radius of the separate finite cell-sector ansatz.
```

The archived Mackey documents used `r` for `s_TM` while also mentioning collar
radius. This preregistration does not. Every component-count statement below
uses `s_TM`; the collar variable is outside the instrument.

### 1.1 Integral source presentation

No lambda-digit arithmetic is permitted.

Work in the integral basis `(1,z,z^2,z^3)` of

```text
K = Q(z),
z = the image of zeta_5, a root of Phi_5(X)=X^4+X^3+X^2+X+1,
O = Z[z] = Z[X]/(Phi_5(X)),
lambda = 1-z.
```

Multiplication by `z` is the companion matrix

```text
C =
[ 0  0  0 -1 ]
[ 1  0  0 -1 ]
[ 0  1  0 -1 ]
[ 0  0  1 -1 ].
```

Set

```text
L = I - C,
A = L^5,
M = I + C^2.
```

Thus `L` is multiplication by `lambda` in the displayed integral basis and
`A` is multiplication by `lambda^5`.

The proposed comparison matrices are

```text
A =
[ -5  15 -20  15 ]
[-10  10  -5  -5 ]
[  5   5 -10  10 ]
[-15  20 -15   5 ]

M =
[1 0 -1 1]
[0 1 -1 0]
[1 0  0 0]
[0 1 -1 1].
```

The instrument must derive these matrices from `C`, not install them as its
working matrices. The displayed copies are comparison values.

Let

```text
Q = Z^4 / A Z^4.
```

The quotient must be constructed by a certified integer-lattice reduction.
Smith or Hermite normal form is allowed, but every transformation matrix must
be checked exactly. If Smith form is used, the instrument must verify

```text
U A V = D,
|det U| = |det V| = 1,
D diagonal and divisibility ordered.
```

A table of expected coset representatives is forbidden.

### 1.2 Induced J action

The instrument must prove directly that `M` preserves `A Z^4`, construct the
induced permutation `J_Q` on all quotient classes, and enumerate its cycles.

It must not derive the cycle census from a valuation formula or install cycles
with the expected lengths.

### 1.3 Dyadic component law

For a cycle `C_m` and the level-`s_TM` dyadic factor, independently construct
the
diagonal permutation

```text
R_(m,s_TM)(i,j) = (i+1 mod m, j+1 mod 2^s_TM).
```

Count its components directly for `m in {1,4,20}` and `s_TM=0..8`.

The result record must also include the exact proof

```text
m = 2^v u, u odd
=> gcd(m,2^s_TM) = 2^min(v,s_TM),
```

so stabilization for every `s_TM>=2` is a theorem, not an extrapolation from
the finite audit.

To interpret this as the component count of the full two-sided Thue-Morse
product, the result package must separately supply a written exact lemma that:

1. the root-of-unity measurable eigenvalues of the two-sided Thue-Morse
   probability system are exactly the dyadic roots; and
2. the number of ergodic components of its product with `C_m` is the
   cardinality of the intersection of that eigenvalue group with the
   `m`-th roots.

If that lemma is absent or merely inferred from the computations at
`s_TM=0..8`, the instrument may report a finite-factor audit but its scientific
decision is `STOP`.

### 1.4 Mirror law without a warmup census

Use the v30 checkpoint carrier

```text
X = F_5^6,
z_6(x) = sum of the six coordinates mod 5,
F_t(x) = g_(z_6(x)+2t mod 5)(x).
```

The five generators are reconstructed exactly from the Public Canon v30 table.
Define directly

```text
H_0 = {x in X : z_6(x)=4},
H_1 = {x in X : z_6(x)=1}.
```

Each has exactly `5^5=3125` states. No orbit warmup, sampled window, or
imported support list is allowed.

The selector law gives, before enumeration,

```text
F_0|H_0 = e,   F_1|H_0 = b,
F_0|H_1 = b,   F_1|H_1 = d.
```

This identity must be checked on all states as an audit. Consequently the
mirror decision is genuinely symbolic:

```text
F_0|H_0 and F_1|H_1 are involutions;
F_1 o F_0 = id on H_1;
F_0 o F_1 = id on H_0.
```

The exact own-half cycle type must be `{1:1, 2:1562}` on both halves. The
proposed unique fixed points are

```text
F_0 on H_0: 3(c_d+v_e) = (1,3,4,2,1,3),
F_1 on H_1: 3c_d       = (1,3,4,2,3,3).
```

Their affine multipliers are exactly `-I_6`. This is also the explicit
compatibility check with the `k=0` clause of `ENTROPY-RG-RETURN [C]`, newly
present on the v30 basis. No higher-scale RG statement is part of this breaker.

### 1.5 E13 arithmetic and kernel premises

Let

```text
iota: Z^4 -> O,
(n_0,n_1,n_2,n_3) -> n_0+n_1 z+n_2 z^2+n_3 z^3.
```

The instrument and result proof must establish, rather than merely name, the
chain

```text
A Z^4 = iota^(-1)(lambda^5 O),
Q = Z^4/A Z^4 ~= O/lambda^5 O,
O_(K,lambda)/lambda^5 O_(K,lambda) ~= O/lambda^5 O.
```

Using the inverse-limit definition

```text
O_(K,lambda) = lim_(n>=1) O/lambda^n O,
```

construct `pi_5` as the fifth coordinate projection. Prove that it is a
continuous, Borel-measurable, surjective additive homomorphism with kernel
`lambda^5 O_(K,lambda)`. The finite cokernel `Q` is not accepted as the Route A
quotient until this identification is complete.

Derive the one-letter masses of the unique two-sided Thue-Morse substitution
probability. The result proof must exhibit the primitive substitution incidence
matrix

```text
[1 1]
[1 1]
```

and its uniquely normalized positive Perron-Frobenius vector
`(1/2,1/2)` at eigenvalue `2` (or give an equivalent exact complement-symmetry
proof together with uniqueness). Thus

```text
m_TM({kappa:kappa_0=0}) = m_TM({kappa:kappa_0=1}) = 1/2.
```

The factor `1/2` below may not be inserted without this derivation.

Using `Fraction`, verify exactly

```text
(1/2)(1/3125) = 1/6250.
```

On the additive quotient `Q`, construct the translation action

```text
T_u(q) = q+u.
```

Verify the regular-action certificate:

```text
T_0 = id;
T_u T_v = T_(u+v);
T_(-u) is the inverse of T_u;
for every q,q' the unique transporter is u=q'-q.
```

This finite regularity is the finite shadow used by the Haar quotient lemma. It
does not itself assert a new L6 measure. The result package must separately give
the exact compact-group lemma that normalized additive Haar measure pushes to
uniform probability on a finite quotient because quotient translations are
transitive and preserve the pushforward. If that lemma is absent, E13 is
`INCOMPLETE / STOP` even when the finite action passes.

Represent the five Canon generators as affine homogeneous matrices over
`F_5`. Verify symbolically, rather than only by sampling states,

```text
a^2=b^2=c^2=d^2=e^2=id,
(bc)^5=(cb)^5=id.
```

Finally derive `M=I+C^2` and verify on the four basis vectors that it is exactly
the linear map (coordinate names here are not Canon generator names)

```text
(x0,x1,x2,x3) -> (x0-x2+x3, x1-x2, x0, x1-x2+x3).
```

## Field 2. Proposed freeze values

These values become binding only if this draft is committed and its exact
SHA-256 is recorded before implementation.

```text
E1  determinantal divisors of A:
    delta_1=5, delta_2=25, delta_3=125, delta_4=3125;
    Smith factors (5,5,5,25);
    Q ~= Z/25 + (Z/5)^3 and |Q|=3125.

E2  J_Q is a permutation of order 20 with cycle census
    {1:1, 4:1, 20:156}; its unique fixed class is zero.

E3  direct product counts equal gcd(m,2^s_TM) for
    m in {1,4,20}, s_TM=0..8;
    c_src(0)=158;
    c_src(1)=315;
    c_src(s_TM)=629 for s_TM=2..8;
    the written valuation proof gives c_src(s_TM)=629 for every s_TM>=2.
    Every printed occurrence of 629 must carry "s_TM>=2".

E5  H_0 and H_1 are the complete sheets z_6=4 and z_6=1,
    3125 states each;
    F_0|H_0=e, F_1|H_0=b, F_0|H_1=b, F_1|H_1=d;
    own maps have cycle type {1:1,2:1562};
    cross restrictions are mutually inverse;
    fixed points are (1,3,4,2,1,3) and (1,3,4,2,3,3);
    both own-map multipliers are -I_6.

E13 A Z^4 corresponds exactly to lambda^5 O;
    Q ~= O/lambda^5 O ~= O_(K,lambda)/lambda^5 O_(K,lambda);
    pi_5 is continuous, measurable and surjective with kernel
    lambda^5 O_(K,lambda);
    the unique Thue-Morse substitution measure has one-letter masses 1/2,1/2;
    normalized additive Haar pushes to uniform mass 1/3125 on Q;
    exact Route A mass arithmetic is 1/6250;
    the translation action of Q on itself is regular;
    all five generators are involutions;
    (bc)^5=(cb)^5=id;
    M=I+C^2 gives exactly
    (x0-x2+x3,x1-x2,x0,x1-x2+x3).
```

The target values `E4`, `E6` through `E12`, the Mackey menu, mixed control and
common-cocycle premise are excluded. This instrument must not print an
agreement verdict about them.

## Field 3. Mandatory controls

All controls execute and print before any claim-carrier verdict. A wrong
control verdict makes the instrument defective and stops the run.

```text
N1 LATTICE ACCEPT
   The diagonal matrix diag(5,5,5,25) must be accepted as having the proposed
   invariant factors.

N2 LATTICE REJECT
   Replace the top-left entry of A by -4, leaving every other entry unchanged.
   The first determinantal divisor becomes 1. The E1 checker must reject it.

N3 ACTION REJECT
   On the real quotient Q, substitute the identity for J_Q. It remains a
   well-defined permutation but has census {1:3125}; the E2 checker must reject
   it. This prevents well-definedness from being mistaken for the cycle gate.

N4 PLATEAU REJECT
   Construct an abstract 3125-point permutation with census
   {1:1,4:1,10:2,20:155}. It still gives 629 for every s_TM>=2, but gives
   c(0)=159 and c(1)=317. The combined E2/E3 gate must reject it. This prevents
   the answer 629 from being hardcoded as the whole source test.

N5 PRODUCT-LAW REJECT
   Replace R_(20,3)(i,j)=(i+1,j+1) by (i+1,j). The orbit count is not
   gcd(20,8)=4. The component-law checker must reject it.

N6 MIRROR ACCEPT
   On two abstract five-point halves, use one fixed point plus two
   transpositions for each own map and mutually inverse cross identities. The
   mirror checker must accept the corresponding toy specification.

N7 MIRROR REJECT
   In a copy of the reconstructed real own-half map, change the image of the
   lexicographically least nonfixed state to itself while leaving its partner
   unchanged. The result is nonbijective and has the wrong fixed census. The
   mirror checker must reject it.

N8 TRANSLATION REJECT
   Replace the full acting translation group by the subgroup generated by
   (0,0,0,5) in coordinates Z/5 x Z/5 x Z/5 x Z/25. Its zero orbit has size 5.
   The regular-action checker must reject it.

N9 RELATION REJECT
   Feed the relation checker the affine map h(x)=2x as a proposed involution.
   Since h^2 is not the identity, it must reject it.

N10 STEP REJECT
    Replace the last coordinate of the proposed step by b-c, omitting +d. The
    basis-column comparison with I+C^2 must reject it.
```

The controls test the checkers; they are not evidence about the claim carrier.

## Field 4. Code and execution policy

`mackey4_source.py` uses Python 3.12 standard library only. Exact `int` and
`Fraction` arithmetic only; no float in any assertion. No NumPy, SymPy, Sage,
network, subprocess, dynamic import, file read, random order, or imported
certificate.

Iteration and output are deterministic and sorted. The program must run from a
directory containing only itself. Target runtime is under 120 seconds.

Before the code pin, the only permitted executions are:

```text
python -m py_compile mackey4_source.py
python mackey4_source.py --synthetic-only
```

The `--synthetic-only` path may execute only N1, N4, N5, N6, N8 and N9. It must
terminate before constructing or inspecting `A`, the real quotient `Q`, the
real `J_Q`, the real generator matrices, `M`, or `F_5^6`. N2, N3, N7 and N10
are mandatory post-pin controls and may first execute only in the pinned full
run. Any pre-pin execution touching a real claim carrier, including any of
those four controls, disqualifies this identifier.

The preregistration must be committed and its SHA-256 recorded before
implementation. The implementing session then freezes the code and records its
SHA-256 before the first claim-carrier execution. Every subsequent execution is
recorded with command, platform, Python version, exit code, stderr byte count
and stdout SHA-256.

Every required written lemma is a self-contained proof, not a restatement of
its conclusion. `py_compile` may create `__pycache__`; the pinned claim run must
therefore use a fresh directory containing exactly the frozen script and no
cache or auxiliary file.

One platform is incubation evidence only. A later public probe would require
its own fresh preregistration and the repository's two-architecture gate.

## Field 5. Systematics

```text
S1  Before the run, fetch origin/main. It must still equal the pinned public
    basis b8d4d585820d04ebd008444661f3a71d6e24f423; if public main has moved,
    STOP for a fresh applicability audit. The instrument branch must descend
    from that basis. Verify that canon-v30 and the declared content commit are
    ancestors of origin/main; Canon SHA-256 and byte count match STATUS;
    canon/SHA256SUMS passes 5/5; and every required public check is green.
S2  Source construction is the integer cokernel of A; lambda-digit arithmetic
    is forbidden.
S3  Quotient coordinates are certified, not assumed from their expected type.
S4  Cycle census is enumerated from the induced action, not generated from the
    expected valuation formula.
S5  The all-s_TM statement rests on a written proof; s_TM=0..8 is only its
    audit.
S6  The Thue-Morse measurable-spectrum lemma is explicit. If absent, STOP.
S7  Living halves are complete z_6 sheets, not a warmed-up orbit sample.
S8  Mirror identities are checked against independently constructed maps and
    must pass the mandatory acceptance and rejection controls.
S9  The Thue-Morse one-letter mass 1/2 is derived from the unique substitution
    measure; it is not inserted as an expected scalar.
S10 Haar uniformity is not inferred from cardinality alone: pi_5 and its
    kernel, the finite regular translation action, and the compact Haar
    quotient lemma are all proved.
S11 The v30 ENTROPY-RG-RETURN row is used only to check the k=0 fixed witnesses
    and -I multipliers. No all-scale statement is imported.
S12 No target component, D_5, subgroup menu or common-cocycle value enters the
    code.
S13 Every statement containing 629 says s_TM>=2.
```

## Field 6. Decision and falsifiers

```text
SOURCE-AGREE
  only if N1-N10 give their proposed verdicts, E1/E2/E3/E5/E13 all match,
  every exact certificate passes, and the written Thue-Morse/product and Haar
  quotient lemmas are complete.

SOURCE-DISAGREE
  if any real-carrier value differs from E1/E2/E3/E5/E13. Preserve the exact
  witness, do not alter either expectation or implementation, and STOP the
  Mackey candidate.

DEFECTIVE INSTRUMENT
  if any mandatory control gives the wrong verdict, a certificate is invalid,
  the independence fence is broken, pre-pin claim computation occurred,
  nondeterminism occurs, or a float enters an assertion. STOP with no
  scientific conclusion.

INCOMPLETE / STOP
  if the finite computations pass but the all-s_TM proof, Thue-Morse
  eigenvalue lemma, one-letter substitution-measure lemma, inverse-limit
  quotient identification, Haar quotient lemma, authority check, or run ledger
  is incomplete.
```

A defect in this preregistration discovered after the first claim-carrier
execution retires `SOURCE-1` in full. No gate is severable after execution. A
successor would receive a new identifier.

Even `SOURCE-AGREE` means only:

```text
The residual source inputs E1, E2, E3, E5 and E13 have an independent exact
v30-pinned reconstruction at incubation candidate grade.
```

It does not decide the target breaker, the common cocycle, the full Mackey
obstruction, any map in `A_A`, or the public bridge.

## Field 7. Action layer and scope fence

```text
SOURCE:        L2 Thue-Morse probability system and finite lambda^5 shadow
FINITE TARGET: L5 checkpoint carrier only for E5/E13 audits
DEPTH:         lambda^5 exactly
ADMITTED s_TM: s_TM>=2 for every 629 conclusion
NEW LIFT:      none
L6 MEASURE:    excluded
SI:            excluded
```

Excluded without exception:

```text
deeper or variable lambda depth;
nonbijective or non-factorizing Route A maps;
collar families with r_collar>2 (outside this instrument);
the target D_5 common cocycle;
the Mackey subgroup menu;
A_A=empty;
closure or movement of ENTROPY-LAYER-BRIDGE.
```

## Freeze record

```text
preregistration: proposed, not yet committed
preregistration SHA-256: not assigned
mackey4_source.py: absent
implementing session: unnamed
claim-carrier computation: none
formal public probe: none
public issue: none
status or Canon change authorized: none
```

This source breaker must be frozen and run independently of the target-side
breaker. Only after both produce valid live results may an owner session assess
whether the archived fixed-depth-five, fiberwise-bijective, `s_TM>=2`
subclass (called `r>=2` in the archive) can be reformulated on the Public Canon
v30 basis.
