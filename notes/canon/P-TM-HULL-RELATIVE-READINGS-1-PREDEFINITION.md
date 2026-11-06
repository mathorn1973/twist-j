# P-TM-HULL-RELATIVE-READINGS-1 predefinition

**Status:** `NON-CANONICAL / STOP-PREDEFINITION / NO ISSUE LOCK / NO PROBE / NO FORMAL RUN`

**Date:** 2026-09-01

This note separates definitions required for a possible two-sided
Thue-Morse-hull reading lane. It is not Canon, a definition adoption,
preregistration, verifier, execution, result, evidence item, or status
proposal. The identifier is provisional and unreserved.

## 1. Authority and routing pin

```text
STATE:                  ACTIVE
CANON:                  Public Canon v74
AUTHORITY:              mathorn1973/twist-j main
TAG:                    canon-v74
TAG_OBJECT:             796b09aef958a9021b93cff0df7f300ef95f5337
TAG_TARGET:             05a74b21df4b7d8c5c53cfa75255684929c1b76c
CONTENT_COMMIT:          2561f7dcadcbbf683ce7b36219ea67378d879a5a
CANON_SHA256:            2db550cb68f6f4ee33b9194f1f6b3bc4d8fec19cd79e79a702c5357577a92c0e
CANON_BYTES:             389246
BASE_MAIN:               8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
REGISTRY_ROWS:           352
SHA256SUMS:              5/5 OK
provisional identifier: P-TM-HULL-RELATIVE-READINGS-1
public issue lock:       ABSENT
formal branch/path:      ABSENT / ABSENT
formal pin/run/result:   ABSENT / NOT AUTHORIZED / ABSENT
```

Before any public definition branch, search current open issues, `probes/`,
the Registry, object and claim locks, and remote branches. Claim one public
issue. A collision or moved normative input requires a new reviewed
disposition.

## 2. Unchanged public inputs

This predefinition reads, but does not change:

```text
DEF-AUTONOMOUS-STATE       Omega=N_0 x F_5^6 and the one-sided update U
DEF-KERNEL-GENERATORS      (g_0,...,g_4)=(a,b,c,d,e)
DEF-SELECTOR               z_6(psi)+2 theta_n mod 5
TM-SHEET-SYNCHRONIZING-GRAPH
ALGEBRAIC-DMATTER          current five-field L1 algebraic binding
DEF-QDD-BALANCED-PISTON
DEF-QDD-MATTER-RECORD
DEF-QDD-DIRECT-WRITE
TIME-CUT-READING           current local pair 00 among its dictionary clauses
METRO-TICK                 positive tick delta_tau=2 pi/5 at its present scope
```

The current `ALGEBRAIC-DMATTER` and `D_clock` are not rewritten. The present
`DEF-LOG-STREAM` and `GATE-L1-L5-LOG-PROJECTION` are not reused: the proposed
streams have a different two-sided source and require their own named gates.

## 3. Proposed L1 hull extension

Let

\[
X=\mathbb F_5^6,
\qquad
F_\varepsilon(\psi)
=g_{z_6(\psi)+2\varepsilon\bmod5}(\psi),
\qquad \varepsilon\in\{0,1\}.
\]

Let \(K_{\rm TM}\subset\{0,1\}^{\mathbb Z}\) be the two-sided Thue-Morse
subshift and \((S\kappa)_m=\kappa_{m+1}\). Propose

\[
\widehat X_{\rm TM}=K_{\rm TM}\times X,
\qquad
V_{\rm hull}(\kappa,\psi)
=\bigl(S\kappa,F_{\kappa_0}(\psi)\bigr).
\]

This is a new hull extension of the checkpoint cocycle. It is not the current
autonomous state \(\Omega\), does not replace \(U\), and is not asserted to
be its natural extension.

Define the proposed graph

\[
h(\kappa)=4+2\kappa_{-1}\pmod5,
\qquad
X_{\rm stab}={(\kappa,\psi):z_6(\psi)=h(\kappa)\}.
\]

Put

