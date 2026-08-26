# JIPC WP3F — E·O=C na Re(s)>0 — návrh preregistrace (DRAFT v2)


Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
ŽÁDNÝ PIN, ŽÁDNÝ BĚH / PUBLIC-PIN-READY: NO**.

Veřejný audit nad Public Canon v65 a sloučeným WP3E uzavřel:

```text
HOLOMORPHIC_ROUTE        = PASS_CONDITIONAL
REGIME                   = A_SELECTED
PRIVATE_ROUTE_B          = CLOSED
PUBLIC_WP3D_PARENT       = MISSING
WRITTEN_CONTRACT         = REPAIR_APPLIED_IN_NOTES
PUBLIC_PIN_READY         = BLOCKED
```

Tento dokument zůstává návrhem. Rozhodnutí režimu nevytváří claim,
pin, veřejnou premisu ani oprávnění k běhu.


## 0.0 REŽIM — rozhodnuto před veřejným pinem

Správce zvolil **cestu A**:

1. nejdřív vznikne a bude sloučena veřejná proba
   `P-JIPC-WP3D-QPOS-MELLIN-1`;
2. teprve potom může vzniknout veřejná WP3F proba s plným
   `candidate-T` stropem.

Cesta B je pro tuto posloupnost **CLOSED / NOT SELECTED**.

Současný WP3D-QPOS notes draft není veřejnou premisou. Před veřejným
pinem musí být přepsán jako soběstačná veřejná proba bez privátního
WP3C/WP2 rodiče, projít vlastním pinem, formálním během,
dvouarchitekturovou branou a merge. Tento dokument zůstává
`NOTES LANE / NON-CANONICAL`; rozhodnutí A samo nevytváří claim, pin
ani oprávnění k běhu.

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
(2) holomorfnost + efektivní jména z WP3E; (3) věta o identitě a
identifikace mocnin (dva přesně registrované přírůstky TCB podle §1).
Racionální řez je svědková množina; WP3E
firewall se ctí (identitu vlastní až tento probe).

### 0.1 Ne-nároky

Nedokazuje se: meromorfní pokračování (krok 3 žebříku), funkcionální
rovnice, Fourier/Poisson, Gamma objekt, kruhové `pi`, archimédovské
místo, globální WP2 šev, žádný L2–L6 lift, SAMPLING NOT PROVIDED.
Uzel N1 dokazuje `p_M=4F` mezi veřejně definovaným Machinovým
jménem a nově vypsaným integrálním jménem; nespotřebovává privátní
WP3B artefakt. Žádné kruhové čtení se nezavádí a
brány `STANDARD_PI_IDENTIFICATION` a `CIRCLE_PI_IDENTIFICATION`
zůstávají v rodičovských hodnotách.

## §1. TCB: `COMPLEX_BALL_MELLIN_TCB/v2`

Dědí se celý `COMPLEX_BALL_MELLIN_TCB/v1` z WP3E. Přírůstky (dva):

**IT-SEGMENT (registrované pravidlo):** nechť `r∈R_{>0}`,
`c∈C` a `B(c,r)⊆D` je otevřený eukleidovský disk. Tento disk není
obdélníková complex-ball reprezentace výpočetního evaluátoru WP3E.

(i) Je-li navíc `c∈R` a `f=0` na reálném průměru
`{c+x:x∈(−r,r)}`, pak `f=0` na `B(c,r)`.

(ii) Pro libovolné `c∈C`: je-li `f=0` na neprázdné otevřené
podmnožině `B(c,r)`, pak `f=0` na `B(c,r)`.

Racionalita středu ani poloměru se nevyžaduje. Vnitřní
Taylorův/Cauchyho důkaz je součástí registrace; žádná Cauchyho
normalizační konstanta nevstupuje do cílového tvrzení ani výpočtu.

**POW-EXPLOG-ID (drobné registrované rozhraní):** jednoznačnost
kladného `n`-tého kořene (z ryzí monotonie `y↦yⁿ` na `(0,∞)`),
umožňující uzel N2a. Nic dalšího; zejména žádný POW_RAT kalkul se
nepřenáší.

Uzly N1 (Machinův most) se dokazují celé v /v1 prostředcích
(kompaktní FTC, derivační algebra, racionální aritmetika).

