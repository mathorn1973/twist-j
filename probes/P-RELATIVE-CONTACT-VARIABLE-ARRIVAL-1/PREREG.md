# P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1

NON-CANONICAL / L1 / result-exposed confirmation protocol.
Owner: A. M. Thorn, coordinated public apparatus session, 2026-11-02.
Reservation: https://github.com/mathorn1973/twist-j/issues/1856.
Authority basis: public `main` at
`0c33e2b281e39127c269ef5dd7f5b529a62e9e65`, Public Canon v107 ACTIVE.

## 1. Question, prior exposure and action layer

Test the complete finite L1 contract in `CONTRACT.md`: one prepared carrier,
one fixed contact word, two retained records and funded reuse for all ten
declared inputs. This supplies a candidate positive witness for
`RELATIVE-CONTACT-COMMON-APPARATUS-OPEN`; neither this protocol nor a passing
run changes the Canon or closes its registry row automatically.

The construction, ten-input endpoint states, two gap values and successful
incubation calculations are already known. This is an explicitly
result-exposed public confirmation, not a blind discovery preregistration.
`PROVENANCE.md` distinguishes those antecedents from this public pin. The
accepted `verify.py`, this protocol and the normative word must be committed,
pushed and read back before the first execution of this public verifier.
Static inspection and compilation are permitted before that pin. Exact pin
commit and file hashes will be recorded in `RUN.md`. No frozen executable,
input family, prediction or failure threshold is revised after execution.

## 2. Equation and complete controller

The coefficient ring is `O = Z[j]`, with `1+j+j^2+j^3+j^4=0` and `rho=j^2`.
For four coefficients `a=(a0,a1,a2,a3)`, use the exact account

```
Q(a) = (5*sum(ai^2) - sum(ai)^2)/2.
C(a,b) = (a,b)                                  if a-b is not in 2O;
C(a,b) = ((a+b+rho*(a-b))/2, (a+b-rho*(a-b))/2) otherwise.
```

Set `u=1-rho`, `w=1+rho`, `b=1+rho^2`. All words act in chronological
left-to-right order. Slots are zero-based in the equations and verifier:
source `Y=(0,1,2)`, receiver clock `(3,4)`, marker `g=5`, selector `(6,7,8)`,
helper `h=9`, sampling gate `t=10`, five memory pairs in A at `11..20` and
five in B at `21..30`. A pair in phase `p` is `(-rho^p*b,rho^p*b)`.

The read word `R` is fully specified in `CONTRACT.md`, and constructed from
its fixed commutator blocks in `verify.py`. Define

```
F = C(0,1) C(1,2); F^-1 = C(1,2)^4 C(0,1)^4; T = C(3,4);
S = R F^-1 R F F T.
```

`R` has 261 contacts and `S` has 535. The complete normative oriented word
is `WORD535.txt`, which uses one-based slots. Its SHA-256 is
`ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b`.
The verifier requires both that exact file hash and contact-for-contact
equality between its parsed list and the independently expanded block word.
Every input and every tick receives this same word. State observations in
the verifier assert predictions; they never select the next operation.
The name `S` is distinct from the native rule U of the Canon.

## 3. Carrier, input data, preparation and finite horizon

There are 31 sites and total account 82. Write
`Y_n=F^n(0,2,0)`, with `n` taken modulo nine. The entire input family is

```
(n,k) in {0,1} x {0,1,2,3,4};
source = Y_n; receiver clock = (rho^k*w,-rho^k*w).
```

These five input sites vary with the input. The other 26 sites have exactly
one common preparation: `g=t=0`, selector `(u,0,0)`, `h=w`, and ten ready
memory pairs `(-b,b)`. No source input is loaded after the initial
preparation. No bank is supplied or reset externally during the run.
All ten preparations share the same labelled residue vector modulo `(1-j)`.
Their total sum is 4. The calculation executes ten complete `S` words per
input, ending after 5,350 primitive contacts. This is the declared common
horizon of three events; no fourth-event guarantee is asserted.

## 4. Frozen predictions and output equality

Use zero-based tick `r=0,...,9`. The source and receiver clock at every
complete-word boundary advance freely to `(Y_(n+r+1), rho^(k+r+1)*w)`.
The controls have `g=t=0`, `h=w`, and selector A, B, skip according to the
number of completed events modulo three. Both complete R endpoints in
each tick are also specified as full 31-site states: the first retains
source phase `n+r`, the second has source phase `n+r-1`; both retain receiver
clock phase `k+r`, and all controls and banks equal the formulas below.

For `n=0`, event ticks are `(0,1,9)`; for `n=1`, `(0,8,9)`. The first event
writes A, the second B, and the third advances the selector without writing.
Let `Delta=1` for `n=0`, and `Delta=8` for `n=1`. The occupied records are

