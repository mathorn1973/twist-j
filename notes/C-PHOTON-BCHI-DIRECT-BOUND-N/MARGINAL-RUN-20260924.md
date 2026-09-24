# Partial-current exact audit: result and run record

PUBLIC; NON-CANONICAL; candidate-C finite audit. Working item
C-PHOTON-BCHI-DIRECT-BOUND-N, [#1143](https://github.com/mathorn1973/twist-j/issues/1143).
Author: A. M. Thorn. Date: 24 September 2026. Original code/text: Apache-2.0.

## Pin and custody

The immutable preregistration, audit and written proof were committed at
`81c86e8fb3c959312bbb0ca937528aacf3310539` before the first scientific execution.
All three files were read back through the public connector byte-for-byte
against their local source. A separate download from that exact public pin
was hash-checked before execution on the run host at 2026-09-24T08:58:00.505252+00:00.
The same hashes were checked again after execution.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| MARGINAL-CURRENT-BOUND.md | 8313 | `7ffd2cf7cd4e1b60271a54da184b9e480d9bd00d4734156a139482df086a8023` |
| MARGINAL-PREREG-20260924.md | 4749 | `6171d278e55cc1e80ec634e416cd22d42d30abafcb5553f7de89e9d16e7ba2b7` |
| verify_partial_current.py | 6819 | `5aa6fbd776d8caf8b2fe85cf33b148818518cfc860046752c8e6eb4a5e5be998` |

No scientific execution preceded this pin. Only syntax inspection and
static review preceded it. This was the first audit execution; no repaired
attempt, discarded run or changed threshold exists.

## Execution

- Platform: Debian GNU/Linux 13 (trixie); architecture: x86_64.
- Python: 3.13.5, standard library only.
- UTC start: 2026-09-24T08:58:23.196930+00:00.
- Elapsed seconds: 0.130096; frozen limit: 60 seconds.
- Exit code: 0; timeout: no.
- Stdout: 593 bytes; SHA-256 `6ef6b2c910b817db6675ae388906ed51a49f45a801c2f4175ccd15a30031490c`.
- Stderr: 0 bytes; SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Working directory contains the three unchanged files from the pin.
Exact command:

```sh
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_partial_current.py
```

Exact stdout, UTF-8 with LF line endings and a final newline:

```text
C-PHOTON-BCHI-DIRECT-BOUND-N partial-current audit (NON-CANONICAL)
Mixed Haar/Z5 edge-projector partition for incidence -6..6: PASS
Inherited four-edge polynomial/SOS identities: PASS
Four-cup zero-exterior fixture L=4: faces=21 rank=17 states=53 Q0=596163/524288 Qplus=1/2097152 Pcircle=1/1192327: PASS
Four-cup zero-exterior fixture L=6: faces=21 rank=17 states=53 Q0=596163/524288 Qplus=1/2097152 Pcircle=1/1192327: PASS
Normalized circulation bounds: one=1/9, pair=1/65, signed_pair=1/129: PASS
Abstract two-pattern covariance can remain 1/129 with no distance parameter: PASS
RESULT PASS
```

## Result and limits

**PASS.** The Fourier projector partition and both inherited polynomial
identities passed in exact arithmetic. For each L=4 and L=6 the physical
four-cup fixture has 21 faces, rank 17, kernel dimension 4 and exactly 53
ternary states among all 625 mod-5 kernel elements. All rational weights
and normalization constants agree with the preregistered predictions.

The four-cup enumeration fixes exterior plaquette values to zero and is
only a finite geometry/algebra fixture. It is not a simulation of the full
measure and is not the source of the universal probability bound. The
abstract mass witnesses are likewise not asserted to occur in the model.

The separate [written argument](MARGINAL-CURRENT-BOUND.md) supplies the
candidate-T partial-marginal bound using mixed Haar/Z5 integration. It
sums all unspecified currents and yields normalized circulation-pattern
bounds 1/9 and, for compatible pairs, 1/65 for co-occurrence and 1/129
for absolute covariance. No distance decay or bound on full edge-current
susceptibility is obtained.

No falsifier fired. No floating-point scientific assertion, fit, MCMC,
new physical reading, cross-layer lift or Canon promotion was made.
The same agent authored and checked the work; no independent blind review
is claimed. This is one x86_64 scientific execution, not a formal
two-architecture computational gate. Ordinary repository CI does not
automatically execute this notes audit. P1 and the photon phase remain open.
