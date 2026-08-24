# ERRATUM: SHA256SUMS.txt path entry

Status: **NON-CANONICAL. DISCLOSURE RECORD.**

This erratum records a path defect in the integrity manifest of this bundle.
No bytes are in question and no evidence is missing. The manifest is not
rewritten; the defect is disclosed instead.

```text
recorded      2026-08-24
basis         Public Canon v62, mathorn1973/twist-j main
              ec810acad66ab73631fdfa7e582043e7363eb435
bundle        notes/C-READ-REDUNDANCY-1/
manifest      SHA256SUMS.txt
```

## 1. The defect

From the bundle directory, `sha256sum -c SHA256SUMS.txt` reports 8 entries
`OK` and one `FAILED`:

```text
sha256sum: PROMO-C-READ-REDUNDANCY-1.md: No such file or directory
PROMO-C-READ-REDUNDANCY-1.md: FAILED open or read
```

This is a **failure to open**, not a hash mismatch. The manifest names the
entry as a sibling of itself, and no such sibling exists.

## 2. The file is not missing

The named file exists in the repository, one directory across, and its bytes
match the manifest exactly:

```text
manifest asserts   b433c48d831c79adf3b3c1970286f8eef496f946ea67f887027afde9ef0318a7
                     PROMO-C-READ-REDUNDANCY-1.md
actual file        b433c48d831c79adf3b3c1970286f8eef496f946ea67f887027afde9ef0318a7
                     notes/canon/PROMO-C-READ-REDUNDANCY-1.md
```

The hash is byte-exact. Nothing was lost, altered, or withheld.

## 3. Why the file is where it is

The placement is correct and the manifest is what is wrong. `POLICY.md`
section 5 requires that a proposed Canon patch live under `notes/canon/`
until a separate sealed public fold applies it. `PROMO-C-READ-REDUNDANCY-1.md`
is exactly such a proposal, and the landing commit `ec3fc0f` created it at
`notes/canon/PROMO-C-READ-REDUNDANCY-1.md` in the same commit that created
this bundle. It has never resided in this directory.

The manifest, and the reading-order list in `MANIFEST.md`, were both written
as though the proposal were a bundle sibling. Recorded as a relative path the
entry would have read `../canon/PROMO-C-READ-REDUNDANCY-1.md`.

## 4. Disposition

```text
DONE      this disclosure record
NOT DONE  no edit to SHA256SUMS.txt
NOT DONE  no edit to MANIFEST.md
NOT DONE  no file moved; the proposal stays under notes/canon/ per POLICY.md 5
NOT DONE  no status, scope, registry, frontier, gate or Canon change
```

To verify the bundle completely, check the eight local entries in place and
check the ninth against `notes/canon/PROMO-C-READ-REDUNDANCY-1.md`:

```text
cd notes/C-READ-REDUNDANCY-1 && sha256sum -c SHA256SUMS.txt
sha256sum notes/canon/PROMO-C-READ-REDUNDANCY-1.md
```

Both together account for every entry in the manifest.
