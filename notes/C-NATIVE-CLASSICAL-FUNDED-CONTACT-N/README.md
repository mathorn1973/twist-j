# Nejmenší rozhraní a hrazený vratný kontakt

**NON-CANONICAL / L1 / candidate-T analytické výsledky.**
Nativní přípustnost: **OPEN**. Fyzikální stav: **NOT_READY**.
A. M. Thorn, 14. října 2026. Apache-2.0.
Samostatná rezervace [#1495](https://github.com/mathorn1973/twist-j/issues/1495).

Navazujeme na hotový audit #1492. Nepřepočítáváme jeho přípravy, generátory,
výstupní tabulky ani důkaz oddělených sektorů. PR #1489 a jeho vlastník
zůstávají nedotčeni. Tato poznámka mění pouze svůj vlastní adresář.

## Co se podařilo určit

| Otázka a přesná třída | Výsledek |
|---|---|
| Kolik hodnot musí rozlišit jednorázové řízení přesného kontaktu? | Právě 5 na připravených přijímačích, právě 25 na všech přijímačích F5². Neznamená to další paměť: současné q,r už tuto informaci obsahují. |
| Kolik nezávislých směrů mají požadované posuny? | Právě 2 nad Q, i na připravené rodině. Jde o rozměr výsledných posunů, nikoli počet druhů bran nebo délku obvodu. |
| Stačí číst pouze q nebo pouze r mezi pevně řízenými původními jednobuněčnými slovy? | Nestačí. Každá z těchto souřadnic se takovým slovem mění nezávisle na druhé. Výrok nepoužívá stavově volený U místo pevného slova. |
| Lze celý kontakt získat v konečném rozšíření grupy původních permutací, které zachovává její vztahy? | Ne: nenulový racionální posun má nekonečný řád. Smíšené akce jsou v této třídě dovoleny; nejde o opakování překážky oddělených sektorů. |
| Nejmenší společná počáteční zásoba pro prázdnou vlnu | 2/5 pro pět připravených přijímačů; 8/5, požadujeme-li přijetí všech 25 přijímačů. Jednotky jsou původní matematické jednotky energie. |
| Jedna konečná zásoba pro přesný posun na všech obsazených vlnách | Neexistuje. Potřebný přírůstek energie je neomezený. |
| Vratná náhrada s omezeným zásobníkem | Přesná involuce H_B: řízený posun, odečet skutečné energie a změna ponechaného směru; nedostatek energie i přeplnění zásobníku mají úplně určenou větev. |

**Globální minimum přes všechny možné architektury není určeno.** Slovo
„nejmenší“ má v každém řádku svou výslovnou třídu. Ani dvě involuce obecně
nemusí generovat konečnou grupu. Při opuštění původních vztahů se proto
zákaz konečného řádu automaticky nepřenáší.

Konkrétní chybějící operací je nyní H_B z [CONTRACT.md](CONTRACT.md).
Při dostatku energie a dopředném směru provede doslova původní kontakt,
včetně pracovního záznamu. Na nepřijatých stavech je to **jiná** mapa než
původní neomezený kontakt C. Pro společnou přípravu B=2/5 přijme všech pět
zdrojových tříd a předá zděděnému klasickému pokračování přesně tutéž vlnu.
Není potřeba nově odvozovat jeho dvě výstupní tabulky.

## Co tím není odvozeno

H_B je přesný matematický požadavek na nové smíšené rozhraní. Není slovem
odvozeným z U. Chybí fyzicky nebo nativně přijatý člen, který současné q,r
skutečně spojí s racionální vlnou a zásobníkem. Výběr stupnice, znamének,
společného posunutí, adresování a spuštění zůstává zděděným předpokladem.

H_B je vratný na celém svém součinovém nosiči včetně obsazených stavů.
To neopravuje neprostotu původního U na všech stavech ani nedodává vratný
autonomní řadič celého protokolu. Zděděná inverze celého tříkrokového běhu
platí na připraveném obrazu; její rozsah se nemění. Racionální zásobník má
omezenou energii, ale nekonečně mnoho přesných hodnot: konečná bitová
paměť ani skutečná baterie z něj neplynou. Směr může využít dvě existující
fáze řadiče pouze po výslovném začlenění jejich aktualizace, nikoli resetem.

## Prameny a ověření

- Základ: public main `8b91a935c426036e00ecb300019fd94734addeec`, sloučení
  [#1492](https://github.com/mathorn1973/twist-j/pull/1492).
- Canon v101: content `421a4ec1daf07c04d19022c1ee219607e83c09a8`,
  SHA-256 `b83a99feccac173bd3c9c5851c5874ca27cbd135f71d136d793b45f86c8a87f7`,
  992352 bytů. Všech pět kontrolních součtů a předchůdnost tagu i content
  commitu byly ověřeny. Aktuální kontroly main na x86_64/aarch64 uspěly.
- Kontakt: [CONTRACT.md](https://github.com/mathorn1973/twist-j/blob/ea924e214ec3c29009fd4590f294954d3e5ad43f/notes/C-NATIVE-CLASSICAL-TWO-CUT-CONTACT-N/CONTRACT.md)
  a [PROOF.md](https://github.com/mathorn1973/twist-j/blob/ea924e214ec3c29009fd4590f294954d3e5ad43f/notes/C-NATIVE-CLASSICAL-TWO-CUT-CONTACT-N/PROOF.md),
  čtené pouze na tomto neměnném commitu #1489.
- Klasické pokračování: #1485, `1b69563af4018b08d7dc75781b12e9553a8c19c3`.
- Odlišná konečná rozhraní: [SPEC.md CW-ALG-1](https://github.com/mathorn1973/twist-j/blob/8b91a935c426036e00ecb300019fd94734addeec/probes/P-ALG-CONTACT-REALIZATION-1/SPEC.md)
  a [důkaz #1398](https://github.com/mathorn1973/twist-j/blob/521d6c77b456677375fe424cc5e2c4ec4eafdb3a/notes/C-CONTACT-INTERFACE-ADMISSION-BOUNDARY-N/PROOF.md).
  Jejich dodané brány W a konečné F5 nosiče neudělují operaci na racionální
  vlně. Jejich tvrzení ani otevřené vlastnictví neměníme.

Důkazy jsou v [PROOF.md](PROOF.md), úplný kontrakt a pevná pravidla nového
testu v [CONTRACT.md](CONTRACT.md). `audit.py` je nový pomocný přesný test,
nikoli nezávislý přezkum jiným autorem ani opakování sondy #1492.
Jeho první běh smí následovat až po zveřejnění a přečtení neměnného zdroje.
Záznam skutečného běhu bude připojen samostatně. Canon se nemění.
