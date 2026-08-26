# JIPC WP3D-QPOS-MELLIN — návrh důkazového kontraktu (DRAFT v3)

Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO**.
Verze 3 zapracovává governance verdikt druhého kola
(`QPOS_* = PASS_MATHEMATICALLY`, `FREEZE_READY = BLOCKED_AS_WRITTEN`):
šest freeze blokátorů a tři upřesnění. Matematické jádro (§3–§6) je
proti v2 beze změny; nová je algoritmická a správní vrstva. Tento
dokument je návrh, ne certifikát; nemění Canon ani stav JIPC.

## 0. Přesný cíl: racionální mezistupeň, ne vybití WP2

Zmrazený WP2 vyžaduje

```text
O-MELLIN-SEEDS:  nezávislé účinné holomorfní E, O, C na Re(s)>0
O-SCALAR-SEAM:   E(s)O(s)=C(s) jako globální meromorfní identita
```

Tento balík **žádnou z těchto povinností nevybíjí**. Dokazuje pouze
hodnotový řez `s,p,q ∈ Q_{>0}`, bez komplexních koulí, holomorfnosti,
analytického pokračování a bez účinného jádra kompaktních integrálů.
Zděděné brány `MELLIN_SEEDS`, `MELLIN_PRODUCT_IDENTITY`,
`WP2_SCALAR_SEAM` zůstávají **bajtově v rodičovských hodnotách**
(§11.A); koncovým uzlem grafu je

```text
WP3D_QPOS_SCALAR_SLICE
```

Dokazované jádro:

\[
\boxed{C(p)C(q)=C(p+q)B(p,q)}
\qquad(p,q\in\mathbb Q_{>0}),
\tag{MP}
\]

\[
\boxed{C(p)\,C(p+\tfrac12)=2^{1-2p}\,C(\tfrac12)\,C(2p)}
\qquad(p\in\mathbb Q_{>0}),
\tag{DUP}
\]

a při typové rovnici `C(1/2)² = pi_atan` (§3.2) oblečený řez

\[
\boxed{\hat E(s)\,\hat O(s)=\hat C(s)}
\qquad(s\in\mathbb Q_{>0}).
\tag{EOC}
\]

### 0.1 Přímý rodič a plný parent-lock

Přímým rodičem je `I-JIPC-WP3C-GAUSSIAN-BRIDGE-v1@0.1.0`. Vnější
freeze obal (mimo archiv):

```text
WP3C archive sha256          56db8d0283219aa4489b7976b77fe2e76873df3fb96e6598f457b1be0ec2908e
WP3C archive receipt sha256  765e84709e7bc6d42525990f65761335c683dd7e446886dd2bb6f5564e17d2fd  (JIPC_WP3C_GAUSS_v0_1.zip.sha256)
WP3C freeze manifest sha256  e9cf0db7c67f7f9cbb76641e50d95136257ceecc30ed47fe6a5ed5240c31607d
WP3C freeze id               I-JIPC-WP3C-GAUSSIAN-BRIDGE-LOCK-1
```

Soubory **uvnitř archivu** (nezávisle přepočtené z ověřeného ZIP;
parent-lock je vede odděleně od vnějšího obalu):

```text
70170e17c55fceba1db131e804f96739b109ad42cde9f7a37fae5a17e504049a  jipc_wp3c_gauss_certificate.json
b94698df6a39240252b62495893ff6f0b88792f078c5ed334dc03915c9f3803a  jipc_wp3c_gauss_environment.json
c430242346e1780cab081b9242660f1f6b39f1bc7fd904cbfee931ab1c7d5088  JIPC_WP3C_GAUSS_EXPECTED.txt
e9cf0db7c67f7f9cbb76641e50d95136257ceecc30ed47fe6a5ed5240c31607d  JIPC_WP3C_GAUSS_FREEZE.json
7d0ae8adaa5d1ba8fd1cd11c1d765113131a7982e14422d0fd2261f39690378b  JIPC_WP3C_GAUSS_FREEZE.sha256
73d089b146faea429eb16994c26f8da0506f71538b9c2c7d0e6a053f72509e77  jipc_wp3c_gauss_kernel.py
20480cde907440a7afb9ca0c5bbb3e29c56f784b67592cdcc113d73aca4cd664  jipc_wp3c_gauss_negative_fixtures.json
3aa0fc2ff68af43531d603459e6a5de985d6c222baa1eec5631143fa2aa373f1  JIPC_WP3C_GAUSS_REPORT.md
ba6e5292470b6e2756614d16a5708a92262ea3665a69aba8e0a6f9cac5d63fbe  jipc_wp3c_gauss_spec.json
7c12a5d130fe23c6f76c4bad47af14988c6994d795c7bbec77a52dbfb9112ed0  jipc_wp3c_gauss_universe.json
42b2ee32d35fb7d53694e23b58e28e5af5824f1fd5f59fee61abdc95d8ea492d  jipc_wp3c_gauss_validate.py
6fef9c55bc36556c44702b934c07c20a5ce15d5bd69da64759730eed1aabab88  JIPC_WP3C_PARENT_LOCK.json
6530d2fcb821a58ab50531eacb3d076b35d3a0d2e54102f7bdd1ed3e4c93141a  JIPC_WP3C_REDTEAM.md
27dfd8be1fb43cf356abf365fde95b99626aeb6c923dd4e53adba9d77ee60abc  JIPC_WP3C_SOURCE_LEDGER.md
42b1193a71324809db0452e3aa0a186553057da5c61baa917f40285718d619dd  README.md
36819c02a7e5a67f28390ed6fe3b00e390dfb4923d6b5354c78044afe43f6079  WP3C_GAUSS_PROOF_CONTRACT.md
```

