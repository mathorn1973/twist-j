# PROMO-C20-TEICHMULLER-SPLIT-1

**STATUS: NON-CANONICAL PROMOTION PROPOSAL.** This note has no authority,
changes no public status, edits no Canon ledger, and authorizes no probe or
formal execution. It freezes one exact L1 promotion proposal and the firewall
separating it from every time, decoder, and physical reading. A later,
separately reviewed and integer-versioned Canon fold may consume it.

## 0. Decision in one block

```text
proposal id             PROMO-C20-TEICHMULLER-SPLIT-1
public claim id         C20-TEICHMULLER-SPLIT
proposed status         T, never T-LOCK
proposed layer          L1
proposed section        1. The axiom and the two projections
evidence                 probes/P-C20-TEICHMULLER-SPLIT-2
only claim premise      J-STEP [T]
time row                TIME-QUANTUM-TOWER [C], unchanged and graph-separated
normative action now    none
next fold if consumed   Public Canon v17 -> v18
```

The proposed decision is deliberately narrow:

1. register the exact local-ring, order-20, `C_4 x C_5`, root-census,
   all-depth two-primary, and reduced-operator statement as one L1 theorem;
2. use only the repaired public probe `P-C20-TEICHMULLER-SPLIT-2`;
3. preserve `TIME-QUANTUM-TOWER [C]` byte-for-byte and add no dependency path
   in either direction;
4. add no all-`k` order, time, tick, clock, chronology, phase, decoder,
   physical-carrier, metrology, uniqueness, or L2-L6 reading;
5. do not consume or stage any private, untracked, predecessor, or all-`k`
   time-tower material.

## 1. Currency and public evidence

This proposal was prepared against:

```text
STATE              ACTIVE
Public Canon       v17
authority          mathorn1973/twist-j public main
tag                canon-v17
activation commit  b12a89315e6378464752b72ac5a484f1fa0c1ec5
content commit     f6d4c303b02a8791afc3ba82a81de5317c745ed0
Canon SHA-256      5be8d455a1ca9a1169d61035ab4c3bb722a72c566539b549c168b9bd3c01d368
Canon bytes        90363
registry counts    195 claims: T 99, D 40, C 22, H 5, O 20, F 9
ledger counts      211 items, 294 dependencies, 195 evidence rows,
                   673 history events, 9 gates, 8 programs
```

The repaired proof-first probe is public through PR #129. Its five files are:

```text
probes/P-C20-TEICHMULLER-SPLIT-2/EXPECTED.txt
probes/P-C20-TEICHMULLER-SPLIT-2/PREREG.md
probes/P-C20-TEICHMULLER-SPLIT-2/RESULT.md
probes/P-C20-TEICHMULLER-SPLIT-2/RUN.md
probes/P-C20-TEICHMULLER-SPLIT-2/verify.py
```

Their sorted bundle-manifest SHA-256 is:

```text
bca1d2850ed40871bc8304defca46ee33f84f31f71a7197b30dfdbc2ded4db90
```

This is the evidence hash for the future row. It is not the verifier hash
`5ba3680f...` and not the stdout hash `4cbf934b...`.

The formal Linux/aarch64 leg and GitHub Linux/x86_64 replay are byte-identical:

```text
prereg SHA-256       b5054f27c7c018f0f8b305b9d26c8f64e34f528e8729eb48d1b8ebfade28733c
verifier SHA-256     5ba3680f2cca840ab458e72e8a2f0febb99c732fcacaeadd68c71c020baacd41
stdout SHA-256       4cbf934b2220c5a5c3de8169a448baac1396236ebc37c286536c3886bb8d86e8
stdout bytes/lines   724 / 7
result               6/6 ALL PASS
GitHub workflow      run 29983108892, job 89129072266, success
```

The protocol-invalid `P-C20-TEICHMULLER-SPLIT-1` predecessor is quarantined
and is not evidence. Its known output may not be copied into the fold.

## 2. Exact proposed theorem

Let

```text
O       = Z[zeta_5],
lambda  = 1 - zeta_5,
A_m     = O/(lambda^m),  m >= 1,
R       = A_4 = O/(5),
J       = 1 + zeta_5^2.
```

