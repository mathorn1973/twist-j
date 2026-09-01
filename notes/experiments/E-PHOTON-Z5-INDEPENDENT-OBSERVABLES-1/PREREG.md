# E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1 preregistration

**Status:** COMPLETE PRE-PIN CANDIDATE / UNEXECUTED / ZERO-EVIDENCE / NON-CANONICAL

**Owner:** A. M. Thorn

**Public reservation:** issue #748

**Parent experiment:** issue #742

**Branch:** `experiment/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1`

**Directory:** `notes/experiments/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1/`

**Public base:** `59cee594b974be6ccddf9785d35cf9da750d36a6`

**Date:** 2026-09-01

This document freezes the contract for the independent saved-state reader
required by issue #748 and by the production firewall in PR #768. The directory
now contains a complete pre-pin candidate reader, oracle, fixture corpus and
verifier. It does not yet pin or accept them, and no formal gate may run before
the candidate is publicly pinned and read back under section 12.

The lane reads exact finite periodic `Z5` link fields and emits exact sufficient
statistics. It does not sample the measure, inspect a production result, choose
a scientific threshold or classify a phase.

## 0. Authority and prerequisites

```text
repository authority       mathorn1973/twist-j main
public Canon               Public Canon v74
Canon tag                  canon-v74
Canon content commit       2561f7dcadcbbf683ce7b36219ea67378d879a5a
Canon SHA-256              2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
Canon bytes                389246
reader public base         59cee594b974be6ccddf9785d35cf9da750d36a6
primal exact kernel        PR #760 merge 5c2d469880828f29023e3cf592e86abbe352cd59
successful mixing pilot    #755 / PR #765 / PR #766
dual source freeze         PR #767 merge 3bb9087cdea293c494ae86b5824e9d8d221fbbfb
production freeze          PR #768 merge 59cee594b974be6ccddf9785d35cf9da750d36a6
```

The current public `main` checks at the reader base passed on `x86_64`,
`aarch64` and the aggregate required context. That fact fixes the starting
surface only; it supplies no reader result.

Production under #742 remains forbidden until all three conditions frozen by
PR #768 hold:

```text
F1  the production preregistration is merged and publicly read back;
F2  this independent reader is pinned, its exact fixtures pass and the result
    is merged and publicly read back;
F3  the separate zero-evidence L=6,8 dual/Ward execution under #756 returns
    DUAL_CROSSCHECK_PASS.
```

This lane can satisfy only `F2`. It cannot satisfy, waive or reinterpret `F1`
or `F3`.

## 1. Frozen question and action layer

The only question is:

```text
Does a second implementation, given only one canonical hashed Z5 link-state
file, reconstruct the frozen gauge-invariant observables and exact sufficient
statistics with the declared orientation, topology and covariance semantics?
```

The action-layer map is

```text
L1 canonical saved link field
  -> L4 charged periodic component topology
  -> L5 deterministic sufficient-statistic record.
```

There is no L6 sampling, measure inference or phase decision in this lane. Its
maximum status is zero-evidence engineering integrity.

## 2. Independence and implementation architecture

The candidate production reader is a C++ implementation designed to
process `L=32` states with compact storage. It must use `O(L^4)` working memory
apart from its serialized output and may use `O(L^5)` work for the complete
separation census. It may not materialize a dense `O(L^8)` incidence or pair
matrix. It consumes only the seven-line state file in `STATE_SCHEMA.md` and the
expected whole-file SHA-256 supplied by its caller after custody-manifest
resolution.

The C++ reader must not:

- include, link, import or copy the primal sampler's observable code;
- consume the sampler's flux cache or in-memory observables;
- treat a sampler summary, state fingerprint or raw log as an observable;
- use a sampler-produced observable file as expected fixture truth.

The independent fixture oracle is Python. It is limited to the small periodic
fixture lattices and independently implements coordinates, coboundaries,
Hodge signs, homology, Polyakov statistics and correlator histograms. It may
not import or reuse C++ reader logic, call the C++ reader to construct expected
answers, use FFI into the reader, or translate a reader-produced record into
an alleged oracle record. The C++ reader and Python oracle may share only the
normative bytes and equations frozen in these documents and the same pinned
fixture state files.

