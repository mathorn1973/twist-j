# Synthesis worklist (NON-CANONICAL)

Working notes of the Public Canon v1 synthesis. Nothing here is a
claim. Branch synthesis/canon-v1; session log at the bottom.

## Decisions

D1 basis frozen (see legacy/CUTOVER_AUDIT.md); D2 registry selection
rule; D3 neutral stable claim ids; D4 single Apache-2.0 license; D5
minimal initial reproductions: approved by the author 2026-07-12.
D6 cutover date: pending; set when Phase A is reviewable.

Standing rules of this synthesis: public statuses are conservative, at
most T in the genesis bundle, and internal sources keep their grades
in the cutover audit; no unproven independence claims (pi and ln phi
carry linear independence over the algebraic numbers only); a
status-labelled statement without a registry identifier is unfinished
draft material and must be registered with evidence, rewritten as a
definition or remark, or removed before the synthesis pull request
opens; every live registry row carries a concrete falsifier or a
decision condition, and check_canon.py rejects placeholders; a live
row whose decision condition cannot be stated faithfully is omitted
with a reason in the audit and queued here, never registered vaguely.

## Queue before the synthesis PR opens

1. Registry completion, cluster by cluster, each with evidence:
   Born quartet (next), Dirac ladder theorem layer, color ladder
   rungs, gravity chain, mass ladder, Weinberg, Maxwell closure,
   alpha value (needs a high precision exact reproduction), cosmology
   register, coupling and metrology arc.
2. Deepen sections 14 and 15 from the sealed arc part bodies at the
   internal basis (they are stated here at frontier resolution).
3. Reconciliation audit rows for every added claim.
4. Deferred frontier rows, each returning only with a concrete
   falsifier or decision condition: W1-INTERFACE-PRINCIPLE,
   KERNEL-BRAID, TIMEQUANTUM-POTENTIAL, the internal O17 residual.
5. The pre PR inventory: sweep the Canon for every status-labelled
   statement without a registry identifier (grep for bracketed
   labels); each gets an identifier and registration, becomes a
   definition or remark, or is removed.
6. Full local check run, security audit, PR template fields.

## Two architecture witness

Recorded per push in the session log. Platforms are named neutrally:
operating system, architecture, Python version.

## Session log

- s1 (2026-07-12): gate hardening and genesis bundle. check_canon.py
  rejects placeholder falsifiers (concrete falsifier or decision
  condition required for every H, O, F row). The bundle: Canon
  candidate in nineteen sections with the concrete kernel definition
  in section 3; registry 44 claims (11 T with evidence, 8 by
  reproduction and 3 by inline derivation; 4 C, the census cluster;
  24 O and 5 H frontier rows, each with a concrete falsifier or
  decision condition); four reproduction witnesses: kernel 15/15,
  alpha-exact-lemma 5/5, born-faces 8/8, census 11/11 (including
  closure under both transitions and second window stability); four
  frontier rows explicitly omitted with reasons in the audit; core,
  frontier, changelog, SHA256SUMS, citation, status candidate line;
  basis frozen; audit mapping for all 44 rows; all checks green
  locally on Ubuntu 24.04 aarch64 (Python 3.12.3).
