# Audit addendum and corrections: the TWIST-J Photon / Fermat disposition, 2026-07-27

```
CORRECTION NOTICE, added 2026-07-27 after the owner's isotropy-6 disposition.
Kept intact as the record. Section 2 C2 of this document is SUPERSEDED:
  C6  "the whole propagator is constant in modulus, which leaves no channel" is
      WRONG as a principle. The free Schroedinger kernel has constant modulus and
      is a real propagator. The A3 computation stands; its reading does not. The
      surviving kill is LOCALITY (instantaneous full support, no time symbol, no
      characteristic cone), not modulus.
  C7  the F_5 quadratic path sum IS the finite-field free Gauss kernel, term for
      term. It succeeded at being the massive free kernel, a different object.
  C8  the F_5 null cone is a Chevalley-Warning artifact: every nondegenerate
      ternary form over F_5 has exactly 25 zeros. The premise of the earlier
      kill 2 is retired, not only its wording.
See claude/AUDIT-ADDENDUM-3-ISOTROPY6_2026-07-27.md.
```

```
SESSION:   audit-external-photon-fermat-note-2026-07-27, addendum
STATUS:    AUDIT ARITHMETIC AND SELF CORRECTION. No candidate, no prereg, no
           freeze, no promotion. No authority. Incubation lane.
SUBJECT:   the owner's disposition bundle
           TWISTJ_Photon_Fermat_Disposition_Bundle_2026-07-27.zip,
           sha256 bbe772cdfb98b1cda0ec70d05ff6e2c75d1209f0d42f143bab4f8ca0e0f5c674,
           received and verified 2026-07-27; and four corrections to
           claude/AUDIT-EXTERNAL-PHOTON-FERMAT-NOTE_2026-07-27.md, three of them
           the owner's and one of them mine.
VERDICT:   The disposition is accepted. Four of my statements were wrong or too
           strong and are corrected below. None of the corrections changes the
           bottom line, and one of them, the amplitude escape, is now closed by a
           new exact computation rather than by the argument I originally gave.
           The main open obligation now has its first frozen number.
```

## 1. The bundle verifies. Section 8 of the original audit is discharged

Every claimed pin reproduces here, byte for byte.

```
bundle                                    bbe772cd...    as claimed
prereg                                    3e0f9585...    as claimed
original verifier                         80c182de...    as claimed
original stdout (delivered)               2b99a12a...    as claimed
original stdout (owner reproduced)        2b99a12a...    identical
break_photon_fermat.py                    2d49e5a7...    identical to mine
break stdout (owner reproduced)           e6d546f1...    identical to mine
both reproduced stderr files              e3b0c442...    the empty-file hash
```

Third independent run of the original verifier in this session, x86_64,
Python 3.11.15, `LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC`, 402 bytes of stdout,
empty stderr, exit 0, **byte identical** to the delivered `photon_fermat_candidate_stdout.txt`.
That is now three runs across two Python minor versions, all on x86_64. It is not
a two-architecture pin, and nobody should quote it as one.

The original audit's section 8 ("the note is not reproducible as delivered") is
withdrawn. It was true of what had been delivered at the time and is false now.

## 2. Corrections to my audit

### C1. "The only canonical option is the zero form" was too strong. Accepted

The owner is right. The restriction of `G = 5 I_4 - 1 1^T` to `ker(Tr_4)` is
divisible by 5 as an integral form, and the divided form is canonical, integral
and nondegenerate mod 5. Verified exactly:

```
G|ker (basis (1,-1,0,0),(0,1,-1,0),(0,0,1,-1))  =  [[10,-5,0],[-5,10,-5],[0,-5,10]]
q_div = (1/5) G|ker                             =  [[2,-1,0],[-1,2,-1],[0,-1,2]]   (A_3 Cartan)
q_div(v,w) = v . w  exactly on ker(Tr_4)
det q_div = 4,  4 mod 5 != 0                    NONDEGENERATE
```

So the correct statement is the owner's three-way split, not my two-way one:

```
raw G mod 5      zero form, vacuous
divided G/5      canonical, integral, nondegenerate      <- I missed this branch
other            externally chosen, needs its own derivation
```

