# Frozen specification for the four-chart contact replay

**NON-CANONICAL / L1. Candidate C-CONTACT-FOUR-CHART-RENEWAL-N.**
Reservation: issue #1866. Public authority remains Public Canon v107 at
main 0c33e2b281e39127c269ef5dd7f5b529a62e9e65.

This is a result-exposed publication replay of analytically known formulas,
not a blind discovery preregistration. At the time this specification was
written, the new verifier had not been executed. The inventories below are
fixed acceptance requirements, not a report of an execution.

Publish and read back the exact verifier and this specification before the
first scientific execution. Record that immutable source pin and the file
hashes in the subsequent run record. Preserve the original source and all
actual first-run evidence, including any failure. No range, witness, output
format or threshold may be adapted after observing the run.

## 1. Exact arithmetic and the primitive being replayed

Use four integer coefficients in the basis (1,rho,rho^2,rho^3), with

    rho^5=1, 1+rho+rho^2+rho^3+rho^4=0, rho=j^2.

Ring multiplication is integer cyclic convolution followed by the displayed
cyclotomic reduction. No floating point approximation is admitted. Set

    U_d=1-rho^d, J_d=1+rho^d, d in {1,2,3,4},
    Q(z)=(5*sum_i z_i^2-(sum_i z_i)^2)/2,
    epsilon(z)=sum_i z_i mod 5.

Subscripts are represented in {1,2,3,4} modulo five. The sole native pair
primitive is the total contact C. It leaves a pair unchanged when its
difference is not coefficientwise even. Otherwise, for a=s+t, b=s-t,
it returns (s+rho*t,s-rho*t).

The implementation must actually repeat this primitive for every C^e,
1<=e<=4. A closed powered-contact formula may supply a comparison value;
it must not replace the native primitive execution. Every enabled primitive
checks preservation of its pair sum, Q(a)+Q(b), and both labelled epsilon
residues. A refused primitive performs the literal identity. Pair checks
therefore cover the complete account and sum, because all other slots stay
unchanged. Every powered macro also checks that all its primitive calls
share the same enabled/refused status.

## 2. Fixed four-chart source, words and inverse

The supplied source, gain and initial chart are

    F_(q,d)(n)=(U_d*n, (4q-J_d)*n, 2J_d).

Fix D=12 and append thirteen zero cascade targets, giving sixteen core
slots numbered 0..15. No edge or exponent is selected from an observed
input value, valuation, output or answer.

The fifteen powered macros are, chronologically,

    (0,1,d), (0,2,d),
    (0,2+s,e_s), s=1..13,
    e_s=2^s*d mod 5 in {1,2,3,4}.

Their primitive C counts are fixed:

| Initial chart d | Forward primitive calls |
| ---: | ---: |
| 1 | 34 |
| 2 | 38 |
| 3 | 37 |
| 4 | 41 |

An inverse replay traverses these fifteen macros in reverse order and
replaces exponent e by 5-e. It acts on the actual complete forward output,
including every occupied leftover and archive. The original complete input
must be recovered coefficient for coefficient. Each forward-plus-inverse
case has exactly 75 primitive calls, including refused calls.

For x=qn+1, v=v_2(x), let a=min(v,13). The comparison endpoint is

    active=U_(2^(a+1)*d)*(x/2^a),
    slot1=2(q*J_d-rho^d)*n,
    slot2=q*U_d^2*n+J_d^2,
    slot(2+s)=U_(e_s)^2*(x/2^s), 1<=s<=a,
    slot(2+s)=0, a<s<=13.

The two prefix macros must be enabled. The cascade flags must consist of
a enabled macros followed by 13-a refused macros. Intermediate prefix
checks include first active value 2q*U_d*n and second active value
U_(2d)*(qn+1).

## 3. Reader and strict depth limit

The reader receives the actual state. Its only inspected slots are the
current active port and the thirteen current cascade targets. It must not
read the old source leftovers, original n, original chart, a lookup table,
or a hidden history.

Count the nonzero prefix of cascade targets. If all thirteen are nonzero,
return the depth-limit sentinel, represented by None in verify.py and
reported as DEPTH_LIMIT. This decision precedes active-port oddness or
shape decoding.

