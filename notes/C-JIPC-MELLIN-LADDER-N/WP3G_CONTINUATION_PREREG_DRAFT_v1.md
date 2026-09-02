# JIPC WP3G — rekurentní meromorfní pokračování a globální identity — návrh (DRAFT v1)


Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
ŽÁDNÝ PIN, ŽÁDNÝ BĚH**. Skeleton následníka WP3F; nic nezakládá.

```text
LADDER_STEP              = 3 + 4 (pokračování + globální identity)
PARENTS_REQUIRED         = merged veřejné WP3F (N7-EOC, N7-REC, N7-DUP,
                           N7-EPULL, N7-JOIN), WP3E, WP3D
FOURIER_NEEDED           = NE (pokračování i globální identity jsou algebraické)
BASIS_AT_DRAFT           = Public Canon v74 (refreeze při claim locku)
```

## 0. Přesný cíl

Na `D = {Re s > 0}` má WP3F pět identit: `Ĉ(s+1) = sĈ(s)/(2p_M)`
(REC-D), `Ĉ(s)Ĉ(s+½) = 2^{3/2-2s}Ĉ(2s)` (DUP-D),
`Ê(s)Ô(s) = Ĉ(s)` (EOC-D), `Ê(s) = 2^{s/2-1}Ĉ(s/2)` (EPULL-D),
`Ô(s) = Ê(s+1)` (JOIN-D) — všechny jako věty na `D`, ne jen na
`Q_{>0}`.

WP3G dokazuje:

1. **MEROMORPHIC_CONTINUATION:** `Ĉ`, `Ê`, `Ô` mají jednoznačné
   meromorfní pokračování na celé `C` s efektivními jmény na každém
   racionálním kompaktním obdélníku v kladné racionální vzdálenosti
   od pólů;
2. **POLES_AND_RESIDUES:** póly `Ĉ` jsou přesně `s = −k`, `k ∈ N_0`,
   jednoduché, s rezidui
   \[
   \operatorname{Res}_{s=-k}\hat C=\frac{2\,(2p_M)^{k}(-1)^{k}}{k!}\neq 0 ;
   \]
   póly `Ê` jsou `s = −2k`, póly `Ô` jsou `s = −2k−1`;
3. **GLOBAL_IDENTITIES:** všech pět identit platí jako identity
   meromorfních funkcí na celém `C`.

Bod 3 je obsahem interní povinnosti `O-SCALAR-SEAM` („globální
meromorfní identita“); jeho případná registrace je samostatné fold
rozhodnutí — Canon nemá JIPC řádky.

## 1. Konstrukce (rekurentní, bez Fouriera)

Pro `N ∈ N` polož na `D_N := {Re s > −N} \ {0,−1,…,−N+1}`

\[
\hat C_N(s):=\frac{(2p_M)^{N}\,\hat C(s+N)}{s(s+1)\cdots(s+N-1)} .
\]

- **Konzistence:** z REC-D na `D` plyne `Ĉ_{N+1} = Ĉ_N` na
  `D_N ∩ D_{N+1}` (jedno použití REC-D v bodě `s+N`); `Ĉ_1 = Ĉ` na
  `D`. Sjednocení definuje meromorfní `Ĉ` na `C`.
- **Hodnoty v celých bodech:** iterací REC-D z `Ĉ(1) = 1/p_M > 0`
  je `Ĉ(m) = 2(2p_M)^{-m}(m−1)! > 0` pro celé `m ≥ 1`; nevymizení
  `Ĉ` v kladných celých bodech je tedy věta (z kladnosti `p_M`),
  nevymizení jinde se netvrdí.
- **Rezidua:** v `s = −k` (`0 ≤ k < N`) je
  `Res = (2p_M)^N Ĉ(N−k) / ∏_{j≠k}(j−k) = (2p_M)^N Ĉ(N−k) /
  [(−1)^k k! (N−k−1)!]`, a dosazením `Ĉ(N−k)` z předchozího bodu
  `Res_{s=−k}Ĉ = 2(2p_M)^k(−1)^k/k!`, nezávisle na `N`; nenulové,
  tedy pól je jednoduchý.
