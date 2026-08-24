# AUDIT: the pentagon balance note, line by line

```text
DATE        2026-08-01
TASK        owner submission: a mathematical advance tying the modulus points
            phi^-1, phi^-2 to the Galois wall through the Rogers dilogarithm,
            with two uniqueness branches and a Bloch-group layer. Owner asked
            for a careful pass, a weighing, and the decoder connection. PUBLIC.
AUTHORITY   none. Audit note, incubation lane. NON-CANONICAL. Creates no claim,
            moves no status, promotes nothing, edits no doc it did not create.
BASIS       Public Canon v30, mathorn1973/twist-j main, verified by clone today.
            STATE ACTIVE, AUTHORITY mathorn1973/twist-j main, tag canon-v30,
            CONTENT_COMMIT 857223fcd5e7bc8c8e68f1df768d6e8222b24ee0,
            CANON_SHA256 2a32dcbd61ee7792fc2cb990b7f223e08876d71bf7ddcf5ec432acd055f3986a,
            CANON_BYTES 157167, canon/SHA256SUMS 5 of 5 OK, tag and content
            commit both ancestors of main (head b8d4d58).
            The submission's own basis statement ("v30, not v29") is correct.
INTERNAL    not reachable this session (no credentials). No internal statement
            is relied on. The v184 snapshot pin is neither confirmed nor denied.
ARTIFACTS   verify_li2_pentagon_balance_1.py   sha256 6f9e449ee0d8e3aa8a7f208f8757689eae77c1e617494d8e79183d6396e97e05
            run stdout                          sha256 ea439c3831af84f42bd2c2837e80505c1b778b5c5151619764bf0e864585085e
            break_li2_pentagon_balance_1.py    sha256 0164a199301c10be836709d2d0a2efa43ca78b50227508f53bf95a1c2b264305
            break stdout                        sha256 755d8d614733e131e057978531d68c6c9dcb6152a30467d40d67627d3a61dd49
            verifier 67 checks 0 failures; breaker 29 checks 0 failures 2 hits.
            Ubuntu 24.04.4, x86_64, Python 3.11.15, one architecture only.
PROVENANCE  this is an audit of incoming material, not a preregistered probe.
            The verifier was written after the material was read. It therefore
            carries audit grade, not probe grade. A public probe must be
            preregistered and pinned fresh before first execution.
```

## 1. Verdict first

```text
sections 1, 2      CORRECT and exact. Re-derived independently. Nothing to fix.
section 4          CORRECT, and stronger than the note claims. The printed
                   five-term expression V(-j, 1+j) is a genuine Abel relation:
                   all five arguments match exactly in Z[zeta_5]. I tried to
                   break it and failed.
section 3.1        DOWNGRADE. The "wall uniqueness" is a shaped tautology. Its
                   content is N(N-5) = 0, which is the answer written as the
                   question. It carries no independent information.
section 3.2        OVERCLAIMS. N = 10 also satisfies 1 - r_N = r_N^2. The
                   printed uniqueness is unique-among-odd-N, and the odd
                   restriction was never justified.
section 5          CORRECTLY labelled H, but the stated obstacle is the wrong
                   one. The real obstacle is sharper and is stated in part 6.
the coincidence    WEAKER THAN IT LOOKS. Both legs are confined a priori to
                   zeta(2)Q. The match is 6/5 = 6/5, an equality of rationals.
                   No numerical agreement is evidence here, at any precision.
new result         The balance equation is itself a clean, unshaped selector
                   and it survives both hits. It replaces section 3 entirely.
```

The note is good work. The two hits are in the weakest section, and the
replacement offered in part 4 is strictly stronger than what it replaces.

## 2. What is already public, and what is new

Half the note is already Public Canon v30 and must be quoted, not derived.