The accepted source and fixture bytes and their SHA-256 values are owned by the
later public candidate pin and `SOURCE_SHA256SUMS`. The formal command, neutral
environment, interpreter/compiler versions and flags are already frozen in
section 12; they are not silently inferred from the invoking shell.

## 3. Input carrier and custody

The serialization is exactly `TWISTJ_Z5_LINK_STATE_V1` in
`STATE_SCHEMA.md`. Its admitted range is

```text
2 <= L <= 32.
```

The production experiment may use only its already frozen sizes
`L={8,12,16,24,32}`. Smaller sizes exist only for synthetic integrity fixtures
and do not acquire evidential weight.

For each `L`, the carrier is

```text
K_L=(Z/LZ)^4,
A in C^1(K_L;Z5).
```

There is no gauge quotient. All periodic holonomy sectors in all four
directions are retained.
Every state file has a mandatory whole-file SHA-256 in an external custody
manifest. A self-declared hash inside the hashed state is forbidden. The state
producer owns the original bytes and manifest row. The caller or formal
verifier resolves the unique row and passes its digest through
`--expected-sha256`; the reader recomputes and verifies the digest before
parsing, never rewrites the state, and binds its output to the verified input
digest and byte count. The C++ reader is deliberately not a manifest parser.

The 64-bit sampler-compatible fingerprints described below are deterministic
cross-checks only. They are not cryptographic custody hashes and cannot replace
SHA-256.

## 4. Coordinates, links and oriented plaquette flux

Coordinates and links have the exact order

```text
site(x0,x1,x2,x3) = (((x0 L + x1) L + x2) L + x3),
0 <= x_mu < L,
link_id(x,mu) = 4 site(x) + mu,
mu = 0,1,2,3.
```

Thus `x3` is the fastest site coordinate and direction is the fastest link
coordinate. Oriented plaquettes use the ordered pair list

```text
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3).
```

For `a<b`, the reader independently computes

```text
F_ab(x) = A_a(x) + A_b(x+e_a) - A_a(x+e_b) - A_b(x) mod 5,
```

reported as the canonical residue `0,1,2,3,4`. The principal integer lift is

```text
principal(0,1,2,3,4) = (0,1,2,-2,-1).
```

The exact five-bin flux census must sum to `6 L^4`.

For compatibility auditing only, `TWISTJ_FNVLIKE64_V1` starts at
`1469598103934665603`, then for each byte performs XOR followed by
multiplication by `1099511628211` modulo `2^64`. The flux fingerprint absorbs
the computed plaquette residues in site-major/pair-major order. The state
fingerprint absorbs the input links followed by those independently computed
flux residues. Both render as exactly sixteen lowercase hexadecimal digits.

## 5. Four-direction Polyakov sufficient statistics

Put `omega=exp(2 pi i/5)`. For every direction `mu` and every transverse base
with `x_mu=0`, define

```text
h_mu(x_perp) = sum_(s=0)^(L-1) A_mu(x+s e_mu) mod 5,
Pbar_mu = L^(-3) sum_(x_perp) omega^(h_mu(x_perp)).
```

The reader records the five exact holonomy counts in each of the four
directions. The counts in each direction sum to `L^3` and determine `Pbar_mu`
exactly in `Q(omega)`.

The per-configuration sufficient statistics are exactly

```text
r = (1/4) sum_mu |Pbar_mu|,
u = (1/4) sum_mu Pbar_mu^5,
v = (1/4) sum_mu |Pbar_mu|^5.
```

In particular, `r`, `u` and `v` are averages of four direction-wise
quantities. They are not formed from the modulus or fifth power of a
direction-averaged `Pbar`.

The four five-bin direction histograms are themselves the exact serialized
sufficient statistics. They determine every `Pbar_mu` in `Q(omega)`, hence the
direction-wise numerator powers in the basis
`1,omega,omega^2,omega^3`, with
`omega^4=-1-omega-omega^2-omega^3`, and the squared numerator moduli in
`Q(sqrt(5))`. A later deterministic reducer reconstructs `r`, `u` and `v` from
those histograms. The reader does not serialize redundant explicit `r`, `u` or
`v` objects, and no binary floating-point value owns these statistics.

Across saved states, the frozen production definitions are

```text
R_L  = E r,
A5_L = |E u| / E v.
```

This reader supplies the sufficient statistics only. It does not estimate the
expectations, fit either finite-size family or issue a Polyakov vote.