- **Ê a Ô:** z EPULL-D a JOIN-D na `D` je pokračování
  `Ê(s) := 2^{s/2-1}Ĉ(s/2)`, `Ô(s) := Ê(s+1)` legitimní (identity
  jsou věty na celém `D`, ne jen na `Q_{>0}`); póly `s/2 = −k`
  resp. `(s+1)/2 = −k`.
- **Efektivní jména:** na racionálním kompaktním obdélníku
  `K ⊂ D_N` v kladné racionální vzdálenosti `d` od pólů má
  `|∏(s+j)| ≥ d^N`, tedy `1/∏(s+j)` má racionální horní mez
  `d^{-N}`; WP3E dodá jméno `Ĉ(s+N)` na `K+N` a jméno
  `(2p_M)^N` vznikne konečným násobením. Reciproční uzel, jeho
  chybová obálka a kanonická volba nejmenšího použitelného `N` jsou
  přesně nové rozhraní `MERO-NAME-ALGEBRA` v §3, nikoli skrytý
  důsledek TCB/v2.

## 2. Globální identity

Obě strany každé z pěti identit jsou meromorfní na `C` (složení
pokračování s afinními mapami `s ↦ s+1, s+½, 2s, s/2`) a rovnají se
na `D` (WP3F). Odečteme je a odstraníme lokálně konečnou sjednocenou
množinu jejich pólů. Na jejím komplementu je rozdíl holomorfní,
mizí na neprázdné otevřené podmnožině `D` a pravidlo
`POLE-AVOIDING-IT-CHAIN` z §3 jej konečným řetězem disků přenese do
každého nepólového bodu. V každém odstraněném bodě proto mají obě
strany totožný **celý Laurentův germ** (včetně hlavní i regulární
části); rovnost reziduí je pouze nutný důsledek a auditní kontrola,
nikoli význam meromorfní rovnosti. Z REC-D ve tvaru
`Ĉ(s) = (2p_M)Ĉ(s+1)/s` plyne zejména

\[
\operatorname{Res}_{s=-k-1}\hat C
=\frac{2p_M}{-k-1}\operatorname{Res}_{s=-k}\hat C ,
\]

což z `2(2p_M)^k(−1)^k/k!` dává `2(2p_M)^{k+1}(−1)^{k+1}/(k+1)!`
(kontrola `k = 0..3` exaktně). Verifier přehrává tento reziduální
řetěz ve formálním Laurentově okruhu `Q[p_M,p_M^{-1}]((z))`, kde
`z` je lokální parametr; žádné numerické `pi` se nevyhodnocuje.

## 3. TCB — `COMPLEX_BALL_MELLIN_TCB/v3`

Dědí se celý TCB/v2 z WP3F. Přírůstky jsou přesně dva:

**MERO-NAME-ALGEBRA (registrované rozšíření nosiče):** k výrazovým
stromům v2 přidává reciproký uzel pouze pro explicitní polynom
`q_N(s)=∏_{j=0}^{N-1}(s+j)` na racionálním kompaktním obdélníku `K`
s certifikovanou racionální separací `d>0` od `{0,−1,…,−N+1}`.
Certifikát dává `|q_N|≥d^N`; uzel nese racionální sup-mez,
ukončující complex-ball evaluátor a standardní inverzní chybovou
obálku. Povoleny jsou dále celočíselné mocniny jména `2p_M`,
racionální afinní pullbacky a konečné součiny/součty z v2. Pro každý
`K` se volí nejmenší `N` s `K+N⊂D`; konzistence `Ĉ_N=Ĉ_{N+1}` na
překryvech dokazuje nezávislost výsledného jména na této volbě.
Žádný obecný neomezený operátor reciproké funkce se nepřidává.

