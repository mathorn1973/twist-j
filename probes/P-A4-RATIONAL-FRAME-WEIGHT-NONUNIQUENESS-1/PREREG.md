# P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1 preregistration

**FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED.**
Author: A. M. Thorn. Date: 2026-09-07.
Public lock: [#875](https://github.com/mathorn1973/twist-j/issues/875).
Branch: `probe/P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1`.

## Authority and custody

Basis: ACTIVE Public Canon v79. Public `main` at claim time is
`a51df34fe1f1f433062faeb18f5e03fd0a8082b2`; `STATUS.md` declares content
commit `48ede94165472e2d77896a7c20ddb3c567f3bcc1`, CANON SHA-256
`025b07fe39ec4ab857a50adf467acc640334a1ea0cb87e8f9500b90948896764`, and
516701 Canon bytes. The declared content commit and `canon-v79` tag are
ancestors of public main. The current x86_64 and aarch64 architecture jobs
and aggregate `check` on main are green.

Before claiming the identifier the session searched open issues and pull
requests, the probe/registry namespace, and both pages of remote branches.
No live `TERNARY-VALUATION`, `NONQUADRATIC-FRAME-WEIGHT`, or equivalent claim
lane was found. The old `claude/decoder-physical-reading-00xa91` branch is
352 commits behind main and contains unrelated generation/QS/TM drafts.
`maintenance/reading-family-discipline` is policy-only and 404 commits behind.
No sealed or abandoned probe is resumed.

The theorem and its proof were known in non-canonical incubation before this
public pin. This public probe is fresh custody. The accepted verifier is newly
pinned here and must not be executed before the commit containing PREREG.md,
PROOF.md and verify.py is pushed and read back from GitHub. Do not amend,
rebase, squash, rename, reuse, or force-push this identifier after the pin.

## Field 1: equation, claim and falsifier

Let

```text
L = A4 = {v in Z^5 : sum_i v_i = 0}
V = L tensor_Z Q
q(v) = sum_i v_i^2
```

and let a ray be a one-dimensional rational subspace `[v]` with `v != 0`.
A complete frame is any four mutually orthogonal rational rays spanning V.

For nonzero rational `a = 3^k u`, where numerator and denominator of `u` are
prime to 3, define

```text
h(a) = 0   if k is even
     = -1  if k is odd and u = 1 mod 3
     = +1  if k is odd and u = 2 mod 3.
```

Put `H([v]) = h(q(v))` and, for rational `t`,

```text
w_t([v]) = 1/4 + t H([v]).
```

The frozen theorem target is:

1. `H` is well-defined on rational rays.
2. For every rational orthogonal complete frame `(v_1,...,v_4)` of V,
   `sum_i H([v_i]) = 0` exactly.
3. Therefore every rational `|t| <= 1/4` gives a nonnegative normalized frame
   weight `w_t`; every `|t| < 1/4` is uniformly strictly positive.
4. On the 30-ray inner Cl(4) set consisting of the ten A4 root rays of norm 2,
   fifteen primitive rays of norm 4, and five simplex rays of norm 20,
   `H=0`, hence every `w_t=1/4`.
5. In the frozen plane `U_012`, with

```text
d1=( 2,-1,-1, 0, 0)   r1=(0, 1,-1,0,0)
d2=(-1, 2,-1, 0, 0)   r2=(1, 0,-1,0,0)
d3=(-1,-1, 2, 0, 0)   r3=(1,-1, 0,0,0),
```

   the projector covers are equal,
   `sum_m P_d_m = sum_m P_r_m = (3/2) P_U`, while
   `D(w_t) = sum_m w_t(d_m) - sum_m w_t(r_m) = 3t`.
   Thus every nonzero `t` is not representable as `tr(W P_v)` by one symmetric
   operator W, even without demanding `W >= 0`.

**Scientific conclusion at this scope:** positivity plus noncontextual
additivity over all complete rational orthogonal records do **not** force
quadratic reading on rational A4 rays.

Falsifier: any rational rescaling changing H; any rational orthogonal frame
with nonzero H-sum; failure of positivity or frame normalization in the stated
t-range; failure of the frozen cover equality or `D=3t`; or an exact common
quadratic representation of a nonzero-t member.

## Field 2: accepted verifier and finite audit domain

Command from repository root:

```text
python3 probes/P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1/verify.py
```

The verifier uses Python standard library only and exact integer/Fraction
arithmetic. It audits, without proving by enumeration:

- square invariance of h on a frozen rational sample;
- the binary residue identity on a frozen exhaustive rational pair set;
- exact orthogonality, determinant law and H-sum on 2000 deterministic
  rational Gram-Schmidt frames;
- the 30 inner rays and their H=0 values;
- the six-ray equal-projector cover and `D=3t` family;
- nonnegative and strictly positive frame normalization at frozen t values;
- one determinant-square-class out-of-domain control where the H-sum is -4.

Universal conclusions rest on PROOF.md. The finite verifier is an audit.
No external dataset, numerical tolerance, fitted parameter, or physical input
is used.

## Field 3: carrier and provenance

The carrier is exactly the rational A4 support above, action layer L4. There
is no measured data and no dependency on an attached incubation bundle.
The public proof is self-contained and restates every mathematical definition
needed by verify.py.

This probe may cite the current public reading-family discipline and current
owner-adopted quadratic registration only as scope boundaries. It does not
modify or reinterpret old probe bytes.

## Field 4: systematics and controls

All scientific assertions are exact. Use deterministic iteration order,
`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`, exit 0, empty stderr, and a 600-second local
ceiling. No floating point is admitted.

Mandatory controls:

- projective square-rescaling invariance;
- determinant identity `prod q(v_i) = 5(det C)^2` on generated A4 frames;
- the standard determinant-one Q^4 orthogonal frame of four norm-3 vectors,
  which must give H-sum -4 and therefore demonstrate that the A4 discriminant
  step is essential rather than a tautology.

## Field 5: threshold and disposition

Mismatch threshold is zero. A completed formal gate passes only on exact stdout,
exit code 0 and empty stderr. Any theorem counterexample is scientific failure
and is preserved. Pin mismatch, timeout, nonzero exit, source defect, or
unexpected platform-dependent bytes are integrity STOP, not scientific
counterevidence.

After the first completed run, `EXPECTED.txt`, `RUN.md` and `RESULT.md` are
added. The required GitHub x86_64 and aarch64 jobs must independently match the
same committed `EXPECTED.txt` byte for byte. A theorem-grade written proof may
earn T; the verifier then audits it.

## Field 6: layer and explicit nonclaims

Scope is **L4 only**: rational support, orthogonal records and scalar weights.
No L4-to-L5 occurrence, L4-to-L6 physical probability, or L1-to-L5 apparatus
gate is asserted.

This probe does **not** claim:

- that J, quantum mechanics or the owner-adopted quadratic decoder is false;
- that the displayed nonquadratic weights are physically realized readings;
- uniqueness or completeness of the physical decoder family;
- a physical effect, apparatus, ready state, pointer, occurrence law, sampling
  law, randomness assumption, post-state instrument or L6 measure;
- a contradiction with real Gleason theorems or with continuity-based results.

Under public reading-family discipline, decoder nonuniqueness is not itself a
physical falsifier unless uniqueness was the frozen claim. The intended public
interpretation is therefore narrow: this theorem closes one attempted
**uniqueness derivation** and leaves the explicitly chosen quadratic reading
available as a declared reading branch.