# P-ALG-CONTACT-REALIZATION-1: Pi_alg a pevný překlad CW-ALG-1

**NON-CANONICAL, L1, candidate-T; veřejný přezkumný návrh. 6. října 2026.**
Tento soubor definuje jednoznačnou kandidátní gramatiku `CW-ALG-1` a její použití na algebraickou permutaci. Není přijetím věty do Canonu, registrací veřejné sondy, přijatým RunSpec ani oznámením výsledku nového běhu. `P-CONTACT-RECORD-1` zůstává samostatnou sondou se svým původním rozsahem. Nová spojovací věta pro V není součástí této sondy.

Tato specifikace zpřístupňuje celé potřebné matematické definice. Zdrojová provenance a SHA-256 původních podkladů jsou v `SOURCE_PROVENANCE.json`; případná nepřístupnost původního místního dokumentu neodstraňuje zde uvedenou gramatiku. Normativní zdrojové brány a čtení odpovídají veřejnému [Canonu v99 na neměnném commitu](https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md). Před případným veřejným přijetím pinů nebo během je nutná nová kontrola tehdy aktuální autority repozitáře; historický commit není tvrzením o aktuálním main.

## Přesné tvrzení a hranice

Na úplném nosiči X=F5^12×{0,1} definujeme projekci rho na F=F5^10×{0,1}, která zapomíná pouze q_x,q_y. Níže uvedený atlas definuje jednu sudou permutaci Pi_alg faktoru, odlišnou od původní lexikografické Pi. Stanovíme jediné pevné nativní slovo

\[
T_{\rm alg}=\operatorname{Expand}\bigl(\mathrm{CW\!\!-\!\!ALG\!\!-\!\!1}(\Pi_{\rm alg})\bigr).
\]

Závěr kandidátní věty je rho T_alg=Pi_alg rho na celém X, včetně libovolných obsazených r a libovolných neznámých q. Slovo vrací obě r přesně do vstupních hodnot. Na níže charakterizované dosažitelné množině Omega_alg platí G T_alg=M G a D_C T_alg=L5 D_C. Celý cílový krok má úplnou syntaktickou inverzi ReverseInvert(T_alg). Slovo nevyžaduje další nosič, čisté pracovní r, přípravu q, reset bitu ani nový nativní list. Jeho úplná expanze ani délka nejsou v tomto návrhu vypočteny nebo spuštěny. Referenční algebraický vykonávač sám není povolenou bránou.

## Úplné brány a homogenní makra

Níže uvedená Walshova tabulka určuje všech pět faktorových souřadnic buňky. Její inverze je 4krát transponovaná uvedená Walshova matice nad F5; spolu s následující q tabulkou proto určuje celou nativní mapu, nikoli pouze projekci.

| Nativní list | Působení na q |
|---|---|
| a_i | q_i zůstává |
| b_i | q_i se neguje |
| c_i,d_i | q_i se mění na 1-q_i |
| e_i | q_i se mění na 2-q_i |
| P,P^-1 | (q_x,q_y) se mění na (q_x,q_y ± q_x) |
| Q_cs,Q_cs^-1 | (q_x,q_y) se mění na (q_x ± q_y,q_y) |
| W_a | obě q zůstávají |
| W_b | při zvolené větvi se obě q negují, jinak zůstávají |

Jednobuněčné listy ostatní buňku fixují. Všechny tyto listy kromě W bit fixují. Přesné podmínky W a úplné faktorové mapy jsou uvedeny níže. Původní a,b,c,d,e,W_a,W_b jsou involuce; P a Q_cs mají uvedené syntaktické inverze.

Homogenizace má přesně tuto konečnou syntaxi:

\[
\tau_{q_i}=e_i d_i,\qquad
\bar a_i=a_i,\quad\bar b_i=b_i,\quad
\bar c_i=\tau_{q_i}^{-1}c_i,\quad
\bar d_i=\tau_{q_i}^{-1}d_i,\quad
\bar e_i=\tau_{q_i}^{-2}e_i.
\tag{11}
\]

Každé neupravené písmeno uvnitř pravé strany těchto definic je **terminální nativní list**. Homogenizace se na ně znovu rekurzivně nepoužívá. Tau_q přičítá 1 do q_i a celý faktor fixuje; každé bar c,bar d,bar e má q_i→-q_i. Homogenní makra jsou involuce na úplném nosiči. Tato makra jsou pouze syntaktické zkratky, nikoli nová primitiva.

## Verze gramatiky a povinné priority CW-ALG-1

1. Použije se původní uspořádaná šestnáctipísmenná makroabeceda (B1), původní (A4) Z_r=[K_0,tau_e_r]^2 a původní (A18) s W_a. Nepoužije se pozdější 48listý ani 20listý Z, varianta jen s W_b, DP násobicí strom ani jiná faktorově ekvivalentní zkratka.
2. Konstantní E_i(1) mají prioritu a vždy jsou translace z (A1)–(A2). Pro každý koeficient c v F5 se při převodu skaláru na opakování použije reprezentant c∈{0,1,2,3,4}. Explicitně napsané záporné exponenty a formální inverze v gramatice se ponechají jako syntaktické inverze. Žádný exponent již určeného SLOVA se neredukuje modulo 5 na základě jeho faktorového působení.
3. Atomy E_1(chi^k) a E_3(chi^k), kde chi je libovolná pístová Walshova souřadnice a k=1,...,4, mají vždy původní definici (A6)–(A7). Tato definice má prioritu před (A11), zejména pro chi=xi_2. Rekurze A11 se proto nikdy nemůže vracet sama do sebe přes E_1(xi_2^k).
4. E_2(xi_1) je přesně N21 z (A8), E_2(xi_3) je přesně N23 z (A9). Tyto dvě definice mají prioritu před (A11). (A11) se použije pouze pro zbývající atomy pracovních souřadnic. Atom E_2(chi^k) pro vnější chi∈L je přesně (A12).
5. Pořadí slov v konečném seznamu R_ij je délka–lex podle přesného čtyřpísmenného pořadí v A.4. Zvolí se první slovo splňující podmínku; epsilon_i,epsilon_j jsou pak jednoznačně znaménka jeho obrazů, nikoli další volba. Test probíhá na podepsaných permutačních maticích během konstrukce pevného slova. V exponentu A11 se znaménka vyhodnotí jako celá čísla ±1; výsledek -1 znamená syntaktickou inverzi, nikoli čtyři kopie.
6. Pro (A15) je použit přesný reprezentant c∈{0,...,4} a pevný součin translací tau_v v A.1. Pro součiny indikátorů v A16 se používá levý prefix prvních k-1 faktorů a poslední faktor v doslova uvedeném pořadí. Cíl/pomocná souřadnice jsou ty uvedené v A16; při vnoření A14 se tyto dvě souřadnice podle požadovaného cíle prohodí. Žádný jiný násobicí strom se nevybírá.
7. V B.3 při cyklické rotaci hrany se dvěma starými body je nový bod poslední; při hraně s jedním starým bodem je tento bod první. Zachovává se orientace, leda při přesně předepsané inverzi pro |U|=3. Všechny zbývající výběry jsou první/nejmenší podle uvedeného lex pořadí. Konečný rozklad permutace používá její doslovné cykly, jejich minima, určené transpoziční páry a pravidla B.2.
8. Expand zachovává pořadí součinů. Exponent n≥0 znamená n doslovných kopií; exponent -n znamená n kopií syntaktické inverze. Inverze součinu obrátí pořadí a invertuje jednotlivé listy. Neprovádí se přepis faktorově ekvivalentních maker, rušení nebo zkracování, které není doslovnou definicí této verze.

