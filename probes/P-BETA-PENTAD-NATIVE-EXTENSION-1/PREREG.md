# PREREG: P-BETA-PENTAD-NATIVE-EXTENSION-1

**Prospective formal revalidation of exposed mathematical targets.**
Owner: A. M. Thorn / coordinated intake 2026-10-13.
Action layer: **L1**. Issue lock: #1481. No Canon promotion.
Base: `5f54015ed8361e3a64cb10894397020ddfadd104`, Public Canon v101.

## 1. Equation and decision targets

All three-dimensional operations below are in `F5`. Freeze

```text
B = ((2,4,0),(4,2,4),(0,4,2))
beta(x,y) = B^-1 (x cross y)
A = ((4,1,0),(0,1,0),(0,1,4))
Phi = ((0,4,1),(0,4,0),(1,4,0))
T = ((1,0,0),(3,4,0),(4,0,4))
```

G1: among all 31 projective directions, the counts are 6 isotropic, 15 of
nonzero square B-norm and 10 of nonsquare norm. The 15 square directions
have orthogonality graph exactly five disjoint triangles. `Aut(beta)` acts
faithfully and fully as `S5` on those five triangles.

G2: on even subsets of that intrinsic pentad, `q2(S)=|S|/2 mod2` is
nondegenerate of dimension four, with five nonzero singular vectors. In a
basis of any four singular vectors it is `e2=sum_(i<j) x_i x_j`. The signed
integral action `sgn(sigma) P_sigma` on `A4` reduces to this binary action
and to the full residual Lie action on the characteristic-five radical
quotient. The explicit quotient map is the one in GEOMETRY_PROOF.
This target does not extend the marked-A5 integral Hodge equivariance to
odd permutations of the integral carrier.

G3: the all-five-generator homogeneous fiber group is exactly
`{+/-I,+/-A,+/-Phi,+/-A Phi}`, order 8; its bracket-preserving subgroup has
order 4. `T` is outside that group and is the signed A4 transposition `(01)`.
`<A,Phi,T>` has order 120; `<Phi,T>` has order 12. No original word has
homogeneous order 3 or 5 on this same fiber; affine order-five translations
are not excluded.
For semantic precision, retaining the full eight-element homogeneous group,
including `-I`, and adding T generates `O(B)` of order 240. The supplied
helper's field `native_plus_T_group=120` denotes `<A,Phi,T>`, not that full
eight-element group augmented by T. The aggregate makes this explicit.

N1: the literal native generator formulas agree with the displayed affine
fiber decompositions on every `F5^6` checkpoint. The active center is
`w_*=(1,4,3)`, and `(-1)^n Phi^chi(z)(w-w_*)` is conserved on `z in {1,4}`.

N2: the first-entry chart `K` is an affine bijection on each fiber over
`(n,s,q,r)` and is conserved across one native step. First entrance occurs
within nine steps for every initial counter; `(n,z)=(14,0)` attains nine.
The universal sharp bound is inherited from
`TM-SHEET-SYNCHRONIZING-GRAPH`, with an additional elementary proof here.

N3: for every `C in GL3(F5)`, `K^-1 C K` is the unique base-preserving
symmetry commuting with full `U` and extending the prescribed active action.
For `C in SO(B,5)` it preserves the affine Lie bracket about the chart's
distinguished center, not about an unrelated zero. A symmetry lift is not
a reversible update of `U` or a native gate word.

N4: require a single n-independent map of the **entire** checkpoint carrier,
preserving `(s,q,r)`, extending that **same prescribed active action** and
commuting with both selector-bit kernels. The complete allowed GL3 class is

```text
C_lambda = I + (lambda-1)(I+A)/2, lambda in {1,2,3,4}.
```

It has two orthogonal members and one determinant-one orthogonal member,
identity. Necessity is established in the proof by `[C,A]=0` and pointwise
fixing of `(2+r,0,1-r)` for every `r`. The accepted verifier independently
solves these linear constraints, finding exactly five affine solutions
including singular `lambda=0`, then four invertible solutions. Sufficiency
is checked on every checkpoint and both selector bits. This does not
classify symmetries that change the base or prescribe a different active
action.

N5: for the linear C-action, the scalar `(-1)^(n+tau)` cancels in
`K^-1 C K`. Thus the first-entry lift can be evaluated from the checkpoint
and an externally supplied length-nine future Thue-Morse factor. The
inherited G3 factor language contains exactly 24 such factors, giving an
upper bound of 24 supplied time-context values. This is neither a minimum
nor an autonomous update/acquisition mechanism and is not asserted for
arbitrary nonlinear permutations of invariant labels.

