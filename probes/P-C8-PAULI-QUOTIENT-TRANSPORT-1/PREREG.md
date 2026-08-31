# P-C8-PAULI-QUOTIENT-TRANSPORT-1

Status: PREREGISTERED / UNRUN / NON-CANONICAL.
Public lock: issue #724. Owner: A. M. Thorn / C8 transport session.
Action layer: L1 exact algebra and externally supplied operator comparisons only.

## Authority and source audit

- Public base: `9f88c4c93aab3139ee0a2e007f0e60891957aa21`.
- Authority: Public Canon v72, `mathorn1973/twist-j main`.
- Canon content commit: `aac8a3a4aff027beb2b08edbde1ae8e59224914c`.
- Canon SHA-256: `39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70`.
- Canon byte count: 374406. Tag: `canon-v72`.
- The base is a descendant of the tag; the intervening changes do not touch
  the normative Canon bundle.

Registered source objects are `PENTIT-ROOT-FACTS [T]`,
`RAMIFIED-TM-LIFT [T]`, `SQRT-PHI-DIGIT-LIFT [T]`, and
`C8-BILINEAR-SHADOW [T]`. In particular, the last row's actual readout,
not a substitute invented to pass this test, is frozen below. Its source proof
is `probes/P-C8-BILINEAR-SHADOW-2/PREREG.md` at the public base, blob
`63b1756ade96ed0d3414a7fdb472f0cdc25c449d`.

`I-BILOCATED [D]` names the order-four element 2 in F5 and zeta8^2 on the
other side. Its foundations witness checks these two orders separately.
It supplies neither a field embedding nor the complete readout map constructed
here. G2 explicitly formalizes its marked multiplicative comparison as
beta_+(2)=i. All use of that orientation is conditional on this D marking;
no forcing theorem, independent physical selection, or stronger dictionary
status is inferred. `SILVER-SIBLING [D]` is background, not a root selector.

Merged #717 and #722 are predecessors, not registered Canon premises. Their
needed character identities are proved again here. Neither issue #716 nor
#721 is closed or registered by this probe. Canon, Registry, Frontier,
dictionaries, gates, workflows, and all prior probe bytes remain unchanged.

The source results and the analytic derivations below are known before the pin.
This is a transparent proof-and-audit exercise, not blind empirical discovery.
Only syntax/compilation checks are permitted before public preregistration;
no execution of this verifier is permitted before its pin and readback.

## Frozen types, equalities, and context

Let K=F25=F5[tau]/(tau^2-2), H=<tau>, H0=F5*=<tau^2>, eta=tau^3,
and sigma(x)=x^5. Fix a formal primitive eighth root z in the complex
comparison, i=z^2, P_k=diag(1,z^k), T=P_1, S=P_2, Z=P_4.
The complete character class is

    E={rho_k:H->mu8, rho_k(tau^n)=z^(kn) : k in {1,3,5,7}}.

The symbol tau is a presentation coordinate, not a naturally selected root.
All branch statements compare both roots and use a SINGLE common character
and root branch across a whole record or across both uses of an operator.

For the character quotient, equality means precomposition by sigma; on the
normalized generator matrices it is equivalently LEFT multiplication by
{I,Z}. It does not mean arbitrary input/output Pauli frames, Pauli conjugation,
Clifford equivalence, or physical gauge equality. G1 audits a broader frame
relation as a negative control and does not adopt it.

For the registered shadow, equality means exact equality at every same named
coordinate. Coordinates are tagged by (Theta,n), (Even,n) with even s2(n),
and (OddPair,n,m) with both digit sums odd. No index permutation, discarded
coordinate, hidden normalization, or branch-dependent choice of character is
allowed. Its source values are nonzero elements of H0 and its transported
values lie in mu4. The complete admissible transport family is E restricted
to these coordinates, or the two extensions of beta_+ when G2's marking is
supplied. This is completeness within that explicit family only.

The one-copy comparison uses all density matrices on an externally supplied
C^2, all fixed Hermitian A, and exact scalar equality of Tr(A rho).
The two-use comparison instead freezes the Bell preparation, the same P_k on
both factors, and the fixed observable X tensor Y with its labelled outcomes.
Neither apparatus nor its Hilbert carrier is asserted to come from TWIST-J.
These are different frozen contexts, not an enlargement after a failed test.

## G1. Quotient, restriction, and frame boundary

Prove and audit

    E/<sigma>  ~=  Iso(H0,mu4),
    res(rho_k)(2)=z^(2k),
    fibres = {1,5} and {3,7},
    P_(k+4)=Z P_k.

