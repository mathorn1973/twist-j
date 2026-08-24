# AUDIT of the beta = 4 probe

```text
STATUS:      INTERNAL, NON-CANONICAL. Candidate-lane audit, no authority.
BASIS:       Public Canon v58 (canon-v58, content 05a0749e,
             CANON_SHA256 647822f5..., 304010 B), gate run this session.
DISCLOSURE:  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
             Written after reading the probe verdict. Not preregistered.
             Independent code, independent method, no import of the probe.
LEGS:        one, Linux x86_64 CPython 3.11.15. Not a two-architecture gate.
VERDICT:     AUDIT-PASS. 16 of 16 audit gates, 0 of 9 breaker findings.
             No claim of the probe is refuted. Two corrections of framing
             and one quantification of the open gap are added.
```

## 1. What was checked, and how it differs from the probe's own check

The probe verified 6561 integer matrices and attacked 14641. This audit
does not sample. It proves the same statements symbolically over
`Z[a,b,c,d]` with exact multivariate polynomial arithmetic, so the
universal quantifier is earned rather than sampled, and it then rebuilds
the correlation matrix by a physically independent route.

```text
audit_bell_beta4_1.py    336d3c3cf113c0ec08609bc9e45c83269384d1f9b7f37cef1aa5650eaa3b8e1b
  stdout                 dd83b9c49577ab952762d73fd03d2ecd5218955d1225fc8d4455af245f6c8b7d
breaker_bell_beta4_1.py  12c631726503ebade4cb7edcb9a52804bc24fc7180c7c552b5a5b9c4bb8eac33
  stdout                 16c7531571945e727d7c89398047d74b5cfcfaecbf2f663cae7a5a93bc0d8de2
```

## 2. Confirmed, at a higher grade than claimed

```text
A  T(X) is exactly as the probe states, including the zero pattern, which
   follows structurally: S_1, S_3 symmetric and S_2 antisymmetric force
   tr(sym . antisym) = 0 in the four off-block entries.

B  Spec(T^T T) = {Q^2, R^2, R^2} holds as a POLYNOMIAL IDENTITY, not a
   numerical coincidence: e1 = Q^2 + 2R^2, e2 = 2Q^2R^2 + R^4,
   e3 = Q^2R^4, each verified as an exact identity in Z[a,b,c,d].

C  Q^2 = u^2 + v^2 + w^2 holds identically, and among integer s only
   s = +-2 closes it, with exact defect (s^2 - 4)D^2. R = 2 det X stands.

E  signature(Q) = (4,0), signature(ad - bc) = (2,2), computed by exact
   congruence. Sylvester then forbids any invertible linear swap. The
   [candidate-F] on the channel-swap symmetry is correct.
```

One improvement on the probe's own argument. The probe asserts
`R^2 <= Q^2` and uses it to order the spectrum. That inequality has an
exact certificate with no analysis and no float:

```text
Q - 2D = (a - d)^2 + (b + c)^2,
Q + 2D = (a + d)^2 + (b - c)^2,
Q^2 - R^2 = [(a-d)^2 + (b+c)^2] . [(a+d)^2 + (b-c)^2].
```

A product of two sums of squares. So `lambda_1 = Q^2` always, with
equality to `R^2` exactly on `a = d, b = -c` or `a = -d, b = c`. The
ordering step of the probe is therefore unconditional.

## 3. Correction one: this is the Horodecki criterion, and it is known

The breaker rebuilt the correlation matrix physically: it formed the
two-qubit state from `X`, built `sigma_i (x) sigma_j` over Gaussian
integers, and computed `<psi| sigma_i (x) sigma_j |psi>` directly.

```text
X1  |piston T| = |physical correlation matrix| on all 6561 matrices.
    The two differ in exactly one entry, (2,2), by sign, which is the
    S_2 = i sigma_y convention. T^T T is therefore identical.
X2  the physical route reproduces the same spectrum identically.
X3  after state normalization, lambda_1 + lambda_2 = 1 + C^2 exactly,
    where C = 2|det X| is the Wootters concurrence of a real pure state.
X4  max over states of that quantity is exactly 2, so CHSH_max = 2 sqrt2.
```

