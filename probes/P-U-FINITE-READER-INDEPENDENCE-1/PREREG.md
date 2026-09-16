# P-U-FINITE-READER-INDEPENDENCE-1 preregistration

**Do not execute before immutable commit, push, and accepted-byte readback.**

Mode: PROOF-FIRST / RESULT-EXPOSED / NON-CANONICAL MATHEMATICS.
Owner: A. M. Thorn. Public base: `e6d6fcc2a23f4277345bc684b410e69aae8d45e0`.
Public lock: [#890](https://github.com/mathorn1973/twist-j/issues/890).
Authority: ACTIVE Public Canon v80, `canon-v80`, content commit
`b00171ef21ecb0d905593224f66f5e8a0f6c28e5`, Canon SHA-256
`8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. The immutable pin/hash record follows public commit and readback.
No formal execution has occurred in preparation.

## 1. Equation and exact targets

For every origin-zero native head `x_0 in F_5^6`, use the complete unchanged
autonomous update `U(n,x)=(n+1,g_(sum(x)+2 theta_n mod 5)(x))` and
`theta_n=popcount(n) mod 2`. A fixed causal reader sees only a fixed length-L
window of decorated checkpoints `(x_n,theta_n)` and is applied at every
consecutive tick with `n>=L+2`. Outputs are 0, 1, or SILENT, with literal
equality and chronological SILENT deletion. It receives no absolute counter,
growing history, additional memory or source input. No feedback changes U.

Prove the following in the full stated classes; finite enumeration audits
these proofs and does not establish an extrapolation:

1. The actual synchronized decorated word has complexity `p(t)<=20,000 t`.
2. Acceptance is either empty or syndetic. An accepted legal word contained
   in `psi_ell(sigma^j(c_0))` gives the sufficient gap `G=2^(j+79)`.
3. Accepted k-block complexity is at most `20,000[L+G(k-1)]`. A fixed global
   reader over all heads has union bound `62,500,000[L+G(k-1)]`, using the
   maximum gap over its nonempty chart classes.
4. These bounds exclude nondegenerate Bernoulli product block frequencies at
   all orders and corresponding block laws supported on the same language.
5. For every prechosen finite horizon h, a fixed finite-window phase reader
   of length `5*2^(h-1)` followed by a binary de Bruijn cycle attains exact
   fair block frequencies through h, then fails at h+1. Thus there is no
   universal finite failure horizon across all finite window lengths.

The first four statements refute only the proposed all-order sufficiency of
this reader class. They do not refute Born marginals, approximate statistics,
finite-horizon apparatuses, arbitrary complete-counter readers, or physics.

## 2. Accepted code

`verify.py` is standalone Python 3.10 or later with only standard-library
imports. It reads no external data or repository file, performs no network
access or random sampling, uses exact integers and rationals only, and prints
one deterministic JSON record. Written proof is `PROOF.md`.

Every completed check contributes to a named exact-check count. A scientific
mismatch is retained in a FALSIFIED transcript with exit 0. An unexpected
exception is an incomplete STOP run, not a physical/scientific falsification;
the identifier is consumed under the ordinary abandoned-pin policy if no
completed exact result exists. Neither accepted source nor thresholds may be
repaired after pin. No dry run or source import is allowed before public pin.
Only syntax/static review is allowed.

## 3. Carrier and frozen audit data

All fixtures are equations and finite exhaustively declared mathematical
carriers; there is no experimental payload.

* All 15,625 origin-zero heads, literal native transitions through tick 11,
  and chart/morphism comparisons at each synchronized tick.
* All 100 clock letters, both digit transitions, literal integer clocks
  `0<=m<4096`, and exact 77-step Boolean reachability from every letter.
* All legal clock pairs, obtained as the least closure of internal
  substitution pairs under `(a,b)->(T1(a),T0(b))`, with constructive nested
  occurrence witnesses. All observed pairs in a literal 4096-letter prefix
  must be included. No finite observed prefix is assumed complete.
* Complete binary Thue-Morse factor languages at the finite lengths used
  below, obtained from all four legal ancestor pairs and dyadic block offsets.
  Direct substitution prefixes provide the independent bounded comparison.
* All ternary output tables on a one-bit or two-bit causal Thue-Morse window:
  `3^2+3^4=90` tables, including empty and one-symbol acceptance. Every active
  table has the independently certified common sufficient gap 16. Accepted
  block supports are audited at k in `{1,2,3,4,8,12}` by complete raw language
  extraction and direct output-prefix extraction. A missing 12-bit word is
  retained per active table. The scalar window is a fixed decorated-reader
  subclass, not the whole class of arbitrary checkpoint readers.
* Binary de Bruijn and finite-history phase positive controls for h=1..8,
  all phase contexts at the inherited sufficient window length, cyclic
  block counts through h, and missing support at h+1.

## 4. Systematics and prior exposure

Execute in Linux or Linux-compatible WSL with LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1. Standard-library Python
>=3.10; repository CI uses 3.12. Record the actual interpreter, platform and
architecture. Require exit 0, empty stderr, deterministic UTF-8 stdout and
a 600-second process ceiling. The code encodes SILENT as the distinct
integer 2; mathematical event symbols remain 0 and 1.

The proposed proof was developed after the merged finite reversible result
`P-RECORD-OCCURRENCE-SYMMETRY-1`. Its known negative and positive results are
disclosed inputs. This probe claims neither blind prediction nor independent
rediscovery of the inherited native chart, phase reader, recurrence,
primitive clock, de Bruijn construction, or driver-only entropy result.

The new step is the complete decorated native language bound after arbitrary
fixed finite-window reading and SILENT deletion, together with its precise
finite-horizon limit. No theorem about a periodic finite checkpoint is used
as a theorem about complete U. Empty acceptance has no ratio. A finite number
of unsynchronized outputs cannot create positive density of an absent tail
word. No limiting block frequency is presumed where absence alone suffices.
Bounded sample consistency cannot replace the written all-length proof.

No independence requirement is attributed universally to physical quantum
experiments. The constants and horizons are sufficient, not minimal. No
physical memory cost, approximate bound, probability dictionary, actual
apparatus or occurrence law is adopted. Arbitrary explicit counter readings
remain outside the finite-window class and may encode prescribed sequences.

## 5. Threshold and disposition

Threshold: zero exact mathematical mismatches. Any admitted violation of the
coding, finite covers, gap claim, complexity bounds, all-order obstruction,
or finite-horizon construction fires the corresponding frozen mathematical
target. Preserve an exact counterexample; do not change the class or threshold.

A complete proof plus identical exact stdout on x86_64 and aarch64 supports
the proposed mathematical result at its stated scope. A proof defect without
an exact negation is unresolved mathematical STOP; integrity, runtime, source
hash, stderr or architecture failure is integrity STOP, not evidence against
Born or any physical owner. A later Canon fold remains separate.

## 6. Action layer and immutable procedure

Action layer: L1 exact native-path and finite-word mathematics. Word counts
and their formal all-prefix limits do not supply an admitted physical stream
or L6 probability. The source equations and word recurrences are inherited
L1 facts. No new L4/L5, L5/L6 or other cross-layer gate is asserted.

Before formal execution, claim exactly this identifier publicly, commit and
push this file with PROOF.md and verify.py, and read back their exact hashes.
Then execute the accepted verifier once in a Linux-compatible environment.
Append EXPECTED.txt, RUN.md and RESULT.md without changing accepted bytes.
Require byte-identical two-architecture CI and merge without squash/rebase.
Keep canon/, STATUS, Registry, Frontier, gates, release and all older probes
unchanged. This lane selects no physical profile under issue #539.
