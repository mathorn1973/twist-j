# P-GYRON-DISCREPANCY-LOG-3 preregistration

Status: `PREREGISTERED CANDIDATE / RESULT-EXPOSED / NO FORMAL RUN`

This document freezes one proof-first exact L1 probe. It contains no verifier
output and earns no scientific, registry, Canon, dependency, gate, evidence,
or release status. Formal execution, compilation, and import of `verify.py`
are forbidden until this document and `verify.py` have been committed
together, pushed, hash-pinned to public issue #171, and read back
byte-for-byte from the public remote.

The analytical targets are already public in the merged predefinition and
issue #171. This is a pinned proof certificate and adversarial audit, not
blind discovery. No equation, carrier, phase convention, proof obligation,
threshold, output route, or scope may move after the initial pin.

## 1. Public identity, authority, and action layer

```text
public lock:          issue #171
public lock URL:      https://github.com/mathorn1973/twist-j/issues/171
probe owner:          A. M. Thorn
probe:                P-GYRON-DISCREPANCY-LOG-3
branch:               probe/P-GYRON-DISCREPANCY-LOG-3
path:                 probes/P-GYRON-DISCREPANCY-LOG-3/
action layer:         L1 only

STATE:                ACTIVE
Public Canon:         v23
authority:            mathorn1973/twist-j main
tag:                  canon-v23
activation commit:    4ac41b4fac3a3794a6e9d5be1e2027d324edb806
content commit:       7830d852229ffc06c9d287d026c8ece290bf339b
Canon SHA-256:        f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
Canon bytes:          116017
issue opening main:   dcd8857c37bdeb3af10157fff4649147b6d5859a
initial branch base:  1a4ae20d05cd76f93f70b2b011979b22a15fcde7

STATUS SHA-256:       a8ec16afadb9d9f85530a54bd82b13b8855059bf05b7c4783f15898bd9854680
registry SHA-256:     6f4c7b350e0f12ba3e7ddc112ce04c4e916d03709aaab7ff007c0c17967a86c1
registry lines:       207 including header; 206 claim rows
```

The frozen public source notes are:

```text
notes/canon/P-GYRON-DISCREPANCY-LOG-3-PREDEFINITION.md
SHA-256: bca4dde1975de979e2bcc589220c0e1e2218b14e7100b677628ce679af88c1cf
bytes:   11115
Git blob: 4917087c8ff6fd2c118a3d7932c2530547282516

notes/canon/P-DECODER-FACTOR-CANONICITY-1-PREDEFINITION.md
SHA-256: c10a4f22afe4a1c7c68feb92864c7acd4b041cb4773e4e7789f280ff98bc75ec
bytes:   31346
Git blob: b38c095e16c7a431cd605469068beb4339c54c08
```

The gyron note is the proof-surface source. The decoder note is a firewall and
context source only. This probe does not test, instantiate, or strengthen any
decoder-factor claim.

A passing probe may later support two separately reviewed theorem rows:

```text
GYRON-DISCREPANCY-LOG [T]
TM-PAIR-SUBSTITUTION-FIXED-POINT [T]
```

It may also support a wording correction to `GYRON-DENSITY [T]`. This probe
does not add or edit those rows. In particular, the current unqualified
finite-prefix invariant in `GYRON-DENSITY [T]` is not a premise of this
probe.

## 2. Known-result disclosure and novelty boundary

Two unattached incubation records are known pre-pin inputs and are not public
evidence:

- `C-GYRON-DISCREPANCY-LOG-1` produced 15/16 against its frozen predicates
  and fired its bound `|d(L)| <= k+2`. That threshold is not moved.
- `C-GYRON-DISCREPANCY-LOG-2` produced 16/16 against its implementation, but
  its prose is ineligible: on the declared domain `N >= 1`, the least
  counterexample to `d(4N)=d(N)` is `N=1`, not `N=3`, and its global sector
  conclusion was inferred from a finite horizon.

Neither record is resumed, repaired, or reinterpreted. The present novelty is
the exact six-state signed-affine transducer, the all-`k` four-step induction,
and the precisely typed stationary phase-averaged fixed-point theorem.

No unattached verifier, transcript, scan, or earlier pull request is evidence
for this probe.

## 3. Falsifier first and scientific routes

Integrity is decided before science.

A complete exact counterexample to any frozen universal mathematical clause
in Theorem A or Theorem B is scientific `FALSIFIED`. A proof gap, incomplete
certificate, malformed carrier, route disagreement, or inability to establish
a universal clause is `STOP`, not a negative mathematical result.

With integrity green, exactly one overall route is allowed:

