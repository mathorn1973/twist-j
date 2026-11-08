# Úplné kontaktní akce a mez binární ikosaedrální grupy

Status: NON-CANONICAL, L1, analytická výzkumná poznámka.

Tento text vznikl ručním odvozením ze skutečných definic veřejného Canonu
v103 a z připnutých podkladů PR #1579. Není veřejnou sondou ani připuštěním
nové operace do původního U. Při napsání tohoto textu nebyl spuštěn žádný
nový vědecký výpočet. Návrh přesných kontrol je v CONTRACTS.md.

## 1. Připnuté zdroje a význam operací

Veřejný základ:

- https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md
  — původní U, šest souřadnic, DEF-RESIDUAL-CONTACT-ARCHITECTURE,
  CONTACT-RECORD, ALGEBRAIC-RESIDUAL-REALIZATION.
- https://github.com/mathorn1973/twist-j/blob/03390dca1c0a69ab8989f0daada0810c9956791a/probes/P-J-PHASE-DECLARED-CONTACT-1/PROOF.md
  — skutečný úplný kontakt, zdrojový pár, hranice přípustnosti.
- https://github.com/mathorn1973/twist-j/blob/03390dca1c0a69ab8989f0daada0810c9956791a/probes/P-CONTACT-RECORD-1/verify.py
  — funkce native, swap_read, literal_leaf, contact_word, reader_word.

Všechny součiny operací v matematickém textu působí zprava doleva.
Případné seznamy listů jsou výslovně označeny jako chronologické.
Souřadnice jedné buňky jsou

    x=(p1,p4,p1p,p4p,q,r)=(p,q,r) in F5^4 x F5 x F5.

Původní operace jsou

    a: (p1,p4,p1p,p4p,q,r) -> (p4,p1,p4p,p1p,q,r),
    b: (p1,p4,p1p,p4p,q,r) -> (-p1p,-p4p,-p1,-p4,-q,-r),
    c: (p1,p4,p1p,p4p,q,r) ->
       (-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r),
    d: (p,q,r) -> ((2,1,3,4)-p,1-q,1-r),
    e: (p,q,r) -> ((2,1,3,4)-p,2-q,1-r).

Všechna čísla zde náleží F5. Dodaná operace Ucal je

    Ucal(p,q,r)=(p,q,P_q(r)),

se skutečnou tabulkou

| q | P_q na (0,1,2,3,4) | Zápis jako permutace |
|---|---|---|
| 0 | (0,2,1,3,4) | (1 2) |
| 1 | (0,1,2,3,4) | I |
| 2 | (2,1,0,3,4) | (0 2) |
| 3 | (1,0,2,3,4) | (0 1) |
| 4 | (1,0,2,3,4) | (0 1) |

Ucal není autonomní U. Je to již deklarované dodatečné rozhraní.

## 2. Hotové kontakty A_x,A_y tvoří přesně C5 x C5

Na úplném dvoubuněčném nosiči F5^12 x {0,1} pišme

    delta(p_x,p_y)=1-h(p_x,p_y)^4 in {0,1}.

Veřejný CONTACT-RECORD dává na všech vstupních hodnotách q,r a obou
hodnotách bitu přesně

    K_i: q_i -> q_i+3 delta,
    A_i=Ucal_i K_i Ucal_i,

kde K_i obnoví všechny ostatní souřadnice. Proto

    A_i: (q_i,r_i) ->
         (q_i+3 delta,P_(q_i+3 delta) P_(q_i)(r_i)).

Delta závisí pouze na pístech; ty jsou při těchto úplných operacích
zachovány. Položme C=Ucal_x Ucal_y. Obě Ucal komutují, C^2=I, a

    A_x=C K_x C,     A_y=C K_y C.

Jde tedy o jednu společnou konjugaci dvou komutujících posunů. Pro
libovolná celá m,n platí

    A_x^m A_y^n:
      q_x -> q_x+3m delta,
      r_x -> P_(q_x+3m delta) P_(q_x)(r_x),
      q_y -> q_y+3n delta,
      r_y -> P_(q_y+3n delta) P_(q_y)(r_y),

