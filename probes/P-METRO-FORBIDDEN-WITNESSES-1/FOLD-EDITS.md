# FOLD EDITS. P-METRO-FORBIDDEN-WITNESSES-1, CANONICAL branch

The owner ratified the five frozen readings as the meaning of the five
forbidding phrases of section 15, so the CANONICAL branch applies. These are
the exact edits a later sealed fold would make. This probe makes none of them.

Anchors verified present exactly once at the pinned basis, Public Canon v56.

## 1. canon/REGISTRY.tsv, one new row

The row is in `FOLD-ROWS.tsv` beside this file, six tab-separated fields.
Insert after the METRO-REDUCTION-CALCULUS row.

## 2. canon/REGISTRY.tsv and canon/FRONTIER.md, the parent clause

One occurrence in each file. Replace

```text
obligation B, the complete forbidden-transformation catalogue with exact witnesses
```

with

```text
obligation B, the complete forbidden-transformation catalogue with exact witnesses, discharged for the five entries section 15 names by METRO-FORBIDDEN-WITNESSES, whose one frozen reading per entry is the ratified meaning of those five phrases, with any further entry still open
```

The parent keeps status O, keeps STOP, and keeps its falsifier, because
obligations D and E are untouched.

## 3. canon/CANON.md, section 15

Insert this paragraph between the METRO-REDUCTION-ARROWS paragraph and the
METRO-REDUCTION-CALCULUS paragraph:

```text
METRO-FORBIDDEN-WITNESSES [C], evidenced by the immutable
`probes/P-METRO-FORBIDDEN-WITNESSES-1` bundle, exhibits an exact functional
obstruction for each of the five forbidden entries above. An obstruction is a
pair of positions with equal pointwise L5 stream whose transported values
differ, so it excludes every output transport `tau` at once rather than one
family of them, and none of the five is an admissible arrow. Each entry is
read minimally and typewise, one ratified reading per phrase: flattening is
loss of the named `N^a` product structure, not a faithful encoding that
transports it; erasing names is forgetting which coordinate a digit-word
action belongs to, not a coordinate permutation that carries the names,
bases, maps and boxes with it; arbitrary factor weights are new relative
weights of the geometry factors, not the exact rational output transport
`tau_R` a reduction arrow already licenses; output-dependent regrouping is
regrouping by output already obtained, not the Nerode quotient, which the
same section admits under its congruence precondition; and replacing boxes by
an unrelated ordering is discarding the canonical box geometry, not the box
transport an admitted coordinate permutation induces. Read broadly instead,
each of the last two phrases would make one admitted arrow forbidden as well,
which the parent's own falsifier excludes. The five witnesses have at most
four states and are checkable by hand. Across the two frozen boxes of 2,304
and 19,683 tuples the obstructing counts are 16,140 for flattening, 18,666
for erasing names, 12,702 for factor weights, 9,072 for output regrouping,
and 13,116 for box reordering, out of 21,987; the four admitted arrows
exhibit zero obstructions across both boxes under their own exact
preconditions; and every obstruction survives reading the composition in the
opposite order. This is computation at a declared finite range, so the result
is C, not T. Obligations D and E are untouched and
METRO-REDUCTION-CALCULUS [O] remains open and STOP.
```

Then, in the METRO-REDUCTION-CALCULUS paragraph, replace

```text
complete exact witnesses for the forbidden catalogue;
```

with

```text
exact witnesses for any forbidden entry beyond the five section 15 names, the ratified reading of those five having been discharged by METRO-FORBIDDEN-WITNESSES;
```

## 4. Version and hashes

Any change to a hashed canon file is a version-incremented fold: a CHANGELOG
entry, canon/SHA256SUMS regenerated for all five files, STATUS.md updated with
the new TAG, CONTENT_COMMIT, CANON_SHA256 and CANON_BYTES. Integer versioning
only. Merge without squash or rebase. Commit as
`A. M. Thorn <thorn@twistj.com>`.

## 5. Traps, verified

```text
1  Never write an incubation candidate id into CANON.md, CORE.md or
   FRONTIER.md. tools/check_canon.py reads C-<NAME> as a status-C token for an
   unregistered claim and fails. The strings used above are safe.
2  Add no FRONTIER.md list item for the new row: list items must be H or O.
3  The registry evidence field is checked to exist on disk, so the probe
   directory and the registry row must land in the same fold.
4  The hashed canon files reject the words sealed, internal, private, hidden
   and unpublished. The prose above avoids all five.
5  Editing a hashed canon file without regenerating canon/SHA256SUMS fails
   immediately. Step 4 is a gate, not bookkeeping.
```
