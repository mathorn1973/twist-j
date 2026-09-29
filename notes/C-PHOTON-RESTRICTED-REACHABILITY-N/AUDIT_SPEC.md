# Prospective finite integer audit

PUBLIC / NON-CANONICAL. Item: C-PHOTON-RESTRICTED-REACHABILITY-N.
Author: A. M. Thorn <thorn@twistj.com>.

This specification and `audit.py` are to be frozen before execution. They
specify an exact finite implementation audit, not an exhaustive examination
of the four-dimensional configuration space and not a proof for arbitrary
L. The accompanying written argument, if accepted, supplies any general
reachability claim. No mixing rate, equilibration diagnosis, sample
reliability, thermodynamic bound, P1 closure, or Canon promotion follows
from a PASS here. A local execution supplies one architecture only.

## Fixed domains and checks

1. Exhaust all 125 triples `(a,b,delta)` in `{0,1,2,3,4}^3`. Here the
   bounded heights are representative flux plus two. Check that the
   modular pair update `(a+delta,b-delta)` changes their total by only
   `-5,0,+5` and agrees with the representative convention. For each of
   the 25 height pairs, check the specified reduction to `(a+b-5,0)`
   when `a+b>=5`, and increase to `(4,a+b+1)` when `a+b<=3`.

2. Exhaust every height configuration on exactly these finite connected
   graphs: the two-vertex edge, the three-vertex path, the four-vertex
   cycle, and the five-vertex star. For each possible total separately,
   breadth-first traversal uses only nonwrapping transfers of one height
   unit along an edge. Require that all configurations with that total
   are reached. This is a finite audit of the fixed-total lemma, not its
   all-graph proof.

3. Use actual periodic square grids for exactly `L in {4,6,8,10}` and
   source `k in {1,2}`. Sites have index `x0+L*x1`, primal links have
   index `2*site+mu`, and the independent curl formula is

   ```text
   curl(x) = a0(x) + a1(x+e0) - a0(x+e1) - a1(x) (mod 5).
   ```

   Check every unit link field against its dual incidence column. Build
   a deterministic breadth-first spanning tree from plaquette zero,
   using the ascending primal-link insertion order defined in the source.
   Construct every fundamental cycle from one non-tree edge followed by
   the unique returning tree path. Require simplicity, closure, the
   unique non-tree-edge coordinate, and exactly `L^2+1` cycles. Keep the
   integer geometric winding on the periodic grid and require a pair of
   cycle winding vectors of determinant `+1` or `-1`; in particular the
   audit includes both noncontractible directions.

4. In each grid and for each source, construct both extremal flux layouts
   explicitly. At the lower extreme, all heights are zero except the
   first height `(2L^2+k) mod 5`. At the upper extreme, all heights are
   four except the first, decreased by `(2L^2-k) mod 5`. Require the
   resulting slice winding to be

   ```text
   w_min = -floor((2L^2+k)/5) <= -6,
   w_max =  floor((2L^2-k)/5) >=  6.
   ```

   Solve for an explicit primal link field using leaf-to-root elimination
   on the dual spanning tree, with source `k` at plaquette zero. Verify
   the resulting field using the independent primal curl formula.

5. From each explicit extreme field, implement every fundamental cycle
   as an ordered sequence of single-link changes for each coefficient
   in `{1,2,3,4}`. Check both `n=1` and `n=L^2`, leaving the other `n-1`
   twisted slices at the same extreme. After every link change recompute
   the full slice curl independently, verify that only the two path
   endpoints differ from the original flux, verify that the slice
   winding differs by at most one, and require the full twisted-slice
   sum to remain inside the original class:

   ```text
   C_minus(n): 2W < -n;   C_zero(n): 2W >= -n.
   ```

   At completion require the original flux to be restored and the
   nonzero prescribed cycle to have been added to the link field.

## Execution and disposition

The audit uses only the Python standard library and exact integers.
There are no random seeds, floating-point numbers, fitted constants,
external inputs, environment-dependent branches, or scientific libraries.
The intended runtime is below 45 seconds on an ordinary single CPU; this
is an engineering target, not an acceptance threshold. The deterministic
stdout is one compact JSON object containing counts, scope
`FINITE_INTEGER_AUDIT_ONLY`, and result `PASS`. Assertions stop execution
on the first failed check. A failure is recorded and investigated without
changing this frozen source or its domains. Any changed audit requires
a separately declared successor and a new source pin.

The first execution is prohibited until the owner has publicly recorded
the source pin. Execution is a reproduction of the above finite checks;
it is not an independent confirmation of the general written proof.
