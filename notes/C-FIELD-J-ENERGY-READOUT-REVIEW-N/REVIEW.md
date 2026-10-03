# Independent review and original-candidate disposition

**PUBLIC, NON-CANONICAL. Overall disposition: REJECT the original candidate's
complete implementation contract.** One exact false-rejection witness fires
claim B as frozen. The mathematical bounded inverse, claims A, C and D, and
the complete disclosed finite census survive this review. No physical or
canonical claim is promoted.

Prepared 1 October 2026 by A. M. Thorn / field_j_breaker session. Assignment:
[issue #1323](https://github.com/mathorn1973/twist-j/issues/1323#issuecomment-5940830218).
Author scientific pin:
[`49dfad177c6ab698b5751de3e56629508982b05f`](https://github.com/mathorn1973/twist-j/commit/49dfad177c6ab698b5751de3e56629508982b05f).
Independent proof/breaker pin:
[`c404c1c53a9af3ce1b2523de8a56a270e082e7c9`](https://github.com/mathorn1973/twist-j/commit/c404c1c53a9af3ce1b2523de8a56a270e082e7c9).

## 1. Claim-by-claim verdict

| Frozen claim | Verdict | Evidence and exact limit |
| --- | --- | --- |
| A: chart, universal energies/traces/norm, distinction between actual A_f and virtual J_f | ACCEPT | Independent complete matrix polarization agrees with the author's coefficient identities. Exact inverse chart and intertwining hold; explicit energy-changing virtual witnesses exist. |
| B: containing box, norm bound, injectivity and mathematical image inverse | ACCEPT | The inverse Gram gives squared-coordinate bounds (12,8,8,12), so the full box is covered; N<=31 and 625>496 prove uniqueness. Enumeration and direct re-encoding prove the mathematical inverse on the stated integer data. |
| B: total Python inverse under the frozen positive syntax contract | REJECT | Tuple subclasses satisfy the prose's tuple shape but the implementation rejects them solely because their exact type is not built-in tuple. The two witnesses below are valid zero observations, not impossible traces or malformed residues. |
| B: finite shell census and maximum norm attainment | ACCEPT | Independent 1225-point census gives 291 points, shells (1,20,30,60,60,120), and maximum 31. This is finite exact evidence from one architecture; it is not a two-architecture gate. |
| C: ell/j ell at fixed B0 and LOW | ACCEPT | Both sources have (e0,e1,S0,S1,N)=(5,5,10,15,25), coefficient tuples (1,-1,-1,1),(-1,0,-2,-2), and LOW values 0,5/16. No global complex phase quotient or physical probability statement is used. |
| D: all-time unchanged-chain receiver blindness | ACCEPT | Independent induction closes at each actual Ghat/A/B/F layer, including source AM-to-R reversals, funding rejections, resource returns and pointer wraps. The full receiver 31-tuple and p agree; finite simulation is an audit only. |

There is no unresolved mathematical or execution BLOCKED item in this
review. Overall REJECT preserves the failed software interface clause; it
does not relabel it as an algebraic, physical or transport falsification.

## 2. Exact false-rejection witnesses

The [frozen author PREREG, section 2](https://github.com/mathorn1973/twist-j/blob/49dfad177c6ab698b5751de3e56629508982b05f/notes/C-FIELD-J-ENERGY-READOUT-N/PREREG.md#L50)
positively admits a tuple of length three, two genuine Python integer
energies with booleans excluded, and a tuple of four genuine canonical
integer residues. It does not exclude tuple subclasses. In particular the
following inert subclass overrides no operation:

```python
class TupleSubclass(tuple):
    pass

zero = (0, 0, 0, 0)
outer_subclass = TupleSubclass((0, 0, zero))
residue_subclass = (0, 0, TupleSubclass(zero))
expected = (zero, zero)
```

Each datum satisfies that positive syntax description, encodes the unique
zero scalar and zero active field, and must return `expected`. Yet
[author inverse line 154](https://github.com/mathorn1973/twist-j/blob/49dfad177c6ab698b5751de3e56629508982b05f/notes/C-FIELD-J-ENERGY-READOUT-N/verify.py#L154)
returns None for `outer_subclass`, because its exact type is TupleSubclass.
[Line 159](https://github.com/mathorn1973/twist-j/blob/49dfad177c6ab698b5751de3e56629508982b05f/notes/C-FIELD-J-ENERGY-READOUT-N/verify.py#L159)
likewise returns None for `residue_subclass`. No arithmetic, bounds or
enumeration is reached. This is an exact source-level counterexample.

The independent [frozen DERIVATION, section 2](https://github.com/mathorn1973/twist-j/blob/c404c1c53a9af3ce1b2523de8a56a270e082e7c9/notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/DERIVATION.md)
already stated that tuple subclasses remain tuples; the independent reader
uses `isinstance(..., tuple)` while retaining exact `type(x) is int` for
every numeric entry. Thus the subclass reading was fixed before exposure to
the author implementation, not invented to reinterpret a passing test.

The frozen finite breaker did **not** include tuple-subclass fixtures.
Its PASS is accurately preserved. This additional failure was found by
post-freeze source comparison, not by that execution, and no separate
execution of the subclass snippets is claimed here. Python's displayed
type-guard control flow is sufficient to establish both return values.

Restricting the original prose after inspection to exact built-in tuples
would narrow its accepted domain and repair the finding retrospectively.
That is not done. The original author and independent pins remain unchanged.
A repaired reader requires its own fresh frozen work; it cannot erase this
original disposition.

## 3. Scientific comparison

The [author proof](https://github.com/mathorn1973/twist-j/blob/49dfad177c6ab698b5751de3e56629508982b05f/notes/C-FIELD-J-ENERGY-READOUT-N/PROOF.md)
and [independent derivation](https://github.com/mathorn1973/twist-j/blob/c404c1c53a9af3ce1b2523de8a56a270e082e7c9/notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/DERIVATION.md)
agree on u=sum a_i^2-a0a1-a1a2-a2a3 and
v=a0a1+a1a2+a2a3-a0a2-a0a3-a1a3. The direct chart pullback gives e0=u+v,
and the virtual J pullback gives e1=u. The independent norm derivation uses
the determinant of multiplication by u+v phi in the real basis (1,phi),
then an exact 2-variable matrix substitution. The author verifies all
quadratic and quartic coefficients in sparse formal polynomials. The
independent finite census additionally computes norm as the determinant of
four-dimensional cyclotomic multiplication. Both implementations independently
chose equivalent five-position cyclic convolution for field multiplication;
the review claims implementation blindness, not completely unrelated
arithmetic algorithms.

Both proofs bound the scalar coefficient box before enumeration and use the
same admitted canonical embedding triangle-inequality theorem with the
independently derived smaller norm bound. Their enumeration strategies are
residue-compatible lifts plus exact re-encoding. The independent test oracle
uses the literal raw field matrix quadratic, while its decoder uses the
explicit scalar u,v forms. The author uses its explicit active-energy formula.
The mathematical inverse is sound, complete, terminating and unique. The
software defect lies before that mathematics, in tuple-shape recognition.

The [canonical chain law](https://github.com/mathorn1973/twist-j/blob/44423153eee6259c7277eec5f5adbed9679f9146/canon/CANON.md#L7596)
and both independent and author inductions retain the source's raw field as
PL A_f^k w in matter state R and P A_f^k w in matter state AM. Thus source
reactions always use h=1; receiver reactions always use h=0. Resource guards,
whole-content swaps and event increments depend only on common coordinates.
This closes the stronger equality of every stored coordinate except source
raw field at every layer, so it covers full receiver histories for all time.
The read-only chain subreview independently derived a single-packet invariant
from the Canon and, after the freeze, found no mismatch in the author's
chain proof or functions. It executed no code and changed no files.

## 4. Executed evidence

The coordinator publicly read back all three independent Git blobs before
execution and ran the unchanged pinned breaker. This reviewer read the
captured stdout and metadata and independently checked stdout/stderr SHA-256.
The exact run record is:

- Input pin: `c404c1c53a9af3ce1b2523de8a56a270e082e7c9`.
- Command: `python3 notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/break.py`.
- Environment: Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12;
  LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1.
- Bound 600 seconds; elapsed 4.609 seconds; exit code 0; stderr 0 bytes.
- Breaker 15364 bytes, SHA-256
  `0aa1aa2eb2347490d38feb930f2a8bb3b0dabbf49d12e3e4fe774d0e3cd24f68`.
- Stdout 610 bytes, SHA-256
  `f12a35424245bbca754ac849d360877956393cd77f894b8f42f279c2e25713c5`.
- Empty stderr SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The output reports the universal matrix/coefficient checks, complete
1225-point census, 143125 typed keys, 74 malformed fixtures, fixed source
ratios, seven rejected and four funded local fixtures, and 76920 initial or
layer-boundary comparisons over all twenty unit seeds, N=2,...,7 and 160
macrosteps. Required source and receiver acceptance/reversal/rejection
branches and receiver pointer wrap were covered. All finite checks passed.
The breaker is independent and self-contained; its PASS does not assert that
it dynamically imported and tested the author function.

After the independent freeze the reviewer also read the author's
[EXPECTED.txt](https://github.com/mathorn1973/twist-j/blob/eda73b3e1fa707d46fd24ff14e23903eb62b98ec/notes/C-FIELD-J-ENERGY-READOUT-N/EXPECTED.txt)
and [RUN.md](https://github.com/mathorn1973/twist-j/blob/eda73b3e1fa707d46fd24ff14e23903eb62b98ec/notes/C-FIELD-J-ENERGY-READOUT-N/RUN.md).
That separate author run reports exit 0, empty stderr, stdout 743 bytes with
SHA-256 `e0fa341c41cc0c1275d020f87b5d5927230099c67a86e09cd905560149522a7d`,
and passing 52500 in-range plus 18750 outside keys and 32000 chain-layer
comparisons. The author output and independent output differ by design;
byte identity between these different implementations is not claimed.
Both local runs are x86_64, so together they are not a two-architecture gate.

## 5. Exposure history and retained limits

Before independent freeze, the reviewer read only the candidate preregistration
blob `3b70d4a2445e88abc3755628d86c71e52c817297`, repository rules and its
admitted canonical definitions/proofs at main
`44423153eee6259c7277eec5f5adbed9679f9146`. The full source links and exposed
historical targets are preserved in the
[independent PREREG](https://github.com/mathorn1973/twist-j/blob/c404c1c53a9af3ce1b2523de8a56a270e082e7c9/notes/C-FIELD-J-ENERGY-READOUT-REVIEW-N/PREREG.md).
Only AST parsing occurred before pin. The canonical-only child subreview
received no candidate implementation. The coordinator then committed,
pushed and publicly read back the independent three-file freeze. Only after
that explicit signal did this reviewer read author PROOF.md and verify.py,
then author run records; the child inspected only the authorized chain slice.
The independent frozen PREREG.md, DERIVATION.md and break.py stayed unchanged.

The review was implementation-blind, not result-blind: counts and ratios were
disclosed in the author preregistration. No unpublished attachment or private
exploratory program was used. No claim follows about physical observation,
energy selection, coherent phase discrimination, Born occurrence, native-U
realization, apparatus reset or a different transport law. The norm-941
modulo-25 capacity boundary and every open physical owner remain unchanged.
