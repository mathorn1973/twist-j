# Prospective replay of the received RECON archive

**NON-CANONICAL / no authority / L1 / exposed-input replay.**

Owner: A. M. Thorn / codex-zero-root-20261125, reservation #2097.
This is a bounded supplement to C-J-ZERO-ROOT-N, not a public probe or a
new claim of blind confirmation. This protocol and its new wrapper must
be committed, pushed and read back before their first execution.

## Basis and prior exposure

Public Canon v117 remains the basis. Main and tag canon-v117 resolve to
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed; the content ancestor is
d65e32c4b8e9a14496d3b7aba46fc384f51f81dc. The five normative hashes were
read back again. CANON.md has 1624192 bytes and SHA-256
93a8d0c17ed88d93a62b56c44d65b6903c980654f7e5ea82da7e363a510a22a9.
The existing candidate parent is
9281f28bba27e94795794e21a70b270d9f521c76.

The owner has now supplied twistj-recon-2026-11-25.tgz as a conversation
attachment. It is a reference, not Git authority. Its 36076 bytes hash to
137a48e98c1643fdc0fa6134279778333e2a7044dae68b529a7f5b8c8f43aa5d.
[ARCHIVE-MANIFEST.tsv](ARCHIVE-MANIFEST.tsv) records the exact 29 regular
members; four directories complete the 33-member tar inventory. The
uncompressed regular files contain 167165 bytes. The wrapper checks all
member names, sizes and hashes before extracting its eight reviewed source
dependencies. It neither edits the received archive nor publishes it.

The owner reports that the original exploration was not preregistered.
All archived outputs, later numerical claims and both witnesses below
have already been exposed. Three same-session Astra/Sol helpers inspected
sources statically, without executing them. The present pin is prospective
only for this new replay. It cannot repair the original chronology, turn
reproduction into independent confirmation, or establish an external author.

## Equation, carrier and interface

The native carrier is the canonical counter times F_5^6 with coordinates
(p1,p4,p1p,p4p,q,r), the five unchanged native generators and selector
(sum(state)+2*popcount(n)) modulo5. Counter origin is zero throughout.
The received A and C sources were compared statically with those formulas.

For a source pair S of free pistons, the receiver is the complete complement,
including q,r, in one common source-independent preparation. Source masks
3,6,9,12 are crossing pairs; 5 and10 are same-index pairs, using bits0..3
for p1,p4,p1p,p4p. Equality is literal equality of receiver tuples, or of
ordered tuples of observations for a history. All 25 source messages and
all 625 common receiver preparations are included for each pair.

The separate contact carrier is O=Z[j], j^5=1 with its cyclotomic relation,
rho=j^2, J=1+rho, phi=-j^2-j^3 and sqrt5=2phi-1. A contact fixes the pair
unless its difference lies in 2O; on an admitted pair it preserves the
midpoint and multiplies the half-difference by rho. This is the canonical
integral contact law, not a complete step of native U. Received B forms
are reconstructed definitions, not recovered earlier author definitions.

## Frozen runs and acceptance conditions

Run from a clean copy of the pinned new wrapper and manifest:

```text
python3 -I -B notes/C-J-ZERO-ROOT-N/archive_replay.py ARCHIVE NEW_OUTPUT_DIRECTORY
```

ARCHIVE is the unchanged attachment with the hash above. The new output
directory must be outside the Git checkout and must not exist. The wrapper
accepts CPython 3.12.14 on Linux x86_64 and GCC14.2.0. It passes a minimal
environment and uses explicit reviewed sibling imports under -I -B.
There is no network operation or credential access in the reviewed code.
The archive's private working-path examples are not used.

