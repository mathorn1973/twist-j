# C-J-CLOSED-WORLD-READ-CAPACITY-N: pre-execution contract

**PUBLIC notes incubation; NON-CANONICAL; L1. No Canon authority.**

Owner: A. M. Thorn / closed-world-capacity session, 2026-10-23.
Reservation: https://github.com/mathorn1973/twist-j/issues/1724.
The user supplied the proposed theorem and small-horizon reconnaissance.
Those values and all proof-derived predictions below are exposed. The
second implementation is code-independent, not an unexposed discovery.

## Equation and complete carrier

Use O=Z[z]/(z^4+z^3+z^2+z+1), coefficient basis (1,z,z^2,z^3),
J=1+z^2, phi=-z^2-z^3 and phi^-1=-1-z^2-z^3. For a unit u and n>=1,
R_n(u)=O/(u^n-1), with tick T(x)=u*x. A finite reader consists of a
nonempty T-invariant subset S and a fixed f:S->{0,...,m-1}. The initial
state is uniform on S. Its complete n-word must be uniform on all m^n
words. S and f may depend on n. No counter input, extra memory, native
admission, equivariance or compatible infinite process is included.

When u^n=1, the quotient is O/(0)=O and is INFINITE. No finite uniform
measure, cardinality zero or finite feasibility verdict is assigned.

For non-torsion u=+/-z^a phi^k, k!=0, define F_d=|N(u^d-1)|,
P_d=sum_(e|d) mu(d/e) F_e, C_d=P_d/d and
W_d=sum_(e|d) mu(d/e)m^e, B_d=W_d/d. The claimed fixed-point identity
inside R_n for d|n is #Fix(T^d)=F_d, proved by ideal divisibility.

Complete feasibility means that some integer 1<=c<=floor(F_n/m^n)
admits an assignment of source cycles to target necklaces: a necklace of
least period d receives nonnegative counts y_e of e-cycles with d|e|n,
sum_e (e/d)y_e=c; total use of each e does not exceed C_e. All necklaces
must be accounted for. Grouping identical allocation patterns is allowed
only by an exactly equivalent integer argument. Fractional flows are not
certificates. The necessary primitive bound is c W_n<=P_n.

## Analytical claims frozen before computation

1. The cycle criterion is necessary and sufficient. The construction
   C_n>=m^n uses c=n: a period-d necklace receives d full n-cycles.
2. For every fixed non-torsion unit and integral m>=2, readers exist for
   all sufficiently large n exactly when m<=L_(2|k|)-1. Above that
   threshold only finitely many horizons can succeed. Phase affects
   finite counts and onset, not this exponent.
3. The explicit integer-only sufficient and exclusion onsets are exactly
   those of PROOF.md section 6. They are sufficient bounds, not minimal
   thresholds. PROOF.md supplies the all-n argument; finite checks alone
   cannot establish it.
4. For a rational probability vector in least common denominator b,
   exact n-fold product counting requires b^n to divide |S|. Uniform
   b-letter refinement supplies the converse eventual construction.
   For step J^k the least positive stride is min{k:b<L_(2k)} under this
   freely selected-support contract only.
5. Uniform all-R_n sampling is a different stronger contract requiring
   m^n|F_n. No physical universe size, sampler, Born occurrence, native-U
   implementation, preparation law, self-location or layer lift follows.

## Exact finite audit domain

- Units in order J, phi^-1, z, J^2; n=1,...,12; m=2,...,7.
- Path A: multiplication matrices constructed from the polynomial quotient,
  exact integer powers and determinant; Mobius inversion and cycle counts.
- Path B: construct an exact integral lattice normal form of u^n-1 and
  explicitly enumerate all quotient classes and multiplication orbits for
  every finite quotient through n=8. A column Hermite representative box
  with certified unimodular column operations is acceptable instead of a
  Smith coordinate box. Its index, relation-lattice equality, unique
  reductions, permutation bijectivity and orbit closure must be audited.
  No singular quotient is enumerated. All counts must match Path A.
- Decide full cycle feasibility for every finite row through n=12. A
  positive result records c and an integer assignment or the proved c=n
  construction; a negative result exhausts all possible c and assignments,
  except when an exact necessary inequality already excludes them.
- Compute the sufficient onsets for |k|=1,m=2 and |k|=2,m=2,...,6.
  Check their defining inequalities and monotonicity premises. Audit the
  determinant/primitive bound P_n>=n*m^n for each relevant unit over
  n=n_*,...,n_*+12. These finite checks audit, not replace, the proof.
- Check the Lucas stride consequences for denominators 2,5,16,256.
- Pure-rotation controls: u=z,n=1 admits m=2,...,5 on selected fixed
  points; for n>=2 with 5 not dividing n no fair m>=2 reader exists;
  for 5|n report INFINITE. Separately, a single N-cycle has no fair
  full-N-word for m>=2. A binary de Bruijn four-cycle has exact fair
  two-letter windows, guarding against an overbroad rotation prohibition.

## Exposed exact controls and independent attack

The supplied J counts for n=1,...,5 are F=(1,11,31,55,121) and
P=(1,10,30,44,120). Binary witnesses at n=2 and n=3 have support sizes
8 and 24 respectively. J at n=1 has no binary reader. An additional
pre-execution deduction is that J at n=5 has no binary reader: two
constant words and one fixed point force c divisible by 5, but c<=3.
The latter is an exposed analytical prediction, not a measured result.

A separate breaker is written from this contract and the mathematical
proof without reading verify.py, then frozen before execution/comparison.
It uses cyclotomic coefficient arithmetic rather than importing the
builder, audits fixed-point/primitive counts and Lucas onsets, and attacks
cycle feasibility by an independently written complete allocation path.
Its precise finite comparison domain and any additional exhaustive small
permutation controls are stated in its own BREAK_CONTRACT.md before pin.
No claim of independent two-architecture confirmation follows from two
programs on the same architecture.

## Freeze, execution and failure

Publish the complete accepted proof, PREREG, verifier, breaker and breaker
contract in Git with A. M. Thorn <thorn@twistj.com>. Read the published
bytes back and record their SHA-256 before either scientific execution.
Before this pin only textual review, syntax parsing and repository
integrity checks are allowed; no import of either scientific program.

Run with Python standard library, exact integers/Fraction only, no
network, floats, random data or target-dependent changes. Use fixed
PYTHONHASHSEED=0, LC_ALL=C and a maximum 2400 seconds per program. Preserve
the first stdout, stderr, exit code and timing even if a failure occurs.
An execution or integrity defect is STOP; do not repair and resume the
same frozen candidate. A mathematical mismatch is retained as a failed
claim at its exact scope. No threshold may move after the pin.

Failures: disagreement of exact paths; a false quotient/orbit certificate;
a positive reader violating primitive capacity; a false feasibility
certificate or missed exact allocation; disagreement of independent
overlapping audit rows; a counterexample to either all-n proof; a Lucas
off-by-one; an asserted uniform finite law on a singular quotient; or an
unqualified claim that rotations cannot give any finite independent window.

Deliver proof and original audit records as a notes-only draft PR. No
Canon, registry, probe, workflow, release, merge or physical status change.
