# P-NATIVE-P-RECURRENCE-BOUNDARY-1

PUBLIC / NON-CANONICAL / L1. Owner: A. M. Thorn,
ChatGPT-native-p-recurrence-20261018. SPDX-License-Identifier: Apache-2.0.
Claim: https://github.com/mathorn1973/twist-j/issues/1630

This is a new successor to the completed #1628/#1629 admission STOP.
It neither resumes that assignment nor changes its owner or verdict.
The disclosed targets below are analytical conjectures before execution.

## 1. Equation and exact assertions

Use raw coordinate order x=(p1,p4,p1p,p4p,q,r) in F5^6. Write z=sum(x),
theta(n)=s_2(n) mod 2, f_t(x)=g_(z+2t)(x), with g=(a,b,c,d,e).
The literal maps, all modulo five, are

```text
a(x)=(p4,p1,p4p,p1p,q,r)
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r)
c(x)=(2-p1p,1+r-p4p,2-p1,1-r-p4,1-q,-r)
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r)
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r)
U(n,x)=(n+1,f_theta(n)(x))
T0=(0,4,0,4,4); T1=(2,1,1,3,1)
```

A. On the synchronized sheet z=4+2 theta(n-1), the k-step raw
linear difference map is (-1)^k B^s, where B exchanges p1 with p1p
and p4 with p4p and fixes q,r, and
s=theta(n-1) XOR theta(n+k-1). For every k>0 and every lower bound N,
choose an integer j with 2^j>k, j=1+theta(k-1) mod 2, and
n=2^j-k+1>=N. Both endpoint bits are one, so the difference map is
(-1)^k I. Combined with the inherited nine-tick synchronization and
the reference permutation, this excludes the full #1629 local paired
contact in the complete literal-product class in section 3.

B. Freeze independently of P the class of all triples (D,delta0,delta1),
where D is a nonempty subset of F5 and delta0,delta1 in F5, such that
C_t=tau^delta_t f_t is a permutation of the full union X_D of z sheets
for both t, with tau=e composed with d (q -> q+1). There are exactly
seven triples: five singleton choices D={z}, delta_t=z-T_t(z), and
two maximal pairs:

```text
D={0,4}, (delta0,delta1)=(0,3)
D={0,1}, (delta0,delta1)=(1,4).
```

No triple has |D|>2. Only the first pair leaves the t=0 update unchanged.
This is a complete classification ONLY of this translation-correction
class, not of arbitrary corrections, controllers or native extensions.

C. On X=X0 union X4 select C_t=tau^(-2t) f_t. Each C_t is an involution
of all 6250 states and preserves each individual z sheet. All occupied
coordinates are included. The full forward clocked compound map is
(n,x)->(n+1,C_theta(n)(x)), with the previous-bit inverse on its image.
This compound tick is newly declared, not one original U tick.

D. Freeze an explicit five-microtick implementation, also newly declared.
Every microtick advances the actual n once. At r0=n mod 5=0 use the
literal selector f_theta(n). At phases 1,2,3,4, put m=n-r0 and t=theta(m).
Apply temporal d,d,d,d when t=0, and e,d,e,d when t=1. Hence
V^5(n,x)=(n+5,C_theta(n)(x)) at every block start n=0 mod 5.
The allowed full state slice at phase r0 is the image of X under that
block's first r0 commands; the explicit sheet sets and inverse are in
PROOF.md. Prove full slice-to-slice bijectivity, including block boundaries
where the next theta bit differs. No additional register is silently reset.
The n+1 compound law and the n+5 blocked law are distinct clock contracts;
theta(5n) is not identified with theta(n), and no such rescaling equality
is claimed.

E. Use the exact paired input
xplus=(1,1,0,0,3,0), xminus=(1,1,0,0,2,0).
Only the native source coordinate q differs. All nonsource coordinates,
including the occupied receiver R=(p4,p4p)=(1,0), are common.
For BOTH t, the corrected receiver outputs are (1,0) and (0,4).
The one fixed present receiver read
rho(R)=sgn(ell(p4)^2-ell(p4p)^2), ell=(0,1,2,-2,-1),
gives +1 and -1 without source, clock or history access. The source
distinction z=0 versus z=4 is retained in the full state at block boundaries.
No permanent record, arbitrary-input message decoder, source depletion,
or complete funded P semantics are claimed.

## 2. Code

