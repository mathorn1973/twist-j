# Independent review of the fixed receiver, root clock and stock census

Status: NON-CANONICAL / L1. Candidate C-FIXED-RECEIVER-SELECTION-REVIEW-N.
Owner: Claude Code session on branch `claude/affectionate-pasteur-35hovw`,
2026-11-07. Review lock: issue #1935.

Authority base: `main` d4d363722f052141a4ce65e9da39f11a74b43b95, ACTIVE
Public Canon v109 (tag `canon-v109` at
650029c20408f1dd665983d72225d0d195fd030e; `canon/CANON.md` SHA-256
035408ec79219cc72a7d3613cf1568154cca185137d2a2daa43b896aae0c6383,
1464066 bytes).

Target: PR #1930, head 3d8d364cb981bb5d53bbede432fb5a4ac4181709, directory
`notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N`. The target has two
source pins:

- receiver source pin 262fa528968145ec8f501c8193aab946896997f6;
- stock source pin 4d9fa863852c6054a5f10ac8e32e8b3ca642d548.

TARGET-SHA256SUMS binds the 19 target files of this review at the head.
The receiver and stock source files there are byte-identical to their pins.

## 1. Scope

The review covers the fixed-receiver continuation only:
RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md, RECEIVER-OBSTRUCTION.md,
RECEIVER-RESULT.md, STOCK-BOUND.md, STOCK-RESULT.md and REVIEW-RESPONSE.md.
These seven review scopes are judged:

- **S1 Operational distinction.** Five names attached to one unchanged
  state give one receiver history. Actual re-encodings are different
  physical preparations.
- **S2 Fixed receiver.** The stock R=3+4j+2j^2, its response, active
  backreaction, literal inverse and accounts.
- **S3 Root clock.** The V_m words, their conservation, V_m^5=jI, the least
  period 25, the padded calendar and the minimum neutral account.
- **S4 Relative phase.** Unit covariance, the q_n(m,X) identities, the D_m
  conjugacy and the relational conclusion.
- **S5 Linear obstruction over K=Q(j).** Irreducibility, the
  twenty-element basis, nonzero projection on every mode, the commutant
  field, no nontrivial projectors, and dimension a multiple of five.
- **S6 Positive H_m family.** Positivity, eigenvalues, the ground mode
  t=-m, equal support and holonomy against unequal coefficients,
  dependence on the embedding, and no cooling under unitary evolution.
- **S7 Stock census.** The minimum 22 for the fixed word and readout, the
  completeness bound (B1), the witnesses T and S, the rotation rule (B4),
  and why minimizing Q alone selects no frame.

Out of scope:

- PROOF.md, FULL-FIELD-PHASE.md, verify.py and verify_fullfield.py;
- the reduced and full-field results of the same directory;
- any physical interpretation: phase, Born rule, alpha, calorimetry or
  physical duration.

## 2. Exposure and provenance

This record cannot be backdated. It is stated here before the new checker
exists.

1. **The target results are public.** The coordinator of this review (this
   session) has read every target Markdown file in scope, including both
   target preregistrations, RECEIVER-EXPECTED.txt, STOCK-EXPECTED.txt and
   RECEIVER-RUN.md. This review is not blind to any result.
2. **An informal check came first.** Before this file existed, the
   coordinator wrote INFORMAL/check_receiver_indep.py and
   INFORMAL/stock_scan.py and ran each once, without a pin. It reported the
   results to the owner. The owner then built three of them into the
   target at 4d9fa86 and 3d8d364:
   - the stock-22 hypothesis and the counts 40/40/40;
   - the relative-phase identity;
   - the twenty-element basis argument.

   The owner also adopted wording corrections. The origin of those
   hypotheses is therefore not independent of this reviewer. This review is
   independent of the target's code, not of the hypotheses' origin.
   INFORMAL/PROVENANCE.md gives the executed bytes, their hashes, the
   transcribed stdout and seven known weaknesses.
3. **One informal replay of a target verifier.** The coordinator replayed
   the target verify_receiver.py (SHA-256
   39aa493ee1a21e9a94d7decad3b20ad8a6f4311dcb87ea33a96169688dfb916f)
   once, informally. Its stdout was byte-identical to RECEIVER-EXPECTED.txt.
   The coordinator saw only that verifier's import lines, never its body.
   It has neither read nor run verify_stock_census.py.