## §2. Důkazový graf

### N1 — MACHIN_INTEGRAL_BRIDGE: `p_M = 4F`

WP3E definuje `p_M := p := pi_atan := 16A_5-4A_{239}`, ale
neidentifikuje toto Machinovo Cauchyho jméno s integrálním, kruhovým,
Gaussianovým ani jiným externím objektem. N1 je soběstačný most:

\[
\boxed{p_M=16A_5-4A_{239}=4\!\int_0^1\!\frac{dt}{1+t^2}=:4F} .
\]

1. **N1a (řadové jméno = integrál).** Pro každé reálné
   `x∈[0,2]` polož `A(x)=∫_0^x dt/(1+t²)`. Výpočetní audit používá
   jen racionální argumenty; psaný FTC důkaz potřebuje `A` na celém
   reálném intervalu.
   Konečná geometrická identita
   `1/(1+t²)=Σ_{n=0}^{N}(−1)^n t^{2n}+(−1)^{N+1}t^{2N+2}/(1+t²)`
   a FTC dávají pro `x=1/q` (ve zmrazené WP3E konvenci
   `S_{q,N}=Σ_{n=0}^{N-1}(−1)^n a_{q,n}`):
   \[
   A(1/q)=S_{q,N+1}+(-1)^{N+1}\rho_{N},\qquad
   0\le\rho_N\le a_{q,N+1},
   \]
   tedy zbytek má znaménko `(−1)^{N+1}` a velikost `≤a_{q,N+1}`,
   Protože `S_{q,N+1}=S_{q,N}+(-1)^N a_{q,N}` a
   `0≤rho_N≤a_{q,N+1}<a_{q,N}`, je
   `A(1/q)-S_{q,N}=(-1)^N(a_{q,N}-rho_N)`. Tedy
   `A(1/q)∈hull(S_{q,N},S_{q,N+1})` pro každé `N`; z
   jednoznačnosti společného bodu Machinových intervalů
   `A(1/q)=A_q`.
2. **N1b (adiční zákon).** Pro reálné `u,v≥0`, `uv<1` a
   `(u+v)/(1−uv)≤2` platí
   `A(u)+A(v)=A((u+v)/(1−uv))`.

   Pro pevné `u` definuj na `x∈[0,v]`
   \[
   H_u(x):=A(u)+A(x)-A\!\left(\frac{u+x}{1-ux}\right).
   \]
   Z podmínek a monotonie zobrazení `x↦(u+x)/(1−ux)` zůstává argument
   `A` v `[0,2]`. Přesná identita
   \[
   (1-ux)^2+(u+x)^2=(1+u^2)(1+x^2)
   \]
   dává `H_u'(x)=0`; protože `H_u(0)=0`, FTC dává `H_u(v)=0`.
   Kernel přehrává pouze tři následující racionální instance.
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
\sup_K|P_E^{(n)}P_O^{(n)}-F_EF_O|\le(M_E+M_O)\,\varepsilon,
\]

pomocí rozkladu `(P_E-F_E)P_O+F_E(P_O-F_O)`. Po přidání chyby
aproximantu `P_C^{(n)}` je celkový koeficient
`M_E+M_O+1`. Jméno funkce `f:=F_EF_O-F_C` proto má rozvrh

\[
h:=\min\{k\in\mathbb N:2^k\ge M_E+M_O+1\},
\qquad m:=n+h+2
\]

a používá rodičovské aproximanty s indexem `m`. Celková chyba
je tím nejvýše `2^{-(n+3)}`. Před pinem se zmrazí jediný
deterministický algoritmus pro koeficientové obálky, přesnost `p_M`
a exponenciály, pořadí součtů a vnější zaokrouhlení. Funkce `f` je
holomorfní na `D` s efektivním jménem na každém racionálním
kompaktním obdélníku.


### N5 — RAY_VANISHING (spotřeba N3 + N4)

