# P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1

**PUBLIC, NON-CANONICAL. Conditional L1 proof audit; result exposed.**
Owner: A. M. Thorn, v101 continuation session, 2026-10-10.
Branch: `probe/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1`.
Public issue: https://github.com/mathorn1973/twist-j/issues/1438.
Authority base: `bebdda8f882d14d3c01bfe1d05769597e7d2869c`.
Successful complete P0 main readback: workflow `38041292763`,
https://github.com/mathorn1973/twist-j/actions/runs/38041292763,
both architecture jobs and aggregate successful on 2026-10-10.
Reservation readback at approximately 10:02 UTC confirmed this same main,
226 actual remote heads and no preexisting exact identifier.

Preliminary collision review covered all 296 open issues/PRs, all 226
actual remote heads, exact all-state identifier search and current tracked
Canon/probe/notes text on 2026-10-10. No matching identifier or mathematical
lane was found. The related occupied first-SUM, hypothetical integer unit
reader, relative-contact chronology and ion second-contact scopes remain
separate and credited below. Public main and the remote namespace are
checked again immediately before reservation; unadvertised private work
cannot be covered by this public scan.

This preregistration freezes an audit of an already derived mathematical
result. The counts, contact representative and continuation equations were
known before the code was written. Only static inspection and compilation
are permitted before the complete public pin and its byte readback. No new
scientific program has been executed during preparation. This is not a
blind prediction, experimental observation or independent physical selection
of the proposed interaction.

## 1. Equation and exact question

All arithmetic is in F5. Freeze the literal native five generators and
selector `G_n(v)=g_(z(v)+2 theta_n)(v)` in PROOF.md section 1, with
`theta_n=popcount(n) mod 2`, `z=sum(v)`, and
`v=(p1,p4,p1p,p4p,q,r)`. Define

```text
x=p1-1, y=p1p-4, c=x+y, h=y-x,
S=p1+p4+p1p+p4p,
M=2*((p1-1)*(p4-3)+(p1p-4)*(p4p-2)),
R=(1-S^2)*(p1+p4p)+S^2*M,
C_s^f(v)=(p1,p4-f(x,y)*s,p1p,p4p+f(x,y)*s,q,r).
```

The class is **exactly** total functions `f:F5^2->F5` depending only on
`(x,y)` for which `C_s^f` commutes with each complete generator b,d,e for
every source s. It is not the broader class of all source-additive contacts
with a preserved piston sum. Literal equality of maps on complete raw
coordinates is the class equivalence; no physical quotient is assumed.

Audit the necessary-and-sufficient covariance equations

```text
f(-x,-y)=-f(x,y), f(y,x)=-f(x,y),
F(-c,h)=F(c,h), F(c,-h)=-F(c,h).
```

They give six free F5 values and exactly 15625 maps. Unit gain on the
actual occupied SUM orbit `c=+/-1,h=+/-2` is exactly `F(1,2)=4`, leaving
3125 maps. They coincide as complete contacts on this orbit, although
they differ elsewhere. The unique affine unit member is
`f_*(x,y)=3*x+2*y=2*(y-x)`; the representative finite state audit uses it.
The normalization is a target condition, not a physical derivation.

For every fixed integer N>=4, the one enlarged forward map is

```text
W_N(n,v,s)=(n+1,G_n(C_s^f(v)),s) if n=N,
W_N(n,v,s)=(n+1,G_n(v),s)       otherwise.
```

At the trigger the contact is followed by one actual native tick; at every
other step there is exactly one native tick. This composite step is an
explicit model premise, with no claim of an available zero-duration gate.
No new source is inserted during the trajectory and n is never reset.

From `E(t,s1,s2)=(0,(t,0,-t,0,-s1,s1),s2)`, the same receiver function
must read t at n=0, t+s1 at every 3<=n<=N, and t+s1+s2 at every n>=N+1.
Readiness uses this declared clock context; n=1,2 have no promised record.
The complete checkpoint must equal free U evolution through n=N and its
`C_s2^f` image thereafter. The proof is all-time; the finite audit below
does not establish it by extrapolation.

## 2. Code and independent methods

- `primary.py`: literal raw-coordinate generators and enumeration by the
  six signed `(c,h)` orbits; complete-state simulation and explicit trace
  formula for restricted inversion.
- `independent.py`: centered-coordinate generators, a 25-variable modular
  covariance constraint matrix and exact RREF/nullspace enumeration; a
  separately generated trace schedule for restricted inversion.
- `verify.py`: input-hash custody and deterministic execution of both
  programs, requiring equal complete JSON bytes and exit 0 with empty stderr.
- `PROOF.md`: self-contained derivation, including the inherited first SUM
  and all-time continuation. `REVIEW.md`: separately derived symbolic review
  and counterexamples to stronger claims.

Both implementations were written before the independent author read the
primary code; their outputs have not been inspected before the pin. The
analytical results and common reporting contract were shared. Subsequent
static cross-review is disclosed; this is methodological separation within
one coordinated assistant session, not an external or blind replication.

The wrapper binds these two programs, proof, review and preregistration by
SHA-256. RUN.md will bind the wrapper itself and immutable public commit.
No run-time input, external scientific dependency, floating point,
randomness, network access or imports between scientific programs are used.
Each child has a fixed 240-second limit; the repository retains its ordinary
600-second whole-verifier limit. No threshold changes after the public pin.

## 3. Carrier, preparations and audit inventory

The complete carrier is `N0 x F5^6 x F5`, with state `(n,v,s2)`.
The added source has the explicitly assumed passive product law under
native evolution. The original q,r are not constant: their free native
evolution is retained, including all dirty intermediate values. Equality
always includes every stored coordinate and the counter.

