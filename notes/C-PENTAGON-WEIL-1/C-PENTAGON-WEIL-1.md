# C-PENTAGON-WEIL-1. Pentagon root-filter normalization of zeta, the Weil equivalence, and the gate order for a J-native positive realization

```
CANDIDATE ID:   C-PENTAGON-WEIL-1
DATE:           2026-07-15
SESSION:        pentagon-weil-anchor-1 (incubation lane, this project)
TARGET LINE:    public (mathorn1973/twist-j) on promotion; nothing promoted now
LAYER:          L6 (measure) declared for the future realization probe;
                this document anchors the freeze and verifies the G0 kernel
AUTHORITY:      none. Candidate document per the project contract.
```

## 0. What this document is

The owner delivered a final frozen ledger (Czech, verbatim in section 6)
closing the pentagon root-filter mathematics package: the normalization
Z_J = zeta, the completed form xi_J = xi, the Weil equivalence W_J = W_xi,
the open obligation of a J-native positive realization, and the mandatory
gate order G0 to G6. This document anchors that freeze in the incubation
lane, records an independent verification of the machine-checkable G0
kernel in exact arithmetic, records the attempts to break it, and fixes
the promotion posture. Per contract, in-project labels are candidate
labels; the bare [T]/[O]/[F] of the frozen text bind only after public
validation.

## 1. Provenance and currency gate

Frozen ledger received from the owner 2026-07-15. Archived copy pinned as
a standalone UTF-8 file (trailing newline included):

```
FROZEN_LEDGER_2026-07-15.md
sha256 afa9969920c9bbc41fc6370c207e8ee4d3ec6142b8d064e1438b62d2286c3660
7602 bytes
```

The hash pins this session's archived transcription (the fenced block in
section 6, identical bytes), not the sender's original byte stream. The
transcription preserves the sender's markdown mangling of \boxed and
\\[1mm] as received.

Currency gate, public target, run 2026-07-15 against a fresh clone of
mathorn1973/twist-j main:

```
STATUS.md       STATE ACTIVE, CANON Public Canon v6, TAG canon-v6,
                AUTHORITY mathorn1973/twist-j main, CUTOVER 2026-07-13,
                CONTENT_COMMIT 46f6412943bbd32bd3a686456c36612a1fc8fb3c,
                CANON_SHA256 5b810f0d7d36254d6968f72cd4cefe6956b772e0046ca41f0a9867b3818bb748,
                CANON_BYTES 60697
HEAD            6bb013bafb2d1c06fcb295fdbfce0f86198fd685, Merge Public Canon v6,
                equal to the peeled tag canon-v6
SHA256SUMS      5 of 5 OK (CANON.md, CORE.md, FRONTIER.md, REGISTRY.tsv,
                CHANGELOG.md); canon/CANON.md hash and byte count match
                STATUS.md exactly
GATE            PASS
```

Registry scan: case-insensitive grep for weil, riemann, root filter, P_0
over canon/ returns no rows; every pentagon hit belongs to the
ENTROPY-PENTAGON-QUOTIENT lane, unrelated to this package. The frozen
ledger's claim "publicly unregistered" is confirmed. Project scan: no
prior candidate document for this topic exists in the project; this
document opens the candidate.

## 2. The candidate package

| id | program label | mathematical grade | statement |
| --- | --- | --- | --- |
| PENTAGON-NORMALIZATION | candidate-T | T, classical analysis | f_5(s) := 5^(1-s) - 1 with the real branch of log 5; Z_J := MerCont over Re s > 1 of P_0/f_5 = zeta; xi_J := (1/2) s (s-1) pi^(-s/2) Gamma(s/2) Z_J = xi, entire, with the filter zeros s_k = 1 - 2 pi i k / log 5 removed and the pole and trivial zeros handled standardly |
| J-WEIL-EQUIVALENCE | candidate-T, conditional | T once the five conventions are frozen | W_J built from xi_J equals W_xi identically; RH iff W_J(g) >= 0 on the frozen admissible space. Equivalence only. No step toward RH. |
| J-WEIL-POSITIVE-REALIZATION | O | open | derive a positive realization W_J(g) = \|A_J g\|^2 or <g, H_J g> with H_J >= 0 from declared J-architecture, without zeta, its zeros, a prime table, or the standard Weil form as hidden input |
| RH | O | open | via G5 after exact G2 to G4 closure |
| RAW-P_0-WITHOUT-FILTER-SUBTRACTION | candidate-F | falsified method | exact witness in C4 below; see also the injected tower in section 4b |
| RENAMED-STANDARD-WEIL-AS-NEW-PROOF | candidate-F | falsified method | renaming W_xi to W_J is not a realization |

