# PREREG. P-RAMIFIED-TM-LIFT-1

Public lock: issue #74. Base: Public Canon v10, commit
`72a04e1e2dae8df66f170b169328611b75a8a1af`.

```text
LAYER:  L1 (state/readout arithmetic). No lift to L2-L6 is claimed.
TARGET: new RAMIFIED-TM-LIFT theorem candidate.
```

## Frozen statement

Let `zeta = zeta_5`, `lambda = 1 - zeta`, and

```text
J_lambda := [J] mod lambda = [1 + zeta^2] mod lambda = 2 in F_5^x.
```

The subscript denotes ramified reduction, not conjugation. Let `s2(n)` be
the binary digit sum, `t_n = s2(n) mod 2`, and let

```text
q : F_5^x -> F_5^x/{+-1} ~= F_2
q(+-1) = 0,  q(+-2) = 1.
```

Define the digit automaton by `T_0(u) = u`, `T_1(u) = J_lambda u`, with
initial state `1`. Equivalently, freeze the recursion

```text
Theta_0      = 1,
Theta_(2n)   = Theta_n,
Theta_(2n+1) = J_lambda Theta_n.                         (A)
```

For every `n in N_0`, the claim is

```text
Theta_n = J_lambda^s2(n),
q(Theta_n) = t_n,
Theta_n^2 = (-1)^t_n in F_5^x.                           (B)
```

The four-cycle `1 -> 2 -> -1 -> -2 -> 1` is the orbit of the digit-1
transition. It is not the chronological `n -> n+1` transition. For
`c_n = nu_2(n+1)`, equivalently the number of trailing one-bits of `n`,
the chronological transition is the exact carry cocycle

```text
s2(n+1)    = s2(n) + 1 - c_n,
Theta_(n+1)= Theta_n J_lambda^(1-c_n),
t_(n+1)    = t_n XOR 1 XOR (c_n mod 2).                  (C)
```

Let `M_J` be multiplication by `J` on the integral power basis
`(1,zeta,zeta^2,zeta^3)` and `Tr4(a,b,c,d) = a+b+c+d`. The inherited
`CODEC-TR4 [T]` premise is

```text
Tr4(M_J x) = 2 Tr4(x) - 5 x_(zeta^2)                    (D)
```

for every `x in Z^4`, and its only nonzero scalar-readout covectors over
`F_5` are the nonzero multiples of `Tr4`, all with multiplier `2`.
Consequently, for every `x0 in Z^4` with `Tr4(x0) = 1 mod 5`, every
`k >= 0`, and every `n in N_0`,

```text
[Tr4(M_J^k x0)]_5              = J_lambda^k,
[Tr4(M_J^s2(n) x0)]_5          = Theta_n,
q([Tr4(M_J^s2(n) x0)]_5)       = t_n.                   (E)
```

Thus the four phases live on the one-dimensional `Tr4` readout quotient,
not on the whole `M_J` state. The fixed `CODEC-TR4/M_J` channel selects
the multiplier `2`; the sign quotient by itself is inversion-blind and
also sends `3^s2(n)` to `t_n`.

The same integer `2` is the exact binary carry weight:

```text
x + y = (x XOR y) + 2 (x AND y)  for all x,y in N_0.       (F)
```

## Frozen all-n proof

1. Reduction modulo `lambda` sends `zeta` to `1`, hence sends
   `J = 1 + zeta^2` to `2`. In `F_5^x`, `2^2 = -1` and `2` has exact
   order four.
2. The two binary identities `s2(2n)=s2(n)` and
   `s2(2n+1)=s2(n)+1` prove by induction on binary length that (A) has
   the unique solution `Theta_n=J_lambda^s2(n)`.
3. The quotient is a group homomorphism with `q(J_lambda)=1`; applying it
   to the preceding formula gives `q(Theta_n)=s2(n) mod 2=t_n`.
   Squaring gives `Theta_n^2=(-1)^s2(n)=(-1)^t_n`.
4. Incrementing `n` clears exactly `c_n` trailing ones and creates one
   new one. This proves the first line of (C). Exponentiation by
   `J_lambda`, followed by `q`, proves the other two lines.