## 2. Code and accepted finite audits

`verify.py` is the accepted standard-library exact aggregate. The three
named helper sources are bound by byte count/SHA-256 in SOURCE_MANIFEST and
by their hashes in the accepted verifier. They are statically reviewed
original implementations; their exploratory wording is retained as source
provenance. The wrapper refuses `python -O`, captures each helper's JSON,
validates declared certificates and adds independent mod-five constraint
elimination. It reads no submitted output JSON or scientific predecessor
module. No floating point, randomness, network or solver is used.

Finite geometry audits reconstruct all 120 automorphisms independently by
PGL2 conjugation and orthonormal-frame enumeration, all intrinsic frames,
binary isometries and 120 signed coordinate permutations; the signed
homomorphism is checked for all 14400 pairs. Native audits check all 78125
checkpoint/generator pairs, all 125000 checkpoint/bit/lambda commutations,
16000 chart affine-basis instances for `n=0..31`, and 20480 entrance cases
for `n=0..4095`. The aggregate additionally checks all 25000 active
checkpoint/bit/counter-parity instances, exact constraints for N4, explicit
checkpoint obstruction witnesses and the 24-factor length-nine language.
Universal time and uniqueness conclusions are proved in
the manuscripts and are not extrapolated from those bounded time ranges.

## 3. Carrier, data and exposure

The carriers are `F5^3`, the even-subset space of five intrinsic triangles,
`A4`, the native checkpoint `F5^6`, and full state `N0 x F5^6`. Exact native
formulas are inherited from the pinned public census/Canon.
SOURCE_MANIFEST binds incoming provenance and current public premise rows.

All theorem targets and reported exploratory outputs were supplied before
this pin. This is formal revalidation, not a new blind prediction or
retrospective preregistration of supplied executions. Supplied JSON results
are excluded from the public formal input and expected stream. New first-run
records alone become accepted computational evidence for this attempt.

## 4. Systematics and integrity

Freeze the public difference basis, B-norm square class, A4 coordinate
labels, temporal composition order, selector `z+2 theta_n`, active sheets,
chart center, and the complete base-preserving extension class. Do not
confuse A4 labels with a differently ordered orthonormal-frame table.
Do not replace B-square by Killing-square: multiplying by the nonsquare 2
changes the selected projective class. Do not infer a physical or native
operation from an abstract automorphism or commuting symmetry.

Publish the complete accepted source and all proof/review/contract files,
then verify immutable public readback before first execution. Record the
pin, exact executable hashes, neutral environment, first stdout/stderr/exit
and timestamps. Keep sources unchanged after pin; no amend, rebase,
force-push, silent retry or threshold adjustment.

## 5. Failure threshold and disposition

Tolerance is **zero**. Any exact counterexample or failed mathematical
assertion fires only the corresponding frozen target. Preserve the first
failure and original pin; do not repair this attempt in place. A missing
file, source/hash mismatch, crash, timeout or architecture/stdout mismatch
without an exact mathematical negation is an integrity STOP, not a physical
falsifier. An uncompleted formal gate is disposed of under the repository's
abandoned-pin policy; never reuse or resume a sealed identifier.

After a completed run add exact EXPECTED.txt, RUN.md and RESULT.md separately.
The existing repository workflow must reproduce the accepted output on both
x86_64 and aarch64 before a two-architecture gate is claimed. A proof may
support a candidate theorem at its explicit scope; neither this PR nor a
passing gate changes the normative registry or Canon.

## 6. Dependencies and excluded conclusions

Inherited owners are listed in SOURCE_MANIFEST, including the already
registered automorphism, carry, A4 and nine-step synchronization theorems.
T1 #1476 concerns autonomous auxiliary context without counter/driver access;
the present first-entry chart receives time information from native n.
Scoped T3 #1479 concerns an onto reversible lift of a lossy update on a
complete occupied product; the present maps centralize U without making
U reversible. Neither prior boundary is weakened.

No physical selector, unique cycle/generator, native implementation of T,
apparatus, occurrence law, complete decoder family, measure, continuum,
SI scale or L2-L6 lift is claimed. The running DP5 attempt and its independent
saved-account audit remain separate; no ion experiment is authorized here.
