# TWISTJ_Z5_LINK_STATE_V1

**Status:** COMPLETE PRE-PIN CANDIDATE / UNEXECUTED / ZERO-EVIDENCE / NON-CANONICAL

**Owner:** issue #748

**Public base:** `59cee594b974be6ccddf9785d35cf9da750d36a6`

This document freezes the canonical saved-link-state bytes consumed by the
independent reader. A conforming file contains a link field only. It contains
no plaquette cache, observable, weight, phase label, threshold or in-memory
sampler value.

## 1. Exact seven-line file

A state file consists of exactly seven LF-terminated lines and no other byte:

```text
TWISTJ_Z5_LINK_STATE_V1
L=<canonical decimal>
CHAIN=<chain identifier>
SAMPLE=<canonical nonnegative decimal>
MACROCYCLE=<canonical nonnegative decimal>
LINKS=<exactly 4*L^4 digits from 0 through 4>
END
```

Equivalently, the exact byte grammar is

```text
"TWISTJ_Z5_LINK_STATE_V1\n"
"L=" LDEC "\n"
"CHAIN=" CHAIN "\n"
"SAMPLE=" NDEC "\n"
"MACROCYCLE=" NDEC "\n"
"LINKS=" LINKDIGIT^(4*L^4) "\n"
"END\n"
```

where

```text
LDEC      := a canonical decimal integer in [2,32]
NDEC      := "0" or [1-9][0-9]*, with value in [0,2^64-1]
CHAIN     := [A-Za-z0-9][A-Za-z0-9_.-]{0,63}
LINKDIGIT := [0-4]
```

`LDEC` is also canonical: it has no sign and no leading zero. Production is
restricted separately to `L={8,12,16,24,32}`. Values `2<=L<8` and other
nonproduction values in the admitted range exist only for integrity fixtures.

## 2. Byte restrictions

Every byte before the mandatory final LF is printable seven-bit ASCII. The
only line separator is byte `0x0a`. The following are forbidden:

- UTF-8 BOM or any byte above `0x7f`;
- CR or CRLF;
- tabs, trailing spaces, blank lines or comments;
- leading or trailing bytes;
- duplicate, reordered, omitted or unknown fields;
- a missing final LF;
- a sign or leading zero in a decimal;
- lowercase or alternate schema spelling;
- a link digit outside `0,1,2,3,4`;
- any payload separator or line wrapping.

The parser decodes `SAMPLE` and `MACROCYCLE` with checked unsigned 64-bit
arithmetic. It computes `4*L^4` with checked integer arithmetic before
accepting the payload. It rejects a decimal overflow or a payload of any other
length.

A conforming parser must construct the canonical seven lines again from its
parsed values and demand byte identity with the input. Acceptance followed by
different reserialization is `STOP_INTEGRITY`.

## 3. Link order

The `LINKS` digit at zero-based offset `i` is the canonical residue of exactly
one positively oriented link. Decode it by

```text
site = i div 4,
mu   = i mod 4,

x3 = site mod L; site = site div L,
x2 = site mod L; site = site div L,
x1 = site mod L; site = site div L,
x0 = site mod L.
```

Equivalently,

```text
site(x0,x1,x2,x3) = (((x0 L + x1) L + x2) L + x3),
i = 4 site + mu.
```

Thus `x3` is the fastest site coordinate and `mu` is the fastest link
coordinate. Negative links are represented only by negating the corresponding
positive-link residue modulo five; they never receive a second payload entry.

## 4. Chain and sample identity

`CHAIN` is an opaque custody identifier satisfying the grammar above. The
reader must reproduce it byte for byte and must not infer hot/cold status,
replica, seed or a phase from its spelling.

`SAMPLE` is zero based for production measurement states. With accepted
thermal endpoint `T`, production sample `s` is saved after the complete
macrocycle

```text
MACROCYCLE = T + s + 1,
0 <= s < 1024.
```

The production executor owns validation of `CHAIN` against the twenty frozen
seed/start identities and validation of `T` against
`{1024,2048,4096,8192}`. The reader checks the canonical metadata and binds it
to output but does not select `T`, replace a chain or interpret a failure as a
phase.

Synthetic fixtures may use their declared fixture `CHAIN`, `SAMPLE` and
`MACROCYCLE`; their exact values and hashes must appear in the future pinned
fixture manifest.

## 5. Mandatory external SHA-256 custody

