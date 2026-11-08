# Nezávislá kontrola kontaktní a geometrické větve

**Status: NON-CANONICAL, L1. Analytická kontrola dokončena; nový vědecký kód NOT_RUN.**

Kontrolor: `contact_scope_refresh`, samostatná větev téže koordinované
asistentské relace. Nejde o vnější lidské přijetí. Tato zpráva vzniká
před prvním spuštěním nových ověřovačů této větve.

## 1. Nezávislost a přesné podklady

Před přípravou vlastního programu jsem četl pouze společný `PREREG.md`,
`FREEZE.json`, čtyři v nich uvedené kontrakty/důkazy, původní veřejné
definice a níže uvedené primární matematické zdroje. Žádný nový autorský
`contact/verify.py`, `geometry/verify.py` ani jejich nové výstupy jsem
neotevřel. Předchozí zdrojový a stavový přezkum veřejných kontaktních
větví je známá expozice; není vydáván za slepou znalost původních map.

Kontrolované SHA-256 souhlasí s manifestem:

| Soubor | SHA-256 |
|---|---|
| PREREG.md | `5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f` |
| FREEZE.json | `7b6475aba1f5a4a48de043c7b7b6f7f6d6cb1432fee5389dd9620f5e6e521861` |
| contact/CONTRACTS.md | `a59c01fae3fda515c430156b3c35700158dc01b72106bdb4fad5822e7939a7e7` |
| contact/PROOF.md | `fe33a9e87ed500feb7ece6d6ef6cb49ef950fb98d2633116e730b582059ab3cf` |
| geometry/PREREG_CONTRACT_DRAFT.md | `2677add0d957bddb190e73362afddbcab73aaf2d5f80a52b69d48d38a5d42dde` |
| geometry/PROOF.md | `a52eadca5c21565224b77493b496554ed7d79387daa02b76b952cc163f67e4de` |

Veřejný základ zůstává Public Canon v103 na
`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`. Původní řád značené
grupy H=120 a úplný Kleinův invariantní okruh jsou přijaté dřívější
výsledky. Tento přezkum je nevydává za nově samostatně odvozené.

## 2. Analytický závěr

**Ve zmrazených hlavních tvrzeních jsem nenašel blokující analytickou
chybu.** Níže uvedené rozsahy jsou podstatnou součástí tohoto závěru.
Počet budoucích úspěšných konečných kontrol je nemůže rozšířit.

### C1: úplné kontakty tvoří C5 × C5

Společná konjugace C=Ucal_x Ucal_y je správná. Ucal_x komutuje s K_y
a Ucal_y s K_x, protože delta závisí pouze na zachovaných pístech.
Oba K jsou nezávislé q-posuny. Na libovolném pevném pistonovém vstupu
s delta=1 dává dvojice exponentů modulo pět různý q-výstup. To je
důkaz přesného řádu 25 a věrnosti, bez omezeného hledání slov.

Pevný záporný svědek souhlasí i ručním výpočtem: dvojí čtení v jednom
portu posune q o šest, tedy o jednu, a vrátí jeho r na nulu; jediné
čtení druhého portu dává q=3,r=1. Záměna portů proto dává předepsané
dva různé úplné výstupy. Selhává pouze braidová relace této konkrétní
dvojice; kontaktní vzorec tím neselhává.

### C2: S3 z M=Ucal a N=e Ucal e

Skutečné e působí na q,r jako (2-q,1-r), na pístech jako involuce
v-p. Proto složené N vrací q i všechny písty přesně a jeho r-akce je
1-P_(2-q)(1-r). Zde není skryté omezení na připravené r.

Na q=0 vzniknou transpozice (1 2),(1 4), na q=2 transpozice
(0 2),(0 4), na q=3,4 se obě shodují a na q=1 jsou identity.
Relace M²=N²=(MN)³=1 tedy platí na celé buňce. Vlákno q=0 má
věrný obraz S3 a poskytuje dolní mez šesti prvků; prezentace poskytuje
horní mez. Výsledek je úplná necyklická grupová akce, s meridiány
řádu dva. Není to 2I ani prostorový uzel.

### C3: každá 2I-akce v Gamma_plus zabije centrální −I

