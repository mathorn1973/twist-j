# Připnuté zdroje a rozsah jejich použití

Datum kontroly: 17. října 2026. Citované externí práce slouží jako
primární matematické zdroje. Nové kontaktní věty jsou odvozeny ze
skutečných definic TWIST-J v přiloženém důkazu; externím autorům se
nepřipisují.

## Veřejný základ TWIST-J

1. [STATUS na main dc162f03](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/STATUS.md).
   Public Canon v103 ACTIVE; CONTENT_COMMIT
   01fb76f6b3b14a6a5ec05d0017ea922390ab6f66.
2. [Canon na témže pevném commitu](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md).
   Použité definice: úplná buňka F5^6, původní a,b,c,d,e a U;
   DEF-RESIDUAL-CONTACT-ARCHITECTURE; CONTACT-RECORD;
   ALGEBRAIC-RESIDUAL-REALIZATION; QUADRATIC-MEMORY-NATIVE-CONTACT.
3. [Veřejné hashe normativních souborů](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/SHA256SUMS).
   Pět lokálních podkladů bylo znovu porovnáno s čerstvým veřejným
   seznamem. Canon: 1 052 518 bajtů, SHA-256
   d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
4. [Veřejná součtová reprodukce](https://github.com/mathorn1973/twist-j/tree/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/reproduce/kernel-connectivity).
   Dříve známá matice úplných součtů a grupa SL2(F5); tato poznámka
   ji nevydává za nově objevenou interakci.
5. [Veřejná barevná algebraická reprodukce](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/reproduce/color-ladder/verify.py).
   Souvislost se značenou grupou, invarianty a dřívějším algebraickým
   základem. Nový test neopakuje celý tento program.

Při kontrole byly úspěšné veřejné x86_64, aarch64 a check úlohy běhu
[39022927713](https://github.com/mathorn1973/twist-j/actions/runs/39022927713)
na uvedeném main; rovněž tagový a vydávací běh. Tato informace se týká
veřejného základu. Novým místním skriptům neuděluje veřejný gate.

## Kontaktní větve a vlastnictví souvisejících otázek

- [#1579, připnutý PROOF.md](https://github.com/mathorn1973/twist-j/blob/03390dca1c0a69ab8989f0daada0810c9956791a/probes/P-J-PHASE-DECLARED-CONTACT-1/PROOF.md).
  Použitý úplný kontakt a jeho vymezená obálka kompatibilní s (z,q,r).
- [Původní doslovné kontaktní listy](https://github.com/mathorn1973/twist-j/blob/03390dca1c0a69ab8989f0daada0810c9956791a/probes/P-CONTACT-RECORD-1/verify.py).
  Definice tabulkové Ucal, W_b a celých A_i, včetně obsazených q,r.
- [#1399, hranice připuštění kontaktu](https://github.com/mathorn1973/twist-j/blob/521d6c77b456677375fe424cc5e2c4ec4eafdb3a/notes/C-CONTACT-INTERFACE-ADMISSION-BOUNDARY-N/PROOF.md).
  Dříve vlastněná faktorová klasifikace a otevřené nezávislé
  připuštění rozhraní. Faktorové grupy se zde nezaměňují s úplnými
  grupovými vztahy.
- [#1502, konečné A4 přijetí](https://github.com/mathorn1973/twist-j/pull/1502#pullrequestreview-5525566559).
  Přesný head 7b4d55502be44b2f2aed4005c909d7dcb50dbc55. Pozdější
  přijetí má přednost před historickou poznámkou „čeká na A4“.
  Přijetí je úzké; globální kladná kompilace a nativní připuštění
  zůstávají otevřené.
- [#1580](https://github.com/mathorn1973/twist-j/issues/1580) a
  [draft #1581](https://github.com/mathorn1973/twist-j/pull/1581), head
  694e5839f50dc9ef19f28792c8c6b9d64307389d.
  Již vlastněný pětifázový přenos přes tři společné reference,
  úplné součty, kontakt a jeho inverzi do placeného přijímače.
  PR vznikl 17. října 2026 v 17:24:57 UTC. Jeho popis byl přečten;
  jeho nové vědecké výsledky zde nebyly nezávisle přepočítány.
  Tento směr se zde neopakuje. Ucal, další dodaná rozhraní,
  příprava a autonomní předpona zůstávají v jeho popisu otevřené.

Kontrola všech 246 vzdálených refs a neomezeného stromu main nenašla
aktivní přesně totožnou kontaktní meridiánovou větev. Starší copánkové
otázky #971, #972, #973 mají jiný výslovný rozsah. Tato stavová
kontrola není tvrzení o světové prioritě matematických výsledků.

## Dřívější souřadnicový podklad této práce

TWIST-J_trojlistek_souradnice_a_nativni_mez.zip, již předaný balíček,
SHA-256 2a11f8019860499f64c457f997c4f7171e0d3bad0e8f8b74d3e7787e69c975ff.
Obsahuje explicitní přechod ke Kleinovým formám, přesné normalizace
u lambda, původní nativní meze, předběžné cíle a dva oddělené výpočty.
Zde je přijatým podkladem, nikoli novým během. Jeho dříve přiznaná
změna formátu časového údaje po prvním pomocném běhu se nepřepisuje;
nová větev od začátku odděluje časy a zachovává první surové výstupy.

## Primární matematická literatura

### Kladné odrazy a geometrická prezentace

Michel Broué, *Reflection Groups, Braid Groups, Hecke Algebras, Finite
Reductive Groups*, Current Developments in Mathematics 2000,
[autorova verze](https://webusers.imj-prg.fr/~michel.broue/boston.pdf).

Použito: §2.10–2.14, distinguished reflection s determinantem
exp(2 pi i/e_H), kladný lokální zdvih a délka jedna; věta 2.29,
skutečná geometrická prezentace braid group; příloha s diagramem G16,
dvěma generátory řádu pět a stupni 20,30. V konvenci cest je potřeba
respektovat autorovo zobrazení do opačné grupy.

### Identifikace konečného kvocientu

Eirini Chavli, *Universal deformations of the finite quotients of the
braid group on 3 strands*, arXiv:1504.02279,
[PDF](https://arxiv.org/pdf/1504.02279).

Použito: úvod str. 2, identifikace
B3 / normal_closure(sigma_i^5) = G16; obecný rámec konečných
kvocientů. Řád nových matic se v poznámce odvozuje z přijatého
H řádu 120 a výslovné obnovy skalárního C5.

### Jednoznačnost dvourozměrné reprezentace

Imre Tuba a Hans Wenzl, *Representations of the braid group B3 and
of SL(2,Z)*, arXiv:math/9912013,
[PDF](https://arxiv.org/pdf/math/9912013).

Použito: věta 2.9(a), určení ireducibilní reprezentace v rozměru dva
spektrem generátoru. Potřebný případ je navíc v geometry/PROOF.md
dokázán samostatně pomocí stop a polarizované Cayleyovy–Hamiltonovy
identity.

### Invariantní okruh a normalizátor 2I

János Kollár, *Automorphisms and twisted forms of rings of invariants*,
arXiv:2212.03772v2,
[HTML](https://arxiv.org/html/2212.03772v2).

Použito: příklad 7, invariantní okruh typu E8, stupně 30,20,12 a
normalizátor N_GL2(2I)=C*·2I. Ten mění současné lineární sdružení
dvou generujících geometrických dvojic na vnitřní sdružení.

### Trojlístková větev a Brieskornovo pokrytí

John Milnor, *On the 3-dimensional Brieskorn manifolds M(p,q,r)*,
1975,
[PDF](https://www.maths.ed.ac.uk/~v1ranick/papers/milnbries.pdf).

Použito v přijatém podkladu: spojení Brieskornovy variety typu (2,3,5)
s cyklickým větvením nad torusovým uzlem. Link komplexního hrotu
w²+h³=0 je T(2,3); link povrchu E8 je jiný, trojrozměrný objekt.
Tyto dva nosiče se v poznámce nezaměňují.

## Citace vlastních výsledků

Novou kontaktní konstrukci a obecnou centrální překážku dokazuje
contact/PROOF.md. Geometrickou opravu a její kompatibilitu dokazuje
geometry/PROOF.md. Strojové stdout slouží jako konečné certifikáty
uvedených identit; rozsah důkazů a závislost na přijatém veřejném
základu se z nich samy neodstraňují.
