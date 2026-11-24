# Four-unit menu at the next power-of-five index

**NON-CANONICAL. NO AUTHORITY. L1. Prospective finite audit, candidate-C only.**

Candidate: C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N, round two.
Owner: A. M. Thorn / ChatGPT-Astra-20261124-Internal-Separation-R2.
Public claim #2090, existing draft PR #2092. Starting candidate head:
`0b81796c01d4bee47eceb6e451670ea0d233610b`.
Current PUBLIC basis: main `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`,
Public Canon v117. This is a new audit. The completed index-25 audit,
its preregistration, sources and receipts remain unchanged.

## Question and exact domain

For the next index **m=125 only**, derive F_m from F_0=0, F_1=1 and the
Fibonacci recurrence. For sigma=-1 then +1 set

    h=5m=625, period=2h=1250,
    N=5 F_m^2+5 sigma F_m+1.

For each N visit every tuple in this exact order:

    a=0,2,...,1248;
    b=1,3,...,1249;
    epsilon=-1,+1.

Compute gcd(N,L_a+epsilon L_b), where L_0=2, L_1=1 and L follows the
same recurrence. There are exactly 2 h^2=781250 tests on each side and
1562500 in total. Modular sequence arithmetic is equivalent and permitted.
The family, order and bounds use no prime factors or previously inspected
outcome at m=125. No other index is part of this audit.

The companion paper question is whether this entire menu has exactly the
same prime-divisibility separation as all sums of at most four signed units
in Z[zeta_5]. The program does not assume or verify that unbounded theorem.
Its output is the exact finite menu. Any claimed completeness will retain
its separate paper proof and internal-review status.

## Reported output

Emit one JSON document using Python json.dumps(data, indent=2,
sort_keys=True), followed by one newline. Integers denoting N, gcd values
and support atoms are decimal strings. Counts, indices, signs and other
small fields are JSON integers. No timing, architecture or nondeterministic
field is written to scientific stdout.

The top-level object has exactly:

    audit: "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/R2-M125"
    m: 125
    h: 625
    period: 1250
    cases: [the sigma=-1 object, the sigma=+1 object]

Each case object has exactly these fields:

    sigma: -1 or +1
    N: decimal string
    tests: 781250
    histogram: [[gcd decimal string, count], ...], sorted by integer gcd
    first_proper: null, or {a, b, epsilon, gcd: decimal string}
    proper_tests: sum of counts with 1 < gcd < N
    support_atoms: sorted decimal strings of the exact blocks below

For each distinct observed gcd d, in ascending numerical order, define

    s_d = gcd(N, d^(bit_length(N))).

This can be calculated with modular exponentiation. Start with [N]. For
each s_d split each current block B into gcd(B,s_d) and B/gcd(B,s_d),
discarding factors 1; leave B unchanged when the gcd is 1 or B. Sort
the final blocks increasingly. These are support atoms for this fixed menu,
not claims of primality or complete factorization. Saturation preserves
every original prime-power multiplicity: its exponent is at least every
prime valuation of N. Thus every s_d is a unitary divisor of N.

Assert that histogram counts total 781250, the first proper tuple agrees
with its recorded gcd, atoms are greater than one and pairwise coprime,
their product is N, and gcd(atom,s_d) is either 1 or the whole atom for
every atom and every distinct observed d. A side with no proper gcd is
a valid negative result, with first_proper null and support_atoms [N].
No asserted number of proper results, gcd value or number of atoms is
specified in advance.

## Two implementations and prospective freeze

The primary source verify.py uses forward Fibonacci/Lucas recurrences.
The separately authored break.py uses powers of the integral matrix
[[1,1],[1,0]] to obtain F_m and the Lucas traces. Both use only the Python
standard library and exact integers. They share this public mathematical
specification and output schema, but neither author reads the other
implementation until both source files are frozen by SHA-256.

Before either scientific execution, commit and push this preregistration
and both accepted sources together and read all three back byte-for-byte
through the GitHub connector. Record that immutable commit and digests.
Static compilation and code review are allowed before execution. A source
defect discovered before the public pin may be corrected before freezing;
after pinning it requires an explicit disposition and new audit identifier.

Run from the repository root using the default current Python interpreter,
with PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0, LC_ALL=C and TZ=UTC:

    python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/round2/verify.py
    python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/round2/break.py

Each process has a 600-second wall-time limit. Write exact stdout to the
separate committed EXPECTED.txt and BREAK_EXPECTED.txt only after a
completed run. Record exit codes, stderr, byte counts and SHA-256 in RUN.md.
Timeout or source failure is retained as an incomplete audit; it never
permits enlarging bounds or silently changing sources.

## Falsifiers, status and limits

An assertion failure, nonempty stderr, nonzero exit, differing full JSON
outputs or failed public source readback stops acceptance. Preserve the
failure and its exact scope. Negative scientific outputs remain valid.

These notes programs are not selected by ordinary repository scientific
replay. Passing two architecture policy jobs alone is not two-architecture
execution of this audit. Any local finite evidence remains candidate-C at
its recorded architecture scope. Independently authored source is a code
comparison; same-session paper review is not external peer review.

No prime factorization is supplied as input, no primality is asserted for
an atom, and no larger index, new threshold, universal arity conclusion,
Canon change, physical interpretation or RH conclusion belongs to this run.
