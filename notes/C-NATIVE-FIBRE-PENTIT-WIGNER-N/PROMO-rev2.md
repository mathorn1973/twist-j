# PROMO-C-NATIVE-FIBRE-PENTIT-WIGNER-N, rev2

**Promotion proposal. NON-CANONICAL. Carries no authority and promotes nothing.**
Validation is public. Date 2026-10-02. Basis: Public Canon v97, tag `canon-v97`,
main `738e0421bd15aaea5bb6ef2a56f1cab752d44de5`. If the public head has moved,
redo the currency gate before using this document.

Rev2 supersedes rev1
(sha256 `7c15adc8d644f051d8c5b66285e3485f7dd42800f67deaa1355954694ce48c37`).
It is rev1 plus statements S7 and S8 of Addendum 1, in one document.

## 1. Candidate

`C-NATIVE-FIBRE-PENTIT-WIGNER-N`. Target line: public, `mathorn1973/twist-j`.
Action layer L1 only. Scope set by the owner: exact representation and a
bounded prohibition of counting. Not an occurrence result. The disposition
`STOP_APPLICABILITY / H_NOT_TESTED` of `C-OCCURRENCE-CYCLE-COUNT-N` stands.

Naming on landing, resolved by content: the note lands as
`notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/`; a probe, if a fold wants
computation-grade T, lands as `probes/P-NATIVE-FIBRE-PENTIT-WIGNER-1/`.

## 2. Exact statements

Carrier and conventions as in PREREG section 1 and ADDENDUM 1 section 1.

**S1, phase-point representation.** On the fibre `(q,r)` the generators act as
the identity (`a`) and as the point reflections `u -> 2s-u` with centres
(0,0), (3,0), (3,3), (1,3) (`b,c,d,e`). With
`A_(q,r)|j> = zeta^(2r(q-j))|2q-j>` over `Z[zeta_5]`: `A_u` are Hermitian
involutions of trace 1, `Tr(A_uA_v) = 5 delta`, `A_sA_uA_s = A_(2s-u)`,
`sum_u A_u = 5I`. Conjugation by `A` at a native centre is the native fibre
map on phase-point indices. The reflections generate exactly the 50 maps
`u -> +-u + t` and change no direction of lines.

**S2, boundary of the selected step.** `U(0,000000) = U(0,212110)`. The
selected one-step map on `F_5^6` has images of 6250 and 9375 states. For
`n >= 3` every origin-zero state selects the same generator: `b` if
`theta_(n-1) != theta_n`, `d` after 11, `e` after 00. This is a clock-driven
statement, not a finite autonomous factor.

**S3, invariant alternating forms.** For the linear parts of `a,b,c` and
multipliers in `F_5^*`, nonzero solutions exist only for (1,1,1), (4,1,1),
(1,4,4), (4,4,4), with dimensions 3, 3, 1, 1. The strictly invariant forms are
span{dkappa^dq, dkappa^dr, dq^dr}. Every nonzero solution has rank 2 and a
four-dimensional radical; the common radical of the strictly invariant family
is the three-dimensional space kappa = q = r = 0. No nondegenerate alternating
form is preserved, even up to a multiplier, in this realization.

**S4, line counting and inversion.** For the 30 lines,
`Pi_L = (1/5) sum_(u in L) A_u` is a rank-one projector and
`Tr(Pi_L Pi_M) = |L cap M|/5`. A real function `mu` on the 25 points with total
1 and line sums `p(L)` is `mu(u) = (sum_(L through u) p(L) - 1)/5`; for
`p(L) = Tr(rho Pi_L)` it equals `W_rho`. A nonnegative point distribution with
membership reading of all 30 lines exists if and only if `W_rho >= 0`.

**S5, real sum-zero negativity.** For every nonzero real `psi` with zero sum,
in any odd dimension `d`, the row `r=0` of `W_psi` sums to zero and is not
identically zero; the negativity is at least `1/(2 sqrt(d(d-1)))`, that is
`sqrt5/20` at `d=5`.

