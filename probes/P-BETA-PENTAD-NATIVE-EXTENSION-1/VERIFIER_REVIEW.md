# Accepted verifier: pre-execution static review

**PUBLIC / NON-CANONICAL. No execution result is asserted here.**
Reviewer: coordinating assistant, A. M. Thorn session 2026-10-13.
This is a review within the same assisted session, not blind or external
review. The targets and submitted exploratory outputs were exposed.

Reviewed accepted `verify.py`: 20881 bytes, SHA-256
`a454e4ae06a03f6c90961efbfea28272eaa0e4de95fd0270183e7a2011a3badf`.
The three byte-identical helper hashes match SOURCE_MANIFEST and the
wrapper's hardcoded source bindings. The source archive's twelve checksum
entries match the twelve other original members. The archive and pasted
summary are preserved separately from the public scientific worktree.

The wrapper hashes all three helper sources before any is executed, refuses
an optimized interpreter and repeats the relevant hash check around each
execution. This keeps the helpers' assert checks enabled and their source
identities fixed. `runpy` executes only these reviewed hash-bound files.
Their exploratory output JSONs are not read. The wrapper captures helper
stdout, rejects stderr and duplicate JSON keys, checks semantic counts and
coordinate bindings, and emits a sorted compact ASCII JSON report.

The original scripts use itertools, collections and json, and write only
stdout. The new wrapper uses standard-library source reading, hashing and
in-process execution; it has no network, subprocess, numerical solver or
filesystem-writing interface. Bytecode writing is disabled. Administrative
AST parsing and hashing have been performed; no candidate was imported or
executed in this pre-execution review.

Mathematical source review checked the following additional certificates:

- The RREF equations assemble `CA-AC=0` with the correct row-major
  coefficients, plus all fifteen scalar equations `C v_r=v_r`. Complete
  elimination enumerates the entire affine solution space, rather than
  checking only the supplied four invertible matrices. Rank eight leaves
  one free parameter; direct substitution checks every enumerated solution.
  The eigenspace projector and determinant/orthogonality classifications
  are independently checked. Necessity of these equations for the specified
  extension class is established in NATIVE_PROOF, not assumed to follow from
  a candidate census.
- The active invariant check covers all 6250 active checkpoints, both bits
  and both counter parities, for 25000 instances. It uses literal native
  formulas and an independently written chart. The P/T witnesses retain
  the exact forced images and failed a-self-loop comparison.
- The four `mu^4(ab)` blocks exhaust nine-letter factors by the inherited
  substitution-language argument. All four adjacent pairs occur in the
  displayed fixed-point prefix. The certificate enumerates all 24 words
  and all 120 initial-sheet entrance cases. This supports an externally
  supplied context upper bound; it does not construct an autonomous updater.
- Group generation distinguishes `<A,Phi,T>=SO(B)` of order120 from
  `<A,Phi,-I,T>=O(B)` of order240, preserving the precise meaning of the
  supplied helper's abbreviated 120-valued field.

The helpers' arbitrary-counter chart census remains n=0..31 and their
entrance census n=0..4095. Their independently assembled automorphism sets
are compared as sets, and their A4 frame labels are compared in coordinate
order. Reports retain the bounded ranges. Universal entrance, symmetry
uniqueness, the complete extension theorem and the parity-cancellation
argument remain written proof obligations. No physical selector, native
implementation, retained archive, reversible U or higher-layer lift is
inferred.

Disposition: no static blocking defect found at this frozen scope. Publish
and read back the complete source before first formal execution. A true
mathematical mismatch, infrastructure failure or altered byte must retain
its first evidence and the preregistered disposition.