Otherwise, all later targets must be zero. The positive gcd of the active
coefficient tuple gives an odd m. Dividing the tuple by m must give exactly
one of U_1,U_2,U_3,U_4. The returned triple is (m,d',v), with

    d'=2^(v+1)*d mod 5.

For each admitted case the caller separately checks

    n=(2^v*m-1)/q, with exact divisibility,
    d=2^(-(v+1))*d' mod 5.

This is a mathematical current-state reader and arithmetic inverse. It is
not a physical normalization gate, a source loader or a native controller.

## 4. Fixed trajectory corpora

These five corpora are evaluated in the order A, B, C, D, E. Overlapping
inputs in different corpora are intentional separate audit cases.

| Corpus | Fixed inputs | Complete forward cases |
| --- | --- | ---: |
| A | q=3; every odd n from 1 through 4095; d=1,2,3,4 | 8192 |
| B | q=1..9; every odd n from 1 through 127; d=1,2,3,4 | 2304 |
| C | q=3; every odd n from 1 through 47; d=1,2,3,4; two fixed occupied old archives | 96 |
| D | q=3; n=5461 and n=13653; d=1,2,3,4 | 8 |
| E | Original E_3 source; every odd n from 1 through 4095 | 2048 |

Total: 12,648 complete forward trajectories and 12,648 complete inverses.
Their combined native-call count is exactly 948,600. Enabled and refused
counts are measured by the actual run and must sum to that total; their
individual values are not guessed in this specification.

### A and B: full core and Galois covariance

Every case checks the complete sixteen-slot endpoint against the explicit
formula, not only its arithmetic answer. A and B must lie within v<=12.
Corpus B includes depth zero when q is even.

Check the source sum and account,

    S(F_(q,d)(n))=2(2q-rho^d)*n+2J_d,
    Q(F_(q,d)(n))=(32q^2-12q+8)*n^2+12.

At q=3, check the three source residues (0,0,4). Check complete endpoint
sum, account and labelled residues against the input.

For each fixed (q,n), retain the d=1 forward trace at all fifteen powered
macro boundaries. For each d=2,3,4, compare the entire sixteen-slot trace
with its exact automorphism image under sigma_d: rho maps to rho^d.
The covariance is checked at corresponding macro boundaries; the primitive
word lengths differ, so the primitive time indices are not identified.

On admitted endpoints check

    Q(active)=5m^2,
    Q(fresh records)=5((qn+1)^2-m^2),
    sum(fresh records)=U_(2d)*(qn+1)-U_(d')*m.

For positive odd q=3 inputs, check the finite-corpus record bound 75 and
its equality condition n=m=1. The 3->5 control has record account 375 and
the strict-ready-plus-literal-record necessary funding expression 4535.

### C: literal occupied old archives

Append exactly two old slots, in order,

    rho, 1+rho^3.

These are the same literal tuples for every n and d. They are disjoint from
all scheduled edges. Their complete values must be unchanged at every
forward macro boundary, at the final endpoint, and after full inversion.
Include their actual accounts and sum in complete-state checks.

Compare Galois covariance only on the sixteen core slots. Applying sigma_d
to the entire eighteen-slot state would also transform these fixed old
archives and would impose a different input contract. Literal archive
retention and core covariance are separate checks.

### D: two distinct saturation controls

For n=5461, x=16384 has valuation 14. For n=13653, x=40960 has valuation 13.
All thirteen targets must be nonzero in all eight cases, and the reader
must return DEPTH_LIMIT.

The valuation-13 witness is essential: its active slot is already odd
after thirteen successful divisions, but it is still outside v<=12 and
must not be accepted. The valuation-14 witness remains even at that cut.

Use the truncated endpoint formula with a=13, complete conservation, the
same macro-boundary core Galois comparisons, and the full native inverse.
These cases are expected boundary witnesses, not successful arithmetic
outputs in the admitted family.

### E: actual original source and original contact word

Use rho-basis u=1-rho and J=1+rho. Prepare

    E_3(n)=(4u*n, 4(2-rho)*n, 2J),

with thirteen zero targets. Execute the two prefix contacts C01,C02 and
the thirteen chronological contacts C_(0,2+s), s=1..13. This is an actual
fifteen-primitive forward word, not a replay of its closed formula. Its
inverse uses four copies of C for every reversed macro, making sixty
inverse calls and seventy-five calls in total per case.

Check every complete endpoint, including

    active=u*J^(v+1)*m,
    slot1=2(3-rho)*n,
    slot2=3u^2*n+J^2,
    record_s=u^2*J^s*2^(v-s)*m, s=1..v,

and zeros after the last successful division. All these cases have
1<=v<=12. Check total source account 272n^2+12, complete conservation,
fresh-record sums and accounts, and exact whole-state restoration.

With c_r defined below, the fresh-record comparison is

    R_E(v,m)=(5*4^v-c_v-c_(v+1))*m^2,
    r_E(v,m)=uJ*(2^v-J^v)*m.

Check R_E>=55 and equality exactly when n=m=1 within this corpus.
At n=1 verify record account 55 and account of the record sum Q(r_E)=85.
These are different quantities. At n=3 verify m=5, record account 250,
and strict-ready-plus-literal-record necessary funding expression 4602.

## 5. Fixed supplementary exact checks

These checks do not add native trajectories or native calls to the totals
above.

1. For all four d, check U_d*J_d=U_(2d), Q(U_d)=5, Q(J_d)=3,
   Q(U_d^2)=15, and the four-factor product of J_(2^r*d), r=0..3,
   equal to the ring unit. Also check
   (u^2J)*conjugate(u^2J)=5, with conjugation rho maps to rho^4.
2. Build c_0=2, c_1=3 and c_(r+2)=3c_(r+1)-c_r. For every r=0..64,
   compare c_r to Q(J^r) computed by exact ring arithmetic.
3. For every v=0..12 and every positive odd m<=31, explicitly form the
   original record list and compare its total account and ring-valued sum
   with R_E and r_E above. This fixed box has 208 (v,m) pairs and includes
   the empty list at v=0.
4. For k=2..64, start from n_0=2^k-1 and perform all k-1 ordinary accelerated
   odd Collatz steps by actually forming 3n+1 and dividing until odd.
   Check valuation one at every step and the formula
   n_i=3^i*2^(k-i)-1, ending at 2*3^(k-1)-1.
   This is 63 fixed prefixes containing 2016 actual integer odd steps.
   It is not a contact execution or a physical reload.

No numerical sampling or finite box substitutes for a universal proof.

## 6. Complete-output fingerprint and scientific stdout

Before inverting each trajectory, append its actual complete forward state
to one deterministic SHA-256 stream. The serialized record is

    [tag, q, n, d, state]

using json.dumps with separators (",", ":"), encoded as ASCII, followed
by one LF byte. Every slot is serialized as its four integer coefficients;
the occupied-archive corpus therefore includes all eighteen slots. The
tags are exactly

    q3, supplied-gain, occupied, depth-limit, original.

Ordering matches the fixed corpus order. Inside A, C and D, n is outermost
and d runs 1..4. B uses increasing q, then increasing odd n, then d=1..4.
D uses n=5461 before n=13653. E uses increasing odd n, q=3 and d=1.
No expected answer, macro trace or omitted leftover is substituted for the
complete actual forward state.

The output fingerprint is determined by the first pinned execution. Its
value and the SHA-256 of complete stdout are not predicted here. Retain the
actual first stdout verbatim after execution and record its byte count,
hash, exit status and stderr disposition. Do not hand-author a successful
EXPECTED file from the known formulas.

All successful scientific output is deterministic and emitted only after
the assertions have completed. It states the fixed inventories, forward
word counts, native-call totals, measured enabled/refused counts,
complete-output fingerprint and scope. Source hashes, platform identity
and execution metadata belong in the separate run record, not in a
nondeterministic scientific transcript.

## 7. Execution restrictions and acceptance

The frozen verifier uses Python standard-library exact integer operations
only. It has no scientific command-line parameters, network access,
external input files, random source or environment-selected bounds.
Run it without optimization so assertions remain active; verify.py
explicitly refuses an optimized invocation.

From the repository root, after public pin/readback, the intended command
has the form

    python3 -I notes/C-CONTACT-FOUR-CHART-RENEWAL-N/verify.py

A completed successful replay requires exit zero, empty stderr, every
fixed assertion, the complete inventory and actual deterministic stdout.
An interruption is incomplete, not PASS. Preserve a failed first result;
do not conceal it by expanding, narrowing or repairing the frozen audit.
Any correction requires an explicit later disposition preserving the
original pin and evidence.

## 8. Proof-only statements and exact limits

The accompanying proofs address arbitrary admitted inputs, literal-archive
resource horizons, the higher-ideal residue filtration, the finite affine
loader obstruction, and necessary sum/account/reachability conditions.
Those infinite statements remain proof claims. This finite replay audits
the displayed identities and explicit controls; it does not establish an
all-input or infinite-time result by enumeration.

In particular:

- The active port returns to one of four ready code shapes. The other
  source ports have not been renewed.
- Four supplied chart-indexed words and a reader do not construct an
  autonomous chart selector.
- Galois covariance does not supply a physical Galois operation.
- A necessary funding inequality is not a reachable reset or an attainable
  minimum.
- Original-source and four-chart executions are separate one-pass audits.
  No sequence of them is described as an executed physical reload.
- The depth cap is fixed at twelve. Saturated outputs remain outside its
  positive arithmetic contract.
- No gain-selection principle, native-U realization, physical energy/time
  calibration, occurrence law, indefinite archive renewal, Collatz
  convergence, Canon promotion or two-architecture scientific replay is
  claimed by this specification.
