# Independent static pre-execution review

2026-10-04. NON-CANONICAL. Disposition: **STATIC ACCEPT of the corrected
scientific candidate**, subject to the prospective administrative pin and
public byte readback required by PREREG.md. This is not an execution result,
an experimental certificate, a Canon promotion, or release of the #1359 HOLD.
The accepted scientific programs have execution count **zero** at this review.

## Review independence and exposure

A separate reviewer agent authored `verify_independent.py` from the target,
source-table interface and disclosed expected report without reading
`verify.py`. Its method uses ordered integer CSV rows, explicit source
custody, polynomial exponent vectors and swap-orbit effects. The primary
uses named CSV fields, multiplicity counters, another polynomial
representation and an exact matrix projector certificate. This is separately
authored implementation evidence, not a claim of an independent laboratory
or a blinded discovery.

The expected history counts, symbolic energies and one-half obstruction were
exposed analytical context. The source CSV files are previously published
evidence, already read before this new probe. No new dynamical simulation or
pulse search was performed during preparation. After the independent
implementation was delivered, the coordinator authorized this reviewer to
read the primary code for static integration review.

The reviewer inspected PREREG.md, MODEL.md, PROOF.md, SOURCES.md, README.md,
both scientific programs, and the archived source schemas and relevant
rows. Both programs passed `ast.parse` without being imported or executed.
The selected source Hamiltonian, closure period and common rotation form
were also checked against [Hrmo et al., Eqs. (1), (5) and adjacent
text](https://www.nature.com/articles/s41467-023-37375-2). That source does
not supply this contact obstruction or a complete fourteen-ion device.
Final INPUTS.json construction, its verifier anchor, Git ancestry, remote
readback and recorded file hashes are subsequent administrative checks.

## Physical premises and analytical argument

The model names actual five-level carriers and uses the same fixed
dictionary on the two active ports. The restriction to identical real
light-shift profiles and coupling magnitude is explicitly an assumption
of this candidate. Arbitrary constant spatial phases are retained. The
model does not equate a raw instantaneous Hamiltonian symmetry with the
symmetry of the completed loop.

The Magnus sign and factors were checked directly. For
`L(t)=eta/2 [A exp(-i delta t) a^dagger-A^dagger exp(i delta t) a]`,
normality of A gives

```text
[L(t1),L(t2)] = -i eta^2/2 A A^dagger sin(delta(t1-t2)).
Omega2(t) = -i eta^2 (delta t-sin(delta t))/(4 delta^2) A A^dagger.
```

The integrated first term has coefficient
`eta(1-exp(-i delta t))/(2 i delta)`. It vanishes after the declared
period. The commutator is central relative to these generators, so higher
Magnus terms vanish. Resolving the finite diagonal A into scalar
displacement blocks justifies the ideal oscillator identity without a
finite Fock cutoff. This is a result about the adopted harmonic model;
it provides no unbounded-excitation validity claim for a physical trap.

The completed phase contains
`D_S^2+D_Q^2+2 cos(phi_S-phi_Q) D_S D_Q`, which commutes with port
interchange. Common rotations and the stated common drift preserve this
property. Finite products therefore commute with `P_ports tensor I_rest`.
Using every such commuting unitary as an enlarged class is legitimate
for a negative result, but not evidence that all these unitaries are
available from the experimental pulses.

At each of the five actual histories with a2=4, the exact coded active
entry is |00>. A rank-one reduced state forces factorization from the
inherited remainder. This does not require the remainder to be pure,
common across histories, fresh, or uncorrelated internally. The two
fixed readout effects |41><41| and |14><14| are exchanged by P and are
orthogonal. The output probabilities are equal and sum to at most one.
Thus each such history has unconditional correct-port probability at
most one half. Full-state success cannot exceed that necessary-port test.
The worst error is defined over all 25 actual histories.

The trace-distance extension uses normalized complete output states and
the same success effect. Its probability difference bound is valid even
when inherited auxiliaries contain correlations. It earns no numerical
model-error value. The optional input-error term correctly requires a
full-state premise and follows from contractivity and the triangle
inequality.

## Exact code audit and corrections before pinning

The source-reading paths refer to the sealed predecessor tables. No
predecessor executable is imported. The independent reader fixes raw CSV
hashes, schemas, canonical integer domains, ordering and complete coverage.
It checks that contact inputs match the corresponding boundary states,
that source outputs are inherited, and that unchanged receiver coordinates
remain unchanged. It then groups every original state coordinate, removing
only the two input labels. The primary derives the same shared report.

Two executable mistakes were found and corrected by static reasoning
**before any public pin or scientific execution**:

1. The first independent draft incorrectly required the particular four
   histories `{0,1} x {0,1}` to coincide at n=7,8 as well as n=9. Reading
   the existing CSV showed that the earlier maximum fibre size four does
   not identify that particular four-history set. The specific-set check
   now applies only at n=9. Maximum fibre sizes at every boundary are still
   calculated from all rows. No expected count or scientific threshold was
   changed to fit a new run.
2. In the primary PSD certificate, let `Pplus=(I+P)/2`, `B=2 Pplus` and
   `Q=Pplus-2 Pplus E41 Pplus`. Then `Q4=4Q=2B-2B E41 B`. The initial
   draft omitted the second factor two. The corrected code uses
   `2*bmat-2*b_e_b`. Since `2 Pplus E41 Pplus` is the rank-one projector
   onto `(|41>+|14>)/sqrt(2)`, Q is the projector of rank 14 in the
   symmetric subspace. The corrected exact identities `Q4^2=4Q4` and
   `trace(Q4)/4=14` have the intended certificate meaning.

The polynomial tests use symbolic variables, including the phase cosine;
they are not samples of physical angles or pulse parameters. The 625
common-rotation entries compare the complete matrix monomials. Neither
test replaces the analytical all-sequence proof. The two different fixed
dictionaries conjugating the logical target to physical SWAP are an
appropriate boundary control, not an authorized mid-history recoding or
a synthesized SWAP gate.

The symbolic energy coefficients follow from the four endpoint terms
under the declared E0=0 normalization. The n=9 information lower bound
requires identical pure coded outputs in a fixed data/remainder
factorization. The proof separately states the weaker fibre-capacity
conclusion for coarse readings. Neither result supplies a pathwise work
budget or sufficient memory dimension.

The primary checks the frozen input manifest before importing the
independent program. The manifest must exclude itself and the primary
verifier that contains its hash, avoiding a cyclic hash construction.
The public Git pin binds those two files; the run record also identifies
the accepted primary bytes. This separation is now explicit in PREREG.md.

## Accepted scope and remaining execution gate

No unresolved scientific or code-path blocker was found in the corrected
candidate during this static review. Its decision is restricted to the
specified completed-loop common-control class, exact coded entry, and a
real isolated post-contact endpoint. It excludes a worst input error
strictly below one half there. It does not exclude individually addressed
controls, unequal fixed dictionaries, asymmetric resources, interleaving
inside unclosed loops, or a combined native/contact endpoint.

The candidate does not supply finite resources through preparation and
both contacts, a fourteen-ion Hamiltonian, all-mode closure, inherited
battery charge, measured error bounds, protection of the first archive,
or derivation of the imported quantum model from J. These limitations are
explicit and necessary; a successful forthcoming exact audit must not be
reported as successful physical realization.

The coordinator must finish the non-circular manifest, pin and push all
accepted bytes, verify the public readback and clean accepted content, and
only then execute on Linux. EXPECTED.txt, RUN.md and RESULT.md must record
that actual later execution. Architecture checks and any subsequent
scientific acceptance remain distinct from this static disposition.
