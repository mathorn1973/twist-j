# C-OMEGA-U-TURING-1

**Title:** Finite checkpoint and internal-halting no-go for Turing universality

**Status:** NON-CANONICAL INCUBATION NOTE. No public T/D/C/H/O/F status is created here.

**Date:** 2026-08-11

**Owner lock:** issue #336

**Layer:** L1 state and autonomous update only. The only read used in the main no-go is entry of the checkpoint into one fixed set `H subset X`. No L2-L6 lift, decoder completion, measure, continuum, or physics claim is made.

**Purpose:** record the strongest exact answer currently obtained to the question whether the existing public autonomous TWIST-J kernel is itself a universal Turing machine, without adding a tape, writable Log, decoder-side universal computation, program-dependent transition law, or noncomputable input encoding.

---

## 0. Public authority and basis

At creation, public authority is:

```text
STATE:          ACTIVE
CANON:          Public Canon v41
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v41
CONTENT_COMMIT: 096e97b44727830102846746f0c723af1c59a2cf
CANON_SHA256:   a15474c4204db637d7ce276ef6ea5dbe94b50af593e46389fd5e77aa16ca80e8
CANON_BYTES:    198932
BASE_MAIN:      29929fbcb873b403e3e0fc1c1c96ef5959ecd6f2
```

The declared Canon hash agrees with `canon/SHA256SUMS`. The `canon-v41` tag and the declared content commit resolve `canon/CANON.md` to the same Git blob. Public Canon v41 is therefore the scientific basis of this Note.

The public Core declares the autonomous state and update:

```text
Omega = N_0 x F_5^6,                    omega = (n, psi),
theta_n = s_2(n) mod 2,
z_6(psi) = sum_k psi_k mod 5,
U(n, psi) = (n + 1, g_(z_6(psi) + 2 theta_n mod 5)(psi)).
```

`N_0` is the forward orbit of zero under the 2-adic odometer. The projection to `F_5^6` is the finite checkpoint and is not the complete autonomous state. Log streams are derived orbit records. Decoder outputs do not feed the update.

This Note uses only that public state type, the fixed Thue-Morse drive, determinism, and finiteness of the checkpoint. It does not use the detailed formulas for the five generators, `CENSUS-313`, the decoder dictionaries, or any physical interpretation.

Public status remains unchanged. In particular, the proof below does not claim that the checkpoint, generators, selector, or decoder are uniquely forced by `J`.

---

## 1. The generic finite-checkpoint system

Let `X` be any finite nonempty set and write

```text
q = |X|.
```

Let

```text
f_0, f_1 : X -> X
```

be arbitrary fixed maps. Let

```text
theta_n = s_2(n) mod 2
```

be the Thue-Morse bit. Define

```text
Omega_X = N_0 x X,
U_X(n,x) = (n+1, f_(theta_n)(x)).
```

The present public TWIST-J L1 system is an instance with

```text
X = F_5^6,
q = 5^6 = 15625,
f_t(x) = g_(z_6(x)+2t mod 5)(x).
```

The generic theorem is intentionally stronger than an audit of the particular generator table: it applies to every pair `f_0,f_1` on the same finite checkpoint carrier.

---

## 2. Tail-capacity theorem

### Candidate theorem T1

Among any `q+1` initial states of `Omega_X`, two forward orbits have a common infinite tail. Hence at most `q` forward orbits are pairwise tail-disjoint.

### Proof

Take arbitrary starts

```text
omega_i = (n_i,x_i),       i = 0,...,q.
```

Choose one common future counter slice

```text
N >= max_i n_i.
```

After exactly `N-n_i` steps, every orbit lies in

```text
{N} x X,
```

which contains exactly `q` states. By the pigeonhole principle, two synchronized images coincide. Since `U_X` is deterministic, their complete future tails coincide. This proves the bound.

The bound is sharp: if `f_0=f_1=id_X`, the `q` starts `(0,x)`, `x in X`, are pairwise tail-disjoint.

