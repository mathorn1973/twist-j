# NON-CANONICAL: fold proposal for P-ENTROPY-RG-RETURN-1

This note is not canon. It proposes the exact edits a later sealed
integer-versioned fold would make after `P-ENTROPY-RG-RETURN-1` merges. It
changes nothing by existing, it edits no file under `canon/`, and it carries
no status of its own. Only a sealed public fold changes the Canon.

## Source

```text
probe:            probes/P-ENTROPY-RG-RETURN-1
pin_commit:       db57f52eddaaba2529c22a072014ba6db0ac06b6
verifier_sha256:  cb0e4a5b6dfed09b3d9c02ae68ce228f13ef5efdc4465a6b202eb00d44fd48b7
stdout_sha256:    b86e083d8f852642c939574b439f097c12a1bf10e595e2d016c1dcb466cdb0d9
legs:             aarch64 local, x86_64 required check, byte identical
earned status:    C at the declared finite range k = 0..14, both letters
```

## Proposed registry row

Schema is `claim_id  status  scope  canon_section  evidence  falsifier`,
tab separated, evidence a path.

```text
claim_id       ENTROPY-RG-RETURN
status         C
scope          for the renormalized block maps Phi^(0)_eps = F_eps and
               Phi^(k+1)_eps = Phi^(k)_(1-eps) o Phi^(k)_eps on the recurrent
               core, at every dyadic scale k = 0..14 and both letters: the
               fixed set is empty on the core and off it unless k = 0 or
               k = 1 mod 4; at k = 0 each letter has exactly one recurrent
               fixed state, the reflection centres 3 (C_D + V_E) and 3 C_D in
               the size-10 component, with 125 further fixed states off the
               core and multiplier exactly minus the identity; at k = 1, 5, 9
               and 13 the fixed set is exactly the opposite living half
               H_(1-eps), 3125 states meeting all 313 components, with
               multiplier exactly the identity at every one of them and
               off-core count 3125 at k = 1 and 0 at k = 5, 9, 13; the image
               of every block map on the core has 3125 states; the scales
               carrying a full-half return are exactly those with 2^k = 2
               mod 5, and no scale with 2^k = 1 mod 5 carries one; no
               continuum, scaling, exponent, monotone, measure or all-scale
               statement follows
canon_section  3. The kernel and the census
evidence       probes/P-ENTROPY-RG-RETURN-1
falsifier      fires if any gate of the pinned verifier fails on re-run, if a
               fixed state exists at any scale in range with k mod 4 in
               {0, 2, 3} and k > 0, if a return scale misses one state of its
               half or carries one non-identity multiplier, if an off-core
               count differs from the frozen value, or if the two
               architectures produce different bytes
```

## Proposed Canon paragraph, section 3

Prose only, no new claim beyond the row, and written to pass
`tools/check_canon.py`:

> The renormalized block maps are two-to-one on the recurrent core, so coarse
> graining is a semigroup. That semigroup has no hyperbolic fixed point at
> state level in the computed range. Outside two exceptional residues it has
> no fixed state at all, and where fixed states exist beyond the first scale
> they are a whole living half whose multiplier is the identity, so no
> expanding or contracting datum exists to be read from them. What the
> computation finds instead is a return: within the range the fixed-point
> data depend on the scale only through the residue of the block length
> modulo the prime, and the return happens exactly where that residue is two.
> Where the residue is one the map does not return. The agreement of that
> residue class with the order of the ramified digit unit of
> RAMIFIED-TM-LIFT is an arithmetic consonance and is recorded as one; no
> physical transfer is claimed and the computed row does not rest on it.

## Proposed accompanying edits

```text
ENTROPY-BLOCK-HALVING   note may gain a pointer: the fixed-point tower of the
                        same maps is ENTROPY-RG-RETURN, and the image
                        statement is re-audited there for k = 0..14
FRONTIER.md             regenerated only; no live H or O row closes or moves,
                        because the new row is closed at birth inside its
                        finite scope
CHANGELOG.md            one entry naming the probe and the row
SHA256SUMS              regenerated; the fold is sealed, integer versioned,
                        tagged, and STATUS.md is updated by the release form
```

## What the fold must not do

It must not widen the range beyond `k = 14`, must not restate the row as an
all-scale law, must not attach a monotone scale function or a C-function to
it, must not read the residue class physically, and must not let any summary
exceed status `C` or the declared scope. The missing monotone object of a
coarse-graining theorem stays open and is not addressed by this row.