The equality `R = A_4 = O/(5)` uses the ideal identity
`(5) = (lambda)^4` in `O`; it does not assert an element equality.
Each `A_m` is a finite local ring with residue field `F_5`, units exactly the
nonzero-residue elements, `|A_m| = 5^m`, and
`|A_m^*| = 4 x 5^(m-1)`.

In `R`, `lambda^4 = 0 != lambda^3`, and characteristic five gives

```text
J^5 = 2,   J^10 = -1,   J^15 = 3,   ord_R(J) = 20.
```

Put `t = J^5 = 2` and `u = J^16 = 3J`. Their orders are four and five,
`tu = J`, and their cyclic subgroups have trivial intersection. Therefore

```text
<J> = <t> x <u> isomorphic to C_4 x C_5.
```

Writing `zeta_5 = 1 - lambda` gives

```text
u - 1 = lambda(-1 + 3 lambda),
(u - 1)^4 = 0 != (u - 1)^3.
```

The kernel of `A_m^* -> F_5^*` is a 5-group. Therefore the Sylow
2-subgroup of every `A_m^*` maps isomorphically to the cyclic `F_5^*` and is
`C_4`; no `A_m` contains an element of order eight. In `R`, uniqueness of
lifts across the odd-order kernel gives the sharper census

```text
mu_8(R) = mu_4(R) = F_5^*,
```

with `F_5^*` embedded as the four nonzero scalar constants.

Finally, reduce the public integer `J-STEP [T]` operator modulo five. The
matrix `M_R` reconstructed from the four reduced `step(e_i)` columns agrees
with the independently reconstructed multiplication-by-`J` action on `R`.
It has exact order 20 and satisfies

```text
M_R^5 = 2I,
M_R^10 = -I,
M_R^16 = 3M_R,
(M_R - 2I)^4 = 0 != (M_R - 2I)^3,
(U - I)^4 = 0 != (U - I)^3,   U = M_R^16.
```

The all-`m` conclusion rests on the exact proof. The finite verifier audits
that proof and every finite claim in `R`; it does not extrapolate the
all-depth statement from its finite prefix.

## 3. Scope firewall

The proposed theorem is exact L1 arithmetic in the declared lambda-adic tower
only. It is not any of the following:

```text
an all-k order theorem for M_J modulo 5^k
a time quantum or physical tick
a clock, chronology, phase, or arrow-of-time statement
a decoder or physical-carrier construction
a metrology or SI scale
a uniqueness theorem or interpretation of another carrier
a claim about carriers outside the declared tower
a lift to L2-L6
```

`TIME-QUANTUM-TOWER [C]` retains its current finite-depth scope:

```text
on Z/5^k, k = 1 to 4 only; no all-k theorem
evidence: reproduce/foundations-places
```

It is neither a premise nor a consequence of the new theorem. The later fold
must leave its registry, normative, evidence, dependency, and history rows
unchanged and must add no direct or transitive path between the two claims.

The order-eight element of `PENTIT-ROOT-FACTS [T]` lives in the separate field
`F_25`, not in an `A_m`. That row is a consistency comparison, not a premise.
`FIB-ROOT-TIES`, `RAMIFIED-TM-LIFT`, and every decoder or metrology row are
also not premises.

## 4. Exact later-fold registry row

If consumed directly while v17 remains active, append this exact six-column
row to `canon/REGISTRY.tsv`:

