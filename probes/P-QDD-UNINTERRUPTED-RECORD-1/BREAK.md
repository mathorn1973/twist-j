# Independent review and exact finite-premise audit

**PUBLIC; L1; NON-CANONICAL.** This is a review of a conditional algebraic
record protocol. It neither supplies a physical apparatus nor changes the
status of `QDD-INSTRUMENT-APPARATUS`.

## Review exposure and execution boundary

The reviewer read the public native generator formulas, the canonical
Galois-code proof, the accepted
`notes/C-QDD-UNINTERRUPTED-RECORD-N/README.md`, the complete new `PROOF.md`,
the new `PREREG.md`, and the declared task. The
reviewer did not read, import, or execute this probe's `verify.py` or the
accepted verifier of the Galois-code probe. This is an independently
constructed audit, not a blind mathematical review: the target identities
and the earlier proof were visible.

`break.py` was constructed from homogeneous affine coefficients and exact
cyclotomic coefficients. Before the public pin, only Python AST parsing
was performed. No scientific assertion or enumeration in the script was
executed. A later execution must receive its own run record; this document
does not report one.

## Independent derivation and attempted breaks

### 1. Stable sheets and source protection

Use homogeneous coordinates `(a,b,c,d,q,r,1)` over F5. The affine matrices
of b, d, e have zero coefficients of q and r in their first four rows.
Their q and r rows have linear coefficient -1 and have no source
dependence. If

    v_delta=(0,0,0,0,-delta,delta),

then `g(x+v_delta)=g(x)-v_delta` for these three maps. This coefficient
identity holds for every native point and every delta. The paired shift
also preserves the trace, so it does not change the selected generator.
The four selector cases on z=1 or 4 select exactly b, d, e and return to
one of the same two sheets. This supplies both the base and closure step
for induction through every finite bit word. No finite word census is
needed to prove the statement for arbitrary waiting times.

The source-sum row changes sign for all three maps: the d/e translation
sum is `2+1+3+4=0` in F5. Hence the transported source mark is invariant.
Its initial value may determine delta pointwise without invalidating the
constant-delta conjugacy: the source is unchanged by the entrance map.

I tried extending this conclusion to the other generators. It fails in
both declared ways. Generator a preserves the sign of the paired shift.
Generator c produces the extra source translation

    (a,b,c,d) -> (a,b+delta,c,d-delta).

At trace zero with driver bit one and delta one, the source outputs are
exactly `(2,2,2,0)` and `(2,1,2,1)`. Thus an unrestricted all-sheet version
of the theorem would be false. The stable-sheet restriction is necessary.

### 2. Reference, preparation, and archive capacity

On one common initial trace sheet, the selected word and the r recurrence
are independent of the source coordinates. One common reference r^0 is
therefore legitimate. Initial points on different sheets cannot silently
be assigned the same reference propagation; the theorem does not do so.

For initial port error e, an incoming cell m, and the admitted source mark
f, the reduced protocol is exactly

    (e,m) -> (e+f,m) -> (epsilon(e+f),m)
          -> (epsilon m,e+f),       epsilon in {1,-1}.

It is a bijection for each fixed epsilon and f, with inverse

    (e_out,m_out) -> (m_out-f,epsilon e_out).

The signed exchange separately is an involution. Immediate exchange
followed by native waiting gives the same final pair as delayed exchange.
These identities cover arbitrary initial e and m, not only ready/blank
inputs. They expose three direct ways to falsify overstatements:

- A nonzero e adds to the recorded f.
- A nonzero m returns to the native port, preventing restoration to r^0.
- Omitting the final sign after odd waiting records -f. The mark 1 becomes 4.

With e=m=0, restoration is pointwise to the freely evolved native
six-tuple. The q coordinate follows from the preserved source and trace,
so restoring only r is not being mistaken for restoring the full point.
During waiting, the checkpoint port remains displaced. Endpoint
restoration therefore does not establish `feeds_U=false` for the protocol.

### 3. Source basis, endpoint basis, and complete coherence

