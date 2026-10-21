# Nezávislá analytická kontrola pohyblivé reference

Předmět: `mass_spectrum/PROOF_MOVING_REFERENCE.md`.

Výsledek: odvození je matematicky konzistentní. Nebyl spuštěn vědecký kód ani numerická zkouška. Kontrola se týká psaného důkazu, nikoli původu přístroje v nativní aktualizaci.

1. **Energie a prostor.** Dvě kopie mají přesně `exp[-i(H_R+H_Y)]=W_R tensor W_Y`. Posun `2alpha I` činí energii nezápornou a dovoluje bezpečnou šířku `h=4pi`. Mění jen deklarovanou globální fázi, nikoli práci či zachování energie. Kapacita `A=q+8pi` a průměr `4pi+q/2` odpovídají sinusové konstrukci.

2. **Společná translace.** Oba původní Hamiltoniány komutují s translacemi svého těžiště; `exp[i eta(R-Y)]` komutuje se společnou translací. Převod podle celkové energie i hraniční projekce respektují tutéž symetrii. Proto celý přesný přístroj zachovává společnou translaci a součet kruhových hybností. Text správně neztotožňuje tento výrok s konzervací součtu dvou hlavních úhlových větví.

3. **Hybnostní hustota.** Protože `H_pair` je vláknový v obou hybnostech, každé Fourierovo `K_tau` splňuje `K_tau* f(P,Q) K_tau=f(P+eta,Q-eta)` pro omezené měřitelné kruhové funkce. Tato identita zůstává přesná po směšování a po vynechání baterie. Nevyžaduje čistý systémový stav ani projekci na vázanou větev.

4. **Původní konečné vstupy.** Normalizace binomických stavů je správná. Podmínka `B>=2N` zajišťuje shodu starého omezeného impulzu s novým globálním cílem na právě použitém vstupu. Text jasně uvádí, že globální cílový operátor mimo tuto podporu je nyní definován nově.

5. **Odezva.** Bounded proudy mají normu nejvýše jedna, a proto půldiamantová vzdálenost `d_L` dává chybu očekávání nejvýše `2d_L`. Při `d_L=O(q^-3)` a `eta~2/q` korekce poměru rychlosti k impulzu mizí. Původní nepromítnuté přípravné a mezipásové členy zůstávají zahrnuty. Pro skutečné konečné vstupy platí potřebná doména polohy; commutatorový a Fourierův odhad ospravedlňuje posun během přístroje, který by samotná stopová vzdálenost neomezila.

6. **Relativní hmotnost.** V lokální hybnostní souřadnici kolem klidu je `p=(P-Q)/2` kanonicky sdruženo s `X=R-Y`: `[X,p]=i`. Opačný impulz mění `p` o `eta`, zatímco relativní rychlost má směrnici `2kappa`. Proto `mu_rel=1/(2kappa)=10/sqrt(16phi+7)`. Doporučeno výslovně přidat slova „v lokální hybnostní souřadnici kolem klidu“; půlení hlavních úhlů není globální kanonická souřadnice na celé dvojité kružnici. Tato formulace nemění dokázaný limit úzkých paketů.

7. **Práce.** Druhá derivace očekávání na pevném `chi0` má uvedené znaménko: `kappa+2<chi0',(H_W(0)-g)chi0'>`. Platí také `3cos(g/2)/20=3(1+sqrt5)/80`. Dvě symetricky kopnuté kopie zdvojnásobí vedoucí rozdíl práce mezi zvolenými exponenciálně místními větvemi logaritmu.

8. **Autonomie.** Text odděluje jednu aplikaci přístroje následovanou volným vývojem od časově nezávislého Hamiltoniánu, který zásah při dalších periodách opakuje. Neprohlašuje autonomní vypnutí, vnitřní hodiny ani konečný prostorový obvod za hotovou součást konstrukce.

Nebyla nalezena chyba vyžadující změnu operátorů, odhadů nebo závěru.
