# P-TM-FOURPHASE-HULL-NONDESCENT-1 preregistration

```text
PREREGISTERED / UNRUN / RESULT-EXPOSED / PROOF-FIRST /
NO VERIFIER EXECUTION / NO SCIENTIFIC RESULT
```

Public claim lock: `#781`. The lock was opened before the public branch,
probe path, pin commit, or formal execution. The collision readback passed.

```text
probe:         P-TM-FOURPHASE-HULL-NONDESCENT-1
claim_id:      TM-FOURPHASE-HULL-NONDESCENT
branch:        probe/P-TM-FOURPHASE-HULL-NONDESCENT-1
path:          probes/P-TM-FOURPHASE-HULL-NONDESCENT-1/
owner:         A. M. Thorn
action layer:  L5 exact symbolic stream only
target:        candidate T, unregistered until a separate Canon fold
```

This pin changes no active Canon byte and earns no status. At this public pin
the directory contains exactly `PREREG.md` and `verify.py`. `EXPECTED.txt`,
`RUN.md`, and `RESULT.md` do not exist until after the first authorized formal
execution of the public pin.

## 0. Authority, currency, and pre-pin STOP

This preregistration is pinned to this fresh public readback:

```text
STATE:              ACTIVE
CANON:              Public Canon v74
AUTHORITY:          mathorn1973/twist-j main
TAG:                canon-v74
TAG_OBJECT:         796b09aef958a9021b93cff0df7f300ef95f5337
ACTIVATION_COMMIT:  05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT:     2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:       2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:        389246
BASE_MAIN:          8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
ACTION_LAYER:       L5 stream
```

The annotated tag resolves to the activation commit, both the activation and
content commits are ancestors of `BASE_MAIN`, the declared Canon hash and byte
count match, `canon/SHA256SUMS` is 5 of 5 OK, and the policy and Canon checks
pass.

At lock time a full no-base reproduction sweep had an unrelated baseline
failure: `reproduce/status-separation/verify.py` still expects 23 reproduction
directories while post-v74 `main` contains 24 after adding
`PHOTON-Z5-EXACT-HEATBATH-KERNEL`. This does not change any theorem below, but
it must be repaired or explicitly disposed before a later Canon-changing v75
fold. A changed authority tuple, a collision, or an unresolved required check
at actual pin time is STOP and requires a fresh readback.

## 1. Collision and lineage boundary

At `BASE_MAIN`, the exact proposed probe and claim names are absent from open
and closed issues and pull requests, remote heads, `probes/`, the Registry,
the Frontier, the Canon, object locks, and claim locks. This scan must be
repeated immediately before opening claim-lock issue #781 and before pinning;
both scans passed.

The following public objects are adjacent but disjoint:

1. `RAMIFIED-TM-LIFT [T]` owns the forward L1 word
   `Theta_n=2^s_2(n)` and its binary sign quotient. It does not own a
   two-sided four-symbol stream carrier or a descent theorem on that carrier.
2. `TM-SHEET-SYNCHRONIZING-GRAPH [T]`, clause G8, reads only the square of the
   phase and explicitly claims no recovery of the four-phase value.
3. `TM-SYM2-REVERSAL-CLOSURE [T]` is a different L5 selector carrier and a
   different reversal action.
4. `TM-ENTROPY-ZERO [T]` owns the binary Thue--Morse stream complexity, not a
   four-symbol lift or its one-block reversors.
5. `P-TM-CORR-ZEROS-1` concerns binary correlation zeros and does not own the
   object or conclusion below.

No public `REQUIRES` edge from the L1 `RAMIFIED-TM-LIFT` is claimed here. The
formula `2^s_2(n)` is proved again on the distinguished forward word. Treating
the new two-sided carrier as a registered physical realization of the L1
phase would be a separate L1-to-L5 bridge and would require its own named
gate.

## 2. Result exposure and evidentiary firewall

The conclusion, proof skeleton, and prototype computations were known before
this public preregistration from the non-authoritative incubation candidate
`C-FOURPHASE-HULL-NONDESCENT-2`. That candidate had one local x86_64 run and a
same-session auxiliary attack. Its code, output, hashes, run record, and
status carry no public evidence credit and are not imported.