N4 dává holomorfní, a tedy spojitou funkci `f:=F_EF_O-F_C` s účinným
jménem na každém racionálním kompaktním obdélníku. Pro každé `σ>0`
zvol racionální posloupnost `s_k∈Q_{>0}`, `s_k→σ`. Z N3 je
`f(s_k)=0`; spojitost z N4 proto dává `f(σ)=0`. Tedy `f=0` na celém
`(0,∞)`.

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
`f(s)=0`; tedy `f≡0` na `D`. (Pravidlo je registrováno pro `c∈C` a `r∈R_{>0}`; auditní
brána §3.5 přehrává pouze jednu racionální instanci.)

### N7 — EOC_ON_D (koncový uzel)

`\hat E\hat O=\hat C` na `D`. Štítek `JIPC_WP3F_EOC_HOLOMORPHIC`,
strop dle režimu §0.0, THEOREM_CARRIER =
WRITTEN_PROOF_NOT_FINITE_AUDIT.

Povinné hrany jsou:

```text
N1 -> N2
N2 + PUBLIC_WP3D_QPOS_PARENT -> N3
PUBLIC_WP3E_PARENT -> N4
N3 + N4 -> N5
N4 + N5 + IT_SEGMENT_RULE -> N6
N6 -> N7
```

`N4→N5` je povinná hrana; `N4` není potomkem N3. Jediným sinkem je
N7 a žádný primární uzel není mrtvý.

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
SAMPLE_BALL_OVERLAP S=3/2+i/2 BITS=2,3 PASS
CHAIN_GEOMETRY S=3/2+i/2 R=3/4 K=2 PASS
PROOF_CONTROLS 14/14 PASS
THEOREM_CARRIER WRITTEN_PROOF_NOT_FINITE_AUDIT
RESULT PASS
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
4. `SAMPLE_BALL_OVERLAP`: v `s=3/2+i/2` sestroj boxy
   `\hat E,\hat O,\hat C` při `b=2,3`; pro každé `b` musí vně
   zaokrouhlený box součinu protínat box `\hat C` a každý box musí
   splnit svůj zmrazený poloměrový rozpočet. Vnořenost ani přísné
   zmenšení průměru průniku se netvrdí.
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
   5. **provenanční guard konstanty:** oblečené semeno musí sestupovat
      z přesné hashované rodičovské aliasové třídy `p_M=p=pi_atan`.
      Stráž kontroluje definici a graf, nikoli doslovný řetězec aliasu;
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


## §4. Falzifikátory, integrity STOP a omezený fallback

`FIRED` vzniká pouze hotovou exaktní matematickou negací:

- F1: exaktní protipříklad vyvrátí některý psaný uzel N1–N7;
- F2: po nezávislém potvrzení aritmetiky vzniknou v témže povoleném
  bodě dva zvukové, navzájem disjunktní boxy pro strany identity;
- F3: exaktní výpočet vyvrátí zmrazenou doménovou podmínku,
  produktový rozvrh nebo geometrii řetězu, nikoli jen implementaci.

`STOP`, nikoli vědecký `FIRED`, nastává při průchodu negativní mutace,
driftu rodičovského hashe či textu, selhání autority, collision scanu,
claim locku, pinu, readbacku, bezpečnosti, timeoutu, determinismu,
bajtů nebo architekturní integrity a při každém selhání, které může
být vadou verifieru. Projde-li omezený audit, ale univerzální důkaz
není přijat, výsledek je nejvýše `BOUNDED-C` na zmrazeném konečném
povrchu.

## §5. Rozhodovací kontrakt, soukromý kontext a cílové štítky

```text
CANDIDATE-T  = oba veřejní theorem-grade rodiče + přijatý psaný
               důkaz N1–N7 + připnutý audit + obě architektury PASS
BOUNDED-C    = audit PASS, ale univerzální důkaz nebo rodič není
               theorem-grade; platí jen konečný zmrazený povrch
FIRED        = hotová exaktní matematická negace
STOP         = integrita, kód, mutace, běh nebo autorita selhala
```

Stdout verifieru vyjadřuje pouze omezený audit a končí `RESULT PASS`.
Výběr stavu patří až do `RESULT.md`.

### 5.1 Soukromá rodová mapa — pouze discovery context