## 3. Source boundary for the new checker

`review.py` is written in a separate, fresh agent context. Its writer may
read only:

- this file;
- these target files at the head, read with
  `git show 3d8d364cb981bb5d53bbede432fb5a4ac4181709:PATH`:
  RECEIVER-CONTACT.md, RECEIVER-DYNAMICS.md, RECEIVER-OBSTRUCTION.md,
  STOCK-BOUND.md and REVIEW-RESPONSE.md;
- the section of `canon/CANON.md` that defines O, q and the total contact
  (RELATIVE-CONTACT-INTEGRAL-LAW and its preamble).

The writer must not read:

- any target `*.py`, `*PREREG*`, `*EXPECTED*`, `*RUN*`, `*RUNS.json`,
  `*RESULT*`, `*SHA256SUMS` or `SOURCE*` file, PROOF.md or FULL-FIELD*;
- anything in INFORMAL/;
- the coordinator's scratch files;
- any PR, issue or CI text.

Before the pin, the writer may only compile the checker for syntax
(`python3 -m py_compile` or `ast.parse`) and inspect it statically. No
scientific check is run, and no part of the checker is executed.

Two further readers, each in its own fresh context, inspect the checker
statically for conformance to this file. They do not execute it. The
coordinator's own inspection is limited to the same question. RUN.md
records every change requested as a result.

The pin commit carries PREREG.md, review.py, the pre-run
MATHEMATICAL-REVIEW.md and a SHA256SUMS manifest. That commit is pushed and
read back byte for byte from GitHub before the first execution.

## 4. Arithmetic conventions for review.py

- **Ring.** O=Z[j] in the basis (1,j,j^2,j^3), with
  j^4=-1-j-j^2-j^3. Multiplication is cyclic five-coefficient convolution
  modulo j^5=1, then reduction.
- **Account.** Q is computed two ways, and the two must agree on every
  element the checker evaluates:
  - the closed form (5 sum c_i^2 - (sum c_i)^2)/2;
  - Tr(a abar)/2, using Tr(j^r)=4 if 5 divides r and -1 otherwise.
- **Contact.** C as in RELATIVE-CONTACT-INTEGRAL-LAW. A pair is admitted
  exactly when all four coefficients of x-y are even. Then s=(x+y)/2,
  t=(x-y)/2 and C sends the pair to (s+rho t, s-rho t) with rho=j^2.
  Otherwise the pair is fixed.
- **Units.** U10 is the set of the ten units +j^s and -j^s, s=0,...,4.
- **Cyclotomic arithmetic.** It runs in Z[X]/(Phi_25(X)) with zeta=X.
  Two maps are used:
  - j is sent to zeta^5;
  - complex conjugation of the principal embedding is
    zeta -> zeta^-1 = zeta^24.
- **Exactness.** No floating point is used anywhere. Integers and
  `fractions.Fraction` are allowed. Tolerance is zero throughout.

## 5. Common objects

Slots hold elements of O.

- **Neutral pair.** (z,-z), with p the first (positive) slot and q the
  second.
- **Receiver.** It acts on a pair (p,q) and one stock slot X. Its word is
  W=[C(p,X), C(p,q)]^5: ten contacts, the stock contact first in each
  block. Its literal inverse reverses W and replaces every contact by C^4:
  forty contacts.
- **Inputs.** The input for digit b is (p,q)=(j^b,-j^b). The reading is
  Q(X_out). A stock succeeds when its five readings are pairwise distinct.
- **Stocks.** R=(3,4,2,0)=1+2a with a=(1,2,1,0). T=(1,2,0,-2)=1+2j-2j^3.
  S=(2,-2,1,0)=2-2j+j^2.
- **Clock layout.** Ten slots; pair k is slots (2k, 2k+1). A whole-pair
  swap (a,b) consists of the slot swaps (2a,2b) and (2a+1,2b+1).
- **Compressed word for V_m.** Pair swaps (3,4), (2,3), (1,2), (0,1) in
  that order. Then contact power 3(m+1) mod 5 on pair 0 and 3m mod 5 on
  each of pairs 1 to 4.
- **Padded word for V_m.** The same eight slot swaps. Then C^3 on pair 0,
  then C^k on each pair 0 to 4 with k the representative of 3m mod 5, then
  4-k blocks of C^5 on pair 4. That is 23 contact attempts for every m.