This is therefore a result-exposed, proof-first probe. The public
`verify.py` is an accepted exact audit authored with knowledge of the expected
mathematics. It was not executed or imported before this pin.
There is no blind-breaker claim. The former auxiliary attack has instead been
used to harden the accepted verifier.

## 3. Exact carriers and notation

Work in `Z/4Z` and `F_5^x`. Define the constant-length substitution

```text
tau(a)       = a (a+1) mod 4,
mu(0)        = 01,
mu(1)        = 10.
```

Let `u` be the one-sided fixed point of `tau` beginning with zero. Define
`K_TM4`, written mathematically as `K_{TM,4}`, to be the two-sided subshift
whose language is the set of all finite factors of `u`. Define `K_TM` in the
same way from the binary Thue--Morse fixed point.

The symbol `K_TM4` is load-bearing. It is not the Canon checkpoint sheet
`X_4`, a graph called `K_4`, or a registered physical carrier.

For `r in K_TM4`, `x in K_TM`, `c in Z/4Z`, and a nonempty finite word `w`,
put

```text
(S r)_m       = r_(m+1),
pi(r)_m       = r_m mod 2,
A_c(r)_m      = r_m+c mod 4,
Phi(r)        = 2^(r_0) mod 5,
Phi_L(w)      = 2^(w_0) mod 5,
q(1)=q(4)     = 0,
q(2)=q(3)     = 1,
rho(x)_m      = x_(-m-1),
iota(r)_m     = -r_(-m-1) mod 4.
```

For a letter map `g:Z/4Z -> Z/4Z`, define the one-block reversal map

```text
R_g(r)_m = g(r_(-m-1)).
```

The center of every reversal is the gap between coordinates `-1` and `0`.
The phrase one-block does not include any higher-block sliding code.

## 4. Written proof

### S1. Fixed point and exact binary factor

The substitution gives

```text
u_(2n)   = u_n,
u_(2n+1) = u_n+1 mod 4.
```

The same recursion and initial value characterize `s_2(n) mod 4`, hence

```text
u_n = s_2(n) mod 4                         for every n>=0.
```

On each letter, `pi tau=mu pi`, so `pi(K_TM4)` is contained in `K_TM`. For
the reverse inclusion, every centered block of a point of `K_TM` is a factor
of `pi(u)` and therefore has a factor lift in the language of `K_TM4`.
Primitivity of `tau` gives a two-sided extension of every such factor.
For a fixed `x in K_TM`, let `C_N` be the nonempty compact cylinder of points
`r in K_TM4` whose binary projection agrees with `x` on `[-N,N]`. The
`C_N` are nested. Compactness gives a point in their intersection, whose
projection is `x`. Therefore

```text
pi(K_TM4)=K_TM.
```

On the distinguished forward word this independently recovers

```text
Phi(S^n u)=2^s_2(n) mod 5.
```

This equality is an arithmetic compatibility, not adoption of `K_TM4` as a
physical phase carrier.

### S2. Rotation closure, elementarily

For every letter and every `c`,

```text
tau A_c = A_c tau.
```

Every residue `c` occurs as a letter in `tau^3(0)`. If a word `w` occurs in
`tau^n(0)`, then `A_c w` occurs in

```text
A_c tau^n(0)=tau^n(c),
```

and `tau^n(c)` occurs as a block of `tau^(n+3)(0)`. Thus `A_c w` is again in
the language. Applying `A_(-c)` gives equality, so every `A_c` preserves the
full two-sided hull. This is an all-length proof, not a prefix inference.

### S3. Reversal closure

For a finite word define `iota(w)=-reverse(w)` letterwise modulo four. A
direct one-letter calculation gives

```text
iota tau = A_(-1) tau iota.
```

Reversal changes concatenation order on both sides, so the one-letter
identity extends to every finite word. Induction and S2 give

```text
iota(tau^n(0))=A_(-n)(tau^n(0)).
```

Every finite factor lies in some `tau^n(0)`. Its `iota` image lies in the
rotated word on the right, and S2 puts that image back in the language.
Hence `iota` preserves `K_TM4` at every length.

### S4. Exact two- and three-letter languages

