# PREREG. P-TM-SYM2-BORN-HALVING-1

Status: PUBLIC FORMAL PROBE PIN CANDIDATE. NOT EXECUTED.

## 0. Identity and authority

```text
probe:         P-TM-SYM2-BORN-HALVING-1
branch:        probe/P-TM-SYM2-BORN-HALVING-1
path:          probes/P-TM-SYM2-BORN-HALVING-1/
owner:         A. M. Thorn / current ChatGPT owner session
claim lock:    issue #378
layer:         L5 -> L6 candidate bridge
public basis:  Public Canon v46 ACTIVE
main:          6545c1d0de61ff4696eb3de1a258139e8891f436
content:       62628ca4da2d938e4e3a122d35c0d93a6debc27f
Canon sha256:  6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff
Canon bytes:   222760
```

STATUS.md, POLICY.md, AGENTS.md, canon/CORE.md, canon/FRONTIER.md,
canon/REGISTRY.tsv, canon/GATES.tsv and the relevant dependency rows were
read from public main before the claim lock. The owner also supplied a fresh
clone readback with canon/SHA256SUMS 5 of 5 OK.

This pull request is probe-only. It changes no Canon, Registry, Frontier,
dependency, gate, status, release, or other probe.

## 1. Result exposure and correction record

This probe is RESULT-EXPOSED and proof-first. Before pin:

- NON-CANONICAL work #375 exposed the candidate source
  `omega(a,b,c)=c-a`;
- NON-CANONICAL work #376 exposed a candidate Born junction;
- an independent reviewer wrote a third exact implementation and reported
  eighteen passing checks, but also found the load-bearing defect that the
  public `ABELIAN-FACE-DICTIONARY [D]` fixes only the modulus
  `|1+zeta_5^k|^2/10`, not an amplitude lift;
- the reviewer supplied a modulus-preserving nonmonomial lift with unequal
  coefficient Born weights;
- the reviewer also disclosed two defects in that review verifier itself:
  a printed gate count 16 versus 18 and a tautological B2 whose content was
  carried by B2r.

None of those runs, files, hashes, or outputs are evidence here. The accepted
verifier below is freshly authored. It has zero formal executions at pin time.
Static compilation only is permitted before pin.

The review also identified two owner decisions required before pin. They are
frozen below and never move under this probe id.

## 2. Public inputs, exact subscopes

### 2.1 TM-SYM2-PROJECTIVE-FOURFOLD [T]

Consume only:

```text
W3 = {001,010,011,100,101,110},
N = bitwise complement,
Sel_class has 48 members,
the projective postcomposition gauge G has four free orbits,
the unique stationary W3 law f is uniform.
```

The following statements carried by the same public row are forbidden as
construction inputs:

```text
the six-line pushforward mu_i=1/6,
M_TM=(1/3)P1+(2/15)P5.
```

They may be recognized only after the new typed bridge has been constructed.

### 2.2 TM-SYM2-SEMILINEAR-TWOFOLD [T]

Consume only the exact character

```text
epsilon_read = chi_Q chi_F
```

on the four selector-gauge classes. Gamma_sl remains a comparison action, not
an adopted gauge.

### 2.3 TM-SYM2-REVERSAL-CLOSURE [T]

R, N and NR are comparison actions. No outcome enlarges the postcomposition
gauge.

### 2.4 MEASURE-BORN-VERB [D]

Consume only the type constraint: the physical measure must be a Born-square
reading of a typed verb. This row supplies no amplitude lift and no numerical
Born probability.

### 2.5 Other public inputs

`BORN-FACE-WEIGHTS [T]` is a modulus compatibility control.
`GOLDEN-SIX-LINE-SYM2-FRAME [T]` supplies the six-line codomain only.
`J-UNIT [T]` and `J-GOLDEN-BRIDGE [T]` supply J and zeta_5 arithmetic.

`GYRON-DENSITY` is not a numerical confirmation in this probe. Equality of a
number on another carrier is outside the target.

## 3. Frozen owner ruling S4: stationary law import

ACCEPT.

The uniform stationary law on W3 is typed L5 window data, not the target L6
physical line measure. It may therefore be imported from
TM-SYM2-PROJECTIVE-FOURFOLD [T].

The verifier may form its N-orbit marginal from this imported law. It may not
use the public line pushforward or M_TM in constructing the bridge. The
appearance of the same rational value on the line carrier after the map is an
outcome, not an input.