## 6. Principal-flux monopole current and local closure

For a missing axis `r`, let `a<b<c` be the other axes and define

```text
(d f)_abc(x)
 = f_bc(x+e_a)-f_bc(x)
 - f_ac(x+e_b)+f_ac(x)
 + f_ab(x+e_c)-f_ab(x).
```

The dual current on the direction-`r` dual link based at `x-e_r` is

```text
m_r(x-e_r) = (-1)^r (d f)_abc(x) / 5.
```

The reader requires exact divisibility by five and checks the local integer
divergence at every dual vertex:

```text
sum_r [m_r(y)-m_r(y-e_r)] = 0.
```

Failure of divisibility, the inherited current range or any local closure is
`STOP_INTEGRITY`. The output includes the exact current histogram for values
`-2,-1,0,1,2`.

## 7. Charged periodic topology

Support connectivity is used only to partition cells into components. It has
no authority to declare wrapping.

### 7.1 Vortex components

Every nonzero primal plaquette has the coefficient `F_ab(x)` in `F5` and is
mapped to its oriented dual plaquette. The dual orientation is fixed by

```text
orientation(p) wedge orientation(star p) = orientation(0,1,2,3).
```

Two occupied dual plaquettes belong to the same component when they meet on a
dual edge, equivalently when their primal plaquettes occur as faces of one
primal three-cell; transitive closure gives the component partition. All
incidences at a junction remain in one component.

For a component `C`, form the charged dual two-chain

```text
z_C = sum_(p in C) F_p [star p] in C_2(T^4;F5).
```

The reader verifies `boundary(z_C)=0` exactly. It then reduces `z_C` in

```text
H_2(T^4;F5) = F5^6
```

against the fixed coordinate-torus order

```text
(0,1),(0,2),(0,3),(1,2),(1,3),(2,3).
```

The six residues are recorded as `0,1,2,3,4`. A vortex component is charged
wrapping exactly when this vector is nonzero. The configuration Boolean is

```text
vortex.wrap = OR_C [homology(z_C) != 0].
```

A support component with an inconsistent geometric lift but zero charged
homology is nonwrapping. Opposite charges and multiplicity are not discarded.
Because the complete input flux is `dA`, the sum of all component homology
vectors must be zero in `F5^6`; failure is `STOP_INTEGRITY`.

### 7.2 Monopole components

Nonzero current links are joined at their dual endpoints. For each connected
component `C`, retain the actual integer coefficients:

```text
j_C = sum_(e in C) m_e [e] in Z_1(T^4;Z).
```

After checking `boundary(j_C)=0`, compute its charged winding vector in

```text
H_1(T^4;Z) = Z^4
```

in direction order `0,1,2,3`. A component wraps exactly when its winding
vector is nonzero, and

```text
monopole.wrap = OR_C [winding(j_C) != 0].
```

The component key is its least `(dual_site,direction)` occupied link. The
reader records for every component both the occupied-link count and the
multiplicity length `sum_e |m_e|`. Components are sorted by key. The primary
largest-component statistic is

```text
M = max_C occupied_links(C) / L^4,
```

with exact numerator and denominator. Complete nonincreasing tails of
occupied-link sizes and multiplicity lengths are retained, including repeated
sizes. No component-size cutoff is introduced.

## 8. Exact connected-correlator sufficient statistics

For a plaquette pair `a<b`, write

```text
W_ab(x) = omega^(F_ab(x)),
y = x+n e_rho.
```

The connected terms are

```text
C^+ = E[W_ab(x) W_ab(y)] - E[W_ab(x)] E[W_ab(y)],
C^- = E[W_ab(x)^(-1) W_ab(y)]
      - E[W_ab(x)^(-1)] E[W_ab(y)].
```

The reflection-positive orientation sum is frozen termwise as

```text
C(n)
 = sum_(rho in {a,b}) C^+_(n e_rho;ab)
 + sum_(rho not in {a,b}) C^-_(n e_rho;ab),
```

over all six `a<b`: twelve longitudinal `C^+` terms and twelve transverse
`C^-` terms.

For every integer

```text
1 <= n <= floor(L/2),
```

and every one of the 24 terms, the reader emits three exact five-bin phase
histograms over all `L^4` translations:

