# JIPC WP3D-QPOS-MELLIN — návrh důkazového kontraktu (DRAFT v3)


Stav: **DRAFT / NOTES LANE / NON-CANONICAL / UNREGISTERED / NEZMRAZENO /
PUBLIC-FREEZE-READY: NO**.

Veřejný audit nad Public Canon v65 rozlišuje matematické jádro od
připravenosti veřejného protokolu:

```text
NOTES_LANE_MERGE              = PASS
QPOS_CORE_IDENTITIES          = NO_COUNTEREXAMPLE_FOUND
WRITTEN_PROOF_CARRIER         = INCOMPLETE
PUBLIC_PARENT_PROVENANCE      = BLOCKED
MACHINE_CONTRACT              = UNFROZEN
PUBLIC_FREEZE_READY           = BLOCKED
```

Historický interní verdikt `QPOS_* = PASS_MATHEMATICALLY` znamená
pouze, že audit nenašel protipříklad k rovnicím (MP), (DUP) a (EOC).
Neznamená sebeobsažný veřejný důkaz, veřejně přípustnou premisovou
stopu ani připravenost k pinu. §4–§5 níže opravují algebraický nosič,
ale úplný řezový důkaz musí být před veřejným pinem ještě uzavřen.
§10a je nezmrazený návrh a §0.1 používá neveřejného rodiče. Tento
dokument je poznámka, ne certifikát; nemění Canon, registr, veřejnou
mapu bran ani stav JIPC.

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

### 0.1 Interní provenance a parent-lock — bez veřejné autority

Historickým interním rodičem je `I-JIPC-WP3C-GAUSSIAN-BRIDGE-v1@0.1.0`.
Tento vztah je v notes lane pouze discovery context. Budoucí veřejná
proba jej nesmí použít jako premisu, evidenci ani hranu důkazového
grafu. Vnější interní freeze obal (mimo archiv):

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

— uzel `BRIDGE_SPECIALIZATION_QPOS`, jediné místo, kde interní
primární graf spotřebovává WP3C. Ve veřejné cestě je tato hrana
zakázána a nahrazuje ji sebeobsažný most podle §11.0.


## 4. Produktová identita na racionálním řezu

**AUDITNÍ STAV:** matematická cesta je konzistentní, ale úplný
kompaktní a limitní důkaz ještě musí být před veřejným pinem rozepsán
v `PREREG.md`. Odkaz na neveřejnou v2 není důkaz.

### 4.1 Kompaktní krok pro `p,q≥1`

Rozklad čtverce `[0,R]²` podél diagonály, substituce `y=xt` v obou
trojúhelnících a poté `w=x(1+t)` musí na úrovni řezů dát

\[
\begin{aligned}
C(p)C(q)=C(p+q)\biggl(
 &\int_0^1\frac{t^{q-1}}{(1+t)^{p+q}}\,dt\\
+&\int_0^1\frac{t^{p-1}}{(1+t)^{p+q}}\,dt
\biggr).
\end{aligned}
\tag{TRI}
\]

První integrál se při `u=t/(1+t)` a následné reflexi stane horní
polovinou `B(p,q)`, druhý dolní polovinou. Tím má kompaktní krok
uzavřít

\[
C(p)C(q)=C(p+q)B(p,q),\qquad p,q\ge1.
\tag{MP>=1}
\]

Veřejná verze musí zvlášť dokázat stejnoměrné mizení ocasu pro
`t∈[0,1]` a nesmí použít Tonelliho větu na nekonečné oblasti.

### 4.2 Půlicí rozklad

(TRI) smí být citována jen v oblasti `p,q≥1`. Půlicí rozklad přes
`u=t/(1+t)` je omezen na tento kompaktní krok; nesmí být přímo
citován pro `p<1` nebo `q<1`.

### 4.3 Konečný sestup na `Q_{>0}²`

Jestliže (MP) platí v `(p+1,q)`, pak z (REC) a (B-REC)