Tato pravidla odstraňují překryvy názvů atomů staršího textu a určují jeden konkrétní úplný q lift. Netvrdí, že všechny dřívější faktorově ekvivalentní aliasy mají na obsazených q totožný účinek. Matematické tvrzení faktoru se tím neposiluje. Odkazy na (11) v převzaté příloze znamenají přesně homogenizaci uvedenou zde.

## Základní souřadnice, faktor a konstrukční důkaz generování
Pracujeme nad \(\mathbb F_5\). Součiny operací působí **zprava doleva** a
\[
[F,G]=FGF^{-1}G^{-1}.
\]
Čísla v exponentu slova označují opakování, nikoli nový stav stroje.

Jedna buňka má souřadnice \((p_1,p_4,p'_1,p'_4,q,r)\). Zkratkou \(p=(p_1,p_2,p_3,p_4)\) dále rozumíme její čtyři pístové souřadnice v tomto pořadí. Píšeme
\[
\mathfrak q(p)=p_1p_4-p_2p_3,
\qquad K=\begin{pmatrix}0&0&0&3\\0&0&2&0\\0&2&0&0\\3&0&0&0\end{pmatrix}.
\]
Zmrazené \(C\) je právě \(K\oplus0_2\), bez jakékoli změny. Pro dvě buňky
\[
G=(\alpha,\beta,\gamma)=(\mathfrak q(p_x),p_x^TKp_y,\mathfrak q(p_y)),
\qquad h=\beta.
\]
Přebíráme veřejné čtení a cílový krok, nikoli jejich nový výběr:
\[
D_C=B_{\rm read}G,\quad
B_{\rm read}=\begin{pmatrix}1&4&2\\4&0&1\\3&4&4\end{pmatrix},\quad
L_5=\begin{pmatrix}3&3&2\\3&4&2\\3&2&0\end{pmatrix},
\]
\[
M=\begin{pmatrix}0&3&0\\4&4&4\\0&3&3\end{pmatrix},
\qquad B_{\rm read}M=L_5B_{\rm read},\qquad \det B_{\rm read}=1.
\]
\(B_{\rm read}\) se nesmí zaměnit s párovým působením \(\mathsf B=(b,b)\).

## 2. Zdrojové ověření před použitím cíle

Veřejná pístová matice je
\[
X_p=\begin{pmatrix}p_1&p_2\\p_3&p_4\end{pmatrix}.
\]
Veřejné \(a\) zamění sloupce; veřejné \(b\) zamění řádky a neguje všechny čtyři položky. Proto přesně, na celém nosiči,
\[
\mathfrak q(ap)=-\mathfrak q(p),\qquad
\mathfrak q(bp)=-\mathfrak q(p).
\]
Polarizace, s \(2^{-1}=3\), dává
\[
h(ax,ay)=-h(x,y),\qquad h(bx,by)=-h(x,y).
\]
To je zdrojová row/column symetrie [veřejného pístového reshapu][piston]. Nezávisí na \(M\), \(L_5\), paměťové kapacitě ani úspěchu kontaktu.

Označme \(\mathsf A=(a,a)\), \(\mathsf B=(b,b)\). Obě jsou komutující involuce. Pro \(i=a,b\) použijeme **přesně** uživatelovu bránu
\[
W_i(z,\eta)=
\begin{cases}
(z,\eta),&h(z)=0,\\
(\mathsf I_i^{\sigma(h(z))\oplus\eta}z,\sigma(h(z))),&h(z)\ne0,
\end{cases}
\]
kde \(\mathsf I_a=\mathsf A\), \(\mathsf I_b=\mathsf B\), \(\sigma=0\) na \(\{1,2\}\), \(\sigma=1\) na \(\{3,4\}\).