For the public TWIST-J checkpoint:

```text
number of pairwise tail-disjoint L1 orbits <= 5^6 = 15625.
```

The starting counters may be arbitrarily large. Merely encoding more information in the initial value of `n` does not evade the tail bound.

---

## 3. Persistent-label corollary

### Candidate theorem T2

Let

```text
P : Omega_X -> A
```

be invariant under the update:

```text
P(U_X(omega)) = P(omega)
```

for every `omega`. Then

```text
|image(P)| <= q.
```

### Proof

Two starts with different invariant labels cannot acquire one common future state, because that state would have to carry both labels. Distinct labels therefore require pairwise tail-disjoint orbits. Apply T1.

### Scope

This blocks an unbounded immutable program label or an unbounded family of persistent halted outputs inside the present L1 state type. It does not by itself exclude a transient computation whose answer is read once and discarded. The stronger Turing obstruction is the reachability theorem below.

---

## 4. Exact finite word summaries

Fix one target set

```text
H subset X.
```

For a finite binary word `w`, define its exact summary

```text
S(w) = (T_w, B_w),
```

where

```text
T_w(x) = final checkpoint after reading w from x,
B_w(x) = 1 iff H is visited at the start or while reading w from x.
```

For concatenation `uv`,

```text
T_(uv) = T_v o T_u,
B_(uv)(x) = B_u(x) OR B_v(T_u(x)).
```

Therefore the summaries form a finite effectively computable monoid. There are at most

```text
q^q * 2^q
```

possible summaries.

No asymptotic approximation and no floating point arithmetic is involved.

---

## 5. Thue-Morse substitution summaries

Let

```text
mu(0) = 01,
mu(1) = 10.
```

Define

```text
A_r = S(mu^r(0)),
B_r = S(mu^r(1)).
```

Since

```text
mu^(r+1)(0) = mu^r(0) mu^r(1),
mu^(r+1)(1) = mu^r(1) mu^r(0),
```

we have the exact recurrence

```text
A_(r+1) = A_r * B_r,
B_(r+1) = B_r * A_r,
```

where `*` denotes summary concatenation.

The pair `(A_r,B_r)` evolves deterministically in a finite set. It is therefore eventually periodic, with exact preperiod and period obtainable by first-repeat detection.

---

## 6. Exact decomposition of every Thue-Morse suffix

Let `n >= 0` be an arbitrary starting counter. Choose the strict next power of two

```text
M = 2^R > n.
```

### Finite prefix

The interval `[n,M)` can be partitioned exactly into aligned dyadic blocks

```text
[a, a+2^r),       2^r divides a.
```

Write `a = j 2^r`. For `0 <= s < 2^r`, the binary digits of `j` and the `r` low digits of `s` occupy disjoint positions, hence

```text
theta_(a+s) = theta_j XOR theta_s.
```

Therefore the Thue-Morse word on the whole block is exactly

```text
mu^r(theta_j),
```

and its complete checkpoint action and target visitation are represented by `A_r` or `B_r`.

### Infinite tail

For every `r >= R`, the aligned interval

```text
[2^r, 2^(r+1))
```

has `j=1`, so its exact word is

```text
mu^r(1).
```

Thus every suffix beginning at `n` is exactly

```text
finite aligned dyadic prefix,
mu^R(1), mu^(R+1)(1), mu^(R+2)(1), ... .
```

This is the structural reason the unbounded counter does not create an unbounded mutable control state.

---

## 7. Exact reachability theorem

### Candidate theorem T3

For every finite `X`, every pair `f_0,f_1`, every fixed target `H subset X`, and every start `(n,x)`, the predicate

```text
exists k >= 0 such that checkpoint(U_X^k(n,x)) lies in H
```

is decidable by a terminating exact algorithm.

### Decision procedure

