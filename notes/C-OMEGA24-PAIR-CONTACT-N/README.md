# Placený zápis na Omega24: uzavřenost domény a hranice realizace

**PUBLIC-content, NON-CANONICAL. 3. října 2026.** Algebraické důsledky:
**candidate-T**. Žádný nový výpočetní doklad. Veřejnou autoritu určuje
[STATUS.md](../../STATUS.md), nyní Public Canon v97. Tato poznámka nemění
Canon, registr ani status otevřeného přístrojového závazku.

Na níže deklarované energetické doméně je každý jednobuňkový placený zápis
přípustný. Výstup zůstává na stejné doméně, takže při dalších kontaktech
není potřeba znovu předpokládat dostatečné nabití. Tento důsledek neodvozuje
přípravu přístroje ani nativní nosič a jeho vazby z U. Navazující
[nativní kontrakt](NATIVE-CONTRACT.md) přesně vymezuje zbývající otázku.

## 1. Deklarovaný nosič

Pracujeme s klasickými diskrétními stavy. Nechť
$\ell:\mathbb F_5\to\{0,1,2,3,4\}$ je celočíselný reprezentant,
$d=(A_1,A_2,A_3,A_4,A_5,f)\in\mathbb F_5^6$ a

$$
\Omega_{24}=\left\{(d,b): b\in\mathbb Z,\ 0\le b\le24,\quad
b+\sum_{j=1}^{6}\ell(d_j)=24\right\}.
$$

Účet má jednotku $\Delta>0$, energii paměti
$\Delta\sum_j\ell(d_j)$ a energii baterie $\Delta b$.
Jde o definici srovnávacího modelu, nikoli o odvození fyzikální energie.
Každý obsah d má v této doméně jediný energetický doplněk
$b=24-\sum_j\ell(d_j)$. Libovolný obsah paměti proto neznamená libovolnou
nezávislou volbu b.

## 2. Uzavřenost vůči jednobuňkovým kontaktům

**Tvrzení (candidate-T).** Pro každý $(d,b)\in\Omega_{24}$, index
$i\in\{1,\ldots,6\}$ a každou cílovou hodnotu $y\in\mathbb F_5$ položme

$$
d_i'=y,\qquad d_j'=d_j\ (j\ne i),\qquad
b'=b+\ell(d_i)-\ell(y).
$$

Potom $(d',b')\in\Omega_{24}$. Každá konečná posloupnost těchto kontaktů
zachovává doménu bez další podmínky nabití před jednotlivými kontakty.

**Důkaz.** Pro právě zapisovanou buňku je

$$
s_i=b+\ell(d_i)=24-\sum_{j\ne i}\ell(d_j).
$$

Ostatních pět složek má celočíselný součet mezi 0 a 20. Proto
$4\le s_i\le24$. Jelikož $0\le\ell(y)\le4$, platí

$$
\boxed{0\le s_i-4\le b'=s_i-\ell(y)\le s_i\le24.}
$$

Ostatní složky se nemění, a tedy

$$
b'+\sum_j\ell(d_j')
=b+\ell(d_i)-\ell(y)+\ell(y)+\sum_{j\ne i}\ell(d_j)=24.
$$

Výstup patří do $\Omega_{24}$; tvrzení o posloupnosti plyne indukcí.
$\square$

Indukce se týká právě popsaných kontaktů. Jiné kroky programu musejí
zachování domény doložit zvlášť. Ponechají-li d,b beze změny, je tato
povinnost okamžitá. Výsledek nezávisí na nulovém počátečním obsahu d.

## 3. Přípustnost a vratnost jsou odlišné výroky

Při pevných ostatních souřadnicích tvoří energetické vlákno přesně pět stavů

$$
\{(a,s_i-\ell(a)):a\in\mathbb F_5\}.
$$