přičemž p_x,p_y i bit jsou obnoveny úplně. To platí i pro obsazená r.

Odtud A_x^5=A_y^5=I a [A_x,A_y]=I. Protože existují p_x,p_y s delta=1,
žádný nenulový pár (m,n) modulo 5 nedává identitu: změnil by alespoň
jednu q souřadnici. Celá generovaná grupa je proto přesně C5 x C5.

Tyto dvě různé operace nemohou samy být obrazy dvou meridiánů v
necyklické reprezentaci trojlístkové grupy. V komutativní grupě totiž
ABA=BAB zkrácením vynutí A=B.

Pevný úplný svědek porušení braidové relace pro dvojici A_x,A_y:

    p_x=(0,1,0,0), p_y=(1,0,0,1),
    q_x=q_y=r_x=r_y=eta=0.

Zde h=0, delta=1. A_x A_y A_x dává

    (q_x,q_y,r_x,r_y)=(1,3,0,1),

zatímco A_y A_x A_y dává

    (q_x,q_y,r_x,r_y)=(3,1,1,0).

Písty a bit jsou v obou případech stejné jako na vstupu.

## 3. Jedna Ucal a původní e již dávají přesnou necyklickou akci S3

Na celé jedné buňce definujme

    M=Ucal,     N=e Ucal e.

Chronologické seznamy listů jsou (Ucal) a (e,Ucal,e).
Operace e je involuce. Na q,r působí jako (2-q,1-r), na pístech jako
D(p)=(2,1,3,4)-p. Protože Ucal písty nemění, N obnoví písty přesně.
Také obnoví q. Na r působí

    N_q(r)=1-P_(2-q)(1-r).

Z pevné tabulky P plyne následující úplná tabulka:

| q | M_q | N_q |
|---|---|---|
| 0 | (1 2) | (1 4) |
| 1 | I | I |
| 2 | (0 2) | (0 4) |
| 3 | (0 1) | (0 1) |
| 4 | (0 1) | (0 1) |

Na vláknech q=0 a q=2 jsou to dvě transpozice se společným právě jedním
prvkem; na q=3,4 jsou stejné a na q=1 jsou obě identitou. Proto na celé
buňce, bez omezení obsazenosti r,

    M^2=N^2=I,
    MNM=NMN,
    (MN)^3=I,
    M != N.

Rovnost všech pístových souřadnic je součástí tvrzení. Například na
vlákně q=0 je MN cyklus (1 4 2), takže má přesně řád tři. Prezentace
<M,N | M^2=N^2=(MN)^3=I> dává nejvýše šest prvků a uvedené vlákno
dává věrnou akci šesti prvků. Úplná generovaná grupa je tedy přesně S3.

Je to přesná necyklická reprezentace abstraktní trojlístkové grupy.
Obrazy meridiánů mají řád dva, nikoli pět. Výsledek nevytváří obraz 2I,
neidentifikuje r s prostorovou křivkou a neodvozuje Ucal z původního U.

Samostatná delší varianta používá C=d b d místo e. Pak
C(q,r)=(2-q,2-r), C^2=I, a C Ucal C má tabulku

    ((0 2), I, (0 1), (1 2), (1 2)).

S M=Ucal rovněž generuje S3, tentokrát na společné trojici {0,1,2}.
Tato varianta není potřebná pro hlavní výsledek; nevstupuje jako další
volnost do jeho kontroly.

## 4. Hlavní mez: všechna pevná slova z původních pěti operací a Ucal

Definujme přesně

    Gamma_plus=<a,b,c,d,e,Ucal> <= Sym(F5^6).

Nejsou zde W_a,W_b, celobuněčné součty ani volba listu podle aktuálního
stavu. Jde o všechny pevné konečné seznamy těchto šesti úplných map.
Není stanovena horní mez délky slova.

### 4.1 Uzavřený tvar všech slov

Každý prvek Gamma_plus má tvar

    q'=epsilon q+c,
    r'=pi_q(r),
    p'=L p+t(q,r),

