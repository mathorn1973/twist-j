# PILOT RESULT — E-PHOTON-Z5-PHASE-MEASUREMENT-1

**Stav:** `STOP_MIXING_OR_INTEGRITY`  
**Důkazní váha:** `ZERO_PILOT_ONLY`  
**Neměnný pilotní pin:** `055c7cd3319a9d6c06dd2faef79dd1f2cb477eb8`  
**Datum běhu:** 2026-09-01

Tento výsledek není závěr o fotonové, stísněné ani rozbité fázi. Pilot byl
určen pouze pro kontrolu výpočetního jádra a míchání. Předem zmrazená gramatika
vrací STOP, takže produkční měření nesmí začít.

## 1. Integrita zdroje a samokontrola

Spojení šesti připnutých částí C++ zdroje má SHA-256

```text
cff060200d245d9888ae22a1cc0af9321d03f4f990118d16253d626ea74189d5
```

Samokontrola C++ a nezávislý Pythonový výpočet oba prošly a shodly se na
stavovém otisku

```text
eaa7bcbe93566b43.
```

```text
SELFTEST_ACTUAL.txt
  sha256 b091329be8d77ff30dff152f750b960c8ced43d56a2c21820d8c0ea975ef380e

REFERENCE_ACTUAL.txt
  sha256 b03760a2793506daf7b4defd50042e163dea32bface798945862a19f3f50fb32
```

Všechny čtyři zmrazené řetězce skončily s návratovým kódem nula, prázdným
stderr a přesně 256 vzorky. Jejich úplné obsahové otisky jsou v
`PILOT_RUNS.tsv`; souhrnné koncové řádky jsou v `PILOT_SUMMARIES.txt`.

## 2. Předem stanovená zkouška míchání

Na `L=6` se horký a studený počátek shodly ve všech čtyřech předem určených
ukazatelích. Největší hot/cold odchylka byla u `logw`, přibližně

```text
z=1.1994.
```

Na `L=8` prošly lokální veličiny `logw`, vírová hustota a monopolová hustota,
ale Polyakovův poloměr selhal:

```text
cold mean = 0.228602994276
hot  mean = 0.142222342979
combined z = 54.6557684643
```

Přitom předem zmrazený odhad účinné velikosti vzorku dal

```text
ESS cold = 197.15
ESS hot  = 256.00.
```

Řetězce jsou tedy uvnitř zachycených oblastí krátce korelované, ale jejich
globální Polyakovův mód se nesmíchal mezi horkým a studeným počátkem. Pilotní
podmínka `z<=4` je porušena o více než řád.

Předem zmrazený analyzátor proto vrátil

```text
PILOT_FAILURES hot_cold_L8_polyakov_radius
RESULT STOP_MIXING_OR_INTEGRITY
```

`PILOT_ANALYSIS.txt` má SHA-256

```text
ba9ed1217cedf06468bc2ce2a2ba405e593874f73cc53509f525d81cb287c775.
```

## 3. Následná diagnóza, nikoli další brána

Po odpálení STOP byla pouze diagnosticky prohlédnuta již vzniklá data. Na
`L=8` měl horký řetězec také nenulovou lichou orientační stopu

```text
score_mean hot  =  0.0134293654537
score_mean cold = -0.0000108767027
```

a viditelnou nerovnováhu mezi toky `f=1` a `f=4`. To je slučitelné s
nepromíchaným globálním orientačním nebo doménovým módem. Není to předem
zaregistrovaný rozhodovací ukazatel a není z toho vyvozena fáze ani příčina.

## 4. Dodatečně nalezená přesnostní mezera

Pilotní přechod počítá všech pět lokálních vah přesně v `Z[phi]`, ale používá
jeden rovnoměrný 64bitový tah `r` a rozhoduje nerovností

```text
r S < 2^64 C.
```

To odstraňuje desetinné zaokrouhlení algebraických mezí, ale nevzorkuje obecné
algebraické pravděpodobnosti přesně. Kumulativní pravděpodobnost je zaokrouhlena
na násobek `2^-64`. Chyba jednoho kroku je nepatrná, avšak tvrzení
`EXACT_PHI_HEATBATH` je doslova příliš silné.

Tento nález nezakládá tvrzení, že způsobil pozorovaný Polyakovův nesoulad.
Zakládá samostatný integritní důvod, proč pilot nelze povýšit ani při lepším
míchání.

## 5. Povinná dispozice

První pilot se nepřepisuje a neopakuje pod stejným pinem. Produkce zůstává
blokována.

Následnický pilot musí před během zmrazit nejméně:

```text
N1  přesný bitový intervalový výběr algebraických kategorií s téměř jistým
    ukončením, nikoli pevné 64bitové zaokrouhlení
N2  ne-lokální, míru zachovávající aktualizaci Polyakovových módů
N3  výslovné globální charge-conjugation a flat-holonomy kontroly
N4  delší hot/cold zkoušku na L=8 s předem danou mezí
N5  stejnou nulovou důkazní váhu až do průchodu mícháním
```

Přirozený kandidát pro `N2` je přesná tepelná lázeň celé neuzavíratelné
Polyakovovy linky: společně posune všech `L` linků jedné periodické čáry,
spočítá pět úplných vah dotčené trubice a vybere jednu přesným bitovým
intervalovým algoritmem. Tento krok může měnit poloměr Polyakovova průměru,
na rozdíl od pouhého globálního plochého posunu, který mění jen jeho fázi.

## 6. Terminální verdikt

```text
KERNEL SELFTESTS                PASS
INDEPENDENT TRANSITION CHECK    PASS for frozen deterministic fixture
FOUR CHAINS EXECUTION           PASS
L6 HOT/COLD MIXING              PASS
L8 LOCAL OBSERVABLE MIXING      PASS under frozen pilot checks
L8 POLYAKOV MIXING              FAIL
EXACT TARGET HEATBATH CLAIM     FAIL after post-run audit
PHASE EVIDENCE                  NONE
PRODUCTION                      BLOCKED
RESULT                          STOP_MIXING_OR_INTEGRITY
```
