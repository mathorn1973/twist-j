# Promotion package: C-J-SINGER-MAHLER-LIFT-1-N

```text
STATUS:           PROPOSED ONLY
AUTHORITY:        NONE
PROPOSED CLAIM:   J-SIGNED-TRACE-MAHLER-RIGIDITY
PROPOSED STATUS:  T
PROPOSED LAYER:   L1
```

No promotion is performed by this package.

## Proposed theorem row

`J-SIGNED-TRACE-MAHLER-RIGIDITY [T]` — Let

\[
f(X)=X^4-3X^3+bX^2+cX+1\in\mathbf Z[X],
\qquad b,c\equiv0\pmod2.
\]

If `f` has no unit-circle root and exactly two roots outside and two roots
inside the unit circle, then

\[
M(f)\geq\varphi^2,
\]

with equality if and only if

\[
f(X)=\Phi_5(X-1)=X^4-3X^3+4X^2-2X+1.
\]

The broader order-15 binary Singer class, including its `p_R`-oriented
subclass, does not satisfy this lower bound or uniqueness: exact strict-lower
and non-target equality witnesses exist.  Therefore the signed trace is the
first sufficient condition in the preregistered A0-A3 ladder; reduction
modulo two alone is not a selector.

## Proposed registered controls

- `X^4-X^3+1` is an exact `p_R` strict-lower witness.
- `f_J(-X)` is an exact distinct `p_R` equality witness.
- `X^4 f_J(1/X)` is an exact equality witness in the `p_L` branch.
- Adding `f(1)=1` is unnecessary for the stated Mahler rigidity and creates
  no new selector claim.

## Existing ownership and compatibility

- `J-MAHLER-MEASURE [T]` continues to own the exact value
  `M(f_J)=phi^2` and its existing arithmetic statement.
- `J-BINARY-NORM-DESCENT [T]` continues to own the binary norm-trace and its
  explicit no-selector guard.  The A0/A1 failures reinforce that guard.
- `J-BINARY-NORM-INDEX [T]` continues to own the inert-prime norm-one index
  and the order-15 attainment statement; no uniqueness of `J` is imported.
- `CARRY-PENTAD [T]` continues to select no exponent, orientation, or
  physical reading.  No reverse dependency is proposed.

## Evidence bundle

- public preregistration pin `49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a`;
- global exact proof in `THEOREM.md`;
- complete frozen-window verifier `verify.py`;
- independent compound-Schur cross-check `crosscheck_schur.py`;
- blind exact breaker `breaker.py` and `BREAKER_AUDIT.md`;
- hashes in `SHA256SUMS`.

## Required review before promotion

1. independent line-by-line review of the positive-sign exterior-resolvent
   factor and the negative-sign global gap;
2. clean execution of `verify.py`, `crosscheck_schur.py`, and `breaker.py` on
   the required public architectures with pinned transcripts;
3. fresh collision scan against open issues, pull requests, remote branches,
   and the active registry;
4. a formal public probe with its own preregistration, expected transcript,
   run record, and two-architecture evidence;
5. explicit preservation of all no-selection and L1-only firewalls.

## Forbidden promotion inferences

The theorem must not be presented as integral matrix-conjugacy uniqueness,
basis uniqueness, exponent selection, a physical selection principle,
entropy production, a decoder statement, a Born/probability derivation, or
an L2-L6 lift.
