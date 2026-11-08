# Návrh zmrazených kontrol — kontaktní meridiány

Status: DRAFT FOR SHARED PREREG; NON-CANONICAL, L1.

Tento soubor sám neprohlašuje dokončenou předběžnou registraci.
Vznikl po ručním důkazu a před prvním novým vědeckým během této větve.
Nesmí být použit k volbě cíle podle výsledků výpočtu.

## C0. Zdroj a rozsah

Zdrojová šestice map je doslova popsána v PROOF.md, oddíl 1, a musí
odpovídat Canonu dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d.
Tabulka Ucal a doslovné kontaktní listy pocházejí z
P-CONTACT-RECORD-1/verify.py, převzatého beze změny v #1579 na
03390dca1c0a69ab8989f0daada0810c9956791a.

Žádné náhodné vzorkování, hledání slov, přeučování čtečky, změna tabulky
P, příprava nové paměti nebo změna cílové grupy podle výstupu.
Pouze celá čísla modulo 5, přesné permutace a doslovné původní listy.

## C1. Celé hotové kontakty

Ověř přesný algebraický vzorec

    A_i(q_i,r_i)=(q_i+3 delta,P_(q_i+3 delta)P_(q_i)(r_i)).

U podkladového CONTACT-RECORD jde o již známý úplný vzorec. Nová
kontrola má z něj nezávisle potvrdit:

    A_x^5=A_y^5=I,
    A_x A_y=A_y A_x,
    A_x=C K_x C, A_y=C K_y C, C=Ucal_x Ucal_y.

Úplné q/r ověření lze provést na dvou hodnotách delta a všech
5^4 hodnotách (q_x,q_y,r_x,r_y), celkem 1250 řádcích. V žádném kroku
se nepředpokládá čistá paměť. Písty a bit jsou analyticky dokazatelní
obnovení pozorovatelé u celých operací, nikoli vymazané souřadnice.

Samostatně ověř doslovnými kontaktními listy pevného svědka

    p_x=(0,1,0,0), p_y=(1,0,0,1), q_x=q_y=r_x=r_y=eta=0,

a úplné konce A_x A_y A_x versus A_y A_x A_y:

    (q_x,q_y,r_x,r_y)=(1,3,0,1) versus (3,1,1,0),

písty i bit obnoveny. Tato kontrola je záporný cíl, její výsledek
se nesmí interpretovat jako selhání předem tvrzené braidové relace.

Přesnost grupy C5 x C5 odvoď z posunů a delta=1, nikoli pouhým
počtem nalezených prvků při omezeném hledání.

## C2. Kladná globální S3 akce

Pevné dvojice slov: M=(Ucal), N=(e,Ucal,e) v chronologickém pořadí.
Ověř doslovným původním e na všech 25 párech (q,r) tabulku

    M_q=((1 2),I,(0 2),(0 1),(0 1)),
    N_q=((1 4),I,(0 4),(0 1),(0 1)).

Pístové obnovení u M,N je affine identita; stačí přesný symbolický
výpočet nebo nula a čtyři pístové bázové vektory pro každý (q,r).
Přípustný redukovaný počet je 25 řádků s odděleným důkazem, že
M,N obnovují písty; přípustný přímý počet je 125 řádků.

Na celém nosiči potvrď

    M²=N²=I, MNM=NMN, (MN)³=I.

Pevný svědek netriviality je q=0,r=1, kde MN posílá r na 4.
Pevný svědek nerovnosti je q=0,r=2, kde M posílá r na1 a N na2.
Přesně šest prvků lze certifikovat tabulkami

    I,M,N,MN,NM,MNM,

a ověřením uzavřenosti těchto šesti tabulek. Nejde o hledání kandidáta.

Výstup musí výslovně říkat: obraz S3, meridiány řádu2, všechny
obsazené hodnoty r, Ucal dodána. Nesmí označit výsledek jako 2I nebo
jako prostorovou či fyzikální realizaci uzlu.

Delší d b d varianta uvedená v důkazu není potřebná pro tento cíl
a nemusí být spouštěna. Není náhradním cílem při selhání e varianty.

## C3. Přesná struktura Gamma_plus

Ověř z definic všech šesti generátorů tvar

    q'=epsilon q+c, r'=pi_q(r), p'=L p+t(q,r).

Předem pevné tabulky pístových lineárních částí:

    a:A, b:B, c:B, d:-I, e:-I, Ucal:I,

kde A je výměna sloupců a B záporná výměna řádků.
Předem pevné nenulové dodatečné členy jsou

    c:(2,1+r,2,1-r), d/e:(2,1,3,4).

Stačí přesná formální kontrola; alternativně pro každou mapu,
každých (q,r) a p=0,e1,e2,e3,e4 porovnej doslovný výstup s předem
uvedeným tvarem. Celkem 6*25*5=750 předem daných řádků.

Ověř všech osm zadaných součinů A^i B^j (-I)^k, i,j,k in {0,1},
jejich vzájemnou různost, komutaci a druhé mocniny I. Přesný řád
Gamma_plus se nesmí hledat ani odhadovat z neúplného výčtu.

Univerzální závěr pro všechna slova se dokazuje uzavřeností tvaru.
Skutečnost, že pístové jádro má exponent5, se dokazuje sečtením
pěti stejných t(q,r); nejde o vyčerpání 5^100 možných funkcí.

Grupový krok pro 2I je analytický důkaz v PROOF.md. Volitelná konečná
podpůrná kontrola smí ověřit pouze předem danou komutátorovou identitu
v SL2(F5) a centralizátor jedné pevné dvojité transpozice v A5.
Nesmí se zaměnit důkaz všech homomorfismů za hledání dvojic v Gamma_plus.

Požadovaný závěr je přesně:

    každý homomorfismus SL2(F5)->Gamma_plus zabíjí -I;
    žádná věrná úplná 2I akce touto šestilistovou abecedou.

Neplatí automaticky pro libovolné faktory, stavové řízení, W_b,
celobuněčné součty nebo autonomní U.

## C4. Menší faktor skutečného U

Ověř pět uvedených affine identit pro chi=(z,r). Stačí nula a šest
bázových vektorů pro každý původní generátor, tedy 35 řádků,
nebo přesný symbolický důkaz. Výběr sigma=z+2 theta_n závisí na chi
a společném n; all-time tvrzení zajišťuje indukce, ne konečný časový běh.

Předem pevný svědek:

    x0=(0,0,0,0,0,0), x2=(3,0,0,0,2,0),
    chi(x0)=chi(x2)=(0,0),
    r(Ucal(x0))=0, r(Ucal(x2))=2.

Ověř svědka doslovnou Ucal. Žádné hledání zastavovacího času.
Rozšířená chi-řízená obálka v PROOF.md má analytickou indukci.
Řízení přistupující k q mimo chi se nesmí zahrnout do záporného závěru.

## C5. Oponentura a selhání

Nezávislá implementace obdrží zmrazené smlouvy a skutečné definice,
nikoli autorův nový kód ani jeho nové výstupy před vlastním prvním během.
Jakákoli odlišnost od pevné tabulky, pístové identity, svědka nebo
grupové relace je FAIL a musí zůstat v záznamu. Analytické námitky
proti rozsahu mají být uvedeny samostatně; úspěšný konečný výpočet
neodstraňuje chybějící obecný důkaz.
