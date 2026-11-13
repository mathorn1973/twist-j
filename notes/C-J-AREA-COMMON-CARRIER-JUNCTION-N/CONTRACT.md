# Conditional typed contract for a common actual history

PUBLIC / NON-CANONICAL / L1. C-J-AREA-COMMON-CARRIER-JUNCTION-N.
A. M. Thorn; Apache-2.0. This document grants no native admission.
Sources and exact versions are in SOURCES.tsv. Source claims under review
are definitions/prospective premises here, not adopted theorems.

## 1. Distinct input types

| Object | Complete mathematical type and law | Permission |
|---|---|---|
| Native forward state | Omega_N=N_0 x F5^6, x=(a,b,c,d,q_N,r_N), U(n,x)=(n+1,g_(sum(x)+2 theta_n mod5)x) | Public declared architecture |
| Native letters | g_0,...,g_4:F5^6->F5^6; literal affine involutions below | Defined maps; free word order is not automatically a U history |
| Area pair | V_A=O^2, O=Z[j]; T_A(alpha,beta)=(J alpha,phi beta) | #1583 selected marked algebraic action |
| Alternating evaluation | omega:V_A x V_A->O; omega((a,b),(c,d))=ad-bc | Two vectors, not one point or an integer path |
| Ramified labels | E_A=F5^2; rho(sum a_k j^k)=sum a_k mod5, componentwise | Algebraic quotient; rho(j)=1 |
| Weyl module | M_W=Q(j)^5; X e_k=e_(k+1), Z e_k=j^k e_k | Chosen linear representation; not a native register or physical effect |
| Funded comparison | S_B=Z^4 x N_0 x {+1,-1}^2 x C4, coordinates (q_B,p_B,u,v,b_B,sigma,eta,c) | #1585 declared extension; not Omega_N |

The abstract Q(j) module records exactly the same monomial algebra as the
chosen complex representation, with a fixed marked j. No physical inner
product, preparation of a ray, interference measurement or Born law is
introduced by using this exact coefficient field.

All native coordinates in the following formulas are in F5:

```
g0(a,b,c,d,q,r) = (b,a,d,c,q,r)
g1(a,b,c,d,q,r) = (-c,-d,-a,-b,-q,-r)
g2(a,b,c,d,q,r) = (2-c,1-d+r,2-a,1-b-r,1-q,-r)
g3(a,b,c,d,q,r) = (2-a,1-b,3-c,4-d,1-q,1-r)
g4(a,b,c,d,q,r) = (2-a,1-b,3-c,4-d,2-q,1-r)
theta_n = popcount(n) mod2.
```

The native n is internal to U. It is not a freely provided B controller
phase or an inverse-time coordinate. No integer energy bank or O^2 pair is
among these six residues. A proposed reading of them requires a named map.

## 2. Declared comparison definitions, not native permissions

On the integer quadruple let

```
Q_h(q,p,u,v) = (q+h,p,u,v)
P_h(q,p,u,v) = (q,p+h,u+h*q,v+h*q)
H_int = q^2+p^2+u^2+v^2, E_B = H_int+b_B.
```

H_int is the integer comparison cost; it is unrelated to the rational
funded contact called H_B in #1498. Q/P have h in {+1,-1}.
For request (axis,epsilon),
h=epsilon*sigma. Form the candidate y; Delta=H_int(y)-H_int(x).
If b_B>=Delta, accept y and b_B-Delta, keeping sigma. Otherwise keep the
integer quadruple and bank and flip sigma. The full step U_* makes the
request (Q,+),(P,eta),(Q,-),(P,-eta) at c=0,1,2,3, then advances c mod4.
Eta is retained. These are the definitions to which an implementation must
be compared, including the rejection branch. No numerical source result
is needed to state them.

The source advertises initial states (0,0,1,-1,B,+1,eta,0), ordered
reference reader R_sq=(u^2,v^2), and A_ref=(u^2-v^2)/4 on that prepared
family. On a general occupied state A_ref is merely a rational number;
the interpretation as newly accumulated path area is NOT part of its type.

