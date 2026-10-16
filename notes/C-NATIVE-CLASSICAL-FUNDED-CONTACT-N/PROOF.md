# Rozhraní, konečný řád a úplný hrazený kontakt

**NON-CANONICAL / L1 / candidate-T.** Původní analytické důkazy,
A. M. Thorn, Apache-2.0. Všechny rovnosti jsou přesné.
Nezávislý přezkum jiným autorem zde není tvrzen.

## 1. Zděděná úloha a měřítka minima

Nativní stav je x=(p0,p1,p2,p3,q,r) nad F5. Při kontaktu se x i n
ponechávají. Původní vlna má racionální souřadnice u,v na konečném D,
symetrický Dirichletův operátor L a energii

    E_D(u,v) = (||v-u||² + <u,Lv>)/2.

Pásky, jejich ukazatel a ostatní ponechané údaje se nemění. Jejich energie
se přičítá k E_D do E_full. Položme H=2I-L a

    ell(0,1,2,3,4) = (0,1,2,-2,-1),
    z(q,r) = (ell(q)/2, (ell(r)+1)/2, 0, 0),
    a(q,r) = S z(q,r),
    S z = (z0-s/5,z1-s/5,z2-s/5,z3-s/5,-s/5) na Y,
    s = z0+z1+z2+z3.

Mimo pět původních zdrojových míst Y je a nulové. Kontakt C posílá
v na v+a a pracovní záznam w na w+E_D(u,v+a)-E_D(u,v).
Jeho pět skutečně připravených přijímačů je zděděná množina

    R* = {(0,4),(1,4),(1,0),(2,0),(0,1)}.

Nepočítáme znovu jejich vznik ani klasické výstupy. Zkoumáme minimum
informace pro jednorázové rozhodnutí, rozměr prostoru posunů, energetickou
zásobu a počet hodnot směru v přesně určeném dokončení s odmítáním.
To jsou různé optimalizační úlohy, nikoli globální počet fyzických součástek.

## 2. Ostré minimum řídicí informace a dva směry

S je prosté: poslední složka S z určí s a rozdíl složek i a 4 určí z_i.
Proto a(q,r) jednoznačně určuje obě hodnoty ell(q),ell(r), a tedy q,r.