| Stage | Exact scope | Limit | Acceptance |
| --- | --- | --- | --- |
| Compile | gcc -O2 -std=c99 -Wall -Wextra on unchanged C/enum_splits.c | 30s | GCC14.2.0; exit0; no diagnostics |
| B | Unchanged B/verify_B.py | 120s | Exit0, empty stderr, byte identity with B/verify_B.stdout |
| C32 | enum_splits 0 32, all 62 nonempty proper splits of six coordinates | 120s | Byte identity with C/splits_n0_T32.txt; exactly masks1..62 once each |
| C-matrix | Unchanged C/break_splits.py with the newly produced complete C32 table | 600s | Byte identity with C/break_splits.stdout; exit0 and empty stderr |
| Early cuts | enum_splits 0 3 MASK 1 for masks3,5,6,9,10,12 | 60s per mask | Exactly 625 preparations and cuts0..3 each; all crossing histories at cuts1,2 have25 classes; current maxima17 crossing and9 same-index; same-index histories never exceed9 |
| A-million | Unchanged A/check_A.py 1000000 | 600s | Byte identity with A/check_A.stdout; exit0 and empty stderr |
| A125 | Unchanged A/analyze_exact_A.py with the received exact_t3_list.txt | 120s | Exactly125 distinct valid list rows; all 25 messages per row through cut200 pass its assertions |
| Witnesses | New short adapter reusing received motor_A.py and oring.py | 30s | Both exact witnesses below, exit0 and empty stderr |

The C-matrix script's own comparator does not ensure that the comparison
file contains all 62 rows. The wrapper checks that property before any
scientific execution and again on the new C32 output. No change to the
received comparator is concealed. Its tail enumeration ends at4096;
all-time conclusions use the separately written RECON-REVIEW proof.

A125 confirms the listed preparations, not completeness of the search
over 5^12 affine preparations. A-million checks all 25 E trajectories to
one million ticks and all 15625 raw starts to cut200. Its target pair is
entered as a formula, not independently recovered from cyclotomic traces.
The infinite-time claims remain separate written arguments.

Two exposed witnesses are fixed in advance:

1. E(3,0) at cut3 and E(2,4) at cut28 both have complementary receiver
   (p4,p4p,q,r)=(4,0,4,2). Their correct PRESENT outputs are respectively
   (4,0) and(0,1). A receiver-only, counter-free function cannot return both.
2. For w=sqrt5*(J-Jbar), reference -5phi and initial cell2, input x=w+4
   admits the overwrite but has mark-J=(1-rho)^2=(0,-1,-3,-1) in the
   (1,j,j^2,j^3) basis. This is nonzero modulo5. The overwrite predicate
   must not be confused with literal mark equality to J.

Every scientific stage uses exact integers. Any nonzero exit, stderr,
timeout, byte mismatch, missing coverage or failed assertion stops the
sequence and remains recorded. A timeout or custody defect supplies no
scientific conclusion. No threshold, horizon, original source byte or
expected output is changed to obtain a pass. Unrun stages are not claimed.

## Exclusions and custody boundary

The full 5^12 A/select_A.c search, A/subclass_A.py, C/layer_pairs.py,
C/coset_check.py, C/late_cut_capacity.py, C/driver_bfs.py, n0_scan.txt
and X/cross.py are statically reviewed only in this supplement. T96 and
late-window tables are received artifacts, not separately rerun here.
X shares A's implementation and is not counted as an independent motor.

The archive contains no original licence declaration, reliable author
signature, preregistration, execution pin, runtime receipt or original
stderr/exit record. Original source and raw logs are not added to the
public repository under an assumed licence. Only this newly authored
wrapper, manifest and commentary use the repository's Apache-2.0 terms.
Replaying owner-supplied references is distinct from publishing their code.
An original-source publication requires resolved permission and provenance.

The archive does not contain the reported 25-cell construction, its
preparation list or executable test. It also lacks the latest corrected
RECON note and its new recheck script. The first zero-root audit's missing
note, author and scripts in PROVENANCE.md are a separate unresolved intake;
this RECON archive must not be substituted for them.

Local results will be recorded as candidate-C, with written arguments
remaining candidate-T only at their declared scope. A new authored review
will identify the public pin, wrapper/manifest hashes, exact output
hashes, return codes and limitations. Raw local execution files remain
outside Git. This single x86_64 replay does not meet a two-architecture
scientific gate. Ordinary repository CI and same-session review do not
change that. No Canon, registry, gate, workflow or sealed probe is edited.
