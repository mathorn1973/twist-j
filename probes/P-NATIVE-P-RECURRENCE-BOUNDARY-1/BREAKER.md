# Frozen independent implementation and attacks

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

This is a method-separate implementation in the same session. The candidate
results were disclosed in the task and preregistration. It is result-exposed,
not an external blind review. The author executable, author proof and any
scientific output were not opened or imported before this implementation was
written. No scientific execution, import or dry run occurred before the code
was supplied for the public pin. Static parsing and custody hashes are allowed.

## Inputs and analytical attack

The exact scientific specification read was
`probes/P-NATIVE-P-RECURRENCE-BOUNDARY-1/PREREG.md` at commit
`27de104a74a5daaa3a9940853590ccc7e0e8c4cf`, SHA-256
`f6d16a47d191866e2299a3802b6fc6590f5fb23042e37895f5d03fd165b6c9f7`.
The reference was read directly from
`notes/C-NATIVE-P-CONTACT-REALIZATION-N/CONTRACT.md` at commit
`217cfc13befc3ab4b14444aed49e3fce7f50a7b7`. The raw affine definitions in
the preregistration were consumed as the native equations; the parent scope
and custody manifest establish their canonical source.

The first attempted escape from A is an arbitrary time-dependent encoding.
It does not invalidate the stated argument. Put
`a=ceil(9/k)`. For any `n>=3+a*k`, use the complete target permutation to
write `y=F_P^a(y0)` and intertwining to write every encoded state at n as
the result of `a*k` original ticks beginning at `n-a*k>=3`. The inherited
synchronization therefore places every encoded cell on the same current
sheet, even though the encoding at each n was arbitrary. On that sheet the
actual letters are e, b, b, d in previous/current-bit order 00, 01, 10, 11.
Their linear parts are respectively `-I,-B,-B,-I`. The k-step difference
map telescopes to the claimed endpoint expression. At the arbitrarily late
binary-complement times, it is scalar. Fixed disjoint raw support then
prevents the source-local witness from changing any present receiver
coordinate. A common present clock cannot separate two equal receiver
arguments. This argument needs target invertibility and an intertwining
valid at every admitted n; it does not cover a restricted start set or an
unaccounted changing external record.

For B, full raw affine bijectivity makes each source sheet map bijectively
onto its prescribed sheet. Thus union permutation is exactly injectivity
and equality of the shifted scalar sheet image. The t=0 image has at most
two sheets, proving the upper bound without testing a maximum cell count.
The exhaustive classification of 31 nonempty subsets and 25 correction
pairs is a separate finite audit of this specified small class.

For D, the independently derived phase sheets, before each microtick, are:

| Block bit | Phase 0 | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Next block |
|---|---|---|---|---|---|---|
| 0 | {0,4} | {0,4} | {2,3} | {0,4} | {2,3} | {0,4} |
| 1 | {0,4} | {1,2} | {1,2} | {0,1} | {2,3} | {0,4} |

The phase-0 inverse selects the original input sheet from the image sheet;
it must not apply the unrestricted selector again. All later inverse
commands are the literal involutions, evaluated using the previous actual
clock. The common last command d and common next-block slice handle every
change of the next block bit. No equality between theta(5n) and theta(n)
enters this argument.

These are candidate-T analytical observations in the frozen scope. The
finite computation, when actually run, is candidate-C until the required
public evidence and review permit any stronger status. No successful run
is asserted by this pre-execution document.

## Frozen executable attacks

`break.py` uses sparse homogeneous affine matrices for the native maps and
composes the actual selected matrices. It does not import the author's
implementation. Exact integers and F5 are the only arithmetic.

1. Check all five literal involutions on every raw checkpoint, e after d on
   every checkpoint, and both selector sheet laws on every checkpoint.
   Enumerate every nonempty sheet subset and every translation pair. Assert
   equality with the seven nominated triples and the unique two-sheet choice
   that leaves t=0 unchanged. Raw affine invertibility justifies the scalar
   sheet reduction for all occupied coordinates.
2. Check inherited nine-tick synchronization on every initial scalar sheet
   at actual starting clocks 0 through 1023. This finite historical audit is
   not a new proof of its universal source theorem. Compose full homogeneous
   matrices at actual clocks 3 through 96 for lengths 1 through 16. Then use
   lengths 1 through 128 and all three lengths adjacent to powers 2^j for
   j=1 through 10. At each length, construct certificates for the analytical
   synchronization threshold and that threshold plus one million. Compare
   the actual composed linear part with the endpoint formula. These finite
   audits are not enumeration of encodings or proof of the universal no-go.
3. Check both corrected maps on every state of both selected full sheets,
   including exact inverse, individual sheet preservation, equality with the
   raw map followed by the declared translation, and complete image equality.
   Additional actual-clock checks exercise the previous-bit compound inverse.
4. Select the earliest actual block starts among 0,5,...,10235 that cover
   all four previous/next block-bit pairs. For each representative, check
   every point of every full microphase sheet union in both directions,
   full image equality, actual clock increments, and both compositions of
   the inverse. Check the five-step compound identity and its entire inverse
   on every selected input at each representative. The first and fifth
   phases test image-sensitive selector inversion and block-bit changes.
5. Check the exposed source-local native pair, all identical nonsource
   coordinates, the retained source sheet distinction, both corrected
   receiver outputs and the single present read. Replay the pair through
   every selected actual five-tick boundary context.
6. Reconstruct the comparison partner, direction reversal and local tick
   from the #1629 contract using integer shear matrices. On the exposed
   mu=1,4 pair, vary all 125 initial Weyl labels and traverse the complete
   four-step accepted/outward cycle. Check exact full inverse, bank and
   energy account, and Weyl action on all five basis states, including its
   central phase. Additionally test all labels and both vertices/directions
   of the shell-valid refusal preparations (q,p,u,v)=(1,1,1,0), bank 3,
   mu=1,4. Test accepted-zero and outward cases for three shell-valid
   representatives mu=0,2,3. This is a finite reference witness audit;
   it does not simulate the complete Y_(8,3).

The executable prints counters obtained from its loops; no undeclared run
count is asserted here. Failure prints an exact named assertion and exits
nonzero. A changed preregistration hash yields an integrity STOP. Successful
stdout is deterministic ASCII with no stderr. The parent executable must
launch this file as a separate process so that both implementations enter
the same public two-architecture replay and complete stdout comparison.

## Limits

A surviving run supports only A--E within the frozen specification. The
literal-product no-go remains an analytical claim at that class, and the
positive actuation remains NEW_DECLARED. The five microticks use the
original letters with a newly declared schedule. This audit supplies no
native realization of the entire reference shell, funded bank mechanism,
physical energy law, Weyl storage implementation, source depletion,
permanent detector record or layer lift. The predecessor's full P admission
remains OPEN / STOP_ADMISSION_UNSUPPLIED.
