# V100-JOIN-1: veřejný přezkum společného kroku a záznamu

NON-CANONICAL, L1. Samostatný návrh P-RESIDUAL-RECORD-COMPOSITION-1.
Rezervace názvu a vlastníka je [issue #1387](https://github.com/mathorn1973/twist-j/issues/1387);
vlastník je pojmenovaná relace `v100-composition-review-20261006`.
Větev předlohy je `codex/residual-record-composition-review-1`.

[PROOF.md](PROOF.md) předkládá jedinou spojovací větu
V=A_y T_alg A_x s jednou přípravou S_0, přesným obrazem S_1, úplnou
inverzí a invariantní doménou pokračování čtené dynamiky. Oba záznamy
mají výslovně jednorázový význam. První syrové r se obnovuje na konci
T_alg; jeho čtverec se chrání po každém listu následující A_y.

[PREREG-DRAFT.md](PREREG-DRAFT.md) je návrh budoucího omezeného auditu,
nikoli přijatý verifier nebo formální pin. [DEPENDENCIES.json](DEPENDENCIES.json)
fixuje přesné předlohy důkazních závislostí. Obsahový commit notes ani
úspěch jejich dokumentačního CI neznamenají přijetí vědeckého kontraktu.

## Přesné předlohy a stav veřejného přijetí

| Závislost | Přezkoumávaná verze | Veřejný stav při předložení |
|---|---|---|
| Původní veřejný základ | [Public Canon v99](https://github.com/mathorn1973/twist-j/blob/68080edc12faf029de48181f0a384f66e42dbc04/STATUS.md) | Přijatá veřejná autorita, main/tag ověřeny |
| Kontaktní záznam | [PR #1388](https://github.com/mathorn1973/twist-j/pull/1388), notes commit `8128286127f1a48b01ebda1a5c1e7a0d88d46095` | Samostatná nezměněná kandidátní předloha; přijetí vědeckého kontraktu nedoloženo |
| Kompilátor a algebraická realizace | [PR #1389](https://github.com/mathorn1973/twist-j/pull/1389), `CW-ALG-1`, notes commit `13081b0dec64ab99386a8cd06759b152e3e05636` | Samostatná kandidátní předloha; přijetí vědeckého kontraktu nedoloženo |
| Spojovací věta | `V100-JOIN-1`, tato předloha | Nový samostatný přezkum, závislosti zatím nepřijaty |

Přímé neměnné důkazní odkazy:

- [Původní kontaktní PROOF](https://github.com/mathorn1973/twist-j/blob/8128286127f1a48b01ebda1a5c1e7a0d88d46095/notes/contact-record-review-1/candidate/PROOF.md).
- [Přesná SPEC CW-ALG-1](https://github.com/mathorn1973/twist-j/blob/13081b0dec64ab99386a8cd06759b152e3e05636/notes/alg-contact-realization-review-1/SPEC.md).

CW-ALG-1 dává původním atomům A6/A7 a konkrétním N21/N23 přednost před
obecnými odvozenými aliasy, fixuje lex pořadí a syntaktické inverze a
zakazuje opakovanou homogenizaci terminálních listů. Tím určuje celé
q-zvednutí jednoho konkrétního T_alg; netvrdí shodný q-lift všech slov se
stejným faktorovým působením. Použije se právě Pi_alg, ne lexikografická Pi.

W_a,W_b, vazby Ucal_i, příprava a koncové čtení jsou výslovné předpoklady
rozšířené architektury. Prokázané následky se od nich v PROOF oddělují.
Nový primitivní list, registr ani příprava mezi kroky se nepřidává.

## Přesná zbývající podmínka

Před formálními běhy chybí přijetí přesných kontraktů/verifierů a vlastní
veřejné piny s readbackem podle aktuální POLICY. Kontaktní verifier je
součástí nezměněného kandidáta; pro algebraickou realizaci a spojení jsou
zatím předloženy návrhy omezeného ověření, nikoli přijaté programy.
Následují vlastní výsledky a přezkum každé sondy, obě architektury téhož
PR headu a agregát check. Společné začlenění v100 proto není připraveno.
Veřejné notes jsou konkrétní přezkumná předloha, nikoli náhrada těchto kroků.

Autorita a kolize byly před rezervacemi znovu ověřeny dne 2026-10-06:
206 refs, úplný veřejný inventář a otevřené issues/PRs, změny vzdálených
větví či náhradní stromy a dostupné komentáře. Žádná kolize těchto tří
kontraktů nalezena nebyla. Před každým budoucím formálním během se kontrola
obnoví; tento historický údaj není trvalým povolením.

Původní reporty zůstaly beze změny. Tato práce neprovedla obrovské slovo
ani nový vědecký běh. Zůstává odděleno ověření referenční mapy a důkaz
konečného překladu. Canon, workflow, QUADRATIC-MEMORY-NATIVE-CONTACT
a ostatní veřejní vlastníci nejsou touto předlohou měněni.

## Konkrétní ověřovač doplněný do této předlohy

Výše uvedený historický stav chybějícího kódu nahrazuje nynější
[verify.py](verify.py). [CHECK-MAP.md](CHECK-MAP.md) uvádí přesné tabulky,
symbolické složení úplných map a důkazní kroky, které nesou obecné závěry.
[VERIFIER-PINS.json](VERIFIER-PINS.json) váže místní kopie obou závislostí
na konkrétní veřejné zdroje; tato vazba není přijatým formálním pinem.

Jde o pokračování existujícího PR #1390. PROOF.md a původní PREREG-DRAFT.md
se nemění a žádná čtvrtá definiční předloha nevzniká. Přiložená kontaktní
kopie je bajtově totožná s předlohou #1388; její samostatný přezkum tím není
nahrazen ani uzavřen. Obecná symbolická mapa používá celý faktorový klíč
H_f a nikdy jej nenahrazuje identitou; konkrétní zvednutí nadále určuje
přesná gramatika CW-ALG-1.

Kód prošel pouze statickým přezkumem a syntaktickými kontrolami bez importu
či spuštění vědeckých funkcí. Před formálním pinem zbývá přijmout přesný kód,
jeho rozsah a samostatné závislosti. Teprve potom následují předepsané běhy,
jejich vlastní veřejné přezkumy a případné společné začlenění v100.