1. Build the finite summary-pair recurrence `(A_r,B_r)` and find its exact preperiod and period.
2. Process the finite aligned dyadic prefix from `n` to `2^R`.
3. Process the tail blocks `B_R,B_(R+1),...`.
4. Once the summary pair is in its periodic part, record the pair

   ```text
   (current checkpoint, summary phase).
   ```

5. If a block summary reports a hit of `H`, return `YES`. Recursive substitution splitting locates an exact first-hit offset if desired.
6. If a boundary pair repeats without a hit, return `NO`. From that repeated checkpoint and summary phase onward, the complete future is identical to a previously checked future.

### Termination

After the finite prefix and finite summary preperiod, the boundary state belongs to

```text
X x Z/pZ,
```

where `p` is the exact summary-pair period. There are only `q p` such pairs. A hit or a repeated pair therefore occurs after finitely many tail boundaries.

A negative answer is consequently a finite cycle certificate, not a bounded-search guess.

---

## 8. Internal-halting Turing no-go

Freeze the following simulation class.

### Class H

A Turing program and input `(M,w)` are encoded computably as one initial simulator state

```text
E(M,w) = (n,x) in Omega_X.
```

The transition law `U_X` is the same for every program and input. There is one fixed internal halt set

```text
H subset X
```

such that the simulated machine halts exactly when the checkpoint first enters `H`. A decoder may report the event, but may not independently decide the ordinary Turing halting problem.

### Candidate theorem T4

No system `U_X` of the generic finite-checkpoint Thue-Morse form is Turing-universal under Class H.

### Proof

Assume such a universal simulation exists. Given an arbitrary Turing machine `M` and input `w`, compute

```text
E(M,w) = (n,x).
```

By Class H, `M(w)` halts exactly when the checkpoint orbit from `(n,x)` reaches the one fixed set `H`.

Apply T3. This gives a terminating exact algorithm deciding whether `M(w)` halts. That contradicts the undecidability of the ordinary Turing halting problem. Therefore the assumed universal simulation does not exist.

### Applied public conclusion

At this exact scope:

```text
The present public TWIST-J L1 kernel is not a universal Turing machine
under computable initial encoding plus one fixed internal checkpoint halt set.
```

The unbounded initial counter is fully admitted. The obstruction is not a shortage of possible inputs. It is the finite mutable checkpoint under one fixed Thue-Morse drive, which makes the frozen internal halt reachability problem decidable.

---

## 9. What is and is not killed

### Killed inside the frozen class

The present L1 architecture cannot obtain ordinary Turing universality merely by:

- calling the unbounded counter a tape;
- calling the derived Log a writable memory;
- hiding an arbitrarily large immutable program label in the finite checkpoint;
- using one fixed finite checkpoint halt condition.

The Log is a history of the orbit. A Turing tape is mutable state whose stored content affects later transitions. Those are different types in the current public architecture.

### Not killed

T4 does not classify systems that add any of the following:

1. **An infinite writable L1 carrier.** This invalidates the finite-summary proof.
2. **A new state-write channel.** Feeding readout back into L1 changes the autonomous state architecture.
3. **Unrestricted decoder computation.** A decoder can be made universal externally, but then the universality belongs to the decoder, not to `U_X`.
4. **A program-dependent transition law or halt predicate.** This places the program in the law rather than in the initial state and is not one universal machine.
5. **A noncomputable initial encoding.** This can hide the halting answer in the input and is excluded by the simulation contract.
6. **A different non-halting notion of computational universality.** T4 is a Class H theorem, not a classification of every possible trace factor, transducer, or intrinsic-universality definition.

No conclusion about physical computability, observers, quantum measurement, cosmology, or the continuum follows from T4.

---

## 10. Relation to the original Boolean question

The motivating question separated three capabilities:

```text
local Boolean algebra
+ addressable write
+ unbounded search/minimization.
```

The current public L1 architecture has:

```text
finite local update              present
unbounded monotone counter       present
unbounded writable memory        not present in the state type
fixed internal halt reachability decidable by T3
internal minimization primitive  not present
```