- **Inverse word.** It applies contact power (5-p) mod 5 on each pair, for
  that pair's forward power p, then the pair swaps in the reverse order
  (0,1), (1,2), (2,3), (3,4).
- **Delta preparation.** e0 puts (1,-1) on pair 0 and zero elsewhere. Its
  account is 4. After n ticks the receiver is attached at pair n mod 5.

## 6. Frozen checks

Every item is a falsifier. Every "all" ranges over the complete finite set
named. Expected values are taken from the target documents and are fixed
here.

**R1 Ring and contact law.**
- Q(closed form) equals Tr(a abar)/2.
- Q>0 for every nonzero element of [-3,3]^4, and Q>=2 there.
- For all 6561 ordered pairs in [-1,1]^4:
  - C^5 is the identity;
  - C^4 equals the rho^-1 inverse formula;
  - sum and Q are preserved;
  - refused pairs are fixed.
- On the 256 pairs from {0,1}^4 x {0,1}^4, exactly 16 are admitted.
- **Unit covariance.** C(ux,uy)=u C(x,y) and Q(ux)=Q(x), for all u in U10
  and all 6561 pairs.
- **Golden unit.** phi=1+j+j^4 satisfies phi^2=phi+1 and Q(phi)=3.
- **Norm identity.** For every nonzero a in [-2,2]^4:
  - a abar=A+B phi with A=x0-x1 and B=x1-x2, where x0, x1, x2 are the
    coefficients of 1, j+j^4 and j^2+j^3 in a abar;
  - Q(a)=2A+B;
  - Q(a)^2-5B^2=4N(a), where N(a) is the exact integer determinant of
    multiplication by a on O;
  - N(a)>=1.
- **Completeness bound (B1).**
  - G=(5I-11^T)/2 and G^-1=(2/5)(I+11^T) multiply to I exactly.
  - 5 c_i^2 <= 4 Q(c) for all 14641 c in [-5,5]^4.
  - Q(5,2,2,2)=32.
  - No c in [-8,8]^4 with some |c_i|>=6 has Q(c)<=44.

**R2 Receiver with R.**
- Q(R)=32, Q(a)=7, Q(1+a)=10.
- The cyclic five-coefficient product (1+a) abar has coefficients
  (7,4,1,2,6), with sum 20.
- For each b, the ten admission decisions are as follows, with k=2b mod 5:
  - in blocks before k, the stock contact refuses and the balanced
    contact admits;
  - in blocks i>=k, the stock contact admits;
  - in those blocks the balanced contact refuses while n=i-k+1 is in
    {1,...,4}, and admits when n=5.
- After n admitted stock contacts, R_n=1+a+rho^n a and p_n=1+a-rho^n a.
- The terminal states R_1,...,R_5 are (1,1,1,1), (3,2,0,-1), (2,3,3,1),
  (1,0,-1,-1) and (3,4,2,0), with Q equal to (2,27,17,7,32).
- The readings for b=0..4 are (32,17,2,7,27).
- The work released by the stock is (0,15,30,25,5).
- The account is 36 and the slot sum is conserved.
- Adding the untouched companion -R gives account 68 and total sum zero.
- The forty-contact inverse restores the complete state.

**R3 Raw triples.**
- The alphabet has twelve elements: 0, 1, j, j^2, j^3, j^4, -1, J=1+j^2,
  a, R, T, phi.
- For all 1728 triples (p,q,X): the receiver and its literal inverse
  restore the triple, total Q and total sum are conserved, and every
  refused contact leaves the pair fixed.
- The all-refused input (1,j,0) stays fixed.

**R4 Labels, re-encodings and semantic controls.**
- **Two-pair pointer.** For all 25 labels r=r0+5r1, the low pair is
  (j^r0,-j^r0) and the high pair is (j^r1,-j^r1). With R on the high pair:
  - the reading equals the R2 reading at b=r1;
  - the low pair is unchanged;
  - the account is 40, or 72 with -R.

  With T, the accounts are 30 and 52.
- **Re-encodings.** For all 125 pairs (r,t), the re-encoding (1+5t)r
  mod 25 keeps r mod 5. Its five high digits are pairwise distinct exactly
  when r mod 5 is nonzero, and all equal when r mod 5=0.
