# P-QDD-RECORD-MONOID-DESCENT-2 result

Status: `PROVED AND AUDITED IN THE FROZEN CLASS / PUBLIC REPLAY PENDING / CANON UNCHANGED`

## Disposition

```text
same-record readback:
  Re-reading or re-conditioning on one already written immutable event is
  idempotent. A passive readback applies no new system branch map.

fresh apparatus repetition:
  A new prepared pointer and record cell applies the HIGH branch map T again.
  Repetitions are counted by the free monoid (N_0,+), and append-only histories
  retain the words H^n rather than collapsing H and HH.

saturation descent:
  The quotient sat(0)=0 and sat(n)=H for n>=1 maps the free count monoid to the
  idempotent terminal-symbol monoid ({0,H},OR). The projective branch action
  n -> [T^n] factors through this quotient if and only if [T]^2=[T]. Because
  the supported projective branch classes form a group, this holds if and only
  if [T]=[Q].

finite breaker:
  T_star=R-C has the frozen effect and two-sided support, obeys T_star^2=Q and
  is not +/-Q. Its projective post-state orbit alternates with period two while
  every terminal record symbol is HIGH.

infinite breaker:
  T_inf=R+(3/5)C+(4/5)J has the same effect and support. Its C-plane phase
  lambda=(3+4i)/5 has norm one and lambda+lambda^-1=6/5. It is not a root of
  unity, so T_inf has infinite projective order. One terminal HIGH symbol is
  compatible with infinitely many exact post-state classes under fresh
  repetition.

target:
  Comparison is last. At token k=2, P_2=E_low and Q_2=E_high. Saturation
  descent therefore conditionally selects the Lueder sign class.

decision:
  RECORD-MONOID-NONDESCENT.

integrity:
  one formal execution; exit zero; empty process stderr; 36/36 exact gates
  PASS; stdout byte-identical to EXPECTED.txt.
```

## Scientific conclusion

A second reading must return the same conditional branch only when "second
reading" means re-reading or re-conditioning on the same immutable event, or
when a separately justified physical bridge forces fresh apparatus repetition
to descend through the saturated terminal-symbol quotient.

The first case is idempotent by set restriction:

```text
(A intersection E) intersection E = A intersection E.
```

It is not a second system interaction. The second case is exactly the missing
physical premise. Algebraically it is equivalent, in the frozen supported
branch class, to

```text
[T]^2=[T]
```

and hence to the one sign class represented by `Q`.

The append-only record protocol does not provide that quotient. It stores
multiplicity as `H`, `HH`, `HHH`, and so on. Fresh interactions may therefore
apply `T`, `T^2`, `T^3`, and so on even though the coarse terminal symbol is
always HIGH. The period-two and infinite-order witnesses show that this is a
real exact freedom rather than a wording ambiguity.

Public Canon v59 defines the decoder as a typed read-only partial interface and
states that decoder outputs do not feed `U`. It supplies no registered map from
`ObservableHistory` to an L4 post-state endomorphism and no bridge identifying
passive readback with fresh apparatus repetition. Therefore the public
architecture does not presently derive saturation descent.

Global blocker O2 of `QDD-INSTRUMENT-APPARATUS [O]` remains open. The remaining
positive route is now typed and exact: construct an independent physical bridge
that makes post-state update a function of the saturated event rather than of
repetition count, without assuming projective idempotence as an input.

## Proposed registry consequences

After the required byte-identical public replay, a later separate Canon fold
may register at most:

```text
QDD-RECORD-SATURATION-DESCENT [T]
QDD-READBACK-REINTERACTION-SEPARATION [T]
QDD-HIGH-REPETITION-ORBIT [T]
```

Their common scope is the exact L4 carrier and monoid comparison frozen in
`PREREG.md`. None claims that the saturation quotient is already a physical law,
that the public decoder is complete, or that this apparatus class exhausts all
J-native apparatuses.

## Evidence boundary

This is L4 apparatus/support only. The free repetition count is not identified
with public `D_clock`. There is no realized L5 event stream, L6 measure,
decoder completion, SI statement or Bell causal account. O1 is untouched.

```text
SAMPLING NOT PROVIDED
```