```text
PROOF-SURVIVES
    Theorem A and Theorem B both pass their complete symbolic proof
    certificates, Gate C local audits pass, and no exact counterexample is
    emitted.

FALSIFIED
    integrity passes and at least one complete exact counterexample to a
    frozen Theorem A or Theorem B clause is emitted.

STOP
    authority, typing, proof, audit, pin, execution, transcript, or
    reproducibility is incomplete or invalid.
```

The verifier also emits separate Theorem A and Theorem B decisions. An
overall `PROOF-SURVIVES` does not promote a row. Public evidence is incomplete
until the external pin and two-architecture part of Gate C passes. Any later
status or wording change requires a separate owner-reviewed Canon fold.

`STOP` has priority over `FALSIFIED`. An implementation failure cannot be
converted into a mathematical counterexample.

## 4. Theorem A: exact prefix discrepancy

### 4.1 Domain and definitions

For every integer `n >= 0`, define the Thue-Morse digit

```text
t_n = s_2(n) mod 2,
```

where `s_2(n)` is the binary popcount.

For every prefix length `L >= 1`, define

```text
n_a(L)  = #{0 <= i <= L-1 : t_i=a},

c_ab(L) = #{0 <= i <= L-2 : (t_i,t_(i+1))=(a,b)},

S(L)    = n_0(L)-n_1(L),

d(L)    = 6 c_00(L)-L.
```

The empty pair census is frozen:

```text
c_00(1)=c_01(1)=c_10(1)=c_11(1)=0,
d(1)=-1.
```

All equalities below use exact integer equality.

### 4.2 Seam and balance identities

Freeze the substitution

```text
mu(0)=01,
mu(1)=10.
```

For every `L >= 1`, the proof must establish

```text
c_00(2L)=c_10(L),
c_01(2L)=n_0(L)+c_11(L),
c_10(2L)=n_1(L)+c_00(L),
c_11(2L)=c_01(L).
```

It must also establish

```text
S(L) in {-1,0,1},
S(2m)=0,
S(2m+1)=(-1)^(t_m),
c_10(L)=n_0(L)-c_00(L)-1.
```

### 4.3 Primitive discrepancy laws

The seam and balance proof must derive, for every `L >= 1`,

```text
d(2L)=-d(L)+3S(L)-6,                           (A1)
d(4L)=d(L)-3S(L).                              (A2)
```

Consequently, for every positive integer `L`,

```text
d(4L)=d(L)     iff L is even,
d(4L)!=d(L)    iff L is odd.
```

The least positive counterexample to the unqualified four-step invariant is

```text
L=1,
d(1)=-1,
d(4)=-4.
```

No domain beginning at `L=2` or `L=3` may be substituted after the pin.

### 4.4 Six-state signed-affine transducer

For `L >= 1`, define

```text
q(L)=(S(L),t_(L-1),t_L).
```

For `q=(s,a,b)`, freeze the transitions

```text
q(2L)=(0,1-a,b),
d(2L)=-d(L)+3s-6,                              (T0)

q(2L+1)=(1-2b,b,1-b),
d(2L+1)=-d(L)+3s-7
         +6[(a,b)=(1,0)].                      (T1)
```

The initial state is

```text
q(1)=(1,0,1),
d(1)=-1.
```

The reachable state set must be proved exactly equal to

```text
A=(-1,1,0)
B=( 0,0,0)
C=( 0,0,1)
D=( 0,1,0)
E=( 0,1,1)
F=( 1,0,1).
```

The proof must establish both closure and reachability. A superset check is
insufficient.

### 4.5 Base extremum certificate

For binary length `n` and reachable state `q`, let

```text
I_n(q)=[min d(L),max d(L)]
```

over all positive `L` of binary length `n` satisfying `q(L)=q`.

The exact base table is:

| state | `q` | `I_5` | `I_6` | `I_7` | `I_8` |
|---|---|---:|---:|---:|---:|
| A | `(-1,1,0)` | `[-5,-3]` | `[-5,-1]` | `[-7,-3]` | `[-5,-1]` |
| B | `(0,0,0)` | `[-6,-6]` | `[-6,-4]` | `[-8,-4]` | `[-6,-2]` |
| C | `(0,0,1)` | `[-4,-4]` | `[-4,-2]` | `[-6,-4]` | `[-4,-2]` |
| D | `(0,1,0)` | `[-2,-2]` | `[0,0]` | `[-2,0]` | `[-2,2]` |
| E | `(0,1,1)` | `[-4,-2]` | `[-2,0]` | `[-4,-2]` | `[-4,0]` |
| F | `(1,0,1)` | `[-3,-1]` | `[-1,1]` | `[-3,1]` | `[-3,3]` |

Every endpoint is part of the proof certificate.

