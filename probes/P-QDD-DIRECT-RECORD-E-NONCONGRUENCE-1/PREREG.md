# PREREG. P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1

Date: 2026-09-01

Author of record: A. M. Thorn

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**.
Public claim lock #782 was opened before the branch and immutable pin. The
accepted verifier was not executed before that pin. These bytes earn no
scientific status.

```text
public claim lock:    #782
branch:               probe/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1
path:                 probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/
proposed claim:       QDD-DIRECT-RECORD-E-NONCONGRUENCE
status ceiling:       T
action layer:         L1
```

Claim lock #782 followed a fresh collision scan and preceded the first public
commit. No formal gate may run before the accepted `PREREG.md` and accepted
`verify.py` are committed together, pushed, and read back byte for byte from
the public remote.

## Authority and currency record

This preregistration is pinned to a fresh public-main read at:

```text
STATE:          ACTIVE
CANON:          Public Canon v74
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v74
CONTENT_COMMIT: 2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:   2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:    389246
BASE_COMMIT:    8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
```

At pin time the declared Canon tag and content commit were ancestors of
`BASE_COMMIT`, `canon/SHA256SUMS` passed 5/5, and the relevant public QDD and
kernel definitions had no semantic delta from the v74 intake head. These are
pin facts. Immediately before claim and pin, public `main` was fetched and
authority, hashes, ancestry, remote branches, issues, probe paths, Registry
identifiers, and every scientific dependency below were rechecked. They
passed. A later changed relevant definition does not mutate this pin.

## Result-exposure disclosure

This is a proof-first, fully result-exposed probe. Before this preregistration
was written, private non-authoritative work had already exposed:

- the two displayed witness pistons;
- equality of their five-field input records;
- inequality of their records after the declared generator `e`; and
- the count that all 312 nonzero sign fibres split.

No private verifier, output, hash, run record, architecture record, or status
is imported as public evidence. The proposed `verify.py` is a fresh
implementation from the public definitions. The universal statement rests on
the written exact proof below; the finite program is its audit, not a blind
discovery experiment.

## Public dependencies and ledger boundary

The proposed later dependency rows are exactly:

```text
QDD-DIRECT-RECORD-E-NONCONGRUENCE  DEF-AUTONOMOUS-STATE
    REQUIRES
    the shifted mirror e is one of the five declared generators of the
    registered autonomous architecture

QDD-DIRECT-RECORD-E-NONCONGRUENCE  QDD-ALGEBRAIC-FACTORIZATION
    REQUIRES
    complete D_QDD_direct equality is the registered Q_QDD equality on the
    finite balanced piston carrier

QDD-DIRECT-RECORD-E-NONCONGRUENCE  QDD-INSTRUMENT-APPARATUS
    BOUNDED_BY
    failure of one L1 record quotient to carry e supplies no physical
    instrument, event, sampling, or measure conclusion
```

The claim remains entirely at L1. It owns no gate, crosses no action layer,
and does not change `canon/GATES.tsv`. It does not move a Frontier row,
`ALGEBRAIC-DMATTER [D]`, or `QDD-INSTRUMENT-APPARATUS [O]`.

## Field 1 — equation and exact proof

### 1.1 Frozen public objects

Let

```text
P = F_5^4,
ell(0,1,2,3,4) = (0,1,2,-2,-1),
L(p_1,p_2,p_3,p_4) = (ell(p_1),ell(p_2),ell(p_3),ell(p_4)).
```

For `p in P`, fix the two unused checkpoint coordinates to zero and put

```text
kappa_p = kappa_(p_1,p_2,p_3,p_4,0,0) in K_QDD,
D_P(p) = D_QDD_direct(kappa_p) in MatterData_QDD.
```

`QDD-ALGEBRAIC-FACTORIZATION [T]` says that the complete tagged direct
record is independent of the two unused coordinates, constant on each
`Q_QDD` fibre, and injective on `QCarrier_QDD`. On the balanced carrier,

```text
Q_QDD(L(p)) = (L(p)L(p)^T, L(p)L(p)^T).
```

Consequently

```text
D_P(p) = D_P(p')  iff  L(p') = +L(p) or L(p') = -L(p)
                    iff  p' = p or p' = -p in F_5^4.             (1)
```

