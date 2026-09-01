# Pilot raw-log disposition

Čtyři úplné textové výstupy mají dohromady 460639 bajtů. Nejsou ručně
přepisovány do této poznámky. Jejich obsahové otisky, počty bajtů a řádků jsou
v `PILOT_RUNS.tsv`; všechny rozhodné souhrnné řádky jsou v
`PILOT_SUMMARIES.txt`.

Úplné logy jsou deterministicky reprodukovatelné z neměnného pinu
`055c7cd3319a9d6c06dd2faef79dd1f2cb477eb8`, čtyř veřejných semen a příkazů v
`README.md`. Předem zmrazený analyzátor navíc zapisuje SHA-256 každého
vstupního logu přímo do `PILOT_ANALYSIS.txt`.

Tato dispozice neskrývá úspěšný výsledek: terminální výsledek je veřejný STOP.
Před jakýmkoli produkčním během musí následnický pilot uložit úplná surová data
v připnutém strojově čitelném formátu nebo jako neměnný běhový artefakt.