### 4.6 Four-bit path induction

For every starting state in `{A,B,C,D,E,F}` and every word

```text
w in {0,1}^4,
```

the four successive transitions must produce a certified final state and an
exact affine map

```text
d -> d+c_w(q).
```

All `6 x 16 = 96` paths are required.

Let `Phi_min` and `Phi_max` be the exact minimum and maximum transfer maps
induced by these paths. The certificate must prove their uniform translation
laws

```text
Phi_min(u-r)=Phi_min(u)-r,
Phi_max(v+r)=Phi_max(v)+r
```

for every uniform scalar shift `r`.

Direct evaluation for each residue class `n=5,6,7,8` must establish

```text
I_(n+4)(q)=I_n(q)+[-2,2]                       (A3)
```

for every reachable state `q`.

The induction step must explicitly use the separate lower- and upper-endpoint
translation laws:

```text
lower_(n+8)
  = Phi_min(lower_(n+4))
  = Phi_min(lower_n-2)
  = lower_(n+4)-2,

upper_(n+8)
  = Phi_max(upper_(n+4))
  = Phi_max(upper_n+2)
  = upper_(n+4)+2.
```

This proves (A3) for every `n >= 5`. Checking finitely many binary lengths
without this translation-equivariant induction is not proof.

### 4.7 All-k extremum theorem

Define

```text
E_k=max_(1<=L<=2^k)|d(L)|.
```

The proof must establish

```text
E_1=2,
E_2=4,
E_k=2(floor((k+1)/4)+2),  k>=3.               (A4)
```

It must separately prove the endpoint law

```text
|d(2^k)|=2 for odd k,
|d(2^k)|=4 for even k,
```

and prove that the endpoint does not alter (A4) for `k>=3`.

The passage from exact-length extrema `I_n(q)` to the cumulative maximum
`E_k` is a symbolic proof obligation. It is not supplied by a finite table.

### 4.8 Corollaries in scope

The only asymptotic conclusions in scope are

```text
d(L)=O(log L),

d(L)/L^epsilon -> 0
for every fixed real epsilon>0,

c_00(L)/L -> 1/6,

c_00(L)/(L-1) -> 1/6.
```

The limits are taken through positive integers `L -> infinity`. The second
pair-frequency normalization is used only for `L>=2`.

The proof must derive the two density limits algebraically from

```text
6c_00(L)=L+d(L)
```

and the logarithmic bound.

No Takagi, Delange, Coquet, periodic-modulator, fractal-sector, or broader
asymptotic classification is included.

## 5. Theorem B: forward phase-averaged fixed point

### 5.1 Exact pair-vector carriers

Use column vectors in pair order

```text
v=(a,b,c,d)=(v_00,v_01,v_10,v_11).
```

The exact matrices have rational entries and all certificate calculations are
carried out over `Q`. They act coefficientwise on both the rational carrier
and its canonical real scalar extension.

Define

```text
V_Q=Q^4,
W_Q={v in V_Q : b=c},
V_R=R^4,
W_R={v in V_R : b=c},
W_1={v in W_R : a+b+c+d=1},
P={v in W_1 : a,b,c,d>=0}.
```

`P` is the normalized stationary pair-law simplex.

### 5.2 Frozen phase and anchoring maps

The internal-child phase has two off-stationary anchoring conventions:

```text
I_L(a,b,c,d)=(0,a+b,c+d,0),
I_R(a,b,c,d)=(0,a+c,b+d,0).
```

The boundary or seam phase is

```text
B(a,b,c,d)=(c,d,a,b).
```

Define the two full four-dimensional forward phase-averaged maps

```text
R_L=(I_L+B)/2,
R_R=(I_R+B)/2.
```

Thus

```text
R_L(a,b,c,d)
  =(c,a+b+d,a+c+d,b)/2,

R_R(a,b,c,d)
  =(c,a+c+d,a+b+d,b)/2.
```

On both stationary subspaces `W_Q` and `W_R`, the maps coincide. Freeze the
exact rational restriction

```text
R_stat=R_L|W_Q=R_R|W_Q.
```

The same rational matrix acts on `W_R` by canonical real scalar extension.
The symbol `R` in Theorem B denotes that real-linear action; its restriction
to `W_Q` is `R_stat`. Thus `R^n v` is typed for every `v in W_1`.

The sum `a+b+c+d` is preserved by `I_L`, `I_R`, `B`, `R_L`, `R_R`, and
by both `R_stat` and `R`.

### 5.3 Full-spectrum systematic control

The exact full four-dimensional characteristic polynomials are

```text
chi_(R_L)(x)=x(x-1)(x-1/2)(x+1/2),

chi_(R_R)(x)=x(x-1)(x+1/2)^2.
```