For completeness, the nonzero implication in (1) is elementary. Equality of
the rank-one matrices `v v^T = w w^T` gives the same rational line, hence
`w=a v`; substitution gives `a^2=1`, so `a=+1` or `a=-1`. The zero matrix has
only the zero vector in its fibre. Thus the 625 pistons form exactly 313
record classes: the singleton zero class and 312 two-element sign classes.

The declared shifted mirror is

```text
e(x) = (c_d + v_e) - x in F_5^6,
c_d + v_e = (2,1,3,4,2,1).
```

Its piston action is therefore

```text
e_P(p) = c - p,                 c = (2,1,3,4) in F_5^4.          (2)
```

### 1.2 Frozen theorem

For every nonzero sign class `{p,-p}` in `P`, the two image records are
different:

```text
D_P(e_P(p)) != D_P(e_P(-p)).                                  (3)
```

Equivalently, all 312 nonzero fibres of `D_P` are split by `e_P`. Therefore
there is no set function

```text
bar_e : im(D_P) -> im(D_P)
```

such that

```text
D_P(e_P(p)) = bar_e(D_P(p))       for every p in P.             (4)
```

Thus the exact direct-record equivalence is not a congruence for the declared
generator `e`.

### 1.3 Proof

Fix `p != 0`. By (2),

```text
e_P(p)  = c - p,
e_P(-p) = c + p.
```

If these residues were equal, then `2p=0`; since two is invertible in
`F_5`, this would give `p=0`, contrary to the choice of the class. If they
were negatives, then

```text
c - p = -(c + p),
```

so `2c=0`, hence `c=0`, contrary to `c=(2,1,3,4)`. They are therefore
neither equal nor negatives. Equation (1) gives (3). Negation fixes only zero
in odd characteristic, so the remaining `624` pistons form exactly
`624/2=312` nonzero sign classes, and the argument applies to every one.

If (4) held, the equal input records `D_P(p)=D_P(-p)` would have equal images
under the set function `bar_e`, contradicting (3). QED.

### 1.4 Frozen explicit witness

The smallest displayed witness used by the audit is

```text
p_+ = (1,0,0,0),             p_- = (4,0,0,0) = -p_+.
```

Their balanced vectors are `v_+=(1,0,0,0)` and `v_-=(-1,0,0,0)`. Their
complete five-field records agree, with

```text
support_state             = SUPPORTED,
total_weight              = 4/5,
branch_weights            = (1/20,3/4),
normalized_weight_state   = NORMALIZED((1/16,15/16)),
density_state             = DENSITY of the same exact rational matrix.
```

After the same shifted mirror, the balanced output pistons are

```text
L(e_P(p_+)) = ( 1,1,-2,-1),
L(e_P(p_-)) = (-2,1,-2,-1).
```

Both output records have total weight `34/5`, but their ordered branch
weights are respectively

```text
(1/20,27/4),              (4/5,6).
```

Their density and normalized-weight fields also differ. The witness is a
concrete instance of the universal proof, not its source.

## Field 2 — proposed exact verifier

Proposed accepted file after owner review:

```text
probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/verify.py
```

The accepted verifier uses only the Python standard library, integers and
`fractions.Fraction`. It contains no float, complex approximation, random
choice, network access, subprocess, external data, predecessor import, or
filesystem write. It freshly implements:

1. the balanced residue lift and its negation law;
2. the piston restriction `e_P(p)=c-p` of the public shifted mirror;
3. the exact rational QDD record formulas supplied by the registered
   factorization theorem;
4. the complete 625-piston record quotient;
5. all 312 nonzero sign fibres before and after `e_P`;
6. the displayed witness and its exact weights; and
7. the zero-translation linear-mirror control, which does descend through the
   sign quotient and isolates the nonzero affine centre.

The verifier is deliberately not an authority checker. Authority, hashes,
pin custody, and remote readback belong to the public protocol and run record;
the scientific output contains only exact mathematical gates.

Formal execution count for this verifier at the time of this pin: **zero**.

## Field 3 — carrier and data