Proof: a generator of C8 must map to one of its four generator roots.
Two such characters agree on tau^2 exactly when their exponents agree modulo
4, hence exactly in the displayed pairs. Precomposition by sigma sends
k to 5k=k+4 modulo 8 on the odd exponents. Each restriction has two extensions,
so restriction induces the stated bijection of orbit sets.

On this diagonal normalized family, equality up to a LEFT Pauli and global
phase gives the same two classes: an off-diagonal Pauli cannot turn a
diagonal matrix into another diagonal matrix, leaving only I and Z.
However the additional input/output frame relation obeys

    X P_k X = z^k P_(-k).

Together with left Z this connects all four exponents. Therefore the two
surviving orientations are not invariant under every relation informally
called 'modulo Pauli'. The equality must be named. Literal equality modulo
a global scalar alone still distinguishes all four, since the 00 entry is 1.

## G2. Conditional dictionary transport

Define the two faithful multiplicative characters of H0 explicitly:

    beta_+(2^j)=i^j,      beta_-(2^j)=i^(-j).

Proof: 2 generates H0 of order four; specifying its primitive image determines
one and only one character. The condition beta_+(2)=i selects exactly
rho_1 and rho_5 among E. It therefore selects ONE orbit in E/<sigma>,
not one root or one representative of E. Without this marking beta_- survives.

This is a theorem about a supplied comparison marking, not a theorem that the
marking is forced. In particular no equality of elements of fields of
characteristics five and zero is asserted.

## G3. Descent of the existing complete bilinear shadow

Write w_n=s2(n), Theta_n=2^w_n, and Y_n^epsilon=(epsilon eta)^w_n.
Use exactly the registered record

    V^epsilon=(Theta_n for every n;
               Y_n^epsilon for even w_n;
               Y_n^epsilon Y_m^epsilon for odd w_n and odd w_m).

The source theorem gives V^+=V^-=V in H0 at every coordinate.
For k=1 or 5, the coordinatewise transported record is exactly beta_+(V).
The closed formulas are

    Theta_n              -> i^w_n,
    Y_n, w_n even        -> i^(3 w_n/2),
    Y_n Y_m, both odd    -> i^(3 (w_n+w_m)/2).

The half exponents here are integers in precisely the tagged contexts.

Proof for every n,m: eta^2=tau^6=3=2^3, so for even w,
Y=3^(w/2); for odd w,v the two signs cancel in the product and
Y_w Y_v=3^((w+v)/2). Restricting either extension of beta_+ gives the formulas.
All expressions depend only on exponent residues modulo eight, which the
verifier exhausts rather than inferring an infinite theorem from a prefix.
The 28 coordinates of that finite audit are eight Theta residues, four even
residues, and sixteen odd/odd pairs, not a replacement for the infinite record.

The fibres of the FULL transported record among all four characters are
exactly {1,5} and {3,7}. The forward implication follows from restriction;
for the converse Theta_1=2 gives i for the first pair and -i for the second.
Within the marked pair, every overlap and every named coordinate agrees.

Each transported scalar is in mu4. If separately read as diag(1,c), it is
an S power, not a non-Clifford gate. The source record's mod-eight exponent
refinement is not a claim that this transported scalar output is a T gate.

## G4. Exact parity boundary of this scalar descent

For h=tau^n,

    rho_(k+4)(h)=(-1)^n rho_k(h).

Since h and its character value are nonzero, equality holds iff n is even.
Thus H0 is the entire branch-invariant scalar subgroup for faithful character
transport. A product has this property iff its TOTAL tau exponent is even.
Here 'degree' in the verifier's labels means this total branch exponent,
not a claim about the Boolean degree of a phase polynomial.

For Y factors the total exponent is 3 times the total digit sum; its parity
is the same. Mixed-parity products therefore fail descent. The explicit
w=0,v=1 witness is eta itself. This maximality is only for individual scalar
monomials in H, not a classification of every nonlinear or relational readout.

## G5. Complete fixed one-copy linear readout classification

For every fixed Hermitian A, and any one (equivalently every) k in E,

    Tr(A P_k rho P_k^dagger) = Tr(A P_(k+4) rho P_(k+4)^dagger)
    for every density rho

holds iff

    Z A Z = A  iff  [A,Z]=0  iff  A=a I+b Z, a,b real.

Proof: conjugation by P_k bijects the density matrices. The claimed equality
is Tr((A-ZAZ) eta)=0 for every density eta. Densities span Herm2(C): the
projectors onto |0>, |1>, |+>, and (|0>+i|1>)/sqrt2 span the Pauli basis.
Nondegeneracy of the trace pairing forces A-ZAZ=0. Expanding in I,X,Y,Z,
conjugation by Z has signs (+,-,-,+), proving the complete fixed subspace.
Conversely each such A satisfies the equality. Since every diagonal A commutes
with every diagonal phase, these readouts are blind to ALL k, not only k+4.
The same conclusion holds componentwise for a frozen family of such reads.