Native permissions and missing resources are separate:

| Operation/resource | Existing authority | N's disposition |
|---|---|---|
| Selector-defined U and finite checkpoint generators | Public Canon definitions | May be cited on their actual domains |
| Fixed freely ordered g_i word | Public mathematical word operation | Must supply its scheduler to call it an actual autonomous run |
| CONTACT-RECORD with W_b and Ucal | Conditional public theorem on its declared extended carrier | Admission remains with #1398/#1578; no compilation here |
| INTEGER-ENERGY-FUNDED-INVOLUTION | Public theorem conditional on chosen reaction, cost and bank | Does not select the reaction, cost or native bank |
| Integer Q/P, bank/guard, reference pair, sigma/eta/c | Supplied by #1585 as a comparison | DECLARED-EXTENDED, never native by definition |
| T_A, rho, chosen X/Z/D, additive character | Algebraic definitions in #1583/public Weyl theorem | REPRESENTATION, never a paid contact by itself |
| Native-to-integer/O^2 loading and reciprocal state updates | UNSUPPLIED for this joint task | Must be supplied with domains, inverse, cost and owner permission |
| Physical phase/energy/time/readout | No joint realization gate supplied | Outside this L1 contract |

## 3. Required common implementation certificate

This is a specification with unfilled fields, not a purported nonempty
admissible class. An implementation must give a set S, literal equality,
and a complete state inventory. It can use shared rather than duplicated
coordinates, but must exhibit total projections on the asserted domain:

```
pi_N:S -> N_adm subset Omega_N
pi_B:S -> B_adm subset S_B
pi_A:S -> A_adm subset V_A x V_A       (if both area vectors are claimed)
pi_R:S -> R_adm                       (ordered current receiver record)
```

N_adm, B_adm, A_adm, R_adm, S and the joint compatibility relation are
UNSUPPLIED. Two vectors are required for an alternating evaluation; a
scheme using only one must state where the second/reference vector comes
from. S is not declared to equal the ambient product. Unused copied
coordinates do not establish coupling or preservation of a common history.

The certificate must additionally fix, before target comparison:

1. A nonempty common source domain D_src and an input encoding. One complete
   receiver/reference/controller preparation r_ready is independent of the
   source label and the desired output. Each variable that differs between
   preparations is assigned explicitly to source or apparatus. The loading
   map, donor state, its inverse/image and resource transfer are part of S.
2. One total permitted transition F:S->S with its exact inverse and domain.
   If only an image inverse or forward simulation is available, say so;
   it does not satisfy a claim of a global permutation. Give the complete
   generator permission table and every guard, including occupied states.
3. One common microstep index and a frozen correspondence to native steps,
   B steps and algebraic operations. A finite macro may expand into several
   native steps, but its intermediate states, exact step count, program and
   inverse are included. Any stuttering or blocking is declared in advance,
   not chosen from the resulting phase. At corresponding cuts prove the
   relevant commuting diagrams, e.g. pi_B F_word=U_* pi_B. A native claim
   must specify whether the other side is actual U or a freely chosen g_i
   word. No T_A=U or n=c identification is implicit.
4. An integer nonnegative total E_tot:S->N_0 with E_tot F=E_tot, and an
   explicit decomposition for system, reference, bank, preparation donor,
   controller and any archive. Zero assigned cost for a finite controller
   is a declared model choice; its state count is still a resource. An
   unbounded counter/archive with zero cost prevents an inference of finite
   energy-shell cardinality unless a separate proof establishes it.
5. A fixed present reader r:R_adm->Out, with literal ordered output equality.
   It cannot consult source labels, discarded preparation, eta, desired
   sign, a nominal word or an external history unless those ports are
   explicitly in the declared receiver and fully accounted for. A cold
   reader and an occupied continuation may have different stated domains;
   there is no implicit universal reset.
