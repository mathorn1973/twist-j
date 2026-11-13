# Native piston Gram descent: result

Status: COMPLETE / NON-CANONICAL / L1.
Analytical claims: candidate-T. The finite classification is candidate-C from
the local runs alone; its proposed candidate-T disposition requires the
unchanged public x86_64/aarch64 workflow against the committed EXPECTED.txt.
No Canon status or cross-layer closure is created by this probe.

## 1. Decision

The full-domain native step does not descend through either preregistered
reading, with the actual counter retained:

```
R_H  = (q,r,A,B,C),
R_HD = (q,r,A,B,C,D),
H = X X^T = ((A,B),(B,C)), D = det X.
```

Both positive assertions H_RAW_DESCENT and H_ORIENTED_DESCENT are FIRED.
The exposed nonzero-determinant witness was confirmed exactly. The negative
statement has the direct proof in PROOF.md, independently reviewed before
execution, and is also covered by both complete finite implementations.

The smallest counter-independent common completion is almost the whole
checkpoint space. It has 15605 classes on 15625 checkpoints: 15595 singleton
classes and ten classes of size three. The required extra-label alphabet is
exactly 16 for GRAM and exactly 8 for ORIENTED.

These minima apply to the frozen class of present-checkpoint readers on the
full N0 x F5^6, with n retained. They do not claim a minimum for readers
depending on n, restricted prepared domains, or physical memory apparatus.

## 2. Complete finite classification

| Quantity | GRAM | ORIENTED |
|---|---:|---:|
| Initial reading classes | 2250 | 3775 |
| First strict refinement | 15591 | 15595 |
| Second strict refinement | 15604 | 15605 |
| Third strict refinement | 15605 | already stable |
| Terminal classes | 15605 | 15605 |
| Terminal singleton classes | 15595 | 15595 |
| Terminal classes of size three | 10 | 10 |
| Initial fibres split by T0 | 2175 | 3700 |
| Initial fibres split by T1 | 2175 | 3700 |
| Sharp extra-label alphabet | 16 | 8 |
| Constructive tagged transition checks | 31250 | 31250 |

These are refinement depths under the common pair of one-step maps. They
are not claimed as observation-window lengths along one Thue-Morse orbit.

The terminal partitions are identical, not merely equal in size. Indeed,
R_HD refines R_H. The coarsest common congruence for R_HD must therefore
refine the one for R_H, by the minimality theorem in PROOF.md. Their equal
finite class counts force equality. This argument, rather than the absence
of a cryptographic collision, establishes the equality of the partitions.
Their independently reproduced custody hashes also agree:

```
partition_sha256:
9d396a7cdcbefb472aacb52783b314599a83313eaa2a46db049f92aaef320882
transition_sha256:
283d923145ebcd552e1f11e7b40a4e08d4aaf1328d6257da299247aedd27b082
```

The complete size and ambiguity histograms and maximal-fibre representatives
are in EXPECTED.txt. For example, the first maximal GRAM fibre has q=r=0
and H=5I, with sixteen terminal blocks. The first maximal ORIENTED fibre
has q=r=0, (A,B,C,D)=(0,0,5,0), with eight terminal blocks. The programs
construct tags by increasing least-member index within each original fibre
and check the resulting two transition maps on every checkpoint.

Consequently, the determinant reduces the worst additional-label alphabet
by a factor of two, but does not reduce the final coarsest common completed
partition. This is a statement about the two specified finite readers.

## 3. The native counterexample

At n=0 the inputs are

```
x=(1,0,0,4,0,4), y=(4,0,0,1,0,4).
```

Both have z=4, q=0, r=4, H=I and D=-1. They both select e under the actual
native selector. Their successors are

```
T0 x=(1,1,3,0,2,2), (A,B,C,D)=(2,-2,4,2),
T0 y=(3,1,3,3,2,2), (A,B,C,D)=(5,2,8,6).
```

Thus the obstruction is present with the same selector and the same
nonzero oriented determinant. Its source is already visible in X and -X:
both H and the two-dimensional determinant lose the common sign, while
the selected affine native step can distinguish it.

## 4. Separately declared centered factor

All tests of the centered comparison passed on S14={x:z in {1,4}}. The
common fixed piston of b,d,e is p*=(1,3,4,2). Subtract p* in F5 and only
then take the balanced lift W. Its row Gram is H*, and D*=det W.

| Control t | Trace z | Native generator | Next trace | W update | D* update |
|---:|---:|---|---:|---|---|
| 0 | 1 | b | 4 | -sigma_x W | -D* |
| 0 | 4 | e | 4 | -W | D* |
| 1 | 1 | d | 1 | -W | D* |
| 1 | 4 | b | 1 | -sigma_x W | -D* |

For H*=((A*,B*),(B*,C*)), the integer quadruple

```
Q=(A*+C*, A*-C*, 2B*, 2D*)
```

satisfies Q0^2-Q1^2-Q2^2-Q3^2=0. Under b its second and fourth coordinates
change sign; under d/e it is unchanged. Hence (n,x)->(n,z,Q) is an explicit
factor of the actual native step on the declared stable sheets.

There are 302 realizable (z,Q) records on these sheets. Ten checkpoints
have Q=0. The audit covered all 6250 stable-sheet checkpoints, all 12500
controlled stable transitions, and all 15625 origin heads through actual
counter bits 0,1,1. Every origin head ends with trace 1, as inherited from
the existing native entrance theorem.

With chi(1)=1 and chi(4)=-1,

```
Q_flat=(Q0,chi(z)Q1,Q2,chi(z)Q3)
```

is invariant under both controls. The disclosed change of sheet frame
removes the two-valued action. PROOF.md relates this reading to the already
registered invariant V, so the mechanism is an explicit quadratic
specialization of U-NATIVE-INVARIANT-AND-NOWRITE.

The real Gram matrix still has three coordinates. The fourth cone
coordinate here is the separately retained signed determinant. The result
does not identify that real Gram with a general complex Herm2 carrier.
The nontrivial cone action is a spatial half-turn; it supplies no boost.
Q0 is an invariant quadratic readout, not the native counter or a measured
energy. Physical space, time, photons and apparatus retain their existing
bridge obligations. The centered stable-domain factor does not repair or
replace the separately declared full-domain raw readers.

## 5. Evidence and disposition

- Builder: iterative canonical partition refinement of literal native maps.
- Blind breaker: independently assembled affine matrices and backward
  distinguishability of all pairs within the initial reading fibres.
- Both exact first runs exited zero with empty stderr. The full stdout was
  byte-identical: 2303 bytes, one LF-terminated line, SHA-256
  1efb8cfdc2c2c6c157c77913a847476c4790f44ecfae23f0d08b9fbf325a5599.
- Each implementation audited all 78125 generator involutions, all 625 raw
  piston identities, both full reader classifications and the independently
  declared centered controls. Source and execution custody are in RUN.md
  and INDEPENDENT.md.
- The required public workflow must reproduce the pinned accepted verifier
  against EXPECTED.txt on x86_64 and aarch64. Local agreement alone is not
  represented as the architecture gate. Its public result belongs to the
  reviewed PR head and the associated workflow, not a new local execution.

The fired positive descent assertions are retained. No threshold, source,
domain, equality or native map was changed after pinning. No singleton
terminal partition was presumed: the ten surviving triples are part of
the result. Canon, registry, gates, workflows and predecessor probes are
unchanged. Promotion requires a separate reviewed public fold.
