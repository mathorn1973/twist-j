# JIPC WP3F — E·O=C na Re(s)>0 — návrh preregistrace (DRAFT v2)

Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
ŽÁDNÝ PIN, ŽÁDNÝ BĚH**. Verze 2 zapracovává red-team kolo 1
(23 nálezů: 1 fatální — nedetekovatelná π-mutace; řetěz disků pro
`t<0`; chybějící POW_RAT↔exp-log identifikace; režim veřejná/interní;
WP3B lock; bajtová jména bran; pořadí EXPECTED).

## 0.0 REŽIM — rozhodnutí správce před pinem

WP3E disciplína: veřejná proba nesmí mít privátní premisu („private
parent is discovery context at most“). Uzel N3 spotřebovává
WP3D-QPOS, který je dnes interní. Dvě přípustné cesty:

- **(A) doporučená:** nejdřív publikovat racionální řez jako veřejnou
  probu `P-JIPC-WP3D-QPOS-MELLIN-1` (obsah je exaktně kernelově
  přehratelný — ideální veřejný materiál); potom WP3F jako veřejná
  proba s plným candidate-T stropem;
- **(B):** WP3F vést jako interní balík (řada WP3C/WP3D) bez
  veřejného candidate-T stropu.

Do rozhodnutí je tento dokument režimově neutrální; všechna lock pole
jsou TBD.

## 0. Přesný cíl

Jediná cílová věta (žebřík WP3D §12, krok 2):

\[
\boxed{\hat E(s)\,\hat O(s)=\hat C(s)
\qquad\text{pro všechna } s\in D:=\{\Re s>0\}}
\tag{EOC-D}
\]

pro oblečená Mellinova semena WP3E (zmrazené trojice `E=(2,1,0,1)`,
`O=(2,1,1,1)`, `C=(4,2,0,2)`, váha `p_M`):

\[
\hat E(s)=2\!\int_0^\infty\! e^{-p_M x^2}x^{s-1}dx,\quad
\hat O(s)=2\!\int_0^\infty\! e^{-p_M x^2}x^{s}dx,\quad
\hat C(s)=4\!\int_0^\infty\! e^{-2p_M r^2}r^{2s-1}dr .
\]

Strategie: (1) racionální svědek z WP3D-QPOS na `Q_{>0}`;
(2) holomorfnost + efektivní jména z WP3E; (3) věta o identitě
(jediný nový TCB kus). Racionální řez je svědková množina; WP3E
firewall se ctí (identitu vlastní až tento probe).

### 0.1 Ne-nároky

Nedokazuje se: meromorfní pokračování (krok 3 žebříku), funkcionální
rovnice, Fourier/Poisson, Gamma objekt, kruhové `pi`, archimédovské
místo, globální WP2 šev, žádný L2–L6 lift, SAMPLING NOT PROVIDED.
Uzel N1 identifikuje **dvě interní Cauchyho jména téže konstanty**
(Machinovo a WP3B integrální); žádné kruhové čtení se nezavádí a
brány `STANDARD_PI_IDENTIFICATION` a `CIRCLE_PI_IDENTIFICATION`
zůstávají v rodičovských hodnotách.

## §1. TCB: `COMPLEX_BALL_MELLIN_TCB/v2`

Dědí se celý `COMPLEX_BALL_MELLIN_TCB/v1` z WP3E. Přírůstky (dva):

**IT-SEGMENT (registrované pravidlo):** nechť `f` je holomorfní na
otevřeném disku `B(c,r)⊆D` (střed i poloměr libovolné reálné;
racionalita se nevyžaduje — klasický důkaz je na ní nezávislý).
(i) Je-li `c` reálné a `f=0` na reálném průměru `{c+x:x∈(−r,r)}`,
pak `f=0` na `B(c,r)`. (ii) Je-li `f=0` na neprázdné otevřené
podmnožině `B(c,r)`, pak `f=0` na `B(c,r)`.
Vnitřní klasický důkaz (Taylor/Cauchy) je součástí registrace, na
téže důvěrové úrovni jako v1 pravidlo „holomorfnost lokálně
stejnoměrné limity“ (klasicky rovněž Cauchy/Morera). Cauchyho
normalizační konstanta se nevyskytuje v žádném tvrzení ani ve
výpočetní vrstvě; hranicí je registrace pravidla.

**POW-EXPLOG-ID (drobné registrované rozhraní):** jednoznačnost
kladného `n`-tého kořene (z ryzí monotonie `y↦yⁿ` na `(0,∞)`),
umožňující uzel N2a. Nic dalšího; zejména žádný POW_RAT kalkul se
nepřenáší.