\[
\begin{aligned}
p\,C(p)C(q)
 &=C(p+1)C(q)\\
 &=C(p+q+1)B(p+1,q)\\
 &=(p+q)C(p+q)\frac{p}{p+q}B(p,q)\\
 &=p\,C(p+q)B(p,q).
\end{aligned}
\]

Protože `p>0`, krácení dává (MP) v `(p,q)`. Druhý argument se
snižuje symetricky. Pro každé `p,q∈Q_{>0}` se nejprve zvolí konečné
celé posuny do oblasti `≥1` a pak se provede konečně mnoho těchto
kroků. Koncovým uzlem je `MELLIN_PRODUCT_IDENTITY_QPOS`.


## 5. Bezodmocninová duplikace na racionálním řezu

**AUDITNÍ STAV:** výsledná identita a algebraický sestup jsou správné,
ale řezová substituční část musí být před veřejným pinem doplněna.

### 5.1 Základní půlicí identita

Pro `p≥1` má afinní substituce `u=(1+v)/2`, sudost a následný
řezový pullback `w=v²` dát

\[
B(p,p)=2^{1-2p}B(\tfrac12,p).
\tag{B-HALF>=1}
\]

Veřejná verze musí vést poslední substituci na řezech `[η,1]`,
dokázat kofinalitu při `η\downarrow0` a zapsat okrajové odhady.

### 5.2 Diagonální sestup

\[
B(p+1,p)=\tfrac12B(p,p),
\]

\[
B(p+1,p+1)=\frac{p}{2p+1}B(p+1,p)
          =\frac{p}{2(2p+1)}B(p,p),
\]

\[
B(\tfrac12,p+1)=\frac{2p}{2p+1}B(\tfrac12,p).
\]

Dosazení (B-HALF) v bodě `p+1` a krácení kladného `p/(2p+1)` vrátí
identitu v bodě `p`. Konečný celočíselný posun ji rozšíří na všechna
`p∈Q_{>0}`. Uzel je `BETA_HALF_IDENTITY_QPOS`.

### 5.3 Duplikace

\[
B(p,p)=\frac{C(p)^2}{C(2p)},\qquad
B(\tfrac12,p)=
\frac{C(\tfrac12)C(p)}{C(p+\tfrac12)}.
\]

Tyto dvě instance (MP), (B-HALF) a kladnost dělených členů dávají

\[
\boxed{
C(p)C(p+\tfrac12)
=2^{1-2p}C(\tfrac12)C(2p)
}.
\tag{DUP}
\]

Koncovým uzlem je `DUPLICATION_SCALAR_QPOS`. Veřejný theorem-grade
stav zůstává zablokovaný do uzavření řezových důkazů §4.1 a §5.1.

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

Pro každou pevnou kladnou reálnou konstantu `a` je zobrazení řezů
`(δ,R)↦(aδ,aR)` kofinální: ke každému cílovému řezu `(δ',R')` lze
zvolit `δ≤δ'/a` a `R≥R'/a`. Toto škálovací lemma opravňuje níže
použité neracionální konstanty.

`x=y·c`, `c=C(1/2)^{-1}`, (E-PULL), (JOIN) a
`w=2\pi_{\mathrm{atan}}x` v (C-QL) dávají:

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


## 7. Měřítkový falzifikátor: tři normalizační zbytky

Při `dμ_λ=λdx`, `λ∈Q_{>0}`, škálují všechna jednorozměrná semena
lineárně. (MP) a (DUP) jsou homogenní stupně dva, a proto kalibraci
nedetekují. Tři pojmenované primitivní detektory jsou zbytky vůči
původním rovnicím:

\[
R_1(\lambda)=C_\lambda(1)-1=\lambda-1,
\]

\[
R_2(\lambda)=C_\lambda(\tfrac12)^2-\pi_{\mathrm{atan}}
=(\lambda^2-1)\pi_{\mathrm{atan}},
\]