The stationary theorem is imported, not re-claimed as new science.

## 4. Frozen owner ruling S5: four selector classes are not three word shells

ACCEPT WITH EXPLICIT TYPE SEPARATION.

Define

```text
C_sel  := Sel_class/G,      |C_sel|=4,   selector-gauge classes,
Q_word := W3/<N>,           |Q_word|=3,  complement orbits of words.
```

There is no asserted map `C_sel -> Q_word`.

At tick n, the complete L5 source schema is

```text
Source5_n =
(
  complete four-class selector-gauge record C_sel,
  epsilon_read on C_sel,
  q(n) in W3,
  omega_n
).
```

Equivalently the oriented current on selector classes is

```text
J_n(C) = omega_n epsilon_read(C),  C in C_sel.
```

The Born conditional acts on the two sheets inside each member of Q_word.
A selector chart maps W3 to the six Lines. Totality requires the map to be
defined for every selector class and every W3 word. A scalar L6 output may be
orientation-blind only if blindness is derived after Source5_n has been typed.

No quotienting of epsilon_read and no 4-to-3 identification is permitted.

## 5. Source theorem to re-derive

For

```text
q(n)=(theta_(n-1),theta_n,theta_(n+1)),
R(a,b,c)=(c,b,a),
omega(a,b,c)=c-a,
```

the probe decides

```text
omega o N = -omega,
omega o R = -omega.
```

It also classifies the rational function space

```text
{h:W3->Q | h o N=-h and h o R=-h}
```

and requires it to be one-dimensional, spanned by omega.

This is a theorem target of this probe. #375 is provenance only.

## 6. Frozen typed verb-lift class

Put `j=zeta_5`, `I5=Z/5Z`, and use the exact Fourier convention

```text
F(a)_k = sum_(r in I5) a_r j^(r k).
```

The public modulus dictionary does not select a phase. The admitted physical
candidate class is therefore frozen explicitly:

```text
v_t = delta_t + delta_(t+1),  t in I5,
V_J^mono = {v_t : t in I5}.
```

For every t and k the target identity is

```text
F(v_t)_k = j^(t k) (1+j^k).
```

For nonzero k,

```text
1+j^k = sigma_(3k)(J),
```

where `sigma_a(j)=j^a`, because `J=1+j^2` and `2^(-1)=3 mod 5`.
The k=0 slot is separately `2`; it is not called a Galois conjugate.

Thus the four nonzero spectral slots are monomial phases times the complete
Galois orbit of J, while the zero slot is typed explicitly. This fixes the
indexing ambiguity exposed before pin.

No claim is made that V_J^mono is the complete class of all amplitude lifts
with the registered moduli.

## 7. Born-halving target

For each t, use the coefficient coordinate effects and exact square norm on
the two-point support of v_t. The normalized Born law must be:

- total on the support;
- independent of the overall scale and sign;
- independent of which support point is called the first sheet;
- identical for all five t.

The verifier must not contain a target six-line probability as an input.

A failure for any member of V_J^mono is scientific NEGATIVE.

## 8. Frozen modulus-only negative control

Let

```text
Psi_k=1+j^k.
```

Form the control spectrum `Psi'` by

```text
Psi'_1 = conjugate(Psi_1)=1+j^4,
Psi'_k = Psi_k for k != 1.
```

This preserves every pointwise modulus. Compute its exact inverse Fourier
coefficients and their coefficient Born squares.

The required boundary theorem is:

```text
same five spectral moduli do not force equal coefficient Born weights.
```

This control is deliberately outside V_J^mono. Its role is to kill the false
stronger inference from ABELIAN-FACE-DICTIONARY modulus data alone. Failure to
establish this boundary is STOP for this probe, not permission to widen the
claim.

## 9. Total bridge and coherence theorem

Let f be the imported uniform stationary W3 law. Form its marginal on Q_word.
For each complement orbit O, use the Born conditional supplied by section 7.
Define the candidate word measure by

```text
mu_B(w) = f_Q([w]) * Born_[w](w).
```

The theorem target is that this is a total normalized measure on W3 and that,
for every frozen selector `s`,

```text
mu_s = s_* mu_B
```

is the same normalized measure on the six Lines.

The proof of selector coherence is universal: if mu_B is constant on W3, every
bijection W3->Lines has the same pushforward. The 48 frozen selectors are a
subset. An optional 6! sweep is only an audit corollary and carries no
independent scientific weight.

