# Výsledek: přesné meze a hrazená vratná brána

**NON-CANONICAL / L1.** Analytické výsledky: **candidate-T**, bez nového
nezávislého přezkumu jiným autorem. Pomocný konečný test: **PASS**.
Nativní přípustnost: **OPEN**. Fyzikální stav: **NOT_READY**.
Canon v101 a cizí pracovní větve se nemění.

## Závěr

Nejmenší jednorázové rozhraní přesného kontaktu musí rozlišovat pět
připravených přijímačů, ale všech 25 přijímačů na úplném nosiči.
Výsledné impulsy napínají přesně dva racionální směry. Meze se týkají
řídicí informace a výsledného prostoru posunů, nikoli globálního počtu bran.

Původní neomezený kontakt nelze získat z konečného rozšíření nativní
permutace se zachováním konečných vztahů; má nekonečný řád. Tento zákaz
dovoluje smíšené akce, ale netýká se všech myslitelných rozšíření nebo
shody pouze na připravené vrstvě. Nedodání obecné nativní abecedy se
nepřeznačuje za obecný důkaz nemožnosti.

V daném energetickém účtu je nejmenší společná zásoba pro prázdnou vlnu
2/5 na připravené rodině a 8/5 na všech přijímačích. Na libovolně
obsazené vlně nestačí žádná společná konečná zásoba. Ponechaný směr a
omezený nezáporný zásobník umožňují úplnou involuci H_B s přesnou
energetickou bilancí. Na hrazené dopředné větvi je její projekce přesně
původní kontakt včetně podepsaného pracovního záznamu. Na odmítnutých
vstupech původní C neuskutečňuje. V celé připravené rodině B=2/5 stačí.

Bez dalšího směrového údaje je pravidlo „proveď posun, pokud jej lze
zaplatit, jinak vše ponech“ neprosté. Konkrétní dvojice úplných stavů
z PROOF.md oddílu 6 tuto variantu vyvrací. Dva směrové stavy jsou nutné
a postačující v této výslovně omezené třídě dokončení. Směr lze sdílet
s existujícím řadičem pouze s úplně určeným ponechaným stavem.

**Chybějící nativní operace je nyní přesně specifikována, nikoli odvozena.**
H_native(B) z PROOF.md zůstává novou otevřenou hypotézou. H_B neřeší
globální neprostotu U ani autonomní vratný řadič celého přístroje.
Zásobník má omezenou energii, ale nikoli prokázanou konečnou přesnost,
fyzickou realizaci či vlastní nativní napájení.

## Neměnný zdroj a první běh

Úplný zdroj byl zveřejněn na
`06ba99583e3f45a94ce4ca50f13702c13031669b` a všechny čtyři soubory byly
přečteny veřejným GitHub rozhraním v base64 a porovnány byt po bytu
s místními soubory před prvním spuštěním. Strom souborů je
`8f75bae7e94964964084f79dd0384b39a3ec76ef`.

| Soubor | Byty | SHA-256 |
|---|---:|---|
| README.md | 5720 | `7542455989b5fb4a923582f5e607e952d5ddb6d46c98bb8581b4b1b0b96f19d8` |
| PROOF.md | 12460 | `d064be2717ed6906777bbc730f019cb578e635be2d48d800ff3baaad334ce00f` |
| CONTRACT.md | 6899 | `bedf7f6f55aafcb8bd82156a62bd6216a7dfc336c081be8ea9b0ab6a31162540` |
| audit.py | 10619 | `0b6bf417d23101b4b0a6a4a9e4948cfdddbae9d68ba6cd075f8c4e3aa82cd80f` |

Z čistého odpojeného checkoutu tohoto veřejného commitu byl proveden
jeden první běh. Zdroj se po něm neměnil, nebyl opakován ani upraven.

```text
command: python -B notes/C-NATIVE-CLASSICAL-FUNDED-CONTACT-N/audit.py
started_utc: 2026-10-14T16:56:19.873138+00:00
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
environment: PYTHONHASHSEED=0, TZ=UTC, LC_ALL=C.UTF-8
wall_seconds: 4.943997120999484
timeout_seconds: 60
timed_out: false
exit_code: 0
stdout_bytes: 380
stdout_sha256: 5fbdf0fcd31f5f9cb377702b7587d8d0e0a1a92207fc781a3136bbae31ee1d77
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Přesné původní stdout je [EXPECTED.txt](EXPECTED.txt), bez ručního
přepisování. Z celkem 7200 stavů bylo 3018 přijato, 3520 odmítnuto
pro nedostatek energie a 662 pro přeplnění zásobníku. Kontroly ověřily
úplnou involuci, všechny ponechané údaje, dvě energetické identity,
účet zásobníku, oba směry a pět negativních kontrol. Zvlášť ověřily
kardinality 5/25, rozměr 2, minima 2/5 a 8/5 a pět počátků cyklu tau_q.

Nebylo znovu spuštěno 625 původních příprav, úplná tabulka generátorů,
dvě klasické výstupní tabulky ani stará numerická simulace. Nový audit
používá sedmimístný podprostor původního D; jeho univerzální závěry
nad celým nosičem stojí na analytickém důkazu, nikoli na konečném výčtu.

## Přezkum a meze ověření

Před zveřejněním byly zkontrolovány obě inverzní větve a jejich oddělení,
znaménko a smíšený člen v energetickém rozdílu, horní i dolní mez zásoby,
všechna zachovaná pole a rozdíl úplného a připraveného nosiče. Přímá
kvadratická energie v testu je oddělena od vzorce použitého v H_B.
Jde o kontrolu stejným autorem, ne slepou nezávislou replikaci.

Statická kontrola Pythonu a místní POLICY, CANON v101, LEDGER,
GATE CONTRACT, STATUS LABELS a kontrola mezer prošly. Úspěšné kontroly
původního main na x86_64/aarch64 nejsou novou dvouarchitekturní reprodukcí
tohoto programu. Ani následné kontroly poznámkového PR takovou reprodukci
samy nevytvářejí. Nový test byl proveden pouze na zde uvedeném x86_64.

Všechny čtyři zmrazené zdrojové soubory zůstávají beze změny. Připojují
se pouze tento záznam a skutečný stdout. Žádná věta nebyla povýšena do
Canonu a žádná větev nativní nebo fyzikální přípustnosti nebyla uzavřena.