Accepted author executable: verify.py, Python standard library only.
Independently authored method-separate executable: break.py, written from
this frozen specification and canonical definitions before verify.py exposure.
Both must be committed, pushed and read back with this preregistration
before ANY scientific execution, import or dry run. The verifier will
run the breaker as a separate process under the same deterministic
repository environment; its complete stdout is part of EXPECTED.txt.
Neither executable imports the other scientific implementation.
Public CI must replay BOTH pinned code files, with byte-identical combined
stdout on x86_64 and aarch64 before any computation-grade promotion.
The code and source manifest are bound by CODE_SHA256SUMS and SOURCES.tsv.
Static parsing, compilation and custody checks are allowed before the pin.

## 3. Carrier, data, admission and equality

The negative class consists of every m>=1, X_m=N_0 x (F5^6)^m with
componentwise original U and ONE common native clock. No CSUM, intervention,
independent phase offsets, added control, extra clock, or nonnative register
is allowed. The product is an explicitly declared product of original
cells; no coupling is inferred. Raw source and receiver coordinate sets
are fixed and disjoint. The class of carriers is nonempty.

The reference is the entire Y_(8,3) and the full F_P in #1629 CONTRACT.md,
source commit 217cfc13befc3ab4b14444aed49e3fce7f50a7b7. It is a
permutation and contains the two specified common-ready accepted inputs
with opposite r_P records. The proposed encoding may be arbitrary,
nonlinear and n-dependent; require faithful full-state decoding and

```text
V_m^k Enc(n,y)=Enc(n+k,F_P(y))
```

for every n>=3, y in Y_(8,3), one fixed k>0. At EVERY such n, all encoded
nonsource raw coordinates coincide for the reference witness pair.
One present receiver function, with only common n and fixed parameters,
must return the reference record throughout the complete encoded domain.
Auxiliary native cells are included in m and in these support conditions.
Fixed spectators may be included; changing external records may not.
The universal negative is an analytical theorem, not a finite search over
encodings or cell counts. Different admitted start sets are outside scope.

The positive class is the full X_D above and its complete microphase
images. Native raw coordinates, letters and theta are ORIGINAL_NATIVE;
free commanded words are ADMITTED_CONDITIONAL at their canonical scope.
The correction actuation, five-phase schedule and selection of X0 union X4
are NEW_DECLARED relative to U. The minimality statement concerns |D| and
the fixed q-translation class only. It is not minimal physical resources.
No P-shell encoding, bank, H_P conservation, Weyl record or physical price
is supplied for the extension. Its complete stored state is exactly n,x;
all six coordinates persist through each inverse. Clock evaluation is an
explicit mathematical rule, not an unpriced physical apparatus claim.

## 4. Systematics and finite audit inventory

Exact integers/F5 only, no float or fitted tolerance. Cover all 15625
checkpoints for raw involutions, tau, selector sheet laws; all nonempty
D and all 25 correction pairs; both bits and all full selected sheets;
all five microphases including inverse and boundary bit changes.
The author finite clock audit covers k=1..256 and j chosen by A with
N=3+ceil(9/k)*k. It checks the bit certificate and composes the actual
affine block on the synchronized sheet, not an assumed target formula.
Both implementations check literal source-local paired acquisition and
the same exposed reference P pair, including its full inverse/bank/Weyl
coordinates; this small reference audit is not a full Y_(8,3) simulation.
The breaker chooses its own exact implementation and additional finite
attacks before freezing. Record this same-session, result-exposed
separation honestly. Reproduction is not independent authorship.

## 5. Failure threshold and dispositions

One exact counterexample to A, B, C, D or E fires its corresponding
falsifier, preserved as such. Zero failures are required for a positive
finite audit. A source/hash/environment mismatch is integrity STOP, not
a mathematical falsifier. A failed or incomplete executable is not
fabricated successful evidence and the repository's pin rules apply.

A surviving proof A gives NO_REALIZATION_IN_FROZEN_CLASS for the entire
literal-product class only. Surviving B-E give DECLARED_EXTENSION_ONLY.
They do NOT give NATIVE_CONTACT_REALIZED_IN_FROZEN_CLASS for P. Broader
P admission remains OPEN / STOP_ADMISSION_UNSUPPLIED at the predecessor's
scope. No negative conclusion about every native or physical architecture.

## 6. Action layer and dependencies

L1 only. Public basis dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d,
Public Canon v103; immutable source #1629 as above. SOURCES.tsv binds
the exact consumed files by commit, Git blob, bytes and SHA-256.
Inherited native chart/nowrite, KERNEL-Z6-SYNCHRONIZATION and
TM-SHEET-SYNCHRONIZING-GRAPH retain their source status and scope.
This work does not rediscover their synchronization or prove a T=diag(J,phi)
reading. No Canon/registry/gate/workflow/policy change, L2-L6 lift,
physical energy/phase/time/SI assertion, merge or release is included.