A state file never contains its own digest. For the #748 fixture gate, the
formal verifier must locate each fixture in the mandatory external custody
manifest `SOURCE_SHA256SUMS` and resolve both its exact byte count and
whole-file SHA-256. It passes the resolved digest to the reader as
`--expected-sha256 <64hex>`; the reader recomputes and verifies the digest
before parsing. A later production caller performs the same resolution from
its production-state custody manifest.

The canonical manifest format is ASCII/LF TSV:

```text
TWISTJ_Z5_SOURCE_SHA256SUMS_V1
path<TAB>bytes<TAB>sha256
<row 1>
...
END
```

`SOURCE_SHA256SUMS` uses the displayed
`TWISTJ_Z5_SOURCE_SHA256SUMS_V1` magic and owns the pinned documentation,
reader, oracle, verifier and fixture bytes. A later production-state manifest
may instead use the magic `TWISTJ_Z5_STATE_SHA256_V1` with exactly the same
column, row, ordering and byte rules. The reader receives neither manifest; it
receives only the digest resolved by its caller.

`SOURCE_SHA256SUMS` cannot contain a row for itself: changing that row would
change the file recursively. Its own exact bytes and SHA-256 are instead owned
by the public candidate-pin and readback receipt. Omission of any other frozen
inventory path is `STOP_INTEGRITY`.

Each data row has exactly three fields:

```text
path    a nonempty relative POSIX path made from [A-Za-z0-9_./-], with no
        leading slash, no empty component, no "." or ".." component and no
        backslash;
bytes   canonical nonnegative decimal exact file length;
sha256  exactly 64 lowercase hexadecimal digits.
```

Rows are unique and sorted by raw ASCII `path` bytes. There is exactly one
header, exactly one column-name line, at least one row and exactly one final
`END` line. The manifest itself obeys printable ASCII, LF-only and mandatory
final-LF rules. A state must have exactly one row.

The producer owns and seals the original state bytes and their manifest row.
The caller or formal verifier performs steps 1 and 2; the independent reader
performs steps 3 through 5:

1. verifies the manifest grammar;
2. resolves exactly one row and verifies its byte length;
3. verifies the supplied SHA-256 before parsing;
4. parses and reserializes the state byte for byte and repeats the verified
   lowercase digest and exact byte count in its reader record;
5. never modifies the state or custody manifest.

An absent row, duplicate row, path escape, byte-count mismatch, digest mismatch
or state mutation is `STOP_INTEGRITY`.

The noncryptographic `TWISTJ_FNVLIKE64_V1` state and flux fingerprints are
computed after parsing as independent integer cross-checks. They do not own
custody and cannot replace this section.

## 6. Canonical reader JSON

One accepted state produces exactly one minified JSON object followed by one
LF. Canonicalization is exactly

```text
json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
+ "\n"
```

No whitespace occurs outside strings. Integers are canonical JSON integers,
booleans are `true` or `false`, and no JSON floating point, `null`, `NaN` or
infinity occurs. Because every key is ASCII, recursive Python sort order is
ASCII lexicographic order. Array order is fixed below. The exact top-level key
order is

```text
correlator, flux, monopole, polyakov, schema, state, vortex
```

The top-level `schema` value is exactly
`TWISTJ_Z5_INDEPENDENT_OBSERVABLES_V1`.

### 6.1 `state`

The exact key order and meanings are

```text
L                  admitted linear size
bytes              exact seven-line input byte count
cache_fingerprint  TWISTJ_FNVLIKE64_V1 over reconstructed flux residues
chain              input CHAIN, reproduced byte for byte
links_sha256       SHA-256 over one raw byte per link residue
macrocycle         input MACROCYCLE
sample             input SAMPLE
schema             literal TWISTJ_Z5_LINK_STATE_V1
sha256             verified whole-file SHA-256 supplied by the caller
state_fingerprint  TWISTJ_FNVLIKE64_V1 over links followed by flux
```

Both fingerprints are exactly sixteen lowercase hexadecimal digits. The
historical field name `cache_fingerprint` does not authorize a cache input:
the reader reconstructs the flux before hashing it.

### 6.2 `flux`

The only key is `counts`. `counts[k]` is the number of plaquettes with residue
`k` in phase order `0,1,2,3,4`; it sums to `6*L^4`. Plaquette iteration is
site-major with pair order `(01,02,03,12,13,23)`.

### 6.3 `polyakov`

The exact key order is `directions,line_count`, where `line_count=L^3`.
`directions` has four entries in increasing `mu`. Each entry has exact key
order `mu,phase_counts`; `phase_counts[k]` counts direction-`mu` Polyakov lines
with holonomy `k` and sums to `L^3`.