Every triple `(t,s1,s2)` in F5^3 is independently prepared, including zero
as a present source value and all initially occupied receiver values.
The model adds one independent source register, access to x,y, a controlled
balanced piston shift and the fixed counter trigger. It adds no blank work
register, source-consumption rule, reset, saved input or hidden phase state.
The one-sided unbounded counter is inherited from the native mathematical
model; its physical availability is an unproved premise.

The frozen finite inventory is:

| Check | Domain / expected inventory |
|---|---|
| Full contact-function class | 15625 distinct 25-byte tables, 390625 point checks |
| Unit subfamily | 3125 tables, equal complete restriction to the SUM orbit |
| Set digests | SHA-256 of concatenated lexicographically sorted 25-byte tables; points `(x,y)` in lexicographic 0..4 order; no delimiters |
| Representative complete contact | 78125 `(v,s)` pairs; inverse, retained coordinates, trace/S and M response |
| Representative covariance | 234375 complete-state b,d,e commutations |
| Prepared runs | all 125 triples at N in `[4,5,6,9,16,31,64]`, 875 trajectories |
| Finite tail | every boundary n=0 through n=N+64 inclusive |
| Complete-state and source comparisons | 73750 each |
| Restricted inverse comparisons | 72875 actual steps |
| Record comparisons | 875 initial, 15125 first-sum, 56000 second-sum boundaries |

The contact is a global permutation of F5^7. W_N is not globally injective;
the frozen raw n=0 collision is zero versus `(2,1,2,1,1,0)` with the same
s2. A clock-based inverse exists on each actual H0-initialized time image;
the finite audit checks it on all prepared trajectories. The symbolic proof
covers the whole reached trace sheet, not just these 125 preparations.

The off-support h=0 witness must defeat the stronger claim of unit gain on
the whole carrier. REVIEW.md also exhibits `h*(u+v)^2` as a covariant
coefficient outside the restricted two-coordinate class. These are expected
negative boundaries, not falsifiers of the restricted theorem.

## 4. Systematics and reading discipline

The displayed native law and predecessor piston translation are public at
Canon v101 base `08ec6f93b5f70ad662bb447cd6cc41ccc62fa5f3`, specifically
`probes/P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md` equations (43)-(44) and
`U-STABLE-PAIRED-PORT-TRANSPORT`. The displacement direction predates this
SUM comparison. Its appearance in a generator identity does not admit
source-controlled use on a live occupied receiver.

The exposed first SUM is prior work in open PR #1430,
`P-U-NATIVE-FIXED-READ-1`, source commit
`ec4995176d36005ba924e0b381c3cc72b97420fc`. Its exact identities are derived
again here from the literal generators. It is not used as normative authority
and receives no novelty credit here. The native receiver/source orientation
differs from canonical RAW-RESIDUE and is not silently substituted for it.

The 3125 alternatives yield the same complete supported trajectories, so
their multiplicity is not a scientific failure or competing physical output.
No class is selected after inspecting a new computed table. Conversely,
neither the prescribed class nor unit normalization is independently derived
from J or from original U. Native stable b,d,e preserve M and cannot alone
perform a nonzero second write of this kind.

No absence detector, physical clock access, two permanent archives, energy
law, nonzero-duration implementation, physical event, measurement law or
Born rule is claimed. No global minimality or uniqueness outside the stated
affine subclass is claimed. The unchanged scalar reader and explicit
readiness intervals are a mathematical interface, not physical readout
admission. The passive source and scheduler remain explicit open premises.

## 5. Failure threshold and disposition

Tolerance is exactly zero. Any false required equation, wrong class count,
duplicate class table, incomplete inventory, wrong complete state, inverse
failure on a reached layer, source disturbance relative to free evolution,
wrong readable value, or disagreement between implementations fires the
restricted audit. Changed pinned bytes, timeout, exception, nonzero exit,
nonempty stderr or malformed output also stop the gate.

The first execution and its exact stdout, stderr and exit status are retained
locally. There is no silent repair, repin, threshold change or rerun to erase
a failure. A completed negative scientific result is recorded and retained.
On a controlled wrapper failure, its stderr also retains every started
child's return code (or TIMEOUT) and exact stdout/stderr as unambiguous
Base64 fields, including an earlier child that had already passed.
If the gate never completes and yields no valid run record, the consumed
identifier is disposed as ABANDONED under POLICY.md; any successor needs a
new issue, identifier and immutable pin.

Only after a successful first pinned Linux execution is exact stdout saved
as EXPECTED.txt and neutral custody written in RUN.md. Both GitHub
architectures must compare against those same bytes. Static review and
all-time proof are not represented as machine executions.

## 6. Action layer and earned scope

Action layer: **L1 state only**. Proposed disposition: conditional theorem
supported by the symbolic proof and separate symbolic review, with the finite
audit as a check. The computation by itself is at most C until required
cross-architecture byte identity. This probe does not change any Canon file,
registered status, open-owner disposition or cross-layer gate.

Success closes only the stated mathematical construction and classification:
under the listed additional premises, one occupied receiver can hold the
first sum and then its accumulated second sum on the actual native timeline.
Physical admission of those premises remains a separate obligation.

In particular, `QDD-INSTRUMENT-APPARATUS`,
`QDD-INSTRUMENT-CLASS-COMPLETENESS` and `QDD-TERMINAL-EVENT-SEMANTICS`
retain their existing open dispositions. This scalar `R in F5` is not a
typed QDD pure-record port or a LOW/HIGH event-transducer realization.
`GATE-L1-QUADRATIC-MEMORY-NATIVE` is also unaffected: its independently
admitted carrier, designated target and global-permutation requirements are
not supplied here. Existing ETH-QDD dictionary adoptions do not automatically
identify this newly declared contact with their physical maps.