Equivalently, including algebraic multiplicity,

```text
Spec(R_L)={1,1/2,0,-1/2},
Spec(R_R)={1,0,-1/2,-1/2}.
```

They are different. The exact witness

```text
e_01=(0,1,0,0)
```

satisfies

```text
R_L(e_01)=(0,1/2,0,1/2),
R_R(e_01)=(0,0,1/2,1/2).
```

Only the restrictions to `W_Q` and their canonical extensions to `W_R` are
robust under the anchoring choice.

### 5.4 Stationary spectrum, fixed point, and convergence

The stationary subspace is invariant under both full maps. The common
restriction has characteristic polynomial

```text
chi_R(x)=x(x-1)(x+1/2)
```

and spectrum

```text
Spec(R_stat)=Spec(R|W_R)={1,-1/2,0}.
```

Freeze

```text
v_*=(1,2,2,1)/6.
```

The proof must establish

```text
Rv_*=v_*.
```

It must prove that `v_*` is the unique fixed point in `W_1`, hence the unique
normalized positive fixed point in `P`.

For every `v in W_1`, the exact spectral decomposition must prove the
componentwise limit

```text
R^n v -> v_*.
```

A numerical eigensolver or a finite list of powers is audit only.

### 5.5 Fixed-phase laws

On `W_R`, define the common internal phase

```text
I=I_L|W_R=I_R|W_R.
```

The proof must establish

```text
I(v_*)=(0,1/2,1/2,0),

B(v_*)=(1/3,1/6,1/6,1/3),

v_*=(I(v_*)+B(v_*))/2.
```

The `00` density is therefore

```text
0   in the internal phase,
1/3 in the boundary phase,
1/6 only after the frozen equal phase average.
```

No fixed-phase density `1/6` is claimed.

## 6. Gate A: symbolic proof certificate for Theorem A

Definitions, domains, integer exactness, and the empty census at `L=1` are
integrity obligations reported under `I01` and `I02`. Gate A uses exactly
the following proof-node names:

```text
A01 SEAMS
    the four substitution seam identities for all L>=1;

A02 BALANCE
    S(L) in {-1,0,1}, the even/odd balance law, and the c_10 identity;

A03 DISCREPANCY
    equations (A1) and (A2), the parity iff, and least counterexample L=1;

A04 TRANSDUCER
    T0, T1, initial state, exact six-state closure, and reachability;

A05 FOUR-BIT
    all 96 affine paths and exact endpoint transfer maps;

A06 BASE-TABLE
    all 24 frozen base intervals for n=5,6,7,8;

A07 INDUCTION
    translation equivariance and the four residue-class all-n induction;

A08 EXTREMA
    endpoint handling and equation (A4) for every k>=1;

A09 COROLLARIES
    O(log L), subpower decay, and both density limits.
```

A finite prefix scan cannot satisfy A01-A09.

## 7. Gate B: symbolic proof certificate for Theorem B

Gate B uses exactly the following proof-node names:

```text
B01 PHASE-MAPS
    exact derivation of I_L, I_R, B, R_L, and R_R from the substitution
    phases, including sum preservation;

B02 ANCHOR-SPECTRA
    the inequality of R_L and R_R, the frozen witness e_01, and both exact
    four-dimensional characteristic polynomials with multiplicity;

B03 STATIONARY
    invariance of W_Q and W_R, equality of both stationary restrictions,
    and spectrum {1,-1/2,0};

B04 FIXED-POINT
    Rv_*=v_*, normalization, positivity, and uniqueness in W_1;

B05 CONVERGENCE+PHASE-LAWS
    exact spectral decomposition proving R^n v -> v_* for every v in W_1,
    together with I(v_*), B(v_*), and their equal phase average.
```

Finite matrix powers or decimal eigenvalues cannot satisfy B02-B05.

## 8. Gate C: independent audit, controls, pin, and reproducibility

Gate C is logically separate from the proofs.

### 8.1 Local exact audit

The verifier must include an independent literal Thue-Morse route that does
not call the transducer or extremum propagation helpers. Freeze the source
horizon `H=256`. The direct route must:

```text
construct literal t_n for 0<=n<=4H;
record n_a(N), c_ab(N), S(N), d(N), and q(N) for every 1<=N<=4H;
check S(N) in {-1,0,1} and c_10(N)=n_0(N)-c_00(N)-1 for 1<=N<=4H;
check all four seams, A1, A2, and the parity iff for every 1<=L<=H;
check S(2m)=0 for every 1<=m<=H;
check S(2m+1)=(-1)^(t_m) for every 0<=m<=H;
check T0 and T1 for every 1<=L<=H;
identify L=1 as the least four-step counterexample among 1<=L<=H;
check the exact binary-length base intervals n=5,6,7,8;
check E_k for k=1,...,8.
```

