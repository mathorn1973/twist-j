# P-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 result

Date 2026-08-17. Preregistration pinned at commit
`98cdb4f42b19445aca15656c9c3f6fe2d7e28737` before the local formal leg.

## Verdict

```text
P1  family agreement through degree 3        T   no falsifier fired
P2  universal degree-4 separator set         T   no falsifier fired
P3  value table reads the index              T   no falsifier fired
P4  spectra of the squared readout           T   no falsifier fired
P5  action table and diagonal collapse       T   no falsifier fired
P6  degree-5 inventory                       T   no falsifier fired
P7  fixed-modulus fourth cumulant            T   no falsifier fired
registry row TT-VECTOR-MOMENT-UNDERDETERMINATION   proposed T, one row,
             awaiting the required check and a later integer-versioned fold
parent TT-VECTOR-STATE-NORMALIZATION               [O] / STOP, unchanged
```

The statement labels are carried by the written proofs in `PREREG.md`; the
verifier audits them at complete finite scope and is not the source of the
status. None of the falsifiers F1 to F8 fired; every gate is an exact
equality over `Q(zeta_5)`, an exact set equality, or an exact measure
equality, so no threshold exists that could have been moved.

## Evidence

```text
PREREG.md    sha256 569546e48301b5cde035dd248243be19274b73a4f92ba2655703663c563d8fdf  18046 B
verify.py    sha256 a0b86d78e414825c386e3f08c654ec73e0d174c73f097cb311fa5244a07f4b67  13802 B
EXPECTED.txt sha256 711bb0e825029c2f77a84f74934c8af32224d53da934bf5c8e484ff801edd59c   3013 B
```

Local formal leg: macOS 26.5.2, aarch64, CPython 3.9.6, from a fresh clone of
the pinned branch at the pin commit, repository root, deterministic
environment, exit 0, empty stderr, 40 of 40 gates PASS, executed twice with
byte-identical stdout. Second-architecture reproduction: Ubuntu 24.04.4 LTS,
x86_64, CPython 3.12.3, from its own fresh clone of the pinned branch, same
stdout byte for byte. The required GitHub x86_64 and aarch64 jobs at
pull-request time rerun this verifier from the repository root and compare
stdout byte for byte against `EXPECTED.txt`, completing the public
two-architecture gate.

Independent break attempt: recorded in the incubation lane cited in
`PREREG.md`, a disjoint closed-form character-sum code path, 11 gates, zero
breaks, including the diagonal moment identity at every degree up to six and
both orbit identities at the moment level. The lane also records the pair
candidate and the discovery order.

## Consequence, stated without inflation

Second-order and degree-3 data leave the squared-readout spectrum free
across a full `Z/5` index and its mixtures; the freedom survives the
diagonal four-fold symmetry; the free datum is read exactly by the twenty
fourth moments; and a Gaussian boundary is unavailable at deterministic
pointwise modulus. An admissible normalization for the parent must therefore
freeze fourth-moment data, the complete state, or an explicit non-Gaussian
closure rule. This probe supplies no `r_T(k)` and does not close the parent
in either direction. No gate is created; `canon/GATES.tsv` is untouched;
`w = v^2` is an `L1` algebraic map and `S_w` is the power spectrum of the
squared readout, not a tensor spectrum and not `r_T(k)`.

## Fold pointer

The consumable proposal is `PROMO.md` in the candidate -2 directory of the
incubation lane, commit `09182ec9b7b4a7649cc3fda5d56c4703ed5a6b52`: one
registry row in section `14. The gravitational wave program`, the frontier
cross-reference line under the parent bullet, the NORMATIVE row at layer
`L1`, no gate, ordinary integer-versioned fold updates `v50` to `v51`. The
fold is a separate, later step under review and is not performed by this
probe.