```text
Re Li_2(sigma_a(J)) = pi^2/100, 9 pi^2/100      WALL-LI2-RUNG [T]
Galois-orbit real-part sum = pi^2/5             WALL-LI2-RUNG [T]
sum / zeta(2) = 6/5, excess above zeta(2)       WALL-LI2-RUNG [T], explicitly
  = pi^2/30                                       already carries pi^2/30
W_N = pi^2 (N-1)(N-2)/(12N) for all N >= 3      WALL-CIRCLE-LEMMA [T]
|J| = phi^-1, arg J = 2 pi/5                    J-PROJECTIONS [T]
J conj(J) = 2 - phi = phi^-2                    exact, re-verified here
Li_2(phi^-1), Li_2(phi^-2) Landen values        classical, Landen 1780
```

So the excess pi^2/30 is not a discovery of this note. It is printed in the
live registry row. The note's genuine contributions are three:

```text
C1  the collapse. 2 L(r) = 3 L(r^2) obtained by putting x = y = r in Abel's
    five-term relation, and the observation that the collapse condition is
    exactly the golden equation.
C2  the balance. W(J) = 2 L(|J|) = 3 L(J conj(J)), one equation instead of two
    separately computed defects.
C3  the Bloch layer. The golden class as pentagon torsion downstairs and an
    explicit five-term boundary upstairs.
```

C1 and C2 are correct and are worth a candidate. C3 is correct and is worth a
second, separate candidate at H.

## 3. Sections 1, 2 and 4, verified

Every step below was recomputed exactly, in Q(sqrt5) pairs and in
Z[zeta_5] = Z[t]/(1+t+t^2+t^3+t^4), with no float in any assertion.

### 3.1 The load-bearing equation

```text
1 - |J| = |J|^2 = J conj(J)          exact in Q(sqrt5)
```

This is the whole engine. It says the golden modulus point is its own
complement after one squaring. Verified, and tied to the registry: the middle
and right members are J-PROJECTIONS and the modulus chord.

### 3.2 The collapse, and why it is not a coincidence

Put x = y = r in Abel's relation for the Rogers dilogarithm. Both right-hand
arguments become x(1-x)/(1-x^2) = x/(1+x). Setting that equal to x^2 gives,
as an integer polynomial identity,

```text
x - x^2(1+x) = -x(x^2 + x - 1)
```

so the collapse happens if and only if x^2 + x - 1 = 0. The golden point is
not chosen. It is the unique positive point at which Abel's relation degenerates
to two terms. That is the strongest sentence in the note and it survives.

### 3.3 The determinant, stated correctly

The note reads det = -5 as evidence that the 5 is not inserted by hand. Half
right. Exact general lemma, verified over all small (p,q): a collapse
p L(r) = q L(r^2) gives the system [[1,1],[p,-q]] with

```text
det = -(p + q)
```

So det = -5 says exactly one thing: Abel's relation has five terms. That is
clean and it is worth printing, but it is not an independent derivation of
p = 5 from the axiom. The pentagon enters through Abel's relation; it does not
come out of it. Print the lemma, drop the stronger reading.

### 3.4 The Rogers correction, and the channel it cancels

With l = log phi, both corrections equal l^2, so

```text
L(r) - L(r^2) = Li_2(r) - Li_2(r^2) = pi^2/30      corrections cancel
L(r) + L(r^2) = zeta(2)                            corrections add to 2 l^2
```

This is the part with decoder consequences. See part 5.

### 3.5 Section 4 survived the breaker

I expected this to be the weak section and attacked it directly. It held.
The five printed arguments are exactly Abel's five terms at
(x, y) = (-zeta_5, 1 + zeta_5), verified as exact identities in Z[zeta_5]:

```text
(1-x)/(1-xy) = -zeta_5^2   = 1 - J
1 - xy       = 1 + zeta_5 + zeta_5^2 = zeta_5^2 / J
(1-y)/(1-xy) = 1 + zeta_5^2 + zeta_5^3 = -(zeta_5 + zeta_5^4) = -|J|
```

All five agree with the note. Independent witness: the Bloch-Wigner sum over
the five terms is 0 to 3e-16. The relation is real.

Two supporting facts I can prove here and the note did not state:

```text
delta([r]) = r /\ (1-r) = r /\ r^2 = 2(r /\ r) = 0
```

