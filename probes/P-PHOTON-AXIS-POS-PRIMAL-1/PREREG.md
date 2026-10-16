# P-PHOTON-AXIS-POS-PRIMAL-1 preregistration

Status: FORMAL PREREGISTRATION / UNEXECUTED / FINITE-SIZE CEILING C

Owner: A. M. Thorn
Public reservation: [issue #1116](https://github.com/mathorn1973/twist-j/issues/1116)
Implementation claim and pre-data resource qualification: #1116 comment 6213831921
Branch: `probe/P-PHOTON-AXIS-POS-PRIMAL-1`
Directory: `probes/P-PHOTON-AXIS-POS-PRIMAL-1/`
Date: 2026-10-16

This document freezes the prospective primal-only finite-size test of the
exact axis coefficient reserved in #1116. It is a new identifier. It does not
reopen, amend, replace, rescue or reinterpret #757, #756 or #742, and no
historical #757 output is an input.

No production chain may run until this preregistration, all accepted source,
`FIXTURE_EXPECTED.txt`, `AXIS_PIN.md` and `SHA256SUMS` are committed, pushed
and publicly read back byte for byte at one immutable pin. Compilation, static
checks, the pilot-2 fixtures, the `L=3,4,6` AXIS fixtures and blind plumbing
runs at sizes outside the production set are development checks, not data.

## 0. Authority and scope lock

```text
STATE:                 ACTIVE
CANON:                 Public Canon v101
PUBLIC MAIN AT CLAIM:  89d3c850a673b5941ffd9831058c6ee9c345710b
TAG:                   canon-v101
CONTENT_COMMIT:        421a4ec1daf07c04d19022c1ee219607e83c09a8
CANON_SHA256:          b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7
CANON_BYTES:           992352
```

`canon/SHA256SUMS` verified 5 of 5 at that commit; the tag and the content
commit are ancestors of it.

The probe measures one finite-size quantity and may return at most
prospectively measured finite-size C-grade evidence about AXIS-POS. It cannot
prove the thermodynamic theorem, O(4) restoration, a shell atom, a physical
photon, `PHOTON-MASSLESS-PHASE`, or close #744. It moves no Canon row.

## Field 1: equation

### 1.1 Measure and transition

The measure is the fixed `W` measure on `K_L = (Z/LZ)^4` at `t = 1`:
link variables `A in C^1(K_L; Z_5)`, plaquette flux `f = dA`, weight
`prod_p W(f_p)` with `W(f) = 2 + 2 cos(2 pi f/5) = |1 + zeta_5^f|^2`, all
topological sectors, no gauge quotient.

One macrocycle is exactly the accepted pilot-2 macrocycle (#755, #757 section
3): one exact single-link heat-bath sweep over all `4L^4` links, one exact
noncontractible-line heat-bath sweep over all `4L^3` lines, one exact-uniform
flat holonomy sheet in each direction and one exact-fair charge conjugation.
Even macrocycles run forward, odd ones in reverse order. All categorical
decisions are exact `Z[phi]` prefix comparisons with the inherited 256-bit
cap; exhaustion is `STOP_INTEGRITY`.

### 1.2 Estimator

Orientations are ordered `(01, 02, 03, 23, 31, 12)` with `F_31 = -F_13`. For
`r in {0,1,2,3}`, `q_r = (2 pi/L) e_r`; `E_r` is the set of the three
orientations containing `r` and `B_r` the other three. With the frozen score

```text
G = (0, 1, 2+sqrt5, -(2+sqrt5), -1),     kappa^2 = 5 - 2 sqrt5,
```

the centred plaquette transform is
`G~_I(q_r) = L^-2 sum_x exp(-i q_r . c_{x,I}) G(f_I(x))`,
`c_{x,I} = x + (e_a + e_b)/2`, and

```text
D_r(A) = (kappa^2/3) [ sum_{I in E_r} |G~_I(q_r)|^2 - sum_{I in B_r} |G~_I(q_r)|^2 ],
D_L(A) = (1/4) sum_r D_r(A).
```

By #1107 and exact hypercubic symmetry `E[D_L] = Delta_L(q_L)`. No axis,
orientation, sign convention, momentum or linear combination is selected
after data.

### 1.3 Exact reduction

`G` lies in `Z[phi]`: `2 + sqrt5 = 1 + 2 phi`. For each orientation `I` and
axis `r` the engine prints the exact slice sums

```text
S_{I,r}(t) = sum_{x : x_r = t} G(f_I(x))  in Z[phi],   t = 0..L-1,
```

as integer pairs `(u, v)` meaning `u + v phi`. The centre shift contributes
only the global phase `exp(-i pi [r in I]/L)`, so

```text
L^4 |G~_I(q_r)|^2 = sum_{k=0}^{L-1} cos(2 pi k/L) R_{I,r}(k),
R_{I,r}(k) = sum_t S_{I,r}(t) S_{I,r}(t+k)  in Z[phi],   R(k) = R(L-k).
```

The committed record carries, per sample, the exact integer contrast
`Q_r(k) = sum_{I in E_r} R_{I,r}(k) - sum_{I in B_r} R_{I,r}(k)` for
`k = 0..L/2`, and per chain the exact totals of every `R_{I,r}(k)`. Then

```text
D_r = kappa^2/(3 L^4) sum_{k=0}^{L/2} m_k cos(2 pi k/L) Q_r(k),
m_k = 1 for k = 0 or 2k = L, m_k = 2 otherwise.
```

All coefficients are below `8 L^7` in absolute value. The floating readout is
fixed: `cos(2 pi k/L)` from closed forms using only `sqrt` (correctly rounded
on every IEEE host), `math.fsum` over `k` separately for the `1` and `phi`
coordinates, `phi = (1 + sqrt5)/2`. `verify.py` proves the reduction exactly
in `Q(phi)[x]/Phi_2L(x)` against the direct centred transform on the frozen
`L = 3, 4, 6` fixture fields.

### 1.4 Secondary quantities (no terminal authority)

```text
X_p = tan(pi f_p/5) = kappa G_p,   X_p^2 = 5 - 2 sqrt5 (f = 1, 4), 5 + 2 sqrt5 (f = 2, 3),
a(A) = (1 + mean_p X_p^2)/2   from the exact flux counts,
R_L(A) = 3 (a(A) - D_L(A)),
P_{I,r} = E |G~_I(q_r)|^2     from the exact per-chain totals of R_{I,r}(k).
```

## Field 2: code

The accepted implementation is the ordered nine-file inventory of
`SHA256SUMS`:

```text
PREREG.md             this document
AXIS_PIN.md           the pin declaration
README.md             commands and file roles
axis_engine.cpp       engine; includes the pilot-2 photon_z5.cpp byte for byte
axis_core.py          exact reduction, records, gates, jackknife, fits, terminal
axis_reader.py        independent numpy reader of the saved link states
run_axis.py           one-shot supervisor
verify.py             formal verifier (standard library)
FIXTURE_EXPECTED.txt  engine output of --axis-fixture 3, 4 and 6
```

`axis_engine.cpp` defines `main` as `pilot2_engine_main`, includes
`../P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/photon_z5.cpp`, and adds only
the `--axis` and `--axis-fixture` modes. Every pilot-2 mode stays reachable and
must reproduce `SELFTEST_EXPECTED.txt`, the modeled-stop fixture and
`REFERENCE_EXPECTED.txt` before production. The macrocycle, the Philox4x32-10
counter source keyed by `(seed, kind, macrocycle, ordinal, block)`, the
namespaces and the update order are the accepted pilot-2 ones. Immutable
dependencies, by SHA-256:

```text
68232b2f44bca6fd71514547e2f5aa0ad8aa85b9d298dde5d9a4109ac2151e14  photon_z5.cpp
263b631d6322526296cef5b32104f9bbc34184a8506f30fc15962687fcd6727a  photon_z5_part1.inc
7d1183e0f8368310be259fb88fac54aaba9e8661c64112e2577e9929e8ea379d  photon_z5_part2.inc
c6f5776e5c401618bd8478cf98bf99ad9020f50b0dc4495e53e2eea4a971686a  photon_z5_part3.inc
442f79534fc7849fa4801d46908c24abf2d22e0b31a5fdec2e4b068bfd66db4b  photon_z5_part4.inc
d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce  analyze_pilot.py
621f95193d744e3b33d1c469e45d83d84d7b44f8cc571ca7695457f08e9a43da  SELFTEST_EXPECTED.txt
6c86ca3be9c94b0581fe9af2fde41352db0b7f20c48d6b7e066bcebe1476d7be  REFERENCE_EXPECTED.txt
1f11fc6fb2ffe9378a0f0ebc8f2fd9223fb958b4a40bb9381c67a8857d947ca3  libboost1.83-dev_1.83.0-4.2_amd64.deb
```

The Boost package is the public Debian `libboost1.83-dev 1.83.0-4.2` for
amd64. The supervisor checks its hash, extracts it with `dpkg-deb -x` into a
temporary build directory and compiles

```text
g++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic -isystem <extracted>/usr/include axis_engine.cpp
```

with empty compiler output required.

Formal host, neutral fields: Debian GNU/Linux 13, x86_64, 2 sockets, 40 cores,
80 logical CPUs, CPython 3.13.5, g++ 14.2.0, numpy 2.5.0 for the reader only.

The pilot-2 statistics (Geyer initial monotone sequence, split and rank
normalization, ties, quantiles, pooled ESS, conservative hot/cold standard
error) are imported from the immutable pilot-2 analyzer. Its Geyer and pooled
ESS loops evaluate every lag before truncating; `axis_core.py` evaluates the
same expressions in the same order and stops at the same truncation lag.
`verify.py` checks bitwise equality with the imported originals.

`axis_reader.py` shares no reduction code with the engine or `axis_core.py`.
For every saved state it checks the format, rebuilds all oriented fluxes with
numpy, recomputes the five flux counts, both `TWISTJ_FNVLIKE64_V1`
fingerprints and all 24 slice-sum series, and requires exact equality with
the engine transcript; it then recomputes `R` and `Q` from its own `S` and
requires exact equality with the committed records.

### Seeds

Fresh family, never used before this pin. For each chain,

```text
seed = first 8 bytes, big-endian, of
       SHA-256("P-PHOTON-AXIS-POS-PRIMAL-1|89d3c850a673b5941ffd9831058c6ee9c345710b|L=<L>|start=<start>|replica=<r>")
```

```text
L8_cold_r1   0x6d4d7b648b1b8128     L8_cold_r2   0xe94c6d0eea7477b0
L8_hot_r1    0xcd39b9919d2e24ff     L8_hot_r2    0x5d9ffe5de7975fee
L12_cold_r1  0x36aa4851e2a40548     L12_cold_r2  0x5a2bb3a34fe22cbf
L12_hot_r1   0x855466a214047b42     L12_hot_r2   0x8cf2843eb264b74c
L16_cold_r1  0x4265ea1a8adad231     L16_cold_r2  0x50eb4abb4fc26ca6
L16_hot_r1   0x324ac736256fbd4d     L16_hot_r2   0xa19ad020de083921
L24_cold_r1  0x0d05f43279568d5d     L24_cold_r2  0xcbde94e5c11f9cf5
L24_hot_r1   0x5daba2e08ccae6ea     L24_hot_r2   0xb9944919459f03d0
L32_cold_r1  0x3852404d4dc7fc9e     L32_cold_r2  0x756618f97498fe03
L32_hot_r1   0x1e1f260ebaf6024a     L32_hot_r2   0x8fee05c44d668a7e
```

No seed from any opened historical run is used. No failed chain is replaced.

## Field 3: carrier and data

```text
sizes                 L = 8, 12, 16, 24, 32
chains per L          4: cold r1, cold r2, hot r1, hot r2
cold start            all-zero links
hot start             exact-uniform Z5 links of the accepted implementation
thermal endpoints     1024, 2048, 4096, 8192 macrocycles
thermal window        the last 512 macrocycles before an endpoint, every macrocycle
measurement           1024 samples per chain after the accepted endpoint T
sample spacing m_L    1, 1, 2, 4, 8 macrocycles for L = 8, 12, 16, 24, 32
sample s              taken after macrocycle T + m_L (s+1); none at T itself
```

The spacing departs from the reservation text and is justified in section 9.

Each chain is one engine process (`--axis`). In each thermal window it prints
the sixteen pilot-2 sentinels per macrocycle in the pilot-2 SAMPLE format; at
each endpoint it prints an ENDPOINT census line and waits for `MEASURE` or
`CONTINUE` on standard input. The supervisor answers with the automated rule
of Field 4 for the four chains of that `L`; nothing else enters. After
`MEASURE` the engine prints, per sample, the SAMPLE line and the 24 exact
`AXIS_S` lines, and writes the link state in the #748 format:

```text
TWISTJ_Z5_LINK_STATE_V1
L=<L>
CHAIN=L<L>_<start>_r<replica>
SAMPLE=<s>
MACROCYCLE=<T + m_L (s+1)>
LINKS=<4 L^4 digits 0..4, offset 4 site + mu, site = ((x0 L + x1) L + x2) L + x3>
END
```

The full transcript of a chain is the engine stdout with the supervisor's
`RUNNER_COMMAND` lines inserted after each ENDPOINT. Link states (about
24 GB) and full transcripts stay on the formal host under the state root, with
SHA-256 custody in `STATE_MANIFEST.tsv` and `CHAINS.tsv`. Committed records:

```text
records/<chain>.thermal.txt   exact byte prefix of the transcript through MEASURE_BEGIN
records/<chain>.measure.txt   header binding the transcript hash, then per sample the
                              SAMPLE line and four AXIS_Q lines, then 24 AXIS_RTOT lines,
                              AXIS_DIAGNOSTICS and the status footer
```

Every committed file stays below 5 MiB; the largest measurement record is
about 2 MB (engineering estimate from a synthetic full-size record).

Allowed additions after the pin are exactly:

```text
records/ (40 files)   CHAINS.tsv   READER.txt   STATE_MANIFEST.tsv
ANALYSIS.txt          EXPECTED.txt RUN.md       RESULT.md
```

## Field 4: systematics and frozen analysis

### 4.1 Thermal rule (#757 section 5, unchanged)

At each candidate endpoint the four chains of one `L` are judged together on
their last 512 macrocycles. A census, cap, prefix-depth, decision-count,
fingerprint-continuity or sample-format failure is `STOP_INTEGRITY`. The
earliest endpoint is accepted only if every chain has moved a noncontractible
line in every direction and, for every sentinel:

```text
unique state fraction per chain                 >= 0.99
strictly positive finite variance               per chain
Geyer IMS ESS per chain                         >= 64
rank-normalized split Rhat                      <= 1.05
folded rank-normalized split Rhat               <= 1.05
pooled rank-normalized bulk ESS                 >= 400
pooled 5%/95% tail ESS                          >= 200
hot/cold mean separation                        <= z 4
first-half/second-half drift in every chain     <= z 4
```

No endpoint accepted by 8192 is `STOP_MIXING`. No restart with new seeds.
The analysis replays the rule from the committed thermal records and requires
it to reproduce every recorded command; a disagreement is `STOP_INTEGRITY`.

### 4.2 Post-measurement gates (#757 section 6, unchanged thresholds)

On the 1024 measurement samples of every chain and every sentinel:

```text
unique state fraction per chain                 >= 0.99
Geyer IMS ESS per chain                         >= 128
rank-normalized split Rhat                      <= 1.03
folded rank-normalized split Rhat               <= 1.03
pooled bulk ESS                                 >= 800
pooled tail ESS                                 >= 400
hot/cold mean separation                        <= z 3
first-half/second-half drift in every chain     <= z 3
fewer than 16 complete blocks (section 4.3) for a sentinel: STOP_MIXING
```

Samples are never extended, thinned differently or discarded.

### 4.3 Uncertainty (#757 section 7, unchanged)

For a scalar observable at fixed `L`: Geyer IMS `tau_int` in each chain,
`tau_max` over the four chains, `b = max(16, ceil(4 tau_max))` rounded up to a
power of two, blocks inside chains only, complete blocks only. Fewer than 16
complete blocks in any chain: the observable is unresolved. Otherwise the
estimate is the mean of all complete-block means, its error the
chain-preserving delete-one-block jackknife over all `N = 4 n_c` blocks,
`nu = N - 1`, and the interval `mean +- t_{0.995,nu} se`. Different `L` are
independent.

`t_{0.995,nu}` is defined by the fixed Cornish-Fisher expansion
(Abramowitz-Stegun 26.7.5, four terms) around `z = 2.5758293035489`; it
agrees with the exact quantile to better than `10^-7` for `nu >= 60`, and
`nu >= 63` whenever an observable is resolved.

### 4.4 Primary inference

For `L in {12, 16, 24, 32}` (`L = 8` is diagnostic) with `D_L` resolved, fit
by weighted least squares with weights `1/se_L^2` and a free intercept

```text
M1:  D_L = Delta_inf + a/L
M2:  D_L = Delta_inf + a/L^2
```

The 99% interval of `Delta_inf` is `Delta_inf +- t_{0.995,nu_fit} se_inf`
with `se_inf^2 = (sum w x^2)/det` from the inverse information matrix and
`nu_fit = min_L (N_L - 1)` over the four fit sizes. The fit chi-square is
reported with no authority. A singular fit, or an unresolved `D_L` at any fit
size, is `AXIS_UNRESOLVED`.

### 4.5 Reported without terminal authority

All four `D_r` with block intervals; per-chain `D_L` means and hot/cold
separation; `a_L` and `R_L = 3(a_L - D_L)` with block intervals; the six
orientation powers at each `q_r` per chain and pooled, from exact totals;
the complete thermal and post-measurement gate surfaces. Under `STOP_MIXING`
the fits are still printed, marked `FIT_AUTHORITY NONE`.

### 4.6 Known systematics

The estimator sits at the lowest momentum, the slowest mode of a local heat
bath. Finite size: the asymptotic families are prospective, not validated. A
positive finite `Delta_L` does not imply a positive limit; #1133 already proves
`Delta_L > 0` at every finite even `L` with a floor that degenerates as `L`
grows, so the probe tests the extrapolated limit, not the finite sign.
Production is single-host; integrity rests on determinism, the independent
reader and the replayed analysis. Floating quantities enter only the
statistics, as in #757.

The inherited post-measurement gates test 64 half-drifts and 16 hot/cold
separations per `L` at `z <= 3`. For ideal stationary chains the normal-theory
chance that at least one fires at a given `L` is `1 - (1 - 0.0027)^64`, about
16%; a synthetic check (200 groups each of independent and of correlated
AR(1) sentinels, no TWIST data, engineering readout) gave 14% and 17.5%. Over
five sizes a `STOP_MIXING` without any real mixing defect therefore has a
probability of roughly one half. The gates are kept as reserved; a
`STOP_MIXING` must be read with this rate in mind and is not by itself
evidence of slow mixing.

## Field 5: failure thresholds and terminal grammar

Exactly one terminal, in this precedence:

```text
1  STOP_INTEGRITY
2  STOP_MIXING
3  AXIS_POS_EVIDENCE
4  AXIS_NONPOS_EVIDENCE
5  AXIS_UNRESOLVED
```

```text
STOP_INTEGRITY        any source, pin, dependency, compile, fixture, state,
                      transcript, record, reader, hash, orientation, Fourier
                      convention, exact closure, replayed thermal command,
                      process exit or stderr, or custody check fails.
STOP_MIXING           integrity passes but a thermal or post-measurement gate
                      fails at any L, including L = 8.
AXIS_POS_EVIDENCE     lower 99% bound of Delta_inf > 0 in BOTH M1 and M2.
AXIS_NONPOS_EVIDENCE  upper 99% bound of Delta_inf <= 0 in BOTH M1 and M2.
AXIS_UNRESOLVED       integrity and mixing pass and neither sign is earned.
```

Falsifier of AXIS-POS at this scope: `AXIS_NONPOS_EVIDENCE`. It is evidence
against AXIS-POS at the declared extrapolation scope, not a falsification of
every photon reading. A fired falsifier, a STOP or an unresolved result is
recorded and merged as it is. No threshold, schedule, size or chain changes
after the pin.

## Field 6: action layer

```text
action layer            L6 finite-volume measure
consumed state          L1 exact Z5 links and flux
cross-layer claim       none
Canon movement          none in this probe
maximum status          C, finite-size evidence at the declared scope
```

## 7. Immutable source table

`PREREG.md` cannot hold its own digest and `AXIS_PIN.md` is written after
it; both are fixed by `SHA256SUMS` and the public pin readback.

```text
SOURCE_TABLE_PLACEHOLDER
```

## 8. Execution and custody lock

The pin is the first commit on the branch containing `AXIS_PIN.md`. After the
public readback of that commit, the only formal command, from the probe
directory on the formal host, is

```text
python3 run_axis.py formal --pin <pin commit> --boost-deb <path> \
    --state-root <empty local directory> --attempt 1
```

with `LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0`. It
refuses to start if a decision artifact exists, a pinned byte differs, HEAD is
not the pin, the probe directory is dirty or the public branch head is not the
pin. It runs the reader, the analysis and `verify.py` once and writes
`EXPECTED.txt`.

An interrupted attempt is not resumed. Attempt `n+1` reruns all twenty chains
from macrocycle zero with the same pin and seeds; the sampler is a pure
function of its seeds, and the supervisor requires every partial transcript of
an earlier attempt to be a byte prefix of the new one. Every attempt is
recorded in `RUN.md`.

The local leg is `verify.py` on the formal host; the GitHub legs rerun it on
x86_64 and aarch64 with byte-identical stdout required.

## 9. Departures from the reservation and owner decisions, all before data

1. **Sample spacing.** The reservation names one macrocycle between samples.
   Before any AXIS output existed, a Gaussian control (noncompact Maxwell
   field, checkerboard heat bath, no TWIST data; engineering readout) gave for
   the same lowest-momentum contrast `tau_int` of about 3, 5, 10, 17 to 26 and
   33 to 41 macrocycles at `L = 8, 12, 16, 24, 32`, consistent with
   `tau ~ 1.47/khat^2`, `khat^2 = 4 sin^2(pi/L)`. With spacing 1 the section
   4.3 rule would leave `L = 24, 32` unresolved by construction, and the probe
   could not return either sign terminal. The owner fixed `m_L = (1,1,2,4,8)`,
   keeping 1024 samples per chain and twice the margin of the minimal choice.
   This raises the cost, reduces nothing, and was chosen from no AXIS value.
   The reservation's successor-identifier clause addresses a count that cannot
   be run; the count is unchanged and runnable, so the identifier is kept by
   owner decision.
2. **Intercept interval.** #757 fixes weighted least squares with jackknife
   errors and a 99% interval but not the quantile. This probe uses the
   Student-t of section 4.3 with `nu_fit = min_L (N_L - 1)`, the #757 section 7
   convention for jackknife intervals.
3. **State storage.** Link states stay on the formal host disk with SHA-256
   custody; only records, hashes and the reader receipt are committed.
4. **Receipt.** The public pin receipt on #1116 is posted by the owner
   directly, because this implementation session's publication path appends a
   footer to comment bodies.

## 10. Prior knowledge and pre-pin development, disclosed

- #1133 (candidate-T, notes): strict positivity of every nonzero finite axis
  coefficient at even `L >= 4`, with a degenerating floor.
- #1150 (draft notes): engineering exact/coexact contrasts at the fixed weight,
  including the `q_min` quantity, from a different floating-point lineage with
  sector filtering; known before this pin. This result is not a blind discovery.
- A parity run of the development engine on the published pilot-2 `L = 6`
  cold r1 chain reproduced all 512 published SAMPLE lines byte for byte. It
  also produced AXIS_S lines; they were deleted unread and only their SHA-256
  `b09db8e13b624ec8a533725d39f2c5d8add6ba0b79c0dd0e026907eb94eb6e54` was kept.
- The Gaussian control of section 9 (no TWIST data).
- A first plumbing run that included `L = 8, 10, 12` under development seeds was
  stopped before any analysis and deleted unread when it was recognised that it
  touched production-adjacent sizes.
- Blind plumbing runs of the full pipeline under the DEVELOPMENT configuration
  (`L = 3, 4, 5, 6`, development seed family, 64 samples). Only integrity
  status lines were inspected; no estimator value was opened.
- Synthetic, non-physical full-size records (pseudo-random numbers, no engine)
  for timing and tamper tests of the analysis and the verifier.