The finite certificate `tau^7(0)` contains all sixteen adjacent pairs, so

```text
L_2=(Z/4Z)^2.
```

Every length-three occurrence starts at one of the two positions inside a
substituted adjacent pair. Conversely every adjacent pair occurs and supplies
both positions. Therefore the exact three-letter language is

```text
L_3 = {(a,a+1,b), (a+1,b,b+1) : a,b in Z/4Z},
```

with all entries modulo four. It has exactly 28 words. This finite exact
certificate is sufficient to reject every excluded one-block map below.
Every surviving map is separately proved on the full language by S2 and S3.

## 5. Frozen theorem package

All clauses have proposed status `T` at exact L5 symbolic-stream scope. The
public pin itself earns no result.

### N1. The four-phase read does not descend

The rotation `A_2` preserves `K_TM4`, commutes with the shift, and satisfies

```text
pi A_2=pi,                    Phi(A_2 r)=-Phi(r).
```

Thus no map of sets `f:K_TM -> F_5^x` can satisfy

```text
f(pi(r))=Phi(r)               for every r in K_TM4.
```

This is stronger than the nonexistence of a continuous factor: the phase read
is not constant on the fibers of `pi` at all.

### N2. The binary quotient does descend

For every `r in K_TM4`,

```text
q(Phi(r))=r_0 mod 2=(pi(r))_0.
```

The sign-blind `C_2` quotient therefore descends even though the full
four-phase value does not.

### N3. Fiber sharpness at every finite length

Let `L>=1` and let `b` be any length-`L` block of `K_TM`. S1 supplies a
length-`L` lift `w` in the language of `K_TM4`; S2 supplies `A_2 w`, with the
same binary projection and opposite read. The first symbol of every lift is
either `b_0` or `b_0+2`. Hence

```text
{Phi_L(w) : w is a K_TM4 block and pi(w)=b}
  = {2^(b_0), -2^(b_0)} in F_5^x.
```

This holds for every finite length. No finite cutoff is part of the theorem.

### N4. The normalized reversal lift

The operator `iota` preserves `K_TM4` by S3. Direct composition of its exact
index map `m -> -m-1` and value map `a -> -a` gives

```text
iota^2=id,
iota S iota=S^(-1),
pi iota=rho pi,
Phi(iota r)=Phi(S^(-1)r)^(-1).
```

The last line is literal multiplier inversion for the normalized choice with
no global phase rotation.

### N5. Complete classification in three named one-block classes

For `R_g(r)_m=g(r_(-m-1))`:

1. Among the eight affine bijections `g(x)=eps*x+c`, with
   `eps in {+1,-1}` and `c in Z/4Z`, exactly four preserve `K_TM4`: all and
   only `g(x)=-x+c`.
2. Among the sixteen arbitrary parity-preserving maps
   `g(x) mod 2=x mod 2`, not assumed bijective, exactly two preserve
   `K_TM4`: `g(x)=-x` and `g(x)=-x+2`. These and only these survivors cover
   the binary reversal `rho` in this class.
3. Among all 24 permutations of the four-letter alphabet, exactly four
   preserve `K_TM4`: again `g(x)=-x+c`.

Every excluded map sends an explicit word of the exact `L_3` outside `L_3`.
Every survivor equals `A_c iota` and therefore preserves the entire hull by
S2 and S3. For the four survivors,

```text
pi R_(-x+c)=rho pi             when c is even,
pi R_(-x+c)=N rho pi           when c is odd,

Phi(R_(-x+c)r)=2^c Phi(S^(-1)r)^(-1).
```

Thus slope `-1` is forced in each of the three declared one-block classes.
The phase is inverted up to the global rotation `2^c`. Literal inversion is
the normalized `c=0` case. The `c=2` survivor adds a global sign, and odd `c`
also complements the binary projection. No claim is made about higher-block
reversal covers or arbitrary sliding codes.

## 6. Six frozen fields