The map is typed on the complete Source5 schema. The final scalar map may
ignore J_n numerically only after totality over every C in C_sel and every
word in W3 has been proved.

## 10. Circularity firewall

The following may not select any source, lift, support, normalization,
conditional law, or branch:

```text
the L6 line value 1/6,
the factorization 1/6=(1/2)(1/3),
M_TM=(1/3)P1+(2/15)P5,
GYRON-DENSITY.
```

The verifier must derive the output measure before printing its common line
weight. It must not import M_TM or any GYRON number.

The imported L5 window law is explicitly permitted by S4 and remains a
different typed object from the L6 output.

## 11. Status ceiling

A positive mathematical result can contain theorem-grade exact lemmas, but the
physical bridge candidate is at most D because:

1. MEASURE-BORN-VERB is D;
2. V_J^mono is frozen here as a typed candidate verb lift, not inherited as a
   public T theorem.

A positive probe therefore proposes no automatic status change.
TM-SYM2-PHYSICAL-MEASURE [O] remains unchanged until a later separately
reviewed fold decides treatment.

## 12. Accepted verifier and gate grammar

`verify.py` is standard-library only and exact. It uses `int`, `Fraction`, and
a direct Q(zeta_5) implementation. No float, network, subprocess, randomness,
clock, argument parsing, or file write.

The accepted verifier computes eighteen named gates:

```text
G01 W3-CARRIER
G02 SOURCE-CHARACTER
G03 SOURCE-UNIQUENESS
G04 TYPE-SEPARATION
G05 MONOMIAL-FOURIER
G06 GALOIS-REINDEX
G07 MONOMIAL-MODULUS
G08 FOURIER-INVERSE
G09 BORN-HALVING
G10 SHEET-ORIENTATION
G11 CONTROL-MODULUS
G12 CONTROL-FULL-SUPPORT
G13 CONTROL-UNEQUAL-BORN
G14 S4-WINDOW-IMPORT
G15 TOTAL-WORD-MEASURE
G16 SELECTOR-COHERENCE
G17 ORIENTATION-TOTALITY
G18 CIRCULARITY-STATUS
```

The printed gate count must be derived from the actual gate list. No hard-coded
mismatched count is permitted.

Scientific result grammar:

```text
SCIENTIFIC_RESULT_BEGIN
SOURCE_SECTOR: <PASS|NEGATIVE>
MONOMIAL_LIFT: <PASS|NEGATIVE>
BORN_HALVING: <PASS|NEGATIVE>
MODULUS_ONLY_CONTROL: <PASS|STOP>
TOTAL_BRIDGE: <PASS|NEGATIVE>
SELECTOR_COHERENCE: <PASS|NEGATIVE>
DERIVED_COMMON_LINE_WEIGHT: <exact Fraction text, computed only at end>
STATUS_CEILING: D
DECISION: <BORN-HALVING-PASS|NEGATIVE|STOP>
SCIENTIFIC_RESULT_END
```

A structural integrity exception is STOP. A counterexample inside the frozen
scientific class routes NEGATIVE with exit zero. The modulus-only control
failure routes STOP because it would leave the scope boundary unproved.

## 13. Falsifiers

NEGATIVE if any one occurs inside the frozen class:

- the source sector is not one-dimensional or omega has the wrong N/R
  character;
- any v_t fails the Fourier identity;
- any v_t has unequal normalized support Born weights;
- the Born law depends on t or sheet orientation;
- the total map is undefined on a Q_word shell or a C_sel class;
- two frozen selector charts yield different L6 measures.

STOP on:

- authority drift or collision;
- pin or byte mismatch;
- failure of the modulus-only negative control;
- any hidden use of the forbidden L6 target/operator/GYRON value;
- type confusion between C_sel and Q_word;
- an attempt to amend, rebase, squash, force-push, move a threshold, or repair
  the frozen class after pin.

## 14. Formal execution

The pin contains exactly this PREREG.md and the accepted verify.py before the
first formal execution.

Formal local command:

```text
python3 probes/P-TM-SYM2-BORN-HALVING-1/verify.py
```

Environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

After the first formal run, add EXPECTED.txt, RUN.md and RESULT.md. The pull
request changes only this probe directory. Required GitHub-hosted x86_64 and
aarch64 jobs must reproduce the same committed EXPECTED.txt byte for byte and
aggregate `check` must pass.

No formal verifier execution occurred before the pin.