Uzly N1 (Machinův most) se dokazují celé v /v1 prostředcích
(kompaktní FTC, derivační algebra, racionální aritmetika).

## §2. Důkazový graf

### N1 — MACHIN_BRIDGE: `p_M = pi_atan` (WP3B)

WP3E výslovně neidentifikuje `p_M` s žádnou jinou konstantou; WP3D je
typován k `pi_atan=4F`, `F=∫_0^1 dt/(1+t²)` (WP3B). Uzel:

\[
\boxed{16A_5-4A_{239}=4\!\int_0^1\!\frac{dt}{1+t^2}} .
\]

1. **N1a (řadové jméno = integrál).** Pro racionální `x∈[0,2]` polož
   `A(x)=∫_0^x dt/(1+t²)` (kompaktní integrál spojitého integrandu).
   Konečná geometrická identita
   `1/(1+t²)=Σ_{n=0}^{N}(−1)^n t^{2n}+(−1)^{N+1}t^{2N+2}/(1+t²)`
   a FTC dávají pro `x=1/q` (ve zmrazené WP3E konvenci
   `S_{q,N}=Σ_{n=0}^{N-1}(−1)^n a_{q,n}`):
   \[
   A(1/q)=S_{q,N+1}+(-1)^{N+1}\rho_{N},\qquad
   0\le\rho_N\le a_{q,N+1},
   \]
   tedy zbytek má znaménko `(−1)^{N+1}` a velikost `≤a_{q,N+1}`,
   takže `A(1/q)∈hull(S_{q,N},S_{q,N+1})` pro každé `N`; z
   jednoznačnosti společného bodu Machinových intervalů
   `A(1/q)=A_q`.
2. **N1b (adiční zákon).** Pro racionální `u,v≥0`, `uv<1`,
   `(u+v)/(1−uv)≤2`:
   `A(u)+A(v)=A((u+v)/(1−uv))`. Důkaz: derivace složené strany je
   `1/(1+x²)` díky přesné polynomiální identitě
   \[
   \boxed{(1-uv)^2+(u+v)^2=(1+u^2)(1+v^2)},
   \]
   rozdíl má nulovou derivaci a mizí v `x=0`; FTC uzavírá.
3. **N1c (kompozice).** Tři aplikace N1b s **krácicími svědky**
   (křížové součiny, kernel je přehrává exaktně):
   - `2A(1/5)=A(5/12)`: `(2/5)/(24/25)=10/24=5/12`,
     svědek `10·12=24·5=120`; `uv=1/25<1`, hodnota `5/12≤2`;
   - `2A(5/12)=A(120/119)`: `(5/6)/(119/144)=720/714=120/119`,
     svědek `720·119=714·120=85680`; `uv=25/144<1`, `120/119≤2`;
   - `A(1)+A(1/239)=A(120/119)`: `(240/239)/(238/239)=240/238
     =120/119`, svědek `240·119=238·120=28560`; `uv=1/239<1`,
     `120/119≤2`.
   Tedy `4A(1/5)−A(1/239)=A(1)=F` a po vynásobení čtyřmi
   `16A_5−4A_{239}=4F`. ∎ *(Kosmetická poznámka mimo audit:
   subtraktivní forma vede na `28561=13⁴`.)*

Konzistence zdarma: WP3B mez `3<4F<16/5` a WP3E mez `3<p_M<16/5` se
po N1 týkají téže konstanty. **Toto je konzistenční, nikoli
diskriminační pozorování** — žádná obálková disjunkce se nikde
netestuje (viz fatální nález kola 1): konečný audit N1 nesou výhradně
exaktní racionální svědci výše.

### N2 — SLICE_OBJECT_IDENTIFICATION (po N1)

Pro reálné `s∈Q_{>0}` se WP3E objekty rovnají WP3D objektům. Tři
pojmenované pod-uzly:

- **N2a POW_RAT_EXP_LOG_ID:** pro `x>0` a `r=m/n` splňuje
  `exp_R(r·log_R x)` rovnici `y^n=x^m` a je kladné (produktový zákon
  `exp` + inverze `log`); jednoznačnost kladného kořene
  (POW-EXPLOG-ID) je ztotožní s WP3D hodnotou `x^r` (POW_RAT).
  Vede se v /v2; WP3D fixture „žádný exp/log ve třídě WP3D“ se
  nedotýká — políčkuje konstrukci uvnitř WP3D, ne identifikaci
  hodnot ve WP3F.