6. A target-independent selection rule and proof of completeness for the
   asserted admissible class. Multiple readings are permitted; the task
   does not demand global decoder uniqueness. Their allowed equivalences,
   contexts and overlapping outputs must nevertheless be fixed.

For every supported source and every actual prefix, all the projections
must be evaluated on the same s_i=F^i(s_0), rather than on separately
prepared runs. A mathematical history (s_0,...,s_m) is not automatically
stored memory. If a reader accesses that history, a material archive and
its updating, occupancy, costs and inverse must be supplied separately.

## 4. Actual-path Weyl typing

For the B projection, let dq_i=q_(i+1)-q_i and dp_i=p_(i+1)-p_i in Z.
Each microstep must declare its actual operator, independently of any area
reader: Q displacement gives X^dq_i, P displacement gives Z^dp_i, and a
refused displacement gives I. If a macro changes both, expand its actual
order; endpoints alone do not define its central phase.

With chronological left multiplication, W_0=I and
W_(i+1)=L_i W_i in GL_5(Q(j)). Equality here is literal operator equality,
not equality up to a scalar phase. A claim only modulo scalars has a
different and strictly weaker output type.

The label used by #1583 is W(a,b)=Z^a X^b. Thus the compatible candidate
edge-label map for these particular B axes is

```
ell_B(dq,dp) = (dp mod5,dq mod5) in E_A.
```

This is a typed label comparison, not an embedding of complete B states or
a native transition. The label map has an infinite kernel. One can also
name the purely arithmetic map iota_Z(p,q)=(p*1_O,q*1_O) into O^2;
rho iota_Z is the residue label map on integer coordinates. No intertwining
of iota_Z with T_A and any B step is assumed. A future use must prove it
on the exact claimed invariant domain.

The auxiliary functional A_path=sum q_i dp_i is calculated on actual
transitions and starts with the explicitly chosen origin. The assertion
that r equals this value, and that an integer-closed word is j^A_path I,
is a proof obligation, not the definition of W. Reduction rho(j)=1 and
the selected character chi:F5->mu5, t->j^t, have different domains and
are never composed as a recovery of the erased algebraic j.

## 5. Frozen admission tests

| Test | Required check | Failure disposition |
|---|---|---|
| Preparation | Same complete r_ready; source-independent preparation; reference/donor cost and inverse | Missing law: STOP; exact false equality refutes that proposal |
| Occupied memory | All admitted u,v/auxiliary states; stored baseline if needed; no overwrite | Restrict reader scope or STOP; no hidden reset |
| Underfunding | b=0 and general failed guard; actual operator I for no displacement | Nominal-word phase is not the executed phase |
| Fivefold | Compare character, current record, bank, clock and whole state separately | Character return cannot stand for full reset |
| Program | Account for eta/sigma/c and actual native n; common versus source-loaded controller | Different program is not common complete preparation |
| Inverse | Global bijection versus image inverse; original selected U versus individual g_i | Missing lift/domain: STOP |
| Area/frame | Two O^2 vectors versus integer polygon; explicit axis/order maps and schedule | Untyped identification: STOP |
| Funding class | All retained resources and independently supplied integer E_tot | Algebraic covariance alone supplies no funding law |

Complete native class: UNSUPPLIED. Complete native comparison inverse:
UNSUPPLIED. Source-independent native loading into the B or O^2 types:
UNSUPPLIED. Common admitted cost/selector: UNSUPPLIED. These are empty
certificate slots, not a proof that the associated mathematical sets are
empty. R1/R2 success would validate source statements at their own scopes;
it would not fill these slots.

## 6. Exports and exclusions

This contract exports exact type/equality/commutation/resource obligations
and the frozen tests above. It supplies no new generator, implementation,
physical apparatus, source-preparation law or all-reachable-state certificate.
No H_B compiler, W_b construction, field-chain obstruction or funded b-lift
is taken from its existing owner. A typed derived history is L1 here, not
automatically an L5 observed stream. No frequency, SI action, hbar,
stationary-action law, physical phase observation or occurrence claim follows.