```text
EQUATION     S1-S4 and N1-N5 exactly as written. The primary theorem is the
             set-theoretic non-descent of Phi through pi. The same package
             includes the descending C2 quotient, all-length finite-block
             fiber sharpness, the normalized reversor, and the complete
             three-class one-block classification.

CODE         probes/P-TM-FOURPHASE-HULL-NONDESCENT-1/verify.py
             SHA256: a730c1abbe6868a471aa07cf6395570378d1005dfc5f42c757d92daa9be16509
             BYTES:  9207
             Python standard library only; exact integers; deterministic;
             no arguments, files, network, subprocesses, floats, randomness,
             clocks, or environment-dependent scientific input.

CARRIER      K_TM4 and K_TM as the exact two-sided substitution languages;
             Z/4Z, F_5^x, the shift, pi, A_c, Phi, Phi_L, rho, iota, and the
             three finite one-block map classes above. No external data.

SYSTEMATICS  The all-length conclusions rest on the written substitution,
             compactness, rotation, and reversal proofs, not on a finite
             prefix. The exact L_3 certificate closes only the finite
             one-block classification. The bounded language scan in the
             verifier is a consistency audit and earns no unbounded scope.
             Higher-block maps, physical carrier selection, and every L6
             measure statement remain outside the admitted class.

THRESHOLD    FIRE on any exact counterexample to S1-S4 or N1-N5, any wrong
             exact language or classification count, an excluded one-block
             map without an L_3 witness, a listed survivor that fails full
             symbolic closure, or a phase/projection formula failure.
             Integrity, pin, architecture, or baseline-check defects are STOP
             and yield no scientific conclusion.

LAYER        L5 exact symbolic stream only. No L1 physical realization, L2
             manifold, L3 boundary, L4 apparatus support, L6 measure,
             decoder, clock, causal, probability, or experimental claim.
```

## 7. Accepted verifier and gate protocol

`verify.py` audits:

1. the substitution, binary factor, rotations, and fixed-point recursion;
2. the exact 16-pair and 28-triple language certificates;
3. non-descent, the descending quotient, and the two-valued first-letter
   fibers;
4. exact composition of the affine index/value operators for `iota^2` and
   `iota S iota=S^(-1)`, plus projection and phase inversion;
5. all three complete one-block classifications, explicit witnesses for
   every exclusion, projection parity, and inversion up to `2^c`;
6. a labeled bounded consistency scan that is not used as the proof of an
   all-length statement.

The verifier is result-exposed and confirmatory. It is not a blind or
independent construction. No auxiliary breaker is part of this public probe.

Before the first formal execution:

1. open the dedicated claim-lock issue and replace
   `#781`;
2. repeat the authority and collision readback;
3. resolve every pre-pin STOP;
4. finalize and hash `PREREG.md` and `verify.py`;
5. commit only those two files on the dedicated branch, push without amend or
   force-push, and read back the exact commit, SHA-256 values, byte counts,
   and Git blobs from the public remote;
6. record the public pin and formal execution count zero on the issue.

Only then may one authorized first formal execution run from a clean detached
checkout of the exact public pin in the sanitized environment

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 probes/P-TM-FOURPHASE-HULL-NONDESCENT-1/verify.py
```

A completed run requires exit zero, empty stderr, every declared PASS line,
and the terminal `RESULT 6/6 ALL PASS`. Its exact stdout becomes
`EXPECTED.txt`; neutral metadata becomes `RUN.md`; the scientific disposition
becomes `RESULT.md`. The required GitHub x86_64 and aarch64 jobs must execute
the same verifier hash and reproduce the same committed stdout byte for byte.
The aggregate `check` must pass before merge. No earlier incubation run or
architecture record can satisfy this gate.

## 8. Scope firewall

Nothing in this probe:

- identifies the registered selector coefficient `2` with a physical phase;
- makes `K_TM4` the unique, canonical, or physical lift of `K_TM`;
- strengthens G8 into a statement about every possible four-phase extension;
- classifies higher-block factor maps or reversors;
- reconstructs a counter, checkpoint, clock, decoder, apparatus, event,
  measure, causal arrow, or experimental outcome;
- supplies a physical time-reversal theorem or CPT operator;
- changes the Canon, Registry, Frontier, dependencies, gates, scheduler, or
  Public Canon v74 release.

A later v75 fold may register only the exact L5 theorem that survives this
public probe. Any adoption, cross-layer dependency, or physical reading is a
separate named and gated transaction.
