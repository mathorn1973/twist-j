# C-RH-SEMISTABLE-FRAME-N: round 8 finite audit preregistration

NON-CANONICAL. No authority. No Canon status changes.

Owner: A. M. Thorn, session ChatGPT-Astra-Sol-20261123-R8.
Public claim: https://github.com/mathorn1973/twist-j/issues/2070.
Public basis: 93c36089db57032a6cbca482ff62c95884567d0f.
External source basis: leanprover-community/riemann-hypothesis at
40e56bab026552e089d7afcfeff08d2defb9c005.
Action layer: NOT_APPLICABLE (finite-dimensional linear algebra).

This is the first computational audit under this identifier in this session.
The earlier conversation proofs and its reviewer's reported computations are
exposed prior information, not blind predictions. The new audit has not run.
This contract freezes its domain and failure threshold before either program
is executed. It does not test actual automorphic matrices or the RH claim.

## Statements and conventions

For linear maps A_u : E_u -> F over one field, put D=dim(F)>0 and
R=sum_u dim(E_u)>0. Define

    eps(A) = max_{W <= F} (sum_u dim(A_u^{-1}(W))/R - dim(W)/D).

Let P : direct_sum(E_u) -> F be the sum of these maps and K=ker(P).
The kernel formula to audit is

    D eps(A) = max_{U_u <= E_u}
      [ dim(K intersect direct_sum(U_u)) - (1-D/R) sum_u dim(U_u) ].

No injectivity or spanning hypothesis is imposed.

Put g=gcd(D,R), a=R/g, b=D/g, N=D*R/g. For positive integer l and
arbitrary matrices X_u of size (a*l) by (b*l), define the square matrix

    M_l = horizontal_concat_u (A_u tensor X_u).

The certificate inequality is

    eps(A) <= 1 - rank(M_l)/(N*l).

A matching subspace W and matrix M_l certify an exact defect. The audit
checks this inequality, not an unbounded search for noncommutative rank.
The characteristic-zero maximum-rank theorem is a separate paper derivation
using the classical maximum-shrunk-subspace / blow-up theorem.

For maps invariant under a declared target/source block decomposition, put
D_alpha=target block dimensions, d_alpha=sum source block dimensions,
k_alpha=sum individual kernel dimensions, r_alpha=d_alpha-k_alpha,
q_alpha=D_alpha/D, p_alpha=d_alpha/R, b_alpha=r_alpha/R,
kappa=sum k_alpha/R, beta=sum |p_alpha-q_alpha|/2, and
B=sum max(q_alpha-b_alpha,0). If r_alpha>0, set

    e_alpha = max_{W in target block}
       (sum_u dim(image(A_{u,alpha}) intersect W)/r_alpha - dim(W)/D_alpha).

A zero-rank block has weight zero in the weighted sum below. Audit:

    max(kappa,beta) <= B <= kappa+beta;
    B <= eps(A) <= B + sum min(q_alpha,b_alpha)*e_alpha;
    if every positive-rank block has e_alpha=0, eps(A)=B;
    if additionally p=q, eps(A)=kappa.

## Frozen domains

### A. Exhaustive finite-field maps and all subspaces

Use exactly these (field order q, target dimension D, source dimensions)
triples, in the listed order:

    (2,2,(1,1)), (3,2,(1,1)), (2,2,(1,2)), (3,2,(1,2)),
    (2,3,(1,1)), (3,3,(1,1)), (2,3,(1,2)), (2,3,(2,2)).

Enumerate every entry of the two source matrices in F_q, with source index,
then row, then column as the flat entry order, lexicographic with values
0,...,q-1. There are 6291 families. Include zero maps and all rank defects.
For every family, compute eps over ALL target subspaces and the kernel
expression over ALL pairs of source subspaces. Compare exact fractions.
The development implementation will use a basis of K and intersection
dimensions for its right-hand side, not just substitute rank(P|U) into the
same expression used for its left-hand side.

### B. Finite Kronecker rank certificates

For every family in A, test l=1 and seeds t=0,1,2,3. For the first
min(32,number of families) families of each triple, also test l=2 and all
four seeds. Within each triple, family_index starts at zero. Initialize
state=1+t+17*family_index and generate the X_u entries in source, row,
column order by repeating

    state = (1103515245*state + 12345) mod 2^31;
    entry = (state >> 16) mod q.

