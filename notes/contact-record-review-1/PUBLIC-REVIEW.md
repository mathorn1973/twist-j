# P-CONTACT-RECORD-1: samostatná větev veřejného přezkumu

NON-CANONICAL, L1. Připravený podklad k přezkumu ze dne 2026-10-06.
Není to přijatá veřejná preregistrace, veřejný pin, provedený formální běh ani
společné začlenění v100. Tento obal nemění vědecký rozsah původního kandidáta.

Navržené veřejné umístění tohoto balíčku je
`notes/contact-record-review-1/`, s tímto souborem a podadresářem `candidate/`.
Nejde o umístění do `probes/` a samotné zveřejnění podkladu nespouští ani
neschvaluje formální sondu. Název a vlastník jsou rezervováni v
[issue #1385](https://github.com/mathorn1973/twist-j/issues/1385),
vlastník `v100-contact-review-20261006`. Rezervace není přijetím kontraktu,
preregistrace nebo verifieru. Stavové věty v nezměněných kopiích popisují
jejich přípravu před touto rezervací; aktuální stav této veřejné předlohy
určuje tento obal, vědecké definice a rozsah nadále původní kandidát.

## Neměnný kandidát a samostatný přezkum

V podadresáři `candidate/` jsou přesné kopie pěti předložených souborů:
[PROOF.md](candidate/PROOF.md), [PREREG.md](candidate/PREREG.md),
[README.md](candidate/README.md), [SOURCES.json](candidate/SOURCES.json)
a [verify.py](candidate/verify.py). Kopie byly porovnány se zdrojem pomocí
SHA-256 a délky v bajtech. Původní soubory nebyly upraveny a žádný ověřovač
ani jeho funkce nebyly při této přípravě spuštěny.

Tato větev posuzuje přesně původní kontakt `K_i`, celou čtečku
`Ucal_i K_i Ucal_i`, její inverzi, dva záznamy bez další přípravy a ochranu
`r_x^2` po jednotlivých listech druhé čtečky. Zachovává minimální třídu
samostatné tříhodnotové reference i všechny negativní hranice. Vložené
registry zůstávají souřadnicemi `F5`; celý nosič je `F5^12 × {0,1}`.

Přijatými předpoklady kandidáta jsou výslovná brána `W_b`, čtecí vazby
`Ucal_i`, jediná počáteční příprava a pevné koncové čtení. Jejich nativní
dostupnost, fyzická realizace, nerušivý detektor ani termodynamická cena se
zde nedokazují. Nulový záznam sám nedokládá dokončení; opakovaná celá čtečka
může záznam smazat. Ochrana prvního čtverce není invariantem celé abecedy.

Spojovací věta `V = A_y T_alg A_x` a formální realizace algebraického svědka
`Pi_alg` mají vlastní přezkumné větve. Jejich přijetí se nesmí předpokládat
při posuzování této sondy, připojovat do její původní preregistrace ani
vydávat za její běh. Společné začlenění v100 přichází až po samostatném
posouzení obou kandidátních důkazů a nové spojovací věty.

## Přesný původ bajtů

Zdrojovou sadu identifikuje místní pracovní artefakt
`contact-record-probe-20261006/probes/P-CONTACT-RECORD-1/`; tento relativní
identifikátor je údaj o původu, nikoli tvrzení o existujícím veřejném commitu.
K veřejnému přezkumu jsou přiloženy všechny zde hashované bajty. Otisky níže
nejsou veřejným pinem a samy nedokládají přijetí preregistrace.

| Soubor v `candidate/` | Bajtů | SHA-256 zdroje i kopie |
|---|---:|---|
| PROOF.md | 13626 | `805137842d66894b36cc5cef17b45bf1c67b81570bf9eb8a4c77c9394d40abf5` |
| PREREG.md | 7910 | `24a24ee5b055fec4b6a1cd6ebb5b4a3ffcec2e0e078b5f5937111e8a253ba4cd` |
| README.md | 3443 | `c9006df8528dae2655bb8a7378b504d2855283f5d8a5a37eed8f81de4b7174f0` |
| SOURCES.json | 4795 | `9943a1d831cc3ccbea1dc520071f8ff1b3a1d88bd4edf27e2cc47ea344fc6929` |
| verify.py | 17430 | `99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134` |

`SOURCES.json` dokládá původ starších místních podpůrných reportů. Jeho
`runtime_dependency: false` zůstává zachováno: veřejný důkaz a ověřovač na
těchto nepřiložených místních reportech za běhu nezávisejí. Starší počty
kontrol nejsou novým během ani náhradou veřejné brány.

## Stav a podmínky dalšího kroku

Aktuální stav této připravené větve je `REVIEW MATERIAL ONLY`:

- Přesné kopie a kontrola původu jsou hotové; původní rozsah zůstal nezměněn.
- Předchozí přezkum matematického návrhu je interní statický přezkum;
  externí přijetí tohoto balíčku není doloženo.
- Přijatý veřejný pin, formální `RUN.md`, `RESULT.md` a `EXPECTED.txt`
  této sondy nejsou doloženy a nejsou součástí balíčku.
- Výsledek veřejných běhů x86_64/aarch64 ani souhrnné brány `check` této
  sondy není doložen. Neprohlašuje se `PASS`, kanonické začlenění ani
  uzavření otevřeného vlastníka.

Před zveřejněním nebo rezervací musí být znovu zkontrolován aktuální veřejný
repozitář, pravidla, platný Canon, kolize identifikátoru a příslušní vlastníci.
Před každým budoucím veřejným během musí být dodržen tehdy aktuální postup
repozitáře, včetně přijetí a připnutí preregistrace i přesného ověřovače.
Teprve následný řádný běh může založit výstupové artefakty. Preregistrovaná
podmínka požaduje na témže PR headu Python 3.12, shodný hash ověřovače,
exit 0, prázdný stderr, byte-identical stdout vůči jedinému `EXPECTED.txt`
na obou veřejných architekturách a úspěšný agregát `check`.

## Kontrola veřejné přenositelnosti

Statické čtení pěti kopií a cílené vyhledání cest, přihlašovacích údajů,
lokálních adres a identifikátorů uživatele neodhalily soukromou absolutní
cestu, heslo ani přístupový token. Balíček neobsahuje binární soubory,
osobní údaje ani historické velké výstupy.

Původní `README.md` a `PREREG.md` obsahují budoucí cestu
`probes/P-CONTACT-RECORD-1/`, příkaz budoucího běhu a odkazy na `POLICY.md`.
Jsou ponechány doslova jako součást návrhu: v nynějším umístění pod `notes/`
nejsou instrukcí k provedení běhu ani známkou přijatého veřejného pinu.
Odkaz na `POLICY.md` znamená aktuální pravidla kořene veřejného repozitáře;
jejich stará či místní kopie tím není prohlášena za aktuální autoritu.

Tento obsah je způsobilý k předložení jako transparentní samostatný podklad
přezkumu po aktuální kontrole repozitáře. Způsobilost k veřejnému formálnímu
běhu nebo společnému začlenění v100 zatím doložena není.
