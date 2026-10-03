# C-FIELD-J-TUPLE-READER-N

**PUBLIC, NON-CANONICAL. Prospective L1 reader-contract successor; unexecuted
and unreviewed.** Owner: A. M. Thorn / root/algebra_builder session.
Coordination and predecessor disposition: [issue #1323](https://github.com/mathorn1973/twist-j/issues/1323).
Original work under Apache-2.0. Prepared 1 October 2026.

## 1. Predecessor, basis and exposure

This is a new narrow candidate. It does not edit, resume or relabel the
immutable C-FIELD-J-ENERGY-READOUT-N pin
`49dfad177c6ab698b5751de3e56629508982b05f`. The coordinator reported rejection
of that candidate's B Python input contract: its preregistration admitted
tuples, including subclasses, while its implementation required exact builtin
tuple types. Consequently both a tuple-subclass outer datum and a subclass
residue tuple could falsely reject an otherwise valid zero datum. The
mathematical bound, injectivity and inverse reasoning survived review, as
did the unrelated A, C and D claims. The original failed contract remains
failed; this candidate supplies a separately specified implementation.

Admitted mathematical inputs are only sections 1-4 of the predecessor
[PROOF.md](https://github.com/mathorn1973/twist-j/blob/49dfad177c6ab698b5751de3e56629508982b05f/notes/C-FIELD-J-ENERGY-READOUT-N/PROOF.md)
and sections 1-2 of the independent review
[DERIVATION.md](https://github.com/mathorn1973/twist-j/blob/c404c1c53a9af3ce1b2523de8a56a270e082e7c9/notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/DERIVATION.md)
at `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`. These remain candidate-level
inputs, not Canon promotion. Their canonical basis remains public v96 at
`44423153eee6259c7277eec5f5adbed9679f9146`, content
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`, CANON.md 873495 bytes and SHA-256
`eb2a7bc1c7e38e130544b9fef4c0f05443df01484bdb55a52fc10b427fcee0a2`.
The coordinator verifies the live authority, ownership and public pin.

The builder authored the predecessor and has seen its verifier, proof,
completed stdout and the review derivation. The known census is 291 states,
shell counts (1,20,30,60,60,120), maximum norm 31. These are exposed regression
targets, not new discoveries. No predecessor Python input behavior is assumed
correct, no predecessor module is imported, and no successor execution has
occurred. The earlier absent exploratory attachments remain absent inputs.

## 2. Exact mathematical carrier

For a=(a0,a1,a2,a3) in Z^4 put

```text
e0(a)=sum a_i^2-a0*a2-a0*a3-a1*a3,
e1(a)=sum a_i^2-a0*a1-a1*a2-a2*a3,
C a=(a1,a2-a3,a0-a1-a3,a1-2*a2+a3),
K5={a:e0(a)<=5},
E5(a)=(e0(a),e1(a),(a0 mod5,a1 mod5,a2 mod5,a3 mod5)).
```

Equality is literal ordered integer-coordinate equality. The admitted proofs
give positive definiteness; unique zero; the containing box
[-3,3] x [-2,2] x [-2,2] x [-3,3]; nonzero norm
N=-e0^2+3e0*e1-e1^2 in [1,31]; and E5 injectivity because 5^4>16*31.
Every valid key has e0 in [0,5], e1 in [0,13]. The field returned is y=C a.
The norm-941/3125-label and modulo-25 theorems retain their existing scopes.

## 3. Complete Python input semantics

The reader accepts an already constructed finite Python object. A tuple
means a builtin tuple or an instance of any actual subclass of builtin
tuple. Nominal membership uses the actual dynamic type and builtin tuple
inheritance; an object's claimed `__class__`, duck typing and virtual tuple
facades do not establish membership. A genuine integer means exactly builtin
int, with type(value) is int; bool and every int subclass are rejected.

Inspect actual tuple storage, not user-defined views: use builtin
tuple.__len__(object) for underlying length and tuple.__getitem__(object,i)
for underlying indexed slots. Never use a subclass's __len__, __getitem__,
__iter__, __getattribute__, __eq__, __hash__, __bool__ or conversion hooks.
The membership check must also avoid the input's __class__ hook. Underlying
slots are the values those explicit base methods expose, regardless of the
subclass's public methods, properties, attributes or added mutable metadata.

A syntactically admitted input has underlying outer tuple length three.
Its first two underlying slots are genuine ints e0,e1; its third slot is a
tuple in the same inclusive sense, with underlying length four and genuine
integer slots r_i satisfying 0<=r_i<5. Every other object or shape rejects
with None, including malformed objects whose own methods raise or do not
terminate. No method on such an object is called. Tuple-subclass constructors
are outside the reader: the contract begins with an existing object.

Normalize an admitted datum into a fresh plain builtin tuple containing its
two genuine ints and a fresh plain tuple of its four genuine residues.
Two admitted inputs are equivalent exactly when these normalized six integer
values agree, irrespective of concrete tuple class or overridden behavior.
The reader must return the same result for equivalent inputs. It returns
None precisely when syntax fails or the normalized datum is outside E5(K5).
Otherwise it returns the plain tuple (a,y), both members plain length-four
tuples of genuine ints, with y=C a and E5(a) equal to the normalized input.
It does not mutate the input or its metadata or invoke user-supplied hooks.

The ordinary Python builtin type/tuple/int operations and exact finite
integer arithmetic are fixed runtime semantics. Deliberate replacement of
the reader's module globals or interpreter builtins, asynchronous process
termination and exhausted runtime resources are not mathematical inputs.
There is no fixed bit-cost claim for unbounded integer inputs.

## 4. Claims, algorithm and fixed failures

Prove the syntax normalization terminates, implements section 3 and bypasses
all subclass hooks. Then prove the reader is total, sound, complete and
unique on this entire object contract. Normalize first; reject energy pairs
outside [0,5] x [0,13]; treat the zero key separately; reject nonzero pairs
outside the norm interval [1,31]. Enumerate residue-compatible lifts in the
proved box, recompute e0,e1, and return the unique match or None. At most
four lifts are examined. The bounds are inherited mathematical facts, not
learned from the regression output.

A false acceptance, false rejection, wrong/plainness-violating output,
input mutation, invoked user hook, crash on a malformed object, or different
results for normalized-equivalent tuple objects fires this new contract.
Any changed inherited arithmetic identity or complete census discrepancy
also fails the audit. Zero tolerance: no domain or threshold adjustment
after the successor pin. Preserve the predecessor's rejection separately.

## 5. Frozen finite audit

verify.py is standalone Python 3.10+ and standard-library-only, with no
project imports, files, network, randomness or floating point. The reader
and its audit are in that one new file. The finite reference image comes
from exact field matrix energies on all 1225 box elements, while the reader
uses the displayed coefficient forms. It must find the exposed 291 states,
six shell counts and maximum norm 31 without duplicate keys.

Exhaust all 52500 keys e0=0,...,5, e1=0,...,13 and all 625 canonical residues.
For each key test the nine outer/inner class combinations of builtin tuple,
a plain tuple subclass, and a tuple subclass whose ordinary access, iteration,
attribute, equality, hashing, truth, string and representation hooks all
raise. Construct these audit objects by builtin tuple.__new__ from plain
stored values. Require all nine results to equal the forward-image oracle,
giving 472500 reader calls. These representative subclass tests supplement
the universal base-operation proof; they do not exhaust Python classes.

Also test all 18750 outside keys from the predecessor domain:
e0 in {-1,6}, e1 in {-1,0,1,13,14,10000}, all residues; and e0=0,...,5,
e1 in {-1,14,10000}, all residues. Test the same nine class combinations,
giving 168750 calls, all rejecting.

The pinned code additionally fixes malformed shapes and values, bool/int
subclass rejection, objects with hostile or forged __class__, lying tuple
views on valid and invalid underlying slots, large integer energy pairs,
mutation-sensitive tuple metadata and valid-to-valid residue replacement.
Explicitly test both original zero-datum subclass counterexamples. Fresh
subclass objects with malformed underlying length or components must reject
without dispatching their hostile methods. Rejection does not inspect or
format invalid user objects for diagnostics. The exact finite fixture list
is part of the pinned code.

## 6. Freeze, reviewer, execution and scope

Freeze this preregistration publicly before dispatching a fresh reviewer.
The reviewer receives this file and the two admitted mathematical inputs,
not successor PROOF.md, verify.py, detailed outputs or current diff. Its
own derivation and implementation freeze before comparison. Prior exposure
to predecessor targets or failures is disclosed; no result-blindness claim
is made. Root owns the issue disposition, publication, pin and run record.

Before scientific execution, freeze all three files in an immutable public
Git commit and record their SHA-256 hashes after public byte readback.
Until root signals that pin, only static source review and AST parsing are
allowed. Do not import this verifier or run an exploratory subset.

Prospective command from repository root in a Linux-compatible environment:

    python3 notes/C-FIELD-J-TUPLE-READER-N/verify.py

Use the existing repository 600-second envelope and LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1. After actual execution only, save
EXPECTED.txt, RUN.md and RESULT.md with immutable pin, command, file/output
hashes and byte counts, neutral runtime metadata, exit code, stderr and
scientific disposition. A notes-only CI pass is not a scientific execution
or two-architecture gate. No promotion is automatic.

Only the bounded scalar reader's Python carrier contract is new. Complete
proof may warrant candidate-T after independent review; finite audit remains
finite evidence. This successor does not re-claim chain blindness or QDD
comparison, build transport, edit Canon, promote any dependency or close a
physical owner. No Stage-B transport implementation starts from this reader
until the coordinator has accepted its independent review.
