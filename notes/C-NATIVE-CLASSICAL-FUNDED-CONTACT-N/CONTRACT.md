# Úplný kontrakt a pevný test H_B

**NON-CANONICAL / L1 / candidate-T návrh, nikoli přijatá nativní brána.**
A. M. Thorn, 14. října 2026, Apache-2.0. Rezervace #1495.
Zděděné definice a neměnné zdroje jsou uvedeny v README.md a PROOF.md.

## 1. Nosič, příprava, rovnost

Při jednom kontaktovém okamžiku je úplný nosič

    (n,x,u,v,A,B_out,k,w,b,sigma,other),
    n in N0, x in F5^6, u,v in Q^D,
    A,B_out: původní dvě dvouslotové racionální pásky,
    k in {0,1}, w in Q, b in Q průnik [0,B], sigma in {+1,-1}.

`B` bez indexu je pevná kapacita zásobníku, nikoli výstupní páska.
`other` obsahuje všechny další výslovně ponechané údaje a nemění se.
Rovností je doslovná rovnost úplného stavu. Žádné souřadnice se
neztotožňují, nenormalizují ani neodstraňují. Neprovádí se nový U krok.

Pro navázání na #1489 je kontakt vložen v původní hranici n=1:
u=v=0, prázdné pásky, k=0,w=0,b=B=2/5,sigma=+1 a R v R*.
Nativní x je skutečný zděděný stav, nikoli nová příprava.
Test obecného H_B zahrnuje i stavy mimo tuto připravenou rodinu.

## 2. Operace, energie, přijímání

Použijeme beze změny původní ell, S, a(q,r) a E_D. Celá mapa je

    d = E_D(u,v+sigma a(q,r)) - E_D(u,v),
    přijmout právě tehdy, když 0 <= b-d <= B.

Přijetí mění pouze

    (v,w,b,sigma) -> (v+sigma a, w+d, b-d, -sigma).

Zamítnutí je identita celého stavu. Platí H_B^-1=H_B, E_full+b je
konstantní, E_full-w je konstantní a w+b je konstantní. Obě směrové
hodnoty mají v tomto modelu stejnou energii. Opačná fyzikální skutečnost
vyžaduje opravu rozdílu d podle PROOF.md, ne ignorování její ceny.

Zásobník má omezenou kapacitu B a je zpočátku společný pro všechny
zdroje. Nejde jen o přejmenování neomezeného podepsaného záznamu w:
b má dvě skutečné hranice a může odmítnout kontakt. w zůstává libovolný
a samostatně ponechaný, takže nevylučujeme obsazené původní účetní stavy.
Na připravené rodině je w+b=B. Tato závislost nezakládá fyzikální zásobník.

## 3. Co přesně musí dodat nativní realizace

Pozitivní kandidát před porovnáním zveřejní úplné přijaté primitivní mapy,
jejich nosiče a energetické účty, slovo a jeho časování, přípravu a konečný
stav všech pomocných souřadnic. Musí splnit úplnou rovnost s H_B, včetně
opačného směru, obsazených vln, účtu w, obou hranic b a zamítnutí.
Je-li zvolen jen menší dosažitelný podnosič, musí být vymezen předem a
výsledek se nesmí označit za úplnou realizaci tohoto kontraktu.

Přijetí brány H_B jako nového písmene není její odvození. Přijetí
racionálního kódu, zásobníku a nového vazebního členu je nová hypotéza.
Podmíněná existence takového rozšíření není fyzikální tvrzení ani výběr
jediného zákona. Potřebné hodiny, provozní okamžik, adresování a obnova
celého přístroje zůstávají mimo tento jednotlivý kontakt.

## 4. Předem stanovený nový výpočet

Tento kontrakt zmrazuje šest položek pro pomocný test; nejde o novou
formální sondu P ani o povýšení veřejného statusu.

1. **Rovnice:** definice H_B, energetický rozdíl (1), dvě invariantní
   energetické kombinace, úplná involutivita, kontrolní příklady oddílů
   2--6 důkazu.