Every referenced target is backed by the direct records: `2L<=2H`,
`2L+1<=2H+1`, and `4L<=4H`. The output fields are frozen as
`horizon=H=256` and `prefixes=4H=1024`.

This finite horizon is audit only. It proves no all-`L` or all-`k` statement.

The matrix audit must independently:

- construct `I_L`, `I_R`, and `B` from the four parent pair symbols;
- construct `R_L` and `R_R` from those phase maps;
- compute exact characteristic polynomials over `Q`;
- restrict both matrices independently to `W_Q` and extend the common matrix
  canonically to `W_R`;
- check the fixed point and phase laws.

The certificate route and direct-audit route may share exact scalar arithmetic
but may not share the transducer, prefix-census, phase-construction, or
characteristic-polynomial implementation. Any route disagreement is `STOP`.

### 8.2 Negative controls

All negative controls are mandatory:

```text
NC1 GLOBAL-FOUR-STEP
    reject the assertion d(4L)=d(L) for every L>=1;
    retain L=1 as the least positive counterexample;

NC2 FULL-ANCHOR-EQUALITY
    reject R_L=R_R on Q^4 and emit the frozen witness e_01;

NC3 FULL-SPECTRUM-EQUALITY
    reject equality of the full R_L and R_R spectra;

NC4 FIXED-PHASE-DENSITY
    reject density 1/6 in either fixed phase at v_*;
    certify the values 0 and 1/3;

NC5 INVERTIBILITY
    reject invertibility of R using its exact zero eigenvalue;

NC6 FINITE-PROOF
    reject any route flag claiming that the L<=256 audit proves an all-L,
    all-n, or all-k clause.
```

If the implementation asserts any forbidden proposition, omits a control, or
uses a control result as a proof substitute, Gate C is `STOP`. If exact
independent mathematics instead supplies a complete counterexample to a
frozen Theorem A or B clause, the scientific route is `FALSIFIED`.

### 8.3 External pin and architecture gate

Gate C is complete only when all of the following pass:

```text
C-PIN
    immutable initial commit containing PREREG.md and verify.py together;

C-REMOTE
    public-remote readback byte-identical to the recorded hashes, byte counts,
    Git blob IDs, and line-ending metadata;

C-AARCH64
    one clean detached native Linux/aarch64 execution of the pinned verifier;

C-PUBLIC-RETURN
    neutral run metadata and exact raw stdout returned publicly to issue #171;

C-X86_64
    first clean GitHub ubuntu-latest x86_64 execution of the byte-identical
    verifier;

C-BYTES
    exit zero, empty stderr, and byte-identical LF stdout on both
    architectures for a valid scientific route.
```

The symbolic proofs, not the architecture count, carry the universal
theorems. The two-architecture gate reproduces the exact audit.

## 9. Scientific falsifiers

Subject to green integrity, the following are scientific falsifiers.

### Theorem A

```text
FA-SEAM
    one exact L>=1 violating a frozen seam identity;

FA-BALANCE
    one exact m or L violating the balance or c_10 identity;

FA-DOUBLING
    one exact L>=1 violating (A1);

FA-FOUR-STEP
    one exact L>=1 violating (A2), the parity iff, or the declared least
    counterexample L=1;

FA-STATE
    an exact reachable state outside {A,...,F}, an unreachable listed state,
    or an exact T0/T1 transition failure;

FA-PATH
    one of the 96 frozen four-bit affine paths is incorrect;

FA-BASE
    one frozen base interval endpoint is incorrect;

FA-INDUCTION
    an exact failure of the endpoint transfer or translation-equivariant
    induction;

FA-EXTREMUM
    one exact k>=1 for which the frozen E_k formula is false;

FA-COROLLARY
    a complete exact argument contradicting one of the stated asymptotic
    consequences.
```

### Theorem B

```text
FB-PHASE
    an exact failure of I_L, I_R, B, R_L, or R_R;

FB-ANCHOR
    failure of the frozen left/right witness or stationary restriction;

FB-SPECTRUM
    an exact characteristic polynomial or stationary-spectrum mismatch;

FB-FIXED
    Rv_*!=v_*, failed normalization or positivity, or another normalized
    stationary fixed point;

FB-LIMIT
    a complete exact normalized stationary input whose orbit does not
    converge componentwise to v_*;

FB-PHASE-LAW
    failure of I(v_*), B(v_*), or their equal phase average.
```

