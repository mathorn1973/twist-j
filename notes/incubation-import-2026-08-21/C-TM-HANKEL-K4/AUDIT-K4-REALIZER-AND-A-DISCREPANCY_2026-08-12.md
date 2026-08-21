# Audit vlastního tvrzení o realizéru, a jedna neshoda mezi implementacemi

Status: NON-CANONICAL recon, gates nothing. 2026-08-12.
Skript ~/jam/claude_scratch/recon_k4_realizer_audit.py, exaktní celočíselná
aritmetika, Bareiss plus přesná Lagrangeova interpolace.

## 1. Co se auditovalo

Tvrdil jsem, že pencil D(t) = det(2M + t Delta) je sudý právě tehdy, když
flip připouští realizér g v S_4 s g^2 . v = v. Dopředný směr je třířádkové
odvození (P M P^T = M a P Delta P^T = -Delta) a je to věta. Obrácený směr
jsem NIKDY nedokázal a vlastník správně říká, že počet 78 z 2874 ho
neustavuje. Audit vezme každý orbitový diagonální pár, vyjmenuje VŠECHNY
realizéry, otestuje involutivní podmínku a porovná s exaktní sudostí.

## 2. Výsledek

```
grupových prvků prohledáno            24
orbitových diagonálních párů          44
histogram počtu realizérů             {1: 44}

realizér s g^2.v=v   pencil sudý   počet
ANO                  ANO             7
ANO                  NE              0     <- dopředný směr, musí být 0
NE                   ANO             0     <- obrácený směr, kdyby > 0, je
NE                   NE             37        bikondicionál nepravdivý
```

Tři čtení:

```
1  dopředný směr nemá porušení, jak věta žádá
2  obrácený směr nemá protipříklad na 44 párech; bikondicionál je tím
   PODPOŘEN, nikoli dokázán. 44 je málo a říkám to rovnou
3  a hlavně: realizér je ve všech 44 případech JEDINÝ. Vlastníkova obava,
   že věta vyžaduje audit všech realizujících prvků, se tím rozpouští:
   audit přes všechny realizéry je triviální, protože je právě jeden.
   Jestli to platí obecně, je to samostatné malé tvrzení, které stojí
   za ověření na plném korpusu a je zadarmo
```

## 3. Neshoda, kterou je nutné vyřešit, ne přejít

Podíl sudých mezi orbitovými diagonálními páry:

```
tato session, běh A (200 párů)      9 / 63   = 14.3 %
tato session, běh B (44 párů)       7 / 44   = 15.9 %
Phase A korpus vlastníka        78 / 2874   =  2.71 %
```

Moje dva nezávislé běhy spolu souhlasí a s korpusem se rozcházejí zhruba
šestinásobně. Není to velikostí vzorku: při p = 0.027 by v 44 párech vyšlo
očekávaně 1.2 a pravděpodobnost sedmi a více je řádu 4e-4. Je to signál, ne
šum.

Podíl orbitových na diagonále přitom sedí (moje 63/200 = 31.5 % proti
2874/8093 = 35.5 %), takže se neliší velikost té třídy, ale podíl sudých
uvnitř ní. Kandidáti na příčinu, v pořadí, jak bych je testoval:

```
K1  jiná definice orbitovosti. Testuji permute_bits přes 24 prvků a beru
    shodu s y. Jestli Phase A klasifikuje S_4 jinak, například přes
    isospektralitu jako proxy, může být jejich třída jinak složená
K2  jiná vzorkovací míra přes skeletony. Já losuji skeleton rovnoměrně a
    beru první řešení; Phase A má M1 gauge randomizaci. Involutivní
    realizéry mohou být na skeletonech rozdělené nerovnoměrně
K3  jiná definice sudosti nebo jiné uzly interpolace. Obojí je exaktní,
    takže by shodu měly dát, ale je to nejlevnější věc ke srovnání
```

Nejrychlejší rozhodčí: vzít deset konkrétních párů z Phase A klasifikovaných
jako orbitové a sudé, a deset jako orbitové a liché, a prohnat je mým
skriptem. Když se verdikty shodnou, je příčina v míře (K2) a je to vlastnost
vzorkování, ne matematiky. Když se rozejdou, je to K1 nebo K3 a jedna
z implementací má chybu.

Do vyřešení bych obě čísla citoval vedle sebe a ani jedno nebral jako
kanonické.

## 4. Co to nemění

Nic z toho nehne s hlavním závěrem: sudost není nonorbitovým mechanismem,
0 z 5219 to uzavírá bez ohledu na to, jak dopadne podíl uvnitř orbitové
třídy. T-A zůstává H.
