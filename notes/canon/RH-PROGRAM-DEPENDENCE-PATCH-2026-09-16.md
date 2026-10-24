# Canon patch proposal: RH as a declared program dependency — v87 refresh

```text
STATUS      NON-CANONICAL Canon patch proposal; no status motion
BASIS       Public Canon v87, tag canon-v87, main fd512f50d90382124e7c00afa926c8083fd56e06
CONTENT     41c8d4229b71437f09957d959975dc1772e95806
CANON.md    sha256 a2517c6d8efb1969a7258f94d9874cca3b5b9beb1aecdfd2e39b56f33961a917, 634207 bytes
DATE        2026-09-16
SUPERSEDES  notes/canon/RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md as a proposal surface
```

This note refreshes the 2026-09-08 proposal against Public Canon v87 and resolves the three proposal-level owner decisions conservatively. It still does not alter Canon bytes. A later fold may copy the proposed row after ordinary policy, collision, registry and gate review.

## 1. Owner declaration and logical type

Owner declaration of 2026-09-08:

> „RH je vyžadováno pro TWIST-J. Padne RH a padá TWIST-J.“

English: RH is required for TWIST-J. If RH falls, TWIST-J falls.

This is a declared program contract, not a theorem derived from the TWIST-J axiom. The declaration therefore enters, if folded, as a standing hypothesis with an explicit falsifier. No computation, probe or later mathematical result can promote the declaration above hypothesis status.

## 2. Decision 1: exact required statement

The required statement is the ordinary Riemann hypothesis for the Riemann zeta function and nothing stronger:

\[
\boxed{
\text{every nontrivial zero }\rho\text{ of }\zeta(s)\text{ satisfies }\Re\rho=\frac12.
}
\]

GRH for `zeta_F`, `L(s,chi_5)`, Hecke towers or any broader family is not part of this declaration. Such hypotheses may occur in separate research lanes, but they are not silently imported into the program-level contract.

This chooses the weakest exact statement matching the owner's literal declaration and avoids coupling the entire program to stronger unresolved claims that are not presently derived as necessary.

## 3. Decision 2: program id

The proposed program-table id is

```text
RH_FOUNDATION
```

It is a dedicated program-level root rather than `ENRICHMENT`. The reason is semantic: the declaration is intended to constrain the program as a whole, while the two existing RH-adjacent rows presently live under `ENRICHMENT` for historical reasons.

Proposed `canon/FRONTIER_PROGRAMS.tsv` row:

```text
RH-PROGRAM-DEPENDENCE   RH_FOUNDATION   ROOT   BLOCKED   FORMAL
```

`BLOCKED` is intentional. Inside TWIST-J the hypothesis is neither proved nor refuted; outside TWIST-J it is decided only by a rigorous proof or disproof of RH.

## 4. Decision 3: consuming rows

No canonical dependency edge is proposed in this patch.

That is a decision, not an omission. The owner declaration is global and currently stronger as a program contract than the public derivation graph can justify row by row. The known RH-adjacent rows remain cross-references only:

- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains under its present program and decision condition;
- `LAMBDA-COCYCLE-ANGLES [H]` remains separate because its content is strictly stronger than bare RH;
- the O5 cluster remains unregistered and supplies no dependency edge until its own definitional lane is completed.

A future fold may add a row-to-row dependency only after the consuming statement and implication are explicitly proved and frozen. The declaration must not be used as a shortcut to create such edges.

## 5. Proposed registry row

Schema: `claim_id  status  scope  canon_section  evidence  falsifier`.

```text
claim_id      RH-PROGRAM-DEPENDENCE
status        H
scope         declared program-level contract of 2026-09-08: TWIST-J requires
              the ordinary Riemann hypothesis for zeta(s), meaning every
              nontrivial zero has real part 1/2; the requirement is adopted
              as a standing hypothesis and is not derived from the axiom;
              no GRH statement, zero-density estimate, prime-distribution
              theorem or row-to-row dependency is asserted by this row
canon_section 18. The frontier
evidence      inline
falsifier     fires, and by the owner declaration falsifies the TWIST-J
              program, only when an independent public record rigorously
              establishes a nontrivial zero rho of zeta(s) with Re(rho) !=
              1/2 by exact enclosure or machine-checked proof; an unverified
              disproof claim is STOP, not F; an external proof of RH retires
              this hypothesis to the changelog with citation and does not by
              itself promote any other TWIST-J row
```

No probe is attached. The row cannot be promoted above `H` by a TWIST-J numerical search or by verified height checks.

## 6. Proposed Canon prose

Suggested paragraph for section 18, subject to fold-time wording checks:

> RH-PROGRAM-DEPENDENCE [H]. TWIST-J requires the ordinary Riemann hypothesis for the Riemann zeta function. This requirement is declared, not derived: it is a standing program hypothesis with an explicit falsifier. A rigorously established nontrivial zero of zeta(s) off the critical line falsifies this row and, by the owner declaration, the program. No row in this Canon is thereby claimed to prove or approach RH. An external proof of RH retires the hypothesis but does not promote unrelated TWIST-J claims.

## 7. F-watch procedure

The watch procedure from `notes/RH-ATTACK-2026-09-15/F-WATCH-2026-09-15.md` is adopted as the operational interpretation for future reviews of this proposal:

1. A reported RH disproof is not a program falsifier by headline, abstract or unsupported manuscript claim.
2. File such a report as `STOP` until an independently checkable exact enclosure or machine-checked proof establishes a specific off-critical nontrivial zero.
3. A verified finite-height statement that all zeros in a checked region lie on the line is evidence about that finite region only and cannot promote `RH-PROGRAM-DEPENDENCE`.
4. A proof of RH from outside TWIST-J retires the hypothesis; it does not convert the declaration into a TWIST-J theorem.
5. Record source, version/date, verification status and the exact logical consequence. Do not infer zero location beyond the verified scope.

This procedure is administrative. It does not itself assert any fact about the current zero set.

## 8. Current research-lane boundaries

The 2026-09-15/16 RH attack material is NON-CANONICAL and remains outside this declaration row:

- lane A: finite Nyman–Beurling projection census and quantitative rate reading;
- lane B: fixed-epsilon Mellin/Hardy shadow condition and accumulating-epsilon ladder;
- lane C: M37 strength annotation with no known zero-location implication;
- lane D: external-claim watch procedure;
- 2026-09-16 exact obstruction: support `r_2,...,r_72` cannot meet finite-certificate target (29).

None of these results proves the declared hypothesis or creates a Canon dependency edge.

## 9. Fold-time checklist

A later activation fold must independently verify:

- collision scan for `RH-PROGRAM-DEPENDENCE` and `RH_FOUNDATION`;
- exact TSV schema and allowed program-id conventions;
- current section numbering and frontier wording at the then-active Canon;
- policy, Canon, ledger and dependency checkers on both architectures;
- tag/content ancestry and `canon/SHA256SUMS`;
- no accidental dependency edge from this declaration to stronger GRH lanes;
- no claim that fixed-epsilon target (41), M37 or any finite zero verification has already proved RH.

Until that fold is merged and released, this file has no Canon authority.