If several exact counterexamples survive integrity, the verifier sorts their
complete ASCII encodings and emits the lexicographically first as the
canonical witness. `RESULT.md` records that exact emitted witness and the
reported failing-gate statuses; no un-emitted set is promised or inferred.

A missing universal proof or an unsuccessful search for a counterexample is
`STOP`, not `FALSIFIED`.

## 10. Code and deterministic execution contract

The initial public pin contains exactly:

```text
probes/P-GYRON-DISCREPANCY-LOG-3/PREREG.md
probes/P-GYRON-DISCREPANCY-LOG-3/verify.py
```

`PREREG.md` is finalized first. Its exact literal SHA-256 is embedded in
`verify.py` before the two files are committed together. The verifier hash is
not embedded in either file; its SHA-256, byte count, Git blob ID, and
line-ending metadata are frozen externally by the initial commit, issue
record, and public-remote readback.

The verifier must:

- be a zero-argument Python program using only the standard library;
- use exact integers and `fractions.Fraction` only;
- use no floating point, decimal approximation, or true division producing
  floats;
- use no randomness, network, subprocess, clock, elapsed-time output,
  external data, filesystem read, or filesystem write;
- use no adaptive horizon, result-dependent expected value, dynamic import,
  `eval`, or `exec`;
- reject command-line arguments deterministically;
- avoid `assert`;
- keep proof-certificate and finite-audit implementations independent as
  specified above;
- derive every route from computed proof, audit, and integrity nodes;
- contain no hard-coded expected scientific decision;
- emit deterministic ASCII-compatible LF-only stdout with one final LF;
- emit empty stderr on `PROOF-SURVIVES` or `FALSIFIED`;
- exit zero on `PROOF-SURVIVES` or `FALSIFIED`;
- emit deterministic `STOP` output and exit nonzero on a structural or
  execution stop.

The embedded preregistration hash is an identifier. The verifier does not read
this file or its own source. External pin validation belongs to the run
harness and issue record.

Before the remote pin is verified, static source review is allowed. Import,
`py_compile`, or any execution of `verify.py` is forbidden.

## 11. Frozen stdout grammar

The verifier emits exactly these ordered line forms. Decimal fields are
computed counts. Every audit token is `PASS` or `FAIL`.

```text
P-GYRON-DISCREPANCY-LOG-3 exact verifier
authority base=1a4ae20d05cd76f93f70b2b011979b22a15fcde7 content=7830d852229ffc06c9d287d026c8ece290bf339b canon_sha256=f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
sources gyron=bca4dde1975de979e2bcc589220c0e1e2218b14e7100b677628ce679af88c1cf decoder=c10a4f22afe4a1c7c68feb92864c7acd4b041cb4773e4e7789f280ff98bc75ec
prereg sha256=<64 lowercase hex>
I01 RUNTIME arguments=<decimal> environment=<decimal>: <status>
I02 EXACTNESS integer=<decimal> rational=<decimal> forbidden=<decimal>: <status>
A01 SEAMS identities=<decimal> proof_nodes=<decimal>: <status>
A02 BALANCE identities=<decimal> proof_nodes=<decimal>: <status>
A03 DISCREPANCY identities=<decimal> boundary=<decimal>: <status>
A04 TRANSDUCER states=<decimal> transitions=<decimal>: <status>
A05 FOUR-BIT states=<decimal> words=<decimal> paths=<decimal>: <status>
A06 BASE-TABLE states=<decimal> lengths=<decimal> cells=<decimal>: <status>
A07 INDUCTION residues=<decimal> transfer_nodes=<decimal>: <status>
A08 EXTREMA formulas=<decimal> endpoint_nodes=<decimal>: <status>
A09 COROLLARIES proof_nodes=<decimal>: <status>
B01 PHASE-MAPS maps=<decimal> basis_checks=<decimal>: <status>
B02 ANCHOR-SPECTRA matrices=<decimal> polynomials=<decimal>: <status>
B03 STATIONARY restriction=<decimal> spectrum=<decimal>: <status>
B04 FIXED-POINT equations=<decimal> uniqueness_nodes=<decimal>: <status>
B05 CONVERGENCE spectral_nodes=<decimal> phase_laws=<decimal>: <status>
C01 DIRECT-PREFIX horizon=<decimal> prefixes=<decimal>: <status>
C02 ROUTE-AGREEMENT discrepancy=<decimal> phase=<decimal>: <status>
C03 NEGATIVE-CONTROLS controls=<decimal>: <status>
SCOPE L1 exact; forward phase-averaged substitution; no coarse-graining, decoder, physical measure, or L2-L6 lift
counterexample: NONE | <complete deterministic ASCII counterexample>
diagnostic: NONE | <deterministic STOP code>
gate A proof: PROOF-SURVIVES | FALSIFIED | STOP
gate B proof: PROOF-SURVIVES | FALSIFIED | STOP
gate C local audit: AUDIT-PASS | STOP
theorem A decision: PROOF-SURVIVES | FALSIFIED | STOP
theorem B decision: PROOF-SURVIVES | FALSIFIED | STOP
run integrity: PASS | FAIL
scientific decision: PROOF-SURVIVES | FALSIFIED | STOP
route: PROOF-SURVIVES | FALSIFIED | STOP
```

