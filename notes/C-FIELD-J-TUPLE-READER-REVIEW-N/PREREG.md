# C-FIELD-J-TUPLE-READER-REVIEW-N

**PUBLIC, NON-CANONICAL. Independent prospective L1 review; unexecuted.**
Owner: root/tuple_reader_breaker, a fresh reviewer session. Original work
under Apache-2.0. Prepared 1 October 2026. Coordination:
[issue 1323](https://github.com/mathorn1973/twist-j/issues/1323).

## 1. Authority, target and exposure

Public Canon v96 at public main base
`44423153eee6259c7277eec5f5adbed9679f9146` is the normative basis; content
commit `d63de7e7345cf5fa5ab344654aafb7238d6d8bca`, canon/CANON.md
873495 bytes, SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
Root has revalidated remote authority, ownership and required checks.
The reviewer read STATUS, POLICY, AGENTS, CORE, FRONTIER and the scalar
reader Canon premises, including the norm-separation proof.

The sole new target specification is
`notes/C-FIELD-J-TUPLE-READER-N/PREREG.md` at public commit
`cba479dcc05fbcadec70007a5a8642547372c1f2`, Git blob
`6fb917541e00d6edeaeb68bea79176dd7dd9e9a1`, SHA-256
`bfa94e9b5d471f65fe3243e2abde2837a40247f0518c09677e6d0fbf31752fb4`.
Root verified public byte readback before supplying this specification.
The only additional noncanonical mathematical inputs read were sections
1-4 of the predecessor PROOF.md at
`49dfad177c6ab698b5751de3e56629508982b05f` and sections 1-2 of its independent
DERIVATION.md at `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`, as explicitly
admitted by the target. These inputs do not gain canonical status.

The prior false rejection of tuple subclasses, the exposed census 291,
shells (1,20,30,60,60,120), and maximum norm 31 are known regression targets.
An agent-status listing also exposed the earlier review's rejection and
finite check counts. No successor author proof, implementation, outputs,
diff, or earlier implementation was read. No module was imported and no
scientific computation was executed. A child reviewer provided syntax-only
static analysis of hostile metaclasses; it saw no author code. This is
independence of derivation and implementation, not result-blindness.

## 2. Exact claim and carrier

For a in Z^4, retain exactly the target's e0,e1,C,K5 and E5 definitions.
The output is (a,Ca) for the unique a in K5 with the normalized key, and
None otherwise. Equality is ordered integer equality. The source object
contract admits actual tuple subclasses, inspects their underlying builtin
tuple slots, admits exactly builtin ints, and rejects every other object
or shape without invoking its hooks or mutating its metadata. A forged
__class__ does not confer membership. Equivalent normalized keys must give
identical plain builtin tuple outputs. Zero remains in the domain.

The review's DERIVATION.md proves normalization and totality on this complete
object contract, and proves the inverse from a pre-enumeration coefficient
bound and the inherited exact norm argument. The finite audit supplements
that proof; it does not enumerate Python classes or prove unbounded claims
from examples. Builtin replacement, interpreter/process failure and exhausted
resources remain excluded exactly as in the target; there is no fixed
bit-cost claim for unbounded integers.

## 3. Independent code, data and systematics

break.py is standalone standard-library Python 3.10+, with no randomness,
floating point, network, project imports or output-file writes in its own
audit. Its independent inverse enumerates at most four residue-compatible
coefficient lifts and evaluates coefficient forms. Its forward image uses
the independently transcribed C, A_f and B_f field matrices: H(Ca) and
H((I+A_f^2)Ca), over the proved 1225-point coefficient box. Every box point
also checks the two coefficient forms. The complete image must have 291
states, shells (1,20,30,60,60,120), maximum norm 31 and no duplicate keys.

Exhaust all 52500 keys in [0,5] x [0,13] x {0,...,4}^4, and the 18750
outside keys with e0 in {-1,6}, e1 in {-1,0,1,13,14,10000}, or e0 in
[0,5], e1 in {-1,14,10000}. For every semantic key use all sixteen
outer/inner combinations of builtin tuple, plain tuple subclass, hostile
tuple subclass and a subclass with hostile metaclass. Thus each reader has
1140000 exhaustive calls. Hostile methods record invocation before raising,
so catching their exception does not conceal the failure.

The fixed code additionally specifies malformed shapes and components,
all integer-subclass and boolean positions, fake tuple objects with forged
or hostile __class__, hostile values in wrong slots, lying length/index/
iterator views, metadata preservation, negative and huge integer energies,
two original zero-subclass counterexamples, valid-to-valid residue changes,
and multiple nested tuple-subclass depths. Malformed objects are never
formatted for diagnostics. Representative hostile hooks include normal
attribute access, length, indexing, iteration, comparison, hashing, truth,
conversion, representation, containment and pickling, plus metaclass MRO,
bases, equality, subclass and instance hooks. Actual nonterminating hooks
are covered by the universal bypass proof rather than entered in the run.

## 4. Freeze, execution and author comparison

Before science execution or author comparison, root commits and publicly
pushes PREREG.md, DERIVATION.md and break.py, then verifies public bytes and
records their hashes. Only static inspection and AST parsing are permitted
before that signal. The frozen files are never rewritten after their pin.

After that public freeze, root supplies the immutable successor author
implementation pin, path, SHA-256 and reader function name. The optional
comparison mode validates that exact file hash before loading its source as
a module without running its __main__ block. The independently frozen oracle
and fixtures are unchanged. No result-driven discovery or test amendments
are permitted under this review identifier.

Prospective commands, from the repository root on Linux-compatible runtime:

    python3 notes/C-FIELD-J-TUPLE-READER-REVIEW-N/break.py
    python3 notes/C-FIELD-J-TUPLE-READER-REVIEW-N/break.py --candidate AUTHOR_FILE --sha256 AUTHOR_SHA256 --reader AUTHOR_READER_NAME

Root binds those three comparison arguments to the public author pin in the
run record and performs serialized runs under the existing 600-second
envelope, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Exact stdout, empty stderr, exit code, neutral
runtime, hashes and byte counts are recorded only after actual execution.
Notes-only CI is not a scientific run or a two-architecture result.

## 5. Fixed decision and scope

Zero tolerance: any false acceptance/rejection, wrong or non-plain output,
hook invocation, input mutation, crash, inequivalent results for equivalent
stored keys, incorrect arithmetic identity, image collision or census
discrepancy rejects the corresponding contract. Missing pin, changed bytes,
runtime failure or absent evidence without an exact negation is integrity
STOP. A failing example is retained and the domain is not narrowed afterward.

The final review separately distinguishes the universal proof from finite
audit and author implementation behavior. No Canon files or physical owners
change; no scope lifts, scientific promotion, transport implementation or
reinterpretation of the predecessor's rejection is authorized.