The frozen text labels the first two rows bare [T]. The mathematics is
classical and sound (section 4); the program labels stay candidate grade
until the public pipeline validates a fold, per contract. No summary here
is stronger than its label.

## 3. Carried input, the one dependency

The ledger uses exactly two facts about P_0 and defines everything else:
P_0(s) = f_5(s) zeta(s) on Re s > 1, and P_0 continues (so P_0(1) = -log 5).
This session reads P_0 as the pentagon root-filter Dirichlet series

```
P_0(s) = sum_{n>=1} c(n) n^(-s),   c(n) = sum_{k=1..4} zeta_5^(k n) = 5*[5|n] - 1,
```

equivalently the sum over the four nontrivial fifth-root directions of the
periodic zeta. Under this reading both facts hold and are verified below
(C1, C3 exactly; entirety and the s = 1 value by imported classical
theorems plus C2 and C5). If the originating session defined P_0
differently, this anchor must be corrected before any promotion; every
downstream row depends only on P_0 = f_5 zeta on Re s > 1.

## 4. Verification record, G0 kernel

```
verifier        verify_pentagon_weil.py
file sha256     24deaef5f4cc8cb8f8d6f5de358f5d20068c7aef6fb50177f5edeca3ba6e1d5b
stdout sha256   e0b6f4f86c12ef06c5ff5be05d5904db63f27e61b5b0402840bb971c474e6cef  (652 bytes)
runtime         under 1 second (limit 120 s)
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform        Linux x86_64, Python 3.11.15 (single platform; a second
                architecture run is required only at public validation)
discipline      Python standard library only; exact arithmetic in every
                assertion (Z[zeta_5] integer four-tuples, Fractions);
                floats printed as witnesses only
```

Exact assertions, all PASS:

```
C1  c(n) = sum_{k=1..4} zeta_5^(kn) = 5*[5|n] - 1, exhaustive over n mod 5,
    exact in Z[zeta_5]. The root-filter coefficient is a congruence filter,
    not a prime filter.
C2  (1-j)(1-j^2)(1-j^3)(1-j^4) = 5 exactly in Z[zeta_5]. Phi_5(1) = 5 =
    N(1-j). Pins P_0(1) = -log 5 with no 2 pi i ambiguity: the four
    principal logs pair conjugately and sum to the real log of a positive
    integer. The residue of the zeta pole reads the norm of (1 - j).
C3  finite root-filter identity, the exact skeleton of P_0 = f_5 zeta:
    sum_{n<=N} c(n) n^(-s) = 5^(1-s) sum_{m<=N/5} m^(-s) - sum_{n<=N} n^(-s),
    exact in Fractions for s in {2,3,4}, N in {5,25,125,625}. The infinite
    statement on Re s > 1 follows by absolute convergence (imported).
C4  raw-carrier asymmetry, the exact reason for the [F] row: the pair
    (2, -1) is s <-> 1-s; f_5(2) = -4/5, f_5(-1) = 24, ratio -1/30, not 1.
    Given xi(2) = xi(-1) = pi/6 > 0 (imported), f_5 xi cannot satisfy the
    functional equation, so the raw carrier cannot host the Weil form.
C5  period sum c(1)+...+c(5) = 0 exactly; partial sums of c are bounded,
    the series converges conditionally for Re s > 0 (imported Dirichlet
    test), so P_0(1) = -log 5 is a genuine series value, not only a
    continuation value.
```

Float witnesses, engineering readouts, printed and not asserted:

```
W1  sum_{n<=10^6} c(n)/n   = -1.609435912436 against -log 5     = -1.609437912434, |diff| 2.000e-06
W2  sum_{n<=10^6} c(n)/n^2 = -1.315947253477 against -2 pi^2/15 = -1.315947253479, |diff| 1.974e-12
```

