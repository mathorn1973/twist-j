# Prospective exact audit: internal four-unit separation

NON-CANONICAL. NO AUTHORITY. Candidate-C only for any completed finite audit.
Action layer: L1, exact algebraic integer arithmetic. No physical or RH claim.
Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Internal-Separation.
Claim: https://github.com/mathorn1973/twist-j/issues/2090
Public basis: main 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed, Public Canon v117.

## 1. Question, equations and fixed input

Let phi satisfy phi^2=phi+1. Fibonacci and Lucas numbers have initial values
F_0=0,F_1=1 and L_0=2,L_1=1 and the recurrence X_(i+2)=X_(i+1)+X_i.
Fix m=25 and derive N=5F_m^2+5F_m+1 from that recurrence. The search must not
use any factor of N to choose or order its tests.

The exact, closed search domain is all triples (a,b,epsilon) in lexicographic
order with a=0,2,...,248, b=1,3,...,249 and epsilon=-1,+1, in that sign order.
For each of the 31250 triples calculate

    value = L_a + epsilon L_b
    g = gcd(N,value).

Report the full histogram of g and the first triple with 1<g<N, or null.
The four-unit interpretation is L_a=phi^a+phi^(-a) for even a and
L_b=phi^b-phi^(-b) for odd b. Repeated units count separately.

This is a bounded existence search, not an assertion that it will succeed.
A null outcome is retained without changing the domain.

## 2. Auxiliary audit of the published factor pair

Only after the main search definition, audit p=251 and q=112128001 as a
published factor pair. Verify their product equals N and certify each is
prime by exact trial division through its integer square root.

Work in the WHOLE quotient Z[phi]/p Z[phi], not one selected embedding.
Find the exact order of phi by its first return in exponents 1,...,250 and
the order of alpha=phi^2 by its first return in exponents 1,...,125.
Failure to return within these stated bounds is a falsifier, not permission
to expand them. Record the resulting orders; do not assert their values
before the audit.

The common formal labels are (epsilon,e) for epsilon=-1,+1 in that order and
e=0,...,249. Label index is e for epsilon=-1 and 250+e for epsilon=+1.
Evaluate all 500 labels as epsilon*phi^e in each whole quotient. They must
be pairwise distinct in each quotient, otherwise the stated label model
is falsified. This includes signs even if a component has smaller order.

For each prime collect the label indices with value 1. These represent all
normalized two-unit vanishing relations. Collect all ORDERED index pairs
(i,j) whose values sum to 1. These represent all normalized three-unit
vanishing relations, including repetitions. Multiplication by a signed
unit normalizes every relation with at most three signed real units to
one of these forms. Compare the two sets exactly. Report their counts,
digests and the cardinality and first element of each symmetric difference.
One-unit sums cannot vanish because every summand is a unit.

Any conclusion about allowing phases j^c additionally uses the previously
proved phase projection O=Z[phi]+j Z[phi], with every coordinate of a unit
being zero or a signed real unit. That paper lemma is attributed separately;
the present executable audit by itself covers the real-unit labels only.

## 3. Algorithms and independent implementation

The main verify.py uses Fibonacci/Lucas recurrences and arithmetic in the
quadratic coefficient pair (constant,phi coefficient). The breaker break.py
is written from THIS specification without reading verify.py. It uses
independent matrix powers for sequence values and the four-coordinate
cyclotomic quotient Z[j]/(1+j+j^2+j^3+j^4) for the auxiliary relations, with
phi=-j^2-j^3. Both use Python's standard library, integers and exact gcd.
No floating arithmetic, probabilistic primality test, external service,
random seed or timing-dependent output is permitted.

The breaker is frozen before implementation comparison. Both exact source
files and this preregistration must be committed, publicly read back and
their SHA-256 values recorded before either scientific execution. Static
source review and compilation without running the program are permitted.
Construction/opposition agents reviewing the paper have shared context;
only separate executable authorship is blind at the code level.

## 4. Deterministic output contract

Each program prints one JSON object, json.dumps(...,sort_keys=True,
separators=(",",":")), followed by one LF. The top-level keys are:

* schema: "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/v1".
* input: object with keys m, F_m, N.
* main: object with keys tests, gcd_histogram, first_proper, test_sha256.
  The histogram is a list [g,count] sorted by g. first_proper is null or
  an object with a,b,epsilon,value,gcd. Hash every test in its prescribed
  order as ASCII "a,b,epsilon,g\n", with decimal integers and no spaces.
* factor_audit: list for p then q of objects with p, prime_trial (true),
  phi_order, alpha_order and signed_labels (number of distinct values).
* short_relations: object with keys two and three. Each has counts (list
  for p,q), sha256 (list for p,q), separators (symmetric difference size)
  and first_separator (null or a list of indices of length one or two).
  Hash sorted two-unit indices as "i\n". Hash sorted three-unit ordered
  pairs as "i,j\n". First separator is the lexicographically least element
  of the symmetric difference, represented as a JSON list.

No timestamp or environment information belongs in scientific stdout.
The two stdout files must agree byte for byte. Preserve verify output as
EXPECTED.txt and breaker output as BREAK_EXPECTED.txt. Record execution
environment, commands, exit codes, sizes and hashes separately in RUN.md.

## 5. Systematics and falsifiers

The fixed inputs and full enumeration avoid data selection after execution.
The entire rational-prime quotient avoids mistaking one vanishing embedding
for content divisibility. Independent representations address implementation
errors, while the shared specification remains a common dependency.

A recurrence identity failure, composite alleged prime, incorrect product,
missing bounded return, repeated formal label or disagreement between the
two complete outputs is a retained failure of the corresponding assertion.
No threshold is moved. A legitimate null search outcome is a negative result.
The search makes no assertion about all m or about a fast factoring method.

## 6. Runtime and scope

Run from the repository root with python3 and no command-line parameters.
The programs have no network or filesystem side effects. A 60-second process
timeout bounds each invocation. An interrupted or nonzero run is recorded
without editing frozen inputs and is not scientific confirmation.

This is a notes-only incubation audit, not a Canon probe or a promotion.
Two local programs on the same x86_64 architecture are not two-architecture
confirmation. Repository CI checks the repository changes; it is not claimed
to rerun these notes-only programs. Any later promotion needs its own gates.