\[
i(\kappa)=4+2(\kappa_{-1}+\kappa_0)\pmod5,
\qquad
(\rho\kappa)_m=\kappa_{-m-1},
\]

and propose, only on \(X_{\rm stab}\),

\[
R_{\rm cp}(\kappa,\psi)
=\bigl(\rho\kappa,g_{i(\kappa)}(\psi)\bigr).
\]

Public candidate probe `P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1` (issue #780,
PR #785) is intended to establish independently at L1:

\[
V_{\rm hull}^9(\widehat X_{\rm TM})=X_{\rm stab},
\qquad
V_{\rm stab}:=V_{\rm hull}|_{X_{\rm stab}}\text{ is invertible},
\]

\[
R_{\rm cp}^2=1,
\qquad
R_{\rm cp}V_{\rm stab} R_{\rm cp}=V_{\rm stab}^{-1},
\]

and the stated natural-extension identification for \(V_{\rm hull}\). Its
local result is currently `candidate-T/L1` with the architecture gate
pending. None of those equations is asserted as a public result by this
predefinition or supplied by v74.

Naming fences:

- `X_stab` avoids collision with the Canon's group `Gamma`;
- `V_hull` distinguishes the new map from the current `U`;
- `R_cp` is a mathematical checkpoint reversor, not physical `T`;
- no set is called the physical bulk or physical carrier.

## 4. Proposed definition inventory

If the prerequisite lands, a later definition package may propose these
objects. The names below are not adopted `NORMATIVE.tsv` rows here.

| Proposed object ID | Kind | Layer | Required gate |
| --- | --- | --- | --- |
| `DEF-TM-HULL-CHECKPOINT-EXTENSION` | definition of `(Xhat_TM,V_hull,X_stab)` | L1 | none |
| `DEF-TM-HULL-ACTION-GROUPOID` | action groupoid of the invertible restriction | L1 | none |
| `DEF-TM-HULL-QDD-STREAM` | two-sided stream of current local QDD formulas | L5 | `GATE-L1-L5-TM-HULL-QDD-STREAM` |
| `DEF-TM-HULL-TIMECUT-STREAM` | two-sided stream of local `00` events | L5 | `GATE-L1-L5-TM-HULL-TIMECUT-STREAM` |
| `DEF-TM-HULL-RELATIVE-METRO-COCYCLE` | signed relative tick on arrows | L5 | `GATE-L1-L5-TM-HULL-METRO-COCYCLE` |
| `DEF-TM-HULL-INTERVAL-RECORD` | finite record on a positively oriented arrow | L5 | `GATE-L1-L5-TM-HULL-INTERVAL-RECORD` |

Each proposed gate has `gate_kind=DEFINITION_PROJECTION`, exact endpoints
`L1 -> L5`, and exactly the displayed owner. A future package must supply its
typed deterministic projection and update `NORMATIVE.tsv`,
`DEPENDENCIES.tsv`, and `GATES.tsv` consistently. This note makes none of
those ledger changes.

## 5. Proposed action groupoid

Conditioned on invertibility of \(V_{\rm stab}\), define

\[
\mathcal G_\infty=X_{\rm stab}\rtimes_{V_{\rm stab}}\mathbb Z.
\]

A pair \((x,n)\) is an arrow \(x\to V_{\rm stab}^n x\), with

\[
s(x,n)=x,
\qquad
t(x,n)=V_{\rm stab}^n x,
\]

\[
(V_{\rm stab}^n x,m)\circ(x,n)=(x,n+m),
\qquad
(x,n)^{-1}=(V_{\rm stab}^n x,-n).
\]

The reversor would induce

\[
\mathfrak R(x,n)=(R_{\rm cp}x,-n).
\]

These are formal groupoid equations only. The orbit quotient
\(X_{\rm stab}/\langle V_{\rm stab}\rangle\) is not substituted: it discards the
oriented arrow and the relative displacement needed below.

## 6. Proposed QDD stream

Let

\[
q_{\rm QDD}:X\to\mathcal Q_{\rm QDD}
\]

denote checkpoint-local evaluation of the current direct algebraic QDD
formula, with \(\mathcal Q_{\rm QDD}\) exactly the present five-field
`MatterData_QDD` type. Naming this local formula does not enlarge the current
domain or physical scope of `ALGEBRAIC-DMATTER`.

For \(x\in X_{\rm stab}\), propose

\[
\mathcal M_x(j)
=q_{\rm QDD}\!\left(\operatorname{pr}_2(V_{\rm stab}^j x)\right),
\qquad j\in\mathbb Z.
\]

With \((\sigma^n a)(j)=a(j+n)\), the intended definition-projection gate
must certify

\[
\mathcal M_{V_{\rm stab}^n x}(j)=\mathcal M_x(j+n),
\qquad
\mathcal M\circ V_{\rm stab}^n=\sigma^n\circ\mathcal M.
\]

This is a stream of algebraic records. It supplies no physical effect,
instrument, occurrence law, sampling, randomness, or L6 measure.

## 7. Proposed `00` event stream

For \(x=(\kappa,\psi)\), propose the local event

\[
e_{00}(x)=\mathbf1\{(\kappa_{-1},\kappa_0)=(0,0)\}
\]

and its stream

\[
\mathcal E_x(j)=e_{00}(V_{\rm stab}^j x)
=\mathbf1\{(\kappa_{j-1},\kappa_j)=(0,0)\}.
\]

The intended gate must certify shift covariance. With the displayed reversal
convention, the symmetric word `00` additionally has the candidate identity

\[
\mathcal E_{R_{\rm cp}x}(j)=\mathcal E_x(-j).
\]

That identity is specific to the unoriented pair `00`. It is not a generic
rule for an oriented word detector and does not extend the physical scope of
`TIME-CUT-READING`.

## 8. Proposed relative metronome cocycle

The current theorem fixes one positively oriented tick

\[
\delta_\tau=\frac{2\pi}{5}.
\]

Propose on arrows

\[
\tau_{\rm met}(x,n)=n\,\delta_\tau.
\]

The intended gate must certify

\[
\tau_{\rm met}(x,n+m)
=\tau_{\rm met}(x,n)+\tau_{\rm met}(V_{\rm stab}^n x,m),
\]

\[
\tau_{\rm met}(V_{\rm stab}^n x,-n)=-\tau_{\rm met}(x,n),
\qquad
\tau_{\rm met}(\mathfrak R(x,n))=-\tau_{\rm met}(x,n).
\]

The signed \(\mathbb Z\)-cocycle is a new proposed definition. It is not an
in-place extension of `METRO-TICK`, not an absolute time coordinate, and not
a physical proper-time or time-reversal theorem.

## 9. Proposed interval records

Let \(a:X_{\rm stab}\to\mathscr A\) be a separately frozen local record map.
For \(j\le k\), propose

\[
A_x^a(j,k)
=a(V_{\rm stab}^j x)a(V_{\rm stab}^{j+1}x)\cdots a(V_{\rm stab}^{k-1}x)
\in\mathscr A^*,
\]

with \(A_x^a(j,j)=\varepsilon\), the empty word. Equivalently, on positive
arrows put

\[
\mathbf A^a(x,n)=A_x^a(0,n),\qquad n\ge0.
\]

The intended gate must certify

\[
A_x^a(j,k)A_x^a(k,\ell)=A_x^a(j,\ell),
\]

\[
A_{V_{\rm stab}^n x}^a(j,k)=A_x^a(j+n,k+n),
\]

and the equivalent arrow composition

\[
\mathbf A^a(x,p)\mathbf A^a(V_{\rm stab}^p x,q)
=\mathbf A^a(x,p+q).
\]

The free monoid generally has no inverse, so \(\mathbf A^a\) is not defined
on negative arrows without an additional output type. A physical record
alphabet, instrument, persistence rule, and trial measure remain unresolved.
No `D_clock^rel` is adopted by this note.

## 10. Direct-`e` QDD noncongruence and the deferred dynamic fence

Public candidate probe `P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1` (issue #782,
PR #784) is independent of the proposed carrier and reversor. At L1 it proves
that all 312 nonzero sign fibres of the current five-field QDD record split
under the declared affine generator `e`. Its local result is
`candidate-T/L1` with the architecture gate pending. It must be treated as a
negative boundary for pointwise record transformation, not as a prohibition
on streams.

If the stable-image result later becomes public, the same algebraic witness
can be placed in one common proposed reversor context:

Freeze the common context and witnesses:

```text
kappa_(-1)=kappa_0=0, hence R_cp uses g_4=e
psi_+=(1,0,0,0,3,0)
psi_-=(4,0,0,0,0,0)
v_+=(1,0,0,0)
v_-=(-1,0,0,0)
```

Both points are on the proposed sheet \(z_6=4\). Their complete current
five-field QDD input record is the same:

```text
(SUPPORTED,
 4/5,
 (1/20,3/4),
 DENSITY(((1,-1/4,-1/4,-1/4),
          (0,0,0,0),
          (0,0,0,0),
          (0,0,0,0))),
 NORMALIZED((1/16,15/16)))
```

The same `e` branch gives balanced pistons

\[
(1,1,-2,-1),\qquad(-2,1,-2,-1),
\]

with ordered branch weights

\[
(1/20,27/4),\qquad(4/5,6),
\]

and unequal output records. Conditional on the public establishment of
\(X_{\rm stab}\) and \(R_{\rm cp}\), this would forbid a set map

\[
r_Q:\mathcal Q_{\rm QDD}\to\mathcal Q_{\rm QDD}
\]

satisfying

\[
q_{\rm QDD}(\operatorname{pr}_2R_{\rm cp}x)
=r_Q(q_{\rm QDD}(\operatorname{pr}_2x))
\]

for every \(x\in X_{\rm stab}\). This is the elementary failure of constancy on
one fibre.

It does not rule out:

- a transformation on the full two-sided stream \(\mathcal M_x\);
- a nonlocal, relational, multivalued, or context-indexed reading;
- a larger record carrying signed or phase-sensitive data;
- another decoder or apparatus;
- physical time-reversal covariance or violation.

No pointwise reversal law for \(\mathcal M\) may be inserted into the proposed
definition package.

## 11. Scope of a later covariance probe

Only after the prerequisite probes, definition adoption, and named gates may
a later probe target:

1. action-groupoid identities and the induced `R_cp` arrow map;
2. QDD-stream shift covariance;
3. `00`-stream covariance and its exact reversal index;
4. the relative-metronome cocycle equations;
5. interval-record concatenation and shift covariance;
6. a separately typed agreement at a marked head on a common domain, if such
   a domain is publicly frozen.

It must exclude:

```text
physical carrier selection
physical status of transient layers
physical instrument or trial measure
completion or replacement of ALGEBRAIC-DMATTER
descent or replacement of the current D_clock
pointwise QDD reversor
physical T symmetry, arrow of time, causality, or thermodynamics
L6 probability or invariant-measure claims
```

## 12. Stop conditions

STOP if:

- the stable-image or QDD prerequisite is absent, changes scope, or fails;
- `X_stab` is called the natural extension of current `U` rather than of the
  newly defined `V_hull`;
- a new L5 object lacks its exact `DEFINITION_PROJECTION` gate;
- a proposed definition is assigned a scientific status;
- current `ALGEBRAIC-DMATTER`, `D_clock`, `TIME-CUT-READING`, or `METRO-TICK`
  is silently retyped or strengthened;
- a pointwise QDD reversor is assumed despite the direct-`e` fibre;
- invariant or Haar measure is called the physical trial measure;
- the mathematical reversor is called physical `T` without an instrument,
  result transformation, preparation rule, and physical measure;
- any public formal run occurs before issue lock, preregistration pin, and
  accepted verifier commit.

## Disposition

This file is a public-reviewable predefinition only. Its formulas may guide a
later definition package. They provide no present public definition, theorem,
dictionary, hypothesis, obligation, gate closure, or status movement.