Imported theorems used, labeled as imports and not claimed as TWIST
results: uniqueness of analytic and meromorphic continuation (identity
theorem); zeta meromorphic with a single simple pole at s = 1, residue 1;
zeta(1 + it) nonzero for t nonzero (Hadamard, de la Vallee Poussin 1896);
xi entire with xi(s) = xi(1-s) (Riemann); the Weil positivity criterion
(Weil 1952; the Bombieri formulation to be fixed at prereg time); the
Dirichlet convergence test; zeta(2) = pi^2/6 (Euler).

### 4a. Divisor bookkeeping (symbolic, recorded)

f_5 is entire with simple zeros exactly at s_k = 1 - 2 pi i k / log 5,
k in Z, since 5^(1-s_k) = exp(2 pi i k) = 1 and f_5'(s_k) = -log 5 times
5^(1-s_k) = -log 5, nonzero. For k nonzero, zeta is holomorphic at s_k
(only pole s = 1), so P_0 = f_5 zeta has a zero there of at least the
order of f_5 and the quotient P_0/f_5 has a removable singularity with
value zeta(s_k). At k = 0 the simple zero of f_5 against the simple pole
of zeta restores the pole: P_0(1) = -log 5 = f_5'(1) times the residue 1.
The boxed correction of the raw path is the log derivative of
P_0 = f_5 zeta: minus zeta'/zeta = minus P_0'/P_0 + f_5'/f_5, with
f_5'/f_5 = log 5 times 5^(1-s) / (1 - 5^(1-s)) after sign cleanup,
matching the frozen text.

### 4b. The exact content of the raw-path correction (derivation note)

For Re s > 1 expand geometrically:

```
f_5'/f_5 (s) = -log 5 * 5^(1-s) / (5^(1-s) - 1) = sum_{m>=1} (log 5 * 5^m) * (5^m)^(-s)
```

so the raw arithmetic side is

```
- P_0'/P_0 (s) = sum_n Lambda(n) n^(-s) - sum_{m>=1} (log 5 * 5^m) * (5^m)^(-s).
```

The uncorrected filter injects a fake prime-power tower at p = 5 with
exponentially growing weight 5^m log 5 at n = 5^m, against the true
Lambda(5^m) = log 5. This is the concrete arithmetic reason the raw path
without divisor subtraction is falsified as a method: the correction is
not a convention, it removes an exponentially weighted counterfeit.

## 5. Break attempts (contract item 4)

```
B1  branch ambiguity in P_0(1). Attempted: sum four principal logs of
    (1 - zeta_5^k) and look for a stray 2 pi i. Closed: conjugate pairs
    cancel the arguments exactly and the product is the positive integer
    5 (C2). No ambiguity survives.
B2  hidden symmetry of the raw carrier. Attempted: find any s <-> 1-s
    symmetry of f_5 xi that would rescue the raw path. Refuted exactly:
    C4 gives the factor -1/30 at the pair (2, -1). The raw completed
    function also carries genuinely extra zeros at s_k on Re s = 1, where
    xi is nonzero (imported Hadamard, de la Vallee Poussin), so any
    explicit-formula reading of it counts spectrum that does not belong
    to zeta. F row stands.
B3  hidden poles from the normalization. Attempted: make P_0/f_5 blow up
    at some s_k with k nonzero. Fails: P_0 = f_5 zeta vanishes there to
    the order of f_5 (4a). No poles are added, none removed except the
    intended restoration at s = 1.
B4  could Z_J differ from zeta anywhere. No: the identity holds on the
    open half plane Re s > 1 and meromorphic continuation on the
    connected plane is unique (imported). Z_J = zeta is total.
B5  smuggled progress. Attempted reading of the equivalence as an RH
    step. It is a renaming; the freeze itself pins that reading as [F]
    (RENAMED-STANDARD-WEIL-AS-NEW-PROOF). The package's value is the
    normalization discipline and the gate order, not RH progress.
```

Nothing broke. The package survives one honest independent attempt.

## 6. Frozen ledger, verbatim (Czech, archived copy, sha256 afa99699...c3660)

