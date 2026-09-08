# Po v81: pracovní program dvou konkrétních uzávěrů

**NON-CANONICAL. Pracovní program a konkrétní konstrukce, 2026-09-08.**

Základem je veřejný Canon v81, tag `canon-v81`, commit
`82d536a71025032d6dd4093db61ecb9f31990250`. Rozhodovací klauzule zůstávají
v [registru](../canon/REGISTRY.tsv), [branách](../canon/GATES.tsv)
a [Frontier](../canon/FRONTIER.md). Tento dokument je nenahrazuje.

Podnětem jsou dodaný `TWIST-J_v81_PLAN_UZAVER_2026-09-08_CZ.md`, doprovodný
text a jím odkazovaná `MAPA-OD-AXIOMU-K-FYZICE_2026-09-08_CZ.md`. Jsou to
návrhy pořadí a konstrukcí; jejich tvrzení ani pokyny se tím automaticky
nestávají přijatou definicí, hypotézou nebo oprávněním k formálnímu běhu.

## Rozvrh podle závislostí

Podpůrná etapa [#905](https://github.com/mathorn1973/twist-j/pull/905) je po
závěrečné recenzi sloučena do veřejného main v commitu
`67a7c03b7a4f37fb9d1d3e0f1150c0b87fc70960`. Zahrnuje návrh obnovy, APPEND,
implementaci přesně dvou expozic a pevnou K1. Tím je tato programová etapa
dokončena. Nevydává se nový Canon a nepřidává se kapacita obnovy ani K2/K3.

Další úsilí míří na dvě konkrétní fyzikální vazby: podepsaný poměr prvních
odezev TRC1 a lokální kvadratický odečet K1 se zachovanou úplnou kovariancí.
Původní klauzule vlastníků zůstávají širší; tyto dílčí vazby je nenahrazují.

| Pořadí | Větev A: jeden měřicí řetězec | Větev B: normalizace TT |
|---|---|---|
| První etapa, zpracována zde | Uzavřený omezený audit dostupnosti metadat NIST run3; konkrétní návrh dvouexpoziční obnovy RRP1/TRC1 | Přesný rozklad momentů potřebných pro kvadratický odečet; audit existujících zdrojů a přesné chybějící mapy K1 |
| Dokončená podpůrná revize #905 | Dvě konvence převzaty do revidovaného návrhu #539; úplný APPEND oddělen od přípustnosti; implementace přesně dvou expozic a její softwarové kontroly | Jedna konkrétní konečná mapa K1, úplný společný zdrojový zákon a analytické kontrakce spotřebovaných momentů |
| Nynější konkrétní dodávka | Pozorovací rovnice pro podepsaný poměr `-349/1421`; dokončená omezená kvalifikace tří zdrojových kandidátů bez kvalifikovaného archivu | Jedno čtení lokální kvadratické anizotropie podepsaného E-pole; čtverec před Fourierovou transformací, úplná kovariance a přesné sousední korelace |
| Chybějící fyzikální evidence | Doložené přípravy `S(e0), S(e1)`, stejný port a první přechod, nezávisle kalibrovaná znaménková cesta; poté předem vymezený test | Doložená realizace zdrojového zákona a podepsaných polí v pevných bodech/oknech; pro `r_T(k)` navíc fyzikální tensorové a skalární čtení se společnou normalizací a kladným skalárním výkonem |

Pořadí vyjadřuje skutečné závislosti, nikoli odhad doby objevu chybějícího
fyzikálního mostu. `READY` v rozvrhu Canon samo nepovoluje výpočet sondy.

[Párová pozorovací rovnice TRC1](V81-TRC1-PAIRED-SIGNED-OBSERVATION-1.md)
vybírá jeden podepsaný výstup a kontrast
`1421 beta_1/alpha_1 + 349 beta_0/alpha_0`. Společné měřítko i `g` odpadají;
relativní zisk, polarita, příprava a časový řez musí být doloženy nezávisle.
[Kvalifikace zdrojů](V81-TRC1-SIGNED-RESPONSE-SOURCE-QUALIFICATION-1.md)
uzavírá vymezený audit OGW #4, dEchorate v2 a jednoho optického zdroje
dispozicí `SOURCE_NOT_QUALIFIED_FOR_THIS_TEST`. Nejde o obecnou neexistenci
archivu ani o neúspěch fyzikálního modelu.

[Lokální odečet K1](V81-K1-LOCAL-SQUARE-OBSERVATION-1.md) určuje funkcionál
kalibrovaných příčných E-komponent. Lokální čtverec dává po transformaci
konvoluci, nikoli čtverec jednotlivých Fourierových koeficientů. Proto
prohazuje přiřazení dvou korelačních hodnot mezi pozicemi `1,4` a `2,3`.
Poznámka dodává plnou kovarianci i její přenos; fyzikální realizace tohoto
zdrojového zákona a převod na gravitační strain zůstávají nedoložené.
Deterministická slotová norma neposkytuje nenulový skalární jmenovatel.

Následující oddíly zachycují dokončený podpůrný základ. Nejsou zadáním
k jeho dalšímu rozšiřování ani k opakování stejného hledání NIST run3.

## A: co první etapa rozhodla a co následuje

### Dostupnost jednoho konkrétního archivního testu

[Kvalifikace NIST](V81-NIST-CALIBRATION-QUALIFICATION-1.md) vybrala pro
ověření připravenosti již odkrytý prefix Alice run3, lokální nastavení 0,
jedno metadaty určené okno a statistiku sousedních fyzikálních pokusů

```text
S11 = sum_(k in I) 1[Y_k >= 1 and Y_(k+1) >= 1].
```

`I` musí zachovat skutečnou sousednost pokusů, úplný jmenovatel, nedetekce,
vyloučené dvojice nastavení a nevyřešené mezery. Nejde o sousednost po
odfiltrování kliků. Číselné okno, rozhodovací práh ani hodnota statistiky
nebyly určeny z výsledků.

Omezené hledání v primární dokumentaci a katalozích skončilo dispozicí
**SOURCE_NOT_QUALIFIED_FOR_THIS_TEST**. Run3 má dokumentovaný problém s
opravou časování a prohlédnuté zdroje neposkytly samostatně dostupný
příslušný konfigurační soubor. To uzavírá tento audit dostupnosti, nikoli
otázku existence metadat ve všech archivech nebo fyzikální platnosti modelu.
Podrobné URL, rozsah hledání a známá expozice jsou v kvalifikační poznámce.

Další datový krok potřebuje nový vstup: samostatná použitelná metadata,
nebo předem zveřejněný rozsah převzetí a sémantického přístupu k metadatům
ve smíšeném archivu. Jiný běh musí být vybrán z dokumentace a dostat vlastní
dispozici zdroje. Do té doby tato statistika nepřechází do fyzikálního testu.

Ani opravené časování samo nedodá převod napěťového prahu na TRC1 `q`,
optické odezvy na `Gamma`, hodin na krok U ani příprav na hlavy a jejich
zákon. NIST kalibrace existují; chybí jejich nezávisle odůvodněné přiřazení
k veličinám tohoto čtení. Tyto rozdíly řeší definice
[#830](https://github.com/mathorn1973/twist-j/issues/830) a zdrojová větev
[#834](https://github.com/mathorn1973/twist-j/issues/834), pod vědeckým
vlastníkem `QDD-INSTRUMENT-APPARATUS [O]`.

### Konkrétní obnova se zachovaným stavem

[Návrh obnovy](V81-RRP1-FINITE-RESET-ADAPTER-1.md) dává dva předem
rezervované rezervoárové nosiče a dvě přípravy při pevném `c=(Gamma,q,N)`.
Starý zbytek vlny, páska a historie přežijí reset i následující přípravu.
Každá příprava má vlastní uvedený energetický vstup; reset starý nosič nemaže.

Návrh obsahuje přesné nosiče, rovnosti, domény a mapy. Pro pevné `H,c` je
množina dostupných stavů konečná; celá rodina nemá tvrzenou jednotnou kapacitu paměti.
Nejde o certifikát fyzikální izolace, ceny resetu ani přístroje NIST.

Po recenzi jsou do [revidovaného nekánonického návrhu #539](canon/DEF-TYPED-APPARATUS-RECORD-CONTRACT.md)
výslovně převzaty dvě oddělené konvence:

1. ReadyState může uchovávat úplnou starou historii v odděleném poli,
   když výběr další přípravy a generované jádrové výstupy nového nosiče
   na této historii nezávisí; úplný záznam starou historii zachovává.
2. Je přípustný reset na výslovné vlastní podmnožině vstupního součinu,
   když dokončení druhé expozice znamená konec dostupné kapacity.

Toto přijetí platí uvnitř revidovaného nekánonického návrhu, nyní sloučeného
do veřejného main; nemění Canon. Přidaná
[implementace](RRP1-TWO-EXPOSURE-RESET-1/README.md) má oddělené kontroly
uchování úplné historie, pásky a nenulového zbytku přes druhou přípravu
a závislostí výpočtu nových jádrových výstupů. Zahrnuje nulové i vícenásobné
průchody, `N=0`, prázdné porty, pasivní čtení a neúplnou nebo vyčerpanou
obnovu. Jde o softwarové ověření omezené implementace, nikoli průchod
vědeckou branou. Zapečetěné implementace RRP1/TRC1 se tím nepřepisují.

Po kontrole a zveřejnění kódu i rozsahu ověření prošlo všech 13 lokálních
regresních testů implementace. Přesný commit, příkaz, prostředí a hashe jsou
v jejím README; nejde o nový formální vědecký výsledek.

Recenzní nález APPEND se řeší přímo v této konstrukci: `HistoryState` je
typ všech konečných posloupností EventRecord a `append` je úplné připojení.
Samostatný predikát kontroluje přípustnost s protokolovou pozicí a správním
deníkem. Nesoudržný nebo delší zápis je hodnota typu, nikoli přípustný běh;
ten vytvoří nejvýše `2*N` interakčních záznamů. Při `N=0` deník rozlišuje
obě přípravy a reset i při prázdné interakční historii.

Dvouexpoziční obnova pomocí rezervovaného nosiče nečistí znovu tentýž
detektor, neodvozuje statistickou nezávislost hlav a nedodává zákon dlouhé
posloupnosti pro `S11`. Pro ten stále musíme rozlišit řezy jedné připravené
historie a opakované přípravy.

### Přechod od kalibrace k jedné předpovědi

Teprve konkrétní fyzikální kontext dovolí sestavit kalibrační řádky `A`
a předpovědní řádky `B` na stejné připuštěné rodině hlav. Existující
kritérium `ker([1;A]) subseteq ker(B)` pak rozhodne, zda kalibračně
nerozlišitelné přípravy dávají stejný výstup. S nejistou kalibrací se
zachová celá kompatibilní množina a rozsah předpovědí. Ověřovaný výsledek
nesmí být přidán jako kalibrační řádek. Kalibrace prvních momentů sama
nezaručuje rozdělení uspořádané statistiky; potřebný společný zákon zůstává
součástí zadání.

## B: přesný vstup do normalizace TT

[TT rozbor](V81-TT-NORMALIZATION-CLOSURE-INPUT-1.md) už dává explicitní
kontrakci druhých a čtvrtých momentů pro
`q_+=v_1^2-v_2^2`, `q_x=2*v_1*v_2`, včetně odečtení koherentního průměru.
To určuje, která data má kandidát skutečně dodat; nevolí mu stavový zákon.

Dodané návrhy je potřeba zpřesnit: pro přímé spektrum v určeném okamžiku
mohou stačit prostorové čtvrté momenty v tomto okamžiku. Dvoučasová data
jsou nutná, pokud je spotřebovává časový filtr nebo vývoj; lze je také
odvodit z úplného počátečního zákona a deterministického vývoje. Nevyžadujeme
zbytečně širší zákon, než používá skutečný odečet.

Nová [mapa K1](V81-TT-K1-SOURCE-MAP-1.md) řeší tuto konkrétní konstrukční
mezeru: z jedné čtyřbitové Thue-Morseovy zdrojové veličiny vezme dvě
překrývající se tříbitová okna, jejich znaménkové posuny použije v monomiálním
zdvihu a reálnou a imaginární část jeho normovaného Fourierova obrazu
vrátí jako dvojici. Poznámka uvádí všech deset zdrojových slov s vahami,
jedinou mapu, úplný společný zákon obou řezů a analytický výpočet momentů.

Zde `x` označuje konečný Fourierův slot a `t` jedno ze dvou oken; fyzikální
prostor a čas se tím nezavádějí. Amplituda vychází z výslovně zvolené
jednotkové koeficientové normy a unitární Fourierovy konvence. Je to úplně
určená konečná konstrukce, jejíž fyzikální připuštění a normalizace akce
vůči skalárnímu sektoru zůstávají otevřené. Bornovy normalizované váhy je
samy neurčí: škálování `v -> a*v` násobí výkon kvadratického pole `a^4`.

K2 a K3 v dodané mapě nemají přesné definice; nevytvářejí zatím připuštěnou
třídu tří kandidátů. Žádný stav se nevybírá podle příznivého `r_T`.
Záporná klauzule vlastníka vyžaduje pokrytí **všech připuštěných
normalizací**. Dva různé výsledky bez pravidla výběru ponechávají otázku
otevřenou. Omezený neúspěch K1 se nesmí vydávat za univerzální zákaz.

## Co se počítá jako výsledek

Podpůrná práce #905 je dokončena. Navazující dodávka obsahuje jednu párovou
pozorovací rovnici TRC1 s přesně vymezeným nedostatkem archivní evidence a
jeden lokální kvadratický funkcionál K1 s úplnou kovariancí a opraveným
přiřazením korelací. Oba fyzikální převody zůstávají podmíněné uvedenou
externí evidencí; neproběhlo vyhodnocení fyzikálního záznamu.
**Uzavřených původních O/H: 0. Nových formálních vět a fyzikálních
testů: 0.** Příslušná otevřená klauzule se rozhodne až dodáním jejích
vlastních vstupů a evidence, nikoli změnou názvu dílčí práce.

Rozsah další práce zůstává u těchto dvou fyzikálních vazeb. Odložení jiných
větví není záporný výsledek a nemění již zmrazené testy.
Další formální sonda dostane vlastní veřejné vymezení, přijatý verifier
a neměnný zveřejněný pin před svým prvním během podle
[POLICY.md](../POLICY.md).
