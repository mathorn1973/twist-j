# RESULT. P-TM-SYM2-BORN-HALVING-1

**Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNCHANGED.**

```text
decision:                  BORN-HALVING-PASS
local formal executions:   1
local exit/stderr:          0 / empty
local gates:                18/18 PASS
status ceiling:             D
two-architecture gate:      PASS
```

## 1. What is new at this probe scope

The public `TM-SYM2-PROJECTIVE-FOURFOLD [T]` already supplies the uniform
stationary law on the six-word carrier. This probe does not re-claim that law,
the mathematical six-line pushforward `1/6`, or the public common operator as
new evidence.

The fresh target is narrower:

```text
typed J-verb monomial lift
    -> exact two-sheet coefficient Born halving
    -> total map on the orientation-retaining L5 source
    -> coherence across every frozen selector chart.
```

The frozen exact verifier returns positive on that class and the same transcript
is reproduced on clean GitHub x86_64 and aarch64 runners.

## 2. Source and type separation

On

```text
W3={001,010,011,100,101,110},
omega(a,b,c)=c-a,
```

the verifier re-derives

```text
omega(Nw)=-omega(w),
omega(Rw)=-omega(w),
```

and the rational joint `(-1,-1)` function sector has dimension one, with
`omega` nonzero in it.

Two quotients remain distinct throughout:

```text
C_sel  = Sel_class/G,   |C_sel|=4, selector-gauge classes,
Q_word = W3/<N>,        |Q_word|=3, complement word shells.
```

No map from the four selector classes to the three word shells is introduced.
The total L5 type retains the complete four-class record and
`epsilon_read=chi_Q chi_F`, together with the current W3 word and `omega`.

**[candidate-T, frozen finite algebra]** The joint source sector and the type
separation are exact within the declared scope.

## 3. The corrected lift statement

The public `ABELIAN-FACE-DICTIONARY [D]` modulus data do not determine an
amplitude lift. This probe does not claim otherwise.

Instead it freezes the typed monomial class

```text
v_t = delta_t + delta_(t+1),   t in Z/5Z.
```

With the exact five-point Fourier convention,

```text
F(v_t)_k = zeta_5^(t k) (1+zeta_5^k).
```

For `k != 0`,

```text
1+zeta_5^k = sigma_(3k)(J),
```

where `sigma_a(zeta_5)=zeta_5^a`; the `k=0` slot is separately `2`.
All five monomial lifts have the same pointwise spectral moduli and exact
inverse Fourier transform back to the frozen two-term coefficient vectors.

**[candidate-T, frozen finite algebra]** These are exact algebraic statements.
They do not establish uniqueness among all amplitude lifts with the same
moduli.

## 4. Born halving

Every `v_t` has two equal nonzero coefficient amplitudes. Coordinate Born
square on its two-point support is therefore normalized, sheet-order
independent, and identical for every `t`.

Only after the equality proof, the conditional law evaluates to

```text
(1/2,1/2).
```

**[candidate-D physical bridge component]** The mathematical halving is exact;
its physical use is bounded by the public `MEASURE-BORN-VERB [D]` type and by
the fact that `V_J^mono` is a frozen candidate lift rather than a public T
selection theorem.

## 5. Modulus-only overclaim is explicitly broken

The frozen negative control changes only the `k=1` spectral value by complex
conjugation while preserving all five pointwise spectral moduli.

Its exact inverse Fourier vector has full five-point coefficient support and
unequal coefficient Born numerators.

Therefore:

```text
same registered spectral moduli
    !=> equal coefficient Born halving.
```

**[candidate-T bounded negative theorem]** The stronger inference from the
public modulus dictionary alone is false. The positive result belongs only to
the narrower typed monomial lift class.

## 6. S4 import and total bridge

Per the pre-pin S4 ruling, the probe imports only the public L5 stationary W3
law. It then forms its three `N`-orbit marginals and applies the independently
proved two-sheet Born conditional.

The resulting word measure is total and normalized. Only after that
construction and normalization are complete, the common six-line pushforward
weight is read as

```text
1/6.
```

The value is therefore an output of this frozen bridge, not an input selecting
the factors.

**[candidate-D]** The physical bridge interpretation remains at most D; the
uniform W3 law itself is an imported public T input and is not new here.

## 7. Selector coherence

The constructed W3 measure is constant. Hence every bijection from W3 to the
six line labels has the same pushforward. The verifier enumerates all `6!`
bijections only as an audit corollary of that universal fact.

