# Kontrola úplných nových důkazů před prvním spuštěním

2026-10-20. Nezávislý kontrolor nečetl primární verifier ani jeho
výstup. Nový vědecký program nebyl při této kontrole spuštěn.

## Přesně přečtené texty

- agents/spectrum_locality/PROOF_GLOBAL_SPECTRUM_AND_LOCALITY.md
- agents/spectral_lift/SPECTRAL_APPARATUS.md
- PREREG.md a CERTIFICATE_SCHEMA.md

## Výsledek analytické kontroly

Nebyla nalezena chyba vyžadující opravu. Kontrola se opírá o vlastní
odvození zaznamenané v INDEPENDENT_SPECTRUM_REVIEW.md, dále konkrétně
o následující prověření doplněných částí:

1. Cayleyův transformovaný operátor má správné znaménko. Pro
   theta=alpha-Arg(lambda) in (0,2pi) je K=cot(theta/2), takže
   (pi-alpha)-2atan(K)=theta-alpha=-Arg(lambda). Norma derivace
   arctan přes Laplaceův integrál je platná operatorová mez; nejde
   o nepřípustný obecný přechod ze skalární Lipschitzovy podmínky.

2. Annulární kontura má deklarovanou délku. Její kruhové části jsou
   alespoň rho od jednotkového spektra, radiální části nejméně
   sin(omega/2)=2rho. Podobnost omezenými exponenciálními vahami
   mění W nejvýše o exp(mu)-1=rho/2. Všechny konstanty resolventy,
   prostorového útlumu a časového šíření v rovnicích (10)-(16)
   spektrálního textu z toho vycházejí s uvedenými faktory.

3. Druhý globální spektrální shluk dává analytickou projekci P_-.
   Nerovnost A>=-P_- a přesné očekávání na s0 poskytují
   ||P_-s0||^2>=3cos(g/2)/5. Redukovaná resolventa má na tomto
   shluku modul alespoň 1/2, neboť |gamma-lambda|<=2. Tím skutečně
   plyne beta_->=3(1+sqrt(5))/80. Nejednoznačnost práce přežívá
   i požadavek exponenciálního prostorového útlumu a zachování
   přesné lokální energie vázané větve.

4. Přímý integrál baterie funguje také pro smíšené a singulárně
   spojité systémové spektrum. Konstrukce nepostuluje vlastní
   normované vektory spojité energie. Horní i dolní hranice
   baterie jsou zahrnuty a mají správnou rezervu h.

5. Znaménko pomocného Fourierova převodu posouvá baterii při
   E->E' o E-E'. Redukovaný kanál a chybové konstanty (14)-(21)
   jsou správné. Fourierova osa není falešným kanonickým
   samosdruženým časovým operátorem na konečném intervalu.

6. Dvojnásobná derivace vlastní rovnice dává správné znaménko
   <chi,H''chi>=kappa+2<chi',(H-g)chi'>. Nelze účtovat jen
   změnu vlastní hodnoty vázané větve po holém kopu.

7. Odhad polohového posunu (25) je platný i pro neomezenou
   polohu X: K_tau zachovává D(X), komutátor má mez
   2|tau| ||[H,X]|| a druhý moment p_L je konečný. To dává
   jak zachování potřebné domény na připraveném vstupu, tak
   odhad očekávání. Normalizace T=L=q nechává tento příspěvek
   v odezvě řádu q^-1.

8. Kladný Borelův logaritmus cílové jednotky V definovaný v plných
   vláknech dává omezený samosdružený K, který komutuje s H0.
   Htot=H0+K je proto autonomní generátor společného volného kroku
   a zásahu. Jeho interakční energie je výslovně započítána a
   samostatně zachována. Tato konstrukce nedodává přepnutí na
   další čistě volné kroky ani vnitřní zastavovací hodiny.

Konečný algebraický audit ověřuje celé vstupní maticové identity a
přesnou kladnost rezervy. Není náhradou těchto analytických důkazů
o nekonečných prostorech.
