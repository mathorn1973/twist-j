# Aktualizace zdrojů a rozsah literatury

Čtení: 2026-10-20, po 21:09:48 UTC. Pouze čtení; žádné externí zápisy,
žádné zprávy třetím osobám, žádný vědecký program nebyl spuštěn.
Zastaralé přílohy nebyly vyhledávány ani použity.

## Aktuální autorita

Repozitář: https://github.com/mathorn1973/twist-j

Předchozí main: 0f26395b17597af882014b99639d1fb6ee6d3d36.
Nově přečtený main: b8bb9ed3ca1403df71c5192959e64cc9a9fb5018.
Datum posledního commitu: 2026-10-20T21:09:48Z.
Tree: ff03053c0528f9dae75af7922e955837d29a7bd1.
Porovnání: ahead 12 commits, behind 0, 14 změněných souborů.

STATUS.md má nezměněný blob 7936da8f8db8ec393d36c039d21e1fb58a93043c.
Zůstává ACTIVE Public Canon v103, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, SHA256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b,
1052518 bytes. AGENTS ani soubory pravidel se v této deltě neměnily.

Relevantní změna: poznámka C-J-PHASE-RESPONSE-CLOSURE-REVIEW-N
(dřívější PR #1675) je nyní na main. Její znovu načtené soubory mají
stejné bloby jako dříve přečtený zdroj:

| Soubor | Blob |
|---|---|
| PROOF.md | 9d860e01d8fd32f4626d5995744c96158319e2b9 |
| RESULT.md | de150337244ff6252ac9eeb60b02f31644211c3c |
| OBLIGATIONS.md | 3b051148d443459925b3b952603d0e6a7f8f1456 |

Obsahová matematika této poznámky se tedy od předchozí kontroly
nezměnila. Přijetí poznámky na main není povýšení do Canonu. Ostatní
změny se týkají C-RH-CM5-HECKE-DICTIONARY-N. Delta neobsahuje změnu
definice kontaktního W, jeho spektra ani dřívějšího důkazu vázané větve.
Nešlo o audit všech otevřených větví.

Pevné odkazy:

- https://github.com/mathorn1973/twist-j/blob/b8bb9ed3ca1403df71c5192959e64cc9a9fb5018/STATUS.md
- https://github.com/mathorn1973/twist-j/compare/0f26395b17597af882014b99639d1fb6ee6d3d36...b8bb9ed3ca1403df71c5192959e64cc9a9fb5018
- https://github.com/mathorn1973/twist-j/blob/b8bb9ed3ca1403df71c5192959e64cc9a9fb5018/notes/C-J-PHASE-RESPONSE-CLOSURE-REVIEW-N/PROOF.md

## Primární literatura a její přesný dosah

### Chiribella, Yang, Renner (2021)

Fundamental energy requirement of reversible quantum operations,
Physical Review X 11, 021014. Primární pevná verze:
https://arxiv.org/html/1908.10884v3

Relevantní jsou vzorce (12)-(15): operace po vláknech celkové energie,
plná cílová unita ve vláknech, která obsahují všechny systémové energie,
a identita u hranic. Konkrétní horní konstrukce článku výslovně
předpokládá konečně mnoho stejně vzdálených hladin. Naše varianta pro
libovolné omezené spektrum a spojitou baterii proto vyžaduje vlastní
přímointegrální důkaz; článek ho za nás nedodává. Sínusový profil a
nutnost rezervy na obou koncích jsou příbuzné známému postupu. Nelze
vydávat obecnou myšlenku baterie či sektorového liftu za nový objev.

Web reference přečtené tímto agentem: turn59view0, turn62view0-3.
Rodič musí zdroj sám otevřít před použitím těchto citací.

### Marvian (2022; arXiv v3 2024)

Restrictions on realizable unitary operations imposed by symmetry
and locality, Nature Physics 18, 283-289. Primární záznam:
https://arxiv.org/abs/2003.05524v3

Výsledek pro složené systémy ukazuje, že obecná symetrická unita nemusí
být dosažitelná skládáním lokálních symetrických unit. Pro naši konstrukci
je to důvod oddělit energetickou konzervaci od fyzické místnosti; není
to bez dalšího zákaz pro zde definovaný jednopárový kontaktní chod.
Web reference: turn59view2.

### Literatura, která zde netvoří důkaz

Yang, Renner, Chiribella: Energy requirement for implementing unitary
gates on energy-unbounded systems, J. Phys. A 55, 494003 (2022),
https://arxiv.org/pdf/2212.11708 . Článek řeší zejména dolní meze a
diskrétní neomezené systémové Hamiltoniány. Nepřebírám z něho tvrzení
o naší spojité baterii nebo o prostorové místnosti. Při hledání byl
jednou otevřen nesouvisející identifikátor 2205.09315; nebyl použit.

Předchozí primární články o nejednoznačnosti logaritmu a o vztahu mezi
kauzálním krokem a místním Hamiltoniánem zůstávají kontextem. Nová
globální mezera W i chybové konstanty aparátu jsou vlastní explicitně
uvedené derivace, nikoli citovaný hotový výsledek těchto článků.