- **Witness r=13.**
  - labels (13,3,18,8,23);
  - high digits (2,0,3,1,4);
  - readings (2,32,7,17,27);
  - signed stock work (-30,0,-25,-15,-5).
- **Semantic controls.** Five name assignments on the unchanged r=13 state
  give five identical complete output states, with reading 2.

**R5 Root clock.**
- **Neutral fixtures, for each m=0..4.** All 5x12 single-site fixtures
  (one alphabet element at one pair site, zero elsewhere) and these dense
  amplitude vectors:
  - (0,0,0,0,0), (1,0,0,0,0), (0,0,0,0,J), (1,j,j^2,j^3,J);
  - (R,a,-1,0,phi), 2(1,j,j^2,j^3,J), (1,0,J,0,-j), (1,1,1,1,1);
  - (T,S,R,a,1).

  On each fixture:
  - the compressed word equals the amplitude formula
    V_m(z)=(j^(m+1) z4, j^m z0, j^m z1, j^m z2, j^m z3);
  - the state stays neutral;
  - the account is preserved;
  - the padded word gives the same endpoint, with 23 attempts and eight
    slot swaps;
  - the literal inverse restores the state;
  - five ticks multiply every amplitude by j;
  - 25 ticks give the identity;
  - the least period is 25 for every nonzero fixture and 1 for zero.
- **Raw fixtures.** Forty deterministic ten-slot states, with slot i of
  state o equal to alphabet[(7o+3i+i*i) mod 12], o=0..39. For each m and
  each state:
  - padded and compressed endpoints agree;
  - the literal inverse restores the state;
  - the account is preserved at every tick;
  - five ticks equal C^3 on every pair;
  - 25 ticks give the identity.
- **Minimum neutral account.** The minimum nonzero neutral account in the
  five-pair carrier is 4: every nonzero amplitude has Q>=2 (from R1), and
  e0 attains 4.

**R6 Clock experiments and relative phase.**
- For each m and each stock X in {R,T,S}:
  - one tick from e0 leaves only pair 1 occupied, with amplitude j^m;
  - thirteen ticks leave only pair 3 occupied, with amplitude j^(13m+2).
- The complete account is 4+Q(X), or 4+2Q(X) with the untouched companion
  -X, whose total sum is zero.
- The receiver inverse and then the clock inverse restore e0 and X.
- With the stock-only frame j^s X, the six tables below (rows s=0..4,
  columns m=0..4) are reproduced exactly:

```text
Q32_ticks_1    [[32,17,2,7,27],[27,32,17,2,7],[7,27,32,17,2],[2,7,27,32,17],[17,2,7,27,32]]
Q32_ticks_13   [[2,32,7,17,27],[17,27,2,32,7],[32,7,17,27,2],[27,2,32,7,17],[7,17,27,2,32]]
Q22_T_ticks_1  [[22,12,2,7,17],[17,22,12,2,7],[7,17,22,12,2],[2,7,17,22,12],[12,2,7,17,22]]
Q22_T_ticks_13 [[2,22,7,12,17],[12,17,2,22,7],[22,7,12,17,2],[17,2,22,7,12],[7,12,17,2,22]]
Q22_S_ticks_1  [[12,7,22,2,17],[17,12,7,22,2],[2,17,12,7,22],[22,2,17,12,7],[7,22,2,17,12]]
Q22_S_ticks_13 [[22,12,2,7,17],[7,17,22,12,2],[12,2,7,17,22],[17,22,12,2,7],[2,7,17,22,12]]
```

- **Relative identity.** For n in {1,13}, every m and X in {R,T,S},
  let u=j^(nm). Then the complete final state (ten clock slots and the
  stock) of the experiment (V_m, X) equals u times the complete final state
  of (V_0, u^-1 X). In particular q_n(m,X)=q_n(0,j^(-nm)X).
- **Simultaneous covariance.** For all u in U10, start from (u e0, u X).
  The final state is u times the unrotated final state, and the reading is
  unchanged.
- **Gauge conjugacy over O.** D_m V_0 D_m^-1=V_m exactly, where
  D_m=diag(1,j^m,j^(2m),j^(3m),j^(4m)) acts on amplitudes.
- **Holonomy.** The product of the five hopping coefficients of V_m around
  the cycle is j for every m.

