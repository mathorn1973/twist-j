# P-QDD-PURE-RECORD-TYPED-BRIDGE-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific
result is earned by this file. The accepted `verify.py` may be parsed and
syntax-compiled before the public pin, but it is not imported or executed
before this file and `verify.py` are committed together, pushed, and read back
byte for byte from the public remote.

Public claim lock: issue 502.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v59
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v59
CONTENT_COMMIT: 5da6b883defebd8edc470db1e2e7ebde095ef20a
CANON_SHA256:   7fdea700589a21303109dbb6c33fecd2d8243d0d09184ab9d471f0a59687f641
CANON_BYTES:    314310
BASE_COMMIT:    1b288cbed5a9ccdfed5edde906df82fa1522870e
```

Target: O2 of `QDD-INSTRUMENT-APPARATUS [O]`.

Layers: L1 exact record and autonomous-state algebra, L4 apparatus/support,
and the declared multi-layer decoder type boundary. The candidate gate under
audit is

```text
GATE-L4-L1-QDD-PURE-RECORD.
```

This probe may classify exact maps and prove an emptiness theorem for one
frozen congruence class. It does not edit `canon/GATES.tsv`, pass the gate,
change the decoder signature, or adopt a new architecture.

## Collision, lineage, and disclosure

Open and closed issues, pull requests, remote branches, probe paths, the
registry, and the gate table were searched before the claim. No collision
exists under the probe identifier or the four proposed claim identifiers.

The merged probes `P-AFFINE-QUADRATIC-READING-1`,
`P-QDD-COMMUTATOR-READOUT-FORK-2`, and
`P-QDD-AFFINE-PURE-RECORD-BRIDGE-1` are result-exposed lineage only. Their
verifiers and calculations are not imported. The accepted verifier below is a
fresh implementation. Non-canonical dry work exposed the expected bridge
boundary and exact coding construction; those bytes and runs are discovery
context, not evidence. Written proofs carry universal statements.

The public claim issue initially drafted a motor action on the HIGH support.
That was corrected before any preregistration pin or formal execution:
`D_J` does not generally preserve `W`; only `A=Q D_J Q|W` is intrinsic there.
The frozen motor congruence below is therefore global on `V`, while `W` is used
only as the L4 restriction whose ordered outputs must be read.

## Field 1: equations and proofs

### A. Public types

Public Canon v59 declares

```text
D_matter : dom(D_matter) subset K -> MatterData,
K = the set of pointed forward U-orbits,
U(n,psi) = (n+1,...).
```

Equality in `K` is equality of complete pointed sequences. Let `sigma` be tail
shift. The first counter coordinate gives

```text
sigma^r(kappa_(n,psi)) != kappa_(n,psi) for every r>0.
```

The completion contract freezes source and output equalities, totality domains,
field ownership, bridge rows, layer endpoints, write targets, `feeds_U`, and
optional U-congruence as distinct fields. The current `canon/GATES.tsv`
contains no `GATE-L4-L1-QDD-PURE-RECORD`.

### B. Global pure-record bridge

Let

```text
V = Q^4,
one = (1,1,1,1)^T,
G = I_4-(1/5)one one^T,
G^-1 = I_4+one one^T,
S = (V minus {0})/{+/-1}.
```

Let `B0=(1,zeta,zeta^2,zeta^3)` and
`iota_B0(v)=sum_i v_i zeta^i`. Public `DEF-QDD-DIRECT-WRITE` defines the
global helper `R_cyc:Q(zeta_5)->MatterData_QDD`. For `v!=0`, put

```text
m(v)   = v^T G v,
rho(v) = v v^T G/m(v),
b_alg([v]) = (m(v),rho(v)).
```

The trace-pairing matrix in `B0` is `G`, and the public rank-one operator
`T_w(x)=w<x,w>_tr` has matrix `v v^T G`. Hence the `total_weight` and
`density` fields of `R_cyc(iota_B0(v))` equal `b_alg([v])` globally.

Moreover

```text
rho(v)^2=rho(v),
rho(v)^sharp=rho(v),
rank rho(v)=1,
Tr rho(v)=1,
v v^T=m(v)rho(v)G^-1.
```

Therefore

```text
b_alg([v])=b_alg([w]) iff w=+v or w=-v.
```

So `b_alg:S->MatterData_QDD` is total and injective. It is a read-only
algebraic bridge with `feeds_U=FALSE`, but the declared decoder does not assign
`S` as a `D_matter` domain or assign stage ownership to this global source.

For the L4 restriction, define target-independently

```text
M_J = multiplication by J in B0,
D_J = M_J-I,
u_x = D_J^x e_0,
P = the G-orthogonal projector onto Q u_2,
Q = I-P,
W = QV,
A = Q D_J Q|W.
```

The global bridge restricts to every nonzero ordered output `OAv` and `AOv`
in `W`.

### C. Current finite leg

The public balanced carrier is

```text
V_eff={0,1,2,-2,-1}^4.
```

Its pure-record image has exactly 313 fibres. In contrast, both `S` and
`W^x/{+/-1}` are infinite; for example

```text
w_n=(1,n,0,-1-n)^T, n in Z,
```

are pairwise distinct sign classes. No map factoring through the current
313-element image can be faithful on the global or L4 rational source.

### D. Two static decoder-domain encodings

For an integer `a`, define the zigzag bijection

```text
z(a)=2a for a>=0, and z(a)=-2a-1 for a<0.
```

For naturals use Cantor pairing

```text
pi(x,y)=((x+y)(x+y+1))/2+y.
```

For a reduced rational `a/b`, `b>0`, put

```text
enc_Q(a/b)=pi(z(a),b-1).
```

For a nonzero vector choose the unique sign whose first nonzero coordinate is
positive and recursively pair the four rational codes. This gives an explicit
bijection from `S` to a decidable subset of `N_0`, with an exact inverse.

With the fixed zero checkpoint `psi_0`, define

```text
eta_1([v]) = kappa_(4 code([v])+1, psi_0),
eta_2([v]) = kappa_(4 code([v])+2, psi_0).
```

Both are injective, their images are disjoint, and both avoid the current
`K_QDD` heads at counter zero. On the disjoint unions

```text
K_QDD disjoint-union im(eta_i)
```

define a set-map extension of `D_matter` by retaining `D_QDD_direct` on
`K_QDD` and setting

```text
D_i(eta_i([v]))=b_alg([v]).
```

These are exact maps of the declared signature. They are not current
read-only decoder maps: each requires a new source-to-autonomous-state encoding
or write convention, so its completion record must declare a new write target
and `feeds_U=TRUE`. The two conventions are distinct under exact pointed-orbit
equality, and no current public equivalence identifies them. Thus the type
signature and algebraic helper do not select a static bridge.

### E. Global motor-to-U-tail no-go

The global motor satisfies

```text
D_J^5=I,
mu_(D_J)=Phi_5.
```

Every nonzero sign class has projective orbit exactly five. Indeed, if
`D_J^k v=epsilon v` for `1<=k<=4` and `epsilon in {+1,-1}`, then
`epsilon^5=1`, so `epsilon=1`; since `k` is invertible modulo five, this would
give `D_J v=v`, contradicting `det(D_J-I)=5`.

Freeze the dynamic bridge class as injective maps `eta:S->K` with a lag
function `r:S->N_0` satisfying

```text
eta(D_J [v])=sigma^(r([v])) eta([v]).
```

Iterating once around the five-cycle gives

```text
eta([v])=sigma^R eta([v]),
R=sum_(j=0)^4 r(D_J^j[v]).
```

Tail freeness forces `R=0`. Every summand is nonnegative, hence all five lags
are zero. Then `eta(D_J[v])=eta([v])`, and injectivity gives the impossible
projective fixed point `D_J[v]=[v]`.

Therefore this frozen faithful U-tail-congruent bridge class is empty. More
generally, because `b_alg` is injective, any factorization
`b_alg=D_out o eta` forces `eta` to be injective and is subject to the same
no-go.

This is not a no-go for every conceivable future bridge. A noncongruent direct
read-only source port or a changed autonomous architecture is outside the
frozen class.

### F. Target comparison last

Only after every bridge classification,

```text
u_2=-one,
P=(1/4)one one^T=E_low,
Q=I-P=E_high.
```

No target effect defines the global record, coding maps, or congruence class.

## Field 2: code

Accepted file:

```text
probes/P-QDD-PURE-RECORD-TYPED-BRIDGE-1/verify.py
```

Python standard library only. Integers and `Fraction` only. `Q(zeta_5)` is
implemented by four rational coefficients modulo `Phi_5`. No float, complex,
approximation, randomness, network, subprocess, external data, predecessor
import, scratch import, or filesystem read or write. Zero arguments.
Deterministic stdout, empty stderr, exit nonzero on any failed gate.

The verifier audits:

1. authority constants, metric, motor, and projective order-five certificates;
2. the cyclotomic trace Gram and global direct-helper rank-one identity;
3. pure-record projector and reconstruction identities;
4. exact sign fibres on a frozen rational control class;
5. the 313-fibre current finite image;
6. infinitely extensible rational controls on `W`;
7. exact rational-code round trips;
8. two disjoint counter encodings and exact decoded records;
9. tail freeness and the nonnegative-lag reduction;
10. one L4 internal-commutator witness read by the global bridge;
11. target comparison last.

Universal injectivity, infinity, static-extension, and U-congruence statements
are carried by the written proofs. The machine is their audit.

## Field 3: carrier

```text
global source:           S=(Q^4 minus {0})/{+/-1}
L4 source:               (W minus {0})/{+/-1}
record:                  (total_weight,density)
current decoder domain:  K_QDD subset K
full decoder type:       dom(D_matter) subset K
static encodings:        eta_1, eta_2
dynamic comparison:      D_J on S versus tail sigma on K
post-state equality:     v ~ -v
```

No external data.

## Field 4: systematics

No tolerance and no retry.

```text
D_J incorrectly treated as preserving W       STOP
read-only algebraic map called D_matter        STOP
set injection called physical selection       STOP
static encoding called U-congruent             STOP
current 313-image widened to Q^4               STOP
new write target hidden                        STOP
feeds_U left implicit                          STOP
target effects used before final comparison   STOP
pre-pin accepted-verifier execution            STOP
post-pin mutation or threshold change          STOP
```

Runtime limit: 120 seconds.

## Field 5: failure threshold and decision

```text
READONLY-BRIDGE-ONLY
  the global algebraic bridge is exact and faithful; the finite current leg is
  insufficient; two exact static orbit encodings exist and are nonselected;
  the frozen faithful global motor-to-U-tail bridge class is empty; and the
  named gate, source ownership, write/feed decision, and passed decoder bridge
  remain absent.