The first-hit value

```text
mu_H(n,x) = min { k >= 0 : checkpoint(U_X^k(n,x)) in H }
```

is externally computable by T3 when it exists. That does not make minimization an internal primitive of `U_X` and does not create writable memory.

The separate NON-CANONICAL Boolean carry note `C-BOOLEAN-CARRY-J-ORBIT-1` is compatible with this result but is not a dependency. The carry route concerns the algebraic bridge from Boolean carry to a conditional `J` orbit. This Note concerns computational capacity of the already declared autonomous state architecture.

---

## 11. Positive route left open

The no-go sharpens the positive question.

The multiplicative powers of `J` provide an abstract infinite index axis

```text
<J> ~= Z.
```

A natural candidate writable carrier would be a group algebra such as

```text
M_J = F_5[<J>] ~= F_5[u,u^-1]
```

or a one-sided variant `F_5[u]`, with coefficients as cells and multiplication by `u` as address shift.

This is only a future construction target. The present public architecture does not contain this carrier, and this Note does not claim that `J` uniquely forces it.

A positive universality program would have to derive or separately postulate, then preregister:

1. the unbounded carrier;
2. one exact local reversible read/write rule;
3. one uniform program/input encoding;
4. one simulation theorem for a known universal machine or tag system;
5. one halt/output readout whose computational power is not supplied externally by the decoder.

Compatibility with `J` is not derivation from `J`.

---

## 12. Incubation provenance and self-break

The predecessor local package was created against Public Canon v39 and is not public evidence. Its exact archive hash is

```text
C-OMEGA-U-TURING-1.zip
sha256 8f07feb958915dc33f272e7ff9d34779a58ab4ea5ed8097e3216666c80fb75fe
```

Pinned local components included:

```text
PREREG.md  sha256 3299d7b9156327f936103f00ff8ffe7b4c0b2380346cfd800a45fb1292dc23cf
verify.py  sha256 2765d29c443fcb48a22c64afbbff14c77119365b6c9211efcb1304bab084fb0f
break.py   sha256 e3d15329b12f3bc375a480acb7e27b61401f59d8ceaaea5b78b718be9c6ecc66
RESULT.md  sha256 b6ca68a78ba7af63ff6a05cec1153bfa36230a7a2419c426c3bca6566088e7f2
```

The verifier and breaker were exact, deterministic, and local. They were run on one x86_64 lane only. Their machine output is therefore at most candidate-C audit provenance. The candidate-T grade of T1-T4 rests on the written proofs, not on the local run.

The self-breaker did not supply blind independent confirmation. It attacked the frozen reachability procedure, dyadic decomposition, summary recurrence, and tail bound. No frozen mathematical falsifier fired in that local campaign.

The v39 package mentioned the then-live `OBSERVER-WRITE-PORT` row. Public Canon v41 retired that row as a category error. This Note does not reuse it. The only current public fact needed here is the Core's typed statement that decoder outputs do not feed the autonomous update.

---

## 13. Status and promotion boundary

Incubation ledger only:

```text
T1  candidate-T  tail capacity
T2  candidate-T  persistent-label bound
T3  candidate-T  exact Thue-Morse reachability decision
T4  candidate-T  Class H Turing nonuniversality
C1  candidate-C  one-lane exact audit provenance
```

No public claim is created by this Note.

A later formal public probe would require a new owner-approved preregistration, a public exact verifier, the repository's two-architecture procedure, and a separate fold decision. Nothing in this Note authorizes a Canon or Registry change.

---

## 14. Final boundary

The result is narrower and stronger than the original intuition.

```text
The present public TWIST-J kernel is not a universal computer in the frozen
internal-halting sense. It is a much narrower exact machine.
```

Any route to Turing universality must add or derive a genuinely unbounded writable carrier or choose a fundamentally different computational semantics. Renaming the counter or the derived Log as memory is not enough.