kde epsilon je 1 nebo -1, c patří F5, pi_q je permutace F5 a
t je funkce F5^2 -> F5^4. Matice L je nezávislá na q,r i p.

Konkrétně položme

    A(p1,p4,p1p,p4p)=(p4,p1,p4p,p1p),
    B(p1,p4,p1p,p4p)=(-p1p,-p4p,-p1,-p4).

Lineární část p je u a rovna A, u b,c rovna B, u d,e rovna -I a
u Ucal rovna I. Matice A,B,-I jsou komutující involuce a jejich osm
součinů je navzájem různých. Tedy

    L in Lcal=<A,B,-I> isomorphic to C2^3.

Důležitá kontrola původního c: jeho dodatečný pístový člen je

    t_c(q,r)=(2,1+r,2,1-r),

takže závisí na r, ale nikoli na p. Neztrácí se tím žádná původní vazba.

Zobrazený tvar je uzavřen na skládání a inverzi. Při součinu F G je
lineární část L_F L_G a dodatečný člen

    L_F t_G(q,r)+t_F(q_G(q),r_G(q,r)).

Zobrazení na q tvoří dihedrální grupu D_10 řádu deset. Po jeho
odstranění působí zobrazení r samostatně na pěti pětiprvkových vláknech,
tedy v podgrupě (S5)^5. Jádro současné projekce na (q,r,L) je podgrupou
aditivní grupy

    T=(F5^4)^(F5^2).

Jde o elementární abelovskou 5-grupu řádu nejvýše 5^100. Pro větu
není třeba dokazovat, že Gamma_plus obsahuje celé toto jádro, nebo
vypočítávat řád Gamma_plus.

### 4.2 Každá akce 2I touto třídou zabije centrální involuci

Nechť G=SL2(F5), z=-I. Grupa G je dokonalá, G=[G,G]. To lze zde
ověřit přímo: pro H=diag(2,3), horní elementární matici u(t) a dolní
elementární matici l(t) platí

    [H,u(t)]=u(3t),     [H,l(t)]=l(3t).

Protože 3 je invertibilní v F5 a u(t),l(t) generují SL2(F5), všechny
generátory leží v komutátorové podgrupě.

Použijeme také tuto malou grupovou větu:

    Každý homomorfismus G -> S5 zabije z.

Důkaz nevyžaduje klasifikaci všech podgrup. Obraz G je dokonalý, a tedy
leží v A5, protože znaménkový homomorfismus jej zabije. Kdyby obraz z
byl netriviální, byl by dvojitou transpozicí. Celý obraz G by pak
ležel v jejím centralizátoru v A5. Tento centralizátor je Kleinova
čtyřgrupa: pro (1 2)(3 4) je tvořen I a třemi dvojitými transpozicemi
na {1,2,3,4}. Je abelovský. Dokonalý obraz v něm musí být triviální,
což odporuje netriviálnosti obrazu z.

Nyní vezměme libovolný homomorfismus

    rho:G -> Gamma_plus.

Jeho složka v Lcal je triviální, protože Lcal je abelovská. Jeho
složka v D_10 je triviální, protože D_10 je řešitelná a dokonalý
řešitelný obraz musí být triviální. Proto rho(G) zachovává jednotlivé
q hodnoty a zobrazení na r dává pět homomorfismů G -> S5. Podle právě
dokázané věty každý z nich zabíjí z.

Rho(z) tedy působí identicky na q,r a má L=I. Leží tudíž v popsaném
5-grupovém pístovém jádře. Jeho řád současně dělí řád z, tedy dvě.
Musí být identitou.

Výsledek:

    rho(-I)=I pro každý rho:SL2(F5)->Gamma_plus.

Každá taková akce faktorizuje přes G/{I,-I}, tedy přes A5. Zvláště
Gamma_plus neobsahuje věrnou kopii 2I. Dodání právě Ucal proto dává
globální S3 z předchozí části, ale neumožní původní úplnou značenou
2I akci s netriviální centrální involucí.