The source LOW projector is `P_L=11^T/4`; endpoint LOW selects only Y_1.
Writing the canonical endpoint map as `W=(sqrt(5)/10) H E`, the independent
cyclotomic audit cancels the nonzero scalar and verifies

    4 D_L H E = H E 11^T,
    (H E)^*(H E) = 20 I - 4 11^T.

These give the intended intertwining and `W^*W=I-11^T/5`. In particular
the source HIGH vector `(1,-1,0,0)` has zero endpoint LOW amplitude and
nonzero sum of endpoint amplitudes. The two bases cannot be interchanged
in an argument about HIGH inputs.

For endpoint indices h,j, the joint record map acts on every matrix unit
as

    |h><j| -> |h><j| tensor |f(h)><f(j)|.

There are sixteen such units, including six LOW/HIGH cross units. None
of those six disappears from the joint state. After tracing the archive,
exactly ten endpoint matrix units remain: the one LOW diagonal unit and all nine
units of the three-dimensional HIGH block. A fine four-label record
followed by discarding the record instead preserves only the four
diagonal units. It therefore destroys six HIGH off-diagonal units that
the coarse protocol preserves.

This proves why pointwise restoration does not mean restoration of an
uncorrelated source-and-archive state. Selecting an archive outcome is an
additional conditional operation and is not a realized event law supplied
by this proof.

With earlier cells passive and a new blank cell at each use, a further
record appends the same f(h) on each basis component. The written
induction yields all-1 records on LOW and all-2 records on HIGH. It does
not yield independent trials. The script checks three successive records
only as a finite audit of this induction step.

## Exact script coverage

`break.py` contains four separately reported audit groups:

1. Five affine involutions, fifteen stable-generator conjugacies, four
   selector transitions, source-sum transport, and the a/c boundary
   witnesses. Matrix equalities check all affine coefficients, rather than
   reproducing a point-update loop from the accepted verifier.
2. All 250 reduced combinations of sign, mark, input error, and incoming
   cell. For each sign and mark the 25 pair states are a permutation;
   inverse, exchange involution, covariance and nonblank/nonready effects
   are checked.
3. Sixteen intertwining entries and sixteen Gram entries in the exact
   ring `Z[j]/(1+j+j^2+j^3+j^4)`, plus the source/endpoint HIGH distinction.
4. All sixteen endpoint matrix units, conditional outcome blocks, six
   joint LOW/HIGH correlations, all HIGH coherences, coarse versus fine
   trace, and repeated equal marks in fresh cells.

All arithmetic is integral and exact. There is no floating point, sampled
native trajectory, external package, network request, random input,
runtime import of another scientific script, or mutable data dependency.

The script audits finite algebraic premises. Arbitrary waiting times and
arbitrarily many admitted recordings are established by written
induction. Neither the finite checks nor those inductions establish
physical preparation, interaction dynamics, an archive material, a
chosen event, an occurrence law, reset by erasure, or a layer lift.

## Pre-pin conclusion

The accepted note and the new `PROOF.md` survive the attacks above.
No mathematical falsifier was found at its declared scope. In particular,
the source protection, arbitrary waiting, full checkpoint restoration
on ready/blank input, and preservation of HIGH coherence are mutually
compatible. Every attempted enlargement identified above has an exact
counterexample or lacks an explicitly required physical premise.

The new proof's equations (8), (20)--(23), (32)--(42) correctly separate
all-word native propagation, preparation and capacity, source and endpoint
bases, metric adjoints, joint correlations, and reduced-state changes.
Known-sheet injectivity suffices everywhere a coherent code is transported;
global native invertibility is neither available nor assumed. The proof's
negative witnesses have the stated signs and full coordinate values.

The preregistration review identified and resolved one scope wording before pin:
the signed port mark exists throughout waiting, before exit, not after the
restoring exchange has completed. `PROOF.md` already states precisely
`n <= j <= N` in (23). The preregistration was required to carry the same
qualification, and its correction was read back. The arithmetic description also distinguishes the main
verifier's rational coefficients from this audit's integer subring.

With both pre-pin wording alignments confirmed, the written review verdict
is **PASS at the declared conditional L1 scope**. This conclusion is a
written review, not a report that `break.py` has passed. Formal execution
and public acceptance remain separate recorded steps after the public pin.
