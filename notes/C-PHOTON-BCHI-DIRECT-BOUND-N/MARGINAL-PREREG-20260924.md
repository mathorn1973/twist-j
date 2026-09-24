# Preregistered partial-current normalization audit

PUBLIC; NON-CANONICAL; no authority. Working item:
C-PHOTON-BCHI-DIRECT-BOUND-N, continuation under issue #1143.
Owner/session: A. M. Thorn / Codex-P1-current-continuation-20260924.
Date: 24 September 2026. Original code/text: Apache-2.0.

This is a notes-only analytical continuation, not a new or resumed P-probe.
The user authorized completion of #1142/#1144 and continuation on P1.
The retained basis is Public Canon v91. Sources are the unchanged #1144
CURRENT-BOUND.md proof and the corrected #1142 handoff at their candidate
scopes. No claim here closes P1, changes the action or raises Canon status.

## Target fixed before execution

Use the original measure on every even periodic four-dimensional torus,
L>=4: n_p in {-1,0,1}, weight 2^(-|supp n|), boundary n=0 mod 5,
j=boundary n/5. Do not replace it by a sector-filtered simulation measure.

For a finite selected edge set S and a disjoint edge set T carrying a
zero-current condition, define the unnormalized partial marginal
Q_T^S(a) by j|S=a and j|T=0, summing ALL other current sectors.
Test the mixed character representation: continuous U(1) integration on
S union T, discrete Z5 averaging elsewhere, character exp(-5i<a,A_S>).

For S the union of k plaquette boundaries with pairwise disjoint
21-plaquette star neighborhoods and a nonzero signed current on all their
edges, the proposed proof gives Q_T^S(a)<=16^(-k) Q_T^S(0).
T may be empty. It must carry zero current; arbitrary nonzero outside
sources and fixed outside plaquette values are not covered by this theorem.

Let Y_p be +1 or -1 when the four currents around p form that oriented
circulation, and 0 otherwise. This is a current-pattern indicator, not a
complete decomposition of the current into elementary loops. Proposed
normalized consequences, in the full measure or conditioned only on j|T=0:

- P(all k selected |Y_p|=1)<=1/(1+8^k).
- Odd products of Y_p have mean zero by global sign reversal.
- For even k, |E product Y_p|<=1/(1+2*8^k).
- In particular P(|Y_p|=1)<=1/9 and |Cov(Y_p,Y_q)|<=1/129 for
  two compatible blocks. These constants are not asserted sharp for W.

The normalized two-pattern covariance is exactly
2[P(Y_p=+1,Y_q=+1)-P(Y_p=+1,Y_q=-1)]. It is not the full edge-current
covariance C_j(e,f). No distance decay, weighted moment or chi_* bound is
claimed. The reference all-zero event is only a denominator comparator;
it is not a postselection imposed on the claimed full-measure probability.

## Frozen exact audit

Before its first execution, commit and publicly read back this file and
verify_partial_current.py on a notes branch. Record their hashes and pin.
Run the script unchanged on an x86_64 host with Python 3, standard library,
integers and Fraction only. Budget: 60 seconds. Expected terminal:
RESULT PASS; exit 0 and empty stderr. No scientific execution preceded
the pin. The prospective constants above are analytical predictions, not
blind targets or numerical discoveries.

The script checks:

1. Exact edge Fourier projectors for every integer incidence from -6 to 6.
2. Both polynomial sum-of-squares identities used by the four-edge proof.
3. A physical 21-face four-cup patch on L=4 and L=6, with all outside
   plaquette values zero, as a separate finite audit fixture. Exact F5
   elimination should give rank 17 and kernel dimension 4. Enumerate all
   625 kernel elements and retain every ternary assignment: expected 53.
   Its expected rational weights are Q0=596163/524288 and
   Qplus=Qminus=1/2097152; circulation probability 1/1192327.
   This restricted fixture is NOT used as a bound for the full torus.
4. The normalized constants for k=1..8 and abstract nonnegative mass
   witnesses saturating the relaxed inequalities. For two patterns those
   inequalities admit covariance 1/129 with no distance parameter; this
   is a logical limitation of the inequalities, not a counterexample in W.

Any failed assertion, nonzero exit, nonempty stderr, changed input or
unexpected fixture value is recorded without changing this pin. A failed
audit is not relabeled PASS; a repaired attempt would require a new pin
and a visible correction. The written universal proof must be checked
separately: finite fixtures cannot establish it.

## Status and review limits

At most candidate-T for the complete written derivation and candidate-C for
the finite audit. The same agent writes and checks this work with access to
the source proof; no blind independent-agent review is claimed. A second
execution of this same script is reproduction only. Normal note-only CI
does not by itself run this scientific audit. No formal two-architecture
acceptance, physical observable selection or layer promotion is claimed.
