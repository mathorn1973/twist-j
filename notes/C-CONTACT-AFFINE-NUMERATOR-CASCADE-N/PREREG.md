# Direct contact affine numerator and bounded division cascade

Status: NON-CANONICAL / L1. Candidate C-CONTACT-AFFINE-NUMERATOR-CASCADE-N.
Owner: Codex session /root. Public main base
0c33e2b281e39127c269ef5dd7f5b529a62e9e65, Public Canon v107.
This is a new incubation contract, not a resumption of the finite table
compiler C-COLLATZ-CONTACT-STEP-RECORD-N or a formal Canon probe.

## Frozen equation, carrier and loading interface

O=Z[j], 1+j+j^2+j^3+j^4=0, rho=j^2, J=1+rho, u=1-rho.
The total integral contact C(a,b) refuses when a-b is not in 2O;
otherwise s=(a+b)/2, t=(a-b)/2, and C(a,b)=(s+rho*t,s-rho*t).
Q(z)=(5*sum(z_i^2)-(sum(z_i))^2)/2 in the j basis.

The declared source encoding, with supplied positive integer gain q, is

 E_q(n)=(2(q-1)u*n, 2((q-1)u+2)*n, 2J), n>0.

Only the first two slots depend on n. This is a fixed coherent linear
encoding, not an input-dependent auxiliary reference or an encoded answer.
It is an explicit premise, not proved reachable from one raw integer slot,
not a consequence of J selecting q=3, and not a free source preparation.
The reference 2J and all zero slots are common across n and q.
No input slot contains qn+1, its odd part or its valuation at initialization.

Use D=12. Core slots 0,1,2 contain E_q(n). Slots 3..15 are 13 fresh zeros.
Thus there are 16 core slots. Optional occupied archives occupy 16 and 17;
they are counted but never touched by this word. The 16-slot input account is

 Q_total=[40q(q-1)+32]*n^2+12,
 S_total=4[q-(q-1)rho]*n+2J.

For q=3 the account is 272n^2+12. It varies with source input. No comparison
with the earlier constant-account binary code is an energy-identification.

## One literal word and complete expected current state

Chronological word W_D:

 C(0,1), C(0,2), C(0,3), C(0,4), ..., C(0,15).

Length D+3=15. Edge choices and length never depend on the input.
The first two contacts are always admitted and must give

 after C01:
  slot0=2q*u*n,
  slot1=2[q-(q-2)rho]*n;
 after C02:
  slot0=u*J*(qn+1),
  slot2=q*u^2*n+J^2.

Let v=v2(qn+1), m=(qn+1)/2^v. On the positive depth contract v<=D,
the final active slot and cascade slots must be exactly

 slot0=u*J^(v+1)*m;
 slot(2+s)=u^2*J^s*(qn+1)/2^s  for 1<=s<=v;
 slot(2+s)=0 for v<s<=D+1.

Slot1 and slot2 retain the displayed source/reference leftovers. No reset
of these slots is claimed. The first v cascade contacts are admitted and
the remaining D+1-v are refused. Every first-v stored value is nonzero.
All optional prior archive values remain identical in their labelled slots.

## Reader and inverse

Read only the current active slot and the current 13 cascade slots.
Find the nonzero prefix of the cascade. If all D+1 slots are nonzero,
return DEPTH_LIMIT rather than an arithmetic pair. Otherwise its length is
the depth v, and all remaining slots must be zero. Compute

 r=J^(-(v+1))*slot0,
 J^(-1)=-rho-rho^3.

Require r=(m,0,-m,0) in the j basis, then read its constant coefficient m.
This is an integer unit normalization followed by one fixed coefficient
reading. No division by the nonunit u, original n, source leftovers, free
counter or target table is allowed in the reader. Invert the arithmetic
pair by n=(2^v*m-1)/q; exact divisibility must hold. The full-state inverse
uses reversed edges and four contacts per reversed edge.

## Frozen finite audit

1. q=3, every odd n=1,3,...,4095 (2048 cases), D=12. Every case must fit
   the positive contract, match all full-state formulas, recover n, and
   return exactly under the complete primitive inverse. Every depth 1..12
   must occur in this corpus.
2. General supplied-gain audit: q=1..9 and every odd n=1..127 (576 cases).
   This includes even q, whose qn+1 is odd and whose depth is zero. All
   cases must match the same formulas and literal word, with full inverse.
3. Occupied-archive audit: q=3, n in {1,3,5,7,15,27,85,1365,4095}, and
   all 25 ordered pairs from the prior-value set {0,1,j,u,J}. Append two
   archived slots, run the identical core word, match full core state,
   preserve both archives and their complete accounts, then invert.
4. Fixed outside-depth witness q=3,n=5461 has qn+1=2^14, beyond D.
   All 13 cascade slots must be nonzero, the active slot remains even,
   reader must return DEPTH_LIMIT, and full-state conservation and inverse
   must still hold. This expected saturation is outside the positive
   arithmetic claim and must not be silently reclassified as a success.
5. For every distinct ordered primitive pair used: sum, Q, both labelled
   coefficient-sum residues modulo five, C^5=id and complete inverse.

No floating point. Exact integers and exact cyclotomic tuples only. Report
actual stdout, exit code, empty stderr, Python/platform/architecture, frozen
source hashes, edge word hash, counts, and SHA-256 of all q=3 current states
in canonical j basis. Canonical boundary fingerprint is compact JSON
[[n,state],...] in increasing odd n order, with no final newline, where
state is a list of 16 four-integer slot tuples. Edge hash is ASCII i,j\n
for each of the 15 chronological edges, including final newline.

## Falsifiers, independence and status

Any wrong synthesis formula, residue/account/sum change, wrong active or
archive port, reader using the source or original n, positive-corpus depth
overflow, failure of inverse, changed occupied archive, differing input-
dependent edge word or failure to flag the outside-depth witness fires the
candidate as stated. A scientific exception or timeout is not a pass.
Frozen source and thresholds are not repaired after execution; any repaired
candidate needs a new identifier and pin.

The accepted verify.py and this contract are publicly committed and read
back before first scientific execution. The independent breaker is written
from this contract without reading verify.py, frozen and publicly pinned
before its own execution/comparison. Its internal basis and algebra must
be independent of the author's j-basis implementation. An independent
symbolic proof must not import the runtime result as a premise.

The synthesis was discovered symbolically before this contract; the audit
tests its stated consequences, not a blind discovery of 3n+1. Both runtime
lanes here are x86_64. They do not satisfy the public two-architecture
scientific gate. Ordinary repository CI does not replay notes/ science.

Positive mathematical scope is the declared coherent source E_q(n), supplied
q, common reference, finite D and v2(qn+1)<=D. Source loading, physical
admission and choice of q=3 remain premises. The output is not E_q(m),
and all source/reference leftovers and archives remain occupied. No repeated
autonomous Collatz step, renewed source, native-U derivation, measured
energy/time, occurrence, global convergence or Canon promotion is claimed.