These four five-bin histograms are the exact sufficient statistics for the
direction-wise quantities. With

```text
Z_mu = sum_k phase_counts[mu][k] omega^k,
Pbar_mu = Z_mu/L^3,
```

a later exact reducer reconstructs

```text
r = (1/4) sum_mu |Pbar_mu|,
u = (1/4) sum_mu Pbar_mu^5,
v = (1/4) sum_mu |Pbar_mu|^5.
```

There are deliberately no redundant serialized `r`, `u` or `v` objects.

### 6.4 `vortex`

The exact key order is

```text
charged_area, closure, components, global_charged_homology_f5,
homology_order, occupied_faces, support_size_tail_desc, wraps
```

`closure` is literal `"PASS"`. `charged_area` is the sum of absolute principal
flux coefficients, `occupied_faces` is the nonzero-support size, and
`homology_order` is `[` `"01"`,`"02"`,`"03"`,`"12"`,`"13"`,`"23"` `]`.
The global homology vector has six residues and must be zero for `F=dA`.

Components are sorted by increasing `anchor_face`, the least site-major,
pair-major primal face index. Each component has exact key order

```text
anchor_face, charged_area, charged_homology_f5, support_faces, wraps
```

`charged_homology_f5` contains six residues `0..4`; component `wraps` is true
exactly when this vector is nonzero, and configuration `wraps` is their OR.
`support_size_tail_desc` lists every component support size, with multiplicity,
in nonincreasing order. Empty support gives empty arrays and `wraps=false`.

### 6.5 `monopole`

The exact key order is

```text
charged_length, charged_length_tail_desc, closure, components,
current_count_order, current_counts, global_windings_z,
largest_support_over_volume, occupied_links, support_size_tail_desc, wraps
```

`closure` is literal `"PASS"`; `current_count_order` is literal
`[-2,-1,0,1,2]`; `current_counts` uses that order and sums to `4*L^4`.
`charged_length=sum_e |m_e|`, while `occupied_links` counts nonzero current
links. `global_windings_z` has four signed integers and must be zero for a
current derived from a periodic exact link state.

Components are sorted by increasing `anchor_link`, the least site-major,
direction-major dual-link index. Each component has exact key order

```text
anchor_link, charged_length, support_links, windings_z, wraps
```

`windings_z` has four signed integers; component `wraps` is true exactly when
this vector is nonzero, and configuration `wraps` is their OR. The two
`*_tail_desc` arrays list every component's size, with multiplicity, in
nonincreasing order. `largest_support_over_volume` is the unreduced pair
`[max_support_links,L^4]`; empty current uses `[0,L^4]`.

### 6.6 `correlator`

The exact key order is `n_max,terms`, with `n_max=floor(L/2)`. There are exactly
24 term objects. All twelve `plus` terms occur first, followed by all twelve
`minus` terms. Within each kind, order is increasing `rho` and then the fixed
plaquette-pair index, retaining only pairs incident on `rho` for `plus` and
only pairs transverse to `rho` for `minus`.

Each term has exact key order

```text
kind, pair, rho, separations
```

`kind` is `"plus"` or `"minus"`; `pair` is the integer array `[a,b]`;
`separations` contains ascending `n=1..floor(L/2)`. Each separation object has
exact key order

```text
count, left_counts, n, product_counts, right_counts
```

`count=L^4`. The three `*_counts` fields are five-bin nonnegative integer
histograms in phase order `0,1,2,3,4`; each sums to `count`. Their phase
definitions are the `C^+` and `C^-` definitions frozen in `PREREG.md`.

## 7. Output custody and block reduction

The formal verifier requires byte identity between the C++ record and the
independent Python canonical record, then checks the frozen expected digest of
the complete record and its correlator section. Its `state.sha256` binds the
record to exactly one manifest-owned input state. `SOURCE_SHA256SUMS` owns the
pinned source and fixture inputs; it is not rewritten by the reader. `RUN.md`
later owns the formal gate stdout digest. None of these custody checks adds a
line to the two-line terminal stdout.

A later deterministic reducer may add per-state histograms within complete
chain-preserving blocks. It must retain input JSON digests and exact integer
sums and must receive, not choose, the block length frozen by the production
analysis. It may not center a correlator per configuration, cross chain
boundaries, discard a complete accepted state or emit a phase label.

## 8. Rejection rule

There is no permissive parse mode. Any violation of this document, including
an unknown JSON key, wrong key order, wrong array order, noncanonical integer,
missing custody hash or inconsistent census, is `STOP_INTEGRITY`. A rejected
state produces no partial sufficient-statistic record.