CURRENT-TYPED-BRIDGE
  a complete already registered bridge supplies every frozen source, domain,
  equality, ownership, write, feed, dependency, layer, and gate field without
  a new convention or architecture change.

U-CONGRUENT-BRIDGE
  an exact faithful member of the frozen global motor-to-U-tail class exists.

ALGEBRAIC-F | FINITE-F | ENCODING-F | U-CONGRUENCE-F | TYPE-F |
TARGET-F | STOP
```

Scientific negative routes exit zero with exact witnesses. Integrity STOP exits
nonzero and carries no scientific conclusion.

Maximum later rows:

```text
QDD-PURE-RECORD-READONLY-BRIDGE [T]
QDD-PURE-RECORD-STATIC-ENCODING-NONSELECTION [T]
QDD-PURE-RECORD-U-CONGRUENCE-NOGO [T]
QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY [T]
```

All are restricted to the frozen exact source, record equality, decoder
signature, and L1/L4/MULTI boundary.

## Field 6: layer and firewalls

L1 exact record and autonomous-state algebra plus L4 apparatus/support. The
candidate cross-layer gate is named but not registered or passed. No L5 stream
or L6 measure.

Global O2 remains open unless a later independently justified architecture
adds a direct read-only L4 source port or supplies another complete physical
bridge. O1 is untouched.

```text
SAMPLING NOT PROVIDED.
```

No decoder completion, `QUADRATIC-DECODER-DATA` status move, SI statement,
Bell claim, Canon, registry, frontier, gate-table, workflow, policy, release,
or existing-probe edit.

## Formal order

Commit and push `PREREG.md` and `verify.py` together; read both back byte for
byte from the public remote; execute the accepted verifier exactly once from
the repository root; add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without
changing pin bytes; open one probe-only pull request; require byte-identical
x86_64 and aarch64 replay and aggregate `check`; merge with a merge commit
only. Canon treatment is separate.