**But the conclusion is unchanged, and now for a stronger reason.** Ternary
quadratic forms over `F_5` are classified by the square class of the
discriminant, and `det q_div = 4 = 2^2` is a square, exactly like `det I_3 = 1`.
An explicit isometry was found by search, basis `((0,1,2),(1,1,2),(1,2,2))`:

```
q_div  is F_5 ISOMETRIC to  x^2 + y^2 + z^2.
```

The section 4 analysis of the original audit therefore transfers to the divided
canonical form verbatim, and it does. Reproduced on `q_div` directly, for
`mus = (1,1,1)` and `(1,2,4,3,1)`: the localization is exact, the null cone has
exactly 25 points, and exactly one distinct amplitude occurs across them. The
owner's own numbers, reproduced independently.

My kill 1 is downgraded from "the canonical carrier makes this vacuous" to "one
of the three branches makes this vacuous, and the other two land in kill 2".

### C2. "Direction blind" is not by itself a falsifier. Accepted, and the falsifier is restated

The owner is right in principle. An isotropic propagator should be direction
blind in phase, and in a normal field theory the physical content can sit in the
support, the determinant, the polarization transport or the boundary condition
rather than in the endpoint phase. My original wording implied that constancy on
the light cone is by itself fatal. It is not.

For this particular object it is fatal anyway, and here is the exact reason,
which is a new computation and not the argument I originally gave.

```
For every one of the 125 endpoints b, and for the canonical q_div, the standard
form, and mixed weights alike:

  K_N conj(K_N)        one single value      (15625 for N = 3, mu = 1)
  field norm to Q      one single integer    (244140625 for N = 3, mu = 1)
  support              125 of 125            no zeros anywhere
```

The propagator is **constant in modulus on the whole endpoint space**, not merely
on the null cone. There is no support structure, no determinant variation, no
amplitude falloff, no zero set. The escape route the owner correctly identified
in general does not exist for this object, because there is nothing for a
selection rule to ride on other than the phase, and the phase has been shown to
be direction blind on the cone.

Restated falsifier, and this is the form that should be quoted:

```
The F_5 quadratic path sum is uniformly distributed in modulus over every
endpoint and carries direction information only in a phase that is constant on
the null branch. It therefore has no channel, of any kind, in which a Fermat
selection could be carried. [F] for the photon reading. The lemma itself
remains [T].
```

### C3. "The dictionary must be non-metric" was too broad. Accepted

What was falsified is the pure arrival-time phase `A(gamma) = j^{c T(gamma)}`,
in 20 of 20 exact cases. That does not kill metric content in general, and the
owner's reformulation is the correct one. Adopted verbatim:

```
The dictionary must not be a pure word metric, a shortest-path cost, or the
arrival time alone in the exponent. A surviving mechanism may be metric in the
principal symbol of a wave operator, provided it carries additional structure:
connection or holonomy, orientation, polarization, time transfer, and support on
the characteristic cone.
```

### C4. My "definitional repair" of Section 6 is withdrawn. My error

I claimed the note's `delta_m` was defined as a maximal angular gap and needed
repair to a covering radius. The delivered note, line 432, already reads
"let `delta_m` be its angular covering radius", and lines 458 to 461 give
precisely the support-function argument
(`h_{K_m}(w) >= cos delta_m` for every unit `w`, hence `(cos delta_m) B` is
contained in `K_m`). I audited a phrase from the summary message instead of the
artifact. The note's convex lemma is correct as written and needs no repair.

What survives from that section of my audit is only the application point, which
the owner states more sharply than I did: longer words over one fixed alphabet
are not a new local alphabet, so `D_m` never actually varies, and the lemma,
though true, has no realization. Adopted.

### C5. Scope of the pinned computation. My omission

The pinned G2 and its verifier run over **one dimensional** paths, `x_k in F_5`,
1 to 4 steps, all nonzero weights, all endpoints. In `d = 1` the only null vector
is 0, so my null-cone objection does not touch the pinned computation at all. It
touches the `d >= 3` lift, which is the only place a photon could live and which
the verifier does not test.

