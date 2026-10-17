# Kontaktní akce a kladné meridiány — předběžný kontrakt

**Status: NON-CANONICAL, L1; místní pomocná kontrola analytické poznámky.**

Tento kontrakt přijímá níže uvedené přesné návrhy před prvním novým
vědeckým během této větve. Nejde o veřejnou P-sondu, změnu Canonu,
připuštění nového rozhraní ani tvrzení o fyzikálním protonu.

## 1. Přijatý veřejný a dříve ověřený základ

- Public Canon v103, `main` a tag `canon-v103`:
  `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`.
- `CONTENT_COMMIT`: `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`.
- Canon má 1 052 518 bajtů a SHA-256
  `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`.
- Kontaktní definice: původní `a,b,c,d,e`,
  `DEF-RESIDUAL-CONTACT-ARCHITECTURE`, `CONTACT-RECORD`,
  `QUADRATIC-MEMORY-NATIVE-CONTACT` na tomto pevném základu.
- PR #1579, head `03390dca1c0a69ab8989f0daada0810c9956791a`,
  poskytuje další připnutý podklad skutečných úplných kontaktních listů.
- Předchozí souřadnicová práce pro značenou grupu
  `H=<S,T>`, řád 120, Kleinův invariantní okruh a vztah forem:
  `TWIST-J_trojlistek_souradnice_a_nativni_mez.zip`, SHA-256
  `2a11f8019860499f64c457f997c4f7171e0d3bad0e8f8b74d3e7787e69c975ff`.

Nový výpočet neopakuje celou předchozí invariantní teorii ani veřejný
pětifázový přenos #1580 / #1581. Nativní připuštění těchto rozhraní
zůstává u současných veřejných vlastníků otevřené.

## 2. Přesně přijaté kontrakty a důkazy

Tímto se jako závazné přijímají celé následující čtyři soubory.
Jejich původní označení „návrh“ popisuje okamžik jejich napsání;
přijetí a zmrazení nastává tímto společným dokumentem a manifestem.

1. `contact/CONTRACTS.md` — cíle C0 až C5.
2. `contact/PROOF.md` — přesné definice, analytické důkazy a rozsahy.
3. `geometry/PREREG_CONTRACT_DRAFT.md` — cíle F0 až F6.
4. `geometry/PROOF.md` — geometrické značení a důkaz jeho existence.

Manifest `FREEZE.json` připne bajtové hashe tohoto dokumentu a všech
čtyř přijatých souborů. Po jeho vytvoření se tyto soubory nepřepisují.
Nutná oprava musí vzniknout v nové pojmenované verzi s důvodem;
předchozí verze, první kód a první výstupy musejí zůstat zachovány.

## 3. Přehled rozhodujících cílů

### Kontaktní část

- Celé hotové čtečky `A_x,A_y` jsou společně sdružené s nezávislými
  pěticyklickými posuny; jejich úplná grupa je přesně `C5 x C5`.
  Zadaný úplný svědek má potvrdit, že právě tato dvojice braidovou
  relaci nesplňuje. Jde o očekávaný záporný výsledek.
- Jediná předem zvolená hlavní kladná dvojice je
  `M=Ucal`, `N=e Ucal e`. Má se potvrdit úplná tabulka, obnovení
  pístů i q, vztahy `M²=N²=I`, `MNM=NMN`, přesný obraz `S3`
  a platnost pro všechny obsazené hodnoty r. Delší varianta `d b d`
  není náhradním kandidátem a nově se netestuje.
- Pro všechna pevná slova v `Gamma_plus=<a,b,c,d,e,Ucal>` se
  dokazuje uzavřený tvar `q'=epsilon q+c`, `r'=pi_q(r)`,
  `p'=L p+t(q,r)`, s `L` v `C2³` a elementárním pětigrupovým
  pístovým jádrem. Konečné kontroly certifikují skutečné generátory;
  závěr pro všechna slova zajišťuje analytická uzavřenost.
- Každý homomorfismus `SL2(F5)->Gamma_plus` má zabít `-I`.
  Nehledají se všechny dvojice slov a nevypočítává se řád
  `Gamma_plus`. Dokonalost `SL2(F5)` a centralizátor dvojité
  transpozice v `A5` mají v důkazu uvedené krátké přesné certifikáty.
