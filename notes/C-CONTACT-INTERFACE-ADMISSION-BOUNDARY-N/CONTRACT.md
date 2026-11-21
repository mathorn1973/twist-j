# Contact interface admission boundary: analytical contract

NON-CANONICAL / NO AUTHORITY. Action layer: L1.
Owner: A. M. Thorn. Public reservation: [#1398][issue].
This is a written-proof task, not a computational preregistration or probe.

## 1. Basis and inherited evidence

Public main is pinned to
`7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`.
STATUS declares Public Canon v100, tag `canon-v100` at
`807dae3fe97dd6a872d5d1305a0133e8e8d856ea`, content commit
`a4cc9666662967527abe711441833ff600c00337`, Canon size 980212 bytes and
SHA-256 `5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4`.
These are source pins, not a new activation. The public main and tag need
not have the same head after the notes-only merge #1397.

The mathematical sources at that main are:

1. [CANON.md][canon]: DEF-RESIDUAL-CONTACT-ARCHITECTURE,
   CONTACT-RECORD, ALGEBRAIC-RESIDUAL-REALIZATION,
   QDD-DIRECT-RECORD-E-NONCONGRUENCE, and the exact scope of
   QUADRATIC-MEMORY-NATIVE-CONTACT.
2. [The complete source-table classification][classification], sections
   2, 3, 5--7. It remains a NON-CANONICAL conditional proof. This successor
   rederives the reduction it needs; it does not promote that package.
3. [The full CW-ALG-1 specification][spec], section 5 and appendices A/B,
   for the precise translation words, factor primitivity, isolated
   three-cycle and constructive alternating-group argument. These source
   constructions are not re-executed or silently replaced.

Attached historical/internal Canons, local unpublished packages, physical
measurement, and the separate actual-U orientation work in #997 are not
evidence dependencies.

## 2. Complete mathematical carrier and class

All field arithmetic is in F5. Boolean addition is XOR, written `xor`.
Products act right to left; `[A,B]=A B A^-1 B^-1`.

The complete carrier and the projection forgetting only q are

    X = F5^12 x {0,1},
    z = (p_x,q_x,r_x; p_y,q_y,r_y; eta),
    F = D x {0,1},  D = F5^10,
    rho(z) = (p_x,p_y,r_x,r_y,eta).

Each p has four native piston coordinates in the existing row-major
2-by-2 reshape. Put

    K = ((0,0,0,3),(0,0,2,0),(0,2,0,0),(3,0,0,0)),
    h(p_x,p_y) = p_x^T K p_y,
    G = (det X_p, h, det Y_p),
    I = b_x b_y,  I_a = a_x a_y,  tau_i = e_i d_i.

Thus h(I s)=-h(s), I tau_i I=tau_i^-1, and tau_i adds one to q_i
while fixing all other coordinates. The data variable s includes all
twelve F5 coordinates, not only pistons or the factor D.

The previously classified complete source-table class consists of every
globally bijective map

    W(s,eta) = (I^a(h(s),eta) s, beta(h(s),eta)),

where a,beta are Boolean functions on F5 x {0,1}. Its h=0 branch is
unrestricted subject to bijectivity. Equality of W, E_W=W I W^-1, and
K_(W,i)=[E_W,tau_i] means literal equality on all X. An involution is an
explicit additional restriction. A fixed port i=x or i=y is used for
each contact statement. No restriction to ready eta or clean q,r is made.

The inherited endpoint form is q_i -> q_i+3 chi(h), with every other
coordinate fixed, chi(0)=1 and the independent bits chi(1),chi(2).
Their ordered pair is the profile 00, 01, 10 or 11. Profile 00 is known
in advance and is not selected by a numerical fit in this task.

## 3. Questions and distinctions to preserve

1. Characterize all W giving chi(k)=0 on a nonzero sign pair. Derive
   exact consequences of passive bit access, one-way coupling and a
   source description that identifies h with -h. In the QDD comparison,
   the two table decisions a,beta must factor through
   (D_P(p_x),D_P(p_y),eta), where the complete individual record obeys
   D_P(p)=D_P(p') iff p'=+p or -p. No broader reading class is excluded.
2. For arbitrary fixed pre/post words whose factor maps are independent
   of q, determine whether a factor-only read can distinguish identity
   from K. Separate this class from the state-selected autonomous U,
   whose selector reads q. No new preparation, borrowed register,
   external label access, reset or event semantics is introduced.
3. Compare the consequences of explicitly stated constraints on W,
   E_W and K. The scaling comparison S_lambda multiplies BOTH piston
   matrices on the RIGHT by diag(lambda,1), fixing q,r,eta. This is a
   mathematical carrier map, not an admitted native or physical symmetry.
   Nonconstancy concerns the response function chi, not the complete
   permutation K. Examine h-preservation at each of the three boundaries.
4. With W_a and every other v100 compiler letter held fixed, determine
   the full factor group when W_b is replaced by any involutive profile-00
   W. Distinguish a shared E/K, shared complete A1--A18 macro maps,
   permutation-group equality, and equality of the already frozen
   syntax-defined T_alg and its q lift. Give explicit prefix witnesses.
5. Identify which premises have not been independently admitted. A
   conditional selector, restricted obstruction, mathematical alternative
   or missing source is not a physical positive/negative closure.

## 4. Evidence and review

Initial analytical reconnaissance preceded this contract and the issue
reservation. It already suggested bidirectional orientation transfer,
sign-blind restrictions, a conditional symmetry selector, and different
permutation parity inside profile 00. This is disclosed known analysis,
not blind preregistered discovery.

No new scientific computation is planned: no enumeration, simulation,
verifier execution, EXPECTED.txt, RUN.md or new candidate-C claim.
Written arguments, including exact counts derived in the proof, provide
the proposed evidence. Repository/source hash, syntax, diff and policy
checks are engineering checks only. A separately required computational
question would need a new frozen scope and code before execution.

Review must check the complete carrier, zero and fixed-point branches,
all occupied bits, source status, scope of each extra premise, and the
changed-generator primitivity/parity argument. Review participation is
recorded: an author of a component cannot be described as an external or
previously uninvolved reviewer of that component.

## 5. Disposition limits

The maximum disposition is a reviewed NON-CANONICAL candidate-T result
at L1. The logical order remains: independent class/interface admission;
selection of a contact law in that admitted class; and separate conditions
on uses of W itself. Nothing here derives C, W_a, the physical admission
of a table class, Ucal, one-time preparation, autonomy, apparatus events,
probabilities, time, energy, scale or a cross-layer lift.

QUADRATIC-MEMORY-NATIVE-CONTACT remains O. Canon, registry, frontier,
gates, sealed probes, workflows and releases are outside this write scope.
The other owners and their outstanding proof/probe records are not closed
or taken over by this note.

[issue]: https://github.com/mathorn1973/twist-j/issues/1398
[canon]: https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/canon/CANON.md
[classification]: https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/notes/C-CONTACT-INTERFACE-CLASSIFICATION-N/PROOF.md
[spec]: https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/probes/P-ALG-CONTACT-REALIZATION-1/SPEC.md
