# Round 9 prospective exact audit

NON-CANONICAL. No Canon authority or status promotion.

- Candidate: C-RH-SEMISTABLE-FRAME-N (existing alias C-RH-BK-CONCENTRATION-N).
- Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261123-R9.
- Claim: issue #2070; draft delivery: PR #2071.
- Public basis: 93c36089db57032a6cbca482ff62c95884567d0f.
- Round 8 continuation basis: e3350f8951cc2a61b3ae3af9e377c44663e10387.
- External source, read only: leanprover-community/riemann-hypothesis at 40e56bab026552e089d7afcfeff08d2defb9c005.
- Action layer: NOT_APPLICABLE (classical algebra and local representation theory).
- Status ceiling: candidate-C for finite executions, candidate-D for the separate paper deductions.
- This is a new audit in the same unsealed incubation item. Round 8 frozen code, contract and first-run records are not modified.

## 1. Object and prospective claims

The defect of a family A_u:E_u -> F with D=dim F and R=sum dim E_u is
eps(A)=max_W [sum_u dim A_u^{-1}(W)/R - dim W/D].

A. Construct exact coordinate-inclusion families which are injective, span the target, and satisfy EVERY off-diagonal pairwise Gram-energy bound with equality, yet have defect (1-rho)*sqrt(sigma)/2, where rho=d/D and sigma=D/R. The all-subspace upper bound is proved separately by the projection trace inequality; computation checks the coordinate certificate and its spectral upper bound, not an enumeration of all complex subspaces.

B. Realize the family by literal finite-group averaging of orthogonal seeds, with all seed characters in one conjugacy orbit and with no common Fourier-blind target vector. This tests the proposed inference from these algebraic properties to small intrinsic defect.

C. Add honest regular finite-group data and a nontrivial generic Hecke corner. Verify exact source/target block balance and persistence of the same intrinsic defect in each block.

D. Check the lattice normal form which identifies the actual local word-prime level with a mirabolic congruence subgroup. This is a finite check of the normal form only. It does not compute automorphic representations, prove a newform theorem, run Lean, or test the actual period ranks.

## 2. Exact domain and fixed cases

All mathematical computation uses integers and fractions, with the Python standard library only. No floating-point arithmetic, randomized trials, external packages, network calls or external mathematical code.

### A. Affine incidence family

The eight ordered parameter pairs (t,m) are fixed:
(2,11), (2,17), (2,29), (3,19), (3,37), (4,37), (4,67), (5,53).

Set s=t^2. For each K in {s-t,s,s+t}, each a=1,...,m-1 and b=0,...,m-1, define the subset
S(K,a,b)={a*j+b mod m: j=0,...,K-1}.
The atom (K,a,b) has integer weight n_K=m-s for K=s-t or s+t, and n_s=2s. A weight means that many distinct identical coordinate copies, which may be processed by weighted exact sums.

Let D be the total weight, d_u the weighted number of atoms containing word u, and lambda_uv the weighted number containing u and v. Require:
- every atom has exactly K members and K>0;
- D=2*m^2*(m-1);
- every d_u=d=2*m*(m-1)*s;
- R=sum d_u=s*D;
- every distinct pair has lambda_uv=2*s^2*(m-1)=d^2/D;
- the normalized coordinate occupancy Q has entries K/s, mean 1, and variance (1-s/m)/s;
- the positive spectral mass sum weight*max(K/s-1,0)/D is (m-s)/(2*m*t);
- the coordinate subspace consisting of all K=s+t atoms attains exactly the same defect;
- all word maps are injective and their images span the full coordinate target;
- the squared defect and variance satisfy the paper upper bound eps^2 <= variance/4.

Fixed prospective counts: 34,134 weighted atom labels (not coordinate copies), 270 individual source counts and 5,689 unordered distinct-word pair counts.

### B. Literal finite-group averaging

Use m=11. The normal subgroup is N=(Z/2)^11; the cyclic group Gamma=C_11 rotates the coordinates. The ambient finite group is N semidirect Gamma. On it take f_u(n,h)=(-1)^(n_u), independent of h.

Exhaust n=0,...,2^11-1, all u, all cyclic rotations h and all standard basis translations in N. Check the character transformation and permutation of all f_u. Under normalized counting measure check <f_u,f_v>=delta_uv. Average over Gamma to obtain b=(sum f_u)/11. Check ||b||^2=1/11 and <f_u,b>=1/11 for every u.

The target is C^Y tensor C*b. For each u its full N-character projection is y tensor b -> y tensor f_u/11, hence is injective. The seed subspaces are I_u tensor C*f_u, whose joint sum is direct. Multiplying all averaged maps by sqrt(11) gives the isometric inclusion family in A. Computation uses only the squared normalization 11; no square-root approximation is permitted.

### C. Generic Hecke corner of S_3 = GL_2(F_2)