**S6, conditional census.** Under the declared reading of the QDD four-vector
in the real sum-zero sector: the LOW direction has negativity `sqrt5/5`;
`|<l,v~>|^2/|v~|^2 = s^2/(4(5Q-s^2))` for every real `v != 0`; over the 624
preparations the negativity has 39 distinct values, minimum `(1+sqrt5)/10` at
32 preparations, maximum `29/220 + (8/55) sqrt5` at 16.

**S7, reader boundary.** `xi_E(u) = Tr(E A_u)` is the unique function on the 25
points whose line averages are `Tr(Pi_L E)`. An effect is a point reader on
line preparations exactly when `0 <= xi_E <= 1`. For the LOW projector of the
declared reading the response is 1 once, 3/4 four times, -1/4 four times,
`(1+sqrt5)/8` eight times, `(1-sqrt5)/8` eight times: twelve negative values.
On the Fourier line state the LOW probability is `1/4`; on the 30 line states
only two LOW probabilities are multiples of `1/5`. The acceptance projector
`I - |+><+|` has a 0/1 response; HIGH does not lie in `[0,1]`.

**S8, counting contract with state change.** For line preparations, line
readers, and the update `u -> u + t delta` with one fresh uniformly counted
`t in F_5` per reading: `Pi_M Pi_L Pi_M = (|L cap M|/5) Pi_M`; counting the
125 microstates returns the two-round law
`Tr(Pi_L Pi_M1) Tr(Pi_M1 Pi_M2)` in all 1080 scenarios; at least one such
coordinate per reading is necessary; the non-disturbing reading returns the
first outcome with count 1 where the law gives `1/5`, in all 900 three-round
scenarios. Ensemble count at L1. No event contract and no native source of
the coordinate.

## 3. Falsifiers

S1: one state or pair where an identity fails. S2: failure of the collision, or
a tick `n >= 3` with two selectors or a selector off the rule. S3: a nonzero
solution for another multiplier triple, or a solution of rank 4 or 6. S4: a
line operator that is not a rank-one projector, a pair of lines with a
different trace, or a state whose inversion differs from `W`. S5: a nonzero
real sum-zero vector in odd dimension with nonnegative row zero, or negativity
below the bound. S6: a preparation with negativity below `(1+sqrt5)/10`, a
different count of minimizers or values, or a mismatch of the table hash.
S7: an effect whose inversion differs from `Tr(E A_u)`, a different LOW
response multiset, or a LOW probability other than `1/4` on the Fourier line
state. S8: a pair of lines where the sandwich identity fails, a two-round
history whose count differs, or a three-round scenario where the
non-disturbing reading agrees with the law.

## 4. Verifiers and pins

```text
BASE
cbda8c9f0fbc7da3b5baeed685d9e8592ecffaa6b70617633a271056ca94757c  PREREG-C-NATIVE-FIBRE-PENTIT-WIGNER-N.md
ddf883612cd6fff00b227d8fca76668fc876ef1873f819da724ee0e66426dd63  verify_c_native_fibre_pentit_wigner_n_2026-10-02.py
3b2bdc432e1bfebcd453b83a6766a2863b6a1d54243180cbc20e0b1ce4ea39ad  stdout, 4476 bytes, 38 of 38 PASS
c48073764b881238f9dc980ddc1b6467dc2b60637f5ddcc22881a7e9f711ddf6  break_check_c_native_fibre_pentit_wigner_n_2026-10-02.py
f1044cc3c1371342ca3bfc5b921460332fa7c07a17999874e556dc1891cf6f0f  breaker stdout, 2660 bytes, 21 of 21 PASS
c423a1edf376c9cdbd0653b4e89a284ed16e9bfea69586c3cb1c5e208351c905  negativity table of the 624, identical by two routes
ADDENDUM 1
f5c518380864989d07fc37c381e12bec984b1408b73ff6d6b5319a55324a7d17  ADDENDUM-1-PREREG-C-NATIVE-FIBRE-PENTIT-WIGNER-N.md
cd609366fb656ca79fd91e7a7090ea35f0974e85bfe5f3616866df27dfe4b346  verify_addendum1_c_native_fibre_pentit_wigner_n_2026-10-02.py
fc5432d288f340038d64edb5ceab9aeec71c3b400cc378c8556878089b549bed  stdout, 2436 bytes, 12 of 12 PASS
6bac007185d0c4424f761b337a8f30a43209d93b250033c69207a4e6935bc816  break_check_addendum1_c_native_fibre_pentit_wigner_n_2026-10-02.py
6e3aa7f8eac8d2df31f6c60f4e2b5cfa78c11a4092501b4a5defa1a12a733bd6  breaker stdout, 1403 bytes, 11 of 11 PASS
```