`M = 1 + C^2` for pure states, with `CHSH_max = 2 sqrt(M)`, is the
Horodecki criterion combined with the Wootters concurrence. It is a
standard result of quantum information, not a new one. The probe has
re-derived it from an integer route.

This is not a demotion of the result. It is the strongest possible
consistency outcome for the stated program goal, an integer deterministic
description of identical quantum physics: the piston carrier reproduces
the standard two-qubit Bell structure exactly, including Tsirelson as an
output. But it must not be presented anywhere as a new physical result,
and the derivation is not independent of Bell. The step
"two settings => sum of the two largest eigenvalues" IS the Horodecki
theorem, which is itself derived from the CHSH operator. The probe is
right that no fit to `2 sqrt2` was performed; it is not right that the
Bell structure was avoided. It was imported at the two-setting step.

## 4. Correction two: the degenerate pair is not "left outside"

The probe reads the spectrum as one direct direction plus two relational
directions, one of which "stays outside the measuring plane". The two
relational eigenvalues are degenerate, so there is no invariant fact
about which one is used. The correct statement is weaker and cleaner:
the CHSH optimization runs over a 2-plane, a 2-plane meets the spectrum
in at most two dimensions, and the maximum of the Rayleigh sum over
2-planes is `lambda_1 + lambda_2 = Q^2 + R^2`. Nothing is discarded; the
plane simply has rank two.

## 5. The open gap, now quantified

The probe says local symmetry alone does not fix the reading, and gives
`diag(2,8,2)` and `diag(2,18,2)` as covariant alternatives. The breaker
identifies that family exactly. Rescaling the antisymmetric axis by
`S_2 -> t S_2` leaves the symmetric block untouched and gives

```text
Spec(T^T T) = {Q^2, R^2, t^4 R^2},      lambda_1 + lambda_2 = Q^2 + t^4 R^2,
beta(t) = 4 t^4.

t = 1 -> beta = 4        t = 2 -> beta = 64       (the diag(2,8,2) case)
t = 3 -> beta = 324      (the diag(2,18,2) case)  t = 5 -> beta = 2500
```

So the missing axiom is not a small wobble around four. Without it the
coefficient runs over a quartic family and four has no distinguished
place in it. That is a sharper statement of the gap than the probe made,
and it is the honest measure of how much work the missing obligation does.

What closes it is one scalar condition, and the audit names it exactly:

```text
||S_1||_F^2 = ||S_2||_F^2 = ||S_3||_F^2 = 2,
```

that is, the three generators carry one common Frobenius norm. `t = 1`
holds if and only if that equality holds. So the open obligation is not
"the Frobenius metric" as a vague requirement; it is the single equal-norm
condition on the basis of the trace-free part, and it needs a derivation
from the architecture rather than a convention.

## 6. Status of the chain after this audit

```text
[candidate-T]  R = 2 det X from the integer identity.        confirmed,
               now symbolic rather than sampled.
[candidate-T]  Spec(T^T T) = {Q^2, R^2, R^2}.                confirmed,
               polynomial identity, plus SOS certificate for the ordering.
[candidate-F]  the Q <-> R channel-swap symmetry.            confirmed
               falsified, by exact signature.
[candidate-T conditional]  two settings => Q^2 + R^2 => beta = 4.
               Confirmed conditionally, and the condition is now exactly
               one equation: equal Frobenius norms of the three
               generators. Under any other equal-covariance normalization
               beta = 4t^4.
[candidate-D]  the positive Pauli metric appears only in the hermitian
               reading at 2. Not audited; it is a reading, correctly
               labelled, and it does not carry the beta result.
```

`BELL-CAUSAL-ACCOUNTING` remains `[O]/STOP`. Nothing here supplies a
source, local apparatus, settings, events, a measure, the factorization
test, setting independence, or the separate controllable-signalling test.

## 7. What the next probe should actually target

The probe proposes `C-BELL-TWO-SETTING-APPARATUS-4-N` on the bridge from
the piston carrier to two local dichotomic instruments. That is the right
lane, but on this audit's evidence the load-bearing question inside it is
narrower and should be named as its first obligation:

```text
derive  ||S_1|| = ||S_2|| = ||S_3||  from the architecture,
or prove that no admissible architecture selects it,
in which case beta is not derived and the row stays open at 4t^4.
```

Everything else in the chain is already exact.
