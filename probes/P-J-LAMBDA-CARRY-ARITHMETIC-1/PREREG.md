# P-J-LAMBDA-CARRY-ARITHMETIC-1: prospective arithmetic compiler audit

2026-10-29. NON-CANONICAL. One complete finite verification contract.
This probe changes no canonical claims, registries, status or frontier.
The public pre-run source pin is established by the containing commit and
reservation record before the first execution of verify.py. The prior
general-carry work had earlier local runs; they are dependencies and are
not retroactively described as prospectively registered public runs.

Public reservation: https://github.com/mathorn1973/twist-j/issues/1818.

Verified public main/activation base:
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`.
Public Canon v106 content commit:
`9242db4f040d67d9417eacd06612230b74248cff`.
The new arithmetic compiler is independently pinned inside verify.py:
SHA-256 `0e3668a7e664f572e6c6c34c49bf454e8d931e6dd05b8f2ebaf3c1b0cd761027`.
The verifier checks the bytes of the actually imported compiler before
running any baseline or new scientific checks.

## Fixed inputs and claim

The mathematical source is Public Canon v106 and the four frozen preceding
files in notes/C-J-LAMBDA-CARRY-N. verify.py contains their exact SHA-256
pins. The immutable old compiler and both old representations are rerun
as dependencies in this fresh prospective gate.

O=Z[zeta_5], lambda=1-zeta_5, J=1+zeta_5^2, J_inverse=-zeta_5-zeta_5^2.
For positive finite N, the target is multiplication by J in A_N=O/(lambda^N)
on N base-five digits, with a returned zero output buffer and returned
zero working registers. A separate archive contains N copied readouts.

This new compiler contains no 1649-state transition lookup. It encodes
each of the four bounded carry coefficients as d_j=c_j+35 in 0..70,
using three base-five cells per coefficient. It uses reversible ADDs
modulo125/625, which expand to an explicit ripple schedule, then to
H/EQ/MUL/SUM, then to the already specified exact positive pair pulses
and local permutations. A dirty output digit is allowed; prepared carry
banks, arithmetic helpers and padding cell start clean.

## Fixed equations and resource predictions

For x,y in0..4:

    h(x,y)=floor((x+y)/5)
          =sum_(k=1..4) binom(x,k)binom(y,5-k) mod5.

H adds h into an arbitrary target and returns two helper cells to zero.
Its generated cost is 208 pair pulses and380 local operations.

The ripple carry cleanup uses the final target digit z:

    c_next=h(A,4-z)+c_in[z=A].

For length L>=2 the declared ADD schedule has exact weighted counts
468(L-1)+2 pair pulses and872(L-1)+4 local operations. For L=1 it is
one SUM, hence1 pair pulse and2 local operations. The inverse reverses
logical exact permutations; physical inverse operations are lowered
using the existing positive-duration constructions.

For u=J orJ_inverse, with their four zeta coefficients u_j, compute

    S=35+sum(d_j)+sum(u_j)b; 27<=S<=323<625,
    a=S mod5; Q=floor(S/5),
    d'_0=35+d0+u0*b-a-Q,
    d'_1=35+d0+d1+(u0+u1)*b-a-2Q,
    d'_2=35+d0+d1+d2+(u0+u1+u2)*b-a-3Q,
    d'_3=Q.

The old all-length proof |c_j|<=35 bounds every reachable new carry.
New d'_j lie in0..70 and are therefore computed exactly modulo125.
The source and prior carry remain intact while the new carry is made
and erased. No branch-dependent gate selection or fresh reset is used.

Predicted generated inventories:

    multiplication: P=136917N, L=255187N+32,
    data and work:14N+22 cells; including archive:15N+22,
    complete word: P=136917N²+N,
    complete word including local gates and initial Fourier preparation:
        T=392104N²+36N.

These are counts for this concrete schedule, and upper bounds on a task
that could have a better compilation. They exclude the program clock,
routing, preparations of clean environments and protection from real
gate errors. No optimization of constants is claimed.

## Falsifiers fixed before first new execution

1. Wrong pinned dependency bytes, disagreement of the two fresh old
   representations, failed exact old primitive phase/matrix check.
2. Any H input/target mismatch or nonzero H helper after evaluation.
3. Any wrong ripple result, changed source, nonzero carry/helper, wrong
   inverse, or mismatch of fully expanded small ripple schedules.
4. S wraps modulo625, wrong residue, output coefficient outside the
   proved domain, or disagreement with any old closed carry edge.
5. Literal reverse coefficient schedule fails to restore the new carry
   bank to zero, or compiled physical primitive blocks disagree with the
   coefficient schedule on the predeclared expanded cases.
6. Any word output differs from exact O arithmetic, any full telescoping
   identity fails, any prior multiplication map hash changes.
7. Wrong generated multiplier output, nonzero workspace, failure of
   digit addition into the dirty target for either unit or either sign.
8. Archived word collision, wrong exact zero-sum count or map hash,
   or failure to reuse cleared work between successive archived ticks.
9. Generated instruction or allocated memory count exceeds the stated
   formula, or physical primitive expansion uses nonpositive duration.

Missing source/access, an execution timeout or external runner failure
is INCOMPLETE, not mathematical falsification or successful completion.
An accepted source change after a run requires a NEW named probe and a
new prospective pin, not a retry under this probe name. All first results
must be retained. Incomplete execution is disposed according to POLICY,
including ABANDONED where required, without reusing this probe name.
No rerun silently replaces a first result.

## Exact finite test set

- Fresh old verify_general.py plus check_independent.py. The first uses
  temporary fresh nonexisting certificate/program files. Their complete
  facts objects must agree. No prior stdout is accepted as a new run.
- H: both signs, all25 inputs and all5 targets,250 cases, complete
  EQ/MUL/SUM execution with two clean helpers; actual physical expansion
  inventories and positive durations. Phase correctness is checked by
  the fresh pinned baseline's exact primitive matrix audits.
- ADD: all pairs of L-digit numbers for L=1,2,3,4, counts25,625,15625,
  390625; each actual ripple schedule and its inverse. H blocks use the
  just-exhausted finite law. Source and all helpers checked every time.
- Fully EQ/MUL/SUM-expanded ADD: all pairs for L=1,2; for L=3,4 the nine
  pairs from {0,1,5^L-1}². Total668 forward/inverse cases.
- Every one of16490 edges in the two old complete carry closures,
  starting with output digit3. Execute the generated coefficient schedule
  with certified ADDs, inspect S, compare exact a,C', then execute its
  literal carry-erasing reverse. For each unit, all five input digits
  at state indices0,floor(M/2),M-1 are additionally expanded through all
  ADD and H blocks to primitive EQ/MUL/SUM,30 complete forward/cleanup
  cases. The index rule is fixed here before the new run.
- All97655 words of lengths1..7, and the same25 old fixed patterns for
  each N=8,9,12,16,32,64,128. Use the complete transition table produced
  by the just-executed new coefficient programs. Compare direct exact
  ring digits, the full O telescoping identity, inverse, and all old
  map hashes. This table is a verification cache, not a compiler input.
- Whole generated multiplier for all words through N3 and all specified
  long patterns. Whole generated E_u for the same words, both units and
  both signs, with target digits(i+2)mod5. Execute at the exhaustively
  checked ADD level, check every workspace bank at completion.
- All archived words for every seed through N5. Execute the actual full
  generated multiplier at certified ADD level on every tick, with the
  same returned workspace, an explicit SUM into each archival cell, and
  retained whole data bank. Check all map hashes and exact O root sums;
  N5 must yield3125 distinct words and120 zero sums.
- Generated primitive-weight inventories and actual allocated cells for
  N=1,2,3,5,8,32,128. The all-N extension is the proved schedule formula,
  not an extrapolation of these examples.

## Execution and output contract

Run Python3.12 or later, with no third-party packages:

    python3 probes/P-J-LAMBDA-CARRY-ARITHMETIC-1/verify.py

The runner may set PYTHONDONTWRITEBYTECODE=1; the exact required command
above does not add a -B argument.

The CLI also accepts --dependency for an explicit directory containing
the exact four pinned old files; this changes no numerical input.
The compiler CLI generates a concrete program with --length N. Adding
--pulses expands every physical operation using the frozen old lowerer.

verify.py has a predetermined540-second internal execution budget; the
repository gate retains its600-second external limit. Expected runtime
is tens of seconds to a few minutes. A budget failure reports INCOMPLETE
and must not be relabeled PASS. Scientific arithmetic uses integers and
exact fractions only. Wall-clock time is used only for the resource
guard and is omitted from deterministic stdout.

On success stdout is one deterministic JSON object. It contains source
pins, old independent equality, exact H/ADD test counts, whole new edge
hashes, multiplication and archive hashes, generated resource counts and
explicit scope flags. Failed assertions cause nonzero exit. No platform
identity, timestamps or temporary paths are included in scientific output,
so independently qualified architectures can compare it byte for byte.

The whole output must be retained for each first prospective run. This
probe does not simulate every quantum amplitude of every pulse of a
large apparatus: exact primitive matrices, exhaustive small block laws,
all reachable coefficient transitions and compositional proofs cover
that generality. The arithmetic model, physical control assumptions,
word preparation, and interpretation of a single actual outcome remain
separate questions.
