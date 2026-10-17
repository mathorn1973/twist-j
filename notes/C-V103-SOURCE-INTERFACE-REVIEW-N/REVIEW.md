# RD disposition: changes required, with scoped agreements retained

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Reviewer: `Codex-v103-RD-20261016`, public claim #1560.

**Disposition: CHANGES REQUIRED** for author result
`e3d35709a86b42c21c1bf57e2be2b3a3cf707598` / PR #1558.
The exact gate-overlap counts and scoped source-blindness theorem survive;
the complete package does not receive an unqualified acceptance.
No Canon promotion or merge is recommended by this review.

## Independence and comparison boundary

The independent analytical derivation was committed, pushed and read back
as `2c9718dbb9661eebdfaf150affb5a3e25eda20fa` before author-result
exposure. Public receipt:
[#1560 comment 6225129123](https://github.com/mathorn1973/twist-j/issues/1560#issuecomment-6225129123).
Its PROOF SHA-256 is
`0d7154a50d6cd5220b606290822b7e2205f71b44b6f3a0135cf98d7e293dfb80`.
That proof and its PREREG/SOURCES remain unchanged.

Only after the receipt were the author's PROOF, RESULT, INTERFACE and
promotion text opened at the result commit above. The author's five
specification files remain byte-identical to
`9cb2b7d89eb1fc955fb67e886e46a379cb1aba43`, which is the result's sole
parent. The author change contains only its nine named note files. The
author's required x86_64, aarch64 and aggregate checks passed in run
38967405852. Those checks do not prove the analytical claims.

The comparison-specific counterproofs below, notably the three-step
preimage count, were written after author-result exposure. They are not
misrepresented as part of the earlier independent proof pin. No numerical
enumeration or scientific program was run at either stage. Same-session
helpers assisted; they are not additional independent reviewers.

All author line references below are to the exact result commit, except
the CONTRACT reference, whose bytes are unchanged from the specification.

## R1. The next-scope preimage has 625 points, not 250

**Blocking.** Author PROOF lines 242–244, RESULT line 33 and
INTERFACE.json line 100 assert that

    P_gate=(T1 o T1 o T0)^-1(G0 intersection X14)

is a 250-point set. This is false; 250 counts the target's two trace
sheets, not its three-step inverse image.

Use the literal trace maps, without computation:

| Initial trace | After T0 | After T1 | After T1 |
|---|---|---|---|
| 0 | 0 | 2 | 1 |
| 1 | 4 | 1 | 1 |
| 2 | 0 | 2 | 1 |
| 3 | 4 | 1 | 1 |
| 4 | 4 | 1 | 1 |

On each fixed initial trace sheet the selected word is a fixed composition
of three affine bijections. It is therefore a bijection from that entire
3125-point sheet onto the entire final z=1 sheet. Thus the full three-step
map is exactly five-to-one onto X1; no endpoint with z=4 is reached.

In G0 intersection X1 there are 25 allowed piston quadruples, five choices
of q and one determined r, hence 125 states. Each has exactly one
preimage on each of five initial trace sheets. Consequently

    |P_gate|=5*125=625.

Replace the false cardinality wherever the successor description repeats
it, and distinguish the 250-point target, its 125-point reachable half
at n=3, and the 625-point preimage. Do not run a successor on an assumed
250-point domain. This review does not execute the proposed subsequent
fixed-receiver/sign-fibre classification.

## R2. Alternative-family prefix tuples are not the native trajectory

**Blocking.** Author PROOF lines 119–120 give incorrect A, B, D at n=1
and incorrect q,r at n=3. Direct substitution into the frozen generators,
as independently pinned in PROOF section 3, gives the correct affine
tuples in order (z,A,B,C,D,q,r):

    n=1: (0,4-mu,2,3,1+4lambda+mu,
          2+2lambda+4mu,2+3lambda+2mu),
    n=3: (1,-mu,0,2,0,
          3+2lambda+4mu,3+3lambda+2mu).

For example at lambda=mu=0 the actual n=1 tuple is
(0,4,2,3,1,2,2), whereas the author prints (0,0,4,3,2,2,2).
The printed tuple even violates its own trace constraint:
A+B+q+r=3 rather than the declared z=0.

These are errors in the claimed exact prefix, not a difference of
coordinate convention. The separately derived h formulas at author
lines 148–151 are correct. Accordingly the unique alternative gate point
and no-tail-gate result survive, while the full displayed trajectory
does not. Correct the derived table additively and retain the failed
original statement in the review history.

## R3. The displayed conjugated field operator is incorrect

**Blocking exact-operator correction.** Author PROOF line 190 prints
the wrong top-right block for W A_f W. Swapping the stated rows and
columns gives

    W A_f W = [[ 1, 0, 1, 0],
               [ 0, 1, 0, 1],
               [-3, 1,-2, 1],
               [ 1,-2, 1,-1]].

In particular its action on e2 is (1,0,-2,1); the author's displayed
matrix gives (0,1,-2,1). Replace the explicit matrix. The general
conjugation principle, displayed B and L conjugates, and scalar identity
H(Wy)-H(y)=y0^2-y1^2+y0*y2-y1*y3 remain correct. The e0 non-isometry
witness and the distinction between relabeling and fixed-marking action
are accepted at their scopes.

## R4. Keep the piston kernel, shell residues, and protected vector distinct

**Required typing correction.** Author PROOF lines 25 and 234 and RESULT
line 32 use `ker(h)=LZ^4 mod 5` while h was defined on checkpoints or
on the native piston marking. These carriers cannot be identified in
the fixed marking.

Let pi_P be the piston projection and define

    h_P(a,b,c,d)=(b+2a,d+2c),
    K=ker(h_P)={(a,3a,c,3c)},
    G_L={(y0,y1,y2,y3):y0+2y1=y2+2y3=0}.

Then W(K)=G_L and ker(h_P pi_P)=pi_P^-1(K). In general K is not G_L:
(1,3,0,0) is in K but its first shell congruence is 2. The intended
checkpoint-to-shell statement is h(x)=0 iff W pi_P(x) is in G_L.

The same error appears in the integer-field column of author PROOF
line 222: for an integer field vector y, shell membership is equivalent
to y mod 5 in G_L, or h_P(W(y mod 5))=0, not h_P(y mod 5)=0.
For instance y=(0,0,-2,1) belongs to LZ^4 but h_P(y mod 5)=(0,2).

The 25 protected vectors and 13 sign fibres in D4.2 are valid counts.
However a bijection of a protected-vector plane with G_L is not the
actual W-piston map. For example

    x=(4,2,1,3,0,1), x'=(3,4,2,1,0,4)

both have V=(0,0,1,3) and are synchronized zero-gate checkpoints,
but W pi_P(x)=(2,4,3,1) differs from W pi_P(x')=(4,3,1,2).
Literal W acting on the vector V itself gives yet another typed input;
it must not replace W acting on pistons without an explicit definition.
State the actual maps and their context rather than equating sets because
both contain 25 elements.

## R5. The one-shot summary is false at the initial boundary

**Required exact-scope correction.** Author RESULT line 23 and PROOF
line 222 assert h=(+/-lambda,-/+lambda) for all n>=0. At n=0,
the literal preparation instead gives (2lambda,-2lambda), as the
author's own PROOF line 132 correctly records. For lambda=1 the value
(2,3) is neither (1,4) nor (4,1).

Restrict the sign-only formula to n>=1 and retain the separate n=0
formula. The gate equivalence h=0 iff lambda=0 and the 20/100
ready-carrier count are unaffected and accepted.

## R6. Record the refuted frozen clause instead of reporting no failures

**Required disposition correction.** CONTRACT line 107 froze
`h_1=B+2A`. The independent proof's E(0,0) witness gives h1=1
and B+2A=2. Author PROOF line 40 derives the correct sum identity
but does not acknowledge the failed literal clause. RESULT line 37
nevertheless says no falsifier fired.

Record that literal clause as refuted, with the sum identity and its
separately retained obstruction. Also record the exact derived errors
R1–R5 rather than retaining a blanket assertion that all equations pass.
The principal exposed hypotheses in #1548 do survive at their stated
scopes, but that does not make every equation in the frozen contract or
the delivered proof true. Preserve the specification pin; provide an
additive erratum and reviewed descendant rather than rewriting it.

## R7. Restore the fixed-context hypotheses in the summary table

**Required scope qualification.** In author PROOF line 223, the claimed
five message classes in h are fixed-common-time statements, not stationary
decoding statements on the whole X14 support. On the one-shot ready graph,
(B,z,lambda)=(2,1,1) and (3,1,4) both give h=(1,4). On the alternative
tail, (C,z,mu)=(2,1,1) and (2,4,4) both give h=(1,2). Add the common
time/context qualifier; the correctly scoped D2 conclusions survive.

Author PROOF line 225 also summarizes contact equality as following from
common (q0,r0) and Y0. Outside an explicit restriction to the original
family, that omits common initial z (or the actual premise of identical
source histories), and the common schedule. The occupied and absence
one-shot inputs have the same initial q,r but different q,r at n=2.
For a common blank receiver, direction +1, full store and B=1, their
n=2 sources eta=(1/2,1/2,0,0) and (0,1/2,0,0) have costs 3/20 and
1/10; both contacts accept and write different waves. Thus common q0,r0
alone is not a valid general sufficient condition. Preserve the explicit
hypotheses of D3.1 in every summary.

## Scoped agreement and boundaries

| Question | Review disposition at the unchanged definitions |
|---|---|
| Original 550-point gate overlap | ACCEPT: no gate point; the necessary sum is always nonzero. |
| Alternative 150-point overlap | ACCEPT: exactly (lambda,mu,n)=(2,0,1), none on its tail; repair the separately false prefix tuples. |
| Registered one-shot/absence overlap | ACCEPT: occupied gate iff lambda=0, 20 of 100 ready states; absence never passes; repair the all-time summary. |
| Original h information | ACCEPT at fixed common time: one linear combination, five fibres of five; 2lambda+mu and lambda+3mu differ by an invertible factor. |
| q,r source composition | ACCEPT under D3.1's common complete receiver and source-independent schedule; occupied one-shot is likewise blind, alternative input is pair-sensitive. |
| W energy distinction | ACCEPT the scalar formula and non-isometry; correct the explicit conjugated matrix and marking equalities. |
| Reset/absence distinctions | ACCEPT the inherited family-specific distinctions; no physical/readiness/absence identification follows from the gate. |
| Q4 proposed successor | CHANGES REQUIRED: preimage has 625 points and only z3=1 is reachable. A new source-access/funding/reading contract remains necessary. |
| Complete author package | CHANGES REQUIRED; not ready for synthesis as an unqualified accepted result. |

The integer raw split and shell results, native preparation/readout
theorems, source encoding and contact law are inherited. The valid new
work is their scoped gate comparison and noninterference composition.
It is not a new implementation or a physical transmitter.

Even after repairing the preimage description, two protected sign fibres
inside a shell gate do not by themselves establish distinct supplied
contact inputs, funding or receiver outputs. A future question must fix
the intended receiver projection rather than treating (b,d,q,r) and
(q,r) as interchangeable, and must separately declare the complete
source-access and contact contract. This review does not execute or
authorize that new study.

## Delivery and validation boundary

The reviewer does not change the author's frozen files. Author repair
belongs in an explicitly identified descendant/additive correction with
the old statements preserved. This independent proof remains pinned;
comparison findings and public receipts are additive.

The review's own ordinary repository checks are administrative. Required
CI must pass on its submitted PR head; this does not turn analytical
agreement into a two-architecture scientific reproduction. The source
author's passing checks did not detect the exact mathematical errors
above. Operational completion of RD is distinct from acceptance of D
and from any Canon promotion.

Local validation: policy, Canon, ledger and gate-contract checks passed;
the changed-path scientific verifier and reproduction checks are not
applicable to this analytical note. All 189 repository unit tests passed
under Python 3.13. An initial run under the host's Python 3.9.6 had one
existing fixture error because that interpreter lacks the `newline`
argument to `Path.write_text`; no repository code was changed to bypass
it. Exact-head CI and remote readback are recorded in the delivery receipt.
