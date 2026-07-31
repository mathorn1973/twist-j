# ADOPT-COIN-MINIMAL-READ

**STATUS: NON-CANONICAL OWNER DISPOSITION. NO PROBE RUN. NO CANON
CHANGE.** This note has no normative authority and changes no claim, gate,
frontier, count, hash, tag, release, or status. It records one candidate input
for a later, separately sealed Public Canon v27 fold.

```text
candidate queue       issue #199
public base           Public Canon v26 ACTIVE
base main             48213275d0ace92d8f034166179a9fee4d53d908
tag                   canon-v26
content commit        138eec5b22a823469e1fa651505815a3d5b36761
Canon SHA-256         3a62711e30b1f3e9c4ade71533354fdf669266f60f4a57ade84e31a8f2878cfd
Canon bytes           141941
owner decision        adopt MINIMAL-READ
named counter         MAXIMAL-REACH, not adopted
future H identifier   COIN-MINIMAL-READ
future O identifier   MINIMAL-READ-DERIVATION
action boundary       L1 dictionary with an unresolved L5-to-L1 route
public evidence       none yet
formal execution      none
provisional release   Public Canon v27, only after public evidence merges
```

The eventual fold must start from the then-current public `main`. The tuple
above is the currency stamp for this disposition, not permission to reuse
stale release fields. Release identifiers, dates, hashes, counts, topology,
and exact path deltas must be recomputed when the owner seals the v27
manifest.

## 1. Owner decision

Adopt `MINIMAL-READ` as the name of the coin-selection premise. Record
`MAXIMAL-REACH` as its honest counter-selector and do not adopt it.

The intended reading is:

```text
MINIMAL-READ    among the complete frozen class of integer-admissible
                alternator coins, select the coin that minimizes both the
                generic covering multiplicity of the composed velocity read
                and the worst-case constant in the uniform ergodic read

MAXIMAL-REACH   select the admissible coin with the largest coherent range
```

The future dictionary choice is `beta_1 [H]`, not `T` or `D`. The mathematical
ranking of the admissible coins can be theorem-grade while the choice of
which ranking the dictionary adopts remains a premise. This note adopts the
premise but supplies no public theorem and therefore cannot add the H row to
the current registry.

The Czech glosses remain ASCII, consistently with the current Canon:

```text
MINIMAL-READ    usporne cteni
MAXIMAL-REACH   nejdelsi dosah
```

## 2. Exact meaning to freeze in a future public probe

The public mathematical carrier must first be proved complete:

```text
A_int = {beta_1, beta_3}.
```

The proof must be all-index, not a finite search. In the proposed route,
`F_n | L_n` together with

```text
L_n^2 - 5 F_n^2 = 4 (-1)^n
```

forces `F_n^2 | 4` for positive odd `n`, leaving exactly `n = 1, 3`.
The future public proof must state its index domain and every parity
restriction explicitly.

On that complete frozen pair, the proposed exact comparison is:

```text
coin       generic cover   rung cover   uniform constant   worst |1-rho|^2
beta_1     2               1            sqrt5/2            16/5
beta_3     6               5            sqrt5              4/5
```

`MINIMAL-READ` therefore selects `beta_1` uniquely by both registered cost
coordinates. The two criteria are extensionally equivalent only on the
complete frozen admissible pair. No general equivalence between covering
multiplicity and ergodic convergence is asserted.

The later public text must say:

- `generic covering multiplicity 2 versus 6`, not unqualified
  `multiplicity 2 versus 6`;
- `rung multiplicity 1 versus 5`;
- `uniform ergodic constant sqrt5/2 versus sqrt5`, a factor two;
- `squared step-operator gap |1-rho|^2 = 16/5 versus 4/5` at the common
  worst momentum, a factor four;
- never `beta_1 reads four times faster`, because the proved uniform constants
  differ by a factor two.

The future preregistration must also freeze the endpoint convention. If the
composed coherent ranges are open, it must state what covers their seams. If
they are closed, it must state how shared endpoints contribute to
multiplicity. The phrase `complete read` is permitted only after the union,
seams, generic points, and rung points are all proved under one convention.
The non-integral `w = 1/2` comparison may be called a generic single tiling
only with the same endpoint qualification.

`MAXIMAL-REACH` selects `beta_3` on the same pair. Its existence is not a
falsifier of `MINIMAL-READ`; it is the named alternative that makes the owner
choice explicit.

## 3. Proposed future H row

After a public formal result establishes the complete carrier and all exact
comparisons above, the later fold may add this status-neutral identifier:

```text
COIN-MINIMAL-READ [H], layer L1

Scope:
  Among the integer-admissible alternator coins proved publicly to be exactly
  {beta_1, beta_3}, the dictionary adopts beta_1 by MINIMAL-READ: beta_1
  uniquely minimizes both generic covering multiplicity and the worst-case
  constant of the uniform ergodic read. MAXIMAL-REACH is the named,
  unadopted counter-selector and would choose beta_3. No claim that the
  decoder architecture forces MINIMAL-READ is included.

Evidence:
  the future public probe and exact evidence tuple that prove completeness,
  multiplicities, ergodic constants, and the squared-gap comparison; the
  location and hash must be known before the row is folded

Falsifier:
  fires if an exact public derivation from the complete registered
  architecture uniquely forces beta_3, or if the frozen admissible-pair or
  ranking theorem fails. Merely exhibiting another preference that chooses
  beta_3 does not fire the row.
```

References must use `COIN-MINIMAL-READ [H]`. `H-COIN-MINIMAL-READ` is not a
claim identifier. Public claim identifiers are status neutral and remain
stable when statuses move.

The H row must depend on the existing `BOOST-READING-SPLIT [T]` and
`BOOST-COUNT-LADDER [D]` only through exact, named public theorem rows added
by the future probe. This note does not freeze the theorem-row granularity,
identifiers, evidence kind, architecture requirement, or dependency edges.

## 4. Proposed future O row

The derivation debt receives the separate status-neutral identifier:

```text
MINIMAL-READ-DERIVATION [O], L1/L5 boundary

Scope:
  Decide whether the complete registered decoder architecture, without
  adopting MINIMAL-READ as a premise, uniquely forces the beta_1 alternator
  coin and its minimum-read property.

Positive closure:
  a complete typed derivation from the registered decoder carrier, maps,
  admissible protocol class, and dependency graph uniquely forces w = 1 and
  beta_1.

Negative closure:
  the complete admissible decoder class is proved nonempty and either
  contains fully compliant beta_1 and beta_3 realizations, so the selector is
  nonunique, or uniquely forces beta_3.

STOP:
  the decoder completion, admissible protocol class, cover-to-output map,
  redundancy bound, dependency graph, or action-layer gate is incomplete;
  or one proposed derivation route fails without classifying the complete
  admissible decoder class.
```

This decision condition is outcome-complete. It does not define failure of
one favored proof as a negative theorem.

## 5. No-feedback route and its boundary

The current public Canon defines the present partial decoder as read-only:
its declared outputs do not feed the autonomous L1 update. It separately
keeps `OBSERVER-WRITE-PORT [H]` live and `STOP` because terminality of the
present partial outputs does not prove terminality of every completed
admissible observer.

The proposed route to `MINIMAL-READ-DERIVATION` is therefore conditional on
all of the following:

1. `OBSERVER-WRITE-PORT [H]` closes positively for a completed typed decoder;
2. the complete admissible protocol class is public;
3. a typed map identifies cover sheets with terminal output reads;
4. the accumulator and its equality or reconciliation rule are public;
5. an exact theorem relates absence of feedback to a bound on admissible
   read redundancy;
6. the L5-to-L1 action-layer boundary has its own named gate.

Only then may one ask whether a multiplicity-`2w` cover delivers redundant
terminal reads that the architecture cannot reconcile and whether the
smallest integer-admissible value, `w = 1`, is forced.

A proof that no-feedback alone tolerates arbitrary finite read multiplicity
kills this route only. It leaves `MINIMAL-READ-DERIVATION [O]` open unless the
proof classifies the complete registered decoder class. It also leaves
`COIN-MINIMAL-READ [H]` available as an explicitly adopted dictionary
premise.

This note neither closes nor changes `OBSERVER-WRITE-PORT`, any of its current
dependencies, or `GATE-L5-L1-OBSERVER-WRITEBACK`.

## 6. Public retirement and decoherence firewalls

The incubation names `O-COIN-CANONICAL` and `O-DECOHERENCE-CLAUSE` do not
exist in the current public registry. They are audit provenance only. The
later public fold must not append retirement, closure, or history events for
absent public identifiers.

The prospective public operation is additive:

```text
add COIN-MINIMAL-READ [H]
add MINIMAL-READ-DERIVATION [O]
```

and only after their public support exists. The internal mapping

```text
O-COIN-CANONICAL
  -> COIN-MINIMAL-READ [H] + MINIMAL-READ-DERIVATION [O]
```