\[
R_3(\lambda;s)=
\hat E_\lambda(s)\hat O_\lambda(s)-\hat C_\lambda(s)
=\lambda(\lambda-1)\hat C(s).
\]

Pro `λ>0`, `λ≠1` jsou všechny tři nenulové. Škálované transformační
zákony nesmějí být použity jako PASS podmínky mutovaného modelu.
Zmrazená fixture zvolí přesnou racionální hodnotu, například `λ=2`,
ponechá původní normalizační rovnice a vyžádá odmítnutí na všech
třech strážích. Ocasní moduly se testují samostatně.

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
- dosažitelnost: jediný sink je `WP3D_QPOS_SCALAR_SLICE`.
  `QPOS_SEED_PACKAGE` spotřebovává uzly existence, modulů, kotvy a
  rekurencí; není předkem svých vlastních složek. Produktová,
  duplikační a oblečená větev dosahují sinku vlastními skutečnými
  hranami. Orientaci `premisa -> spotřebitel` uvádí §10a.

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


## 10a. Strojová smlouva — NEZMRAZENÝ NÁVRH

Následující blok nesmí být použit jako pin ani spuštěn:

```text
FZ1_BRIDGE_SOURCE           = TBD_PUBLIC_PROOF_OR_INTERNAL_ONLY
FZ2_WRITTEN_PROOF_4_5      = INCOMPLETE
FZ3_ALLOWED_IMPORTS         = TBD
FZ4_RAT_AND_AST_POLICY      = TBD
FZ5_RESOURCE_AND_JSON_CAPS  = TBD
FZ6_ARTIFACT_SET_AND_HASHES = TBD
FREEZE_READY                = NO
```

Před změnou `FREEZE_READY` musí být uzavřen veřejně přípustný most,
doplněny řezové důkazy, určeny všechny strojové hodnoty, napsány a
staticky přijaty artefakty a zmrazen jejich úplný inventář a hashe.
Žádná hodnota se nesmí doplnit až při freeze.

Nezmrazený skeleton:

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
                       kofinální přechody (δ,R)↦(δ²,R²) a
                       (δ,R)↦(aδ,aR) pro pevné a>0
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
allowed_imports      : TBD_FREEZE_BLOCKER; zvolit právě jedno:
                       přesně `from fractions import Fraction`, nebo
                       vlastní normalizovaný Rat; hybrid je zakázán
audit_only_registry  : BRIDGE_REDERIVATION_AUDIT,
                       S1_ANCHOR_IDENTIFICATION_AUDIT,
                       WALLIS_LATTICE_CROSSCHECK
measure_binding      : rodičovská aditivní délková míra; součinová
                       míra vázána na tutéž 1D míru; tři rovnostní
                       detektory kalibrace (§7)
parameter_domains    : s,p,q ∈ Q_{>0} redukované; b ∈ Nat;
                       N_input=6, N_value=12, EOC ∈ {1,2,3}
resource_bounds      : TBD_FREEZE_BLOCKER; před pinem určit přesná
                       celá maxima pro čas, racionální bity, fixtures,
                       JSON, stdout a paměťový povrch