```text
product[k] = number of x whose product phase is omega^k,
left[k]    = number of x whose left phase is omega^k,
right[k]   = number of x whose right phase is omega^k.
```

For `C^+`, the three exponents are respectively
`F_ab(x)+F_ab(y)`, `F_ab(x)`, `F_ab(y)` modulo five. For `C^-`, they are
`-F_ab(x)+F_ab(y)`, `-F_ab(x)`, `F_ab(y)` modulo five. Every histogram must
sum to `L^4`.

These integer histograms are the owned sufficient statistics. Complete-block
histograms are formed by integer addition within one chain after the frozen
analysis layer supplies its block length. Only then is

```text
E[product] - E[left] E[right]
```

formed. Configuration-centering first is forbidden. Blocks never cross chain
boundaries, and the reader neither chooses the block length nor runs the
jackknife, GLS fit or phase classifier.

The full separation range includes all values needed by the frozen ratios. In
particular it includes `C(5)` for the `L=16` ratio window, `C(7)` for `L=24`
and `C(9)` for `L=32`.

## 9. Deterministic reader record

One successfully read state produces one canonical ASCII, LF-terminated,
minified JSON object. Canonicalization is exactly Python
`json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True)` plus
one LF. Its top-level keys therefore occur in this exact order:

```text
correlator, flux, monopole, polyakov, schema, state, vortex
```

The nested inventory and order are frozen in `STATE_SCHEMA.md`. The record
contains integers, booleans and restricted ASCII strings only; JSON floating
point, `NaN`, infinities and insignificant whitespace are forbidden. Arrays
have the coordinate, component and term orders frozen above. The record repeats
the verified input SHA-256. It does not contain a phase label.

Reader records and any later block-sufficient-statistic files are immutable
once written. The formal verifier requires C++/Python byte identity and checks
frozen expected full-record and correlator digests. `RUN.md` later owns the
formal two-line stdout digest; custody does not add stdout fields.

## 10. Required independent fixtures

The candidate pin must contain independent Python fixtures on small periodic
lattices. At minimum the corpus must contain:

1. the all-zero state;
2. a flat-holonomy state with zero plaquette flux and changed Polyakov data;
3. exact positive and negative plaquette-orientation controls across a periodic
   boundary;
4. a local nonwrapping vortex surface;
5. charged wrapped vortex components whose total homology cancels, as required
   for `F=dA`;
6. a support-winding but charged-homology-zero vortex negative control;
7. contractible and charged-wrapping monopole-current component controls;
8. positive and negative current-orientation and local-closure controls;
9. a correlator record that distinguishes block covariance from forbidden
   configuration-centering;
10. malformed ASCII, CRLF, bad length, bad residue, noncanonical decimal,
    absent hash and hash-mismatch controls;
11. the sampler-compatible flux and state fingerprint fixtures;
12. byte-identical complete JSON from the independent Python oracle and C++
    reader on every accepted positive fixture.

Fixture states and expected oracle bytes must be fixed before the formal gate.
No fixture may be created from production data.

## 11. Integrity failures and exact terminal grammar

Completed formal-gate stdout is exactly one of these two two-line ASCII/LF
records and has no other byte:

```text
STOP_INTEGRITY
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

or

```text
INDEPENDENT_READER_FIXTURE_PASS
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

`STOP_INTEGRITY` has precedence and fires on any modeled source or pin mismatch,
noncanonical state, missing or wrong SHA-256, orientation mismatch, flux-count
failure, fingerprint mismatch, nonintegral or nonclosed current, component
boundary failure, charged-homology failure, total-homology failure, malformed
JSON, histogram census failure, Python/C++ disagreement, process failure,
nonempty stderr or custody failure that the verifier models as a complete
terminal.

`INDEPENDENT_READER_FIXTURE_PASS` is available only when every frozen fixture,
exact integer audit, canonical-byte comparison and custody check passes.

Neither terminal is phase evidence. The strings

```text
PHOTON_EVIDENCE
CONFINED_EVIDENCE
Z5_BROKEN_EVIDENCE
MULTIPHASE_OR_TRANSITION
AMBIGUOUS_FINITE_SIZE
STOP_MIXING
DUAL_CROSSCHECK_PASS
```

are forbidden as reader conclusions. In later production, a reproducible
reader/state mismatch is owned by the production terminal `STOP_INTEGRITY`;
this lane does not run that production terminal classifier.