Enumerate all six permutations of {0,1,2} and their left regular 6 by 6 matrices. Let tau=(0 1), E=(I-L_tau)/2, Z_triv=sum L_g/6, Z_sign=sum sign(g)L_g/6 and Z_std=I-Z_triv-Z_sign.

Check E is a self-adjoint idempotent of rank 3; E Z_triv=0; E Z_sign and E Z_std are orthogonal idempotents of ranks 1 and 2 whose sum is E. All six matrices E L_g E commute pairwise and their rational span has dimension 2.

Tensor the data from A by this regular representation and apply E. In every one of the eight families verify exact source and target weights 1/3, 2/3, zero kernel and span budget, the same intrinsic defect in both blocks, and weighted intrinsic defect equal to the untensored defect. The paper proof treats arbitrary regular finite-group factors; the finite audit only treats this six-element example.

### D. Mirabolic normal form

Use (k,p)=(1,2),(1,3),(1,5),(2,2),(2,3). For each pair enumerate all k by k matrices C with entries 0,...,p^2-1; retain those with determinant not divisible by p.

In the (k+1)-dimensional ambient space put z=e_1, ell=(p,1,0,...,0), and let the columns of B be z, w_1=e_1-p*e_2, e_3,...,e_(k+1). Set G=B diag(1,C) B^{-1}, exactly over the rationals.

Check G*z=z, ell*G=ell and det G=det C. Check every entry of G and G^{-1} is p-integral if and only if the first column of C is e_1 modulo p. A rational is p-integral when the denominator of its reduced fraction is not divisible by p.

Fixed prospective counts: 6,855 matrices before the determinant filter; 4,012 after it; exactly 528 satisfy the integral ambient-stabilizer condition. The paper argument applies to every residue characteristic, and is not inferred by extrapolating these cases.

## 3. Falsifiers and failure handling

Any failed identity, wrong count, nonzero pairwise discrepancy, missing character transformation, wrong Hecke block or failure of the lattice biconditional is a failure of that subtest. Preserve the first stdout, stderr and exit status. A timeout is a recorded non-completion, not a pass. A discrepancy between the independently authored programs is a failure to confirm.

Do not change these cases, expected formulae, limits or thresholds after execution. Do not silently fix and rerun a fired implementation. An amendment, if genuinely necessary, must preserve the failed first run and use a separately named and newly preregistered audit. No such amendment is presumed.

The audit cannot falsify or confirm RH and cannot prove semistability of the actual automorphic maps. It tests specific finite constructions and normal forms only.

## 4. Freeze, independence and execution order

1. Commit and publish this contract on the existing branch; read it back at an immutable commit.
2. Development Sol writes verify_r9.py from this contract. Opponent Sol independently writes break_r9.py from this contract without reading verify_r9.py, its outputs or unpublished implementation. Use separate Git worktrees.
3. Both programs must be frozen and committed before comparison. Static parsing and paper review are permitted before freezing; no scientific test execution, imported execution or exploratory computation is permitted.
4. Publish both programs, verify their exact readback bytes and record the immutable execution pin before either first run.
5. Run each script once under a 180-second wall limit, preserving stdout, stderr and exit status under the names below. Root runs both only after both freezes. No optional reruns to manufacture agreement.
6. The whole report and opponent reviews are then committed and read back. These are same-session independent implementations on one x86_64 architecture, not an external review or a public two-architecture gate.

Expected program interface: Python 3, no arguments, stdout human-readable exact diagnostics and a final pass/fail summary, nonzero exit on any failure. Exact output byte identity between the programs is not required.

## 5. Prospective artifact paths

All paths are relative to notes/C-RH-SEMISTABLE-FRAME-N/round9/:

- PREREG.md (this file, immutable)
- verify_r9.py
- break_r9.py
- verify_first.stdout.txt
- verify_first.stderr.txt
- verify_first.record.json
- break_first.stdout.txt
- break_first.stderr.txt
- break_first.record.json
- PROOF.md
- SOURCE_MAP.md
- RESULTS.md
- REVIEW.md
- CUSTODY.md

The existing parent README and PROMO-C-RH-SEMISTABLE-FRAME-N.md may be updated to link this continuation. Existing round 8 frozen evidence remains unchanged. Repo-backed artifacts are handed off through Git.

## 6. Limits and scientific separation

The sharp-obstruction family is an abstract counterexample to an inference from the audited properties. It is not identified with the actual P_u, does not reproduce their full adelic construction, and is not a counterexample to RH.

The local newform application depends on the pinned source's primitive split Hida realization and classical theorems cited in the paper note. Finite checks here do not replace those hypotheses or a formal proof.

The actual global period ranks and the hoped-for exponential intrinsic-defect bound remain separate open obligations. The centered frame estimates of issue #2065 / PR #2067 are used with attribution.