Project copies carry the prefix `claude_`. All four programs: standard library,
exact arithmetic, no float, a few seconds. The base verifier runs from the
repository root and checks the SHA-256 of `reproduce/census/verify.py`; the
other three need no repository file. Environment:
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`. One
architecture so far: platform Ubuntu 24.04, architecture x86_64.

Exposure. Targets were seen before each freeze, and both pinned verifiers have
already been executed in the incubation lane. Both breakers were written by
the session that wrote the verifiers: they are independent code paths, not
independent authors. A public probe must declare all of this, pin fresh, and
run its two legs under its own pin. It cannot claim blindness.

## 5. Proposed status and scope

| Statement | Proposed status | Grade |
| --- | --- | --- |
| S1 | T | proof inline, exhaustive finite audit |
| S2 | T | substitution and proof from `KERNEL-Z6-SYNCHRONIZATION` |
| S3 | T after two-architecture byte identity, C before | exact finite linear algebra |
| S4 | T | proof inline, exhaustive finite audit |
| S5 | T | proof inline |
| S6 | C, conditional on the declared reading | finite census |
| S7 | T for uniqueness and the control value; C, conditional on the declared reading, for the LOW and HIGH tables | proof inline; finite tables |
| S8 | T | proof inline, exhaustive finite audit |

No H or O row closes. `QDD-INSTRUMENT-APPARATUS`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS` and `QDD-TERMINAL-EVENT-SEMANTICS` keep
their status and scope.

## 6. Dependency edges

```text
S1 -> QDD-U-INDUCED-CHANNEL, U-NATIVE-COMMON-READY-SOURCE-RETENTION
S2 -> KERNEL-Z6-SYNCHRONIZATION
S3 -> generator definitions of the declared architecture
S4 -> S1
S5 -> S1
S6 -> S4, S5, U-NATIVE-READER-STREAM-SPECTRA (the ratio s^2/(4(5Q-s^2)))
S7 -> S4
S8 -> S4
```

## 7. Edits a fold would make

Minimal landing, no normative file touched: add
`notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/`, marked NON-CANONICAL, with the two
preregistrations, the two verifiers, their stdout as `EXPECTED` files, the two
breakers, the two results, a `RUN.md` and a `README.md`.

If a later integer-versioned fold adopts rows, in the registry schema
`claim_id  status  scope  canon_section  evidence  falsifier`:

```text
U-NATIVE-FIBRE-PHASE-POINT   T   scope of S1 and S2   section 2   probes/P-NATIVE-FIBRE-PENTIT-WIGNER-1
KERNEL-INVARIANT-ALTERNATING-FORMS   T   scope of S3   section 16   probes/P-NATIVE-FIBRE-PENTIT-WIGNER-1
PENTIT-LINE-COUNT-INVERSION   T   scope of S4 and S8   section 8   inline
PENTIT-REAL-SUMZERO-NEGATIVITY   T   scope of S5   section 8   inline
PENTIT-POINT-READER-UNIQUENESS   T   scope of S7, uniqueness only   section 8   inline
QDD-SUMZERO-WIGNER-CENSUS   C   scope of S6 and the tables of S7, conditional on the declared reading   section 2   probes/P-NATIVE-FIBRE-PENTIT-WIGNER-1
```

Section numbers and row names are suggestions for the fold author. Frontier:
no edit. `CORE.md`: no edit. The reading premise of S6 and S7 is not proposed
as a D row; that is an owner decision.

Prose for any hashed file must be checked against `tools/check_canon.py`
before it is written.

## 8. Open items carried with the proposal

1. Sharp bound `(1+sqrt5)/10` for the negativity in the real sum-zero sector at
   `d=5`: `[O]`, falsifier one vector below that value; evidence is the census
   and a box search of 1450 vectors.
2. Second architecture leg pending for all four programs.
3. A breaker by an independent author is still owed.
4. Owner decision on the reading premise.