so [r] and [r^2] lie in B(Q(sqrt5)) directly, with no appeal to literature.
Q(sqrt5) is real quadratic, so r_2 = 0 and the Bloch group is finite: beta is
torsion by rank, not by citation. And 5 L(beta) = zeta(2), so beta is
5-torsion under the standard normalisation. That converts most of the note's
[external T] into something checkable in-session. Good. Keep it that way.

## 4. The two hits, and the replacement

### HIT 1, section 3.1 is a shaped tautology

The condition tested is Delta_N = zeta(2)/N. Substituting the exact closed form
Delta_N/zeta(2) = (N^2 - 5N + 2)/(2N) turns it into

```text
N^2 - 5N + 2 = 2      i.e.      N(N - 5) = 0
```

The equation is its own answer. A condition whose normal form is N(N-5) = 0
cannot be evidence that N = 5 is special; it is the assertion that N = 5 is
special, written as an equation. The uniqueness is true and worthless.
Downgrade it from a rigidity claim to a remark, or cut it.

### HIT 2, section 3.2 overclaims

The note restricts to odd N without justification and then concludes over the
whole root-circle family. For even N the minimal nonzero modulus is
2 sin(pi/N), not 2 sin(pi/2N). Sweeping both parities, N = 3..4000:

```text
1 - r_N = r_N^2   holds at   N in {5, 10}
```

because r_10 = 2 sin(pi/10) = phi^-1 exactly. The collapse happens at order 10
too. The printed "N = 5 uniquely" is false as stated.

This is a correction, not a demolition. Q(zeta_10) = Q(zeta_5), so orders 5 and
10 are two root-circle presentations of one field, and both present the same
point. The honest statement is about the field, not the order:

```text
the golden collapse point lies in Q(zeta_5); among all root circles it appears
as the minimal wall modulus at exactly the two orders 5 and 10, which generate
the same field.
```

### The replacement: use the balance equation itself as the selector

Both hits are avoided by testing the balance rather than a shaped defect
condition. This is new and it is the main mathematical result of this audit.

```text
[candidate-T, NON-CANONICAL]  Balance selection

For integer N >= 3, N != 4, let
    r_N = min { |1 + zeta_N^a| : 1 <= a <= N-1, 1 + zeta_N^a != 0 }
        = 2 sin(pi/2N) for odd N,  2 sin(pi/N) for even N,
and let W_N = sum_(a=1)^(N-1) Re Li_2(1 + zeta_N^a) = pi^2 (N-1)(N-2)/(12N)
[WALL-CIRCLE-LEMMA, T]. Then

    W_N = 2 L(r_N)      <=>   N = 5
    W_N = 3 L(r_N^2)    <=>   N = 5

N = 4 is excluded because r_4 = sqrt2 > 1 and Rogers L is not defined there.
```

Proof, elementary and complete:

```text
(i)   W_N/zeta(2) = (N-1)(N-2)/(2N) = (N - 3 + 2/N)/2 is strictly increasing
      for N >= 3. Exact rationals.
(ii)  r_N is strictly decreasing within each parity class, since sin is
      increasing on (0, pi/2] and the argument strictly decreases.
(iii) Rogers L is strictly increasing on (0,1):
      L'(x) = -log(1-x)/(2x) - log(x)/(2(1-x)) > 0, both terms positive.
(iv)  Hence W_N - 2 L(r_N) is strictly increasing within each parity class, so
      it has at most one zero per class.
(v)   N = 5 is a zero: both sides are pi^2/5.
(vi)  The even class has no integer zero: the gap is negative at N = 6 and
      positive at N = 8, so its single crossing is strictly interior.
```

Swept numerically over N = 3..1001 in both parities as corroboration: the only
integer solution of either equation is N = 5. Crucially this selector kills the
N = 10 counterexample that defeats section 3.2:

```text
W_10 = (18/5) zeta(2)          2 L(r_10) = (6/5) zeta(2)          not equal
```

So the balance is a strictly stronger selector than the modulus condition
alone, and it is not shaped: it is the candidate's own equation, asked of every
order in the family.

## 5. HIT 3, the evidential weight of the coincidence

This is the item the note does not raise and it matters more than either hit.