- **N2b SUP_EQUALS_LIMIT:** integrand je pro reálné `s>0` kladný,
  síť kompaktních řezů monotónní; monotónní supremum (WP3D TRUNC-0)
  = Cauchyho limita sítě (WP3E) z úplnosti. Explicitní lemma, obě
  strany /v1+/v2.
- **N2c COFINAL_CUTS:** WP3E within-branch kompatibilita
  `u`-formy s poloosovou formou (WP3E §1.11) + kofinalita řezů
  `(δ,R)↔(e^{u_-},e^{u_+})`. Žádné křížové čtení větví.

### N3 — RATIONAL_WITNESS (spotřeba WP3D-QPOS)

Z uzamčeného WP3D-QPOS-MELLIN (koncový uzel
`WP3D_QPOS_SCALAR_SLICE`): `\hat E(s)\hat O(s)=\hat C(s)` pro
`s∈Q_{>0}`; po N1+N2 výrok o WP3E objektech s vahou `p_M`.
Režimová podmínka §0.0 určuje, zda je citovaný artefakt veřejný.

### N4 — PRODUCT_EFFECTIVE_NAME

Jsou-li `P_j^{(n)}` WP3E aproximanty s chybou `≤2^{-(n+1)}` na `K`,
polož **n-uniformní** racionální meze

\[
M_j:=\overline{\sup_K}\,|P_j^{(1)}|+1
\qquad(j\in\{E,O\}),
\]

kde `\overline{\sup_K}` je racionální horní mez supréma konečné
exponenciální sumy na obdélníku `K`: `|Σc_ke^{α_ks}|≤Σ|c_k|·
e^{\Re α_k·σ^*_k}` s `σ^*_k` = ten kraj `K`, který maximalizuje
`\Re α_k·σ` (monotonie v `σ`), vyhodnoceno exp-obálkou /v1.
`M_j` skutečně majorizuje každé `|P_j^{(n)}|` i `|F_j|` na `K`
(`|P^{(n)}|≤|P^{(1)}|+2^{-2}+2^{-(n+1)}≤\overline{\sup}|P^{(1)}|+1`).
Pak pro `ε=2^{-(n+1)}≤1`

\[
\sup_K|P_E^{(n)}P_O^{(n)}-F_EF_O|\le(M_E+M_O+1)\,\varepsilon,
\]

a jméno funkce `f:=F_EF_O-F_C` má rozvrh

\[
n\mapsto n+\lceil\log_2(M_E+M_O+1)\rceil+2
\]

(`+1` za součin, `+1` za rozdíl s `F_C`). `f` je holomorfní na `D`
s efektivním jménem na každém racionálním kompaktním obdélníku.

### N5 — RAY_VANISHING (bez nového TCB)

`f=0` na `(0,∞)`: racionální `s_k→σ`, `f(s_k)=0` (N3), spojitost
s modulem z efektivního jména; hustota = archimédovská kofinalita.

### N6 — DISK_CHAIN_PROPAGATION

Pro `s=σ+it∈D` polož `r=σ/2` a řetěz

\[
c_k=\sigma+\mathrm i\,\operatorname{sgn}(t)\,k\,\frac\sigma4,
\qquad k=0,\dots,K,\quad K=\Bigl\lceil\frac{4|t|}\sigma\Bigr\rceil,
\]

s posledním diskem `B(c_K,r)∋s` (pro `t=0` je `K=0`): každý disk
leží v `D` (vzdálenost středů od hranice `≥σ`, poloměr `σ/2`),
`|c_{k+1}-c_k|=σ/4<r`, a `|s-c_K|≤σ/4<r` (protože
`|t-\operatorname{sgn}(t)Kσ/4|≤σ/4`). Základna: `B(c_0,r)` má reálný
střed a reálný průměr `(σ/2,3σ/2)⊂(0,∞)`, kde `f=0` (N5) —
IT-SEGMENT(i). Krok: `f=0` na `B(c_k,r)` a `B(c_{k+1},r)∩B(c_k,r)`
je neprázdná otevřená množina — IT-SEGMENT(ii). Po `K` krocích
`f(s)=0`; tedy `f≡0` na `D`. (Pravidlo je registrováno pro libovolné
reálné středy/poloměry; auditní brána §3.5 přehrává racionální
instanci.)

### N7 — EOC_ON_D (koncový uzel)

`\hat E\hat O=\hat C` na `D`. Štítek `JIPC_WP3F_EOC_HOLOMORPHIC`,
strop dle režimu §0.0, THEOREM_CARRIER =
WRITTEN_PROOF_NOT_FINITE_AUDIT.

