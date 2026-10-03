# P-J-LAMBDA6-DECODER-INTERFACE-2: frozen scope before public execution

Status before execution: candidate-T proof with exact audit; NON-CANONICAL. Action layer L1. Scope: complete lambda-six arithmetic reading/inverse and pure-J data dynamics. The old `P-J-TWO-TRACE-RESIDUE-DECODER-1` is sealed and remains unchanged. This successor has its own public identifier, branch, preregistration and verifier. No scientific execution may occur until the coordinator has committed and pushed this contract, the accepted code, and the independent review verifier, and recorded the public pin and SHA-256 hashes.

## 1. Equation and claim

In `O=Z[zeta5]`, `lambda=1-zeta5`, `J=1+zeta5^2`, use `D6(alpha)=(S(alpha),S(J alpha),alpha mod lambda^6 O)` on every nonzero integral scalar of norm at most 941. Provide an exact encoder, total image recognizer/inverse, canonical strip representative and signed integer J exponent, plus mutually inverse data maps T6 and T6_inverse intertwining multiplication by J and J^-1. Six digits are canonical lambda-adic digits with carries, not coordinates of the additive vector space F5^6.

The analytical claims and exact quantifiers are frozen in PROOF.md. They include termination for nonrepresentable input, both half-open strip boundaries, exact ideal transport, image soundness/completeness, the characteristic-25 obstruction to an additive identification with F5^6, and the first sufficient depth six within the original ideal-reading sequence. No broader norm bound, prime, geometric programme or physical U implementation is included.

## 2. Code and interface

`decoder.py` implements exactly the API in INTERFACE.md: `encode(alpha)`, `decode(s0,s1,digits)`, `T6(s0,s1,digits)`, and `T6_inverse(s0,s1,digits)`. The returned frozen Decoded record has `coefficients`, `strip_coefficients`, `unit_exponent`, and `norm`. Scalar and digit inputs accept tuple or list of the exact length and strictly integer entries; bool is excluded. Outputs are tuples. Input digit residues must already be in `[0,4]`, with exactly six digits. Malformed/nonimage decoder input raises InvalidReading, a ValueError subclass. Data steps accept every well-formed reading, including those outside the image. No silent coercion occurs.

The implementation derives a lazy finite index from every vector in the proved complete box `[-8,8]^4`, filtering the original strip and norm bound. The cache is a deterministic consequence of that enumeration, not an external precomputed oracle. Importing the module performs no scientific enumeration. The residue implementation uses exact repeated lambda division and canonical remainders. Every normalization step transports traces and residue together.

`primary.py` is the accepted author audit. Its arithmetic oracle independently uses polynomial convolution/reduction, Galois conjugation and an exact inverse multiplication matrix for lambda^6. It does not call author digit division to define expected residue classes. An independently authored `independent_decoder.py` is separately frozen before reading either author program and included by the coordinator at the public pin. The formal exact command is `python3 probes/P-J-LAMBDA6-DECODER-INTERFACE-2/verify.py` from repository root. That coordinator wrapper first enforces `INPUTS.sha256` and then executes both `primary.py` and `independent_decoder.py`; both run on both required CI architectures. The wrapper, manifest, proofs and all programs are included in the same public freeze. No post-pin code edits are permitted.

## 3. Carrier and disclosed data

Freeze coefficient order `(1,zeta,zeta^2,zeta^3)`, `N=u^2+uv-v^2`, `S0=2u+v`, `S1=3u-v`, and `B941={0<=v<u,1<=N<=941}`. The v=0 boundary is included and u=v excluded. The source proves all strip coefficients lie in `[-8,8]`; no sampled, restricted or enlarged carrier is allowed. The full inverse domain includes all integer J translates of the strip, with negative exponents admitted.

Public authority baseline is `5e872c22a18043c8126945a982efad55472cea82`, Public Canon v97. Inherited public claims are J-TWO-TRACE-RESIDUE-INVERSE [T], J-OBSERVED-SCALAR-CODE-CAPACITY [T], and C20-TEICHMULLER-SPLIT [T]. Public probe source `P-J-TWO-TRACE-RESIDUE-DECODER-1/PROOF.md` has SHA-256 `491f568d1c03c20578af7858cccae40a97f0ff5b83af272e2ec49295a96a3fc0`. The source strip has 3150 elements and compact sorted-coefficient SHA-256 `6a08d7de33b4cadb615f942b37202540dd6dea0f59f2412ffb822389c7c1cdab`.

The original local ramified census and proof are already exposed inputs, preserved in the separately published original bundle with original records intact. The eight known counts are `(256,1170,1384,2603,2882,3150,3150,3150)`; they are not new blind predictions and are not recomputed as a new eight-depth census here. The norm argument for k>=6 and the three exact depth-five pairs in PROOF.md are known analytical inputs. This probe audits their direct certificates and completes the interface; it does not upgrade intermediate counts by assertion. The author has read the older mod-25 code. Independent reviewer code exposure is recorded separately.

## 4. Exact audit and systematics

Use Python 3.12 standard-library exact integers and Fraction only. Floating-point objects occur solely as deliberately malformed type fixtures and never in scientific arithmetic. No random sampling, fuzzing, external numerical library, measured embedding, logarithm, or host-dependent scientific input is allowed. The verifier prints deterministic compact JSON with sorted keys and one final LF; elapsed time, paths and machine metadata are not scientific stdout.

