# Statický přezkum konkrétního kódu CW-ALG-1

NON-CANONICAL, L1. Datum 2026-10-06. Stav vědeckého běhu: **NOT RUN**.
Jde o statický podklad existujícího PR #1389, nikoli přijatý formální pin
nebo rozhodnutí veřejného přezkumu.

| Soubor | Přezkoumaný SHA-256 |
|---|---|
| verify.py | `115f6cae93934792a31178bd5b2ea630336ac7e43cf2abbeca8e2db0823222b0` |
| compiler_identity_checks.py | `54bb787eb9a222a5a7fe764863002b4490826c099ac3e599992a7d28ccbe04b7` |

Zdroj byl přečten autorem algebraického ověřovače, odděleným přezkumem
spojovacího ověřovače a koordinátorem. Kontrolovány byly původní mapy,
pořadí součinů, priority atomů, indexy obsazených registrů, atlas/inverze,
větvení a domény, orientace podpory seed, B3–B6, q-rekurence a soulad
rozsahů s PREREG-DRAFT. Mapa CHECK-MAP.md pojmenovává každou konečnou
množinu a odlišuje ji od symboliky a písemných univerzálních závěrů.

Povolena a provedena byla jen syntaktická kontrola Pythonu 3.12:
`ast.parse` zdrojového textu a `compile` do **nespuštěného** objektu kódu,
kontrola importů a surových hashů. Po výslovném uvedení pomocného modulu
do seznamu přípustných závislostí neskončila kontrola syntaxe ani hashů
chybou. Kandidát ani pomocný modul nebyl importován, žádná jeho funkce
nebyla zavolána, vědecké assertiony ani enumerace neproběhly.

Ruční dispozice syntaktických upozornění:

- Dekorátory `lru_cache` a těla tříd pouze definují cache a metody;
  konstrukce Grammar ani její matematické funkce se při importu nevolají.
- Jediný nestandardní import je přiložený `compiler_identity_checks`, až
  uvnitř main. Jeho bajty zahrnuje budoucí přijatý pin a reportované hashe.
- Zápis přes `sys.stdout.buffer.write` je zamýšlený jediný JSON stdout
  s LF. Program nepíše výsledkové soubory, bytecode, síť ani jiné procesy.
- `sys.version_info` vynucuje Python 3.12; úspěšný stdout neobsahuje čas,
  architekturu, jméno stroje ani místní cestu.
- Původní SPEC a PREREG-DRAFT odpovídají veřejným bajtům. Hodnoty hashů
  jsou kontrolovány čtením zdrojů, nikoli spuštěním `source_bindings`.

Před připnutím byly opraveny provenance hash, explicitní evidence q účinku
E/K0/Z, návaznost kovektorů A6, omezení fronty redukovaného dosahu a
payloady selhání. To jsou opravy ještě nepřijatého kódu; nejsou přepsáním
zmrazeného běhu. Původní matematická SPEC se nemění.

Při tomto čtení nebyla nalezena další blokující chyba. Statický přezkum
nepotvrzuje budoucí PASS, čas běhu ani veřejné přijetí. Chybí přijetí
přesného kódu a jeho analytických závislostí, vlastní formální pin s
readbackem a až následný předepsaný běh a dvouarchitekturní evidence.