The sequence is deterministic integer arithmetic, not statistical evidence.
For every generated matrix verify the certificate inequality using the eps
already obtained by exhaustive subspace enumeration. Existence of an optimal
matrix in this finite search is NOT asserted.

### C. Genuine finite group averaging, over Q

Order N=F_2^2 as (0,0),(0,1),(1,0),(1,1). Let s swap coordinates and
P=(I+s)/2 act on Q^N. Form the three characters
chi10(x)=(-1)^x1, chi01(x)=(-1)^x2, chi11(x)=(-1)^(x1+x2).
Check that their ordinary rational Gram matrix is 4I and their rank is 3.
Check that P maps them to b,b,c with b,c independent; each resulting line
map is injective, the target span has dimension 2, and their synthesis has
kernel spanned by (1,-1,0).

In target coordinates (b,c), the matrices are e1,e1,e2. The line W=span(e1)
has defect 1/6. Use l=1,a=3,b=2,N=6 and the following three auxiliary
3 by 2 matrices (columns displayed):

    X1=(e1,e2), X2=(e2,e3), X3=(e1,e2).

Check rank(M_1)=5. The lower subspace witness and upper rank witness must
therefore certify eps=1/6 exactly. This is a finite group-averaging model,
not an identification with the automorphic family.

### D. Exhaustive block budgets

There are two source maps. Each source has two ordered one-dimensional
blocks. Each map is block diagonal, with one arbitrary column in each
corresponding target block. Enumerate every column for target block sizes
(1,1) and (1,2) over F_2 and F_3, and sizes (2,2) over F_2. These are 1146
families. Compute the full eps over ALL target subspaces, not only block
subspaces. Compute each positive-rank e_alpha over ALL subspaces of that
target block. Check every block-budget statement above, including the
conditional equalities whenever their stated hypotheses hold.

### E. Normalization of relative trace errors

For all integers s,t in 1,...,8, n in 2,...,8, m in 1,...,n-1, and both
signs delta1,delta2 in {-1,+1}, put p=(s,t)/(s+t), eta=m/n,
ai=1+deltai*eta, mu=sum p_i*a_i, q_i=p_i*a_i/mu and
v=sum |p_i-q_i|/2. Audit the rational inequality

    2*v <= eta*(1+v*v),

which, for 0<=v<=1 and 0<=eta<1, is equivalent to
v<=eta/(1+sqrt(1-eta^2)). There are 7168 grid cases. Additionally check the
exact equality case eta=3/5, p=(2/3,1/3), a=(2/5,8/5), q=(1/3,2/3), v=1/3.
Check the two 2-by-2 probability tables with entries (1/2,0,0,1/2) and
(1/4,1/4,1/4,1/4): identical row and column marginals, joint total
variation 1/2. No implication from two marginals to joint balance is tested
as a positive claim.

## Implementations, pin and execution

Files: verify.py (development), break.py (opposition), this PREREG.md.
Both programs use Python's standard library, integer arithmetic and Fraction
only for scientific assertions. No floating point, numerical rank tolerances,
network access, random seeds, external packages or mutable fixtures.

The opponent receives this contract and its Git commit, but does not read
verify.py. Both programs must be committed and pushed before either run,
with their hashes read back from Git. Freeze break.py before any comparison
with verify.py. Static parsing is permitted before the pin.

Run both from the repository root with PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1 and PYTHONUTF8=1. First-run budget: 180 seconds per
program. The two outputs need not be byte-identical because these are distinct
implementations; each must give exact domain counts and the same mathematical
verdicts. Record each stdout and hash separately, actual architecture and
Python version. One local architecture is a one-lane candidate-C audit.
Same-session adversarial coding is not external independent confirmation.

Failure threshold: any failed asserted equality/inequality, nonzero exit,
uncaught exception, incomplete domain, or exhausted time budget is a recorded
failure of this audit. Preserve its code, domain, output and result. Do not
edit the frozen programs, move thresholds or silently rerun a repaired pin.
Any repair needs a new prospectively frozen audit instance with the failed
instance retained. A passing finite audit is not a proof over all dimensions.

Promotion is outside this package. Final custody includes the English proof
note, source references, opponent dispositions and PROMO-C-RH-SEMISTABLE-FRAME-N.
