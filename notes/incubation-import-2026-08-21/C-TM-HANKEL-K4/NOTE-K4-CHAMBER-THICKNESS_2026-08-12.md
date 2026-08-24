# Tloušťka komory: co ta dvě čísla ve skutečnosti říkají

Status: NON-CANONICAL analýza, gates nothing. Reakce na exaktní rho census
a branch-free taxonomii. 2026-08-12.

## 1. Číslo, které v tabulce je a nikdo ho nespočítal

Taxonomie má 532 protínajících záznamů a rozpadá se podle profilu konců na
37 (konce (7,0,9)) a 406 + 87 + 2 = 495 (konce (9,0,7)). Proti populacím
6676 a 1417 to dává míru protnutí na stranu:

```
konce (7,0,9):   37 / 6676  =  0.554 %
konce (9,0,7):  495 / 1417  = 34.933 %
poměr                          63.0 krát
```

To je nejostřejší asymetrie v celém korpusu, ostřejší než midpointová
(99.72 proti 68.71) a ostřejší než populační (4.71 ku 1), a je to táž věc
změřená přímo. Kladně nakloněná komora je tlustá, záporně nakloněná tenká.

Nabízí se čtení, které obě asymetrie spojuje do jedné: populační poměr
NENÍ nezávislý jev, může být důsledkem tloušťky. Tlustá komora drží oba
konce uvnitř, takže se pár započítá jako diagonální; tenká je pouští ven,
takže se páry z ní ztrácejí do smíšených kategorií. Testovatelné přímo na
korpusu: podíl smíšených párů (jeden konec vzácný, druhý (8,0,8)) by měl
být na záporné straně výrazně vyšší. Phase A ta čísla má.

## 2. Musím opravit vlastní dřívější „zavřené dveře"

Dříve jsem prohlásil, že velikostní překážka neexistuje, na základě toho,
že medián ceil ||Delta||_2 je 16 a typická tabulka má čtyři kladná vlastní
čísla pod touto hodnotou, takže Weylova nutná podmínka je splnitelná. To
je pravda, ale je to hrubá mez, a já z ní udělal silnější závěr, než unese:
napsal jsem, že každé pravé no-go musí být aritmetické, nikdy velikostní.

Pencil census ukazuje, že to bylo přestřelené. Ostrou verzí téhož je
poloha zobecněných vlastních čísel páru (M, Delta), a ta je přesně to, co
se teď měří. Medián rho = 1.381 znamená, že typická tětiva dojde asi do
42 procent vzdálenosti k nejbližší stěně. To JE velikostní tvrzení a je
naživu. Zabil jsem hrubou verzi, ne myšlenku.

## 3. Trace jako mechanismus: navrženo a vyvráceno, ale podceněně

Napadlo mě, že Tr K je fiber invariant zadarmo (plyne z Tr(Delta) = 0,
dokázáno), takže kdyby Tr K předpovídalo stranu, byla by shoda stran
skoro automatická. Otestováno na 20 000 náhodných tabulkách:

```
(8,0,8)   19965   medián Tr  -15
(7,0,9)      22   medián Tr  -19   rozsah [-35, -5]
(9,0,7)      13   medián Tr  -27   rozsah [-41, -11]
rozsahy se PŘEKRÝVAJÍ; nejlepší jediný práh klasifikuje stranu na 65.7 %,
proti majoritnímu základu 62.9 %
```

Vyvráceno: Tr K stranu nerozhoduje. Ale přiznávám i slabinu testu: 22 a 13
záznamů je příliš málo na cokoli, i na ten náznak trendu ve správném
směru. Ten test patří na TVŮJ korpus, kde je vzácných profilů 6676 a 1417,
tedy o tři řády víc, a stojí jeden průchod. Jestli tam Tr K separuje, je to
mechanismus; jestli ne, je hypotéza mrtvá pořádně. Teď je mrtvá jen slabě.

Vedlejší nález ze stejného běhu, který stojí za zápis: na náhodných
tabulkách je poměr (7,0,9) ku (9,0,7) jen 1.69 ku 1, kdežto ve fiber
korpusu 4.71 ku 1. Fiber podmínka tedy kladnou stranu obohacuje zhruba
2.8 krát. Je to ale konfundované konvenční asymetrií sampleru, takže bez
symetrizace se z toho nic tvrdit nedá.

## 4. Poctivá syntéza po pěti mrtvých hypotézách

Není tu symetrie, není rigidita jako zákon, není návrat jako zákon, není
skrytá involuce, není trace jako rozhodovač. Co tu je:

```
GEOMETRIE ŠKÁLY. Fiber tětivy jsou krátké vůči šířce komory, s tenkým
near-critical ocasem, kde nejsou. Kladná komora je 63 krát tlustší než
záporná. A na veličině, která jediná rozhoduje T-A, tedy na vzdálenosti
do OPAČNÉ komory, ocas prakticky není: minimum 0.3883, nonorbitové
minimum 0.7196, do 0.1 nic.
```

To je nejsilnější pravdivé tvrzení, jaké korpus unese, a je to tvrzení o
škále, ne o zákonu. Zároveň má poctivou míru: v nejtěsnějším z 8093
záznamů by tětiva musela být prodloužena o 39 procent, tedy dojde do
72 procent potřebné vzdálenosti. To není propast, to je slušná rezerva.

## 5. Dva levné kroky, oba na existujícím korpusu

```
K1  Tr K proti straně na 8093 diagonálách. Jeden průchod, rozhodne
    hypotézu ze sekce 3 s třemi řády větší silou než můj test.
K2  Těch 46 záznamů BEZ jakéhokoli reálného kořene je nejčistší
    podpopulace v celém korpusu: u nich je inercie konstantní na CELÉ
    přímce, ne jen na segmentu. To je jediná třída, kde T-A neplatí
    „na segmentu", ale bezpodmínečně. Kdyby se ta třída dala algebraicky
    charakterizovat, je to skutečná věta pro podtřídu, a je to nejmenší
    cíl, který v korpusu zbývá.
```

A k Phase B souhlas s vlastníkovým čtením: cílený lov na skeletonech s
malým rho dává smysl, tvrzení „svědek existuje" nedává. Navíc extrapolace
téže přímky obecně není jiný přípustný Boolean fiber pár, takže rho_opp je
míra blízkosti, ne dosažitelnosti.

T-A zůstává H.