Následující mapa zachycuje soukromou WP2/WP3C rodovou linii.
**Není veřejnou mapou bran a veřejná WP3F ji nezdědí.** Public Canon
v65 nemá odpovídající JIPC/MELLIN/WP2 řádky v `REGISTRY.tsv`,
`GATES.tsv` ani `EVIDENCE.tsv`. Do veřejného `PREREG.md` se mapa
nepřenese.

Soukromé rodové hodnoty bez veřejné autority:

```text
MELLIN_SEEDS                     = BLOCKED            (private-lineage value only; no public authority)
MELLIN_PRODUCT_IDENTITY          = BLOCKED            (private-lineage value only; no public authority)
WP2_SCALAR_SEAM                  = BLOCKED_BY_MELLIN_PRODUCT_IDENTITY (private-lineage value only; no public authority)
STANDARD_PI_IDENTIFICATION       = BLOCKED            (private-lineage value only; no public authority)
CIRCLE_PI_IDENTIFICATION         = BLOCKED            (private-lineage value only; no public authority)
ANALYTIC_CONTINUATION            = BLOCKED            (jméno dle WP3D §11.C)
FUNCTIONAL_EQUATION              = BLOCKED            (jméno dle WP3D §11.C)
FOURIER_SELF_DUAL_NORMALIZATION  = BLOCKED
POISSON_SUMMATION                = BLOCKED
GAMMA_AS_COMPLEX_FUNCTION        = BLOCKED
PROTOCOL_VERDICT                 = NO_VERDICT
```

Také následující `blocker_details` jsou pouze soukromým rodovým
kontextem, nikoli veřejným stavovým přechodem.

```text
blocker_details (private-lineage context only):
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

## §6. Otevřené závislosti — podmínky veřejného pinu

1. **Režim:** `A_SELECTED`; `B_CLOSED`.

2. **Veřejný WP3E lock:** PR #569 je sloučen jako
   `9a4b479b0a7a9ce39772f77f16dd363602ec72c7`. Parent-lock ponese:

   ```text
   preregistration pin  46004772f3a6510791adf2ae4afd14a8a9f7f5af
   PREREG SHA-256       af078f17645dc8b5ef78acefb53bf73b791045efd2147bf2d87ed5006e9bdd80
   verify SHA-256       373ff274abcc27e06b12e8aee1ebd0bfc0de6bebbc66ed69e1c53e87a06369d1
   stdout SHA-256       f51edb6ed4d7733abca72ea45e091cfa9241c36848b9509d532828e609cc2056
   formal result head   289ea861c6289f0e6426b1cabffd0c54fb7c059f
   result status        candidate-T / L1 / public Canon unchanged
   ```

   Lock musí citovat přesná rodičovská tvrzení. WP3E bez samostatného
   foldu není aktivní veřejné `[T]`.

3. **Veřejný WP3D-QPOS lock:** současný notes draft podmínku nesplňuje.
   Nejdřív musí vzniknout claim issue, větev
   `probe/P-JIPC-WP3D-QPOS-MELLIN-1`, soběstačný veřejný `PREREG.md`
   a dosud nespouštěný `verify.py` bez privátní WP3C/WP2 premisy.
   Následují pin, první formální běh, `EXPECTED/RUN/RESULT`,
   x86_64+aarch64 brána a merge. Skončí-li WP3D pouze `C`, strop
   WP3F se snižuje nejvýše na `C`.

4. **Veřejný WP3F claim lock:** po merge WP3D provést nový úplný
   collision scan a teprve potom otevřít jediný claim issue a zmrazit
   identifikátor, branch, path, owner, L1 a result-exposed režim.

5. **Autorita a base:** aktuální authority tuple a `BASE_COMMIT` se
   pořídí až z tehdejšího veřejného `main` po merge WP3D.

6. **TCB a strojová smlouva:** před pinem zmrazit přesný TCB/v2,
   opravené IT-SEGMENT, úplný DAG s `N4→N5`, algoritmus produktového
   jména, obálky, zaokrouhlení, prostředkové meze, všech 14 kontrol
   a přesné stdout bajty bez `SHRINK` a theorem-level `DECISION`.

7. **Accepted verifier:** `PREREG.md` a nikdy nespouštěný
   self-contained `verify.py` se připnou společně. Žádný formální
   výpočet ani výsledek nesmí vzniknout dříve.