In particular every one of the frozen 48 selector charts agrees. No selector
representative is selected and no semilinear or reversal comparison action is
adopted as a new gauge.

The L5 source remains orientation-retaining. The scalar L6 candidate is
orientation-blind only as the output of the typed total map.

**[candidate-D]** This supplies the required selector coherence for the frozen
candidate bridge without repairing the fired N2 selector canonicality result.

## 8. What is deliberately not a confirmation

This probe does not count the following as independent scientific controls:

- reproduction of the public `M_TM` operator from a uniform six-line measure;
- a numeral-only comparison with `GYRON-DENSITY`;
- the all-720 bijection sweep beyond its role as a finite audit corollary;
- re-derivation of the stationary thirds already public in FOURFOLD.

Those statements carry no additional confirmation weight for the Born-halving
target.

## 9. Exact transcript and pin identity

The accepted verifier printed:

```text
G01 W3-CARRIER PASS
G02 SOURCE-CHARACTER PASS
G03 SOURCE-UNIQUENESS PASS
G04 TYPE-SEPARATION PASS
G05 MONOMIAL-FOURIER PASS
G06 GALOIS-REINDEX PASS
G07 MONOMIAL-MODULUS PASS
G08 FOURIER-INVERSE PASS
G09 BORN-HALVING PASS
G10 SHEET-ORIENTATION PASS
G11 CONTROL-MODULUS PASS
G12 CONTROL-FULL-SUPPORT PASS
G13 CONTROL-UNEQUAL-BORN PASS
G14 S4-WINDOW-IMPORT PASS
G15 TOTAL-WORD-MEASURE PASS
G16 SELECTOR-COHERENCE PASS
G17 ORIENTATION-TOTALITY PASS
G18 CIRCULARITY-STATUS PASS
GATE_COUNT 18
```

The frozen identity is:

```text
pin commit:       0e930978878453800fa078f75b9a0e25c2963787
verifier sha256:  a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
stdout sha256:    52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d
stdout bytes:     741
stdout lines:     30
```

The pinnuté `PREREG.md`, `verify.py`, and `EXPECTED.txt` were not changed after
the scientific run.

## 10. First CI preflight failure, preserved

The first pull-request workflow `31813175546` stopped on both architectures
before any changed-probe verifier replay. The repository RUN parser required
`stdout_lines` and the exact field name `verifier_sha256`; the initial RUN
record omitted the former and used `verify_sha256` for the latter.

This was an evidence-metadata schema failure. The correction changed only
`RUN.md`, recorded the failure, and did not alter the pin, verifier,
`EXPECTED.txt`, thresholds, route, scientific output, or local execution count.
It carries no scientific negative verdict.

## 11. Two-architecture gate

The corrected evidence head
`b7d86f655921aceabee140e44d4e93d5f7c678fb` was tested by clean pull-request
workflow `31813296463` at tested merge
`55858de4921c9edd9b530e07a29db383a136f5c1`.

```text
x86_64 job       94808833870   success
platform         Ubuntu 24.04.4 LTS
python           CPython 3.12.13
VERIFY PASS      verifier a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
                 stdout   52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d

aarch64 job      94808834014   success
platform         Ubuntu 24.04.4 LTS
python           CPython 3.12.13
VERIFY PASS      verifier a9dbe6d5549aa3e0bb5f21cc4d8e26586cbcf95141df141432b710e8fdb0f6f7
                 stdout   52ee81ddd10c7af5e00ff1a2a1b6ea2fed9905b1f235349b73c0732fb2ead51d

aggregate check  94808891578   success
terminal         TWO-ARCHITECTURE CHECK PASS
```

Both architecture jobs also passed policy, all 99 repository unit tests,
Canon and ledger checks. The x86_64 and aarch64 clean replays therefore satisfy
the public two-architecture computation gate for the pinned verifier.

## 12. Scientific disposition

**[candidate-D]** The frozen monomial J-verb class supplies exact Born halving
and a total selector-coherent L5-to-L6 candidate map without assuming the
target `1/6`.

**[candidate-T bounded negative]** The registered spectral moduli alone do not
force that halving; a same-modulus nonmonomial lift breaks it.

This probe does **not** by itself change or close
`TM-SYM2-PHYSICAL-MEASURE [O]`. Public status, dependency, gate, Canon and
Frontier treatment remain a separate reviewed fold. No `D_matter`, SI, new
gauge, or decoder-completion claim is made.
