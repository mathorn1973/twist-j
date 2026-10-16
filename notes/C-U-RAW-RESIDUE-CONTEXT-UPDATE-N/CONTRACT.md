# Raw-residue context: comparison contract

**NON-CANONICAL. Proof-first, result-exposed, L1 only. Candidate-T.**
Date: 2026-10-12, Europe/Prague. Author: A. M. Thorn.
Reservation: [#1474](https://github.com/mathorn1973/twist-j/issues/1474).

This is written mathematics in a notes package, not a formal public probe.
The conclusions were derived and discussed before public pinning. There is
no claim of blind discovery, scientific execution, computational evidence,
physical implementation or Canon promotion.

## 1. Authority and source binding

The public basis is commit
`5f54015ed8361e3a64cb10894397020ddfadd104`, Public Canon v101 ACTIVE.
Its authority declaration names content commit
`421a4ec1daf07c04d19022c1ee219607e83c09a8` and tag `canon-v101`.
The unchanged Canon has 992352 bytes and SHA-256
`b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`.
The local file hash and byte count agree. The coordinating session verified
public authority and CI before reserving this lane; this note does not claim
a second independent remote verification.

Normative premises, at that immutable basis:

- [STATUS](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/STATUS.md),
  [POLICY](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/POLICY.md)
  and [AGENTS](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/AGENTS.md).
- [U-NATIVE-RAW-RESIDUE-READOUT](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/canon/CANON.md#u-native-raw-residue-readout-t):
  the first-three-tick receiver table, alternating-floor sum, synchronized
  inverse and actual Thue-Morse increment identity.
- U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO and
  U-NATIVE-RAW-RESIDUE-PRESENCE-BOUNDARY in the same Canon: current receiver
  and absence limitations at their registered scopes.
- [Existing supplementary audit README](https://github.com/mathorn1973/twist-j/blob/5f54015ed8361e3a64cb10894397020ddfadd104/reproduce/u_raw_residue_port/README.md):
  evaluation context versus mechanism, including the known twenty-context
  successor ambiguity. Its executable is neither imported nor executed here.

The actual native law is unchanged:

```text
Omega = N_0 x F5^6,
psi = (p1,p4,p1p,p4p,q,r),
theta_n = popcount(n) mod 2,
z(psi) = sum(psi) mod 5,
U(n,psi) = (n+1, g_(z(psi)+2 theta_n mod5)(psi)),
(g_0,...,g_4) = (a,b,c,d,e).
```

The complete input family is every P in F5^4, launched at origin zero
with the same receiver C_0=(q_0,r_0)=(0,1). Its label is
`kappa(P)=p1+p4+p1p+p4p mod5`. Every label has 125 inputs.
The observed current receiver is C_n(P)=(q_n,r_n). No source-side sum is
inserted into the preparation.

## 2. Class A: finite autonomous source-independent context

Admit every finite nonempty set A, every self-map h:A->A and one common
initial context a_0 independent of P. Define a_(n+1)=h(a_n).
The context receives no n, driver bit, checkpoint, receiver, source,
history, additional input or feedback. h need not be a permutation.
The reader is any fixed function d:A x F5^2 -> Y for any output set Y.

For an arbitrary F:F5->Y, the tested eventual readout property is:

```text
for every P there is a finite N_P such that
d(a_n,C_n(P)) = F(kappa(P)) for every n >= N_P.
```

All finite sizes, transient lengths, periods and nonlinear reader tables
are included. Equality of contexts, receiver states and outputs is literal.
The proposed complete decision is: such an eventual property is possible
only for constant F; constant F is attained by a one-state context and a
constant reader. In particular no member of this entire class reads all
five original residues permanently, even after an arbitrary waiting time.

This does not exclude a receiver-driven observer storing the payload,
an unbounded context, exposed native driving information, a larger observed
port, a different preparation, feedback or an interaction added to U.

## 3. Class B: an explicitly bit-driven finite reading context

This is a different supplied interface. At transition n->n+1 the context
receives exactly one exposed bit b_n=theta_n, with its ordering and
synchronization specified as part of the contract. It receives no integer
n, source coordinate, receiver value or saved receiver history.
The driver access is an additional admitted resource; the construction
does not derive a device for acquiring it.

The context is source-independent and starts once at a common state I0.
The complete context set is

```text
B = {I0,I1,I2} disjoint-union
    ({+1,-1} x {1,4} x F5).
```

At every bit b in {0,1}, the primitive startup transitions are
`I0->I1`, `I1->I2`, `I2->(+1,1,0)`.
They ignore b. A ready context is tau=(sigma,z,nu). Put

```text
t(z)=0 if z=4, and 1 if z=1,
delta=[b=t(z)],
h_b(sigma,z,nu)=(-sigma, 4+2b mod5, nu+delta mod5).
```

This is one total transition rule on all 23 contexts and both bits. It
does not use a fresh preparation on repetition. The rules are not asserted
to be bijections or to implement reversible material registers. Discarded
information, physical acquisition, energy costs and a realization of the
context mechanism require a separately admitted complete apparatus.

The fixed reader d_B:B x F5^2 -> {BLANK} union
{PRESENT(k):k in F5} returns BLANK at I0,I1,I2. At ready tau, calculate

```text
qhat = 1 + sigma*(q-z) + nu mod5,
rhat = sigma*r - nu mod5.
```

Use the fixed table

```text
(1,0)->0, (2,0)->1, (2,1)->2, (3,1)->3, (1,2)->4.
```

Return PRESENT(k) when (qhat,rhat) has table value k, and BLANK otherwise.
The proposed result is exact PRESENT(kappa(P)) for every P and n>=3;
startup is exactly BLANK for n=0,1,2. PRESENT(0) is distinct from BLANK.
BLANK here is a reading/readiness convention, not an absence certificate.

The bound is 20 ready contexts plus three startup contexts, hence 23 total.
It is an existence upper bound, not a proved optimum over class B or other
interface classes. The result supplies neither a finite autonomous clock
of class A nor an in-machine implementation of the native reader.

## 4. Receiver-driven payload observers are a separate class

A processor receiving C_1 can store kappa because the inherited five C_1
values are distinct. Such a processor has source-dependent memory after
that observation. It is outside both A and B above. Calling its stored
payload a source-independent clock would change the contract.
No construction or minimum for the complete observer/apparatus class is
claimed here.

## 5. Adjacent ownership and novelty

1. Public v101 already supplies the twenty-valued *evaluation* context and
   its particular successor ambiguity. That example is inherited and gets
   no novelty credit. The new A claim quantifies over every finite
   autonomous source-independent context, using explicit arbitrarily late
   modulo-period witnesses. The new B claim supplies an exact driven
   update, initial readiness and source/resource accounting.
2. [C-U-CLOCK-BLIND-AUTONOMOUS-FACTOR-N](https://github.com/mathorn1973/twist-j/tree/33ce1af982f08bb83b242c64111b0e4ef807fd34/notes/C-U-CLOCK-BLIND-AUTONOMOUS-FACTOR-N),
   owner #1290, has a fixed present-*checkpoint* factor with no auxiliary
   memory, n, driver or history. Its f(F_theta(x))=L f(x) classification
   concerns a different observed carrier and dynamical-factor question.
   Our A allows arbitrary finite independent auxiliary context but reads
   only (q,r) and asks for a permanent original-sum value. Neither result
   is substituted for the other.
3. [P-U-NATIVE-FIXED-READ-1](https://github.com/mathorn1973/twist-j/tree/ec4995176d36005ba924e0b381c3cc72b97420fc/probes/P-U-NATIVE-FIXED-READ-1),
   owner #1429 / PR #1430, studies actual writing into an independently
   occupied piston receiver with a source fibre (q,r), a fixed local
   polynomial read and a declared affine preparation class. That port
   orientation and preparation are not the v101 raw-piston/common-(q,r)
   family used here. No new native SUM/write result is claimed.

## 6. Decision rules and execution boundary

- A fails if the explicit digital lemma, same-context modular argument,
  exact receiver supports or their connected overlaps fail, or if an
  admitted nonconstant eventual F is exhibited.
- B fails if the total update, startup timing, increment identity or
  fixed readout fails on an admitted native input/time. Changed driver
  access, wrong synchronization or another preparation changes the class.
- A proof gap is STOP pending repair, not an empirical falsifier or a
  global physical impossibility statement.
- Only analytical derivations are supplied. No scientific program has
  been authored, imported or executed for this package. Any later
  supplementary audit requires separately frozen source, a public pin and
  byte readback before its first scientific execution. Its finite checks
  would audit the proof, not establish the all-time quantifiers.
- No Canon, registry, frontier, workflow, status, physical owner or L2-L6
  gate changes. No ion experiment, occurrence law, sampling law, source
  erasure, autonomous native context register, reset, repeated loading or
  six-label presence/absence channel is supplied.