2. **Kód:** pouze samostatný `audit.py` v tomto adresáři. Standardní
   knihovna Pythonu a Fraction; žádné náhodné veličiny ani desetinná
   aritmetika, žádný import původního ověřovače. Přesné veřejné byty
   budou přečteny před prvním spuštěním. Statická kontrola je dovolena.
3. **Nosič:** všech 25 současných přijímačů, zvlášť zděděná množina R*;
   dva směry; kapacity B=2/5 a 8/5; zásoby 0,B/2,B; čtyři u a šest v
   podle kódu, tedy přesně 7200 kontaktových případů. Vlna je podporována
   na původním Y a dvou dalších místech (0,0,2),(4,0,0), obou v D.
   Jde o přesný podprostor původního nosiče. Obsazené pásky, ukazatel,
   nativní souřadnice a program zůstávají ve stavu a kontrolují se.
   Účet w začíná v hlavním testu na 7/11; samostatní svědci používají
   i w=0 a 2/5. Celou rodinu 625 příprav ani původní F nespouštíme.
4. **Systematika:** energie se počítá přímo kvadratickou formou, kdežto
   H_B používá odvozený lineární rozdíl. Sedmimístná podmatice L je
   odvozena přímo z původních pěti slupek; nulová vlna mimo podporu
   zajišťuje přesnou rovnost s energií na celém D. Není to změna D.
   Samostatně se kontroluje dimenze posunů, maximum energie a cyklus
   tau_q. Všechny očekávané analytické závěry jsou již odvozené a známé;
   nejde o slepou předpověď ani nezávislý přezkum jiným autorem.
5. **Práh a zdroje:** nula porušených přesných rovností, 60 sekund
   celkového času pro jediné první spuštění, jeden proces. Při selhání
   uchovat zdroj i úplný dostupný výstup, nerozšiřovat meze a neopravovat
   zmrazený zdroj zpětně. Výsledek je podpůrný konečný test; univerzální
   věty závisejí na důkazech. Úspěch kontrol repozitáře na dvou
   architekturách není opakováním tohoto pomocného programu.
6. **Vrstva:** výhradně L1. Žádný fyzikální PASS, nová jednotka SI,
   četnost, měřicí zákon, nativní přijetí, přepsání Canonu nebo cizího PR.

## 5. Zvlášť rozlišující testy a důvody odmítnutí

- **Kolize bez směru:** R=(0,1),a=S e1,B=2/5. Stavy
  (u,v,b,w)=(0,0,2/5,0) a (0,a,0,2/5) se naivním dopředným zákonem
  s identickým odmítnutím oba zobrazí do druhého z nich. Tento zákon
  vyvracíme; H_B musí kolizi odstranit ponecháním opačného směru.
- **Obsazená vlna:** při u=0,v=a je skutečná cena dalšího dopředného
  posunu 6/5, nikoli přípravná cena 2/5. Kandidát, který účtuje vždy
  jen cenu z prázdné vlny, nezachovává energii.
- **Přeplnění:** při u=0,v=-a,b=B uvolní dopředný krok 2/5.
  H_B jej zamítne, protože zásobník je plný. Kontrola jen b-d>=0 nestačí.
- **Rozsah řízení:** pět hodnot R* nesmí být zaměněno za celý F5².
  Například (q,r)=(3,2) potřebuje z prázdné vlny 8/5 a musí být při
  B=2/5 odmítnuto. Při B=8/5 musejí všechny prázdné přijímače projít.
- **Nativní vztah:** naivní připsání d/2 ke každému tau_q poruší
  tau_q^5=I. Kandidát se zachováním všech původních vztahů je tím
  vyvrácen; kandidát s výslovně novým vazebním zákonem je jiná třída.

Každá nová realizace musí také projít testem na obsazených pomocných
stavech, které sama přidá. Uvedený konečný soubor takový univerzální
certifikát sám nenahrazuje. Potenciálně neomezený algoritmus výběru
nebo nepočítaná přesnost registru nesmějí být označeny za konečný zdroj.