```
pA = -k mod 5; pB = -(k+Delta) mod 5.
```

A record `p` means phase one in that set's pair numbered `p`, and phase
zero in the other four pairs. The blank set has all five phases zero; it is
different from record zero. Set A carries its stated record from tick zero;
B is blank until tick `Delta` and carries its stated record thereafter.
Each occupied archive remains exactly equal at all subsequent complete-S
boundaries through the horizon. Intra-word immobility is not predicted.

The ordered pair `(pA,pB)` distinguishes all ten inputs: `k=-pA mod5` and
`(pA-pB) mod5=1` or `3` distinguishes `Delta=1` or `8`, hence `n=0` or `1`.
There are five first-record values and two second-record alternatives at
each first-record value. Neither individual five-valued record distinguishes
all ten inputs by itself. Output equality means literal equality of the
two complete ten-site bank states, equivalently equality of their valid
one-hot codes. All ten endpoints retain the one common initial residue
vector: the distinctions are in phases, not in altered residues.

An onset is only the first `C(Y_middle,g)` contact of an active R, identified
by `g:0 -> u` at its designated position. These positions have one-based
contact offsets 1 and 270 within S. Other internal changes of `g` are not
onsets. In particular, no claim that `g` alone remains zero between these
designated onsets is made; the active gate uses the pair `(g,h)`.

| Source input | First two onsets | First two R completions | Elapsed contacts |
|---|---|---|---:|
| n=0 | 1, 805 | 261, 1065 | 804 |
| n=1 | 270, 4281 | 530, 4541 | 4011 |

The actual bank-write microcontact, onset and R completion are distinct.
The clock counts free macro advances modulo five, not every contact.
Ten complete inverse words, reversing S and repeating each contact four
times, restore every complete preparation. The exposed endpoint digest,
using the frozen verifier serialization, is
`a10212635f9c3a5079952aa7a46a24352f62c6506fcb43cc4c10295ea4d347e4`.

## 5. Accepted exact code and systematics

`verify.py` is a self-contained Python 3 standard-library verifier, accepted
and frozen with this file. Run it from the repository root with assertions
enabled. It prints deterministic UTF-8 JSON with a final newline, writes no
files and uses neither floating point, randomness nor external data.

It exhausts all ten preparations, 100 full-S boundaries, 200 full-R
checkpoints, 30 designated onsets and ten complete trajectory inverses.
It applies 267,500 forward/inverse contacts. Every changed pair is computed
both in four coefficients modulo the cyclotomic polynomial and independently
in five cyclic coefficients modulo a constant vector. The results agree
after every applied contact. Each arithmetic implementation checks exact
sum, quadratic account and each labelled residue for its contact results;
memoization only reuses immutable, exactly checked pair maps.

The verifier also checks the exact common 26-site auxiliary preparation,
the singleton input/end residue-vector class, pair-record injection,
retention at boundaries, both timing conventions and the already exposed
endpoint digest. It reports hashes of all full boundaries and R endpoints.
It has no dependency on earlier private code or result files. This is an
independent representation crosscheck inside one executable, not a claim
of two independent implementations of the whole experiment.

The author records one local run. Repository CI must replay the same accepted
verifier against one committed `EXPECTED.txt`, with zero exit code and empty
stderr, on GitHub-hosted x86_64 and aarch64 using Python 3.12. Both required
architecture jobs and their aggregate `check` must pass. Agreement of
multiple sessions on one architecture alone does not satisfy that gate.

## 6. Failure threshold and limitations

Tolerance is exactly zero. Any word/hash mismatch, arithmetic disagreement,
incorrect complete checkpoint, wrong event count or schedule, incorrect
record, collision of declared joint outputs, failed inverse, archive change
at a certified boundary, violated common preparation or invariant, incorrect
timing, or endpoint-digest mismatch fires the relevant frozen prediction.
Record the outcome without changing this domain or executable to rescue it.
Byte disagreement with `EXPECTED.txt`, nonzero exit or nonempty stderr fails
the reproduction gate. An incomplete gate follows the repository's abandoned
pin policy, retaining the consumed identifier and frozen source.

This contract concerns exactly the declared ten-input, ten-tick family.
It asserts no arbitrary-interval measurement (for example gaps 1 and 6
alias modulo five), permanent lock, indefinitely reusable archive, source
independence after preparation, randomness, optimality or shortest word.
It supplies no native-U compilation, cross-layer lift, measured-energy
identity, external post-start loading interface or physical realization.
Algebraic proofs remain candidate-T and finite results candidate-C until
the appropriate public review and separate Canon decision.