Further, the prereg declares its layer honestly:

```
prereg: "L1, state and finite algebra. No claim is made at L2 geometry, L5
stream, L6 measure, or at the physical decoder bridge. Any lift from the exact
finite results below to photon propagation requires a separate named gate."
```

The preregistered artifact was correctly scoped and correctly layered. The
overreach lived entirely in the delivered summary, not in the pin. That is worth
recording as a positive: the discipline held exactly where it was pinned, and
failed only where nothing was pinned.

## 3. My own gate firing in this addendum, recorded

```
FIRED: two literal assertions in A4 were written for sum_i k_i^4, while P_4 sums
over the SYMMETRIC alphabet and therefore doubles every term. Correct literals:
|k|^4 coefficient 6/5 not 3/5, H_4 axis 4/5 not 2/5, body -8/15 not -4/15. The
derived bound 1/30 is unaffected, because the same factor 2 sits in M_2 = 2 I.
Bookkeeping error in my gate, not in the claim. Repaired and reported.
```

## 4. What is unchanged

```
currency Kill 0                   stands, accepted by the owner
word metric route, O3             stands, CLOSED NEGATIVE
arrival-time phase                stands, [F] in the declared scope
sections 1 to 4 of the note       stand, [T] as general mathematics
section 2 has no discriminating power and no public target row   stands
section 3 has no carrier while the shift vanishes                stands
the quadratic path sum as the photon mechanism                   [F]
```

## 5. New result: the first frozen number for the successor probe

The successor probe the owner proposes needs a preregisterable anisotropy bound.
Here is one, exact, and it is available before the operator is chosen.

For a symmetric step alphabet `S` with weights `w_s`, the weighted graph symbol is

```
L(k) = sum_s w_s (1 - cos(k . s)) = (1/2) k^T M_2 k - (1/24) sum_s w_s (k.s)^4 + O(k^6),
M_2 = sum_s w_s s s^T.
```

The quartic term splits exactly into an isotropic piece and the degree 4 cubic
harmonic, `P_4 = a |k|^4 + H_4` with `Delta H_4 = 0`, and `a = Delta^2 P_4 / 120`.
Computed exactly, in rational arithmetic:

```
alphabet                M_2      a        H_4 axis / face / body    frozen bound      peak to peak
nearest-neighbour(6)     2 I     6/5      +4/5  -1/5  -8/15          |k|^2 / 30        |k|^2 / 18
chebyshev(26)           18 I   126/5     -36/5  +9/5 +24/5           |k|^2 / 30        |k|^2 / 18
nn + face diagonal(18)  10 I    54/5      -4/5  +1/5  +8/15          |k|^2 / 150       |k|^2 / 90
```

The bound is the maximum fractional deviation of the dispersion from its isotropic
value, through `O(k^4)`, relative to the `O(k^2)` term. For the six-step alphabet
the two extremes carry exact sum-of-squares certificates,

```
|k|^4 - sum k_i^4       = 2 sum_{i<j} k_i^2 k_j^2        >= 0   (axis is the maximum)
3 sum k_i^4 - |k|^4     = sum_{i<j} (k_i^2 - k_j^2)^2    >= 0   (body diagonal is the minimum)
```

so `|k|^2 / 30` is a **global** bound over all directions, not a check on three
symmetry axes.

**And the anisotropy is exactly cancellable.** Per shell, `H_4` is an exact
rational multiple of one and the same cubic harmonic:

```
shell 1, axis, 6 steps            H_4 = + 2 K_cubic     M_2 =  2 I
shell 2, face diagonal, 12 steps  H_4 = - 4 K_cubic     M_2 =  8 I
shell 3, body diagonal, 8 steps   H_4 = -16 K_cubic     M_2 =  8 I
```

so the fourth-order anisotropy vanishes identically on the positive cone

```
w_1 = 2 w_2 + 8 w_3
```

verified at `(2,1,0)`, `(8,0,1)`, `(10,1,1)`, `(18,5,1)`, each keeping `M_2`
positive and isotropic. A positively weighted two-shell alphabet is exactly
isotropic through `O(k^4)`.