```text
state carrier:        P = F_5^4, the public piston block
integer lift:         ell(F_5)^4 subset Q^4
record codomain:      MatterData_QDD, exactly its five current fields
record equality:      complete tagged componentwise equality
source equivalence:   p ~ -p, derived from complete record equality
tested action:        e_P(p)=c-p with c=(2,1,3,4)
external data:        none
```

The two fibre coordinates, counter, later checkpoints, apparatus data,
events, and measures are not inputs.

## Field 4 — systematics and controls

There is no tolerance, fit, retry, sampling, or exceptional class.

```text
balanced lift not negation-equivariant          STOP
record equality weaker or stronger than +/-     CLAIM FIRES
zero counted as a two-element sign class         STOP
one nonzero sign fibre left unsplit by e_P       CLAIM FIRES
branch order LOW,HIGH swapped                    STOP
q or r allowed to affect the record              STOP
private implementation or output imported        STOP
authority or dependency drift before pin          STOP
pre-pin execution of the accepted verifier        STOP
post-pin mutation of equation, code or threshold  STOP
```

The zero-centre control replaces `e_P(p)=c-p` by `m(p)=-p`. This control must
preserve every sign class. It is not an alternative public generator and
earns no claim; it checks that the obstruction is the nonzero affine centre,
not negation itself.

## Field 5 — failure threshold and decision

The primary threshold is universal and hard:

```text
PASS
    exactly 313 record classes occur on all 625 pistons;
    exactly 312 of them are nonzero sign fibres;
    every one of the 312 is split by e_P;
    the explicit witness and complete field-difference pattern hold;
    the zero-centre control descends.

FIRE
    any exact counterexample to one theorem clause, including even one
    unsplit nonzero sign fibre, a different class count, or a failed witness.

INTEGRITY STOP
    malformed carrier, unexpected exception, pin mismatch, changed accepted
    bytes, nonempty stderr, wrong exit status, or stdout mismatch.
```

Only an exit-zero run, empty stderr, and stdout byte-identical to the
post-pin committed `EXPECTED.txt` count as a successful formal execution.
No current `EXPECTED.txt` exists because this pinned verifier has not run.

Maximum later public row after the required public architecture gate:

```text
QDD-DIRECT-RECORD-E-NONCONGRUENCE [T]
```

Its scope is exactly the finite L1 piston carrier, exact five-field public
record, and the one declared generator `e`.

## Field 6 — action layer and firewalls

Action layer: **L1 only**. No L1-to-L4, L1-to-L5, or L1-to-L6 lift is
attempted, so no gate is created or passed.

This probe does not:

- assert any additional dynamical structure beyond the one declared
  generator `e` and its piston restriction;
- alter the fact that the underlying generator `e` is an involution on the
  checkpoint carrier;
- rule out a nonlocal action on a complete record stream, a relation,
  multivalued map, context-indexed map, or an enlarged signed record;
- alter the five-field schema or authorize deletion or addition of a field;
- move or refute `ALGEBRAIC-DMATTER [D]`;
- close `QDD-INSTRUMENT-APPARATUS [O]` in either direction;
- supply an effect, instrument, event, occurrence law, sampling law, physical
  measure, or decoder completion; or
- create a Frontier, gate, CORE-selection, SI, empirical, or higher-layer
  conclusion.

The exact interpretation is only this: an invertible state map need not
descend to a deterministic point map on a coarser record quotient.

## Required public sequence after owner acceptance

1. Fetch current public `main`; rerun authority, collision, issue, path,
   Registry and remote-ref scans.
2. Open the public claim-lock issue and replace
   `#782` before the first commit.
3. Review and accept the final `PREREG.md` and fresh `verify.py` without
   executing the accepted verifier.
4. Commit and push exactly those accepted files on the named probe branch;
   record the commit and both SHA-256 hashes; read both files back from the
   public remote.
5. Only then run the pinned verifier locally in the deterministic public
   environment and record its exact stdout.
6. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing the frozen
   preregistration, verifier, equation, scope, or threshold.
7. Open one reviewed pull request changing only this probe directory and
   require byte-identical x86_64 and aarch64 public jobs.
8. A later separate Canon fold may add only the earned L1 theorem row and the
   three declared dependency edges. Frontier and gates remain unchanged.