```
# STATUS: KONEČNÉ ZMRAZENÍ PŘIJATO
**MĚNOVÁ BRÁNA [PASS].** Veřejný `main` nadále deklaruje stav ACTIVE, Public Canon v6, tag `canon-v6`, s autoritou `mathorn1973/twist-j main`. Veřejný registr je autoritativní ledger a samotný statusový štítek v narativu ještě nevytváří veřejný claim. ([GitHub][1])
Tvoje dopředná pojistka je nutná. Syrová funkce (\mathcal P_0) není správný nosič Weilovy formy bez explicitní korekce kořenového filtru.
## 1. Zmrazená normalizace [T]
Nejprve se musí fixovat větev
[
5^{1-s}:=\exp!\bigl((1-s)\log 5\bigr),
\qquad \log 5>0,
]
a položit
[
f_5(s):=5^{1-s}-1.
]
Pro (\operatorname{Re}s>1) platí
[
\mathcal P_0(s)=f_5(s)\zeta(s).
]
Proto jednoznačnost meromorfního pokračování dává
[
\boxed{
Z_J(s):=
\operatorname{MerCont}_{\operatorname{Re}s>1}
\frac{\mathcal P_0(s)}{f_5(s)}
==============================
\zeta(s).
}
]
Toto není zavedení nové funkce. Je to přesná normalizace root-filter reprezentace zety.
Nuly filtru jsou
[
s_k=1-\frac{2\pi i k}{\log 5},
\qquad k\in\mathbb Z.
]
Pro (k\neq0) je (\zeta) holomorfní a podíl má odstranitelné singularity. Pro (k=0), tedy (s=1),
[
\mathcal P_0(1)=-\log 5,
]
zatímco normalizovaný podíl obnoví standardní jednoduchý pól (\zeta).
Dokončená normalizace je proto
[
\boxed{
\xi_J(s):=
\frac12s(s-1)\pi^{-s/2}
\Gamma!\left(\frac s2\right)Z_J(s)
==================================
\xi(s).
}
]
Faktor (s-1) odstraní pól (Z_J=\zeta) v (s=1). Faktor (s) spolu s Gamma faktorem zajistí standardní odstranitelnost v (s=0). Výsledkem je standardní celistvá funkce (\xi), bez root-filter nul na (\operatorname{Re}s=1).
## 2. Dvě korektní cesty
### Čistá cesta
Pracovat výhradně s
[
Z_J(s)=\zeta(s),
\qquad
\xi_J(s)=\xi(s).
]
Tato cesta automaticky odstraní umělý divisor (f_5). Pro Weilovu formu je to správná výchozí normalizace.
### Syrová cesta
Pracovat s (\mathcal P_0), ale v každém logaritmickém nebo explicitním vzorci připojit přesnou korekci:
[
\boxed{
-\frac{\zeta'}{\zeta}(s)
========================
-\frac{\mathcal P_0'}{\mathcal P_0}(s)
+
\frac{f_5'}{f_5}(s)
}
]
s
[
\frac{f_5'}{f_5}(s)
===================
\log5,
\frac{5^{1-s}}{1-5^{1-s}}.
]
V jazyce divisorů to znamená přesně odečíst nuly (f_5), jejich násobnosti a příslušné konstantní členy explicitní formule. Tyto nuly nejsou aritmetickým spektrem zety. Jsou artefaktem konečného kořenového filtru.
První cesta je kanonicky čistší.
# 3. Dva budoucí claimy
## `J-WEIL-EQUIVALENCE` [T matematicky, veřejně neregistrováno]
Nechť je jednou provždy zmrazeno:
1. přesné Weilovo testovací prostředí (\mathcal W),
2. Fourierova nebo Mellinova konvence,
3. Gamma normalizace,
4. zacházení s póly a triviálními nulami,
5. konjugace a involuce na testovacích funkcích.
Definujme (W_J) jako standardní Weilovu formu vytvořenou z (\xi_J). Protože
[
\xi_J=\xi,
]
platí identicky
[
\boxed{W_J=W_\xi.}
]
Tedy standardní Weilovo kritérium přepsané přes (\xi_J) je matematicky ekvivalentní standardnímu kritériu pro (\xi). To je T, ale nepřináší nový krok směrem k RH.
Přesný statusový obsah je:
[
\boxed{
\mathrm{RH}
\iff
W_J(g)\ge0
\quad\text{pro všechny přípustné }g\in\mathcal W.
}
]
T zde označuje ekvivalenci. Neoznačuje dokázanou pravou stranu.
## `J-WEIL-POSITIVE-REALIZATION` [O]
Otevřený závazek je podstatně silnější:
> Odvodit z předem deklarované (J)-architektury novou pozitivní realizaci přesně téže formy (W_J), například
> [
> W_J(g)=|A_Jg|^2
> ]
> nebo
> [
> W_J(g)=\langle g,H_Jg\rangle,
> \qquad H_J\ge0,
> ]
> a nezavést přitom (\zeta), její nuly, tabulku prvočísel ani standardní Weilovu formu jako skrytý vstup.
Toto je skutečný RH program. Pouhé označení
[
W_\xi\longmapsto W_J
]
není realizace. Je to přejmenování.
# 4. Povinné pořadí bran
Budoucí sonda musí projít v tomto pořadí:
[
\begin{array}{ll}
\mathrm{G0} &
\mathcal P_0/f_5=Z_J=\zeta
\text{ jako přesná meromorfní identita},[1mm]
\mathrm{G1} &
\xi_J=\xi
\text{ včetně pólů, triviálních nul a Gamma faktoru},[1mm]
\mathrm{G2} &
W_J=W_\xi
\text{ na přesně zmrazeném testovacím prostoru},[1mm]
\mathrm{G3} &
\text{aritmetická strana reprodukuje přesně }
\Lambda(n),[1mm]
\mathrm{G4} &
\text{archimédovský člen souhlasí přesně},[1mm]
\mathrm{G5} &
W_J(g)\ge0
\text{ pro všechny přípustné }g,[1mm]
\mathrm{G6} &
\text{pozitivita je odvozena z deklarované architektury,
nikoli importována.}
\end{array}
]
G0 až G2 jsou ekvivalenční účetnictví. G3 a G4 dokazují, že navržená konstrukce je skutečně správná globální forma. G5 je RH zeď. G6 je podmínka novosti a (J)-nativnosti.
## Logická disciplína negativního vektoru
Je důležité zachovat pořadí:
* záporný vektor **před uzavřením G2 až G4** falsifikuje navrženou realizaci;
* záporný vektor **po přesném uzavření G2 až G4** by falsifikoval pozitivitu standardní Weilovy formy, tedy RH.
Negativní výsledek nesmí být předčasně interpretován jako protipříklad k RH, pokud ještě není dokázána přesná rovnost forem.
# 5. Preregistrační zmrazení
Pro `J-WEIL-POSITIVE-REALIZATION`:
[
\boxed{\text{vrstva: L6, measure}}
]
s pěti povinnými poli:
| Pole              | Zmrazený obsah                                                                                                   |
| ----------------- | ---------------------------------------------------------------------------------------------------------------- |
| Equation          | přesná definice (W_J), testovací prostor a tvrzení (W_J=W_\xi)                                                   |
| Code version      | pin zdrojového souboru před prvním během                                                                         |
| Dataset           | žádný externí seznam nul ani prvočísel; případné testovací funkce generované deklarovaným pravidlem              |
| Systematics       | větev (\log5), Fourierova konvence, Gamma člen, divisor (f_5), póly, triviální nuly, uzávěr testovacího prostoru |
| Failure threshold | jediný přesný nesoulad nebo jediný přípustný (g) s (W_J(g)<0)                                                    |
Samostatný named gate je nutný pro každý přechod z konečného pentagonového paketu nebo kernelové vrstvy do globální L6 formy. Žádný takový lift nevzniká slovem „Weil“.
# Konečný ledger návrhu
[
\boxed{
\begin{array}{lll}
\text{PENTAGON-NORMALIZATION} & [T] &
Z_J=\zeta,\quad \xi_J=\xi,[1mm]
\text{J-WEIL-EQUIVALENCE} & [T] &
\text{standardní forma pouze přepsána přes }\xi_J,[1mm]
\text{J-WEIL-POSITIVE-REALIZATION} & [O] &
\text{nová pozitivní reprezentace z }J,[1mm]
\text{RH} & [O],&[1mm]
\text{RAW-}\mathcal P_0\text{-WITHOUT-FILTER-SUBTRACTION} & [F],&[1mm]
\text{RENAMED-STANDARD-WEIL-AS-NEW-PROOF} & [F].&
\end{array}
}
]
**KONEČNÝ STATUS: PENTAGONOVÝ MATEMATICKÝ BALÍK UZAVŘEN. NORMALIZACE UZAVŘENA [T]. WEILOVA EKVIVALENCE [T]. NOVÁ POZITIVNÍ (J)-REALIZACE [O]. RH [O].**
Poslední kruh není další identita. Je to kladnost přesně normalizované globální formy, odvozená bez skrytého vložení problému, který má vyřešit.
[1]: https://github.com/mathorn1973/twist-j "GitHub - mathorn1973/twist-j: TWIST-J investigates one simple, risky hypothesis:  Physical reality is not, at bottom, a continuous field on a pre-given spacetime. It is a closed, exact, deterministic integer system. Continuum, geometry, probability and fields are its large-scale readings. · GitHub"
```