That reframes the whole obligation:

```
Higher-order continuum isotropy is NOT an obstruction in principle. It is a
question about which shell weights the canonical decoder graph actually carries.
If the canonical weights sit on the cone w_1 = 2 w_2 + 8 w_3, isotropy holds
through O(k^4) with zero fitting. If they do not, the residual is a NUMBER, it is
computable before any data is opened, and it is a falsifier.
```

## 6. One review point on the proposed successor probe

The proposed plan is the right plan. One gate in it is near-vacuous as written.

```
proposed falsifier: "if the spatial O(k^2) tensor is not exactly c I_3 ... the
photon continuum reading fails"
```

`M_2 = c I_3` follows from cubic symmetry of the alphabet alone. It holds for all
three alphabets above, at 2, 18 and 10, and it will hold for any step set closed
under the octahedral group. That gate cannot fire against any symmetric candidate,
so it will produce a green line without testing anything. This is the same defect
as gate N3 in the earlier D-GEOM audit: it manufactures the appearance of
confirmation.

Keep it as an integrity check, do not count it as a science gate, and move the
discriminating weight onto the `O(k^4)` gate, which now has a number to freeze.
Suggested replacement, preregisterable today:

```
G3'  decompose the quartic symbol of the CANONICAL decoder graph exactly into
     a |k|^4 and the l = 4 cubic harmonic, in rational arithmetic.
G4'  DECISION, frozen before the computation:
       ISOTROPIC-4  if the harmonic coefficient is exactly 0
       BOUNDED      if the frozen fractional bound is at or below a threshold
                    declared now, with the exact rational reported
       ANISOTROPIC  otherwise, and the number is the falsifier
     No threshold may be set after the coefficient is seen.
```

The `O(k^6)` remainder must be carried explicitly or the bound is not a bound.

## 7. The merged obligation list

```
[F]  raw G mod 5 as the quadratic photon action                (vacuous branch)
[F]  the quadratic F_5 path sum as the photon Fermat mechanism (constant modulus,
     no channel; the lemma itself remains [T])
[F]  a fixed finite additive word metric as the origin of euclidean optics
[F]  j^{c T(path)} as localization on the fastest path, in the declared scope
[T]  the divided canonical Gram is nondegenerate and F_5 isometric to x^2+y^2+z^2
[T]  the exact O(k^4) split and the frozen bounds above
[T]  the cancellation cone w_1 = 2 w_2 + 8 w_3
[O]  derive the canonical photon transfer or wave operator W
[O]  derive c_t and c_s, not choose them, and exhibit the null characteristic branch
[O]  compute the canonical decoder graph's shell weights and place them against
     the cancellation cone
[O]  carry the O(k^6) remainder explicitly
[O]  derive the gauge and holonomy phase from the registered Z_5 connection
[O]  nonzero shift only if a rotational sector is genuinely opened
```

## 8. Pins

```
addendum verifier   09adc2472e10c29099ec49cdb77e48534cfe62743f0fe061a04b62d80bfe4c04  (18535 B)
addendum stdout     43404eaf4afcb1d1eec6aa98cea44d5b25efaee69371dfe860ff151137fe6d6d  (6506 B)
                    38 PASS, 0 FAIL, exit 0, stderr empty, under two seconds
original verifier rerun here, byte identical to the delivered stdout: 2b99a12a...
platform            x86_64, Python 3.11.15, LC_ALL=C LANG=C PYTHONHASHSEED=0 TZ=UTC
```

One single-architecture run. Audit arithmetic. Not a probe, no status label of its
own, and it would need its own preregistration and a genuine two-architecture pin
to become one.

## 9. Non-claims

No candidate opened, no id claimed, no threshold set, no status moved. The
anisotropy bounds in section 5 are computed for named test alphabets, not for the
canonical decoder graph, whose step set and weights were not read in this session
and must be read from the registered object before any of those numbers is quoted
as a TWIST-J result. The `O(k^6)` remainder is not carried. The v184 pin remains
unverified this session; the Private Canon HEAD was not reachable.