Povinná cesta: `N1 → N2 → N3 → {N4, N5} → N6 → N7`; jediný sink,
žádný mrtvý uzel.

## §3. Ohraničený auditní povrch verifieru

Verifier přebírá závazky WP3E: zero-arg, žádné I/O (soubor, stdin,
prostředí, hodiny, síť), jediný import `fractions.Fraction`, tvrdý
timeout 600 s, bajtová identita stdout na x86_64 i aarch64,
Python 3.12. Přesné PASS řádky stdout se zmrazí ve Field-4 stylu
v PREREG před pinem; **soubor `EXPECTED.txt` se commituje až po
jediném formálním běhu** (pořadí WP3E: pin → veřejné přečtení →
formální běh → commit EXPECTED/RUN/RESULT → two-architecture gate).

**Zmrazený formát stdout (Field-4 styl, hodnotově prostý):** žádný
vypočtený řád veličiny se v stdout neobjevuje — číselné meze, boxy a
sup-hodnoty jsou interní pro audit, stdout nese jen rozhodnutí bran.
Návrh přesných řádek (finální bajty potvrdí pin; soubor EXPECTED.txt
se commituje až z auditovaného stdout formálního běhu):

```text
JIPC_WP3F_EOC_HOLOMORPHIC_AUDIT 1
ARITHMETIC Q_INTERVAL_COMPLEX_BOX PASS
MACHIN_BRIDGE_WITNESSES POLY,CROSS3,DOMAINS,INDEXING PASS
SLICE_WITNESS_REPLAY S=1,2,3 RING=Q[g,g^-1] PASS
PRODUCT_NAME_SCHEDULE K=[1,3/2]x[-1/2,1/2] N=1 PASS
SAMPLE_BALL_OVERLAP S=3/2+i/2 BITS=2,3 SHRINK PASS
CHAIN_GEOMETRY S=3/2+i/2 R=3/4 K=2 PASS
PROOF_CONTROLS 14/14 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
DECISION JIPC-WP3F-EOC-HOLOMORPHIC-CONFIRMED
```

Brány:

1. `MACHIN_BRIDGE_WITNESSES`: polynomiální identita N1b
   (exaktně, jako polynom v `u,v`); tři krácicí svědci
   `10·12=24·5`, `720·119=714·120`, `240·119=238·120`; podmínky
   `uv<1` a hodnota `≤2` pro každou aplikaci; indexace N1a
   (znaménko `(−1)^{N+1}`, `ρ_N≤a_{q,N+1}`) na zmrazeném `N`.
2. `SLICE_WITNESS_REPLAY`: exaktní přehrání (EOC) v `s∈{1,2,3}`
   v `Q[g,g^{-1}]`, `π̂=g²` (`\hat E(1)=1`,
   `\hat O(1)=\hat C(1)=π̂^{-1}`).
3. `PRODUCT_NAME_SCHEDULE`: na `K=[1,3/2]×[−1/2,1/2]` spočti
   zmrazeným postupem racionální `M_E,M_O` (algoritmus N4 je
   součástí zmrazeného povrchu; hodnoty vydá formální běh) a ověř
   posunutý rozvrh pro `n=1`.
4. `SAMPLE_BALL_OVERLAP`: v `s=3/2+i/2` boxy `\hat E,\hat O,\hat C`
   při `b=2,3`; box součinu (vnější zaokrouhlení) protíná box
   `\hat C`; společný průměr se mezi `b=2` a `b=3` zmenší.
5. `CHAIN_GEOMETRY`: racionální instance N6 pro `s=3/2+i/2`
   (`r=3/4`, `K=2`, sgn(t)=+1): středy v `D`, kroky `<r`,
   `|s-c_K|<r`, reálný průměr základny v `(0,∞)`.
6. `PROOF_CONTROLS` (negativní mutace, min. 12 — každá selhává na
   pojmenované sémantické stráži):
   1. mutovaná polynomiální identita N1b (koeficient);
   2. mutovaný krácicí svědek `120/119` (např. `720·119↦720·118`);
   3. porušená podmínka `uv<1` (aplikace N1b s `uv≥1`);
   4. mutovaná indexace N1a (zbytek `≤a_{q,N}` místo `a_{q,N+1}`
      se špatným znaménkem);
   5. **provenanční guard konstanty:** oblečené semeno citující
      jiné registrované jméno konstanty než `p_M` (jmenná/grafová
      stráž; žádný numerický test — obálky téže reálné hodnoty se
      protínají vždy);
   6. křížové čtení `O:=E(s+1)` v definiční vrstvě;
   7. vynechaný uzel N1 (přímé lepení WP3D↔WP3E bez mostu);
   8. mutovaný rozvrh N4 (chybějící `+2` posun);
   9. rozbitá geometrie řetězu: krok středů `σ` místo `σ/4`
      (`c_{k+1}∉B(c_k,r)`);
   10. `r=2σ` (disk obsahuje body s `Re s≤0` mimo `D`);
   11. mutovaný reálný průměr základny (posunutý mimo nulový
       paprsek, IT-SEGMENT(i) nepoužitelný);
   12. mutovaný svědek `s=1` (`\hat E(1)=1↦π̂`);
   13. nárok pokračování / funkcionální rovnice (STOP stráž);
   14. `s` s `Re s≤0`.