Při pevném nezměněném řízení je kontakt na tomto vlákně bijektivní právě
tehdy, když jeho mapa $a\mapsto g(a)$ permutuje $\mathbb F_5$.
Inverze pak použije $g^{-1}$ a odpovídající opačnou změnu b.
Pevné přepsání každého a na nulu je energeticky přípustné, ale všech pět
stavů vlákna spojí do jednoho. Uzavřenost domény tedy sama nedokazuje
vratnost ani dostupnost takového přepsání.

SUM zachovávající zdroj s pevným $x,\kappa\in\mathbb F_5$ používá
$g(a)=a+\kappa x$; jeho inverze odečte $\kappa x$.
FLAG používá $g(f)=f+1$ a inverze odečte jedničku. Oba energetické lifty
jsou permutace na své deklarované doméně. Tím není doloženo jejich
uskutečnění pouze párovými nativními interakcemi.

## 4. Podmíněný párový rozklad

Přijměme skutečně jeden lokální nosič

$$
\widetilde B=\{(b,c):0\le b\le24,\ c\in\mathbb F_5\},\qquad
E_{\widetilde B}(b,c)=\Delta b.
$$

Stejná energie má pět různých vnitřních stavů. Na párech
$X\!:\!\widetilde B$ a $A\!:\!\widetilde B$ přijměme mapy

$$
\begin{aligned}
W_\kappa^+:(x,(b,c))&\longmapsto(x,(b,c+\kappa x)),\\
V:(a,(b,c))&\longmapsto
   (a+c,(b+\ell(a)-\ell(a+c),c)),\\
W_\kappa^-:(x,(b,c))&\longmapsto(x,(b,c-\kappa x)).
\end{aligned}
$$

Hodnoty a,c se sčítají modulo 5; b je celé číslo. V má uvedený tvar
na hladinách $4\le\ell(a)+b\le24$. Chceme-li úplnou párovou permutaci
také na celém nezávislém součinu $A\times\widetilde B$, na zbývajících
hladinách ji doplníme identitou. Hladiny jsou invariantní; inverze na
úplných hladinách odečte c a obrátí energetický rozdíl.

Na $\Omega_{24}\times\mathbb F_5$ tato okrajová větev **není nikdy
potřeba**. Každá cílová buňka leží podle oddílu 2 na úplné hladině,
W± nemění b ani d a V zachovává $\Omega_{24}$. Platí to při každém
mezistavu a pro každé počáteční c.

Při neměnném x dává přímé složení na této doméně

$$
W_\kappa^-VW_\kappa^+(x,a,b,c)=
\bigl(x,a+c+\kappa x,b+\ell(a)-\ell(a+c+\kappa x),c\bigr).
$$

Proto pro **připravené c=0** dostáváme přesně energeticky rozšířený SUM.
Pro jiné c se pomocník také vrátí, ale paměť dostane navíc posun o c.
Energetická přípustnost na celé doméně podmínku c=0 nenahrazuje.
Vrací se pomocná složka c; energetická hladina b se obecně nevrací
a zůstává součástí úplného výstupu.

Zdroj se nemění, takže kladná konstrukce nevyžaduje ploché $E_X$.
Párovost však předpokládá, že $\widetilde B$ je skutečně jeden lokální
nosič a obě interakce jsou dostupné. Při elementárním rozdělení X,A,b,c
má V tři argumenty. Závorka kolem b,c sama fyzickou aritu nesnižuje.

## 5. Správná příprava archivu zůstává nutná

Uvažujme pevně zadaných šest logických přenosů

$$
q_1\to A_1,\quad w_1\to A_2,\quad s_1\to A_3,\quad
v_1\to A_3,\quad w_2\to A_4,\quad v_2\to A_5,
$$

kde $\psi_n=(u_n,v_n,w_n,s_n,q_n,r_n)$ označuje n-tý checkpoint
původního zdroje. Každý přenos přičítá $\kappa$ krát uvedený symbol
a mezi dvěma skupinami a po druhé skupině se jednou zvýší FLAG.
Za předpokladu správného čtení těchto checkpointů a c=0 při každém
datovém makrokontaktu platí algebraicky

