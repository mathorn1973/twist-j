# J-kontakt: čtení, konečná reference a uchovaná historie

**NON-CANONICAL · L1 · česká konsolidace z 3. října 2026.**
Veřejnou autoritou zůstává Public Canon v97. Zdejší nové důkazy mají nejvýše
pracovní označení **candidate-T**; tato poznámka nemění žádný veřejný status.
Koordinační objekt: [#1347](https://github.com/mathorn1973/twist-j/issues/1347).

Společný koherentní kontakt už není vhodné uvádět jako celý chybějící úkol.
V přijatém amplitudovém modelu lze spojit oba J porty, následné měření,
placené archivy, baterii i konečnou energetickou referenci. Nynější otázka
zní, jak se takový přístroj skládá do pokračující historie a které jeho
zdroje ještě zůstávají dodané.

Tato mapa spojuje původní čtení a kaskádu se dvěma navazujícími podklady
o přístroji. [Důkazy](PROOF.md) dávají samostatně přezkoumatelnou matematickou
realizaci včetně **dvou J kontaktů**. [Původ a síla evidence](EVIDENCE.md)
oddělují tyto argumenty od hlášených běhů nedodaných programů. Především
5 955 kontrol a 35 průchodů z posledního podkladu zde nejsou reprodukovanou
výpočetní evidencí.

## M01 — Co je nyní uzavřené a co je další hranice

| Oblast | Co máme v přesně vymezené matematice | Co tím není odvozeno |
|---|---|---|
| Kontakt | Úplné koherentní větve obou portů a následných kontextů. | Tento amplitudový nosič a jeho vazby z nativního U. |
| Paměť | Čerstvé placené archivy; první záznamy mohou zůstat při dalším kontaktu nedotčené. | Neomezená paměť, bezplatná obnova archivů ani nový nezávislý zdroj. |
| Energie | Přesné zachování zvoleného účtu pole, reference, baterie a obsazených archivů. | Fyzikální původ Hamiltoniánu a role generátoru času. |
| Přesnost | Pro trojúhelníkovou referenci chyba celého konečného programu nejvýše min(4, 24/(2N²+1)) ve čtverci vektorové normy. | Přesný sedminulový cíl při konečném N ani optimálnost profilu. |
| Příprava | Přesně popsaný cílový profil a jeho cena v rozměru a střední energii. | Příprava právě této reference z nezávisle popsaných zdrojů. |
| Výskyt | Koherentní historie a jejich kvadratické váhy. | Výběr jediné skutečné historie a odvození jejího výskytu z U/J. |

Poslední řádek se týká tohoto přístroje a odvození. Veřejný vybraný model
ETH-QDD-1 již přijímá zdroj, záznam a uspořádaný Bornův zákon prostřednictvím
`QDD-SELECTED-SOURCE`, `QDD-SELECTED-RECORD` a `QDD-SELECTED-BORN`.
Přijetí zákona a jeho nativní realizace jsou odlišné závazky; přesné současné
znění drží [FRONTIER](../../canon/FRONTIER.md).

## M02 — Čtení má zachovat budoucí působení

Pro zvolenou třídu operací a pozorování požadujeme

$$R(x)=R(y)\ \Longrightarrow\ O(wx)=O(wy).$$

Je to požadavek na konkrétní rozhraní, nikoli předpoklad jedinečnosti všech
fyzikálních čtení. Ztracený rozdíl se nesmí v dalším kroku tiše znovu dodat.
U přístroje bude takovým rozdílem korelace pole s referencí.

V aritmetické větvi je $j=e^{2\pi i/5}$ primitivní pátý kořen jednotky.
Položme $\mathcal O=\mathbb Z[j]=\mathbb Z[J]$,
$J=1+j^2$. Konečné čtení na celém $\mathcal O$, které má úplné přechody pro
násobení J i skalární přičtení jedničky, má třídy podle ideálu.
Oba indukované přechody jsou permutace, protože původní operace jsou
surjektivní. Jejich konjugace poskytují posuny o $J^k$ a ty generují
aditivní grupu okruhu. Třída nuly je proto aditivní podgrupa invariantní
pod J, tedy ideál; všechny ostatní třídy jsou její kosety.
Tvrzení předpokládá **celý okruh a obě operace**, ne jednu orbitu nebo
omezený kódovník. Ideál ani fyzické čtení nevybírá.

Prvočíselná návratová větev [#1346](https://github.com/mathorn1973/twist-j/issues/1346)
řeší jinou část: J je jednotka, takže $(J^n\alpha)=(\alpha)$ a
prvoideálové valuace zdroje se nemění. Zbytkové hodiny délky $r_i$ navštíví
jen $\operatorname{lcm}(r_i)$ společných fází, ne obecně jejich součin.
Čtení $n\mapsto J^n$ tak může přesně sledovat čas a současně nerozlišovat
zdroje při stejném čase. Nezávislost hodin nebo příprav z CRT neplyne.
Starší zvolený ideálový kalkul má vlastní
[veřejnou sondu](../../probes/P-RECORD-QUOTIENT-CALCULUS-1/PREREG.md).

## M03 — Kaskáda, LOW a kalendář zůstávají různými objekty

Nechť $P e_q=e_{q+1}$ modulo 5 a $b(n)$ je dvojková adresa. Roznásobením
konečného součinu dostáváme

$$
C_\varepsilon=\prod_{a=0}^{k-1}(I+(-1)^{\varepsilon_a}P^{2^a})
=\sum_{n=0}^{2^k-1}(-1)^{\varepsilon\cdot b(n)}P^n.
$$

Pro čtyři patra, s maticí jedniček $\mathbf E$, je

$$C_{0000}=I+3\mathbf E,\qquad C_{1111}=5I-\mathbf E=L,\qquad L^2=5L.$$

Součtový vztah plyne z počtů zbytků čísel 0 až 15 modulo 5. Rozdílový
součin má na konstantním vektoru hodnotu nula a na každém nenulovém
Fourierově módu hodnotu $\prod_{a=1}^4(1-j^a)=5$.
Pro zarovnané bloky tedy

$$\sum_{n=0}^{16^m-1}(-1)^{s_2(n)}P^n=L^m=5^{m-1}L.$$

Na impulsu $e_0$ vzniká směr $\ell=(4,-1,-1,-1,-1)$.
Normalizované $L/16$ má hodnost čtyři, kdežto
$|\ell\rangle\langle\ell|/20$ hodnost jednu. Příprava tohoto směru
z impulsu tedy není LOW výběrem libovolné přípravy.
Pro reálné $v_i$, $x=(0,v_1,v_2,v_3,v_4)$, $s=\sum v_i$, $Q=\sum v_i^2$, platí

$$\frac{|\langle\ell,Lx\rangle|^2}{\|\ell\|^2\|Lx\|^2}
=\frac{s^2}{4(5Q-s^2)}\quad(x\ne0).$$

To je přesný algebraický poměr na uvedeném řezu. Nenese samo zákon
skutečných výskytů. Norma tělesa portového součinu, norma stavového vektoru
a fyzikální energie jsou tři různé veličiny.

Ani kalendář se nepřenáší automaticky. Pro okno délky H a $2^k>H$, $k\ge10$,
mají časy $n_t=t2^k+H$, $t\in\{3,5,6,9,12\}$ stejná předchozí H-bitová
okna Thue–Morse i stejný zbytek modulo 1024, ale všech pět zbytků modulo 5.
Důvod je sudá binární parita těchto t a absence přenosu do jejich bitů.
Příslušné rozhraní
[#866](../../probes/P-U-PREPARATION-EVENT-RECORD-1/PREREG.md)
proto nemá pětkovou fázi bez dalšího přístupu k čítači. Nativní U čítač
obsahuje; omezená čtečka k němu nemusí mít potřebný přístup.

## M04 — Co rozhoduje šest nul a sedmá podmínka

Přijatý instrument má $K_\pm=(I\pm P^2)/2$. Ze vstupu $e_0$ má každý port
váhu $1/2$ a podmíněná rozdílová větev je
$\psi_-=(e_0-e_2)/\sqrt2$.
Ve standardní pětkové přímkové konvenci šest projektorů přímek přes
$u=(1,0)$ splňuje $\sum_{L\ni u}\Pi_L=I+A_u$, kde
$A_u e_q=e_{2-q}$. Jejich společné jádro je

$$\operatorname{span}\{e_0-e_2,e_3-e_4\}.$$

Šest nul tedy ještě neurčuje jediný stav. Přidáním nulové váhy výsledku
$q=3$ v již používaném polohovém kontextu zůstane jediný směr $\psi_-$.
Pro kladný normalizovaný operátor stavu je pak vynucen
$|\psi_-\rangle\langle\psi_-|$. Pozitivita je důležitá: nulová očekávání
kladných projektorů omezují podporu stavu do jejich společného jádra.

Jedno společné kladné bodové rozdělení $\mu$ na afinní rovině se stejnými
přímkovými odpověďmi naproti tomu dává

$$\sum_{L\ni u}\Pr_\mu(L)=1+5\mu(u)\ge1.$$

Každý bod mimo u leží právě na jedné z těchto přímek. Alespoň jedna
zakázaná váha je nejméně $1/6$; rovnoměrné rozdělení mimo u mez dosahuje.
Tím je vyloučena tato bodová třída, nikoli všechny možné skryté přístroje.
Jde o alternativní kontexty a o jeden podmíněný stav. Ani sedm nul neurčuje
celý instrument na všech přípravách. Přehled původní Wignerovy konvence je
v [C-NATIVE-FIBRE-PENTIT-WIGNER-N](../C-NATIVE-FIBRE-PENTIT-WIGNER-N/README.md).
Otázku globálního minima negativity tato konstrukce nepotřebuje a neřeší;
navazující veřejný objekt zůstává [#1344](https://github.com/mathorn1973/twist-j/issues/1344).

## M05 — Cena přesnosti konečné reference

Zvolené pole má $H_F=2I-P-P^\dagger$ se sektory energií
$0,a=(5-\sqrt5)/2,b=(5+\sqrt5)/2$.
Reference s hladinami $(i,j)\in\{0,\ldots,2N\}^2$ má energii $ai+bj$.
Pro $N\ge1$ položme

$$
c_i=\min(i,2N-i),\quad
S_N=\frac{N(2N^2+1)}3,\quad
\eta_N=\frac1{S_N}\sum_{i,j=1}^{2N-1}c_ic_j|i,j\rangle.
$$

Sousední překryv v každé ose je
$r_N=1-3/(2N^2+1)$. Rozměr registru je $(2N+1)^2$, obsazená počáteční
podpora $(2N-1)^2$ a střední energie $5N$. Prázdné krajní hladiny jsou
potřebné pro energetické přechody.

Plochý profil na **téže podpoře** má stejný rozměr a střední energii,
ale překryv $r_{\rm flat}=1-1/(2N-1)$. Platí

$$r_N-r_{\rm flat}=
\frac{2(N-1)(N-2)}{(2N^2+1)(2N-1)}.$$

Od $N=3$ je trojúhelníkový profil lepší v tomto srovnání; neprokazujeme
stejnou cenu jeho přípravy ani optimum mezi všemi profily.
Jeho amplitudy jsou racionální. Energetické projektory pole však obsahují
algebraická čísla, takže racionalita reference sama nezaručuje skalární
zlomkovou aritmetiku celého stroje.

Sedmá společná váha je přesně

$$x_N=\Pr(-,q=3)=\frac{1-r_N^2}{10}
=\frac{12N^2-3}{10(2N^2+1)^2}>0.$$

Podmíněná váha po portu minus je **$2x_N$**. Celá společná rozdílová
poziční větev je $(1/4-x_N,0,1/4-x_N,x_N,x_N)$ a má součet $1/2$.
Prvních šest nul zůstává přesných: účinný rozdílový stav zůstává v záporném
prostoru $A_u$, který má rozměr dva; sedmá podmínka v něm zachytí příměs.

| N | Rozměr registru | $x_{\rm flat}$ na téže podpoře | $x_N$ |
|---:|---:|---:|---:|
| 3 | 49 | 9/250 | 21/722 |
| 5 | 121 | 17/810 | 33/2890 |
| 8 | 289 | 29/2250 | 17/3698 |

Původní hlášená plochá rodina používala **jiný parametr**: délku podpory n,
rozměr $(n+2)^2$, energii $5(n+1)/2$, mez $8/n$ a
$x=(2n-1)/(10n^2)$. Srovnání v tabulce jí odpovídá při $n=2N-1$.
Trojúhelníková rodina má chybu této váhy řádu $N^{-2}$ místo $N^{-1}$.
Přesný cíl stále neplní. Nenulový konečně podporovaný stav nemůže být
invariantní pod nenulovým oboustranným posunem; jde o překážku v této
realizaci, nikoli obecný zákaz všech měřidel.

## M06 — Jedna reference pro celý pokračující postup

V [důkazu](PROOF.md) je definován konečný energetický lift na společných
úplných blocích, včetně doplnění unitárních hradel na jejich okraji.
Na dosažitelném prostoru platí

$$\mathcal L(W_2)\mathcal L(W_1)=\mathcal L(W_2W_1).$$

Posuny reference se skládají do rozdílu počáteční a konečné energie pole.
Pro celý konečný ideální program W, včetně archivů a nedotčeného vnějšího
systému, proto platí

$$\|\Psi_{\rm model}-\Psi_{\rm ideal}\otimes\eta_N\|^2
\le\min\left(4,\frac{24}{2N^2+1}\right).$$

Podmínkou je stejné pole, stejný lift, stejná reference a zachované
korelace; účet ostatních registrů se také musí zachovávat.
Počet kroků do této meze nevstupuje. Paměť, baterie a řízení s délkou
programu přesto rostou. Nejde o proud nových nezávislých pokusů ani
o návrat reference po každém kroku do čistého stavu.

Pro archivní váhy lze použít jednu mapu $\Gamma_N$ na počáteční stav,
která tlumí energetické mezisektorové členy překryvy $r_N,r_N,r_N^2$:

$$p(b,h)=\operatorname{Tr}[M_{b,h}\Gamma_N(\rho)M_{b,h}^\dagger].$$

To není skutečný stav samotného pole před měřením. První J kontakt
komutuje s $H_F$ a připravuje svou větev přesně. Odchylka vzniká v následném
energeticky provedeném měření. Opakované vložení nové $\Gamma_N$ by
odstranilo korelace a popsalo jiný postup.

## M07 — Jeden J kontakt se dvěma odečty versus dva J kontakty

**A. Jeden J kontakt, K následných měření.** Poslední dodaný podklad má

$$M_{b,h}=\Pi_{d_K,m_K}\cdots\Pi_{d_1,m_1}K_b.$$

Archivuje port a K výsledků. Zvolený účet začíná baterií $K+2$;
po j měřeních a uvolnění pracovního ukazatele je $B_j=K+1-j$.
Konec obsahuje $K+1$ zaplacených archivů a baterii 1.
Pro dva stejné projektivní kontexty bez dalšího zásahu je
$\Pi_{m_2}\Pi_{m_1}=0$ při $m_2\ne m_1$, takže

$$\Pr(m_2\ne m_1)=0.$$

Opakovatelnost patří soustavě pole–reference. Chybný postup s novým
nezávislým $\Gamma_N$ mezi polohovými měřeními by dal přes oba porty

$$\Pr(m_2\ne m_1)_{\rm forget}=\frac{8(1-r_N)(2+r_N)}{25}.$$

Pro $N=2$ je to $64/225$ místo nuly. Správné společné minusové historie
jsou $(0,0):7/36$, $(2,2):7/36$, $(3,3):1/18$, $(4,4):1/18$.
Součet je $1/2$; druhý port se nevyřazuje.

**B. Dva úplné J kontakty.** Původní konstrukční požadavek má jiné slovo:

$$M_{b_1,m_1,b_2,m_2}=
\Pi_{d_2,m_2}K_{b_2}\Pi_{d_1,m_1}K_{b_1}.$$

[Samostatná konstrukce](PROOF.md#p05) definuje úplný placený unitární
zápis každého instrumentu do čerstvé buňky a jeho energetický lift.
Používá čtyři archivy a baterii $5\to4\to3\to2\to1$.
První dvojice archivů zůstává při druhém kontaktu nedotčená, včetně své
celé redukované matice stavu. Referenci nepřipravujeme znovu; její konečný
stav je explicitně určen společnými větvovými vektory. Stejná celková
mez z M06 platí i pro tento program.

Jde o zde zapsanou matematickou realizaci, nikoli o ověření chybějícího
programu s pracovními ukazateli. V ideálním polohovém příkladu ze $e_0$
má 16 historií váhu $1/16$: $m_1\in\{0,2\}$ a
$m_2\in\{m_1,m_1+2\}$ modulo 5, s oběma porty při každém kontaktu.
Neshodné odečty zde mohou nastat, protože mezi nimi působí nové J.
To neodporuje přesné opakovatelnosti postupu A.

Obecný odhad skládáním dvou chyb by za rovnoměrných jednopokusových
předpokladů dal čtvercovou mez $32/n$. Není chybný, ale pro výše vymezený
společný lift je slabší než důkaz pro celý program. Samotná mez na jednom
vstupu druhé použití libovolného přístroje nezaručuje.

## M08 — Pracovní připravenost a úplná inverze

Hlášený program A má $4+3K$ dopředných kroků, dva čtecí kroky a přesnou
inverzi, tedy navrženou periodu $6K+10$; pro $K=2$ jde o 10 dopředných
a 22 celkových kroků. Počet kroků sám není důkazem úplného přechodu.
[Důkaz](PROOF.md) uvádí obecnou hodinovou konstrukci, pro kterou příslušná
mocnina identity skutečně platí. Shoda nedodaného programu s ní zůstává
k ověření. Čtení zde znamená pasivní čtecí okno, nikoli neúčtovaný další
zápis do vnější paměti.

Úplná inverze archivy smaže. Nová vlastnost je, že se mezi dopřednými
měřeními mazat nemusí. Ani původní $T_n^{16}=I$, ani nová navržená perioda
neznamenají obnovu celého zařízení při současném ponechání všech záznamů.

## M09 — Co už má veřejný program a co se nepřenáší automaticky

Ve v97 mají status **T** již tyto konkrétní L1 výsledky
([registr](../../canon/REGISTRY.tsv), [úplný Canon](../../canon/CANON.md)):

| Výsledek v97 | Obsah a hranice vůči této poznámce |
|---|---|
| FIELD-CONDITIONAL-POINTER-INSTRUMENT | Úplný podmíněný LOW/HIGH instrument, placený append a konečné uchované historie na paketovém nosiči. Není automaticky novým J± přímkovým instrumentem. |
| FIELD-COHERENT-POINTER-PREPARATION | Konečná lokální přibližná příprava koherentní E banky s čistými lázněmi, zachovanými vedlejšími výstupy a společnou chybou. Není přípravou zdejší trojúhelníkové energetické reference. |
| FIELD-FETCHED-PROGRAM-CONTROL | Pevný unitární řadič s uloženým programem, adresováním, čtecím oknem a inverzí. Přesná hradla, fáze, zdroje a abstraktní tik zůstávají dodány. |

Starší [přehled premis](../C-V96-MEASUREMENT-CLOSURE-N/PREMISES.md) je
užitečný pro porovnání nosičů; současný status určuje registr v97, nikoli
staré označení candidate v jeho podkladových poznámkách.
[C-QDD-UNINTERRUPTED-RECORD-N](../C-QDD-UNINTERRUPTED-RECORD-N/README.md)
už také rozlišuje souvislý nativní přenos a připuštěné vnější zápisy.
Nový text si nepřisvojuje první konstrukci paměti, opakování nebo přípravy.

Energetická omezení přesných a přibližných měření patří do známého rámce
Wigner–Araki–Yanase; viz
[Loveridge a Busch](https://arxiv.org/abs/1012.4362).
Opakované využití koherentních zdrojů má rozsáhlý předchozí kontext, např.
[Åberg, Catalytic Coherence](https://arxiv.org/abs/1304.1060).
Zdejší důkaz používá explicitní společný stav a nezávisí na předpokladu
bezplatné nezávislé obnovy. Priorita či novost konkrétní konstrukce nebyla
literární rešerší stanovena.

## M10 — Další konstrukční práce

1. Doplnit skutečný spustitelný balík, veřejně zmrazit jeho zdroje a přesný
   ověřovací kontrakt. Teprve potom kontrolovat deklarované úplné přechody,
   hranice baterie, čtecí okno, inverse a běhová tvrzení. Zdejší důkaz
   neposkytuje zpětnou předregistraci již hlášených běhů.
2. Propojit dvojici J kontaktů z P05 s konkrétním programem a zdokumentovat
   všechny čtyři archivy, skutečnou použitou referenci a případná řídicí
   data. Rozlišovat pokračování téhož pole a přípravu nového zdroje.
3. Stavět přípravu trojúhelníkové reference včetně čistoty, fází, vedlejších
   výstupů a energetického účtu. Rovnice
   $2c_i-c_{i-1}-c_{i+1}=2\delta_{i,N}$, $c_0=c_{2N}=0$, je místní popis
   profilu, nikoli jeho hotová fyzikální příprava. Počítání dvojic se
   stejným součtem nezajistí součet amplitud, pokud zůstane rozlišující
   informace o původních dvojicích.

Samostatně zůstává původ přijatého koherentního modelu z U/J, fyzikální
čas a výskyt skutečné události. Kaskáda neodvozuje celý prostor, Hodgeův
rozměr, fotonovou fázi, látkové režimy, gravitaci, vazby ani kosmologii.
Tyto větve mají své přesné otevřené podmínky ve
[veřejné frontier](../../canon/FRONTIER.md); poznámka neuzavírá žádnou
z jejích 23 položek O a 2 položek H.

Text je zatím pouze česky. Identifikátory M01–M10 a P01–P08 jsou stabilní
odkazy pro budoucí překlady; překlad má zachovat rozlišení stavů, protokolů
a síly evidence.