## §4. Falzifikátory

- F1: selhání kterékoli brány §3 (svědci N1, replay, rozvrh,
  ball-overlap, geometrie).
- F2: kterákoli negativní mutace projde svou pojmenovanou stráží.
- F3: WP3E po merge nese jinou definici trojic/`p_M`, než cituje
  tento prereg → STOP (integrita, ne vědecký falzifikátor).
- Integrity mismatch bez přesné matematické negace je STOP.

## §5. STOP hranice a štítky (cílový stav)

Zděděné brány se přebírají **bajtově v rodičovských jménech a
hodnotách**; nové vysvětlení jde jen do `blocker_details`:

```text
MELLIN_SEEDS                     = BLOCKED            (bajtově zděděno)
MELLIN_PRODUCT_IDENTITY          = BLOCKED            (bajtově zděděno)
WP2_SCALAR_SEAM                  = BLOCKED_BY_MELLIN_PRODUCT_IDENTITY (bajtově zděděno)
STANDARD_PI_IDENTIFICATION       = BLOCKED            (bajtově zděděno)
CIRCLE_PI_IDENTIFICATION         = BLOCKED            (bajtově zděděno)
ANALYTIC_CONTINUATION            = BLOCKED            (jméno dle WP3D §11.C)
FUNCTIONAL_EQUATION              = BLOCKED            (jméno dle WP3D §11.C)
FOURIER_SELF_DUAL_NORMALIZATION  = BLOCKED
POISSON_SUMMATION                = BLOCKED
GAMMA_AS_COMPLEX_FUNCTION        = BLOCKED
PROTOCOL_VERDICT                 = NO_VERDICT
```

```text
blocker_details (aktualizace, hodnoty bran beze změn):
MELLIN_SEEDS            : účinná holomorfní semena drží WP3E (candidate-T);
                          veřejný fold rozhodne správce
MELLIN_PRODUCT_IDENTITY : racionální řez drží WP3D-QPOS; identita na
                          Re(s)>0 je cílem tohoto probe (WP3F)
WP2_SCALAR_SEAM         : chybí meromorfní pokračování (krok 3)
                          a globální šev (krok 4)
```

Nové štítky:

```text
JIPC_WP3F_EOC_HOLOMORPHIC        = cíl: PASS_RELATIVE_TO_COMPLEX_BALL_MELLIN_TCB_V2
MACHIN_BRIDGE                    = cíl: PASS (uzel, /v1 prostředky)
IT_SEGMENT_RULE                  = TCB/v2 registrace (ne PASS uzel)
POW_EXPLOG_ID_RULE               = TCB/v2 registrace (ne PASS uzel)
```

## §6. Otevřené závislosti (podmínky pinu — governance, ne verifier)

1. **Režim §0.0** rozhodnut správcem (A: WP3D-QPOS public probe
   nejdřív; B: interní WP3F).
2. **WP3E lock:** merge PR #569 — SPLNĚNO (merge commit
   `9a4b479b0a7a9ce39772f77f16dd363602ec72c7` na `main`, po v65);
   zbývá doplnit hashe a
   přesná znění vět.
3. **WP3D-QPOS lock:** freeze (interní, či veřejný dle režimu);
   doplnit lock pole.
4. **WP3B lock:** hashe + přesné zmrazené znění `pi_atan := 4F`,
   `F=∫_0^1 dt/(1+t²)`, `3<pi_atan<16/5` (N1 a konzistenční
   poznámka je spotřebovávají přímo, ne přes WP3D).
5. **Claim lock:** veřejné/interní issue dle režimu, před pinem.
6. Pořadí zámků a zákaz běhu před nimi je podmínka pinu (governance);
   **není** to verifierová mutace — verifier je bezvstupový.
7. Do splnění 1–5 je dokument DRAFT; žádný pin, žádný výpočet
   výsledků.