```tsv
C20-TEICHMULLER-SPLIT	T	for O = Z[zeta_5], lambda = 1 - zeta_5, A_m = O/(lambda^m) for m >= 1, and R = A_4 = O/(5), where (5) = (lambda)^4 is an equality of ideals in O and not an element equality, A_m is a finite local ring with residue field F_5, the units are exactly the elements of nonzero residue, |A_m| = 5^m, and |A_m^*| = 4 x 5^(m-1); in R, lambda^4 = 0 != lambda^3, J = 1 + zeta_5^2 has exact order 20, and t = J^5 = 2 and u = J^16 = 3J give <J> = <t> x <u> isomorphic to C_4 x C_5 with (u - 1)^4 = 0 != (u - 1)^3; mu_8(R) = mu_4(R) = F_5^* embedded as the nonzero scalar constants, and for every m >= 1 the Sylow 2-subgroup of A_m^* is C_4, so no A_m contains an element of order 8; M_R = M_J mod 5, reconstructed from the public J-STEP columns, agrees with multiplication by J, has exact order 20, satisfies M_R^5 = 2I, M_R^10 = -I, M_R^16 = 3M_R, (M_R - 2I)^4 = 0 != (M_R - 2I)^3, and, for U = M_R^16, (U - I)^4 = 0 != (U - I)^3; L1 exact arithmetic only, with no all-k order claim for M_J modulo 5^k, time, tick, clock, decoder, physical carrier, metrology, uniqueness, or L2-L6 claim	1. The axiom and the two projections	probes/P-C20-TEICHMULLER-SPLIT-2	fires if the pinned evidence bundle or two-architecture transcript differs, if the ideal, locality, residue, cardinality, unit, order, split, nilpotency, root-census, all-m Sylow 2-subgroup, or reduced J-STEP statement in the frozen scope is false, if a nonconstant fourth or eighth root occurs in R, or if an element of order 8 occurs in any A_m; any all-k order modulo 5^k, time, clock, decoder, or physical interpretation is outside this theorem
```

The UTF-8 scope has SHA-256:

```text
4abf9303c8f796d9ff316d3e49bd6fae5d3551304b76503ae21e9f247842232b
```

## 5. Exact later-fold Canon text

In section 1, immediately after the public `J-STEP [T]` paragraph, insert:

```text
C20-TEICHMULLER-SPLIT [T], evidenced by
probes/P-C20-TEICHMULLER-SPLIT-2, is an L1 arithmetic theorem. Put
O = Z[zeta_5], lambda = 1 - zeta_5, A_m = O/(lambda^m), and
R = A_4 = O/(5). The last equality uses (5) = (lambda)^4 as ideals
in O; it does not assert 5 = lambda^4 as elements. Each A_m is local
with residue field F_5, its units are exactly the elements of nonzero
residue, |A_m| = 5^m, and |A_m^*| = 4 x 5^(m-1).

In R, lambda^4 = 0 != lambda^3. The characteristic-five identity gives
J^5 = 2, hence J^10 = -1, J^15 = 3, and J has exact order 20. With
t = J^5 = 2 and u = J^16 = 3J, the factors have orders 4 and 5,
J = tu, and <J> = <t> x <u> isomorphic to C_4 x C_5. Moreover
u - 1 = lambda(-1 + 3 lambda), whose second factor is a unit, so
(u - 1)^4 = 0 != (u - 1)^3.

At depth four, the kernel of R^* -> F_5^* is a 5-group. Therefore the
four nonzero scalar constants are exactly both root sets:
mu_8(R) = mu_4(R) = F_5^*. For every m >= 1 the kernel of
A_m^* -> F_5^* is again a 5-group, so the Sylow 2-subgroup of A_m^*
is C_4 and no A_m contains an element of order 8. The literal
scalar-root description is asserted only for R.

For the operator leg of C20-TEICHMULLER-SPLIT [T], reducing the four
public J-STEP columns modulo 5 gives M_R, which agrees with
multiplication by J. It has exact order 20 and satisfies
M_R^5 = 2I, M_R^10 = -I, and M_R^16 = 3M_R. Since M_R - 2I is
multiplication by -lambda(j + 1),
(M_R - 2I)^4 = 0 != (M_R - 2I)^3. For U = M_R^16,
U - I = 3(M_R - 2I), so (U - I)^4 = 0 != (U - I)^3.

The scope of C20-TEICHMULLER-SPLIT [T] is exact L1 arithmetic only.
The all-m unit-group result is not an all-k order theorem for M_J
modulo 5^k and does not strengthen TIME-QUANTUM-TOWER [C]. It supplies
no time, tick, clock, decoder, physical carrier, metrology scale,
unique interpretation, or L2-L6 lift.
```

Display-equation fencing and line wrapping may be applied mechanically in the
later Canon, but the mathematical wording and sentence-local claim labels are
frozen. The word `internal` must not enter a hashed Canon file.

## 6. Exact companion-ledger edits

### 6.1 NORMATIVE.tsv

Append:

```tsv
C20-TEICHMULLER-SPLIT	THEOREM	C20-TEICHMULLER-SPLIT	T	L1		canon/CANON.md::1. The axiom and the two projections
```

### 6.2 DEPENDENCIES.tsv

Append exactly one edge:

```tsv
C20-TEICHMULLER-SPLIT	J-STEP	REQUIRES	the reduced matrix leg reconstructs M_R from the four public J-STEP columns and identifies it with multiplication by J
```

`J-STEP [T]` is the only claim premise. Add no edge to
`DEF-ARCHITECTURE`, `TIME-QUANTUM-TOWER`, `FIB-ROOT-TIES`,
`RAMIFIED-TM-LIFT`, or `PENTIT-ROOT-FACTS`.

### 6.3 EVIDENCE.tsv

Append:

```tsv
C20-TEICHMULLER-SPLIT	EV-C20-TEICHMULLER-SPLIT	PUBLIC_PROBE	probes/P-C20-TEICHMULLER-SPLIT-2	bca1d2850ed40871bc8304defca46ee33f84f31f71a7197b30dfdbc2ded4db90	bundle-manifest-sha256-v1	two-architecture
```

### 6.4 HISTORY.tsv

For an immediate v17 to v18 fold on 2026-07-23, append:

```tsv
CANON18-DECLARE-C20-TEICHMULLER-SPLIT	1	2026-07-23	canon-v18	C20-TEICHMULLER-SPLIT	DECLARE	-	T	4abf9303c8f796d9ff316d3e49bd6fae5d3551304b76503ae21e9f247842232b	EV-C20-TEICHMULLER-SPLIT	probes/P-C20-TEICHMULLER-SPLIT-2	bca1d2850ed40871bc8304defca46ee33f84f31f71a7197b30dfdbc2ded4db90	The repaired public proof-first probe and byte-identical aarch64 and x86_64 transcripts establish the L1 ramified C20 split, root census, all-m two-primary theorem, and reduced J-STEP identities; no TIME-QUANTUM-TOWER, decoder, physical-carrier, or higher-layer claim is promoted
```

If another Canon release lands first, recompute the release number, event id,
date, base, counts, and all release-form values.

## 7. Count, generated-view, and reproduction effects

Starting directly from public v17, the expected delta is:

```text
claims                  195 -> 196
T                        99 -> 100
D                        40 -> 40
C                        22 -> 22
H                         5 -> 5
O                        20 -> 20
F                         9 -> 9
live H/O                 25 -> 25
NORMATIVE items         211 -> 212
DEPENDENCIES            294 -> 295
EVIDENCE rows           195 -> 196
evidence two-arch       117 -> 118
HISTORY events          673 -> 674
GATES                     9 -> 9
programs                  8 -> 8
reproductions            22 -> 22
```

The later content fold is expected to change exactly these 14 files:

```text
canon/CANON.md
canon/REGISTRY.tsv
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/CORE.md
canon/CHANGELOG.md
canon/STATUS_COUNTS.tsv
canon/SHA256SUMS
reproduce/status-separation/verify.py
reproduce/status-separation/EXPECTED.txt
reproduce/status-separation/README.md
tools/test_architecture_map_report.py
```

Before running the generator, relabel the v17 `GENERATED CURRENT COUNTS`
markers as `GENERATED CANON17 COUNTS`, insert the new v18 heading and its new
`GENERATED CURRENT COUNTS` block, and only then run
`tools/generate_canon_views.py --apply` and its check. With no live-row change,
`canon/FRONTIER.md` is expected to remain byte-identical and must not be staged
merely because the generator was run. `canon/GATES.tsv`,
`canon/FRONTIER_PROGRAMS.tsv`, and `canon/CORE_SELECTION.tsv` also remain
byte-identical.

The status-separation reproduction moves from 10 to 11 checks. Its new C20
check must require all of the following:

```text
C20-TEICHMULLER-SPLIT is T and L1, with Canon section 1 source
its evidence path is exactly probes/P-C20-TEICHMULLER-SPLIT-2
its exact scope contains the ideal boundary, locality, C_4 x C_5,
all-depth order-8 exclusion, and the negative all-k/time/L2-L6 firewall
J-STEP remains T
the only outgoing C20 dependency is J-STEP REQUIRES
TIME-QUANTUM-TOWER remains C at its current finite k=1..4 scope
TIME-QUANTUM-TOWER retains evidence reproduce/foundations-places
there is no direct or transitive dependency path in either direction
```

