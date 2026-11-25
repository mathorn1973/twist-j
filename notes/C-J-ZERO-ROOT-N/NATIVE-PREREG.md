# C-J-ZERO-ROOT-N, native two-residue supplement

PUBLIC / NON-CANONICAL / L1. Prospective exact audit of the proposed analytical
construction. The construction and predicted outputs were known before this
pin. It is not a blind discovery experiment. The public owner is
[issue #2097](https://github.com/mathorn1973/twist-j/issues/2097). The session
is `codex-zero-root-20261125` and the delegated source-review lane is `native`.

## Equation

Write `O = Z[j]`, `Phi_5(j) = 0`, `ell = 1-j`, `rho = j^2`, and let `Tr`
be the field trace to Q. For `x = u ell^2 + v ell^3 mod 5O` define

```text
r_k(x) = (2 Tr(rho^k x) - 2 Tr(x))/5 mod 5, k = 0,...,4.
E(u,v) = (-2u-v-3, 0, v, 0, 3, 2u) in F_5^6.
```

Supply `E(u,v)` at native counter zero. The actual selectors are `a,c,e`.
At cut three the complete checkpoint is `(0,r_1,1,r_4,4,1+2u)` and the two
receiver pistons are `r_1=v-2u` and `r_4=-v`. A fixed reader of only the
current counter and the two current receiver pistons returns `BLANK` on
cuts zero through two and `PRESENT(r_1,r_4)` at every cut from three. Its
cutoff defines the declared record time. The raw receiver need not remain
constant before or after that time. `PRESENT(0,0)` is an admitted record.

## Code

`native_verify.py` uses Python 3.10 or later and the standard library only. Run it from
the repository root with the exact command below after the pin and public
readback. The script uses independently implemented cyclotomic polynomial
arithmetic for target values and direct coordinate functions for the native
generators. The operations that prepare, advance and read the native state
never call the reference trace computation.

```sh
python3 -I notes/C-J-ZERO-ROOT-N/native_verify.py
```

## Carrier and data

The complete native carrier is `N_0 x F_5^6` with the existing counter and
unchanged update. The variable source coordinates are `(p1,p1p,r)`, with
one balancing relation, and the receiver coordinates `(p4,p4p,q)` start at
the common raw value `(0,0,3)`. The capture preparation is supplied. The
raw receiver piston record has two field digits. It determines all five
relative residues on this layer and, together with the current counter,
allows recovery of the admitted complete field. The audit uses all 25
input pairs, all native cuts `n=0,...,64` and all consecutive edges within
that horizon. It also uses all 25 naturally ordered polynomial coefficient
preparations with common receiver `(q,r)=(0,1)` as a separate example of the
raw two-coordinate apparatus boundary.

## Systematics

The only schedule is the native origin-zero Thue–Morse driver. `p1,p4,p1p,p4p,q,r`
is the checkpoint coordinate order. `r` as a raw native coordinate and
`r_k` as a relative datum have different types. `z` is the native sum of six
field coordinates. It is not the characteristic-zero field trace of `x`.
The comparison uses the marked ascending powers of `j` and the generator
order `(a,b,c,d,e)`. In the verifier, the trace target is evaluated over Z
before reducing the quotient modulo five. Integer representatives `0,...,4`
are used only for the finite audit and ring reference.

The new correlated preparation, the observation at cut three and the fixed
tail reader are all supplied explicitly. The proof gives an all-time result
on the admitted family. The finite audit does not establish the all-time
quantifier by extrapolation. The physical source preparation, physical access
to the port and a separate internal decoder circuit are unspecified. This
supplement contains no renewal criterion or arbitrary-input writer claim.

## Failure threshold

One exact counterexample rejects the affected assertion. The verifier must
check divisibility and the full relative profile against the independent
polynomial targets, coverage of the 25 source and output words, a truly
common receiver at preparation, non-preloading of `r_1` as any input
coordinate function, the actual three selectors and complete endpoint,
the synchronized selector and closed receiver continuation, the fixed
reader at all audited cuts, the per-cut complete state uniqueness and
the family inverse. It must also check that the natural coefficient control
has a common `(q,r)` history on the entire layer despite nonconstant targets.
The written proof rejects any exact all-time violation in its stated family.

The finite run must exit zero with empty stderr and emit the declared
summary with its exact counts. A runtime or custody failure without a
mathematical counterexample gives STOP. Frozen inputs remain as recorded.
The verifier checks complete states, not just the receiver endpoints.

The exact predicted summary is

```text
Polynomial targets and distinct literal write words: 25
Complete native cuts and edges: 1625, 1600
Tail readings and whole-state reconstructions: 1550, 1550
Complete inverse edges and complete inverse words: 1600, 25
Natural coefficient control: 25 inputs, 65 cuts, one common port history
PASS
```

## Action layer and authority

This supplement concerns L1 of the original `U` on native checkpoints. It
proposes no canon change or cross-layer interpretation. The parent source
pin is `42aa800e6e87cca234491b386ac0fe412f7ebb4d`. Its public basis is
`canon-v117` at `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed` with content
commit `d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`. The exact generator
definitions and related scope premises are pinned in `NATIVE-PROOF.md`.