may appear in private reconciliation material but not as a public retirement
event.

Likewise, an internal proposal to absorb `O-DECOHERENCE-CLAUSE` into a future
`DRIFT-IS-THE-READ` theorem creates no present public closure. Any public
drift theorem must declare the translation-covariant read and long-window
premises, their exact domains, and their dependencies. Anchoring those
premises to `MEASURE-BORN-VERB` or another decoder row is separate work and
is not decided here.

## 7. Required public evidence route

The reviewed incubation bundle is an audit input, not public evidence. Its
bytes, scripts, stdout, failed-run diary, and amendment narrative must not be
copied into the public repository as a substitute for the formal protocol.

Before either future row enters Canon:

1. claim one collision-free public issue and probe identifier;
2. write a self-contained public `PREREG.md` with the six required fields,
   exact endpoint convention, all-index rigidity proof, named standard steps,
   action layer, premises, and falsifiers;
3. fold the accepted exact checks into one public verifier and pin it with
   the preregistration before any formal execution;
4. preserve both positive and negative outcomes, including `beta_3`,
   nonuniqueness, a third admissible coin, an endpoint gap, or a failed
   uniform bound;
5. obtain the required byte-identical public architecture records;
6. merge the formal probe result at no stronger status or scope than earned;
7. only then decide whether the exact result and these owner-approved H/O
   rows are included in the sealed v27 manifest.

The owner audit checked the supplied incubation package manifest:

```text
bundle name           boostlane20260729.zip
bundle SHA-256        723e3788d9f8bc2ce8cc214cdb963f332ac1c2968abed9a92838543fe414570f
manifest entries      25
manifest mismatches   0
```

These fields prove only the integrity of the reviewed audit input. They prove
no public scientific claim and create no architecture record.

## 8. Expected later fold surface

If the formal public result merges and the owner seals this item into v27,
the composed content fold is expected to update, at minimum:

```text
canon/CANON.md
canon/CHANGELOG.md
canon/CORE.md
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/FRONTIER.md
canon/FRONTIER_PROGRAMS.tsv
canon/GATES.tsv, only if a new owned gate is publicly frozen
canon/HISTORY.tsv
canon/NORMATIVE.tsv
canon/REGISTRY.tsv
canon/SHA256SUMS
canon/STATUS_COUNTS.tsv
reproduce/status-separation/EXPECTED.txt
reproduce/status-separation/README.md
reproduce/status-separation/verify.py
tools/test_architecture_map_report.py, if the composed topology changes it
```

The exact path set, row counts, evidence classes, dependencies, gates,
history sequences, and signed release arithmetic cannot be frozen before the
formal probe result and complete v27 manifest exist. No standalone claim
delta is asserted by this note.

The final release must preserve the queue topology:

```text
B <- C <- R
```

`B` is the then-current public base, `C` is one complete composed content
commit, and `R` changes only `STATUS.md`, `README.md`, and `CITATION.cff`.
This notes branch is not the release branch.

## 9. Naming firewall

The following alternatives remain rejected:

```text
ECONOMY-OF-READ       duplicates MINIMAL-READ with a longer name
LEAST-ACTION-READ     imports an unearned physics principle
GAP-MATCHING          names an outcome, not the selector premise
SPIN-COVER-SELECTOR   promotes a remark into a normative rule
```

The fold-ready sentence is:

> The beta_1 coin is adopted as H because it is the least redundant complete
> read allowed by integrality, and on the frozen admissible pair the distinct
> multiplicity and uniform-read criteria both select it. It remains H until
> MINIMAL-READ-DERIVATION closes.

`Distinct` replaces `independent`: both criteria are derived from the same
frozen coin family and must not be presented as independent experiments.

## 10. Scope and safety firewall

This note:

- contains no executable artifact;
- runs no verifier or reproduction;
- changes no public Canon byte;
- creates no public theorem, dictionary, obligation, gate, or dependency;
- imports no incubation source, stdout, failed-run diary, or private path;
- records no secret, credential, private hostname, machine nickname, binary,
  model, or personal datum;
- does not claim that `MINIMAL-READ` is derived;
- does not claim that the decoder is complete;
- does not turn a route failure into a negative theorem;
- does not retire an absent public identifier;
- does not select `MAXIMAL-REACH`;
- does not promote any L1-to-L5 or L5-to-L1 bridge.

Public Canon v26 remains fully authoritative while this disposition is
reviewed. Inclusion in Public Canon v27 remains provisional until the owner
seals the complete manifest and every required formal result has already
merged through its own reviewed public protocol.