Update the architecture-map pinned counts to 196 claims, `T = 100`, and
`two-architecture = 118`. Evidence `none = 39` and direct architecture
requirements `162` remain unchanged.

Freeze the v18 changelog entry as:

```text
Canon v18 adds C20-TEICHMULLER-SPLIT [T] at L1 from the corrected public
proof-first probe P-C20-TEICHMULLER-SPLIT-2. It registers the finite-local-ring
model, the exact C_4 x C_5 split of the J-cycle in R, the complete root census
there, the all-depth C_4 two-primary conclusion in the declared lambda-adic
tower, and the independently reconstructed reduced J-STEP operator.
TIME-QUANTUM-TOWER [C] is unchanged and has no dependency edge to or from the
new theorem. No time, decoder, physical carrier, metrology, or L2-L6 reading
is added.
```

## 8. Later sealed-fold and release ceremony

This notes-only PR changes exactly this file. It creates no tag, release, or
Canon authority.

The notes-only promo PR must first merge, and this exact file must then be
read back byte-for-byte from public `main`. Only after that public readback
passes may a fresh v18 branch and worktree be created from the resulting
public `main`; no fold branch prepared before the promo merge is eligible.

Before the immutable content commit, the fresh fold must run at minimum:

```text
python tools/generate_canon_views.py --apply
python tools/generate_canon_views.py --check-dir canon
python -m unittest discover -s tools -p "test_*.py"
python tools/check_ledger.py
python tools/check_verifier.py --base <ACTUAL-FOLD-BASE>
python tools/check_reproduce.py --base <ACTUAL-FOLD-BASE>
git diff --check
```

After the content checks:

1. create one immutable content commit containing only the 14 expected files;
2. compute its full SHA plus the exact Canon SHA-256 and byte count;
3. create a separate release-form commit changing exactly `STATUS.md`,
   `README.md`, and `CITATION.cff`;
4. run `check_policy.py`, `check_canon.py`, and the full activation gate
   against the named content commit only after that exact three-file
   release-form commit exists;
5. push a dedicated PR and require the GitHub Ubuntu byte replay to pass;
6. merge by merge commit, never squash or rebase;
7. verify the public merge tree equals the reviewed release tree;
8. publish the annotated `canon-v18` tag with message `Public Canon v18`
   on that verified public merge commit;
9. require the tag workflow activation manifest;
10. create a draft release with exactly `activation-manifest.json` and the
    tagged `canon/SHA256SUMS`, download both back, compare bytes, then publish;
11. require the release-event asset readback workflow and final public
    main/tag/release readback to pass.

The content commit changes all six current `Public Canon v17` occurrences
in `canon/CANON.md` to v18. The separate release-form commit changes only:

```text
STATUS.md
README.md
CITATION.cff
```

In that release form, `STATUS.md` names the immutable content commit and keeps
`CUTOVER: 2026-07-13`; `CITATION.cff` records version `18` and
`date-released: 2026-07-23`.

## 9. Stop conditions, provenance, and security

Stop the promotion if any of these occurs:

1. the public `-2` bundle differs from the recorded five-file manifest hash;
2. the exact registry scope differs from its recorded SHA-256;
3. the ideal equality is rewritten as an element equality;
4. the order-20 claim is extended from `R` to every `A_m`;
5. `<J> ~= C_4 x C_5` is confused with the whole unit group `R^*`;
6. the scalar root census is extended beyond `R`;
7. nilpotency is asserted for the integer matrix `M_J`;
8. an edge or interpretation connects the theorem to time or decoder rows;
9. the invalid `-1` predecessor or untracked all-`k` material enters the diff;
10. a generated view, count, transcript, checksum, or public byte readback
    differs from its frozen expectation.

This proposal contains markdown only. It carries no executable artifact,
secret, credential, private hostname, private path, machine nickname, private
log, binary, model file, or personal data. It does not rerun any verifier.
