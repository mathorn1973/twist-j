# AUDIT: the Euler-Widder hierarchy, and how deep its RH content actually sits

```text
Status     NON-CANONICAL independent audit of the owner-completed branch
           notes/c-rh-stieltjes-widder-euler-1-n (issue 471, head f0a455a1).
           No authority, no registry motion, no fold. RH remains O.
           Canon v57 untouched and confirmed untouched by the branch.
Session    AUDIT-EULER-WIDDER-DEPTH, 2026-08-20.
Basis      Public Canon v57 ACTIVE, main 4ef54f0c, tag canon-v57 resolving to
           the same commit. Branch diff against main: nine files under
           notes/, zero normative files.
Preregs    leg 1  eaec1369.. (7869 B), frozen with its program before any run
           leg 1B e368ea13.. (4065 B), same discipline
Disclosure RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
Verdict    the construction verifies. Every owner-facing gate passed,
           including both recorded depths reproduced exactly. Two gates of
           this audit's OWN auxiliary claims fired and are archived with
           their diagnosis. The audit adds an exact detection criterion, a
           depth law, an unconditional vacuity theorem for the low levels,
           and an exponential masking measurement. Together these say where
           the next attack must NOT go.
```

## 1. What was confirmed in the branch

```text
[T re-verified]  the pole calculus. With z_P = rho(rho-1) and
    f(u) = sum_P m_P/(u - z_P), the Widder operator acts as
    W_k(u) = sum_P m_P (2k-1)! (-z_P)^k / (u - z_P)^(2k).
    Verified as an exact rational-function identity, k = 1..6, four distinct
    roots, by symbolic differentiation over Q, not by sampling.
[T re-verified]  f > 0 and W_1 > 0 unconditionally. The reason is one sign:
    for every zero in the open strip A := -Re z = gamma^2 + beta(1-beta) > 0,
    so each conjugate pair contributes 2(u+A)/((u+A)^2+B^2) to f and
    2[A(u+A)^2 + B^2(2u+A)]/((u+A)^2+B^2)^2 to W_1, both positive. The
    branch's closed forms agree with the pole calculus exactly.
[C reproduced]  both recorded depths, exactly: rho = 9/10 + i/2 first goes
    negative at k = 2, and rho = 3/4 + 10i at k = 32.
[import, not re-proved]  Widder's characterization in the Sokal form. Every
    conclusion below is conditional on that operator family being correct;
    the branch's own frozen premise, and this audit inherits it.
```

The Stieltjes equivalence itself is a pole-location statement and is correct
as written. The branch says so plainly, and that honesty is worth recording:
it is a reformulation, not a positive representation.

## 2. Exact detection criterion, no scan and no pi

```text
[candidate-T]  Write z = -A + iB. The contribution of one conjugate pair to
W_k is negative for some u > 0 if and only if

        Re[(A - iB)^k] < 0.
```

Proof. The pair contributes proportionally to cos(k(2 phi - theta)) with
theta = arg(A - iB) and phi = arg((u+A) - iB). As u runs over (0, infinity),
phi decreases from theta to 0, so 2 phi - theta sweeps (-theta, theta)
monotonically and the infimum of the cosine over u is cos(k theta). Since
cos(k theta) is the sign of Re[(A - iB)^k], the criterion follows.

This replaces a search over u by a single integer test in Z[i]. For rational
zero data the whole question is decided by exact integer powers, with no
floating point, no transcendental constant and no zero table. The owner's two
data points fall straight out: 17 - 20i squares to -111 - 680i, so k = 2; and
1603 - 80i first turns its real part negative at k = 32.

## 3. The depth law

```text
[candidate-T]  the first failing level of an isolated pair is

        k_min = ceil( pi / (2 arctan(B/A)) ),
        B/A = gamma(2 beta - 1) / (gamma^2 + beta(1-beta)),

    hence asymptotically, for fixed beta > 1/2 and large height,

        k_min  ~  pi gamma / (2 (2 beta - 1)).
```

Verified on all thirty-eight grid points with a certified rational enclosure
of pi computed inside the verifier by Machin with exact truncation bounds:
the predicted lower and upper brackets COINCIDE with the exact value in every
row. The measured slopes match the law: at beta = 3/4 the depth runs
32, 63, 158, 315 for gamma = 10, 20, 50, 100, a slope of pi per unit height;
at beta = 3/5 the slope is pi/0.4; at beta = 9/10 it is pi/1.6.