$$
A_{\rm final}=A_0+\kappa A_*(\text{vstup}),\qquad
f_{\rm final}=f_0+2,
$$

$$
A_*(\text{vstup})=(q_1,w_1,s_1+v_1,w_2,v_2).
$$

Všechny součty v těchto rovnicích jsou modulo 5. Původní garance
$A_{\rm final}=A_*$ a $f_{\rm final}=2$ patří k přípravě
$A_0=0,f_0=0,\kappa=1$; společně s c=0 má tato příprava b=24.
Přípustnost na neprázdné paměti nedává stejný konečný archiv ani stejný
výstup původní čtečky. Samotné f=2 značí dokončení, nikoli rozlišení vstupů.

## 6. Časování a rozsah vratnosti

Mezi W+, V a W− musí být čtený x stále týž. Jestliže první krok četl
$x_{\rm start}$ a poslední odečítá $x_{\rm end}$, z c=0 zůstane

$$c_{\rm final}=\kappa(x_{\rm start}-x_{\rm end}).$$

Proto se mezi podkroky nesmí nepozorovaně vložit U. Pro vložení do
původního stroje musí kontaktní okno zachovat celé psi i n. Nový program,
hodiny a mapa checkpointů potřebují vlastní důkaz. Původní osmikrokový
kalendář ani formule $n=\lfloor m/8\rfloor$ se automaticky nepřenášejí.
Bijektivita W+ také neprokazuje dostupnost jediného zpětného pulzu:
$W^-=(W^+)^4$ je algebraická rovnost, ale její realizace čtyřmi aplikacemi
mění časový účet.

Vratnost těchto kontaktů není vratností celého vývoje. Pokud při
$\kappa=0$ dva různé úplné počátky splynou v totožný úplný stav včetně
pomocníků, programu a hodin, je příslušný celkový vývoj neprostý.
Případná rozlišující stopa se nesmí vynechat a shoda projekce vydávat
za shodu úplných stavů. Zde se nový test takové kolize neprovádí.

## 7. Evidence a otevřená hranice

Oddíly 2–5 jsou samostatné algebraické důkazy v deklarovaném modelu.
Nový vědecký běh, verifier, RUN ani EXPECTED tato poznámka neobsahuje.
Repozitářové kontroly nejsou výpočetním dokladem existence přístroje.

Vstupem byla uživatelem dodaná `NOTE_CZ.md` o párovém konzervativním
kontaktu a navazující místní zmrazený kontrakt. Při přípravě této poznámky
byly zkontrolovány jejich bajtové otisky:

- dodaná poznámka: `d15e01e87a488ca60d99329e31b3f4f98ff150b4e33d6cfc07dc5852dfb56b92`;
- místní kontrakt: `7a2cb9a05f3c7caeed7d9c02a45b12b84cf8b179336a5aef19e3a9a41f598614`.

Otisky identifikují podklady; nejsou důkazem jejich běhových tvrzení.
Původní balíky ani zmrazené bajty se touto veřejnou poznámkou nepřepisují.
Zdejší důkazy nevyžadují přístup k místním přílohám. Nativní kontrakt
vedle této poznámky je samostatná veřejná formulace otevřených podmínek.

Rozlišení matematické konstrukce a fyzikální realizace odpovídá
[CORE](../../canon/CORE.md) a otevřenému `QDD-INSTRUMENT-APPARATUS`
v [FRONTIER](../../canon/FRONTIER.md) a [registru](../../canon/REGISTRY.tsv).
Nativní původ nosiče, energie a vazeb zůstává otevřený. Uzavřenost
$\Omega_{24}$ odstranila energetický okraj této konstrukce; neodvodila
přípravu, interakce, řízení, fyzické hodiny ani existenci nativního přístroje.