edge_direction       : premise -> consumer
bridge_source        : BRIDGE_SOURCE_QPOS = TBD_FREEZE_BLOCKER
result_dependencies  :
  WP3D_QPOS_MELLIN_FAMILIES -> WP3D_QPOS_TAIL_MODULI
  WP3D_QPOS_MELLIN_FAMILIES -> C_UNIT_ANCHOR_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> C_SHIFT_RECURRENCE_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> E_HALF_PULLBACK_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> ODD_EVEN_SHIFT_JOIN_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> BETA_MIDPOINT_SPLIT_QPOS
  WP3D_QPOS_MELLIN_FAMILIES -> BETA_RECURRENCE_DESCENT_QPOS
  WP3D_QPOS_TAIL_MODULI -> QPOS_SEED_PACKAGE
  C_UNIT_ANCHOR_QPOS -> QPOS_SEED_PACKAGE
  C_SHIFT_RECURRENCE_QPOS -> QPOS_SEED_PACKAGE
  BETA_MIDPOINT_SPLIT_QPOS -> QPOS_SEED_PACKAGE
  BETA_RECURRENCE_DESCENT_QPOS -> QPOS_SEED_PACKAGE
  C_SHIFT_RECURRENCE_QPOS -> MELLIN_PRODUCT_IDENTITY_QPOS
  BETA_RECURRENCE_DESCENT_QPOS -> MELLIN_PRODUCT_IDENTITY_QPOS
  BETA_MIDPOINT_SPLIT_QPOS -> BETA_HALF_IDENTITY_QPOS
  BETA_RECURRENCE_DESCENT_QPOS -> BETA_HALF_IDENTITY_QPOS
  MELLIN_PRODUCT_IDENTITY_QPOS -> DUPLICATION_SCALAR_QPOS
  BETA_HALF_IDENTITY_QPOS -> DUPLICATION_SCALAR_QPOS
  BRIDGE_SOURCE_QPOS -> BRIDGE_SPECIALIZATION_QPOS
  E_HALF_PULLBACK_QPOS -> DRESSED_EOC_QPOS
  ODD_EVEN_SHIFT_JOIN_QPOS -> DRESSED_EOC_QPOS
  C_QUADRATIC_TO_LINEAR_PULLBACK_QPOS -> DRESSED_EOC_QPOS
  BRIDGE_SPECIALIZATION_QPOS -> DRESSED_EOC_QPOS
  DUPLICATION_SCALAR_QPOS -> DRESSED_EOC_QPOS
  QPOS_SEED_PACKAGE -> WP3D_QPOS_SCALAR_SLICE
  MELLIN_PRODUCT_IDENTITY_QPOS -> WP3D_QPOS_SCALAR_SLICE
  DUPLICATION_SCALAR_QPOS -> WP3D_QPOS_SCALAR_SLICE
  DRESSED_EOC_QPOS -> WP3D_QPOS_SCALAR_SLICE
```

## 11. Výsledkové štítky

### 11.0 Veřejná a interní premisová hranice

```text
INTERNAL ROUTE:
  WP3C/WP2 locky mohou být interními premisami;
  žádný veřejný candidate-T ani veřejný pin z nich neplyne.

PUBLIC ROUTE:
  neveřejný archiv, attachment, interní hash, universe gate ani
  PI_ATAN_GAUSS_TYPED_IDENTITY jsou pouze discovery context;
  nesmějí být premisou, evidencí ani hranou veřejného grafu.
```

Ve veřejné cestě se §9.A přesune do primárního grafu a sebeobsažně
dokáže `C(1/2)^2=4∫_0^1dt/(1+t^2)`. Integrální konstanta dostane
odlišný název, například `p_I`; rovnost `p_M=p_I` musí vlastnit
výslovný veřejný Machinův most. Interní štítky níže nejsou veřejné
statusy `T/D/C/H/O/F`.

### 11.A Interní kompatibilitní mapa — bez veřejné autority

Následující mapa je pouze interní kompatibilitní údaj. V notes lane
nemění žádnou veřejnou bránu a do veřejné preregistrace se nepřenese.

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

Zděděná hodnota `SCALAR_GAMMA_ORBIT_THEOREM` není v tomto dokumentu
zmrazena:

```text
SCALAR_GAMMA_ORBIT_THEOREM = TBD_PRIVATE_READBACK
```

To je freeze blokátor interní cesty; ve veřejné cestě se tento řádek
i celá interní mapa §11.A vypouštějí.

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

Fourierův a Poissonův krok až potom. Dalším krokem není pin ani běh.
Nejprve musí být uzavřen veřejný most, doplněny řezové důkazy,
serializován DAG a určeny všechny `TBD_FREEZE_BLOCKER` hodnoty. Teprve
potom lze vytvořit dosud nespouštěný kernel, validátor a fixtures.
