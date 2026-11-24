# Exact discrete reconstruction from a boundary

**NON-CANONICAL / NO AUTHORITY. Action layer: L1.**
Owner: A. M. Thorn. Reservation: [#1421](https://github.com/mathorn1973/twist-j/issues/1421).
Public basis: `7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`, Public Canon v100.

The all-size proof passed separate review at candidate-T scope. Both first
finite audits passed with identical complete output on local x86_64,
providing candidate-C evidence. See [RESULT.md](RESULT.md).

This note gives an exact positive construction and an exact obstruction for
two separately selected finite classes. It asks whether a literal boundary
reader determines the complete admissible configuration. All equalities
are coordinate equalities over F5; no quotient or tolerance is used.

## Results proved at conditional candidate-T scope

For a nonempty affine class `X={x:Hx=b}`, restriction `R` has an exact inverse
on its image if and only if `ker H intersect ker R = {0}`. A mere bound on
the number of states does not establish that the selected reader is injective.

On `V_N={0,...,N-1}^3`, impose the eight-corner equation
`Delta_0 Delta_1 Delta_2 f=0` on every unit cube. For every `N>=2`, arbitrary
values on the union of the three coordinate-zero faces extend uniquely by

```text
f(i,j,k)=f(i,j,0)+f(i,0,k)+f(0,j,k)
         -f(i,0,0)-f(0,j,0)-f(0,0,k)+f(0,0,0).
```

The full admissible class has dimension `3N^2-3N+1`, exactly the number of
sites on that face union. This uses a local constraint to remove otherwise
independent interior data. It does not encode arbitrary unconstrained
`N^3`-coordinate fields into the same face data. Telescoping supplies the
all-size proof; finite matrix checks audit its implementation.

For edge fields on a growing nonperiodic box, Gauss's equation `dE=rho`
has a different result. Even after fixing **every individual edge with an
endpoint on the outer vertex boundary**, a nonempty fibre has `5^k_N`
members, where

```text
k_2=0;
k_N=2m^3-3m^2+1 for m=N-2>=1.
```

The complete ambiguity is the cycle space of the induced interior graph.
It has a constructive basis from a spanning tree. For `N>=4` it is nonzero
and grows in order as the interior volume. The result fixes the complete
stated Gauss-only class; additional curl or admission constraints would
define a new problem.

The pinned public Maxwell comparison retains all **24 directed edge labels**
on its eight-vertex torus. Its known whole-torus kernel dimension is 17.
On the marked four-vertex slice, five independent internal cycles leave
the entire complement and every crossing edge fixed. If only charge and
the eight crossing values are fixed on the full torus, the kernel has
dimension 10, comprising the cycles of both slices.

Exact reconstruction also has an operational consequence. If `R` is
injective, every admissible map `P:X->X` preserving all its boundary values
is the identity. An invariant deterministic law `U` transfers as
`U_B=R U D`; reversibility transfers with it, but locality does not follow
from conjugacy alone. The note's explicit update is pointwise multiplication
by 2 modulo 5, with inverse multiplication by 3. Under this chosen law,
each frozen nonzero Gauss witness remains boundary-invisible throughout
its period-four orbit.

## Evidence and reproduction

- [PREREG.md](PREREG.md): frozen class, reader, exposure, falsifiers and audit.
- [PROOF.md](PROOF.md): all-size proofs, complete bases and exact scope.
- `verify.py`: primary dense modular elimination and face-basis audit.
- `break.py`: separately authored preregistration-only implementation.
- `REVIEW.md`: independent written proof review, with its exact input pin.
- `RUN.md`: neutral first-execution record and program/source hashes.
- `EXPECTED.txt`: complete matching first-run finite audit stdout.
- `RESULT.md`: findings and status ceiling.
- `CUSTODY.md`: included and excluded implementation provenance.
- `PROMO-C-DISCRETE-BOUNDARY-RECONSTRUCTION-N.md`: review package and limits.

From a checkout containing the complete package, use Python 3.12 or later:

```sh
LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC python3 -I notes/C-DISCRETE-BOUNDARY-RECONSTRUCTION-N/verify.py
LC_ALL=C LANG=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC python3 -I notes/C-DISCRETE-BOUNDARY-RECONSTRUCTION-N/break.py
```

The two stdout streams must agree byte for byte with `EXPECTED.txt`; both
exit codes must be zero and both stderr streams empty. The original first
runs use a separately enforced 180-second wall timeout. `RUN.md` records
their exact checkout, environment and observed outcomes. These programs
audit the cube sizes 2 through 6, box sizes 2 through 7, all specified
kernel bases and the complete torus comparisons. They do not enumerate
every state: linear identities are checked on complete bases.

## Interpretation and missing native bridge

The added boxes, fields, readers, constraints and update are selected
comparison objects. No scalable carrier, region selection, complete reader
or intertwining with the original autonomous `U` has been supplied.
The original `Omega=N_0 times F5^6` is unchanged. The note neither derives
physical dimension nor supplies a physical entropy law, quantum recovery,
an area coefficient or a physical locality result.

The reconstruction formula uses only addition and subtraction and works
over any abelian group. Dimension and cycle-space arguments work over any
field. Counting by powers of five and the chosen four-phase orbit use F5;
they do not select five as a physical constant.

The earlier unmerged [#1288 / PR #1289](https://github.com/mathorn1973/twist-j/pull/1289)
owns the fixed-source capacity and uniform-radius support statements.
This note neither re-earns those statements nor depends on that unmerged
proof. Other selected D3 spectrum, wave, transport and energy lanes remain
separate. All work stays in this note; public Canon and registered claims
receive no promotion.