Normal completion emits all 34 lines in this order, with LF separators and one
final LF.

Unexpected internal exceptions are converted to the same 34-line `STOP`
grammar. The diagnostic may contain only a frozen exception-class code, never
an exception message, traceback, platform path, hostname, or private detail.

No exact expected stdout or expected scientific decision is frozen in this
document.

## 12. Pin and formal run order

The following order is mandatory.

1. Finalize `PREREG.md`.
2. Compute the exact `PREREG.md` SHA-256 and embed it literally in `verify.py`.
3. Statically review the final `verify.py` bytes, including the embedded hash,
   without importing, compiling, or executing them. Then commit
   `PREREG.md` and `verify.py` together on
   `probe/P-GYRON-DISCREPANCY-LOG-3`.
4. Push the two-file pin. Do not open a pull request.
5. Record in issue #171:
   - the full pin commit SHA and its full parent SHA;
   - the exact two-file inventory;
   - SHA-256, byte count, and Git blob ID for both files;
   - LF, CR, NUL, and final-LF metadata for both files.
6. Read both files back from the public remote at the exact pin commit and
   establish local/remote byte identity. Record the successful readback in
   issue #171. Do not open a pull request.
7. Only after that public readback and an explicit owner authorization
   recorded on issue #171, perform exactly one native Linux/aarch64 formal
   execution
   from a clean detached checkout:

   ```text
   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
   python3 probes/P-GYRON-DISCREPANCY-LOG-3/verify.py
   ```

8. Return the neutral run metadata and exact raw stdout publicly to issue
   #171. The return records UTC start and finish, exact command and
   environment, detached commit, pre-run and post-run clean status, stdout
   bytes, stderr bytes, exit code, file hashes, stdout SHA-256, byte count,
   and final-byte metadata.
9. For a valid zero-exit route with empty stderr, freeze the returned raw
   stdout byte-for-byte as `EXPECTED.txt`.
10. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` together in one result
    commit without changing either pinned file, then push. The probe directory
    now contains all five policy-required files.
11. Only now open the draft pull request against public `main`. It changes
    only `probes/P-GYRON-DISCREPANCY-LOG-3/`.
12. Let the required GitHub Linux/x86_64 check perform the first clean replay
    of the identical pinned verifier and compare exact bytes.
13. If that replay passes, record its neutral provenance in issue #171 and in
    one additive provenance commit. That commit may add the x86_64 provenance
    and final Gate C disposition to `RUN.md` and `RESULT.md`; it may not
    modify `PREREG.md`, `verify.py`, or `EXPECTED.txt`.
14. Push the additive provenance commit and require the final pull-request
    head to pass every policy and scientific check.

The initial two-file pin is intentionally not a pull-request head:
`tools/check_policy.py` requires all five probe files. No amend, rebase,
squash, force-push, verifier mutation, or preregistration mutation is
permitted after the pin. A defect seals this probe name.

A same-architecture rerun is not the required second architecture. Machine
nicknames are forbidden. `RUN.md` uses neutral fields such as
`platform: Ubuntu 24.04` and `architecture: aarch64`.

## 13. Output files

### Initial two-file pin

```text
PREREG.md
verify.py
```

No pull request is opened at this state.

### Native aarch64 result commit

After the public raw return, add together:

```text
EXPECTED.txt
RUN.md
RESULT.md
```

`EXPECTED.txt` contains the exact returned aarch64 stdout only.

At this commit, `RUN.md` records the immutable pin, public readback, native
aarch64 execution, exact command, neutral environment, exits, stderr status,
hashes, byte counts, and raw-return identity. It marks the GitHub x86_64
provenance as pending.

At this commit, `RESULT.md` records the local Gate A, Gate B, and Gate C audit
decisions, the Theorem A and Theorem B decisions, the scientific route, the
canonical emitted exact falsifier or `NONE`, every reported gate and control
status, the scope firewall, and the pending cross-architecture reproduction.
It claims no earned public status.

Only after this commit is pushed may the draft pull request be opened.

### Additive x86_64 provenance commit

After the first clean GitHub x86_64 replay passes, one additive provenance
commit records:

- the neutral x86_64 environment and check identity;
- identical verifier and preregistration hashes;
- exit zero and empty stderr;
- byte-identical stdout;
- the completed external Gate C disposition.

This commit may add that provenance and final reproducibility disposition to
`RUN.md` and `RESULT.md`. It does not change `PREREG.md`, `verify.py`, or
`EXPECTED.txt`.

No generated dataset, scan dump, cache, binary artifact, second verifier, or
auxiliary transcript is tracked.

## 14. STOP semantics

Any one of the following routes `STOP`:

- authority, tag, content commit, opening-main base, source hash, byte count,
  or public issue mismatch;
- collision with another branch, issue, probe, or directory;
- missing or changed preregistration field;
- import, compilation, or execution before verified public pin;
- a post-pin source or line-ending mutation;
- incomplete domain, boundary convention, phase convention, equality, map,
  proof node, or output route;
- incomplete six-state reachability or closure;
- missing four-bit path, base interval, endpoint, or induction node;
- finite enumeration presented as proof of an all-`L`, all-`n`, or all-`k`
  statement;
- numerical eigenvalues presented as proof of Theorem B;
- proof and audit implementations sharing a forbidden helper;
- route disagreement;
- missing or failed negative control caused by implementation or scope;
- nondeterminism, adaptive range, exception, timeout, malformed stdout, or
  unexpected filesystem or environment dependence;
- invalid commit, parent, inventory, hash, byte count, Git blob, line-ending
  metadata, or remote readback;
- opening a pull request at the initial two-file pin;
- dirty detached checkout;
- nonzero exit or nonempty stderr on a purported valid scientific route;
- architecture mismatch, verifier mismatch, or stdout byte mismatch;
- any decoder, coarse-graining, physical-measure, or L2-L6 conclusion emitted
  by the implementation.

A proof defect without a complete exact mathematical counterexample is
`STOP`, not `FALSIFIED`.

A valid `FALSIFIED` route exits zero, writes empty stderr, preserves the exact
counterexample, and proceeds through the same architecture reproduction. An
explicit `STOP` exits nonzero. A STOP seals this probe name and authorizes no
repair, threshold move, reinterpretation, or rerun.

## 15. No-coarse-graining, decoder, and physical-lift firewall

This probe is L1 exact mathematics only.

The operator `R` is a normalized forward substitution or inflation operator
for stationary sliding-pair frequencies. It is not:

- a coarse-graining map;
- a desubstitution or inverse substitution;
- an inverse RG map;
- a blocking-origin-independent finite-prefix histogram;
- a finite-prefix invariant;
- a map on histories or decoder outputs;
- a decoder factor, quotient, maximal invariant, or universality class;
- a physical probability or physical measure;
- an L1-to-L5 or L1-to-L6 bridge.

The equality of the `R_L` and `R_R` restrictions holds only on the frozen
stationary subspaces `W_Q` and `W_R`. It
does not identify the full anchoring maps or their spectra.

The value `1/6` is the stationary equal-phase sliding-pair density. It is not
identified here with:

- the six-line cardinal average;
- a Born multiplier;
- a mass density;
- a cosmological parameter;
- a selector weight;
- an apparatus outcome;
- an L5 stream or L6 measure.

This probe neither supplies nor modifies the owner of
`TM-SYM2-PHYSICAL-MEASURE [O]`, `QUADRATIC-DECODER-DATA [O]`,
`DEF-DECODER-COMPLETION-CONTRACT`, or any decoder/QDD obligation.

In particular, it does not:

- prove decoder existence, totality, uniqueness, canonicity, completeness, or
  terminality;
- transfer a binary-leg statement to the linear or quadratic decoder leg;
- infer an exact source map, marginal, event map, normalization, or layer
  gate from a common numeric value;
- reopen or repair `TM-SYM2-MEASURE [F]`;
- derive the factorization `1/6=(1/2)(1/3)` as a physical bridge;
- promote any statement to L2, L3, L4, L5, or L6;
- edit Canon, registry, frontier, evidence, dependency, gate, status,
  workflow, or release files.

No broader periodic-modulator exclusion, fractal classification, physical
density, mass, measure, time, geometry, cosmology, or observable statement is
authorized.

## 16. Pre-pin declaration

No formal execution, import, compilation, or verifier output occurred under
this probe before the preregistration pin.

The exposed analytical conclusions, merged gyron predefinition, issue #171,
earlier incubation outcomes, and current defective finite-prefix wording in
`GYRON-DENSITY [T]` are disclosed above. They may not be used to alter a
threshold or hard-code the verifier route.

The accepted verifier is reviewed only statically before its bytes become
public.
