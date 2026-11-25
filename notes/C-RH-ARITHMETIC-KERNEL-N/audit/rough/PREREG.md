# C-RH-ARITHMETIC-KERNEL-N, rough-support and least-prime subtask

NON-CANONICAL. No authority. Classical signed arithmetic only. No Git write.

Let w(d)=(-2)^omega(d) on squarefree split support, zero otherwise. Let
R(X)=sum_(d^3>X^2,d<=X) w(d) S_chi(floor(X/d)). Freeze the rough slice B(X)
by P^-(d)^3>X, taking the least prime of 1 as infinity. Let H(X)=R(X)-B(X).

Paper targets before computation:
1. Establish an exact quotient formula for B using only split primes above
   X^(2/3) and unordered pairs of distinct split primes each above X^(1/3).
   Establish H by the exact least-split-prime decomposition at the same strict
   boundary; state each argument and moving cutoff.
2. Derive B(X) ~ -(1-log 2) L(1,chi_5) X/log X from the classical fixed modulus
   prime number theorem. For each fixed quotient q compute the semiprime
   constant via sum of reciprocals of split primes. Give a tail estimate
   O(X/(Q log X)) with a uniform constant after quotient truncation at Q,
   remaining in the signed bounded residue kernel. An unsigned harmonic
   truncation does not qualify.
3. Use an unconditional classical Mertens bound and the already established
   absolutely summable Dirichlet unit to compare H with -B at the leading
   scale. Then establish an all-large-window lower bound for Q_H(Y) using H's
   positive part. The conclusion concerns this precise separated-bound route.
   The upper bound for Q_R remains the target.
4. If run, use a single exact Python integer check for every N through 8192
   using an independent trial-prime factorization and a second prime/semiprime
   quotient enumeration. Compare B, H and R through exact support identities,
   including cutoff equalities. Fixed endpoint control: N=11^3 tests whether
   an equality in the least-prime rule wrongly enters B. Use a fixture
   d=11*19 with N=1000 to reject omitting the d^3>N^2 cut because this d lies
   below the tail and has nonzero residue weight. Independently resolve the
   isolated fixture at both boundaries. Freeze source by SHA-256 before run.
   Any run is auxiliary candidate-C on one architecture, no asymptotic inference.