## 12. Pin, readback and one-shot formal execution

Before the public candidate pin, only document review, compilation, static
analysis and explicitly non-formal development tests are permitted. No formal
gate may run.

The candidate pin must commit and push, in one publicly readable state:

- these final documentation files;
- the accepted C++ production reader;
- the structurally independent Python fixture oracle;
- the exact fixture corpus;
- the accepted verifier and its exact command;
- the complete exact-TSV source/fixture manifest `SOURCE_SHA256SUMS`;
- compiler/interpreter versions and build flags;
- the exact expected inventory and terminal grammar.

The exact formal command, issued from the repository root, is

```text
python -B notes/experiments/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1/verify.py
```

The neutral execution environment is frozen as

```text
operating system  Windows NT 10.0.26200 x64
Python            3.12.10
CXX               unset; verifier resolves g++.exe
compiler          g++.exe MinGW-W64 x86_64-ucrt-posix-seh
                  Brecht Sanders r7, version 15.2.0
compile flags      -std=c++20 -O2 -Wall -Wextra -pedantic
bytecode policy    Python -B; no repository __pycache__
```

`SOURCE_SHA256SUMS` owns every frozen document, source, verifier and fixture
listed in `README.md`, but cannot contain its own recursive row. The public pin
and readback receipt own the manifest's exact bytes and SHA-256.

Every pinned byte and the branch commit must be read back from the public
remote before execution. The pin is never amended, rebased, squashed or
force-pushed.

After readback, the formal fixture gate runs once from the repository root. A
completed modeled terminal must exit zero, write empty stderr and printable
ASCII/LF stdout. Its exact stdout becomes `EXPECTED.txt`; `RUN.md` records the
pin, command, neutral environment, exit status, byte count and hashes. A crash,
nonzero exit or other failure to produce one complete modeled terminal consumes
the pin under the abandoned-pin rule; it is not rerun after repair under this
identifier.

The formal fixture gate is a pinned, one-shot local execution. Because this is
an `E-...` experiment lane rather than a public `P-...` probe, the repository's
generic changed-note `x86_64`, `aarch64` and aggregate required checks audit the
repository and pull request; they are not claimed to replay this formal reader
gate automatically. Those generic required checks must still pass. Only a
merged, publicly read-back record of the pinned local
`INDEPENDENT_READER_FIXTURE_PASS` satisfies production-firewall clause `F2`.

## 13. Hard scientific boundary

This lane does not:

- generate, open or inspect any production state;
- start or authorize #742;
- select thermal endpoints, seeds, chain replacements or sample counts;
- choose or alter block lengths, uncertainty rules, fit families, windows,
  wrapping thresholds or phase vectors;
- implement the independent dual ensemble or execute the Ward comparison;
- infer a phase, massless limit, continuum pole or physical photon;
- change Canon, Registry, Gates, Frontier, releases or public status.

The action, production sizes, starts, twenty seeds, thermal endpoints,
measurement count, uncertainty rule, Polyakov fits, topology thresholds,
correlator windows, phase vectors and production terminal precedence remain
exactly those frozen by PR #768. This reader implements only the already
declared saved-state reconstruction obligation.

## 14. Freeze table

```text
input schema             FIXED TWISTJ_Z5_LINK_STATE_V1
input range              FIXED 2 <= L <= 32
production sizes         INHERITED {8,12,16,24,32}
link/site order          FIXED section 4
plaquette orientation    FIXED section 4
principal lift/current   FIXED section 6
Polyakov ownership       FIXED section 5, direction-wise r/u/v
vortex Boolean           FIXED per-component charged H_2(T4;F5)
monopole Boolean         FIXED per-component charged H_1(T4;Z)
component primary size   FIXED occupied links / L^4
correlator terms         FIXED 12 C+ plus 12 C-
correlator separations   FIXED 1..floor(L/2)
covariance construction  FIXED after block aggregation
reader output            FIXED Python-sort-key canonical exact JSON
implementation split     FIXED production C++ / independent Python oracle
terminal grammar         FIXED STOP_INTEGRITY / INDEPENDENT_READER_FIXTURE_PASS
evidential status        FIXED ZERO_ENGINEERING_ONLY
```

No item in this table may be changed after the candidate pin in response to a
fixture, production observable or scientific outcome.
