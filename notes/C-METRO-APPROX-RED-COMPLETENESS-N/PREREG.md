# PREREG C-METRO-APPROX-RED-COMPLETENESS-N

Status: NON-CANONICAL incubation candidate, no authority, promotes nothing.
Target on promotion: METRO-REDUCTION-CALCULUS [O], obligation E, as input to an
owner re-scope, not as a closure. Session: Claude (Cowork), 2026-09-22.
Basis: Public Canon v91, section 15. Known-result disclosure: the witnesses
were found by a helper agent's scratch exploration in this session; this
verifier is new code.

## 1. Equation

F_x(v) = w(delta_v x) over all V-tuples v; Phi(P) = {F_x : x in S_reach(P)}.
Readings of "complete": RV, P ~V P' iff equal sets of start V-futures; RS,
P ~S P' iff equal sets of canonical start streams (encoding as in
C-METRO-COMMON-BLOCKING-N).

E-INV (written proof): each of the four admitted arrows preserves Phi up to its
transport (relabeling transports; restriction keeps S_reach and futures;
the Nerode quotient under Pre_3 has F_[x] = F_x; permutation transports
V-tuples). Hence approx_red implies equal Phi.

E-POS (written proof): on commuting tuples every Sigma*-reachable state is
V-reachable, Pre_3 holds automatically, and the reach+Nerode normal form is
determined by the set of start V-futures; so ~V implies approx_red via
P -> reach -> quotient ~= quotient' <- reach' <- P'.

Witnesses: W-V (noncommuting, ~V, Phi differs) and W-S (rank one, MSD and LSD,
equal canonical streams under E0 and Z0, Phi differs), as coded.

## 2. Code
verify_approx_red.py, standard library, exact.

## 3. Data
Witnesses as coded; census q=2, a=2, |S|=2, A0={0}, binary w, 1024 tuples.

## 4. Systematics
Census is finite range (candidate-C). E-INV and E-POS are written proofs.

## 5. Falsifier (fixed before computation)
Fires if W-V or W-S fails to reproduce, if a commuting ~V pair in the census
has different Phi or a Pre_3 failure appears on a commuting tuple.
Expected consequence if nothing fires: approx_red is incomplete for U_RF
under RV and under RS; it is complete under RV on the commuting class. The
registered E cannot close positively without an owner re-scope; incompleteness
is not among the row's negative-closure clauses.

## 6. Layer
L5.