Tvrzení se nevztahuje automaticky na libovolné homomorfní faktory
Gamma_plus ani na stavově řízené programy. Nevztahuje se na abecedu
s W_b nebo s celobuněčnými součty. Je to mez přesné grupové akce
prostřednictvím úplných pevných slov v právě uvedené šestici map.

## 5. Oddělená mez pro samotné Ucal pod skutečným U

Položme

    z(x)=sum(p)+q+r,     chi(x)=(z(x),r).

Všech pět původních map uzavírá tento menší faktor:

| list | nové (z,r) |
|---|---|
| a | (z,r) |
| b | (-z,-r) |
| c | (2-z,-r) |
| d | (2-z,1-r) |
| e | (3-z,1-r) |

Také skutečný autonomní výběr sigma=z+2 theta_n používá jen z a
společný čítač n. Proto dvě přípravy se stejným n,z,r mají pod
skutečným U shodné (n,z,r) historie po libovolně mnoha krocích.

Ucal tuto ekvivalenci nezachovává. Pevný svědek je

    x0=(0,0,0,0,0,0),
    x2=(3,0,0,0,2,0).

Oba vstupy mají chi=(0,0). Avšak Ucal(x0) má r=0, kdežto Ucal(x2)
má r=2. Proto Ucal nemůže být na úplném nosiči přesně realizována
žádným společným pevným počtem skutečných dopředných kroků U.
Nejde jen o nemožnost pevného slova: argument už obsahuje stavový
výběr listu, který je součástí původního U.

Stejná indukce platí v následující přesně vymezené obálce:

- konečně mnoho úplných buněk a společně připravené další buňky;
- slotové původní listy, jejich inverze, skutečné dopředné U kroky,
  celobuněčné součty a rozdíly a výměny úplných buněk;
- společná počáteční paměť řízení, jejíž aktualizace, volba operace,
  přijetí/odmítnutí a zastavení používají jen historii chi všech buněk
  a společné vnější vstupy.

Celobuněčné součty zachovávají faktor proto, že chi je lineární.
Tvrzení nezískává fyzikální připuštění těchto součtů; pouze klasifikuje
uvedenou matematickou obálku. V této obálce není možná přesná Ucal
ani se společnými pomocnými buňkami. Řízení, které nově čte q nebo
písty mimo chi, zde není zahrnuto.

Pro W_b už existuje silnější relevantní veřejná mez: #1579 ukazuje,
že W_b poruší kompatibilitu s (z,q,r), a právě proto přenese danou
pístovou odlišnost do kontaktu. Zde se toto zjištění neopakuje jako
nový objev. Chi svědek pouze odděleně zpřesňuje druhý nedodaný vstup,
totiž vazbu z q do r u Ucal.

## 6. Novost a hranice návaznosti

Nové analytické doplnění tvoří:

1. Přesná společná konjugace a úplná grupa C5 x C5 pro dvojici již
   hotových kontaktů A_x,A_y, s pevným svědkem porušení meridiánové
   relace touto dvojicí.
2. Globální S3 z M=Ucal, N=e Ucal e, včetně všech obsazených r a
   úplného obnovení pístů.
3. Univerzální tvar všech slov z {a,b,c,d,e,Ucal} a odtud věta, že
   každá jejich 2I akce zabije centrální -I.
4. Konkrétní menší faktor chi a jeho dvoustavový svědek vylučující
   přesnou Ucal v uvedené obálce skutečného U.

Body 1 a 4 jsou přímé nové důsledky dřívějších úplných vzorců, nikoli
nově objevené původní kontaktní mapy či obecná mez čtení. Veřejná
q-slepá mez kompilátoru, nedodanost W_b/Ucal a čistě deklarované
součtové konstrukce se zde nepřeznačují jako nové výsledky.

Nic v textu nedokazuje prostorový uzel, jeho stabilitu, zachování
baryonového čísla, energii kontaktu, hmotnostní poměr ani fyzikální
připuštění Ucal. Výsledek určuje konkrétní schopnost již dodané vazby
a konkrétní hranici celých pevných slov i po jejím přidání.