**R7 Stock census, Q<=32.**
- Enumerate all 14641 c in [-5,5]^4. Exactly 1811 have Q<=32.
- Apply the literal receiver to all five inputs of each.
- Successes by level are exactly {22:40, 28:40, 32:40}, 120 in total, and
  there is none below 22.
- R, T and S all succeed.
- T reads (22,12,2,7,17) with work (0,10,20,15,5). S reads
  (12,7,22,2,17). j^3 S reads (22,2,17,12,7).
- For T: Q(1+2j-2j^3-1)=Q(j-j^3)=5 and Q(1+j-j^3)=7. The cyclic product
  (1+a) abar with a=j-j^3 has coefficients (2,0,-2,-1,1).
- Accounts:
  - high pair plus T or S: 26, or 48 with the neutral companion;
  - two-pair pointer plus T: 30, or 52 with the neutral companion.
- The minimum record in the lexicographic order of (Q, stock) is Q=22,
  stock (-4,-2,-2,-3), readings (17,12,7,22,2).
- Every success's full inverse restores all five inputs.
- **Canonical digest.**
  - Sort the success list by the pair (Q, stock tuple).
  - Each record is an object with keys `Q` (int), `stock` (four ints) and
    `readings` (five ints, b=0..4).
  - Serialize the list with
    `json.dumps(records, sort_keys=True, separators=(",",":"))`, append
    one LF, and take the SHA-256 of the ASCII bytes.
  - Expected digest:
    a176b08e95b22febaf0e5edec05a6024a271cb08e26050ff6ad795134ecf142c.

**R8 Box census [-2,2]^4.**
- All 625 stocks, with no Q cutoff.
- Exactly 32 succeed: {22:16, 28:8, 32:8}.
- The same canonical digest is
  c09ba2caeb2c494642a664140ac8d8574268e7af120b59de68467e9061448cad.

**R9 Rotation rule (B4).**
- For all 1811 candidates of R7, every s=0..4 and every b:
  reading_{j^s X}(b)=reading_X(b-s mod 5).
- For every nonzero candidate, the five j^s X are pairwise distinct, have
  equal Q, and either all succeed or all fail.

**R10 Linear algebra and spectra, exactly in Z[zeta_25].**
- **Eisenstein.** Phi_25(X+1) and Phi_5(X+1) are Eisenstein at 5: monic,
  every lower coefficient divisible by 5, constant term not divisible
  by 25.
- **The root j.** j=zeta^5 satisfies 1+j+j^2+j^3+j^4=0.
- **The roots lambda_t.** lambda_t=zeta^(1+5t) satisfies lambda_t^5=j, and
  the five lambda_t are pairwise distinct.
- **Basis.** The exponents 5i+k, 0<=i<=3 and 0<=k<=4, are exactly
  0,...,19, each once.
- **Eigenvectors.** w_t=(1, lambda_t^-1, ..., lambda_t^-4) satisfies
  V w_t=lambda_t w_t exactly.
- **Left vectors.** l_t=(1, lambda_t, ..., lambda_t^4) pairs with w_t to 5
  and with w_t' to 0 for t'!=t.
- **Projections and reconstruction.** For every neutral R5 fixture z and
  every t: c_t=(1/5) sum_k z_k lambda_t^k is nonzero when z is nonzero,
  and 5z=sum_t (5c_t) w_t exactly.
- **Commutant.**
  - The 20 matrices j^i V^k (0<=i<=3, 0<=k<=4) are Q-linear maps on Q^20.
  - Their rank modulo 1000003 is 20.
  - The commutation system XV=VX on Q^20 has nullity 20 modulo both
    1000003 and 998244353.
  - Hence the rational commutant has dimension exactly 20: the rank modulo
    p is a lower bound on the rational rank, and the nullity modulo p is an
    upper bound on the rational nullity.
- **Invertible filters.** For all 242 nonzero integer coefficient vectors
  P in {-1,0,1}^5, the integer determinant of the 20x20 rational matrix
  of P(V) is nonzero. It is computed exactly, by fraction-free
  elimination.
- **H_m.** For each m:
  - H_m=2I-j^m V-j^-m V* equals (I-j^m V)*(I-j^m V) exactly;
  - H_m w_t=mu w_t with mu=2-zeta^e-zeta^-e and e=1+5(t+m) mod 25;
  - H_m=D_m H_0 D_m^-1.
