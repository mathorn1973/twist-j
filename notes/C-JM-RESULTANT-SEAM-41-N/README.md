# Two records and the resultant-41 seam

**Status:** NON-CANONICAL, `C-JM-RESULTANT-SEAM-41-N`, L1.
**Grade:** candidate-T analytical results with candidate-C exact, result-exposed
checks on one x86_64 architecture. No earned public status is claimed.
**Owner:** A. M. Thorn, session `seam41-pr-2026-10-20`.
**Custody:** [issue #1670](https://github.com/mathorn1973/twist-j/issues/1670).

This PR archives the completed statement before any successor investigation.
The author supplied the product polynomial, resultant and first four period
counts. The analytical qualifications and extensions were already completed
in the source report. This is not a fresh discovery run, a retrospective
public preregistration or an independent confirmation.

## The statement being preserved

Fix

```text
f=x^4-3x^3+4x^2-2x+1,
g=x^4-4x^3+8x^2-4x+1,
A=Z[x]/(f), B=Z[x]/(g), R=Z[x]/(fg), S=A x B.
```

**The two fixed rank-four integer steps admit one polynomial record glued
through the common quotient F41 at x -> 19. The inclusion R -> S has index
41 and identifies R with A x_(F41) B. There are exactly 41 marked extension
classes 0 -> A -> E -> B -> 0 as Z[x]-modules; allowing the specified endpoint
unit relabelings leaves two middle-module types. Split and glued steps have
respective orders 40 and 1640 modulo 41, although all their toral fixed-point
counts agree. The glued order is not closed under inherited CM conjugation;
adjoining the conjugate common step generates the entire maximal product.**

The fixed realization is `J=1+j^2`, `m=zeta8`, `M=1+m+m^2`, and
`alpha=(J,M)`. One must distinguish the three orders:

```text
R subset S=Z[J] x Z[M] subset O=Z[j] x Z[m],
[S:R]=41, [O:S]=3, [O:R]=123.
```

The 41 classes are **marked module extensions**, not 41 unmarked rings,
41 physical choices, or a classification of every integral 8-by-8 matrix.
The mod-41 common quotient is F41, but the whole glued residue algebra is
`F41[epsilon]/(epsilon^2) x F41^6`; its nilpotent component is retained.

At the selected seam,

```text
J,M -> 19,       bar(J) -> 17,       bar(M) -> 7,
J bar(J) -> 36,                    M bar(M) -> 10.
```

Thus neither `bar(alpha)` nor `alpha bar(alpha)` belongs to R, and
`R[bar(alpha)]=O`. This is a precise inherited-conjugation obstruction, not
an impossibility theorem for every external or differently typed reading.

The common finite field has the smallest possible cardinality **conditional
on retaining both phase orders 5 and 8 faithfully**: 40 divides q-1, so
q>=41, attained by F41. No unconditional physical coupling-cost minimum
follows. The block step gives a compatibility condition/common factor, not
writing of a new message from one branch into the other.

The rank-eight rational algebra is `Q(zeta5) x Q(zeta8)`, not a field.
The full field compositum is separately `Q(zeta40)`, of degree 16.

## Proof and exact certificates

[REPORT.md](REPORT.md) contains the complete inherited ten-section analysis:
fixed objects, period counts, the fiber-product proof and Bezout certificate,
the marked Ext classification, modular nilpotent dynamics, the silver index
3, inherited-conjugation failure and closure, the conditional finite-field
minimum, and the coupling/Born boundaries.

The three source scripts and their successful outputs are unchanged:

| Script | Archived stdout |
|---|---|
| `audit.py` | `ACTUAL.txt` |
| `conjugation_audit.py` | `CONJUGATION-ACTUAL.txt` |
| `supplement.py` | `SUPPLEMENT-ACTUAL.txt` |

`PREREG.md` and `SEAM-SUPPLEMENT-PREREG.md` are byte-identical **local source
preregistrations**. They were not pushed public pins before those executions.
[PROVENANCE.md](PROVENANCE.md) records that boundary, source hashes,
publication-only edits, omitted intermediate material and the replay record.

## Replay

The recorded source environment is Linux, x86_64, Python 3.13.5,
SymPy 1.14.0. SymPy is an external replay dependency, not vendored code.
The following wrapper checks the manifest, runs the unchanged scripts in an
isolated temporary directory, requires exit zero and empty stderr, and compares
stdout byte for byte:

```sh
python3 -m pip install 'sympy==1.14.0'
python3 notes/C-JM-RESULTANT-SEAM-41-N/replay.py
```

Repository CI for this notes-only PR is a policy/integrity check. It does
**not** automatically run these SymPy scripts and is not scientific
two-architecture evidence. A local replay is reproduction only.

## Relation to public work

The comparison basis is Public Canon v103 at public main
`e7fe4e38048cdb6019df0599b47ad20a952475a9`, unchanged from the completed source
analysis. Authority is declared by [STATUS.md](../../STATUS.md).
`TWO-PLACE-PHYSICS [D]` and the open apparatus owners keep their exact scopes.
No Canon, registry, frontier, gate, formal probe or workflow is changed.

The adjacent candidate `C-C40-RECIPROCAL-RAMIFIED-SEAM-N`, owned by
[issue #750](https://github.com/mathorn1973/twist-j/issues/750), concerns the
ramified 2/5 reductions of Phi40. It is a distinct carrier/question, not this
resultant-41 seam, and is not reused or resumed here.

[PROMO-C-JM-RESULTANT-SEAM-41-N.md](PROMO-C-JM-RESULTANT-SEAM-41-N.md) records
only the disposition for later review. No successor Born pairing, positive
metric, occurrence law, physical dimension/time, apparatus, measured constant
or cross-layer lift is supplied by this archival PR.