This does not make the gates equal. On |+>, P_k and ZP_k produce orthogonal
pure states: their inner product is (1+z^4)/2=0. The verifier checks the
normalized rank-one densities and zero overlap exactly. A tracked correction
bit b can instead implement Z^b P_(k+4b)=P_k; carrying that bit is not forgetting
it, and no such physical record is supplied here.

## G6. Correlated two-use positive and independent-branch negative controls

Supply externally |Phi>=(|00>+|11>)/sqrt2 and the same P_k on both factors.
Then

    |Phi_k>=(P_k tensor P_k)|Phi>
           =(|00>+i^k|11>)/sqrt2.

The COMMON branch change k->k+4 adds Z tensor Z, which acts as identity on
span{|00>,|11>}. Moreover

    (X tensor Y)|Phi_k> = +|Phi_k> for k=1,5,
    (X tensor Y)|Phi_k> = -|Phi_k> for k=3,7.

Proof: X tensor Y sends |00> to i|11> and |11> to -i|00>; substitute i^k=+i
or -i. This is an exact quotient-faithful comparator with labelled outcomes,
without choosing a representative inside either pair. Changing only one
factor by Z negates the relative coefficient and reverses that outcome.
Thus correlated/common branch and independent per-use branches are not the
same assumption. This is two uses on a prepared pair, not copying an unknown
quantum state, and not an implementation derived from the scalar shadow.

## G7. Source involution, field sum, and Born-norm firewalls

Source sigma acts by exponent 5, whereas complex conjugation on mu8 acts by
exponent -1. An intertwining character rho_k would require 6k=0 modulo 8.
The only solutions are k=0,4; neither is faithful. In particular

    N_K/F5(tau)=tau^6=3,
    beta_+(3)=-i,
    rho_k(tau) conjugate(rho_k(tau))=1.

The multiplicative transport does NOT intertwine these norms. Also
beta_+(1+1)=i differs from beta_+(1)+beta_+(1)=2. No unital field embedding
F5->C exists at all, because it would send 5*1=0 to 5*1!=0.
The complete readout transport proved in G3 preserves the explicitly stated
products and powers, not addition, a Hilbert norm, a Born measure, or the
Born involution of a different residual product ring.

## Method, systematics, and failure threshold

Accepted code: `verify.py`, 10667 bytes, SHA-256
`091c2c924ab4ce530e556ebd8c99a128abc8b76bfb7ac764217efb8de452de2f`.
Python standard library only. The only imports are fractions, itertools, and
math. Rational coefficients in Q[z]/(z^4+1) represent the operator comparison;
F25 uses integer pairs modulo five. There is no float, external dataset,
randomness, network, filesystem access, subprocess, environment-dependent
branch, or optional dependency in the verifier. Checks use explicit exceptions
and cannot be disabled by Python optimization.

The finite scopes are all 25 source field elements for the root pair, eight
H elements, four faithful characters and their products, all exponent residues
modulo eight and residue pairs, the four-element Pauli basis, and four exact
one- and two-use phase cases. The universal readout and all-index statements
rest on the displayed proofs and finite spanning/period arguments.

PASS requires seven PASS lines followed by RESULT 7/7 ALL PASS, exit zero,
empty stderr, unchanged pinned file hashes, and byte-identical stdout on the
required x86_64 and aarch64 workflow jobs. Any false displayed theorem, wrong
fibre, hidden marking, wrong parity, false commutant classification, failed
control, or illicit norm/gauge identification kills the affected claim.
An implementation or integrity failure alone is STOP until distinguished from
an exact mathematical counterexample. Pinned PREREG.md and verify.py must never
be amended after execution; failures are retained with the original pin.

No physical carrier, apparatus, preparation, coupling, branch occurrence,
Born rule, common-branch law in Nature, decoder completion, speedup,
universality, clock, gravity, SI quantity, or L2-L6 lift is claimed. Invariance
of this one readout does not select a raw k or decide all possible readings.

## External terminology sources

These sources fix comparison terminology only. No source code, dataset, or
external software implementation is imported. The matrix identities and proofs
are self-contained above.

- S. X. Cui, D. Gottesman, A. Krishna, *Diagonal gates in the Clifford
  hierarchy*, Physical Review A 95, 012329 (2017), arXiv:1608.06596v1.
  https://arxiv.org/abs/1608.06596v1
  The level depends on both polynomial degree and root order, not Boolean
  degree alone. Hierarchy membership is not an operational equality rule.
- IBM Quantum, TGate and ZGate matrix definitions, consulted 2026-08-31:
  https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.TGate
  https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.ZGate
  Only the displayed matrices are used, not SDK behaviour or versions.