- **Ground mode.** At the principal embedding, mu=4 sin^2(pi e/25), which
  increases strictly with d=min(e,25-e) on 0..12. The ground mode is
  therefore the t of least d.
  - The argmin t over m=0..4 is (0,4,3,2,1).
  - For m=0, the d values over t=0..4 are (1,6,11,9,4).
  - Every mu is nonzero, since d is never 0.

## 7. Exploratory outputs

These are not falsifiers. Their values are not predicted. They are reported
unchanged and are not used to judge the target.

- **X1 Level counts up to Q<=44.** The same box [-5,5]^4 is complete
  there, because 4*44/5<36.
- **X2 Symmetries of the 120 successes.** Is the set closed under each of
  these maps, applied to the stock alone:
  - negation;
  - complex conjugation j -> j^-1;
  - the Galois maps j -> j^2 and j -> j^3?

  Also reported: the orbit count under stock multiplication by U10.

## 8. Output

Stdout is exactly one line:
`json.dumps(result, sort_keys=True, separators=(",",":"))` followed by LF.

It contains:
- the status string;
- the R2 readings and the R7 and R8 counts, digests and minimum record;
- the six R6 tables;
- the R10 argmin vector;
- the X1 and X2 values;
- the number of executed checks;
- `"verdict":"PASS"`.

It contains no paths, times, platform values or floating-point numbers.
Any failed check raises an exception. The process then exits nonzero and
prints no PASS line.

## 9. Execution

The run happens once, after the pin and the readback, in this order:

1. **Target binding.** Make a clean worktree of the target head. Run
   `sha256sum -c` against TARGET-SHA256SUMS inside its target directory.
   Any mismatch stops the run.
2. **Review checker.** From the repository root of the pinned review
   commit:

   ```sh
   env -i PATH=/usr/local/bin:/usr/bin:/bin LC_ALL=C LANG=C TZ=UTC \
     PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
     timeout 900 prlimit --as=2147483648 \
     python3 -I -B notes/C-FIXED-RECEIVER-SELECTION-REVIEW-N/review.py
   ```

   Stdout is saved as EXPECTED.txt.
3. **Replay of the target verifiers.** In the target worktree's directory,
   with the same environment, run `verify_receiver.py` and then
   `verify_stock_census.py`. Use the target's own limits: timeout 300 and
   `prlimit --as=1073741824`. Each stdout must equal RECEIVER-EXPECTED.txt
   and STOCK-EXPECTED.txt byte for byte.
4. **Informal rerun.** In INFORMAL/, with the same environment, run
   `python3 -I check_receiver_indep.py` and then
   `python3 -I stock_scan.py check_receiver_indep.py`. Compare their stdout
   with the transcription in INFORMAL/PROVENANCE.md.

Each process must exit 0 with empty stderr and no timeout. RUN.md records
the commands, the environment (OS, architecture, Python version), exit
codes, byte counts and SHA-256 of every stdout and stderr. It records no
machine nicknames.

This is a single x86_64 lane. A second-architecture replay of the same
pinned bytes is welcome. If one is done, it is recorded separately and does
not alter this run.

## 10. Failure handling

An exception, a nonzero exit, nonempty stderr, a timeout or any stdout
mismatch is not a pass.

A fired check is recorded unchanged. If a failure is a defect of the
checker rather than a property of the target, RUN.md says so and keeps the
frozen file. Any correction is a new, separately pinned revision, and both
runs are retained.

Known target results never justify dropping a case, moving a threshold or
editing an expected value.

A replay mismatch of a target verifier is reported as a target replay
failure, distinct from review.py. A mismatch in the informal rerun is
reported as a reproducibility failure of the informal bytes only.

## 11. Interpretation

MATHEMATICAL-REVIEW.md reviews the in-scope files without code, section by
section. It gives each scope S1 to S7 one verdict: accept, accept with
stated corrections, or reject. A computational pass confirms only the
finite statements listed in section 6. Two kinds of statement rest on the
hand review alone:
- infinite statements, such as "every nonzero K^5 vector" or "any W with
  W^5=jI";
- interpretive statements.

A mathematical fit is not a Canon fold. This review changes no target
file, registry row, status, Canon text or release. Accepting the review, and
any later merge or promotion, are decisions for the Canon owner.
