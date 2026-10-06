# P-CONTACT-RECORD-1 — výsledek omezeného auditu

Status: PASS — dokončený místní omezený audit; veřejná dvouarchitekturní brána následuje.

První formální běh veřejně přijatého a přečteného pinu skončil exit 0,
prázdným stderr a přesnými 815 bajty v šesti řádcích EXPECTED.txt.
Otisk stdout: `a003c89fa6776a4679e0c81e3ffeed0b65cc96186480b6b7d7ddb104cae234d4`.
RUN.md obsahuje pin, prostředí a úplné vazby bajtů.

Splněny všechny původní omezené kontroly: úplné kontaktní a čtecí mapy,
jejich inverze, připravený pár i obsazený první registr, listová ochrana
prvního čtverce, minimální reference v určené třídě a negativní hranice.
Provedeno přesně 25000 doslovných kompozic na pěti pevných pístových párech,
225000 prefixových hranic druhé čtečky a 1000 připravených případů.
Úplné malé tabulky a symbolické afinní kontrakty mají počty uvedené
v EXPECTED.txt, shodné s nezměněnou preregistrací. Nejde o enumeraci X.
Žádný deklarovaný falsifikátor nebyl tímto během spuštěn.

Univerzální závěry nese samostatně přijatý původní písemný důkaz, nikoli
extrapolace pěti pístových svědků. Oba bity původního kontaktního kontraktu
zůstávají povoleny. Složení s T_alg není předmětem této sondy.
W_b, Ucal, příprava a čtení jsou deklarované předpoklady architektury.

Před veřejným přijetím výsledku musí stejný PR head projít x86_64, aarch64
a agregátem check, s byte-identical stdout a stejným balíkem.
Tato výpočetní evidence není provedením T_alg, společným v100 ani změnou
Canonu či vědeckého statusu vlastníka. Původní reporty zůstaly nezměněné.