**Involutivita včetně obou bitů.** Na nenulové větvi položme \(s=\sigma(h)\), \(k=s\oplus\eta\). Po první aplikaci je orientace \(s'=s\oplus k=\eta\), bit je \(s\). Druhá aplikace tedy použije exponent \(s'\oplus s=k\), vrátí data a nastaví bit \(s'=\eta\). Nulová větev je identita. Tím
\[
W_a^2=W_b^2=I
\]
na celém \(\mathbb F_5^{12}\times\{0,1\}\), bez resetu a bez výjimky pro obsazenou paměť.

## 3. Transformační zákony a rozbití staré překážky

Použijme v každé buňce invertibilní Walshovy souřadnice
\[
\begin{aligned}
s&=p_1+p_2+p_3+p_4,&v&=p_1+p_2-p_3-p_4,\\
u&=p_1-p_2+p_3-p_4,&t&=p_1-p_2-p_3+p_4.
\end{aligned}
\]
Platí \(\mathfrak q=4(st-uv)\). Přesné působení původních písmen na \((s,v,u,t,r)\) je:

| Písmeno | Výstup \((s,v,u,t,r)\) |
|---|---|
| \(a\) | \((s,v,-u,-t,r)\) |
| \(b\) | \((-s,v,-u,t,-r)\) |
| \(c\) | \((1-s,v+2r,2-u,t-2r,-r)\) |
| \(d,e\) | \((-s,1-v,-u,2-t,1-r)\) |

\(P^{\pm1}\) přičítá/odečítá první buňku do druhé; \(Q_{\rm cs}^{\pm1}\) druhou do první, ve všech souřadnicích. Na Gramově trojici:
\[
P^{\pm1}G=(\alpha,\beta\pm\alpha,\gamma\pm2\beta+\alpha),
\]
\[
Q_{\rm cs}^{\pm1}G=(\alpha\pm2\beta+\gamma,\beta\pm\gamma,\gamma).
\]
Pro každé jednotlivé afinní písmeno s písty \(p'=Lp+t_g(r)\) platí při působení na první buňce
\[
G'=\bigl(\varepsilon_g\alpha+2\langle Lp_x,t_g\rangle+\mathfrak q(t_g),
\langle Lp_x,p_y\rangle+\langle t_g,p_y\rangle,\gamma\bigr),
\]
kde \(\langle p,v\rangle=p^TKv\), \(\varepsilon_{a,b,c}=-1\), \(\varepsilon_{d,e}=1\). Na druhé buňce je analogický vzorec s nezměněnou \(\alpha\). Konkrétně \(t_a=t_b=0\), \(t_c=(2,1+r,2,1-r)\), \(t_d=t_e=(2,1,3,4)\); lineární části jsou přímo určeny tabulkou. Tím jsou dány symbolické zákony všech původních generátorů, nikoli jen hodnoty na vzorku.

Obě nové brány mají na pozorování stejný zákon:
\[
(G,\eta)\mapsto
\begin{cases}(G,\eta),&\beta=0,\\
((-1)^{\sigma(\beta)\oplus\eta}G,\sigma(\beta)),&\beta\ne0.
\end{cases}
\]
Jejich působení na ostatní pístové údaje je rozdílné.

Starý pomocný základ byl
\[
\mathcal B=(S,V,R),\quad
S=(s_x,s_y),\quad V=(v_x,v_y),\quad R=(r_x,r_y).
\]
\(W_a\) jej nemění. Naproti tomu \(W_b\) na nenulové větvi posílá
\[
(S,V,R)\longmapsto((-1)^kS,V,(-1)^kR),\quad k=\sigma(h)\oplus\eta.
\]
\(k\) není určen starým základem ani starým základem spolu s bitem.

**Explicitní protipříklad faktorizace.** V obou stavech zvolme \(q_x=q_y=r_x=r_y=0\), \(\eta=0\),
\[
p_x=(4,4,4,4),\quad
p_y^+=(2,3,3,2),\quad p_y^-=(3,2,2,3).
\]
Oba mají \(S=(1,0),V=R=0\). Smíšené čtení je však \(h_+=1\), \(h_-=4\). První stav \(W_b\) ponechá, zatímco u druhého změní \(p_x\) na \((1,1,1,1)\), ponechá uvedené \(p_y^-\) a nastaví bit 1. Výstupní \(S\) jsou \((1,0)\) a \((4,0)\).

**Jediná mapa \(F_{W_b}:\mathcal B\to\mathcal B\) tedy neexistuje.** Předchozí no-go se na tuto novou abecedu nepřenáší.

## 4. Nejmenší přesný konečný faktor

Označme
\[
\rho:\mathbb F_5^{12}\times\{0,1\}\longrightarrow
\mathcal F=\mathbb F_5^{10}\times\{0,1\},
\]
kde \(\rho\) ponechá oba písty, obě \(r\) a bit, zapomene právě \(q_x,q_y\). Píšeme \(D=\mathbb F_5^{10}\),
\[
N=|\mathcal F|=19\,531\,250,\qquad |\rho^{-1}(f)|=25.
\]

Všechny generátory na \(\mathcal F\) působí jako permutace: žádné \(q\) nevstupuje do ponechaných souřadnic, \(G\) ani větvení \(W_i\). Toto dává přesnou uzavřenost.

Pro minimalitu definujme ekvivalenci úplných stavů rovností \((G,\eta)\) **po každém konečném slově celé nové abecedy**, včetně prázdného slova. Shodné \(\rho\) implikuje tuto nerozlišitelnost. Obráceně:

1. Rozdílné bity rozliší prázdné slovo.
2. Rozdílné písty rozliší původní translace, protože \(K\) je regulární a
   \[
   \mathfrak q(p+a)-\mathfrak q(p'+a)
   =\mathfrak q(p)-\mathfrak q(p')+2(p-p')^TKa
   \]
   nemůže pro \(p\ne p'\) zmizet pro všechna \(a\).
3. Jestliže se liší pouze některé \(r\), písmeno \(c\) vystaví nenulový pístový rozdíl \((0,\Delta r,0,-\Delta r)\); následná translace jej rozliší.

Potřebné translace jsou veřejně známé [KERNEL-CONNECT-ALL-K][translations]; příloha A navíc poskytuje jejich konkrétní slova pro tento faktor. Ekvivalence je proto přesně rovnost \(\rho\). **Jde o nejhrubší možný deterministický faktor zachovávající požadovaná pozorování pod všemi slovy**, nikoli o pouhý horní odhad velikosti.

Definujme \(\Omega_0=\{z\in X:\eta(z)=0\}\) s libovolnými písty, oběma r a oběma q. Každé písmeno bijektivně mapuje celé 25prvkové zapomenuté vlákno na celé další vlákno. Pro libovolné pevné slovo s faktorem \(\bar T\) tedy
\[
\bigcup_{n\ge0}T^n(\Omega_0)
=\rho^{-1}\!\left(\bigcup_{n\ge0}\bar T^n(D\times\{0\})\right).
\tag{1}
\]

## 5. Úplná grupa nové abecedy na faktoru

Nechť \(\Gamma\) je grupa všech konečných povolených slov na \(\mathcal F\). Dokážeme
\[
\boxed{\Gamma=\operatorname{Alt}(\mathcal F).}
\tag{2}
\]
Důkaz nepoužívá cíl \(M\). Skládá se z primitivity, konkrétního třícyklu a explicitního kompilátoru třícyklů.

### 5.1 Primitivita

Původní slova obsahují všechny translace \(D\), které působí shodně na obou bitových vrstvách. Každá vrstva je tedy tranzitivní a \(W_a\) některé stavy mezi vrstvami převádí. \(\Gamma\) je tranzitivní.

Každý systém bloků invariantní vůči translacím má jednu ze dvou podob:

- **Oddělené vrstvy:** bloky ve vrstvě \(\eta\) jsou kosety podprostoru \(H_\eta\le D\).
- **Spojené vrstvy:** bloky jsou
  \[
  ((z+H)\times\{0\})\ \cup\ ((z+d+H)\times\{1\})
  \tag{3}
  \]
  pro jeden podprostor \(H\) a jeden posun \(d\).

Úplnost klasifikace: blok obsahující \((0,0)\) má ve vrstvě 0 právě svůj translační stabilizátor \(H\); průnik s vrstvou 1 je buď prázdný, nebo jeden koset téhož \(H\). Translace poté určí všechny ostatní bloky. Při prázdném průniku se druhá vrstva klasifikuje samostatně.

V odděleném případě musí výstupní bit \(W_a\) být konstantní na každém kosetu \(H_\eta\). Jeho dvě funkce jsou
\[
f_0(h)=\mathbf1_{h\in\{3,4\}},\qquad
f_1(h)=\mathbf1_{h\notin\{1,2\}}.
\]
Pro obě je prostor aditivních period funkce \(f_\eta\circ h\) právě
\[
\operatorname{rad}(h)=\langle r_x,r_y\rangle.
\]
Skutečně, perioda \(v\) s \(h(v)\ne0\) by na přímce \(tv\) ztotožnila hodnoty u \(0,h(v),-h(v)\), což neplatí. Jestliže \(h(v)=0\), ale \(v\) neleží v radikálu, existuje \(z\), pro něž \(h(z+tv)\) proběhne celé \(\mathbb F_5\); ani to není perioda. Radikál naopak hodnotu nemění.

Tedy \(H_\eta\subseteq\langle r_x,r_y\rangle\). Invariance vůči lineárním částem \(c_x,c_y\), které nenulové \(r\) převádějí také do pístů, nutí \(H_\eta=0\). Dostáváme jen jednoprvkové bloky.

Ve spojeném případě mají původní afinní generátory na obou vrstvách stejné působení. Proto \(L_gH=H\) a \(L_gd-d\in H\). Píšeme-li \(d=(d_x,d_y)\), \(P\) dává \((0,d_x)\in H\), invariance vůči \(Q_{\rm cs}\) pak \((d_x,0)\in H\). Analogicky získáme \((d_y,0),(0,d_y)\in H\), tedy \(d\in H\). Posun v (3) lze vypustit.

Pro \(h(z)\ne0\) jsou oba vstupy \((z,0),(z,1)\) v témže bloku a jejich obrazy pod \(W_i\) mají data \(z,\mathsf I_i z\). Tedy
\[
(\mathsf A-I)z,(\mathsf B-I)z\in H\quad(h(z)\ne0).
\]
Aktivní vektory \(h\ne0\) lineárně generují \(D\): pro libovolné \(w\) vezměme aktivní \(v\); nenulový polynom \(h(v+tw)\) stupně nejvýše 2 nemůže zmizet ve všech čtyřech nenulových \(t\). Proto \(w\) je rozdílem násobků dvou aktivních vektorů.

Takže \(H\) obsahuje obrazy \(\mathsf A-I\) a \(\mathsf B-I\). V tabulce oddílu 3 jejich součet obsahuje všechny souřadnice \(S,U,T,R\). Lineární část \(c\) převádí \(r\) také do \(v\), čímž doplní \(V\). Tedy \(H=D\). Zbývá jen celý nosič jako jediný blok. Primitivita je dokázána.

### 5.2 Konkrétní třícyklus

Příloha A určuje výhradně povolenými slovy následující jediný třícyklus na \(\mathcal F\):
\[
C_*=(\zeta_0,\zeta_1,\zeta_2),
\tag{4}
\]
kde oba písty jsou pevné
\[
p_x=(3,0,3,0),\qquad p_y=(4,1,1,4),
\]
a
\[
\begin{array}{c|ccc}
&\zeta_0&\zeta_1&\zeta_2\\\hline
(r_x,r_y)&(2,0)&(0,1)&(3,0)\\
\eta&0&0&0
\end{array}
\]
Všechny ostatní faktorové stavy fixuje. Důkaz přílohy je algebraický a platí i pro libovolně obsazené původní pracovní souřadnice.

### 5.3 Od třícyklu ke všem sudým permutacím

Uspořádejme povolená písmena podle přílohy B. Vezměme **pevný konečný seznam** všech konjugovaných třícyklů
\[
wC_*w^{-1},\qquad |w|\le N,
\tag{5}
\]
v pořadí podle délky a potom lexikograficky. Jejich trojice podpor tvoří souvislý hypergraf.

Pro důkaz sledujme rozklad na komponenty po délce \(k\). Jakmile se rozklad při přidání délky \(k+1\) nezmění, každý generátor i jeho inverze komponenty permutuje: obraz každé dosavadní hrany je již hranou dalšího seznamu. Rozklad je tedy invariantním systémem bloků. Primitivita a počáteční neprázdná tříbodová hrana vylučují vše kromě jediné komponenty. Před stabilizací počet komponent pokaždé klesá, takže mez \(N\) postačuje.

Příloha B z takového souvislého seznamu **explicitně sestaví slovo pro libovolný třícyklus** a potom pro libovolnou sudou permutaci. Proto \(\operatorname{Alt}(\mathcal F)\subseteq\Gamma\). Není potřebná nevyčíslená klasifikační věta o primitivních grupách.

Opačná inkluze je také přesná. Každé původní písmeno působí stejnou permutací na dvou bitových vrstvách, tedy je sudé. Každé \(W_i\) má jednu transpozici na každou dvojici dat \(z,\mathsf I_i z\) s nenulovým \(h\). Počet aktivních dat je
\[
25(5^4-1)\,4\,5^3=7\,800\,000,
\]
proto \(W_i\) obsahuje \(3\,900\,000\) transpozic a je sudé. Tím platí (2).


## Algebraický atlas a přesná permutace

Následující atlas je přepis stávajících pístů, nikoli rozšíření fyzického stavu. Indexy j,n,L jsou souřadnice definice cílové permutace. Ve výsledném nativním slově nejsou nové registry.
## 1. Normalizace bez velkého pořadníku vláken

Písty dvou buněk zapišme jako matice `X,Y` rozměru 2×2. Pro pevné čtení

\[
g=(\alpha,\beta,\gamma)
=(\det X,\tfrac12[\det(X+Y)-\det X-\det Y],\det Y),
\qquad \kappa=\beta^2-\alpha\gamma.
\]

Vlákno `g=0` ponecháme celé beze změny. Pro `g≠0` zvolme nejmenší `t∈{0,1,2}` takové, že

\[
a=\alpha+2t\beta+t^2\gamma\ne0,\qquad b=\beta+t\gamma.
\]

Takové `t` existuje: nenulový polynom stupně nejvýše dva nemá tři různé kořeny. Položme

\[
D_a=\operatorname{diag}(1,a),\quad
L=(X+tY)D_a^{-1}\in\mathrm{SL}_2(\mathbb F_5),\quad Z=L^{-1}Y,
\]
\[
\xi=aZ_{11}-b,\qquad \lambda=aZ_{12},\qquad \mu=Z_{21}.
\]

Pak přesně

\[
\xi^2+\lambda\mu=\kappa.
\]

Inverze je explicitní:

\[
Z=\begin{pmatrix}(\xi+b)/a&\lambda/a\\ \mu&b-\xi\end{pmatrix},
\qquad Y=LZ,\qquad X=LD_a-tY.
\]

Všechna dělení jsou nenulovými prvky `F5`; jejich inverze jsou třetí mocniny. Dvě původní souřadnice `r` zůstávají samostatnými nezměněnými údaji.

## 2. Kuželosečka jako jeden původní pětičetný údaj a nejvýše šest pozic

Definujme `n∈F5` a index `j`:

- Při `λ≠0`: `j=λ−1∈{0,1,2,3}`, `n=ξ`.
- Při `λ=0`: `n=μ`. Kořen `ξ=0` nebo kořen v `{1,2}` dostane `j=4`; kořen v `{3,4}` dostane `j=5`.

Počet přípustných indexů je

\[
m(\kappa)=\begin{cases}
5,&\kappa=0,\\6,&\kappa\in\{1,4\},\\4,&\kappa\in\{2,3\}.
\end{cases}
\]

Inverze pořadníku nepotřebuje vyhledávání:

- Pro `j<4`: `λ=j+1`, `ξ=n`, `μ=(κ−n²)/λ`.
- Pro `j≥4`: `λ=0`, `μ=n`; použije se příslušný kořen `κ`, tedy `0`, dvojice `1,4` nebo dvojice `2,3`.

Při nenulovém Gramu jsme tedy pouze přepsali stávající data bijekcí

\[
(X,Y,r_x,r_y)\longleftrightarrow
(g,L,n,j,r_x,r_y).
\]

Pro každý přípustný `(g,j)` je přesně `120·5·25=15000` různých trojic `(L,n,(r_x,r_y))`. Tyto údaje navržený krok ponechá. Nejde o přidané stavy ani pomocné registry; původní písty z nich obnoví uvedená inverze.

## 3. Přenos jednoho obsazeného bitu

Pevný veřejný cíl je

\[
Mg=(3\beta,\ 4(\alpha+\beta+\gamma),\ 3(\beta+\gamma)).
\]

Pro nenulové `g` má jeho cílová orbita maximální počet pozic

\[
m_*(g)=\begin{cases}
5,&g=s(2,1,3),\ s\ne0,\\6,&\text{jinak}.
\end{cases}
\]

První případ je právě `Mg=−g`; tento údaj nahrazuje jakékoli procházení orbity za běhu. Vychází z pevného orbitového rozkladu cíle, nikoli z nového výběru čtení.

Z již existujícího indexu a bitu vypočteme celé číslo

\[
\ell=j+m(\kappa)\eta.
\]

Jestliže `ℓ≥m*(g)`, ponecháme úplný faktorový stav beze změny. Jinak nastavíme

\[
g'=Mg,\quad m'=m(\kappa(g')),\quad
\eta'=\mathbf1_{\ell\ge m'},\quad j'=\ell-m'\eta',
\]

a obnovíme písty ze `(g',L,n,j')`. Údaje `L,n,r_x,r_y` se nemění. Inverzní krok používá `M⁻¹` a stejnou zachovanou hodnotu `ℓ`:

\[
M^{-1}(a,b,c)=(4b-2c,\ 2a,\ 2c-2a).
\]

Tím je na všech stavech určena jedna matematická permutace. Nulový Gram je identita pro oba vstupní bity.

## 4. Přesný dosah a velikost redukce

Redukovaný nenulový nosič `(g,j,η)` má **1280 stavů**, z nich 640 připravených. Dosažitelná část má 740 stavů; je přesně `ℓ<m*(g)`. Každý její cyklus navštíví vlákno s maximálním `m=m*`, kde jsou všechny jeho indexy v bitu 0. Proto dosažitelnost není pouhým horním odhadem.

Cyklový rozklad této 1280prvkové permutace má 540 pevných bodů, deset cyklů délky 2 a 72 cyklů délky 10. Na plném faktoru `F5^10×{0,1}` je dosažitelných

\[
165625+740\cdot15000=11265625
\]

stavů, včetně 1500000 stavů s obsazeným bitem. Nulový Gram přispívá pouze připravenou vrstvou. Na celé této množině platí `G Π_alg=M G`, a proto také požadovaná rovnost pro `D_C` a `L5`. Kompozice s dalším totožným krokem bit neresetuje.

Tato redukce **není faktorem celé povolené abecedy**. Původní generátory například přenášejí `r` do pístů a mění údaje, které zde konkrétní permutace ponechá. Nejmenší faktor celé abecedy má stále `2·5^10` stavů. Číslo 1280 proto nelze dosadit za jeho velikost do předchozího univerzálního kompilátoru.


### Přímé odvození orbitových šířek a počtů

Pro samostatnost tvrzení o m_* není potřeba externí tabulka orbit. V bázi
\[
e=(2,1,3),\quad v=(2,0,2),\quad w=(2,0,3)
\]
pišme g=Ae+Bv+Cw. Pro N=M+I platí Ne=0, Nv=e, Nw=v. Proto N^3=0,
\[
M^k g=(-1)^k\bigl((A-kB+\tbinom{k}{2}C)e+(B-kC)v+Cw\bigr).
\]
Přímé dosazení do kappa=beta^2-alpha gamma dává
\[
\kappa(g)=B^2+3AC-C^2,\qquad
\kappa(M^k g)=\kappa(g)+kC^2.
\]
Je-li C≠0, k=0,...,4 projde všechny hodnoty kappa a maximální šířka je 6. Je-li C=0 a B≠0, je kappa=B^2 nenulový čtverec a šířka je stále 6. Zbývající nenulové g=Ae mají kappa=0, Mg=-g a šířku 5. Tím je uvedená podmínka pro m_* dokázána přímo.

Z téže nilpotentní formule plyne M^10=I. Platí M^5=-I a ani M, ani M^5 nemá nenulový pevný bod; body délky 2 jsou přesně nenulové násobky e, protože M^2-I=N(N-2I) a N-2I je invertibilní. Ostatních 120 nenulových Gramů má délku 10. Tedy aktivní redukovaný nosič má 4·5+120·6=740 stavů, deset dvoucyklů a 72 deseticyklů.

Nulových pístových dvojic je 6625: při X=0 je 145 singularních Y; při každém ze 144 nenulových rank-1 X dovolí převod X na diag(1,0) invertibilními levými/pravými změnami 45 možností Y, neboť Y22=0, Y12·Y21=0 a Y11 je libovolné. Nulové rovnosti determinantů i polarizace se při tomto převodu pouze násobí nenulovým determinantovým faktorem. Celkem 145+144·45=6625. Nenulový atlas má 120·5=600 pístových označení na každý (g,j), takže (5^8-6625)/600=640 připravených redukovaných stavů, celkem 1280 s bitem. Zbývajících 1280-740=540 redukovaných stavů je fixovaných. Dosažitelných pístových/bitových stavů je 6625+740·600=450625. Násobení volnými r,q dává uvedené plné počty.
### Parita, nativní realizace a přesné q chování

Každý redukovaný cyklus na (g,j,eta), g≠0, se opakuje pro každé z 15000 označení (L,n,r_x,r_y). Proto je Pi_alg sudá i bez použití parity malé 1280prvkové permutace. Nulové vlákno je identita. Přílohy A/B tedy lze aplikovat na právě tento explicitní cíl. Úplné T_alg je definováno výše, nikoli jako libovolný lift nebo jako nativní list „Pi_alg“.

Pro libovolný nativní list w platí trojúhelníková mapa
\[
w(f,q)=(F_w(f),H_w(f)q+t_w(f)).
\]
Úplné listové H,t jsou dány uvedenou q tabulkou. Pro součin UV (V působí první) platí přesně
\[
H_{UV}(f)=H_U(F_Vf)H_V(f),\qquad
t_{UV}(f)=H_U(F_Vf)t_V(f)+t_U(F_Vf).
\]
Pro inverzi, s f=F_w^{-1}(f'), platí
\[
H_{w^{-1}}(f')=H_w(f)^{-1},\qquad
t_{w^{-1}}(f')=-H_w(f)^{-1}t_w(f).
\]
Tato konečná rekurence spolu s CW-ALG-1 určuje q účinek pro každé vstupní f,q, bez dalšího výběru. Homogenní makra mají t=0, stejně jako P,Q_cs,W_a,W_b; tedy na hranici celého T_alg
\[
T_{\rm alg}(f,q)=(\Pi_{\rm alg}f,H_{T_{\rm alg}}(f)q),\qquad H_{T_{\rm alg}}(f)\in GL_2(\mathbb F_5).
\]
Netvrdíme H=I ani q=0. Nulová translace na hranici neznamená nulové q v nativních mezikrocích. Homogenizace je vlastnost slov, nikoli příprava neznámého q.

Úplná inverze je ReverseInvert(Expand(CW-ALG-1(Pi_alg))). Souřadnicově se nejprve určí f=Pi_alg^-1(f') a poté q=H_T(f)^-1 q'. Samostatná kompilace Pi_alg^-1 se nesmí bez dalšího důkazu zaměnit s touto úplnou inverzí. Rovněž faktorová perioda 10 sama netvrdí T_alg^10=I na X.

### Dosažitelná množina a příprava

Přesně
\[
\Omega_{\rm alg}=\rho^{-1}\bigl(\{G=0,\eta=0\}\cup
\{G\ne0,\ j+m(\kappa(G))\eta<m_*(G)\}\bigr).
\]
Je to dosažitelný uzávěr T_alg z celé vrstvy eta=0 s libovolnými písty,r,q. Každý aktivní cyklus navštíví maximální šířku, kde tentýž slot má bit0; každé q vlákno je bijektivně přenášeno a je celé zahrnuto ve vstupu. Velikost je 281640625. Na této množině G T_alg=M G a proto D_C T_alg=L5 D_C, pro všechna q a obsazené bity, bez resetu. Mimo ni je fixována faktorová permutace, nikoli automaticky úplná q mapa.

Pro menší přípravu S0={r_x=r_y=eta=0}, |S0|=5^10, je dosažitelný uzávěr samotného T_alg přesně Omega_alg∩{r_x=r_y=0}, velikosti 11265625. Zachování r se vztahuje ke konci T_alg; během nativního slova může být libovolné obsazené r použito a poté přesně vráceno. Tento závěr o T_alg neurčuje dosažitelný uzávěr budoucího složení s readery U_iK_iU_i.

## Úplná převzatá slovní gramatika s prioritami CW-ALG-1

Následující A/B definice jsou normativní součástí této kandidátní verze společně s prioritami výše. Číslování je zachováno kvůli přezkumu proti původnímu zdroji. Výskyty „(10)“ v popisném starším textu označují zdejší definici T_alg a „(12)“ její zdejší ReverseInvert; žádná stará lexikografická Pi se nepřebírá.
## Příloha A. Úplná slovní gramatika základního třícyklu

V této příloze každé pomocné písmeno znamená přesně uvedené slovo. Není dovoleno nahradit je nezkompilovanou bránou. Souřadnicové tvrzení makra se vždy týká faktoru; všechna makra zachovávají také nulové \(q\) podle (11). Inverze a součiny se rozepisují syntakticky. Všechny souřadnicové vektory jsou ve Walshově pořadí \((s,v,u,t,r)\) každé buňky.

### A.1 Všech deset jednotkových translací

Pro \(g=\bar c,\bar d\) položme
\[
D_g=g_xg_y,\qquad Y_g=D_gP^{-1}D_gP.
\]
V dalších vzorcích zkracujeme \(Y_c:=Y_{\bar c}\), \(Y_d:=Y_{\bar d}\). Pro afinní involuci \(g(z)=Lz+t_g\) je toto přesně translace druhé buňky o \(t_g\). V našem pořadí
\[
t_c=(1,0,2,0,0),\qquad t_d=(0,1,0,2,1).
\]
Definujme
\[
Y_{ac}=a_yY_ca_y,\quad Y_{ad}=a_yY_da_y,\quad Y_{bd}=b_yY_db_y,
\]
\[
\begin{aligned}
Y_s&=Y_c^3Y_{ac}^3,&Y_u&=Y_c^4Y_{ac},\\
Y_t&=Y_{ad}Y_d^{-1},&Y_r&=Y_{bd}^2Y_d^{-2},\\
Y_v&=Y_dY_t^{-2}Y_r^{-1}.
\end{aligned}
\tag{A1}
\]
To jsou jednotkové translace uvedených souřadnic druhé buňky. Například \(t_c+L_at_c=(2,0,0,0,0)\) a \(L_bt_d-t_d=(0,0,0,0,3)\), což ověřuje příslušné koeficienty. Jednotkové translace první buňky jsou
\[
X_j=Q_{\rm cs}Y_jQ_{\rm cs}^{-1}Y_j^{-1},\qquad j=s,v,u,t,r.
\tag{A2}
\]
Pro libovolný konkrétní vektor \(v\in D\) značí \(\tau_v\) součin těchto deseti slov s exponenty rovnými souřadnicím \(v\) v reprezentantech \(0,\ldots,4\), v pevném pořadí \((s_x,v_x,u_x,t_x,r_x,s_y,v_y,u_y,t_y,r_y)\). Tím je slovo \(\tau_v\) jednoznačně určeno.

### A.2 Zápis indikátoru nulového smíšeného čtení

Položme
\[
E_a=W_a\mathsf A W_a,\quad E_b=W_b\mathsf B W_b,\quad K_0=E_aE_b.
\]
Na \(h\ne0\) obě \(E_i\) pouze přepnou bit a data ponechají. Na \(h=0\) jsou \(\mathsf A\), respektive \(\mathsf B\), a bit ponechají. Proto
\[
K_0(z,\eta)=\begin{cases}(\mathsf A\mathsf Bz,\eta),&h=0,\\(z,\eta),&h\ne0.
\end{cases}
\tag{A3}
\]
Translace \(r_x\) nebo \(r_y\) nemění \(h\), zatímco \(\mathsf A\mathsf B\) obě \(r\) neguje. Pro \(r=r_x,r_y\) tedy
\[
Z_r=[K_0,\tau_{e_r}]^2
\tag{A4}
\]
působí přesně
\[
r\longmapsto r+1-h^4,
\]
a všechny ostatní faktorové souřadnice včetně bitu vrátí. Na nulové větvi samotný komutátor posune o \(-2\), jeho druhá mocnina o \(-4=1\). Na nenulové větvi je identitou. Toto je první nelineární datová operace získaná z obou zmrazených zapisovačů.

### A.3 Slova pro mocniny libovolné pístové souřadnice

Píšeme \(E_r(f)\) pro slovo, jehož již dokázané působení je přičtení \(f\) do \(r\); následující vzorce toto slovo skutečně definují. Pro slovo \(U=E_r(f)\) a pístový posun \(v\) definujme slovní operátor
\[
\mathcal D_v(U)=\tau_{-v}U\tau_vU^{-1}.
\tag{A5}
\]
Jeho působení je \(E_r(f(z+v)-f(z))\). \(\mathcal D_v^k\) značí \(k\) vnořených použití (A5).

Nechť \(\chi\) je kterákoli z osmi Walshových pístových souřadnic. Pokud je v první buňce a \(\chi(p_x)=\ell^Tp_x\), zvolme **jednoznačně** posun v druhém pístu \(v_\chi=K^{-1}\ell\), s ostatními položkami nulovými; pokud je v druhé buňce, prohoďme buňky. Vektor se do (A1)–(A2) převede danou Walshovou maticí. Pak
\[
h(z+v_\chi)=h(z)+\chi(z).
\]
Čtyři konečné diference dávají \(-4!\chi^4=\chi^4\) v \(\mathbb F_5\). Proto pevné slovo
\[
U_{r,\chi,4}=\mathcal D_{v_\chi}^4(Z_r)
\tag{A6}
\]
je \(E_r(\chi^4)\).

Nechť \(e_\chi\) je jednotkový posun souřadnice \(\chi\) ve Walshově bázi. Položme \(D=\mathcal D_{e_\chi}\), \(U_0=\tau_{e_r}\), \(U_4=U_{r,\chi,4}\) a dále
\[
\begin{aligned}
U_1&=(D^3(U_4)U_0^{-1})^4,\\
U_2&=(D^2(U_4)U_1^{-4}U_0^{-4})^3,\\
U_3&=(D(U_4)U_2^{-1}U_1^{-4}U_0^{-1})^4.
\end{aligned}
\tag{A7}
\]
Pak \(U_k=E_r(\chi^k)\) pro \(k=0,\ldots,4\). Ověření jsou identity
\[
\Delta^3\chi^4=4\chi+1,\quad
\Delta^2\chi^4=2\chi^2+4\chi+4,\quad
\Delta\chi^4=4\chi^3+\chi^2+4\chi+1.
\]
Tím jsou daná slova pro oba cíle \(r_x,r_y\), nikoli jen existence potřebných posunů.

### A.4 Tři původní pracovní souřadnice

Pro zbytek přílohy označme
\[
\xi_1=r_x,\qquad \xi_2=v_x,\qquad \xi_3=r_y.
\]
Sedm zbývajících pístových souřadnic je
\[
L=(s_x,s_y,u_x,u_y,v_y,t_x,t_y).
\]
Z nativních slov definujme
\[
H_0=\tau_{-e_{s_x}-2e_{u_x}}\bar c_xb_x,\quad
N_{21}=H_0a_xH_0a_x.
\tag{A8}
\]
První slovo přičítá \(-2r_x\) do \(v_x\) a \(2r_x\) do \(t_x\); druhé je přesně \(E_2(\xi_1)\). Dále
\[
N_{23}=(Q_{\rm cs}N_{21}Q_{\rm cs}^{-1}N_{21}^{-1})^{-1}=E_2(\xi_3).
\tag{A9}
\]
Z (A7) máme \(E_1(\xi_2)\), \(E_3(\xi_2)\) a jejich mocniny. Definujme
\[
J_{12}=N_{21}E_1(\xi_2)^{-1}N_{21},
\]
\[
J_{23}=E_3(\xi_2)N_{23}^{-1}E_3(\xi_2).
\tag{A10}
\]
První působí \((\xi_1,\xi_2)\mapsto(-\xi_2,\xi_1)\), druhé \((\xi_2,\xi_3)\mapsto(-\xi_3,\xi_2)\); ostatní faktorové souřadnice fixují.

Následující malý konečný pořadník odstraňuje jakoukoli neurčenou volbu slova pro záměnu pracovních souřadnic. Seřaďme slova délky nejvýše 23 v abecedě
\[
(J_{12},J_{12}^{-1},J_{23},J_{23}^{-1})
\]
podle délky a lexikograficky. Pro uspořádané různé \(i,j\in\{1,2,3\}\) vezměme první slovo \(R_{ij}\), jehož podepsaná permutační matice posílá \(e_1\mapsto\epsilon_i e_i\), \(e_2\mapsto\epsilon_j e_j\). Mez 23 postačuje: tyto dvě čtvrtotáčky generují všech 24 podepsaných permutací determinantu 1 ve třech souřadnicích, tedy každého vrcholu jejich Cayleyova grafu dosáhne jednoduchá cesta délky nejvýše 23. Generování je elementární: jejich čtverce mění znaménka dvojic os a jejich permutační obrazy generují všechny permutace tří os.

Pro \(k=1,\ldots,4\) definujme
\[
E_i(\xi_j^k)=
\left(R_{ij}E_1(\xi_2^k)R_{ij}^{-1}\right)^{\epsilon_i\epsilon_j^k},
\tag{A11}
\]
kde exponent \(-1\) lze ponechat jako inverzi. Koeficient je vlastní inverzí, takže výsledek má jednotkový koeficient. Zde \(E_1(\xi_2^k)\) je již pevně (A6)–(A7).

Pro vnější souřadnici \(\chi\) z \(L\) definují (A6)–(A7) \(E_1(\chi^k),E_3(\chi^k)\). Položme
\[
E_2(\chi^k)=J_{12}E_1(\chi^k)J_{12}^{-1}.
\tag{A12}
\]
Konstantní \(E_i(1)\) jsou jednotkové translace (A1)–(A2). Dostali jsme konkrétní slova pro všechny atomy, které budou potřeba.

### A.5 Přesné násobení kontrolních polynomů

Pro různé pracovní souřadnice \(i,j\) a polynomy \(f,g\) nezávislé na obou \(\xi_i,\xi_j\) použijeme
\[
Q_{ij}=E_j(\xi_i^2),
\]
\[
K_j(g)=[E_i(g),Q_{ij}],\qquad
R_j(g)=K_j(g)K_j(-g)^{-1}.
\tag{A13}
\]
Přímo na libovolných vstupních hodnotách:
\[
K_j(g)=E_j(-2\xi_i g+g^2),\qquad
R_j(g)=E_j(-4\xi_i g)=E_j(\xi_i g).
\]
Proto
\[
\boxed{E_j(fg)=[E_i(f),R_j(g)]^{-1}.}
\tag{A14}
\]
Pomocná souřadnice \(\xi_i\) se vrátí do své původní hodnoty, jakákoli byla. Rovnice nepředpokládá nulový pomocný vstup ani známou hodnotu bitu. Součty se realizují součinem slov, znaménko inverzí a skalár mocninou.

Pro úplnou syntaxi potřebujeme jen indikátory
\[
\delta_{\chi,c}=1-(\chi-c)^4.
\]
Jejich slovo do cíle \(i\) je
\[
E_i(\delta_{\chi,c})=
E_i(1)\left(\tau_{ce_\chi}E_i(\chi^4)\tau_{-ce_\chi}\right)^{-1}.
\tag{A15}
\]
Vždy \(\chi\ne\xi_i\); potřebné atomy jsou (A11)–(A12).

Definice pro součin se čte **rekurzivně podle jeho počtu faktorů**: jediný faktor použije (A15); součin prvních \(k-1\) faktorů označme \(f\), poslední \(g\), a použijme (A14), případně s prohozením \(i,j\), podle požadovaného cíle. Obě rekurzivní volání mají méně faktorů. Znaménko minus v \(E_i(-g)\) je prostě inverze již určeného slova. Pomocná souřadnice je vždy předem uvedena níže a všechny kontrolní proměnné jsou mimo dvojici cíl/pomocná souřadnice. Tím je rekurze konečná a jednoznačná.

### A.6 Jeden třícyklus, úplně rozepsaný do předchozích maker

Položme
\[
L^0=(1,0,1,0,0,0,1),\qquad
\delta_L=\prod_{k=1}^7\delta_{L_k,L_k^0},
\]
v pořadí souřadnic \(L\) z A.4. Definujme tato tři slova pomocí A.5, s posledním faktorem uvedeným za \(\delta_L\):
\[
\begin{aligned}
F&=E_1(\delta_L\delta_{\xi_3,0}),&&\text{pomocná souřadnice }\xi_2,\\
G_0&=E_3(\delta_L\delta_{\xi_1,0}),&&\text{pomocná souřadnice }\xi_2,\\
H&=E_1(\delta_L\delta_{\xi_2,0}),&&\text{pomocná souřadnice }\xi_3.
\end{aligned}
\tag{A16}
\]
Označme v rovině \((\xi_1,\xi_3)\) body \(O=(0,0)\), \(E=(1,0)\), \(N_0=(0,1)\). Na vrstvě \(L=L^0\) je \(F\) posun \(\xi_1\) právě při \(\xi_3=0\), \(G_0\) posun \(\xi_3\) právě při \(\xi_1=0\). Jejich komutátor je
\[
K_1=[F,G_0]=(O,E,N_0)
\]
pro každé \(\xi_2\), na obou bitech. Mimo tuto vrstvu je identita. Dále
\[
\Psi=[K_1,H]=(O,E,E+N_0,2E,N_0)
\tag{A17}
\]
právě při \(L=L^0,\xi_2=0\), opět na obou bitech; všechny ostatní stavy fixuje. Tyto malé cykly dostaneme dosazením do čtyř faktorů komutátoru: jde o symbolický výpočet na jejich přesně určených podporách.

Na tomto pístu jsou \(p_x=(3,0,3,0)\), \(p_y=(4,1,1,4)\), \(h=2\). Označme
\[
\tau=\tau_{2e_{r_x}},\qquad
\Psi'=W_a\tau\Psi\tau^{-1}W_a,
\qquad
\boxed{C_*=[\Psi,\Psi'].}
\tag{A18}
\]
Zde končí úplná základní slovní gramatika.

Pro kontrolu podpory: \(\tau\Psi\tau^{-1}\) má v rovině \(r\) podporu
\[
\{2E,3E,3E+N_0,4E,2E+N_0\}
\]
na obou bitech. Na tomto pístu \(W_a\) ponechá bit-0 vrstvu; bit-1 vrstvu přenese na jiný píst \(\mathsf A p\) a bit 0. Písty jsou různé, protože \(u_x=1\). Podpory \(\Psi\) a \(\Psi'\) se tedy protínají v **jediném úplném faktorovém stavu**: původní píst, \(r=2E\), bit 0.

Jestliže dvě permutace mají právě jeden společný bod podpory \(z\), jejich komutátor je třícyklus \((z,Fz,Gz)\). Zde \(\Psi(2E)=N_0\), \(\Psi'(2E)=3E\). Dostáváme přesně (4), nikoli třícyklus duplikovaný na obou bitech. Výpočet také dokazuje, že po makru nezůstává žádný pracovní příznak nebo nevrácená pomocná hodnota.

## Příloha B. Pevný univerzální slovní kompilátor

Tato příloha definuje konečnou gramatiku \(\operatorname{CW}\) použitou v definici T_alg této specifikace. Všechny její seznamy a výběry jsou **konstanty konstrukce slova**, nikoli podmínky vyhodnocované na vstupních datech při použití \(T\).

### B.1 Pevná pořadí a pevný seznam hran

Stavy \(\mathcal F\) mají přesné lexikografické pořadí \((p_{x,1},p_{x,2},p_{x,3},p_{x,4},r_x,p_{y,1},p_{y,2},p_{y,3},p_{y,4},r_y,\eta)\), s \(0<1<2<3<4\) pro datové souřadnice a \(0<1\) pro poslední bit. Všechny abecední pořadníky jsou pořadníky syntaktických řetězců; součin řetězce \(g_1\cdots g_k\) působí jako \(g_1\circ\cdots\circ g_k\).

Použijme přesně uspořádanou šestnáctipísmennou **makroabecedu**
\[
(\bar a_x,\bar b_x,\bar c_x,\bar d_x,\bar e_x,
\bar a_y,\bar b_y,\bar c_y,\bar d_y,\bar e_y,
P,P^{-1},Q_{\rm cs},Q_{\rm cs}^{-1},W_a,W_b).
\tag{B1}
\]
Její makra jsou (11). Shoda některých faktorových permutací není důvodem odstraňovat syntaktické duplicity. Abeceda obsahuje inverzi každé své faktorové permutace a její faktorová grupa je tatáž \(\Gamma\).

Seznam \(\mathcal E\) obsahuje všechny řetězce délky \(0,1,\ldots,N\) v pořadí délka–lex. Každému \(w\) přiřadíme **slovo**
\[
E_w=wC_*w^{-1}
\]
a jeho orientovanou trojici
\[
(w\zeta_0,w\zeta_1,w\zeta_2).
\tag{B2}
\]
To je konečný seznam délky \(\sum_{k=0}^N16^k\), výslovně vymezený před použitím cílové permutace. Jeho souvislost byla dokázána v 5.3. Nevyžaduje testování rovnice s \(L_5\).

### B.2 Hvězdicové třícykly a jejich skládání

Pevné kotvy jsou \(a=\zeta_0,b=\zeta_1\). Začneme
\[
U=\{\zeta_0,\zeta_1,\zeta_2\},\qquad S_{\zeta_2}=C_*.
\]
Udržujeme slova
\[
S_x=(a,b,x)\qquad(x\in U\setminus\{a,b\}),
\]
která mimo \(U\) fixují všechny stavy.

Pro různé \(i,j\ne b\) definujme slovo
\[
K(a,j)=S_j^{-1},\quad K(i,a)=S_i,\quad
K(i,j)=S_jS_i^{-1}S_j^{-1}\quad(i,j\notin\{a,b\}).
\tag{B3}
\]
Je to \((b,i,j)\). Pro tři různé body z \(U\) definujme
\[
\mathcal C_U(i,j,k)=K(i,j)K(j,k)\quad(b\notin\{i,j,k\}).
\tag{B4}
\]
Pokud trojice obsahuje \(b\), cyklicky ji otočme do tvaru \((b,i,j)\) a použijme \(K(i,j)\). V obou případech je výsledné slovo přesně \((i,j,k)\).

**Kanonický rozklad libovolné sudé permutace \(g\) množiny \(U\).** Každý její netriviální cyklus napišme s nejmenším bodem na začátku, cykly seřaďme podle těchto počátků. Cyklus \((c_1,\ldots,c_m)\) nahraďme seznamem transpozic
\[
(c_1c_m)(c_1c_{m-1})\cdots(c_1c_2).
\]
Seznamy zřetězme v uvedeném pořadí. Jejich celková délka je sudá. Každou sousední dvojici převeďme na slovo takto:

- Stejné transpozice dávají prázdné slovo.
- Mají-li právě jeden společný bod, přepišme je jednoznačně jako \((p\ s)(s\ q)\) a použijme \(\mathcal C_U(p,s,q)\).
- Jsou-li disjunktní, seřaďme body uvnitř každé transpozice, zachovejme pořadí obou transpozic a použijme
  \[
  (a'\ b')(c'\ d')=
  \mathcal C_U(a',c',b')\mathcal C_U(a',c',d').
  \]

Výsledný součin v původním pořadí označme \(\operatorname{Even}_U(g)\). Nevolá žádný vyhledávač slov; jde o uvedené pevné cyklové identity.

### B.3 Připojení jednoho nebo dvou nových bodů

**Rutina Attach2.** Máme známé slovo \(E=(p,q,x)\), kde \(p,q\in U\), \(x\notin U\); trojici cyklicky otočíme tak, aby nový bod byl poslední. Definujme permutaci \(g_0\) množiny \(U\) pomocí \(p\mapsto a,q\mapsto b\); ostatní prvky definičního oboru seřaďme a přiřaďme vzestupně ostatním obrazům.

- Je-li \(g_0\) sudá, položme \(g=g_0\).
- Je-li lichá a \(|U|\ge4\), postkomponujme ji transpozicí dvou nejmenších bodů \(U\setminus\{a,b\}\). Výsledek \(g\) je sudý a předepsané dva obrazy zachová.
- Je-li lichá a \(|U|=3\), nahraďme \(E\) jeho inverzí, prohoďme \(p,q\) a znovu stejným pravidlem sestavme \(g_0\). Ten je nyní sudý; položme \(g=g_0\).

Použijme dosavadní hvězdy a definujme
\[
S_x=\operatorname{Even}_U(g)\,E\,\operatorname{Even}_U(g)^{-1}.
\tag{B5}
\]
Je to \((a,b,x)\). Připojme \(x\) do \(U\), staré hvězdy zachovejme.

**Hrana s jediným starým bodem.** Má-li vybraná orientovaná hrana tvar \(E=(p,x,y)\), \(p\in U\), \(x,y\notin U\), vezměme za \(q,r\) dva nejmenší body \(U\setminus\{p\}\). Pak
\[
[\mathcal C_U(p,q,r),E]=(p,q,x).
\tag{B6}
\]
Tuto odvozenou hranu použijme v Attach2 pro \(x\). Potom použijme původní hranu \(E=(p,x,y)\) v Attach2 pro \(y\). Všechny podpory a orientace ve vzorci jsou určené, bez volby dalšího svědka.

### B.4 Konečný počet kroků, definice CW a inverze

Proveďme přesně \(N-3\) následujících **konstrukčních** kroků. Pokud \(U=\mathcal F\), krok nic nezmění. Jinak vezměme první položku pevného seznamu \(\mathcal E\), jejíž podpora potkává \(U\) i doplněk. Souvislost dokazuje její existenci. Podle velikosti průniku 2 nebo 1 použijme B.3. Při každém netriviálním kroku přibude alespoň jeden bod, takže po stanoveném počtu kroků je \(U=\mathcal F\).

Tím dostaneme **jednoznačně určenou rodinu slov** \(S_x\) pro všechny body kromě dvou pevných kotev. Nakonec definujme
\[
\boxed{\operatorname{CW}(g)=\operatorname{Even}_{\mathcal F}(g).}
\tag{B7}
\]
V definici T_alg této specifikace dosadíme právě explicitní \(g=\Pi_{\rm alg}\) z algebraického atlasu. Každá uvedená rekurze končí: A.5 snižuje počet polynomových faktorů; B.4 má pevný počet \(N-3\) kroků; seznamy v A.4 a B.1 mají explicitní konečné meze. Při expanzi se nepřidávají žádné nové listové operace. To dokazuje, že definice T_alg určuje jeden konečný syntaktický řetězec, nikoli množinu možných řešení.

Všechny inverze v této příloze jsou syntaktické reverze již určených slov. Proto se stejně konečně a jednoznačně rozepíše inverze ReverseInvert(T_alg). Budování pořadníků, hvězd a cyklového rozkladu se **neprovádí uvnitř stavu TWIST-J**. Tyto konečné matematické definice určují pevné zapojení; žádný jejich pracovní seznam, index, podprostor nebo cílová matice není přidán do nosiče.


## Důkazní závislosti a stav přezkumu

Kandidátní závěr závisí na úplných zdrojových mapách, primitivě, nativním izolovaném třícyklu A1–A18, konečném hypergrafovém kompilátoru B1–B7, bijektivitě atlasu a kapacitě slotů. V tomto souboru jsou všechny tyto matematické argumenty uvedeny; rozhodnutí nezávislého přezkumu je dosud otevřené. Upřesnění precedence je nová fixace syntaktické verze, a proto se na její celý q lift nepřenáší dřívější numerický výsledek jiné zkratky či kompilátoru.

`PREREG-DRAFT.md` specifikuje plán omezených kontrol, jejich limity a požadovanou architekturní evidenci. Žádná kontrola z tohoto nového návrhu nebyla spuštěna. Původní lokální audity atlasu, lex Pi nebo Z20 nejsou veřejným replayem CW-ALG-1, celého T_alg ani následného V. Úspěch omezených kontrol nemůže sám potvrdit obrovské nativní slovo; jeho realizaci nese uvedený konstrukční důkaz.

Veřejné začlenění této sondy a následné v100 vyžaduje samostatné přezkumy, přijaté piny a splnění aktuálního postupu repozitáře. Tento dokument nemění Canon, registr, frontier ani status dřívějších kandidátů.

[status]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/STATUS.md
[policy]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/POLICY.md
[agents]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/AGENTS.md
[ci]: https://github.com/mathorn1973/twist-j/actions/runs/37343760427
[tag-ci]: https://github.com/mathorn1973/twist-j/actions/runs/37343817392
[release-ci]: https://github.com/mathorn1973/twist-j/actions/runs/37347576212
[release]: https://github.com/mathorn1973/twist-j/releases/tag/canon-v99
[issue]: https://github.com/mathorn1973/twist-j/issues/1384
[piston]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md#L2920-L2966
[translations]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md#L10500-L10534
[capacity]: https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/canon/CANON.md#L9142-L9380