Read plainly: the depth needed to see an off-line zero grows linearly in its
height and blows up as it approaches the critical line. The hierarchy sees
low, badly-off-line zeros cheaply and sees the ones that matter never.

## 4. The low levels are unconditionally true

This is the finding that redirects the next attack.

```text
[candidate-T]  Every zero with |gamma| >= 1 and 0 < beta < 1 satisfies
    B <= A, because gamma(2 beta - 1) <= gamma <= gamma^2 <= A. Hence
    theta <= pi/4, hence Re[(A - iB)^2] > 0, hence every conjugate pair
    contributes NON-NEGATIVELY to W_2 at every u > 0. Therefore

        W_2 >= 0 holds unconditionally,

    with no RH input, using only the classical absence of zeros below height
    one. More sharply, if no off-line zero exists below height H, then every
    level k <= floor(pi H / 2) is unconditionally non-negative.
```

At the standard verification height H = 3 x 10^12 that is

```text
        4 712 388 980 384 levels, all unconditionally non-negative.
```

So the branch's own next step, "attack the structure of W_2", is aimed at a
statement that is already a theorem without RH. It cannot decide anything.
The same holds for W_3, W_100, and every level below roughly 4.7 x 10^12.
The owner's sentence "the first possible place of failure is k = 2" is true
for an arbitrary pole configuration and false for the zeta zeros: given only
what is already known about them, the first possible place of failure is
astronomically deep.

## 5. Exponential masking at the level where failure first appears

Even at its own first negative level, a high off-line zero is buried.

```text
[candidate-C]  for an off-line pair at height 50 with beta = 3/4, whose exact
    first negative degree is 158, a background of nine on-line poles at
    heights 14 to 48 keeps the aggregate positive at every sampled u, and the
    dominant positive term exceeds the negative one by a factor above 10^175.
```

The mechanism is the factorial-normalized weight |z|^(-k): at depth k the
hierarchy is dominated exponentially by the LOWEST poles. An off-line zero at
height gamma needs depth about pi gamma / 2, and at that depth every on-line
zero below it outweighs it by a factor of order (gamma^2/gamma_low^2)^k. The
signal appears exactly where it is exponentially invisible.

## 6. Two gates of this audit fired. Both are mine, not the branch's

```text
WA7 FIRED. Leg 1 predicted that a small on-line background would rescue every
    negative sample of an off-line pair at its first negative degree. It did
    not. Diagnosis, confirmed exactly in leg 1B: the probe pair sat at height
    2, BELOW the entire background, so the |z|^(-k) weighting made it the
    dominant pole and nothing could mask it. The prediction had the right
    mechanism and the wrong configuration. Leg 1B places the pair above part
    of the spectrum and the masking appears at once, with the 10^175 margin
    of section 5.
XA1 FIRED. Leg 1B asserted that contribution magnitude decreases with height
    at fixed level and u. False as stated: the weight A^k/(u+A)^(2k) peaks at
    A = u, so it increases for A < u and decreases only for A > u. The grid
    included samples on the rising side. The masking gates XA2 and XA4 are
    unaffected, since every pole involved there has A far above the sampled u.
```

Both are archived, neither is deleted, no threshold moved, and both runs are
recorded with their exit code 2 and the decision word AUDIT-DISAGREEMENT.
That decision word refers to these two auxiliary claims of the audit. Every
gate touching the owner's branch passed.

## 7. Where this leaves the route

```text
[public T]        Canon v57 active and untouched. RH remains O.
[confirmed]       the Stieltjes equivalence and the pole calculus are right,
                  and the branch states their status honestly.
[candidate-T]     exact detection criterion Re[(A - iB)^k] < 0.
[candidate-T]     depth law k_min = ceil(pi/(2 arctan(B/A))) ~ pi gamma/(2(2beta-1)).
[candidate-T]     W_2 >= 0 unconditionally; all levels below floor(pi H / 2)
                  are unconditionally non-negative, about 4.7 x 10^12 of them
                  at the current verification height.
[candidate-C]     exponential masking of a high off-line zero at its own first
                  negative level, margin above 10^175 in the frozen synthetic.
[O]               unchanged: prove W_k >= 0 for all k, or refute it.
```

The practical consequence is a redirection, and it is the point of this
audit. Do not attack W_2, and do not attack any fixed level: every fixed
level is a theorem already, and the first level with RH content is beyond any
computation. Only the uniform statement carries the content, which is the
second half of the owner's own closing sentence, the transition
W_k -> W_(k+1) driven by the Euler and gamma parts. Any such argument must be
structural in k from the start. A numerical or level-by-level approach is not
merely hard here; it is provably empty.