By WALL-CIRCLE-LEMMA, W_N/zeta(2) = (N-1)(N-2)/(2N) is a RATIONAL for every N.
By the collapse, L(r)/zeta(2) and L(r^2)/zeta(2) are rationals. Both legs of
the balance therefore live, a priori and before any computation, in the same
one-dimensional Q-vector space zeta(2)Q. The balance is the statement

```text
6/5 = 6/5
```

an equality of two rational numbers. It follows that no numerical agreement,
at any precision whatsoever, is evidence for a bridge between the two sides.
Verifying the balance to a thousand digits would add nothing. All the content
is in the two derivations, and they are different derivations:

```text
wall leg     Euler reflection plus the boundary evaluation
             Re Li_2(e^(i theta)) = pi^2 B_2(theta/2 pi), a Bernoulli fact.
             Verified here: the canon's boundary formula IS pi^2 B_2, exact.
modulus leg  golden complement plus Abel five-term collapse, a Bloch fact.
```

No morphism between them is exhibited anywhere in the note. State the balance
as an exact equality of two independently derived rationals, and say so. Do not
let it carry the word "explains".

## 6. The real obstacle to section 5, and it is sharper than the five listed

The note lists five technical conditions for the relative-regulator reading
(choice of Bloch group variant, flattenings, relative map, Galois canonicity,
matching the wall operator). Those are all real. But there is a structural
obstacle upstream of all five, and it is new:

```text
Every wall point is already a Bloch class.
```

For z = 1 + zeta_N^a we have 1 - z = -zeta_N^a, a root of unity, verified here
to have order 10 for each of the four Galois images of J. A root of unity is
torsion in K^*, so delta([z]) = z /\ (1-z) = 0 in Lambda^2 tensor Q. The wall
points are in B(Q(zeta_5)) for free, at every N and a.

That is good news and bad news, and the bad news dominates:

```text
good  there is a genuine common home. Both the modulus points and the wall
      points are Bloch classes. The seam the note is reaching for exists.
bad   the canonical regulator on B(Q(zeta_5)) at a complex place is the
      Bloch-Wigner function D, which is IMAGINARY-part data. The Canon's wall
      operator is Re Li_2, which is real-part data and is explicitly not a
      field trace. D(sigma_a(J)) is nonzero (witnesses +0.9238, -0.7848,
      +0.7848, -0.9238) and its orbit sum vanishes trivially by conjugation.
```

So Re Li_2 and D are orthogonal components of the same Li_2 values, and the
wall lives on the component the Bloch regulator does not see. Combined with
part 5, the consequence is precise and it should be written into the H
candidate as its governing constraint:

```text
the relative-regulator hypothesis must explain a RATIONAL, not match a period,
and it must do so with an operator that is provably not the Bloch-Wigner
regulator. A numerical test of it is impossible in principle.
```

That is a harder target than the note assumes, and naming it now prevents a
session from burning itself on numerical agreement.

## 7. The decoder connection

Three findings, one of them negative and worth more than the other two.

### 7.1 Rogers L is the named bridge H-CHANNEL-SEPARATION asks for

The 2026-07-25 memo conjectures H-CHANNEL-SEPARATION: every registered claim
is carried by exactly one J-channel, and nothing mixes them except through a
named bridge. Argument axis carries pi and is rigid; modulus axis carries
log phi and needs an anchor.

At the golden point the ordinary dilogarithm mixes both axes:

```text
Li_2(phi^-1)  = pi^2/10 - log^2 phi        argument content AND modulus content
Li_2(phi^-2)  = pi^2/15 - log^2 phi
```

The Rogers counterterm (1/2) log x log(1-x) is exactly a modulus-channel
counterterm. At the golden point it removes the log^2 phi content completely:

```text
L(phi^-1) = (3/5) zeta(2)       pure argument axis, no log phi
L(phi^-2) = (2/5) zeta(2)       pure argument axis, no log phi
```

So the Rogers dilogarithm is a map with a modulus CARRIER and an argument
VALUE. That is the named-bridge genre in one line, and it is cleaner than the
Landen partition the 2026-07-31 recon proposed under the id
C-LI2-MODULUS-POINTS-1: the partition still carries 2 log^2 phi explicitly,
whereas L cancels it.

