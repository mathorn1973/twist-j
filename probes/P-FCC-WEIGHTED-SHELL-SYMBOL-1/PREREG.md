# P-FCC-WEIGHTED-SHELL-SYMBOL-1

Status: `PREREGISTERED / UNRUN` at this file state.

```text
public claim issue:  #691
successor program:   PHOTON-CONE-CONVERGENCE (non-canonical until fold)
target claim:        FCC-WEIGHTED-SHELL-SYMBOL
branch:              probe/P-FCC-WEIGHTED-SHELL-SYMBOL-1
path:                probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1/
owner:               A. M. Thorn / current Codex owner session
action layer:        L2 only
proposed status:     T by the finite proof below; verifier is an audit
```

This probe creates no Canon, Registry, Frontier, dependency, gate, program,
or status change. A later sealed fold alone may consume its result.

## 1. Authority and lineage

The claim was opened against this verified authority:

```text
STATE:          ACTIVE
CANON:          Public Canon v71
TAG:            canon-v71
main:           7f4c102e27e7b2ebdf5ca9215db5c5ab846ebbe2
CONTENT_COMMIT: a77d720433c19976f9ab663d023ec9364eac34eb
CANON_SHA256:   0306abb2e7f855ceb4fcbfdf14265a9d2c5c8bd23b35868b74a92aae16b5e279
CANON_BYTES:    369836
policy run:     33313400934 PASS
```

`P-A3-FCC-POINT-GROUP-1` is an `ABANDONED` public identifier. This probe does
not resume, repair, rename, or reuse it. The divergent public notes refs
`notes/c-photon-point-group-1` and `notes/census-v2-and-photon-lane` remain
preserved. Their old text named `P-FCC-TRANSFER-SYMBOL-1` and was explicitly
`UNFROZEN, NOT FOR PIN`; that identity and its bytes are not used here.

## 2. Equation and exact claim

Use one ambient carrier, `Z^3`. For

```text
N = {2,4,8,10,16},
S_n = {v in Z^3 : v_1^2+v_2^2+v_3^2=n},
W* = (w2,w4,w8,w10,w16) = (6,1,15,1,1),
S(k) = sum_(n in N) w_n sum_(v in S_n) (cos(<k,v>)-1),
```

freeze the coefficient convention

```text
M_d(k) = sum_n w_n sum_(v in S_n) <k,v>^d.
```

The target block is

```text
T1  (|S_2|,|S_4|,|S_8|,|S_10|,|S_16|) = (12,6,12,24,6).

T2  W* is the unique positive integral solution of minimum total weight to
    -4w2 + 32w4 - 64w8 + 440w10 + 512w16 = 0.

T3  M_2 = 648 (k_x^2+k_y^2+k_z^2).

T4  M_4 = 3168 (k_x^2+k_y^2+k_z^2)^2.

T5  M_6 = 21888 sum_i k_i^6
          + 63360 sum_(i != j) k_i^4 k_j^2
          + 0 k_x^2 k_y^2 k_z^2,
    where the sum over i != j uses ordered pairs.

T6  the weighted multiset is invariant under all 48 signed coordinate
    permutations, and M_6 is not proportional to |k|^6.
```

Consequently the formal Taylor coefficients through fourth order are

```text
S(k) = -324 |k|^2 + 132 |k|^4 + terms of degree at least six,
```

while the exact sixth-order term is anisotropic. No global continuum or
remainder-bound claim is included.

## 3. Written finite proof

Every shell is the signed-permutation orbit of the displayed representative:

```text
S_2:  (1,1,0),  size 12
S_4:  (2,0,0),  size 6
S_8:  (2,2,0),  size 12
S_10: (3,1,0),  size 24
S_16: (4,0,0),  size 6.
```

All coordinates lie in `[-4,4]`: a coordinate of absolute value at least 5
would already have squared norm at least 25. The complete sorted nonnegative
square partitions of the five norms are

```text
2  = 1+1+0,
4  = 4+0+0,
8  = 4+4+0,
10 = 9+1+0,
16 = 16+0+0.
```

Each partition has exactly the displayed representative. Its distinct signed
permutations therefore enumerate the whole shell, prove T1, and prove the
group invariance in T6.

Divide the weight equation by four and put

```text
a=w4, b=w8, c=w10, d=w16,
w2 = 8a - 16b + 110c + 128d.
```

The displayed `W*` is positive, has total 24, and satisfies the equation. To
classify every positive solution with total at most 24, use
`b <= 23-a-c-d`, which follows from `w2>=1`. Hence

```text
w2 >= 24a + 126c + 144d - 368.
```

If `c+d>=3`, the right side is at least 52, impossible at total at most 24.
Thus `c=d=1`. The total and positivity conditions become

```text
b >= ceil((216+9a)/15),
b <= floor((8a+237)/16),
b <= 21-a.
```

The first and third inequalities imply `a<=4`. Direct substitution of
`a=1,2,3,4` leaves only `a=1,b=15`, giving `w2=6`. This proves T2 without
using the verifier.

For T3--T5, expand each finite orbit with