## 7. Gate map, frozen order, current state

```
G0  P_0/f_5 = Z_J = zeta          CLOSED at candidate grade by this document,
                                  modulo the carried input of section 3
G1  xi_J = xi                     CLOSED as accounting; Gamma and pi facts imported
G2  W_J = W_xi on frozen space    OPEN until the five conventions are frozen in PREREG
G3  arithmetic side = Lambda(n)   OPEN, per proposed realization
G4  archimedean term exact        OPEN, per proposed realization
G5  W_J(g) >= 0                   OPEN, the RH wall
G6  positivity derived, not       OPEN, the novelty and J-nativeness condition
    imported
```

Negative-vector discipline as frozen: before G2 to G4 close, a negative
vector kills the proposed realization, not RH. Only after exact closure of
G2 to G4 would an admissible negative vector bear on RH itself.

## 8. Promotion posture

No public registration now. J-WEIL-EQUIVALENCE alone adds no public step;
the frozen text says so itself. When the owner opens the RH lane publicly,
the fold should carry: the O row J-WEIL-POSITIVE-REALIZATION with its
falsifier, the two F guard rows as method falsifications, and the G0 to G6
gate order with the negative-vector discipline. Prereg layer L6, five
fields as frozen in the ledger, no external zero or prime lists as data,
and one named gate per lift from any finite pentagon packet or kernel
layer to the global L6 form. The fold decision is the owner's. No T by
talk; no canon by living in the project.