Uvažujme jednorázové rozhraní kappa:R->K. Celá následná mapa klasického
stavu smí z R používat pouze kappa, při společném počátečním pomocném
stavu. Jestliže kappa(R)=kappa(R'), vyvolá na v=0 stejný výstup.
Přesná rovnost s C proto vyžaduje a(R)=a(R'), a tedy R=R'.
Nutně |im kappa|>=25 na R=F5² a >=5 na R*. Identické čtení R tuto mez
dosahuje. Jde o počet rozlišitelných vstupních případů, nikoli povinnost
vytvořit nový registr. Při sériovém binárním přenosu se tato mez vztahuje
na úplný rozlišující záznam, nikoli na počet hodnot jednoho vodiče.

Všechny posuny leží v span_Q(S e0,S e1). Na R* se vyskytují 0,
(S e0)/2 a S e1, takže afinní i lineární obal má přesně rozměr dva.
Pevná invertibilní lineární změna klasických souřadnic tento rozměr
nezmění. Z toho plyne zákaz jediného pevného směru d s posuny c(R)d.
Nejde o zákaz opakovaného použití jedné brány s různým směrováním:
po přenesení do společného výstupního rámce musejí výsledné impulsy
společně napnout alespoň tyto dva směry.

Původní jednobuněčné generátory mají na přijímači tvar

    q' = epsilon q + c,       r' = epsilon' r + d,

kde epsilon,epsilon' jsou +/-1 a c,d jsou konstanty daného písmene.
Tato vlastnost je uzavřená na pevná slova i inverze. V celé historii
q-only řízení se proto nerozliší (0,4) a (0,1); v r-only řízení se
nerozliší (1,0) a (2,0). Platí to i pro adaptivní výběr slov používající
jen pozorovanou souřadnici a společné nezávislé pomocné údaje: indukcí
jsou pozorování i rozhodnutí stejná. Požadované a jsou v obou párech různé.
Přístup k druhé souřadnici, k pístům, k volenému indexu nebo další skutečný
U krok mění třídu. Zvláště se tento důkaz nevztahuje na stavově volený U.

## 3. Překážka, která dovoluje smíšené akce

Nechť G je grupa permutací F5^6 generovaná původními g0,...,g4.
Je konečná, protože její nosič je konečný. Ve třídě R_fin dovolme
libovolnou akci konečné grupy G_tilde na úplném smíšeném nosiči, s
projekcí na G a konečným jádrem. Smíšené závislosti jsou povoleny;
nepředpokládáme oddělenost nativní a klasické části. Zahrnut je i přesný
homomorfní zdvih G, jenž zachovává všechny původní vztahy.

**Věta.** Žádná operace této třídy se na celém nosiči nerovná C.

Každý prvek konečné G_tilde má konečný řád. Pro R s a(R)!=0 však

    C^m: v -> v + m a(R)                 (m=1,2,...).

Nativní R je ponecháno a Q nemá nenulovou aditivní torzi, takže žádná
kladná mocnina není identita. Zahrnutí pracovního záznamu to nezmění.
To je spor. Tentýž argument platí pro každou konečnou nově připuštěnou
permutaci, má-li její úplná racionální akce zachovat její konečný řád.

**Rozsah je podstatný.** Konečný počet generátorů nebo jejich involutivita
sama konečnost grupy nedává. Dvě afinní reflexe mohou generovat posun.
Konečný řadič propojený s nekonečným racionálním nosičem také může mít
nekonečný řád celého vývoje. Taková vazba už musí být zvlášť definována;
není obsažena v původních vztazích. Stejně tak tato věta nevyřazuje
nové celočíselné nosiče, neomezený čítač ani shodu pouze na prázdné vrstvě.
Konečná permutace může na této vrstvě vložit požadovaný signál a příště
jej vrátit. Není to ovšem původní C na libovolně obsazené vlně.

Konkrétně tau_q=g4 g3 přičítá do q jedničku a ostatní nativní souřadnice
fixuje, takže tau_q^5=I. Připsat při každém použití navíc pevný racionální
impuls d/2 dává po pěti použitích 5d/2, čímž porušíme tento vztah.
Zdvih s impulsem [ell(q+1)-ell(q)]d/2 vztah naopak zachová: při přechodu
q=2->3 použije -2d a ostatní čtyři kroky d/2. Součet je nula.
Tato explicitní oprava připomíná, že převod modulo pěti do Q potřebuje
vlastní pravidlo přenosu; pouhé zachování g_i²=I nestačí.

Původní C také fixuje n, zatímco každé neprázdné slovo jen z dopředných
U kroků n zvětší. Změna kontaktového okamžiku nebo přidání zpětného
hodinového kroku je jiný kontrakt. Neudělujeme původnímu U globální inverzi.

## 4. Energetický rozdíl a ostré meze

Pro libovolné obsazené u,v, R a sigma v {+1,-1} platí

    Delta_sigma = E_D(u,v+sigma a)-E_D(u,v)
                = sigma <v-Hu/2,a> + ||a||²/2.              (1)

Stačí rozvinout obě kvadratické formy. Pásky ani jejich energie se
nemění. Pro prázdnou vlnu je potřebná energie

    e(z0,z1) = (4z0²+4z1²-2z0 z1)/10.                     (2)

Na zděděném R* je maximum 2/5, dosažené například v (q,r)=(0,1).
Při zachování energie, nezápornosti zbývající zásoby, ponechání nativního
stavu a energeticky rovnocenných směrových stavech je společná příprava
b0>=2/5 nutná. Konstrukce v oddílu 5 ukazuje postačitelnost i s kapacitou
B=2/5. Nejde o nově objevenou hodnotu zděděné přípravné práce; nová je
její nutnost a postačitelnost jako společné zásoby pro úplný hrazený zákon.

Pro všech 25 přijímačů leží z0 v {-1,-1/2,0,1/2,1} a z1 v
{-1/2,0,1/2,1,3/2}. Kvadratická funkce (2) je v každé souřadnici
konvexní. Maximum na obdélníku proto leží v rohu. Čtyři rohové hodnoty
jsou 2/5,8/5,3/5,1 pro (z0,z1)=(-1,-1/2),(-1,3/2),(1,-1/2),(1,3/2).
Všechny rohy jsou přípustné a maximum 8/5 nastává při (q,r)=(3,2).
To je ostrá společná zásoba pro všechny prázdné vstupy, nikoli jen R*.

Na všech obsazených vlnách společná konečná zásoba neexistuje. Zvolme
a!=0, u=0 a v=t a. Pak

    Delta_+ = (2t+1)e(a),       e(a)=||a||²/2>0,

což pro racionální t>=0 překročí každé konečné B. Ani více zásobníků
s konečným společným dostupným obnosem tuto mez neodstraní.
Záporná Delta může naopak přeplnit zásobník s omezenou kapacitou.
Úplný zákon proto musí řešit obě energetické hranice.

Tyto meze předpokládají, že právě zásobník platí změnu vlny. Povolený
pokles energie dalšího změněného registru by byl další výslovně počítaný
zdroj; v původním kontaktu se nativní stav nemění.

## 5. Úplná hrazená involuce

Přidejme ke zděděnému stavu C zásobník b v Q průnik [0,B] pro pevnou
kapacitu B>=0 a směr sigma v {+1,-1}. Původní pracovní záznam w v Q
ponecháme. Při změně směru mají oba stavy v tomto matematickém modelu
stejnou energii; fyzická realizace této vlastnosti není tvrzena.

Vyčíslíme (1) a definujeme H_B takto:

    pokud 0 <= b-Delta_sigma <= B:
        v' = v + sigma a(q,r),
        b' = b - Delta_sigma,
        w' = w + Delta_sigma,
        sigma' = -sigma;
    jinak:
        (v',b',w',sigma') = (v,b,w,sigma).

n,x,u, obě pásky, ukazatel a další uvedené nezúčastněné údaje se fixují.
Neexistuje vymazaná větev, nový prázdný registr ani postselekce.

**Věta.** H_B je involuce na celém uvedeném součinu pro libovolné B.
Zachovává E_full+b, E_full-w i b+w.

Na přijaté větvi se a nezmění. Pro opačný směr v novém stavu platí
Delta'=-Delta. Druhá nabídnutá zásoba je b'-Delta'=b, která leží
v [0,B]. Druhý krok je proto přijatý a vrací v,b,w i sigma. Zamítnutý
stav zůstává totožný, takže při druhém použití zůstane zamítnutý.
Přijatá větev nemůže skončit v zamítnuté větvi, jak právě ukazuje
zpětná kontrola. To prokazuje úplnou prostotu i surjektivitu.
Energetické a účetní identity plynou přímo z definice Delta.
Jakákoli další energie závislá jen na fixovaných n,x je také zachována;
nemusíme ji pro samotný kontakt prohlašovat za nulovou.

Při sigma=+1 a dostatku místa i energie je projekce na původní
(n,x,u,v,pásky,ukazatel,w) přesně C. Pro R*, prázdnou vlnu, w=0,
b=B=2/5 jsou všechny větve přijaty. Původní klasický stav po kontaktu
je identický se stavem #1489; nové ponechané údaje jsou b=B-e(a),sigma=-1.
Při následných F krocích se b,sigma ponechají, a jejich původní úplná
energetická rovnost tedy ihned dává E_full+b=B. F zde znovu netestujeme.

Jestliže mají fyzické směrové stavy energie epsilon_+,epsilon_-, musí
se do Delta přidat epsilon_(-sigma)-epsilon_sigma a totéž do celkového
energetického účtu. Inverzní důkaz přežije, ale mez 2/5 se bez dalšího
nepřenáší. Všechny fyzické části zásobníku a řízení vyžadují vlastní
přijetí; tabulka racionálních energií není jeho náhradou.

## 6. Proč prosté odmítnutí bez směru ztrácí vratnost

Zmrazme třídu zákonů bez dalšího měněného údaje, které na každém vstupu
provedou dopředné C a b'=b-Delta, pokud je zásoba v [0,B], a jinak
ponechají celý stav. Uvažujme R=(0,1), a=S e1 a B=e(a)=2/5.

    A: (u,v,b,w)=(0,0,2/5,0),
    Z: (u,v,b,w)=(0,a,0,2/5).

A se přijatým krokem změní v Z. Ze Z by další dopředný krok potřeboval
Delta=3e(a)=6/5, takže je zamítnut a Z se změní opět v Z.
Dva různé úplné vstupy mají stejný výstup. Ponechaný účet w kolizi
neopravuje; je již součástí obou zobrazených stavů.

Jedna hodnota směru tedy v této třídě nestačí. Dvě postačí podle oddílu 5.
Přesné minimum je dva směrové stavy **pro toto dokončení s identickým
odmítnutím**. Obecný zákaz bezbitových konzervativních doplnění netvrdíme:
například návrat na jiný konec energetického řetězce mění odmítací zákon.
Existující fáze řadiče mohou směr nést, ale jejich úplná aktualizace se
musí výslovně započítat. Hodiny ani program nelze po kontaktu zahodit.

## 7. Zbývající hypotéza a vyvrácení

Hypotéza H_native(B): existuje nezávisle přípustná rozšířená nativní
abeceda a pevné slovo, jehož úplná mapa je H_B na nosiči CONTRACT.md,
se všemi vedlejšími registry a energetickými náklady zahrnutými.
Žádná taková abeceda nebo slovo zde nebyly nalezeny. Samotné vložení
H_B do seznamu bran hypotézu nedokazuje; jen ji přijímá za nový předpoklad.

Kandidát musí před testem specifikovat úplné primitivní mapy, energii,
počáteční pomocné stavy, řazení a rovnost výstupu. Vyvrátí jej jediný
obsazený vstup s odlišným v', změněným zdrojem, chybějícím záznamem,
porušením H_B²=I nebo energetické identity. Zvlášť ostrý test je dvojice
A,Z výše. Záporný výsledek této dvojice odmítá konkrétní naivní zákon,
nikoli všechna přípustná rozšíření.

Výsledek tedy zužuje chybějící rozhraní a předkládá jeho úplný vratný
energetický kontrakt. Nezavírá nativní ani fyzikální otázku. Canon v101,
QUADRATIC-MEMORY-NATIVE-CONTACT a QDD-INSTRUMENT-APPARATUS zůstávají beze změny.