```text
(v_x k_x+v_y k_y+v_z k_z)^d
 = sum_(i+j+l=d) d!/(i!j!l!) v_x^i v_y^j v_z^l k_x^i k_y^j k_z^l.
```

Sign closure cancels every odd exponent. By coordinate symmetry it is enough
to display one fixed coordinate and one fixed ordered coordinate pair. Direct
substitution in the five complete orbits gives

```text
n    |S_n|  sum x^2  sum x^4  sum x^2y^2  sum x^6  sum x^4y^2
2      12       8        8          4          8          4
4       6       8       32          0        128          0
8      12      32      128         64        512        256
10     24      80      656         72       5840        360
16      6      32      512          0       8192          0
```

After multiplication by `W*`, the corresponding totals are

```text
sum w x^2       = 648,
sum w x^4       = 3168,
sum w x^2 y^2   = 1056,
sum w x^6       = 21888,
sum w x^4 y^2   = 4224,
sum w x^2 y^2 z^2 = 0.
```

The multinomial factors for `x^2y^2` and `x^4y^2` are respectively 6 and
15, giving `6336` and `63360`; every shell vector has a zero coordinate, so
the triple-square coefficient vanishes. This yields T3--T5 as written.
`verify.py` independently constructs every vector and every multinomial
coefficient rather than importing this table. If M6 were `21888 |k|^6`, its
`k_i^4 k_j^2` coefficient would be `3*21888=65664` and its triple-square
coefficient would be `6*21888=131328`, not `63360` and `0`. Thus T6 follows.

## 4. Accepted code

```text
file:    probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1/verify.py
bytes:   9978
sha256:  7a853f0940a0c2794e40530270aebfe988a3b3596afb62d46db1bcd6413a1673
```

The accepted verifier uses only the Python standard library and exact integer
arithmetic. It has no arguments, floating point, randomness, network,
subprocess, clock, input file, environment-dependent ordering, or write. It
buffers successful ASCII stdout. A gate failure emits no stdout, one sanitized
`STOP` line on stderr, and exits 1; an argument exits 2 with the fixed usage
line.

Before the immutable pin, syntax compilation and static review alone are
permitted. The formal command after pin and public readback is

```text
python3 probes/P-FCC-WEIGHTED-SHELL-SYMBOL-1/verify.py
```

from the repository root under

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
```

## 5. Carrier, systematics, and exposed preparation

There is no external data. The complete carrier is the five displayed norm
shells in `Z^3`, and the only weight input is displayed `W*`.

The verifier freezes these audit gates:

```text
G01 shell sizes;
G02 FCC even-coordinate-sum membership;
G03 group order and one-orbit shell descriptions;
G04 weight admissibility;
G05 unique minimum by complete bounded enumeration and independent elimination;
G06--G08 exact M2, M4, M6 coefficient dictionaries;
G09 exact sixth-order nonisotropy;
G10 weighted mass 288 and 48-group invariance;
G11 Taylor coefficients;
S01 norm-nine split-orbit control (6,24);
S02 uniform-weight cone value 916 and w2 mutation 648 to 656;
S03 dropped-vector symmetry breaker;
S04 fresh-state transcript determinism.
```

Before this pin, public notes exposed `W*`, the shell family, the moment
values, flat flux, and the expected sixth-order anisotropy. The present
verifier was authored against those exposed values. They are preparation, not
evidence. Flat flux is not consumed by this scalar moment probe.

## 6. Outcomes, falsifier, and layer firewall

```text
SYMBOL-PROVED
  the finite proof is complete and every audit, execution, transcript,
  security, and architecture gate passes;

SYMBOL-REFUTED
  an independently checked exact shell, weight-minimality, coefficient, or
  group-action counterexample refutes the frozen identity block;

STOP
  authority, collision, typing, proof completeness, code, pin, integrity,
  transcript, security, or architecture requirements fail.
```

A failing runtime audit is `STOP` until independently diagnosed; it is not by
itself a scientific refutation. No threshold or tolerance exists.

Action layer is `L2` only: a displayed spatial carrier and its scalar symbol.
No L1 state derivation, L3 boundary, L4 support chain, L5 clock/stream, or L6
measure is consumed or produced, so this probe owns no cross-layer gate.

The result does not select the FCC carrier, `W*`, its scale, or flat flux from
`J`, the architecture, `U`, or a decoder. It supplies no temporal
characteristic, Herm2 identification, global or tangent null cone, Lorentz
claim, Gibbs state, roughening, phase, propagator, polarization, apparatus,
continuum, or physical photon.

## 7. Immutable sequence

1. Commit and push exactly `PREREG.md` and `verify.py`; never amend, rebase,
   squash, or force-push the pinned history.
2. Record pin commit, parent, hashes, bytes, blobs, and remote byte readback in
   issue #691.
3. Only then execute the accepted command once in a clean Linux-compatible
   checkout at the pin.
4. On exit 0 and empty stderr, add exact `EXPECTED.txt`, neutral `RUN.md`, and
   `RESULT.md` without changing either pinned file.
5. Push the additive result commit and open one PR changing this directory
   only. Require byte-identical x86_64 and aarch64 jobs before review and
   merge without squash or rebase.

No execution is authorized at this file state before the remote pin readback.