## 9. Live falsifiers, candidate scope

```
F-a  any n with c(n) != 5*[5|n] - 1 (killed exhaustively over residues, C1)
F-b  any exact finite-range violation of the C3 identity
F-c  a demonstration that the originating P_0 differs from f_5 zeta on
     Re s > 1 (this would retire the whole package, not repair it)
F-d  for the future realization: one admissible g with W_J(g) < 0 before
     G2 to G4 close kills the realization; after exact closure such g
     would falsify RH and must be handled per the negative-vector
     discipline, never announced prematurely
```

## 10. Public probe record (added 2026-07-15, after owner registration)

The owner registered and ran the public validation of this candidate as
probe P-PENTAGON-WEIL-1 on mathorn1973/twist-j:

```
Issue           #41
Draft PR        #42 (intentionally draft, unmerged; registry and Canon
                untouched)
Branch          probe/P-PENTAGON-WEIL-1, path probes/P-PENTAGON-WEIL-1/
                (PREREG.md, verify.py, EXPECTED.txt, RUN.md, RESULT.md;
                five files of a single probe)
Prereg pin      6be1231a4366dbcc04f7251afe7adb44df555250
Final head      a7ff00565591a3d0019f2147ab32f3212c5c4cbb
aarch64 run     6/6 PASS, exit 0, empty stderr
GitHub x86_64   byte-identical output; policy workflow 29451642640 success
stdout sha256   f042368571e4f3d302a6cfbe47c6d344bcdf8411d9dd4dca3a21aa9f216797fe
Scope           G0/L5 normalization accounting only; no Weil positivity or
                RH claim; RH and Weil positivity remain [O]
```