Uzavřený tvar zachovává veškerou původní vazbu c na r. Pístová
lineární část je nezávislá na q,r; její komutující generátory skutečně
tvoří C2³. Projekce na q je v D10. Po vynucení identity na q,r a L
zbývají pouze p-posuny závislé na vstupním q,r. Jejich skládání je
obyčejné bodové sčítání, takže jádro má exponent pět.

Komutátorový důkaz dokonalosti SL2(F5) je správný pro horní i dolní
elementární matice: konjugace diag(2,3) násobí parametr čtyřmi, a
komutátor jej tedy násobí třemi. Elementární generování plyne z
Gaussovy eliminace. Použití této obecné generující věty se nepředstírá
jako důsledek deseti konečných maticových kontrol.

Každý obraz SL2(F5) v S5 leží v A5. Kdyby obraz −I byl netriviální,
byl by dvojitou transpozicí a celý obraz by ležel v jejím Kleinově
centralizátoru. Dokonalá grupa nemá netriviální abelovský obraz.
Proto −I zmizí v každé z pěti r-permutačních složek. V pístovém
5-jádře zároveň nemůže přežít prvek řádu dělícího dvěma.

Závěr je tedy univerzální pro všechny homomorfismy do konkrétní
grupy úplných pevných slov. Nepřechází automaticky na jiné programy,
homomorfní faktory cílové grupy, W_b, CSUM nebo nové společné řízení.
Přímý součin konečně mnoha oddělených buněk podléhá téže větě po
každé složce. Permutace adres nejsou tímto dodatkem pokryty.

### C4: menší faktor skutečného U

Pět affine rovnic pro chi=(sum(x),r) souhlasí s původními mapami.
Skutečný výběr listu závisí pouze na z a společném n, proto se
shodnost faktorových historií zachovává indukcí pro všechny časy.
Ucal na pevném páru x0,x2 dává r=0 proti r=2, takže tuto ekvivalenci
porušuje. Tento argument opravdu obsahuje stavový výběr původního U;
není pouhou větou o volných pevných slovech.

Uvedená rozšířená obálka je rovněž uzavřená: chi je lineární, a
úplné součty/rozdíly i výměny buněk ji proto přenášejí. Indukce
obsahuje paměť, volbu další operace i zastavení jen za výslovného
omezení řízení na chi-historii a společné vnější vstupy. Nový přímý
přístup ke q nebo pístech by předpoklad změnil.

## 3. Geometrická kontrola

### F0–F4: značení, odrazy a Galoisův převod

Ruční násobení potvrzuje explicitní C=A²,D=B³, jejich braidovou
relaci a stopu CD rovnou jedné. Z Cayleyovy–Hamiltonovy identity
plyne (CD)³=−I. Z C³=A,D²=B plyne zachování celé původní H.
Nenulový determinant CD−DC vylučuje společnou invariantní přímku.

Původní j³A nemá vlastní hodnotu jedna. Naproti tomu jA má
vlastní hodnoty 1,j². Rozlišení jednoduchého kladného oběhu od jeho
druhé mocniny je správné při zadaném komplexním vložení.

R1=j³C,R2=j³D mají vlastní hodnoty 1,j a determinant j. Jejich
centrální součin má šestou mocninu jI, čímž generují i μ5.
Triviální průnik μ5 s H plyne z determinantu, takže velikost G je
600. Tento závěr nevyžaduje vyčerpání slov.

Galoisův převod je semilineární sdružení v předepsaném významu:
nejprve se použije sigma3 na koeficienty, potom Q. Nemůže být
zaměněn za pouhou lineární změnu báze A na C při pevném vložení,
protože jejich stopy jsou různé. Q i jeho uvedená inverze jsou
integrální, s jednotkovým determinantem a.

### F5–F6: skutečné pokrytí a redukce

Ze známého invariantního okruhu H a vah skalárů μ5 vychází
C[V]^G=C[h,w]. Dvanáct nulových přímek f tvoří odrazové
nadroviny; mimo ně je akce volná. Jejich komplement v C² je
souvislý. Omezení kvocientové mapy je tedy skutečné souvislé
regulární pokrytí, nejen formální řešení stejné rovnice.

Přechod V/H -> V/G má stupen pět a místní charakter f -> jf.
Konkrétní polynomiální ověření ve vlastním programu pracuje s celým
f0(su+av,v), nikoli pouze s jeho stupněm. Vyšší dvě formy a jejich
invariantní vztah zůstávají přijatými předchozími vstupy.