- Faktor `chi=(sum(x),r)` se uzavírá pod původními generátory
  i skutečným výběrem autonomního U. Předepsaný dvoustavový svědek
  ukáže, že dodaná `Ucal` tento faktor porušuje. Závěr pro libovolný
  čas i pro přesně vymezenou chi-řízenou obálku plyne indukcí.

Bez dalšího výpočetního cíle se přijímá také přímý důsledek centrální
věty: pro konečně mnoho oddělených buněk s pouhými slotovými pevnými
slovy je grupa podgrupou `Gamma_plus^m`; `-I` se proto zabije v každé
složce. Dovětek nezahrnuje permutace adres, nové společné řízení,
`W_b`, celobuněčné součty ani jiné interakce.

### Geometrická část

- Pevné komplexní vložení je `j=exp(2 pi i/5)`.
  Rovnost se rozhoduje přesnou cyklotomickou aritmetikou.
- Záporný svědek původního kladného značení je
  `det(j³ A-I)=2+2j+j³ != 0`. `j A` má netriviální vlastní
  hodnotu `j²`; nelze jej zaměnit s jednoduchým kladným odrazem.
- Jediná zvolená oprava je `C=A²`, `D=B³` a
  `R1=j³ C`, `R2=j³ D`. Ověří se předepsané matice, braidová
  relace, páté mocniny, centra `(CD)³=-I` a
  `(R1 R2)³=-j³ I`, a generující certifikáty.
- `Q=[[a,0],[-s,1]]`, `a=j+j⁴`, `s=j²-j³`, má výslovnou
  integrální inverzi a uskutečňuje přesně uvedený Galoisův převod.
- Konkrétní forma `f=f0(su+av,v)` se má ověřit koeficientově:
  pod `R1,R2` má charakter `f -> j f`; nejde jen o kontrolu stupně.
- Redukce je modulo `lambda=1-j`, tedy do `F5`, a musí dát
  `A0²`, `B0³`, sdružené s původními `A0,B0` maticí
  `diag(2,1)`. Toto sdružení nepřidává fyzikální oprávnění.
- Existence skutečné kladné geometrické dvojice s těmito obrazy se
  dokazuje z invariantního kvocientu, geometrické prezentace,
  jednoznačnosti dvourozměrné dvojice a normalizátoru `2I`.
  Není vydávána za závěr konečného strojového výčtu cest.

## 4. Protokol implementací a prvních běhů

Budou vytvořeny dvě autorské implementace (kontaktní a geometrická)
a jedna nezávislá implementace společných cílů. Nezávislý kontrolor
obdrží tento kontrakt, přijaté definice, důkazy a primární zdroje;
před svým prvním během neobdrží nový autorský kód ani jeho výstupy.

Každý zdrojový kód se před prvním vědeckým spuštěním samostatně
zahashuje a připne v `IMPLEMENTATIONS.json`. Všechny tři implementace
musejí být připnuté před zahájením prvního z těchto běhů.

Výstupy mají od počátku deterministický obsah; časy běhů patří do
samostatného provozního záznamu. První stdout i stderr se ukládají
do nových souborů s výhradním vytvořením, nikoli přepsáním existujícího
souboru. Zachová se příkaz, verze prostředí, návratový kód a hashe.

Pokud některý pevný cíl selže, výstup zůstane FAIL. Výpočet se nesmí
přesměrovat na jinou dvojici, tabulku, kořen, normalizaci nebo cílovou
grupu. Chyba implementace se případně opraví v nové verzi s uchováním
původního zdroje a prvního výstupu. Opakování je přípustné pouze pro
konkrétní nevyřešenou chybu nebo námitku, ne pro kosmetickou změnu
reportu po úspěšném běhu.

## 5. Co úspěšná kontrola znamená

Konečné kontroly podporují uvedené algebraické důkazy. Nepředstavují
veřejný dvouarchitekturní gate, kontrolu všech fyzikálních stavů,
uskutečnění interakce původním U, odvození baryonového čísla nebo
hmotnosti, ani důkaz prostorového trojlístku uvnitř protonu.

V nové poznámce se rozlišují čtyři různé věci: úplné pevné operace,
skutečný autonomní výběr U, kladná komplexní monodromie a fyzikální
čtení. Žádná z nich se nezaměňuje za jinou bez vlastního důkazu.