Third-environment reproduction by this session (2026-07-15): fetched the
probe branch, ran verify.py from repo root under LC_ALL=C LANG=C
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC on Linux x86_64
(Python 3.11.15, independent environment, same architecture as the GitHub
check): 6/6 PASS, exit 0, empty stderr, stdout byte-identical to
EXPECTED.txt, sha256 equal to the pin above. The public verifier is the
owner's independent implementation (six gates G01-G06, including the
signed raw coefficient (1-5^m) log 5 and correction +5^m log 5 through
m = 12), distinct from this candidate's verifier: the two code paths
confirm each other.

Candidate status after this record: publicly reproduced at G0 scope on two
architectures plus one independent environment; fold pending at the
owner's discretion. The successor work is C-WEIL-REALIZATION-1 and
O-WEIL-REALIZATION_RECON_2026-07-15 (attack on the remaining [O] rows).

## Appendix A. Verifier source (pinned 24deaef5f4cc8cb8f8d6f5de358f5d20068c7aef6fb50177f5edeca3ba6e1d5b)

~~~python
#!/usr/bin/env python3
# verify_pentagon_weil.py
# Candidate C-PENTAGON-WEIL-1: exact verification of the G0 kernel of the
# pentagon root-filter normalization  Z_J := MerCont(P0/f5) = zeta,
# with f5(s) = 5^(1-s) - 1 and P0(s) = sum_n c(n) n^(-s),
# c(n) = sum_{k=1..4} zeta_5^(k n).
#
# Discipline: Python 3 standard library only. Exact arithmetic in every
# assertion (integers, Z[zeta_5] four-tuples, Fractions). Floats appear only
# in printed engineering witnesses, never in an assertion.
# Frozen environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
# PYTHONHASHSEED=0 TZ=UTC. Deterministic output.

from fractions import Fraction
import math

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ---------------------------------------------------------------------------
# Z[zeta_5], basis (1, j, j^2, j^3), reduction j^4 = -(1+j+j^2+j^3), j^5 = 1.
# ---------------------------------------------------------------------------
def zmul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    r = [c[0] + c[5], c[1] + c[6], c[2], c[3]]  # fold j^5 -> 1, j^6 -> j
    k4 = c[4]                                    # spread j^4
    return (r[0] - k4, r[1] - k4, r[2] - k4, r[3] - k4)

def zpow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = zmul(r, a)
    return r

J5 = (0, 1, 0, 0)  # j = zeta_5

# C1: root-filter coefficient. For every residue r mod 5:
#     sum_{k=1..4} j^(k r) = 4 if r = 0, else -1, exactly in Z[zeta_5].
# Exhaustive over residues covers all n by periodicity.
ok = True
for r in range(5):
    s = (0, 0, 0, 0)
    for k in range(1, 5):
        t = zpow(J5, (k * r) % 5)
        s = tuple(x + y for x, y in zip(s, t))
    want = (4, 0, 0, 0) if r == 0 else (-1, 0, 0, 0)
    ok = ok and (s == want)
check("C1 c(n) = sum_k zeta_5^(kn) = 5*[5|n] - 1, exhaustive over n mod 5, exact in Z[zeta_5]", ok)

# C2: prod_{k=1..4} (1 - j^k) = 5 exactly in Z[zeta_5].
# This is Phi_5(1) = 5 = N(1 - j). It pins P0(1) = -log 5 with no 2*pi*i
# ambiguity: the four principal logs pair conjugately and their sum is the
# real log of this positive integer.
p = (1, 0, 0, 0)
for k in range(1, 5):
    jk = zpow(J5, k)
    term = tuple((1 if i == 0 else 0) - jk[i] for i in range(4))
    p = zmul(p, term)
check("C2 (1-j)(1-j^2)(1-j^3)(1-j^4) = 5, exact in Z[zeta_5]", p == (5, 0, 0, 0))