Redukce je výlučně j -> 1 do O/(1-j)=F5. Dává Cbar=A0² a
Dbar=B0³; současné sdružení přes diag(2,1) je přesná algebraická
identita. Žádné oprávnění fyzikálně přejmenovat nebo řídit buňky
z této identity neplyne.

### Existence společné kladné geometrické dvojice

Potřebnou obecnou část jsem ověřil také v primárních zdrojích:

- [Broué, autorský text](https://webusers.imj-prg.fr/~michel.broue/boston.pdf),
  definice kladného odrazu a zdvihu u (2.10), věta 2.29 a tabulka
  na tiskové straně 93: G16 má dva uzly řádu pět a braidovou relaci
  délky tři. Schéma bylo ověřeno i v obrazu příslušné stránky.
  G16 nepatří mezi výjimky věty 2.29.
- [Chavli, arXiv:1504.02279](https://arxiv.org/pdf/1504.02279),
  úvod na straně 2 výslovně označuje B3 s pátými mocninami
  generátorů jako G16. Rank 600 je uveden též v důsledku 4.11.
- [Tuba–Wenzl, arXiv:math/9912013](https://arxiv.org/pdf/math/9912013),
  věta 2.9(a). Pro rozměr dva nejsou zapotřebí dodatečné kořenové
  volby, které se v téže větě objevují až v rozměrech čtyři a pět.
- [Kollár, arXiv:2212.03772v2](https://arxiv.org/html/2212.03772v2),
  příklad 7 přímo dává normalizátor 2I jako součin 2I se skaláry.

Vlastní dvourozměrný důkaz v geometry/PROOF.md je správný:
polarizovaná Cayleyova–Hamiltonova identita vynutí tr(XY)=j a
diagonalizace X určí oba diagonální členy Y i nenulový součin
jeho mimodiagonálních členů. Zbývá jen sdružení diagonální maticí.

Proto jsou geometrická generující dvojice a zadané R1,R2 současně
lineárně sdružené. Sdružující matice normalizuje G, tedy i [G,G]=H,
a podle normalizátoru se její působení liší od prvku H jen skalárem.
Přípustná společná změna základního listu proto uskuteční požadované
vnitřní sdružení. Existenční závěr je oprávněný. Neřeší konkrétní
předem zadané parametrizované přístupové cesty. Bod f=0 nesmí být
použit jako základní bod komplementu.

## 4. Vlastní ověřovač a jeho omezení

`verify.py` vznikl samostatně ze zmrazených definic. Používá:

- doslovné nativní listy a vlastní skládání čtrnáctilistového kontaktu;
- úplných 1 250 q/r řádků pro C1, pevného úplného svědka a 125
  pistonových afinních řádků pro C2;
- 750 předem stanovených řádků generátorového tvaru, osm zadaných
  lineárních součinů, dva pěticílové komutátory a přesný centralizátor
  jedné dvojité transpozice;
- 35 afinních řádků chi a pevného rozlišujícího svědka;
- vlastní cyklotomickou aritmetiku přes pětiprvkové cyklické
  koeficientové vektory modulo jediný součtový vztah;
- vlastní dvourozměrné matice a celé dvojproměnné polynomy.

Nevyhledává žádný nový kandidát, slovo, odraz, kořen nebo normalizaci.
Nevyčerpává Gamma_plus a neodhaduje její řád. Výstup je deterministický
JSON bez časů; kód nemá síťové ani souborové vstupy a nezávisí na
autorských implementacích. Běžné celočíselné aritmetické operace
postačují; dodatečné balíčky nejsou potřebné.

**Vědecké spuštění a import dosud neproběhly.** Přípustné předběžné
technické úkony jsou pouze statické čtení/syntaktické parsování a
kontrolní součty. Všechny tři zdroje musejí být zmrazeny společným
manifestem před prvním z jejich běhů. Jakýkoli první FAIL musí zůstat
zachován; úspěch se v této zprávě nepředjímá.

## 5. Dispozice

Analytické důkazy jsou v deklarovaném rozsahu připravené ke společné
přesné kontrole. Nežádám změnu žádného zmrazeného cíle. Tato větev
nepřebírá nativní připuštění kontaktu od veřejných vlastníků,
neopakuje #1580/#1581, nemění fyzikální stav a nedokazuje proton,
hmotnost, energii nebo prostorovou stabilitu trojlístku.
