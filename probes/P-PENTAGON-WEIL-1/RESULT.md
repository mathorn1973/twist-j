# P-PENTAGON-WEIL-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE REPRODUCIBILITY GATE PASS; PUBLIC CLAIM UNREGISTERED

## Scientific decision

```text
G01 ROOT-FILTER                         PASS
G02 CYCLOTOMIC VALUE-AT-ONE CERTIFICATE PASS
G03 EXACT FINITE CUTOFF                 PASS
G04 RAW STANDARD-SYMMETRY FALSIFIER     PASS
G05 NATURAL-SERIES ACCOUNTING           PASS
G06 SIGNED LOG-DERIVATIVE CORRECTION    PASS
RESULT                                  6/6 ALL PASS
```

### Post-run evidence-map correction

No frozen artifact is changed by this correction. In `verify.py` and
`EXPECTED.txt`, the printed `G01` through `G06` prefixes are immutable
historical machine-row labels. For scientific evidence mapping, read them
as `V01` through `V06`:

```text
V01 -> PREREG G01  finite root-filter certificate
V02 -> PREREG G02  cyclotomic/value-at-one certificate
V03 -> PREREG G03  exact finite cutoff
V04 -> PREREG G04  raw standard-symmetry falsifier
V05 -> PREREG G02  natural-series subclaim at s=1
V06 -> PREREG G05  signed logarithmic-derivative correction
```

`PREREG G06` (RH equivalence in the open critical strip) is proof-only. It
is established by the inline divisor argument, not by a verifier row, and
is not part of the `6/6` machine count. Thus `6/6` means all six exact
computational assertions passed; it does not mean one machine assertion
exists for every preregistered scientific gate.

The first formal execution reproduces every frozen finite exact check.  In
particular, it confirms the residue filter `c(n)=5[5|n]-1`, the cyclotomic
product `prod_(a=1)^4(1-j^a)=5`, the correct finite cutoff through every
`N=1..625` for `s=2,3,4`, the ratio `f_5(2)/f_5(-1)=-1/30`, the exact
harmonic block identity through `M=125`, and the sign accounting that removes
the artificial `5^m log 5` tower.

Together with the inline derivations in `PREREG.md`, this supports the frozen
G0 candidate normalization

```text
P_0(s) = (5^(1-s)-1) zeta(s)                 on Re(s)>1,
Z_J(s) = MerCont P_0(s)/(5^(1-s)-1) = zeta(s),
xi_J(s) = xi(s).
```

The analytic continuation, zeta functional equation, Euler product, and
standard completion remain explicitly imported classical theorems.  The
verifier audits exact finite algebra and sign accounting; it does not prove
those imports computationally.

## Scope and non-conclusions

- The raw carrier `P_0` is not used as an uncorrected Weil-form carrier.
- G04 excludes only the standard constant unit-root-number symmetry of the
  raw completion.  The stated variable-factor identity remains valid.
- The RH statement for zeros of `P_0` in the open critical strip is an exact
  equivalence only.  Neither side is proved here.
- No Weil test space, involution, quadratic form, positive realization,
  Hilbert space, or self-adjoint operator is defined by this probe.
- `J-WEIL-POSITIVE-REALIZATION` and RH remain open.
- No claim has been added to the public registry or Canon.  Any promotion or
  Canon fold is a separate sealed public step.

The name `P-PENTAGON-WEIL-1` identifies the route.  This first probe acts only
at the L5 analytic/root-filter layer and performs no L5-to-L6 lift.

## Formal evidence

```text
initial base:          6bb013bafb2d1c06fcb295fdbfce0f86198fd685
public lock:           issue 41
preregistration pin:   6be1231a4366dbcc04f7251afe7adb44df555250
PREREG.md SHA-256:     f7e3b3ea14be504e73a26f49c29b7b87bc67655f6ccd215d6de3eadc5bd12774
verify.py SHA-256:     5655888c9c8eac7fe49b2734235d9a65d318fac8b57b7d2a90b67a1f450f614c
formal run commit:     5a2771232335a173318ecb3d7b37a5e62d4111dd
EXPECTED.txt SHA-256:  f042368571e4f3d302a6cfbe47c6d344bcdf8411d9dd4dca3a21aa9f216797fe
RUN.md SHA-256:        ee2aa4612b7e9073c910468ff604e1c38724a3a1bea37f2a01a8dfef114e9ad1

platform:              Ubuntu 24.04.4 LTS
architecture:          aarch64
Python:                3.12.3
exit code:             0
stderr:                0 bytes
stdout SHA-256:        f042368571e4f3d302a6cfbe47c6d344bcdf8411d9dd4dca3a21aa9f216797fe
stdout bytes:          711
stdout lines:          12
```

`EXPECTED.txt` is the exact first formal stdout.

Two-architecture record:

```text
aarch64 leg    Ubuntu 24.04.4 LTS, CPython 3.12.3, neutral environment;
               first formal execution recorded in RUN.md; verifier
               5655888c...f614c; stdout f0423685...797fe, 711 bytes.
x86_64 leg     GitHub check on pull request 42, evidence head
               8a889586e571a8e6e811559f6bd5c2d8f9875db3; run
               29451572197, job 87475031267, conclusion success;
               Ubuntu 24.04.4 runner, CPython 3.12.13; verifier and stdout
               byte-identical to the aarch64 leg.
gate:          PASS.  The aarch64 and GitHub x86_64 verifier outputs are
               byte-identical.
```

This gate establishes reproducibility of the exact audit.  It does not
register a public claim, prove RH, or provide Weil positivity.