# C3: finite root-filter regrouping, the exact skeleton of P0 = f5 * zeta:
#     sum_{n<=N} c(n) n^(-s) = 5^(1-s) * sum_{m<=N/5} m^(-s) - sum_{n<=N} n^(-s)
# exact in Fractions for integer s >= 2 and N a multiple of 5.
ok = True
for s in (2, 3, 4):
    for N in (5, 25, 125, 625):
        lhs = sum(Fraction(4 if n % 5 == 0 else -1) / Fraction(n) ** s
                  for n in range(1, N + 1))
        rhs = (Fraction(1, 5 ** (s - 1))
               * sum(Fraction(1) / Fraction(m) ** s for m in range(1, N // 5 + 1))
               - sum(Fraction(1) / Fraction(n) ** s for n in range(1, N + 1)))
        ok = ok and (lhs == rhs)
check("C3 finite identity sum c(n)n^-s = 5^(1-s) sum m^-s - sum n^-s, s in {2,3,4}, N in {5,25,125,625}, exact Fractions", ok)

# C4: the raw carrier f5*xi cannot satisfy the s <-> 1-s functional equation.
# The pair (2, -1) is s <-> 1-s. Exact rationals:
#     f5(2) = 5^(-1) - 1 = -4/5,   f5(-1) = 5^2 - 1 = 24,
#     ratio f5(2)/f5(-1) = -1/30 != 1.
# Given xi(2) = xi(-1) != 0 [imported: functional equation; xi(2) = pi/6 > 0],
# f5(s)*xi(s) at 2 and -1 differ by the exact factor -1/30, so symmetry fails.
f5_2 = Fraction(1, 5) - 1
f5_m1 = Fraction(25) - 1
check("C4 raw-carrier asymmetry: f5(2) = -4/5, f5(-1) = 24, ratio -1/30 != 1, exact",
      f5_2 == Fraction(-4, 5) and f5_m1 == 24
      and f5_2 / f5_m1 == Fraction(-1, 30) and f5_2 != f5_m1)

# C5: the full period sum vanishes: c(1)+...+c(5) = 0.
# Bounded partial sums; the Dirichlet series converges conditionally for
# Re s > 0 [imported Dirichlet test], so P0(1) = -log 5 is a series value.
check("C5 period sum c(1..5) = 0, exact",
      sum(4 if r % 5 == 0 else -1 for r in range(1, 6)) == 0)

# ---------------------------------------------------------------------------
# Engineering witnesses. Floats, printed only, asserted never.
# ---------------------------------------------------------------------------
N = 10 ** 6
acc = 0.0
for n in range(1, N + 1):
    acc += (4.0 if n % 5 == 0 else -1.0) / n
print("W1 witness sum_{n<=1e6} c(n)/n   = %.12f ; -log 5     = %.12f ; |diff| = %.3e"
      % (acc, -math.log(5.0), abs(acc + math.log(5.0))))

acc2 = 0.0
for n in range(1, N + 1):
    acc2 += (4.0 if n % 5 == 0 else -1.0) / (n * n)
print("W2 witness sum_{n<=1e6} c(n)/n^2 = %.12f ; -2*pi^2/15 = %.12f ; |diff| = %.3e"
      % (acc2, -2.0 * math.pi ** 2 / 15.0, abs(acc2 + 2.0 * math.pi ** 2 / 15.0)))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS G0 kernel at candidate grade" if not FAILED else "FAIL"))
~~~

## Appendix B. Verifier stdout (pinned e0b6f4f86c12ef06c5ff5be05d5904db63f27e61b5b0402840bb971c474e6cef, 652 bytes)

```
PASS C1 c(n) = sum_k zeta_5^(kn) = 5*[5|n] - 1, exhaustive over n mod 5, exact in Z[zeta_5]
PASS C2 (1-j)(1-j^2)(1-j^3)(1-j^4) = 5, exact in Z[zeta_5]
PASS C3 finite identity sum c(n)n^-s = 5^(1-s) sum m^-s - sum n^-s, s in {2,3,4}, N in {5,25,125,625}, exact Fractions
PASS C4 raw-carrier asymmetry: f5(2) = -4/5, f5(-1) = 24, ratio -1/30 != 1, exact
PASS C5 period sum c(1..5) = 0, exact
W1 witness sum_{n<=1e6} c(n)/n   = -1.609435912436 ; -log 5     = -1.609437912434 ; |diff| = 2.000e-06
W2 witness sum_{n<=1e6} c(n)/n^2 = -1.315947253477 ; -2*pi^2/15 = -1.315947253479 ; |diff| = 1.974e-12
FAILED: none
VERDICT: PASS G0 kernel at candidate grade
```
