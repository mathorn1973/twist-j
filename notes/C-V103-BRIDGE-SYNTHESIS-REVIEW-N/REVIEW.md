# RZ disposition: package accepted for review closure, no status change

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Reviewer: `Claude-v103-RZ-20261017`, public claim #1572.

**Disposition: ACCEPT as a complete notes package; one sequencing finding;
no scientific status changes.** Synthesis head
`2a3250932553c1c36e88c48f0aa0d2f69f99f2b6` (PR #1571, claim #1569) meets
its own frozen contract and the repository's operational requirements. The
independent break attempt found no counterexample to any of the twenty rows
of `CLAIMS.tsv`. Every candidate label stays a candidate. Public Canon v102
is unchanged. The merge is the author's decision.

## 1. Authority intake

Fresh clone of `mathorn1973/twist-j`; no attachment, mirror or rendered
page was used. `STATUS.md`: STATE ACTIVE, CANON Public Canon v102,
AUTHORITY `mathorn1973/twist-j main`, TAG `canon-v102`, CONTENT_COMMIT
`b04e22dd3ed8e4240cff347364f24670d4183a4d`, CANON_SHA256
`c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1`,
CANON_BYTES 1024033. `main` is `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`,
the commit the annotated tag `canon-v102` (object
`5ffacfe5e13622f51460d274c9591a28ef37358d`) points to. CONTENT_COMMIT and
the tag commit are ancestors of `main`. `sha256sum -c canon/SHA256SUMS`
from the repository root: 5 of 5 OK. `canon/CANON.md` matches the declared
hash and byte count. `git ls-remote --heads origin` was scanned: the only
branch on the synthesis lane is `notes/C-V103-BRIDGE-SYNTHESIS-N`; no
review branch or issue for it existed before #1572.

## 2. Package checks on the synthesis head

Three commits, all `A. M. Thorn <thorn@twistj.com>`, all descending from
`main`:

```text
c8485301  notes: freeze v103 bridge synthesis scope (#1569)          5 specification files
c0f637d4  notes: synthesize reviewed v103 residue bridge ...         6 result files
2a325093  notes: clarify completed synthesis review coverage (#1569) ACCEPTANCE.md, RESULT.md
```

Diff against `main`: eleven new files, all under `notes/`, 1892 lines
added, no existing file changed. Nothing under `canon/`, `probes/`,
`tools/` or the workflow is touched. The five specification files
(README, CONTRACT, PREREG, SOURCES.tsv, INPUTS.sha256) have identical blob
ids at the specification commit and at the head. The third commit changes
only the two result files, and only the sentences describing which helper
checks were completed; the contract permits result wording to be refined.

Repository validators on the head tree:

```text
check_policy.py         POLICY PASS
check_canon.py          CANON PASS v102 claims=523
check_ledger.py         LEDGER PASS claims=523 items=587 dependencies=1083 evidence=523 history=1070 gates=26 programs=7
check_gate_contract.py  GATE CONTRACT PASS gates=26
check_status_labels.py  STATUS LABELS PASS
```

Public-safety scan of the eleven files: no secret, credential, address,
hostname, machine nickname or coordination-surface reference; no non-ASCII
byte, no trailing whitespace, no CRLF. Three of the authority words that
`tools/check_canon.py` rejects in hashed Canon files occur in the synthesis
PREREG and ACCEPTANCE, in ordinary English senses, in unhashed notes, where
the check does not apply. The proposed Canon passage
`notes/canon/V103-BRIDGE-PROPOSAL.md` is clean against both lists of
`tools/check_canon.py` (the forbidden-phrase list and the authority-word
pattern), so a future fold would not fail on wording.

Custody: `custody_check.py` materialized every one of the 165 Git rows of
the synthesis `SOURCES.tsv` from its named commit and compared blob id,
SHA-256 and byte count; 165 of 165 agree, and `INPUTS.sha256` agrees on all
170 rows with no extra row. The five receipt rows (comment bodies) were not
re-hashed; the synthesis itself classifies them as mutable observations,
not evidence.

CI on the head, read from the runs and jobs API: run 38980352387, event
`pull_request`, attempt 1, conclusion success; `architecture-x86_64`
success, `architecture-aarch64` success, `check` success, `publication`
skipped (correct for a pull-request event). The synthesis session
identifier follows the established public practice of this repository
(ten such identifiers already on `main`).

## 3. Independent break attempt

`break_bridge_synthesis.py` was written from the Public Canon v102
definitions (native generators and selector at the "Native two-message
reading contracts" section, field marking and image criterion at "Shared
proof 2", contact section `eta` and `S`), then compared with the
definitions displayed in `SYNTHESIS.md`; they agree. Standard library only,
`int` and `Fraction`, no float. 104 checks, 0 failures; exact stdout in
`break_bridge_synthesis.stdout.txt`.

What was verified, and by which method:

- Degree-two identities on the grid `{0,1,2}^4`, which determines a
  quadratic polynomial in four variables, hence proofs:
  `4H=Q+(2c+2a-b)^2+(2d-a+3b)^2`, `2Q=5a^2+(a+2b)^2`,
  `3Q=5b^2+(3a+b)^2`, the four-square identity of B quoted in ACCEPTANCE
  RB4, `H(Wy)-H(y)=a^2-b^2+ac-bd`, `h1+h2=2A+B`, `h1-h2=2C+D`, and the
  literal `H` against `y^t B_f y/2`.
- Inherited matrix identities recomputed exactly: `A_f^5=I`,
  `sum A_f^j=0`, `A_f^t B_f A_f=B_f`, `L=(I-A_f)(I-A_f^2)`, `det L=25`,
  `L^2=5A_f^3`, `V_inv=A_f^2 L`, `V_inv L=L V_inv=5I`, `L^t B_f L=5B_f`,
  `B_f` positive definite by exact leading principal minors, `H(Lu)=5H(u)`.
- Residue sets over all 625 classes: image of `L mod 5` equals the
  criterion set equals `G_L`; `W(K)=G_L`; `K` and `G_L` meet only in zero;
  `ker(L mod 5)=G_L`, so `ker(pi_L)=LZ^4`; `A_f` acts on `G_L` as
  `(s,t)->(s+t,t)`; the fixed subgroup is exactly
  `{(0,0,0,0),(1,2,0,0),(2,4,0,0),(3,1,0,0),(4,3,0,0)}`.
- Unit shell: both bounding boxes derived from the two completions
  (`|a|,|b|<=1`, `|c|<=2`, `|d|<=3`; and `|a|,|b|,|c|<=2`, `|d|<=4`) lie
  inside the enumeration box `[-6,6]^4`; exactly 20 units; fibers
  `4+8+4+4`, none at `+-(1,1)`; no nonzero vector with `H<=0`.
- The `20+5` classification by brute force, including the two proof
  steps checked without Cauchy-Schwarz: `pi_L` injective on the 20 units,
  image equal to `G_L` minus the fixed subgroup, the difference of two
  distinct units never in `LZ^4`, and `A_f u-u` never in `LZ^4` for a unit.
- Native dynamics over all 15625 checkpoints: each `g_j` an involution;
  the four displayed `h(g_j x)` relations; no `h`-only law for `g0` and
  bijectivity of `p->(h(p),h(g0 p))`; `|G0|=625`, `|X14|=6250`,
  `|G0 cap X14|=250`; selection on `X14` uses only `g1,g3,g4`;
  `T_t(G0 cap X14)=G0 cap X_(4+2t)` with image 125 and exactly two
  preimages per target; `T_0` fixes only `(1,3,4,2,1,3)` and `T_1` only
  `(1,3,4,2,3,3)`; zero and nonzero `h` are preserved on `X14`.
- Zero orbit: `x0=x1=0`, `x2=(2,1,2,1,1,0)`, `x3=(0,0,1,3,1,1)`,
  `x4=g1(x3)=(4,2,0,0,4,4)` with `theta3=0`, `z3=1`; `h(x_n)=0` and
  `z(x_n) in {1,4}` for all `n<=2^16` as a finite witness to the
  induction; `rho3=(0,0,3,1)` outside the fixed subgroup;
  `rho4=(2,4,0,0)` inside it and in no unit image. Three-step
  synchronization: each initial trace sheet maps bijectively onto `X_1`;
  625 initial checkpoints gated at boundary 3; 125 distinct gated targets.
- Coset minimum: within `[-6,6]^4` the least `H` on the coset of
  `(0,0,3,1)` is 5, attained only at `(0,0,-2,1)`; the next value is 10.
  `Lu*=y*`, `H(u*)=1`, `V_inv y*/5=u*`, and `u*=(0,-1,-1,2)` is the only
  unit of residue `rho3`. The global lower bound rests on `H(y)=5H(u)` and
  `H(u)>=1` for nonzero integer `u`, which follows from positivity and
  integrality and was checked independently of the synthesis text.
- ACCEPTANCE arithmetic: `H(e0)=2` (RB1); `(L^t L/5)[0,0]=7` while
  `B_f[0,0]=4` (RB3); `(I+A_f)(0,0,1,0)=(1,0,0,1)` with `H=2`, not 3
  (RB8); RB's displayed expansion equals 4 while the correct substitution
  gives `3+1+4-1-6=1` (RB9). The central proofs of sections 3.2 to 3.4
  were re-derived without any of RB1 to RB8.
- Preparation families, simulated for `2^13` steps under the
  Thue-Morse driver. Original family: prefix gate values exactly as
  displayed; `x2=x0` because `g2` is an involution; no gate point on any of
  the 25 orbits; support 22 per orbit (2 prefix states plus a 20-point
  tail), 25 pairwise disjoint tails, total 550; the tail parametrization
  (`s,z in {1,-1}`, `B=0`, `C=sz lambda`, `D=sz mu`, `r=z-s-q`,
  `h=s(1+zk,1-zk)`) holds at every tail point; all 25 quotient histories
  `(z,q,r)` coincide; at every fixed `n<64` the full piston separates the
  25 pairs while `h` takes exactly five values. Alternative family:
  `q0=3lambda+mu+4`, `r0=2lambda+3mu+3`; prefix values as displayed; the
  single gate point is `(lambda,mu)=(2,0)` at `n=1`, checkpoint
  `(2,1,2,1,1,3)`; support 150 = 100 tail + 50 prefix; the tail
  parametrization holds; the initial `(q0,r0)` separates all 25 pairs.
  One-shot: prefix `h` is `(2lambda,-2lambda)`, `(lambda,-lambda)`,
  `(lambda,-lambda)` and the tail `h` is `(-2Bz lambda,2Bz lambda)`; the
  gate holds iff `lambda=0` at every simulated time; every tail state lies
  in the 100-state ready graph, where `3-BzD` reads the payload and exactly
  20 states have `h=0`; the five occupied quotient histories coincide;
  absence never passes and `h1+h2` never vanishes; absence and occupied
  controls differ at `n=2` and agree from `n=3`. The five quotient
  restrictions of the generators hold, and the original family starts at
  `Q=(2,0,1)`.
- Optional five-cell comparison: characteristic polynomials, exact
  orders 4, 3, 6, 5 and infinite (cap 60), definiteness, the semidefinite
  case with nullity one, the Jordan chain `A^n w=(-1)^n(w-nv)` for
  `n<12`, and the face-reversed mixed cell giving exactly `A_f`.

Not computed, and why: the complete-receiver noninterference theorem of
section 5 depends on a full receiver that is not defined as code in this
package; its premises are stated explicitly (common complete initial
receiver, common source-independent protocol, source drawn only from
`(q,r)`), its conclusion is determinism by induction, its quotient-history
step is verified above, and the injectivity of `S` follows from the Canon
definition `Sz(y_i)-Sz(y_4)=z_i`. The completeness of the family supports
(550, 150) is an inherited theorem; the simulation is a finite consistency
check, not a new proof.

Section 3.4 quantifier: the statement "there is no sequence
`(u_n)_(n>=3)` of units with `Lu_n mod 5=W pi_P(x_n)` for every `n>=3`"
follows from the single boundary `n=4` and is stated exactly that
modestly. The synthesis extends it nowhere.

Side observation, a computed witness and not a claim: on the zero orbit
the residue `W pi_P(x_n)` lies in the fixed subgroup first at `n=4` and
then at `n=6,10,16,18,24,28,30,...`; among `3<=n<=2^16` this happens
exactly 16384 = `2^14` times. It is one run without a preregistration or a
falsifier; any hypothesis built on it must earn its own pin.

## 4. Findings

**RZ1 (sequencing, not blocking review closure).** None of the eight
source lanes is in `main`. The result heads of A, RA, B, RB, C, RC, D and
RD are not ancestors of `main`; `probes/` and `notes/` on `main` do not
contain their directories; the registry has no row for them. Their pull
requests #1555, #1556, #1557, #1558, #1562, #1563, #1566 and #1568 are
open. The synthesis therefore rests on pinned but unmerged public work,
and the package does not say so: "inherited" in `CLAIMS.tsv` covers both
the v102 identities, which are canonical, and source-lane content, which
is not. Consequence: a fold of the proposed passage into the Canon is
possible only after the source probes are merged, each by its own
one-probe pull request; otherwise the Canon would cite evidence absent
from `main`. One sentence in `ACCEPTANCE.md` (a result file, not a pinned
specification file) would close the gap.

**RZ2 (outside reach).** The five receipt rows of the synthesis manifest
were not re-hashed by this review; the synthesis itself does not rely on
them as evidence.

**RZ3 (none).** No counterexample to any of the twenty `CLAIMS.tsv` rows
within the ranges stated above. The nine RB exclusions and the eight D
corrections are arithmetically correct, and the central proofs depend on
none of the excluded statements.

## 5. Audit run record

```text
command:      LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 -I break_bridge_synthesis.py
platform:     Ubuntu 24.04
architecture: x86_64
python:       3.13
exit code:    0
stderr:       empty
stdout:       6437 bytes, sha256 96e9ccb8035804b4d562707eddb92d33fdf9bf1bc89412cd2517c6cc44a52d8d
script:       24953 bytes, sha256 645d5b805017a2b749e5a6b21fbd172968ac0e4f64b0f2c12f57942ab8007e5e
wall time:    under 2 seconds
exposure:     result-exposed; script written after reading the synthesis
pin:          none before execution; script and stdout committed together
```

An earlier form of the same script, differing only in two dead lines and
the docstring, produced byte-identical stdout on the same machine. The
stdout is a one-architecture audit witness. A second architecture would
make it a reproduction, not a theorem; the theorems in the synthesis are
carried by its written proofs, which this review re-derived.

## 6. Pins

```text
twist-j main             a632c6a162dc87e60104d7a478e7650a6d5c4a1b
synthesis head           2a3250932553c1c36e88c48f0aa0d2f69f99f2b6
synthesis spec pin       c8485301e1d72e6e47159d8f66b3a1a12a920477
synthesis CI run         38980352387 (x86_64 and aarch64 success, check success)
```
