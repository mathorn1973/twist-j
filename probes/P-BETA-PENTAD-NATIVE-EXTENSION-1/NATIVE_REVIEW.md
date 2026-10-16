# Native proof review and scope reconciliation

**PUBLIC / NON-CANONICAL / prospective L1 proof review.**
Reservation: [#1481](https://github.com/mathorn1973/twist-j/issues/1481).
Date: 2026-10-13. This review was separately reasoned within the same
assisted session, with the supplied proofs and exploratory outputs exposed.
It is neither blind confirmation, external peer review nor a completed
formal execution. This preparation read source text only; it did not import
or execute any supplied scientific script or contact a numerical machine.

The reviewed statement is [NATIVE_PROOF.md](NATIVE_PROOF.md), adapted from
the supplied `NATIVE_EXTENSION_PROOF.md`. Formal audit results remain
pending the new public source pin and recorded first execution.

## 1. Authority and inherited claims

The worktree declares Public Canon v101 ACTIVE, content commit
`421a4ec1daf07c04d19022c1ee219607e83c09a8`. Read-only local hashing confirmed
992352 Canon bytes and SHA-256
`b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`.
Public authority is the declared main/tag, not the imported package.

| Input in Canon v101 | What the native proof uses or retains |
|---|---|
| Section 2, native generator formulas and ODOMETER-INTERNALIZED | Omega=N_0 x F_5^6, existing n and actual Thue-Morse selector |
| U-NATIVE-INVARIANT-AND-NOWRITE | Active conserved centered coordinates are inherited, not newly discovered information retention |
| FIRED-COMMUTATOR-NOGO | Active b,d,e have spatially abelian homogeneous parts; their two-coordinate translation fiber is different from this three-dimensional piston W |
| TM-SHEET-SYNCHRONIZING-GRAPH G3/G4/G7 | Uniform sharp nine-letter synchronization already exists; the supplied n=14 witness and direct recurrence proof refine its presentation |
| TRACEKERNEL-F5-HODGE-BRACKET | The explicit residual B and beta, conditional on its registered closure premise when given the physical dictionary reading |
| TRACEKERNEL-F5-AUTOMORPHISM-BOUNDARY | Aut(beta)=SO(B,5), order120; the faithful-GL2 eight-of-480 boundary remains unchanged |
| U-COUNTER-REACHABLE-AMPLITUDE-CLASS | A conserved chart can attach arbitrary stipulated invertible actions; intertwining does not select a physical target |

Canon's nine-letter theorem is stronger than a bare entrance bound: every
admitted nine-letter factor synchronizes all sheets to the terminal active
sheet. The supplied prose compared chiefly with origin-zero three-step
synchronization. The formal proof now explicitly credits the existing
arbitrary-window nine-letter theorem and its sharp eight-letter obstruction.

## 2. Algebra checked by independent substitution

The fiber decomposition p=4s*1+w is exact because 4*4=1 in F_5. The
three-coordinate inverse is (a,b-a,c-b,-c). Substituting this inverse into
the five six-coordinate formulas gives exactly A,-P,-P,-I,-I and the stated
base changes/translations. In particular c has sum 1-s and translation
h(r); the dependence on r is retained.

A and P commute, square to I, preserve B and have determinant one. Their
four-element group excludes -I by determinant. The full homogeneous image
therefore has eight elements; precisely its four determinant-one elements
preserve beta. The determinant-minus-one elements reverse beta. This is
an abelian C2^3 group; it is not the Canon's distinct nonabelian dihedral
group of order eight in the faithful-GL2 classification. Its bracket
subgroup is the Klein four group.

The image statement is restricted to same-base piston differences. It
does not say the complete six-coordinate generator group is abelian:
c couples r into the piston translation. Thus the canonical silent
commutator [a,c] can remain a nontranslation even though the homogeneous
three-dimensional fiber parts commute. Order-five affine translations
are also compatible with the absence of homogeneous order five.

The active center w_star=3t satisfies 2w_star=t and P w_star=-w_star.
The sign at a counter increment cancels the -I part; the z-sheet switch
cancels the P part of b. These give the conserved coordinate (1).
The four-coordinate center is (1,3,4,2), the old active piston center.

To relate this to the canonical active vector explicitly, put

    A0=p1+p1p, B0=p4+p4p,
    C0=p1-p1p-2, D0=p4-p4p-1,
    epsilon=+1 on z=1 and -1 on z=4,
    V=(A0,B0,epsilon*C0,epsilon*D0).

Canonical V changes by a common minus sign per step. Reconstruct the
centered piston with pair sums A0,B0 and differences epsilon*C0,
epsilon*D0, remove 4(A0+B0)*1, and take difference-basis coordinates.
This fixed linear rank-three map T satisfies K=(-1)^n T(V). Together
with the base sum it is the inherited four-coordinate conservation in
another decomposition. It does not claim recovery of initial information
lost between different base fibers.

## 3. Arbitrary-time and uniqueness quantifiers

The entrance argument uses actual Thue-Morse recursion, not an arbitrary
controlled word. Runs have length at most two; consecutive 01 starts are
at distance at most four; 11 starts are corresponding odd positions at
distance at most eight. Counting both bits of the next pair gives the
uniform nine-step bound from every nonnegative initial counter. The explicit
sheet sequence at n=14 remains outside {1,4} through the eighth step and
enters on the ninth. No finite counter sample is substituted for this proof.

First-entry fiber transport is bijective on each fiber. Pulling the
prescribed active action backward by it proves existence and uniqueness
even though different bases can merge under U. Uniqueness is relative to
fixing (n,s,q,r) and to the specified active action for one fixed C. It
does not classify base-changing actions or arbitrary centralizers.

The affine bracket origin is m=mathcalK^-1(0). The lifted action fixes m;
its homogeneous part is L^-1 C L with L a B-isometry. Consequently C in
SO(B,5) gives a bracket automorphism on displacements at m. A translated
affine map is not a linear automorphism at an unrelated zero. This origin
qualification is necessary and is included in the formal statement.

## 4. Checkpoint-only completeness

Transport through the three entrance edges forces the affine transient
maps (6), even if arbitrary transient bijections were initially allowed.
The a self-loop at z=0 forces [C,A]=0 and fixes every
(2+r,0,1-r). These vectors span ker(A+I). Because A has two distinct
eigenvalues, C is identity on that plane and multiplication by one
nonzero lambda on its complementary line. This establishes necessity
of all four C_lambda; testing those four alone would not do so.

Sufficiency follows from the forced entrance edges, the inverse c edge,
the active conservation and the two a self-loops. Orthogonality requires
lambda^2=1 and determinant one requires lambda=1. Thus the GL class has
four elements, the orthogonal class has I,-A, and the bracket class has
only I. On the active subset alone all GL3 actions still exist.

The concrete C=P mismatch is correct: at s=q=r=0 the forced map sends
w=0 to (2,3,1), whereas a sends that output to (1,3,2). This refutes
that specified checkpoint-only extension, not every conceivable symmetry
of the checkpoint machine.

## 5. T1, T3 and realization remain separate

[T1 at c5c4555a1641cdf39f235642e0e9230274d75d5f](https://github.com/mathorn1973/twist-j/tree/c5c4555a1641cdf39f235642e0e9230274d75d5f/notes/C-U-RAW-RESIDUE-CONTEXT-UPDATE-N)
excludes nonconstant eventually permanent original-residue readout from
the raw receiver using a common finite autonomous source-independent
context. It expressly permits a different supplied driver/counter interface
or a larger observed port. The native lift uses both, so it leaves T1 intact.

A supplied finite future-word context is an evaluation resource. Its next
window needs a newly supplied future bit; the finite alphabet is not a
closed autonomous generator of the aperiodic driver. For linear C, the
scalar epsilon=(-1)^(n+tau) cancels exactly:

    mathcalK_b=epsilon J_b,
    mathcalK_b^-1 C mathcalK_b
        =J_b^-1 epsilon^-1 C epsilon J_b=J_b^-1 C J_b.

The map J_b is determined by the checkpoint base and nine future bits.
Canonical G3 gives exactly 24 admitted length-nine factors, so an externally
supplied alphabet of at most 24 time contexts suffices to evaluate the
entire linear GL3 action on all fibers. This is a concrete upper bound,
not 24 complete apparatus states, a minimum, an autonomous context updater,
a driver-acquisition mechanism or a physical gate. The parity cancellation
is not automatic for arbitrary nonlinear invariant-label permutations.

[T3 at 145266fd4bc0961f9294a5f3eb6e95613b36d43d](https://github.com/mathorn1973/twist-j/tree/145266fd4bc0961f9294a5f3eb6e95613b36d43d/notes/C-U-FIELD-CONTEXT-COMPATIBILITY-N)
excludes a complete reversible lift projecting literally to the specified
nonsurjective fixed-bit context map on every context/helper input. The
present Phi_C are bijective relabelings commuting with a noninjective U;
they are not a replacement bijective evolution. The explicit n=0 merger
in NATIVE_PROOF.md confirms that the original loss between bases remains.
It does not supply T2's retained-contact archive or repair the T3 factor
condition. No field/native encoder is derived.

Finally, the counter-dependent symmetry is not a word in the native
generators. A missing homogeneous operation still needs an explicitly
admitted contact and resources. Since every permutation of 125 conserved
labels lifts as well, the centralizer construction alone cannot select
this Lie bracket, the intrinsic pentad or a physical target evolution.

## 6. Supplied script review and execution boundary

The supplied `native_fiber_audit.py` is exact standard-library code with
top-level loops; importing it would execute those loops. It was read only.
Its literal and decomposed formulas match the proof. Its enumerated
counter domains are n=0..31 for the chart and n=0..4095 for entrance.
Affine-basis checks use zero plus three coordinate units, sufficient for
equality of two already-proved affine maps at each tested base. These
finite domains are not an all-counter proof.

The supplied JSON reports the four counts credited in NATIVE_PROOF.md.
The original prose additionally mentions 25000 active one-step instances;
that separate count is not emitted or separately enumerated by the supplied
native script. It is not carried here as an independently verified result.
The new formal verifier must earn its own recorded gates and outcome after
pinning. This review supplies no current execution PASS, architecture
confirmation or Canon disposition.
