# C-J-ZERO-ROOT-N, current-state reference supplement

PUBLIC / NON-CANONICAL / L1. This prospective finite audit follows the
analytical derivation in [reference-PROOF.md](reference-PROOF.md). The
predicted results are already known.
The public reservation is [issue #2097](https://github.com/mathorn1973/twist-j/issues/2097).
The session is `codex-zero-root-20261125` and the source lane is `native`.

## Equation

Use the unchanged original update `U` and the already frozen preparation
`E(u,v)=(-2u-v-3,0,v,0,3,2u)` at counter zero. Write the current raw
checkpoint as `w=(p1,p4,p1p,p4p,q,r)`. All arithmetic here is in `F_5`.

```text
z = sum(w)
A = p1+p1p       C = p1-p1p-2
B = p4+p4p       D = p4-p4p-1
R(w) = BLANK                                           if z not in {1,4}
     = PRESENT(3(AB+3CD+1), 3(AB-3CD-1))               otherwise
```

The exact required output on each admitted orbit is `BLANK` at cuts zero,
one and two, then `PRESENT(r_1,r_4)` at every cut from three. The whole
native state retains its original counter for evolution. The read function
receives only the current six coordinates, without that counter, the
original source or history. `PRESENT(0,0)` and `BLANK` are distinct tags.

The separate information control compares the projections of the complete
25-state family onto the four pistons at cuts two and eight. They are
equal even though the required readiness tags at those cuts differ.
One additional launch with all six raw coordinates zero is outside the
prepared family. It is BLANK at cuts zero through two and reads
`PRESENT(0,3)` at every cut from three, including its exact cut-three
checkpoint `(0,0,1,3,1,1)`. The prepared ring-zero launch is instead
`E(0,0)=(2,0,0,0,3,0)` and reads `PRESENT(0,0)`.

## Code

Run the pinned standard-library checker with Python 3.10 or later after
public byte readback, from the repository root.

```sh
python3 -I notes/C-J-ZERO-ROOT-N/reference_verify.py
```

The script checks the SHA-256 of `native_verify.py` and loads its directly
specified native generators, supplied preparation and cyclotomic polynomial
target evaluator. It adds a separate implementation of `R(w)` and a finite
audit of the new relations. This is an extension of the earlier verifier,
with reproduction of its reused portions. It is not an independent audit
of the native or polynomial target implementations.

## Carrier and data

The full carrier remains `N_0 x F_5^6`. The 25 launches are all pairs
`(u,v)` in `F_5^2` with the earlier raw preparation. The ring target on
`x=u ell^2+v ell^3 mod 5O` is the previous relative trace code. The finite
audit covers every cut `n=0,...,64` and all edges in that horizon. The new
reader takes the four current piston coordinates and uses `q,r` only
through the native readiness sum `z`. Two of the four pistons are the
previous receiver and the other two serve as existing phase references.

## Systematics

The origin, clock, generator order, supplied launch, and polynomial
interpretation retain the exact prior contracts. `z` is a sum of raw
native field coordinates. The readout has no cyclotomic trace operation,
absolute or relative, and supplies no feedback to `U`. The `Tr` evaluation
appears only in the separate polynomial calculation inside the reused
comparison code. The alternate clock-assisted decoder is unnecessary to
the new readout and is not called by the new verifier.

The [proof](reference-PROOF.md) gives the all-time assertion and the exact
scope of the four-piston control. The identical current-state reader is
applied at every finite audit cut. Invoking it neither adds a native
state register nor establishes a material circuit for the read function.

## Failure threshold

One exact violation rejects the affected assertion. The audit must check
the initial selectors and literal cut-three residue pair, distinct complete
states, the exact reference coordinates and constant products throughout
the tail, and the specified BLANK or PRESENT value at every cut. A zero
pair that is reported as BLANK at any admitted tail cut is a failure. At
cuts two and eight the projected four-piston sets must be equal, of size
25, with disjoint sets of readiness tags. All previous sources remain
unchanged. The raw all-zero control must have the actual prefix `a,c,e`,
the exact cut-three field and the declared tag and pair at every audited
cut. Custody or runtime failure without an arithmetic counterexample
gives STOP. Successful execution exits zero, emits empty stderr and
produces exactly the following summary.

```text
Complete native cuts and edges: 1625, 1600
Counter-free BLANK and PRESENT readings: 75, 1550
Reference signs and invariant coordinate products: 1550, 1550
Distinct recorded pairs: 25, zero-pair readings: 62
Four-piston readiness collision: 25 equal projections at cuts 2 and 8
Raw all-zero control: BLANK at 3 cuts, PRESENT(0,3) at 62 cuts
PASS
```

## Action layer and authority

This is an L1 observation on the same prepared original native history.
It asserts no cross-layer result. The earlier immutable native supplement
is `8c31f9d7f9d770d0a16a79960c69da2f5abc316c`, based on `canon-v117`
activation `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, normative content
`d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`. The reused script has SHA-256
`8b98125d9dcd0043b098aee93d2529649a50e2a3c49e31aadd4e67e02052b308`.