**POLE-AVOIDING-IT-CHAIN (registrované pravidlo):** pro lokálně
konečnou explicitní množinu pólů a dva body jejího komplementu smí
být IT-SEGMENT(ii) iterován jen s konečným certifikátem
`(c_i,r_i)`: sousední disky se neprázdně překrývají, každý uzavřený
disk má kladnou racionální separaci od všech relevantních pólů a
první disk protíná otevřenou oblast, kde je rovnost známa; cílový bod
leží v posledním disku. IT-SEGMENT se používá v domain-generic podobě
WP3F s `Ω = C \ P`. Existence
takového řetězu pro zdejší celočíselné a půlceločíselné množiny pólů
je součástí pravidla; verifier kontroluje jeden nepólový a jeden
zakázaný řetěz.

Žádný Fourier, Poisson, kruhové `pi`, funkcionální rovnice ani
nevymizení mimo kladné celé body se do TCB/v3 nepřidává.

## 4. Auditní povrch (návrh)

```text
JIPC_WP3G_CONTINUATION_AUDIT 1
ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS
RESIDUE_CHAIN K=0..6 RING=Q[p_M,p_M^-1] PASS
INTEGER_VALUES M=1..6 RING=Q[p_M,p_M^-1] PASS
CONSISTENCY_OVERLAP N=1,2 S=1/2+i/2 BITS=2,3 PASS
GLOBAL_IDENTITY_BALLS S=-3/2+i/2 F=5 BITS=2,3 PASS
POLE_AVOIDING_CHAIN S=-3/2+i/2 D=1/2 PASS
PROOF_CONTROLS 12/12 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
```

Rodičovské hashe jsou zámek v textu PREREG (kontroluje reviewer);
verifier žádné soubory nečte a žádnou readback bránu netiskne.
Přesně 12 zmrazených kontrol: mutované reziduum (`k! ↦ (k+1)!`), mutovaný
faktor `(2p_M)^N`, řetěz procházející pólem, obdélník dotýkající se
pólu (`d = 0`), mutovaná konzistence `Ĉ_{N+1} ≠ Ĉ_N`, nárok
nevymizení mimo celé body, nárok funkcionální rovnice, `s` v pólu,
mutovaný pól `Ê` (`−2k ↦ −k`), mutovaná celočíselná hodnota
(`(m−1)! ↦ m!`), mutovaný rozvrh jmen, provenanční stráž `p_M`.

## 5. Ne-nároky a STOP hranice

Nedokazuje se: funkcionální rovnice `s ↔ 1−s` (vyžaduje
Fourier/Poisson, a před nimi identifikaci periody `exp_C` s
`2p_M` — samostatná budoucí proba, navrhované jméno
`P-JIPC-EXP-PERIOD-1`, v této složce nerozepsaná), nevymizení `Ĉ`
mimo celé body (samostatný uzel, potřebný pro logaritmické
derivace), Gamma objekt jménem, kruhové `pi`, archimédovské místo,
L2–L6.

## 6. Podmínky pinu a formální pořadí

Po merge veřejného WP3F: čerstvý collision scan; veřejný claim lock
s tehdejším readback tuple a úplně zmrazeným TCB/v3 včetně obou
přírůstků; jediná formální větev a adresář; společný immutable pin
úplného PREREG a nikdy nespouštěného verifieru; vzdálený readback
obou blobů a statický audit přečtených bajtů; preflight; teprve potom
jediný formální běh. Po dokončeném běhu je `EXPECTED.txt` jediný
stdout artefakt a vzniknou `EXPECTED.txt`, `RUN.md`, `RESULT.md`.
Nedokončí-li se po pinu žádný běh, PREREG a verifier zůstávají
nezměněné a vznikne jen povinný `RESULT.md` se
`Status: ABANDONED`; bez `EXPECTED.txt` a bez `RUN.md`, identifikátor
se nikdy neobnovuje ani znovu nepoužije.