**Sekundární WP2 lock**, přesné hodnoty:

```text
WP2 archive sha256           152ea2e8709080089f2af30ebf4bc951181bd2d07a0e0298d6f872513311ae5f
WP2 archive receipt sha256   35e2f0a695f50b9ca2cd829133bb1f0bab0e9058463e0291f930fad6198de9ae
WP2 freeze manifest sha256   c166de2f87f76e1ff5860445f0bd88eabe5efc31bc54721cc12069d8147e1080
WP2 freeze receipt sha256    f166002e206763ae806e3f7c8cc728a617a052bcb31bccc13d9405d3f6379145
WP2 mellin profile sha256    c2e0371e142d6c3c12fee7ab47ae223596bf061f6d99ad9c27735b68cf478ac1
WP2 universe sha256          eab9cec4e33f84f76fec6815b2028bb682512097228ca66d719c14c85c35dc86
WP2 report sha256            bda1bb31ad73aa99a3e0c275c71d886771d24eb697f28e6541bfc329a46f6ccd
WP2 freeze id                I-JIPC-WP2-DUAL-LANE-LOCK-2
WP2 version                  0.1.1
```

`JIPC_WP3D_PARENT_LOCK.json` musí nést obě sekce včetně přesných
znění povinností `O-MELLIN-SEEDS` a `O-SCALAR-SEAM`. Spotřebovávaný
rodičovský uzel je certifikátový uzel `PI_ATAN_GAUSS_TYPED_IDENTITY`;
`PI_ATAN_EQUALS_PI_GAUSS` je pouze brána universe a
`P_GAUSSIAN_NORMALIZED` patří výhradně do auditu řezu `s=1` (§6.3).

### 0.2 Kritérium importu

O importu rozhoduje **pozitivní seznam primitiv a důkazový graf**,
nikoli jméno symbolu. Přejmenování `C` není import; importem je
nepovolená závislost (převzetí hodnoty, identity nebo věty mimo
povolenou třídu). Není dovolena žádná závislost na Gamma/Beta teorii,
kruhovém `pi`, goniometrii, komplexní proměnné, Fourierovi,
Poissonovi, Tonellim na nekonečné oblasti ani logaritmu.

### 0.3 Definice semen — bez křížového čtení

Pro racionální `s>0`, vše ve smyslu kompaktních řezů a monotónních
limit (§2):

\[
C(s):=\int_0^\infty x^{s-1}e^{-x}\,dx,
\qquad
B(p,q):=\int_0^1 u^{p-1}(1-u)^{q-1}\,du,
\]

\[
E(s):=\int_0^\infty x^{s-1}\,e^{-x^2}\,dx,
\qquad
O(s):=\int_0^\infty x^{s-1}\cdot\bigl(x\,e^{-x^2}\bigr)\,dx .
\]

`O` čte **samostatně** liché semeno `x·e^{-x²}`; definice `O:=E(s+1)`
je zakázané křížové čtení. Rovnost `O(s)=E(s+1)` je dokazovaný
spojovací uzel `ODD_EVEN_SHIFT_JOIN_QPOS` (§3.1). Oblečená semena
(`p := pi_atan`):

\[
\hat E(s):=2\int_0^\infty e^{-p x^2}x^{s-1}dx,
\qquad
\hat O(s):=2\int_0^\infty e^{-p x^2}x^{s}dx,
\qquad
\hat C(s):=4\int_0^\infty e^{-2p r^2}r^{2s-1}dr ;
\]

kvadratický tvar `\hat C` je primární objekt WP2, lineární podoba je
pullback uzel `C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS` (§6.1).

## 1. Přírůstek TCB: `MELLIN_CALCULUS_TCB/v1`

Dědí se celý `GAUSSIAN_CALCULUS_TCB/v1`. Přírůstek:

1. **POW_RAT_ANALYTIC** — analytická vrstva racionálních mocnin,
   s úplným odvozovacím grafem (existence neplyne z pouhé monotonie a
   spojitost neplyne z pouhé jednoznačnosti):

   ```text
   POLYNOMIAL_CONTINUITY_AND_UNBOUNDEDNESS
   → POSITIVE_NTH_ROOT_EXISTENCE_BY_SUPREMUM
   → ROOT_UNIQUENESS_AND_ORDER
   → ROOT_CONTINUITY
   → POW_RAT_DERIVATIVE
   ```

   - existence: `x^{1/n} := sup{y≥0 : yⁿ≤x}` — supremum existuje
     z úplnosti; že je kořenem, plyne ze spojitosti a neomezenosti
     polynomu `y↦yⁿ` (první uzel grafu);
   - jednoznačnost a uspořádání z ryzí monotonie `y↦yⁿ` na `[0,∞)`;
   - spojitost kořene jako samostatný uzel (vlastní `ε–δ` důkaz
     z monotonie a hustoty racionálních řezů);
   - derivace **přímým algebraickým argumentem**, bez obecné věty
     o inverzní funkci: pro `z=x^{1/n}`, `z_h=(x+h)^{1/n}` je
     \[
     z_h-z=\frac{h}{\sum_{j=0}^{n-1}z_h^{\,n-1-j}z^{\,j}},
     \]
     a spojitost kořene dává `d/dx\,x^{1/n}=\tfrac1n x^{1/n-1}`;
     poté explicitně zapsané řetězové pravidlo (samostatná položka)
     a `d/dx\,x^{m/n}=(m/n)x^{m/n-1}` na `(0,∞)`;
   - zákony (každý z jednoznačnosti kořene): nezávislost na
     reprezentaci exponentu, `x^{r+r'}=x^r x^{r'}`, `(xy)^r=x^r y^r`,
     `(x^r)^{r'}=x^{rr'}`, `x^{-r}:=1/x^r` s rozšířenými zákony;
   - mezní chování v nule: pro `r=m/n>0`, `0<ε≤1`:
     `0<x<εⁿ ⟹ x^{1/n}<ε ⟹ x^{m/n}≤x^{1/n}<ε`; konvence `x^0=1`.
2. **POW_RAT_QCERT** — účinná vrstva: půlicí certifikát `yⁿ`-zkouškou
   vyžaduje účinné jméno základu; kontraktní moduly §2 používají
   výhradně racionální základy.
3. **TRUNC-0** — oboustranné kompaktní řezy s monotónní limitou
   v obou koncích, plus **kofinální lemma řezů**: síť
   `(δ,R)↦(δ²,R²)` je kofinální v síti všech řezů (k danému
   `(δ',R')` existuje `(δ,R)` s `δ²≤δ'`, `R²≥R'`), takže supremum
   přes umocněné řezy splývá se supremem přes všechny řezy. Toto
   lemma konzumují pullbacky `y=x²` (§3) a `x=r²` (§6.1).

Realizace `x^r` přes `exp(r·log x)`, logaritmus nebo reálný
iracionální exponent je mimo třídu (fixture §10).

## 2. Existence semen: nekruhové pořadí a modulové algoritmy

Pořadí je závazné: nejprve kompaktní řezy, pak limita, pak moduly.
Symboly `∫_0^δ`, `∫_R^∞` se před konstrukcí nevlastního integrálu
nevyskytují.

### 2.1 Kompaktní řezové odhady

Pro racionální `0<ε<δ≤1≤R<T` a `s∈Q_{>0}`:

\[
0\le\int_\varepsilon^\delta x^{s-1}e^{-x}dx
\le\frac{\delta^{s}-\varepsilon^{s}}{s},
\tag{M0'}
\]

a s celým `k≥s-1` (`x^{s-1}≤x^k` pro `x≥1`; `e^x≥x^{k+2}/(k+2)!`,
tedy `x^k e^{-x}≤(k+2)!/x²`; primitiv `-1/x`):

\[
0\le\int_R^T x^{s-1}e^{-x}dx
\le(k+2)!\left(\frac1R-\frac1T\right).
\tag{M∞'}
\]

Síť řezů je monotónní, shora omezená `1/s+(k+2)!`; monotónní úplnost
dává `C(s):=sup_N C_{1/N,N}(s)`, `0<C(s)<∞`. Teprve pak, jako limity
(M0') a (M∞'):

\[
0\le C(s)-C_{\delta,R}(s)\le\frac{\delta^s}{s}+\frac{(k+2)!}{R}.
\tag{M}
\]

### 2.2 Univerzální dolní obálka a algoritmus pro `C`

Pro redukované `r=a/c>0` definuj

\[
\boxed{\;D_b(r):=2^{-\lceil c(b+1+c)/a\rceil},
\qquad
\frac{D_b(r)^{\,r}}{r}\le 2^{-(b+1)}\;}
\]

(kontrola: `D_b(r)^r≤2^{-(b+1+c)}` a `1/r=c/a≤c≤2^c`). Modulový
algoritmus pro `C(s)`, `s=a/c` redukované, cíl `2^{-b}`:

\[
\delta_b^C=D_b(s),
\qquad
R_b^C=(k+2)!\,2^{\,b+1},\quad k=\lceil s-1\rceil .
\]

Výstupem jsou explicitní racionální čísla; POW_RAT_QCERT se používá
jen na racionální základ `2`.

### 2.3 Modulové algoritmy pro `E`, `O`, `B` (výstupní formule)

Se stejnou obálkou `D_b` a s řadovým odhadem
`e^{x²}≥x^{2ℓ}/ℓ!` (tedy `x^k e^{-x²}≤ℓ!/x²` pro `x≥1`, `2ℓ≥k+2`):

\[
\begin{aligned}
E(s):\quad
&k_E=\lceil s-1\rceil,\quad
\ell_E=\Bigl\lceil\tfrac{k_E+2}{2}\Bigr\rceil,\quad
\delta_b^{E}=D_b(s),\quad
R_b^{E}=\ell_E!\,2^{\,b+1};
\\[2mm]
O(s):\quad
&k_O=\lceil s\rceil,\quad
\ell_O=\Bigl\lceil\tfrac{k_O+2}{2}\Bigr\rceil,\quad
\delta_b^{O}=D_b(s{+}1),\quad
R_b^{O}=\ell_O!\,2^{\,b+1};
\\[2mm]
B(p,q):\quad
&\delta_b^{B}=D_{b+1}(p),\quad
{\delta'}_b^{B}=D_{b+1}(q),
\end{aligned}
\]

kde u Beta stačí univerzální racionální majoranta
`max(1,2^{1-q})≤2` na `(0,1/2]` (a symetricky), takže dolní řez
přispívá `≤2·D_{b+1}(p)^p/p≤2^{-(b+1)}` a horní totéž s `q`;
u `O` je dolní příspěvek `δ^{s+1}/(s+1)≤2^{-(b+1)}` s `δ=D_b(s+1)`
(je-li `s=a/c` redukované, je `s+1=(a+c)/c` opět redukované).
Součet vždy `≤2^{-b}`.

**Rozsah štítku:** `WP3D_QPOS_TAIL_MODULI` pokrývá **pouze holá
semena `C,B,E,O`**. Oblečená semena `\hat E,\hat O,\hat C` mají
existenci (substitucí, §6), ale žádný modulový nárok; ten by
vyžadoval zamčené racionální obálky `pi_atan` (WP3B dává
`3<pi_atan<16/5`) a je ponechán mimo tento balík.

### 2.4 Přesná kotva, rekurence a balíčkový uzel

FTC: `C(1)=lim(e^{-δ}-e^{-R})=1` — uzel `C_UNIT_ANCHOR_QPOS`.
Z derivace `d/dx(x^s e^{-x})` a řezových certifikátů okrajů:

\[
\boxed{C(s+1)=s\,C(s)} .
\tag{REC}
\]

Beta: (B-SPLIT) `B(p,q)=B(p+1,q)+B(p,q+1)`; per partes (B-PARTS)
`qB(p+1,q)=pB(p,q+1)`; odtud (B-REC)
`B(p+1,q)=\tfrac{p}{p+q}B(p,q)`, `B(p,q+1)=\tfrac{q}{p+q}B(p,q)`;
symetrie z afinního `u↦1-u`.

Uzly vrstvy semen (existence, moduly, kotva, rekurence, symetrie) se
agregují do uzlu **`QPOS_SEED_PACKAGE`**, který je povinným předkem
koncového sinku (§8); tím žádný primární uzel není mrtvý.

## 3. Pullback sudého semene, spojovací uzel a most

Substituce `y=x²` na řezech (kladná `C¹`), kofinální lemma §1:

\[
\boxed{E(s)=\tfrac12\,C(s/2)} .
\tag{E-PULL}
\]

### 3.1 Spojovací uzel

Na řezech `x·x^{s-1}=x^{s}` (POW_RAT_ANALYTIC), integrandy splývají:

\[
\boxed{O(s)=E(s+1)}
\tag{JOIN}
\]

— uzel `ODD_EVEN_SHIFT_JOIN_QPOS`; definice zůstávají oddělené.

### 3.2 Most

Z (E-PULL): `C(1/2)=2E(1)=I`. Rodičovský certifikátový uzel
`PI_ATAN_GAUSS_TYPED_IDENTITY` dává

\[
C(\tfrac12)^2=\pi_{\mathrm{atan}},
\qquad C(\tfrac12)>0
\tag{BRIDGE}
\]

— uzel `BRIDGE_SPECIALIZATION_QPOS`, jediné místo, kde primární graf
spotřebovává WP3C.

## 4. Produktová identita na racionálním řezu

Beze změny proti v2 (matematicky schváleno): kompaktní krok pro
`p,q≥1` (čtverec `[0,R]²`, diagonála, směrnice `y=xt`, kompaktní
Fubini, `w=x(1+t)`, stejnoměrné sevření (M∞') s `R(1+t)≥R` a vahou
`≤1`, spojitost částečných integrálů jako výslovná součást
FUBINI-COMPACT), identita (TRI), půlicí pullback `u=t/(1+t)`
(diagonála `t=1` ↦ střed `u=1/2`, platnost jen `p,q≥1`), a dvoukrokový
sestup přes (REC) + (B-REC) na celé `Q_{>0}²` — uzel
`MELLIN_PRODUCT_IDENTITY_QPOS`.

## 5. Bezodmocninová duplikace na racionálním řezu

Beze změny proti v2: (B-HALF) `B(p,p)=2^{1-2p}B(1/2,p)` pro `p≥1`
(afinní `u=(1+v)/2`, sudost, `v=w^{1/2}` s TRUNC-0 usmířením), pak
diagonální dvojkrokový sestup

\[
B(p{+}1,p)=\tfrac12 B(p,p),\quad
B(p{+}1,p{+}1)=\tfrac{p}{2p+1}B(p{+}1,p),\quad
B(\tfrac12,p{+}1)=\tfrac{2p}{2p+1}B(\tfrac12,p)
\]

s přesným krácením mocnin dvojky — uzel `BETA_HALF_IDENTITY_QPOS`;
a duplikační řez

\[
\boxed{C(p)\,C(p+\tfrac12)=2^{1-2p}\,C(\tfrac12)\,C(2p)}
\tag{DUP}
\]

(dvakrát (MP), jednou (B-HALF), dělení kladnými `C(p+1/2)`, `C(p)`)
— uzel `DUPLICATION_SCALAR_QPOS`.

## 6. Oblečený řez `Ê·Ô=Ĉ` a kotva `s=1`

### 6.1 Kvadraticko-lineární pullback

`x=r²` na řezech (kofinální lemma §1):

\[
\hat C(s)=4\int_0^\infty e^{-2p r^2}r^{2s-1}dr
=2\int_0^\infty e^{-2p x}x^{s-1}dx
\tag{C-QL}
\]

— uzel `C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS`.

### 6.2 Výpočet řezu

`x=y·c`, `c=C(1/2)^{-1}` (POW_RAT na kladné konstantě), (E-PULL),
(JOIN), `w=2\pi_{\mathrm{atan}}x` v (C-QL):

\[
\hat E(s)=C(\tfrac12)^{-s}C(\tfrac s2),
\quad
\hat O(s)=C(\tfrac12)^{-(s+1)}C(\tfrac{s+1}2),
\quad
\hat C(s)=2\,(2\pi_{\mathrm{atan}})^{-s}C(s),
\]

a dosazením (DUP) s `p=s/2` a `C(1/2)^{-2s}=\pi_{\mathrm{atan}}^{-s}`:

\[
\hat E(s)\,\hat O(s)=\hat C(s)
\]

— uzel `DRESSED_EOC_QPOS`; koncový uzel `WP3D_QPOS_SCALAR_SLICE`.

### 6.3 Kotva `s=1`

**Bez dalšího rodičovského uzlu** (rovnost `\hat E(1)=1` už
spotřebovává (BRIDGE)): `\hat E(1)=C(\tfrac12)^{-1}C(\tfrac12)=1`,
`\hat O(1)=\hat C(1)=1/\pi_{\mathrm{atan}}`.

*Identifikační poznámka [AUDIT_ONLY]:* substitucí z definice je
`\hat E(1)=G(\pi_{\mathrm{atan}})`, takže řez `s=1` reprodukuje
rodičovský uzel `P_GAUSSIAN_NORMALIZED` — křížová kontrola
`S1_ANCHOR_IDENTIFICATION_AUDIT`, mimo primární graf.

## 7. Měřítkový falzifikátor: právě tři algebraické rovnostní detektory

Při `dμ_λ=λdx` škálují všechna semena lineárně. (MP) i (DUP) jsou
homogenní stupně 2 na obou stranách — kalibraci nedetekují. **Právě
tři algebraické rovnostní detektory** jsou

\[
C_λ(1)=λ,\qquad
C_λ(\tfrac12)^2=λ^2\pi_{\mathrm{atan}},\qquad
\hat E_λ\hat O_λ=λ\,\hat C_λ
\]

(uzly `C_UNIT_ANCHOR_QPOS`, `BRIDGE_SPECIALIZATION_QPOS`,
`DRESSED_EOC_QPOS`; poslední proto, že levá strana má stupeň 2 a
pravá 1). Ocasní **moduly** jsou změnou míry citlivé také, ale nejsou
rovnostními detektory — jejich mutace se testuje samostatně (§10).

## 8. Co přesně přehrává exaktní konečný kernel

Okruh přehrání je jednoznačně

\[
\boxed{\;\mathbb Q[g,g^{-1}],\qquad \hat\pi:=g^2\;}
\]

(žádná dvojznačná lokalizace; `\hat\pi^{-1}=g^{-2}` je v okruhu).
Zmrazené meze:

```text
N_input          = 6      # vstupní půlindexy 1 ≤ k ≤ N_input, argumenty k/2
N_value          = 12     # uzávěr závislostí: DUP pro p=k/2 potřebuje C do půlindexu 2k ≤ N_value
EOC replay domain = s ∈ {1, 2, 3}   # jen celá s; obecné k/2 by dalo g^{-1/2}, 2^{1/2}, C(k/4)
```

Oba indexy `1≤j,k≤N` jsou vynucené; vstupní mez a uzávěr závislostí
jsou rozlišené. Bez plovoucí čárky se přehrává:

- rozklad čtverce, diagonální stráž, sestavení `B` ze dvou polovin
  kolem `u=1/2` (rovnosti racionálních funkcí a exponentových
  vektorů);
- jakobiány: `x` (směrnice), `(1-u)^{-2}`, lineární `w=x(1+t)` a
  `w=2\hat\pi x`, kvadratické `y=x²`, `x=r²`, odmocninový `v=w^{1/2}`;
- koeficienty (REC), (B-SPLIT), (B-PARTS), (B-REC), sestup §4.3,
  diagonální dvojkrok §5, (JOIN) jako exponentová rovnost;
- `HALF_LATTICE_BOUNDED_REPLAY_N`: pro `k≤N_input` redukce
  `C(k/2)`, `B(j/2,k/2)` rekurencemi na prvky `\mathbb Q[g,g^{-1}]`
  (hodnoty do půlindexu `N_value`) a exaktní ověření (DUP) na tomto
  rozsahu; (EOC) jen pro `s∈{1,2,3}`; zvláště `B(1/2,1/2)=g^2` a
  kotva `s=1`. Neomezené tvrzení jen s explicitním indukčním
  certifikátem (symbolický rekurentní krok + báze); jinak platí
  pouze zmrazený rozsah;
- dosažitelnost: jediný sink `WP3D_QPOS_SCALAR_SLICE`; každý primární
  uzel je jeho předkem; vrstvu semen (včetně `C_UNIT_ANCHOR_QPOS`)
  váže povinný agregátor `QPOS_SEED_PACKAGE` s povinnými předchůdci
  `MELLIN_PRODUCT_IDENTITY_QPOS` a `BRIDGE_SPECIALIZATION_QPOS` na
  cestě k sinku.

Kernel nepřehrává limitní analýzu, moduly ani intervalové obaly;
stav `PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB`, nikdy
`FORMALLY_VERIFIED`.

## 9. Nezávislé kontroly (AUDIT_ONLY, mimo primární graf)

- **A. Rederivace mostu bodem (1/2,1/2).** Začíná explicitně Beta
  symetrií a půlicím pullbackem na řezech:
  \[
  B(\tfrac12,\tfrac12)
  =2\int_0^{1/2}\frac{du}{\sqrt{u(1-u)}}
  =2\int_0^1\frac{t^{-1/2}}{1+t}\,dt
  =4F
  \]
  (druhá rovnost `u=t/(1+t)` na `[η,1]` s monotónní limitou, třetí
  `t=v²`; není potřeba integrál přes `(0,∞)` ani krok `t↦1/t`).
  (MP) v bodě `(1/2,1/2)` (sestup §4.3, bez (BRIDGE)) pak uzavře
  `C(1/2)²=C(1)B(1/2,1/2)=4F=\pi_{\mathrm{atan}}`. Audit odvozuje
  relaci `g²=\hat\pi` **analyticky, mimo okruh** `\mathbb Q[g,g^{-1}]`,
  který ji už předpokládá; (TRI) se pod `p,q<1` necituje.
- **B. Wallisova mřížka.** (DUP) na půlceločíselné mřížce proti
  dvojným faktoriálům WP3C §4.

## 10. Povinné záporné zkoušky

Validátor musí odmítnout alespoň (1–23 jako ve v2, s úpravami):

1. nepovolenou závislost na Gamma/Beta teorii (hodnota, identita,
   věta mimo graf); test jména symbolu nesmí být odmítacím důvodem;
2. goniometrickou substituci nebo polární krok;
3. kruhové `pi` v oblečených semenech místo `pi_atan`;
4. prohození nekonečných iterovaných integrálů bez useknutí;
5. chybný jakobián `u=t/(1+t)` nebo chybějící faktor `x` v `y=xt`;
6. mutaci duplikačního faktoru (`2^{-2p}`, `2^{2-2p}`, přemístěné
   `C(1/2)`);
7. sestup §4.3 bez svědka (B-PARTS);
8. (MP)/(DUP) pro `p≤0`, `q≤0` či iracionální exponent;
9. `x^{s-1}` v `x=0` bez řezu pro `s<1`;
10. vypuštění okrajových členů bez racionálního certifikátu;
11. (BRIDGE) bez citace `PI_ATAN_GAUSS_TYPED_IDENTITY`, citaci brány
    místo uzlu, nebo `sqrt` jako nový symbol;
12. měřítkovou mutaci adresovanou na (MP)/(DUP); správné zkoušky
    míří na tři rovnostní detektory §7 a všechny tři musí mutaci
    chytit; samostatná zkouška pro modulovou vrstvu (mutovaný modul
    při změněné míře nesmí projít);
13. limitu `R→∞` bez stejnoměrného sevření (M∞');
14. definici `O(s):=E(s+1)` či jiné křížové čtení v definiční
    vrstvě;
15. výrok o holomorfnosti, komplexním `s`, pokračování, Fourierovi,
    funkcionální rovnici, místním modulu, archimédovském místě;
16. kernelovou závislost na numerické hodnotě `\hat\pi` mimo
    `\mathbb Q[g,g^{-1}]`, `\hat\pi=g²`; přehrání mimo zmrazené meze
    (`k>N_input`, hodnota za `N_value`, (EOC) pro `s∉{1,2,3}`, např.
    `s=1/2`); neomezené mřížkové tvrzení bez indukčního certifikátu;
17. mutaci (E-PULL) (`1/2↦1`, `s/2↦s`);
18. chybný jakobián `y=x²`, `x=r²` (C-QL) nebo `v=w^{1/2}`;
19. POW_RAT přes `exp(r·log x)`/logaritmus/iracionální exponent;
    záměnu vrstev ANALYTIC/QCERT; přeskočený uzel odvozovacího grafu
    §1 (např. „existence z monotonie“ bez supremového uzlu);
20. jednokrokový (B-REC) svědek diagonálního sestupu;
21. citaci (TRI) či půlicího rozkladu §4.2 pro `p<1` nebo `q<1`
    (včetně auditu §9.A);
22. modulové tvrzení bez algoritmického výstupu — pro každé ze
    semen `C,B,E,O` musí být výstupní formule (§2.2–2.3); ocasní
    symboly před konstrukcí nevlastního integrálu; modulový nárok na
    oblečená semena (mimo rozsah štítku);
23. stavový nárok nad rámec řezu: `MELLIN_SEEDS`,
    `MELLIN_PRODUCT_IDENTITY` či `WP2_SCALAR_SEAM` v jiné než bajtově
    zděděné hodnotě (§11.A) — včetně „vylepšených“ blokačních kódů
    v mapě bran; mrtvý primární uzel (uzel bez cesty k sinku).

## 10a. Strojová smlouva (skeleton ke zmrazení před kernelem)

Whitelist, DAG a no-go musí být zmrazeny jako strojové položky, ne
próza. Skeleton (hodnoty finalizuje freeze):

```text
allowed_types        : Nat, Int, Rat (redukované a/c), Real(parent),
                       RatExponent, CompactCut(δ,R), SeedFamily{C,B,E,O,Ê,Ô,Ĉ},
                       RingElem(Q[g,g^{-1}])
allowed_operations   : tělesové operace a přesné nerovnosti; kompaktní
                       orientovaný integrál + FTC; kompaktní Fubini na
                       obdélníku s diagonální stráží; 1D kladná C¹
                       substituce + reflexe; exp řada s racionálním
                       zbytkem; supremový kořen (POW_RAT_ANALYTIC graf);
                       monotónní sup přes racionální síť řezů;
                       kofinální přechod (δ,R)↦(δ²,R²)
proof_registry       : uzly §2–§6 pod kanonickými ID z §11.C,
                       agregátor QPOS_SEED_PACKAGE, sink WP3D_QPOS_SCALAR_SLICE
semantic_rules       : import = závislost, ne jméno (§0.2); oddělení
                       definiční vrstvy a spojovacích uzlů (§0.3);
                       (TRI) jen p,q≥1; typování k rodičovské míře;
                       moduly jen s výstupní formulí
allowed_source_ast   : bez ast.Div (pravé dělení; celočíselné `//`
                       povoleno), bez float literálů, bez importů mimo
                       allowed_imports, AST whitelist po vzoru WP3C
                       kernel auditu
allowed_imports      : žádné (kernel je uzavřený; fractions-ekvivalent
                       vlastní implementací, rozhodne freeze)
audit_only_registry  : BRIDGE_REDERIVATION_AUDIT,
                       S1_ANCHOR_IDENTIFICATION_AUDIT,
                       WALLIS_LATTICE_CROSSCHECK
measure_binding      : rodičovská aditivní délková míra; součinová
                       míra vázána na tutéž 1D míru; tři rovnostní
                       detektory kalibrace (§7)
parameter_domains    : s,p,q ∈ Q_{>0} redukované; b ∈ Nat;
                       N_input=6, N_value=12, EOC ∈ {1,2,3}
resource_bounds      : po vzoru rodiče (max_certificate_rational_bits,
                       max_fixtures, json limity) — čísla určí freeze
result_dependencies  : hrany DAG: QPOS_SEED_PACKAGE →
                       {E_HALF_PULLBACK_QPOS, ODD_EVEN_SHIFT_JOIN_QPOS,
                        BRIDGE_SPECIALIZATION_QPOS} →
                       MELLIN_PRODUCT_IDENTITY_QPOS →
                       {BETA_HALF_IDENTITY_QPOS, DUPLICATION_SCALAR_QPOS} →
                       {C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS, DRESSED_EOC_QPOS} →
                       WP3D_QPOS_SCALAR_SLICE
```

## 11. Výsledkové štítky

### 11.A Zděděná mapa bran — bajtově, beze změn

Převzato doslovně z `jipc_wp3c_gauss_universe.json` (hodnoty se
nesmějí přeformulovat; nová vysvětlení patří do `blocker_details`):

```text
ARCHIMEDEAN_PLACE_CONSTRUCTION      = BLOCKED
CIRCLE_PI_IDENTIFICATION            = BLOCKED
FOURIER_SELF_DUAL_NORMALIZATION     = BLOCKED
FULL_C_EFF                          = BLOCKED
G1_LOCAL_CHILDREN                   = BLOCKED
G2_REPRESENTATION_SEAM              = BLOCKED
G3_TATE_MODULE                      = BLOCKED
GAUSSIAN_FINITE_SQUARE_SCHEMA       = PASS
GAUSSIAN_NORMALIZATION_BRIDGE       = PASS_RELATIVE_TO_GAUSSIAN_CALCULUS_TCB
LOCAL_ZETA_MODULE                   = BLOCKED
MELLIN_PRODUCT_IDENTITY             = BLOCKED
MELLIN_SEEDS                        = BLOCKED
PHYSICAL_MEASURE_SELECTION          = BLOCKED
PI_ATAN_EQUALS_PI_GAUSS             = PASS_RELATIVE_TO_GAUSSIAN_CALCULUS_TCB
STANDARD_PI_IDENTIFICATION          = BLOCKED
WP2_O_GAUSSIAN_BRIDGE               = PASS_RELATIVE_TO_GAUSSIAN_CALCULUS_TCB
WP2_O_POSITIVE_P                    = PASS_INHERITED_FROM_WP3B
WP2_SCALAR_NORMALIZATION_OBSTRUCTION= CLEARED_RELATIVE_TO_GAUSSIAN_CALCULUS_TCB
WP2_SCALAR_SEAM                     = BLOCKED_BY_MELLIN_PRODUCT_IDENTITY
```

Zděděný kontrolní výsledek `SCALAR_GAMMA_ORBIT_THEOREM = NONUNIQUE…`
se přebírá **bajtově z WP2 universe** (přesnou hodnotu vloží freeze
z locknutého souboru; zde se nesmí přepisovat po paměti).

### 11.B `blocker_details` (vysvětlení, ne hodnoty bran)

```text
MELLIN_SEEDS            : chybí účinné holomorfní jádro (komplexní koule, Re(s)>0)
MELLIN_PRODUCT_IDENTITY : dokázán jen racionální hodnotový řez Q_{>0}
WP2_SCALAR_SEAM         : chybí globální meromorfní identita; QPOS řez viz WP3D_QPOS_SCALAR_SLICE
```

### 11.C Nové QPOS štítky

```text
QPOS_SEED_PACKAGE                   = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
WP3D_QPOS_MELLIN_FAMILIES           = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
WP3D_QPOS_TAIL_MODULI               = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB   # jen holá semena C,B,E,O
C_UNIT_ANCHOR_QPOS                  = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
C_SHIFT_RECURRENCE_QPOS             = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
E_HALF_PULLBACK_QPOS                = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
ODD_EVEN_SHIFT_JOIN_QPOS            = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
BRIDGE_SPECIALIZATION_QPOS          = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
MELLIN_PRODUCT_IDENTITY_QPOS        = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
BETA_MIDPOINT_SPLIT_QPOS            = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
BETA_RECURRENCE_DESCENT_QPOS        = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
BETA_HALF_IDENTITY_QPOS             = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
DUPLICATION_SCALAR_QPOS             = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
DRESSED_EOC_QPOS                    = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
WP3D_QPOS_SCALAR_SLICE              = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB

HALF_LATTICE_BOUNDED_REPLAY_N       = EXECUTED_EXACT_KERNEL_BOUNDED (N_input=6, N_value=12, EOC∈{1,2,3})
BRIDGE_REDERIVATION_AUDIT           = AUDIT_ONLY_NOT_IN_PRIMARY_PROOF_GRAPH
S1_ANCHOR_IDENTIFICATION_AUDIT      = AUDIT_ONLY_NOT_IN_PRIMARY_PROOF_GRAPH
WALLIS_LATTICE_CROSSCHECK           = AUDIT_ONLY_NOT_IN_PRIMARY_PROOF_GRAPH

MELLIN_EFFECTIVE_NAME               = BLOCKED_FINITE_INTEGRAL_BALL_KERNEL
GAMMA_AS_COMPLEX_FUNCTION           = BLOCKED
ANALYTIC_CONTINUATION               = BLOCKED
POISSON_SUMMATION                   = BLOCKED
FUNCTIONAL_EQUATION                 = BLOCKED
```

### 11.D Rozsahové stavy

```text
COMPLETENESS_CAPABILITY     = NONE
CLASS_VERDICT               = NOT_REQUESTED
NO_GO_RESULT                = NONE_IN_THIS_PACKAGE
CONSTRUCTION_CONTENT_STATUS = PASS_RELATIVE_TO_MELLIN_CALCULUS_TCB
PROTOCOL_VERDICT            = NO_VERDICT
```

WP3D-QPOS-MELLIN smí říci: v převzaté míře existují racionální
Mellinovy rodiny `E,O,C` s algoritmickými ocasními moduly (výstupní
formule pro všechna čtyři holá semena), splňují na `Q_{>0}`
produktovou identitu, bezodmocninovou duplikaci a oblečený řez
`Ê·Ô=Ĉ` s kotvou `s=1`. Nesmí říci nic o holomorfnosti, globální
identitě, Gamma funkci, kruhovém `pi`, samoduální míře, funkcionální
rovnici ani archimédovském místě.

## 12. Cesta k WP2 (mimo tento balík)

```text
1. nezávislé účinné holomorfní E/O/C          (komplexní koule, účinné jádro)
2. identita E(s)O(s)=C(s) na Re(s)>0          (holomorfní rozšíření řezu)
3. rekurentní meromorfní pokračování          (přes (REC))
4. globální WP2 skalární šev                  (O-SCALAR-SEAM)
```

Fourierův a Poissonův krok až potom. Nejdřív se zmrazí tento QPOS
mezistupeň: kernel, validátor a fixtures se staví nad §10a smlouvou.