Worth naming: this is the third independent appearance of the same wall in
this program. The Li and Toeplitz work found that finite positive profiles
cannot decide support; the Hankel hard-edge probe measured a detection
ceiling T* growing with height; the Widder hierarchy now shows a detection
depth growing linearly with height and an exponential masking on top. Three
different coordinates, one obstruction: the finite certificate is always
unconditionally true, and the RH content always sits past the horizon. The
pattern itself is now the most informative object in the lane, and the useful
question may be whether that horizon can be proved to be intrinsic.

## 8. Run record

```text
order        leg 1 prereg and program frozen together, ast.parse only before
             the pin, one run; then leg 1B under the same discipline. No
             threshold moved. Stdout carries no time, path or host.
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC; Linux x86_64; CPython 3.11.15. Single platform, so
             candidate labels only.
leg 1        prereg eaec13692f377522d40cb3c21895e81a8dd780a09baaa356edf10e3df0d86781 (7869 B)
             code   2fafe1c60a8af6999391f845ea2daa15da629fa7e4a4fdd7b3d8b87cef75bff1 (12674 B)
             stdout a86bb7b423133c682e0c2e8b408b7cf89056e59a64f79d34c8e46c8fc7366205 (2843 B)
             12/13 PASS, WA7 fired, exit 2
leg 1B       prereg e368ea137a106132f8d725fccfb88766f9db5cfae0e1a8f16334c21e40679b92 (4065 B)
             code   d8464024a0d4f3a595f84f60b6b13e91c04a9a0a80517b182f66db5709d92146 (5319 B)
             stdout bdf366524cb69657729cfa3707fcefbf37e2e3d2e7d509966568e08237e37d8b (1219 B)
             4/5 PASS, XA1 fired, exit 2
pins         AUDIT_PIN-WIDDER.txt f24122ae.., AUDIT_PIN-WIDDER-1B.txt 0b281237..
carrier      rational zero parameters only; no zeta ordinate instantiated, no
             zero table read, no float formed, math never imported; pi used
             only through a Machin enclosure computed inside the verifier.
```

## 9. Scope firewall

L6 only. Single platform, candidate grades only. Nothing here earns a public
T, moves a registry row, or touches Canon v57. No statement is made about the
truth of RH. The masking result is a statement about a frozen synthetic
configuration and is evidence about a mechanism, not a theorem about the true
zero set, whose density is not modelled here. The vacuity result depends on
the classical zero-free height and on the verification height as labelled
imports, and on Widder's characterization exactly as the branch froze it.

## 10. Addendum recorded at write time: main advanced, and one fork closed

While this audit was being written, public `main` advanced from `4ef54f0c` to
`1ca497af` by the merge of PR 473. Canon is unchanged: still Public Canon
v57, same tag, same content commit `8e8b04ab`, same `CANON_SHA256` and byte
count, and the merge adds only one probe directory with no registry delta.
The basis of this audit is therefore unaffected, and the branch carrying this
record is based on the newer `main`.

The merged probe, `P-QDD-FRESH-RECORD-NOFEEDBACK-2`, settles the fork this
session named in `CORRECTION-AUDIT-QDD-TERMINALITY-1_2026-08-20.md`, and it
settles it on the negative branch:

```text
decision: NONIMPLICATION.
witness:  T_star = R_k - C_k, target-independent, self-adjoint, involutive,
          T_star^sharp T_star = Q_k, ordinary repeatability, and
          T_star^2 = Q_k with T_star not +/- Q_k.
```

That is precisely the object the correction record predicted a negative
result would have to exhibit: an architecturally admissible non-terminal
member of the `[R - C]` kind satisfying every other frozen law. So fresh
pointer, fresh blank record cell, append-only record, no old-record feedback
and rational reversibility together do NOT force projective idempotence.

The probe also names the positive boundary, and it is worth quoting because
it is the sharpened successor of this session's QA6: record sufficiency,
meaning that the conditioned ray depends only on the terminal outcome symbol
and not on the repetition count, is equivalent in the frozen invertible
branch class to fresh-pointer ray terminality, to projective idempotence, and
to the single physical class of `+/- Q`. The open question is no longer
whether the old premises imply terminality. It is what physical principle
delivers record sufficiency.

This addendum is a cross-lane note. It changes nothing in sections 1 to 9,
which stand as run and recorded.