5. Reducing (D) modulo five gives `Tr4 M_J = 2 Tr4`. Induction on `k`
   gives `Tr4(M_J^k x0)=2^k Tr4(x0) mod 5`. With `Tr4(x0)=1`, this is
   the first line of (E); substitution `k=s2(n)` and step 3 give the
   remaining lines.
6. The public uniqueness clause in `CODEC-TR4` says that the fixed
   nonzero readout line has no multiplier other than `2`. This removes
   the inverse-generator ambiguity only after the `M_J/Tr4` channel is
   fixed; no global uniqueness of four-phase lifts is asserted.
7. At every binary position, `x XOR y` contains the bits present in exactly
   one input, while `x AND y` contains the bits present in both and must be
   shifted left once. Summing the place values proves (F) for all
   nonnegative integers. If an integer coefficient `mu` replaced `2` in
   (F) for all `x,y`, the single case `x=y=1` would force `mu=2`. This is
   an arithmetic consonance, not a physical carry identification.

As a consequence, not a premise, the signed word recovers the registered
breath identity

```text
(-1)^t_n = (-1)^n (-1)^t_floor(n/2).
```

The proof above, not a finite sweep or architecture count, is the proposed
basis for status T. The frozen verifier is an audit.

## The five frozen fields

```text
EQUATION     Statements (A)-(F), exactly at the scopes above. Novel content
             is their composition into the fixed ramified C4 -> C2 readout
             and carry cocycle, plus the exact carry-weight consonance (F).
             Statement (D) and readout uniqueness remain inherited
             CODEC-TR4 premises, not newly earned claims.
CODE         verify.py, sha256
             31adb8209ddf11237319389c59c533251d01f3278ea9ff33482c58341472d39f
             (6909 bytes). Python standard library only, exact integers,
             deterministic, no file/network/subprocess access, no floats,
             run from repo root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
CARRIER      theorem: n in N_0, k >= 0, F_5^x, and every x0 in Z^4 with
             Tr4(x0)=1 mod 5. Audit: digit/quotient through n=2^20;
             dyadic recursion through n<2^19; carry through n<2^20;
             every nonzero covector and multiplier over F_5; all 125
             residue seeds with Tr4=1 through k=16; inverse-quotient guard
             n<2^18; carry-coefficient search -4<=mu<=8 and 0<=x,y<64;
             recovered breath for 1<=n<=2^20.
SYSTEMATICS  exact proof has no numerical approximation. Audit limitations
             are its frozen finite prefixes and implementation correctness;
             they do not enlarge or establish the all-n scope. The supplied
             incubation files and their prior x86_64 run are source material
             only and are not formal evidence. A defect found in PREREG.md or
             verify.py after the pin invalidates this probe: these files stay
             immutable, execution stops, and a new named issue/probe/pin is
             required. Only result-record corrections may be follow-up commits.
THRESHOLD    KILL the theorem candidate on any exact counterexample at a
             declared n, k, or x0; any gap in proof steps 1-7; any mismatch
             with an inherited premise; or any unreconciled FAIL in gates
             01-10. A formal leg passes only with exit 0, empty stderr, all
             ten PASS lines, the RESULT 10/10 ALL PASS line, and byte-identical
             stdout on the recorded aarch64 and GitHub x86_64 runs.
```

## Dependencies and fences

Frozen theorem premises:

```text
DEF-ODOMETER-ORBIT       definition of the forward N_0 carrier
PENTIT-ROOT-FACTS [T]    the ramified image J_lambda=2
QUBIT-FROM-F5 [T]        F_5^x/{+-1} is the two-class sign quotient
CODEC-TR4 [T]            exact defect identity and unique readout line
```

`TM-BREATH-TOWER [T]` is recovered at its signed recursion, not used as a
premise. `READING-SPLIT [D]`, `ODOMETER-INTERNALIZED [D]`,
`PENTIT-ROOT-READING [D]`, and `TIME-QUANTUM-TOWER [C]` remain unchanged
and are not `REQUIRES` edges.

No checkpoint factorization, decoder totality or uniqueness, parity on all
of `Z_2`, physical carry/phase identification, temporal arrow, run/record
reading, equality with the order-eight foreign carrier, or lift to L2-L6 is
claimed. PR #68 and PR #71 are conceptually adjacent but are not premises
and are not changed by this probe. Any Canon or ledger fold, and the proposed
checkpoint-factorization attack, require separate public work.
