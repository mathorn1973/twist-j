# P-WALL-EXCESS-5-1 preregistration

```text
PROBE       P-WALL-EXCESS-5-1
LANE        section 16, p = 5 and the wall
LAYER       L1 (state algebra). No lift.
BASE        Public Canon v23, tag canon-v23, content commit 7830d852,
            CANON_SHA256 f842b613, CANON_BYTES 116017, SHA256SUMS 5 of 5 OK.
VERIFIER    verify.py in this directory,
            sha256 f08fc9bb00f64c538601fc70f6b0ced6eb5c40c1c0830088bffdfb30542e1a86
ENV         LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
            Python standard library only, exact rational arithmetic, no float
            anywhere, run from repository root.
BUDGET      under 120 seconds. Local measurement in the originating lane:
            15 seconds.
OWNER       one owner; claim the public issue before executing.
```

## 0. Disclosure

Confirmatory, same as its sibling probe: derived first in the project
incubation lane on 2026-07-26 (memo
`RG-STRUKTURA-NOSIC-A-DVA-NOGO_2026-07-26.md`, break round BR-2 to BR-5),
frozen here before the public verifier executes. The verifier in this
directory is fresh code.

## 1. The question

`WALL-CIRCLE-LEMMA [T]` proves the closed form for every `N >= 3`, so every
p = 5 wall readout is now computable as a rational function of `N`. That
makes a question decidable that was previously only assertable: which of the
registered p = 5 readouts actually distinguish `p = 5`, and which are
generic in `N` and therefore carry no selection content at all.

This matters because the canon section is titled "p = 5 and the wall". An
earlier lane note already found that the rung itself is p-generic. The
present probe asks the sharper question and finds that one readout, the
excess of the orbital sum above one, is uniquely p = 5, while another
tempting pattern is not.

## 2. The frozen statement

```text
S1  Normalizing by zeta(2), the full nontrivial-root sum is
    sum_(a=1)^(N-1) w(N,a) = (N-1)(N-2)/(2N), with
    w(N,a) = 3 (N - 2a)^2 / (2 N^2).
S2  Its excess above 1 is (N^2 - 5N + 2)/(2N). This excess equals 1/N if and
    only if N(N - 5) = 0, hence for exactly one integer N >= 3, namely
    N = 5. The registered value 1/5 = 1/p is therefore specific to p = 5.
S3  The channel ratio w(N,1)/w(N,2) = (N-2)^2/(N-4)^2 equals 9 for exactly
    one integer N >= 3, namely N = 5.
S4  NEGATIVE, registers nothing: the per-pair difference is 12(N-3)/N^2 and
    its deficit below 1 is (N-6)^2/N^2, which equals 1/N^2 for N in {5, 7}.
    The 24/25 and 1/25 pattern is therefore NOT specific to p = 5 and is
    inadmissible as evidence or as a bridge to any one-bit structure.
```

## 3. Gates, frozen before execution

```text
G01 P5-VALUES         closed form reproduces the registered p = 5 readouts
G02 ORBIT-SUM         the (N-1)(N-2)/(2N) identity, N = 3..2000
G03 EXCESS-SELECTS-5  the excess equals 1/N for exactly one N, namely 5,
                      with the algebraic equivalence to N(N-5) = 0 checked
                      as an identity rather than asserted
G04 RATIO-SELECTS-5   the ratio 9 occurs for exactly one N, namely 5
G05 DEFICIT-GENERIC   scope guard: the deficit hits 1/N^2 at N = 5 and 7
```

## 4. Failure threshold and falsifier

```text
FIRE if the closed form fails to reproduce any registered p = 5 readout.
FIRE if any N in 3..2000 violates the orbital-sum identity.
FIRE if the excess equals 1/N for any N other than 5 in the tested range,
     or if the algebraic equivalence to N(N-5) = 0 fails at any N.
FIRE if the channel ratio 9 occurs at any N other than 5 in the range.
FIRE if the deficit set is anything other than {5, 7} in the range.
FIRE if the aarch64 and x86_64 transcripts differ in any byte.
```

Note the asymmetry deliberately built in: G05 is designed to fail the
program's own temptation, and it passes by confirming that the tempting
pattern is generic. If a later session rediscovers 24/25 and 1/25 and
proposes it as evidence, this gate is the standing refutation.

## 5. Systematics

```text
The range 3..2000 is finite. S2 and S3 are proved algebraically inside the
  gates (as identities over the whole range) and not merely observed, so
  the finite range is a calibration of a proof, not the proof itself.
No polylogarithm is evaluated. Every value is an exact Fraction derived
  from the WALL-CIRCLE-LEMMA closed form, which is already [T].
N = 4 is excluded from the ratio gate only because w(4,2) = 0 makes the
  ratio undefined there; the exclusion is explicit in the gate.
```

## 6. Scope: what this probe does NOT claim

```text
It does not claim the wall selects p = 5. One readout being unique to 5 is
  not a selection argument; the selection rests on P5-ROOT-SELECTION and
  its named witnesses, untouched here.
It makes no imaginary-part claim, no field-trace claim, no substrate,
  normalization, regularization or physical claim.
It does not modify WALL-CIRCLE-LEMMA or WALL-LI2-RUNG. It reads them.
It has no dependency on the renormalization lane; the sibling probe uses
  the same closed form as an input but the two results are independent.
```