### 7.2 It does NOT supply a modulus anchor. Negative result, recorded.

The recon left this open: "Whether it helps anchor the modulus channel (the
blocker behind CURVATURE-OPERATOR-CANONICAL and METRO-EDGE-SCALE) is open and
is not claimed." It is now answered, and the answer is no.

```text
zeta(2)/5 is dimensionless. The Rogers bridge moves the modulus point's VALUE
onto the argument axis; it does not supply a SCALE. An SI anchor requires a
measured quantity, and nothing here is measured.
```

Therefore H-ANCHOR-FORCED is untouched. METRO-EDGE-SCALE is untouched.
CURVATURE-OPERATOR-CANONICAL is untouched. No frontier row moves. Anyone
tempted to read the golden rationalisation as an anchor should stop here.

### 7.3 A concrete repair to the channel-separation probe, before it is written

The memo proposes classifying all registry rows by channel "from their scope
text and value type" and checking three prohibitions mechanically. This
candidate breaks that rule as stated:

```text
carrier channel   MODULUS    (r = |J| = phi^-1,  J conj(J) = phi^-2)
value channel     ARGUMENT   (rational multiples of zeta(2))
```

A classifier keyed on value type alone files this row as argument-side and
never notices it touches the modulus axis at all. The probe must classify
carrier-channel and value-channel as two separate fields, and define a named
bridge as precisely a row where the two differ. That is a one-line amendment to
a preregistration that has not been written yet, which is the cheapest possible
moment to make it.

### 7.4 The lift the note correctly refuses, and why the refusal must stay

The note writes: "the coefficients 2 and 3 arise from the multiplicity of terms
in the five-term relation. It does not follow that 2 is two forces or that 3 is
the spatial dimension. Such an identification would be an additional
unsupported lift."

Correct, and it should be strengthened rather than merely repeated. The 2 and
the 3 are the left and right term counts of Abel's relation. They are a fact
about the dilogarithm, they take the same values at every point where the
collapse occurs, and they have no dependence on J whatsoever. There is nothing
for a decoder reading to attach to. The temptation is strong precisely because
p = 5 and d = 3 are program constants; that is the reason to name the refusal
in the candidate itself, not only in a note.

## 8. What to do

```text
1  Open C-LI2-PENTAGON-BALANCE-1 at candidate-T, scope archimedean special
   values only, carrying the collapse, the balance, the term-count lemma, and
   the balance-selection uniqueness. Drop sections 3.1 and 3.2 as printed.
2  Open C-LI2-RELATIVE-BLOCH-SEAM-2 at candidate-H, carrying the explicit
   Abel relation at (-zeta_5, 1+zeta_5) as verified fact, and the relative
   regulator reading as the hypothesis, with the part 6 constraint written in
   as its governing difficulty.
3  Resolve the id collision with the recon's suggested C-LI2-MODULUS-POINTS-1
   before either is claimed. Content, not id: the balance candidate strictly
   contains the Landen partition the recon proposed, so one lane, not two.
4  Record 7.2 as a closed question on the recon, not as a frontier move.
5  Carry 7.3 into the channel-separation preregistration when it is written.
6  A public probe needs a fresh preregistration and a pin before first
   execution, plus a second architecture. This session ran one architecture
   and wrote its verifier after reading the material. Audit grade only.
```

## 9. Falsifier for this audit

This audit is wrong, and must be corrected before use, if any quoted registry
row text, status or value differs from mathorn1973/twist-j main at tag
canon-v30 with the pins in the header; if the collapse identity
x - x^2(1+x) = -x(x^2+x-1) fails; if the balance-selection proof has a gap in
monotonicity (i), (ii) or (iii); if some integer N >= 3, N != 4, other than 5
satisfies W_N = 2 L(r_N) or W_N = 3 L(r_N^2); if 1 - r_N = r_N^2 holds at some
N outside {5, 10}; if any of the five Abel arguments at (-zeta_5, 1+zeta_5)
differs from the printed value in Z[zeta_5]; if delta([1 + zeta_N^a]) is shown
nonzero in Lambda^2 tensor Q for some N, a; or if either pinned script fails on
exact re-run at the recorded hashes.
