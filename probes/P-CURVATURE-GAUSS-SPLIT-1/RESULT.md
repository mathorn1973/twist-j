# P-CURVATURE-GAUSS-SPLIT-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision

```text
TRACE ambient=-881/8 internal=-881/8 exterior=0 cross=0
RANK ambient=292 nullity=526
RANK internal=292 nullity=526
RANK exterior=0 nullity=818
LEAKAGE A=NONZERO C=NONZERO
DECISION INTRINSIC
RESULT VALID
```

At the frozen historical curvature operator the exterior commutator term is
the exact zero matrix, so the Gauss split identity `K_amb = K_int + K_ext`
collapses to `K_amb = K_int` on `V`: the ambient compression of the
commutator equals the purely intrinsic commutator of the compressed
generators. All fifteen preregistered integrity gates pass
(`AUDIT PASS 15/15`), both independent routes agree entrywise on all three
matrices before any observable is printed, and the public anchor identity

```text
Tr_V(K_amb^2) = Tr_V(K_int^2) + cross + Tr_V(K_ext^2) = -881/8
```

is reconstructed exactly with internal trace `-881/8`, exterior `0`, and
cross `0`.

The preregistered leakage diagnostics decide the mechanism: both leakage
maps `L_A = QAP` and `L_C = QCP` are nonzero, yet
`K_ext = L_A* L_C - L_C* L_A` vanishes exactly. The equality
`K_amb = K_int` therefore comes from exact cancellation of nonzero leakage
contributions, not from invariance of `V` under `A` and `C`. This is the
discrete Theorema Egregium statement for this operator, in exactly the
algebraic sense frozen by the ruling: the historical compression reproduces
the internal commutator with no net embedding contribution.

`DECISION INTRINSIC` is one of the three preregistered first-class outcomes.
No falsifier fired and no integrity gate stopped the run.

## Scope and non-conclusions

This result concerns exactly

```text
X = F_5^6,
H = <b,d>,
V = F^H intersect 1_X^perp  (dim V = 818),
K_amb = P[A,C]P |_V,
K_int = [PAP, PCP] |_V,
K_ext = (PAQCP - PCQAP) |_V,
```

with the counting inner product, the frozen orbit basis `(B)`, and Gram
skew-adjointness, as incorporated from the merged ruling. In particular:

- the labels `amb`, `int`, `ext` describe the exact algebraic split only;
  no differential-geometric Gauss equation, second fundamental form, or
  physical embedding theorem is asserted;
- `INTRINSIC` does not mean `A` and `C` preserve `V`; the printed leakage
  diagnostics show they do not;
- no canonical curvature operator is selected, no spectrum is asserted, no
  continuum or boundary lift is claimed, and no sign is read physically;
- `CURVATURE-OPERATOR-CANONICAL` remains `[O]`.

A reproduced outcome may later support a separately named claim such as
`CURVATURE-HISTORICAL-GAUSS-SPLIT` at exactly this carrier, measure, group,
and operator scope. Folding it into the registry, frontier, or Canon is a
separate sealed public step. This probe changes only
`probes/P-CURVATURE-GAUSS-SPLIT-1/`.

## Formal evidence

```text
ruling merge:          57de0af8a50e14e52f0fa81e0158f6a370cab5a5
ruling file SHA-256:   94ae6278c5ec27262d7eeb443e1a8461a84c2f59df6f315fb5fda24f63bcb02e
preregistration pin:   03582ff94368353d339002769b7fff45e37b36de
PREREG.md SHA-256:     c05cfd8ef591f6dd8b340f2cb1e1f91f85631eb4cf8b4632587fc8d73623cc78
verify.py SHA-256:     4080da59872a923b0ce4204a93184e17307f6923243d97f0f3105c771c48b8bd
formal run commit:     b971f14806b366c22f46883253cfe3b994dcb15a
public lock:           issue 22

platform:              Ubuntu 24.04.4 LTS
architecture:          aarch64
Python:                3.12.3
exit code:             0
stderr:                0 bytes
stdout SHA-256:        3f10bf3acf930755c80af943e5bc9b4db1b12b6c00715c1bb4dd0157e8296189
stdout bytes:          1445
stdout lines:          21
RUN.md SHA-256:        9a8cfbd344188a63ea5c8835df891360a4728da3a034bbcdff4d24313f865f66
```

`EXPECTED.txt` is the exact formal stdout. `RUN.md` contains only neutral
public environment fields. Two independent executions on the formal aarch64
host were byte-identical, and `tools/check_verifier.py` reproduced
`EXPECTED.txt` byte for byte from the pin.

An additional independent witness run on a separate Ubuntu x86_64 host
(CPython 3.11.15, neutral environment, exit 0, empty stderr) reproduced
`EXPECTED.txt` byte for byte with the same stdout SHA-256. This witness is
informative only.

Two-architecture record:

```text
aarch64 leg    Ubuntu 24.04.4 LTS, CPython 3.12.3, neutral environment;
               first formal execution; RUN.md in this directory.
x86_64 leg     GitHub check on pull request 39, head
               c523042b18353f235428a9734c8291c99173c41b;
               run 29402674399, job 87310702784, conclusion success;
               Ubuntu 24.04 runner, CPython 3.12.13; verifier
               byte-identical (4080da59...), stdout byte-identical
               (3f10bf3a..., 1445 bytes); log carries
               VERIFY PASS P-CURVATURE-GAUSS-SPLIT-1.
gate:          PASS. The aarch64 and GitHub x86_64 outputs are byte-identical.
```