Freeze these audits before execution:

1. Build lambda^6's integer multiplication matrix by generic polynomial multiplication; invert with Fraction; require determinant 15625, integral inverse numerator after multiplying by 15625, and both inverse identities. Its modular inverse-coordinate signatures define independent exact ideal classes.
2. Enumerate all `5^6=15625` canonical digit strings. Independently reconstruct their representatives, require distinct lattice signatures, and compare every author digit conversion/representative. Check 5 nonzero and 25 zero in the quotient.
3. Enumerate the entire `17^4=83521` coefficient box by independent polynomial arithmetic. Require the inherited 3150 strip elements and exact compact-strip digest. Recompute each included scalar's two traces and norm by Galois ring operations and compare its encoded datum with the independent lattice class.
4. Exhaust every normalized arithmetic trace pair `u=1,...,46`, `v=0,...,u-1`, `1<=u^2+uv-v^2<=941`, and every one of the 15625 residues. These are all normalized trace candidates before representability, because S0<=92 implies u<=46. Require acceptance with exact beta, exponent zero and norm precisely for the independent scalar image; require InvalidReading for every other key, including nonrepresentable trace pairs. Require such nonrepresentable pairs are actually exercised. For each normalized pair choose the lexicographically first nonimage residue and transport it independently through exponents -31 and 31; both must still be rejected.
5. On all residue classes and each signed trace pair `(-2,7)`, `(0,0)`, `(2,3)`, compare both data operators with independent ring multiplication and both inverse compositions. This covers the entire finite residue action even outside the image.
6. For every strip scalar and every exponent in `(-31,-7,-1,0,1,7,31)`, form the original scalar independently by ring multiplication. Require exact encoder agreement, correct original/strip/exponent/norm decoding, and forward/backward intertwining. Every strip scalar with v=0 also tests its excluded u=v representative under J^-1. Unit seeds at exponents -257 and 257 exercise larger positive and negative integers; these finite audits do not replace the all-integer proof.
7. Exercise strict type/shape/canonical-range rejection, including bool, float, string, None, generators, wrong-length tuples, noncanonical digits, zero and norm-1296 scalar inputs. Exhaust initial arithmetic rejection conditions over trace pairs in `[-20,20]^2`, and named norm-zero, incompatible-residue, above-bound, nonintegral and very-large-integer fixtures. Tuple/list equivalence and tuple outputs are required by the interface.
8. Directly verify the three already disclosed depth-five quotient identities, common traces, norm/strip membership, and their thirty disjoint root-of-unity collision pairs. Do not search for substitute witnesses or infer a new full lower-depth count.

No runtime speedup is claimed. The workflow's 600-second verifier timeout includes the independent review audit. Proof totality means mathematical termination on finite arbitrary-size inputs, not an unlimited practical resource promise.

## 5. Failure threshold and disposition

Zero tolerance for any mismatch, incomplete domain, bad residue equivalence, wrong signed exponent, failure of either data inverse, acceptance outside the exact image, rejection inside it, incorrect boundary handling, original strip anchor mismatch, or violated certificate. Any falsifier stops the verifier with nonzero exit; preserve exact stdout/stderr, public pin and failing case. No threshold, carrier, endpoint, norm bound, witness or implementation may change after the formal pin. A failed version receives its proper public disposition; any correction requires a new identifier/pin under repository policy.

On success, save exact stdout as EXPECTED.txt, record public pin, file hashes, actual command, neutral platform/architecture, Python version, exit status and output hashes in RUN.md, and state earned scope in RESULT.md. The required clean x86_64 and aarch64 jobs must produce byte-identical stdout against that same EXPECTED.txt with matching verifier bytes and empty stderr. Independent proof review and the two-architecture computation gate are separate requirements.

## 6. Decision and exclusions

PASS supports the frozen complete arithmetic interface and its explicit proof scope. The exact minimum depth is established from the disclosed analytical norm bound and thirty-pair certificate relative to the inherited strip cardinality, not from assuming a census count. This is a refinement alongside the sealed mod-25 decoder. It supplies no preferred physical codebook, finite storage of unbounded trace integers, noise correction, acquisition/energy benefit, source-controlled native contact, realization of U, or higher-layer bridge. Publication and any Canon fold remain separate coordinator actions.

## Abandoned predecessor, disclosed before this successor pin

P-J-LAMBDA6-DECODER-INTERFACE-1 was pinned at
561679f65aa4b0a534cd94129fe243ac8fc9936b but never executed. Git normalized
REVIEW-FREEZE.json after its raw-byte manifest was computed, invalidating
custody. The identifier was retired with Status: ABANDONED in commit
32c8ffe2. No scientific counterexample or result was obtained. This successor
changes only the probe identifier and packaging/custody, preserving the same
mathematical carrier, API, code algorithms, test domains and thresholds.
Its per-directory .gitattributes disables text rewriting; staged and committed
Git blobs must match the exact manifest before execution. The reviewer's
original freeze and code remain byte-identical, with their historical ID1
mapping preserved; independent_decoder.py is mapped unchanged into this ID2.
