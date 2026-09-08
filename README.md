# Dino Odkrywca

Apka o dinozaurach dla 3-latka (iPad, PWA). Jeden plik `index.html` – bez frameworków, bez budowania.

## Uruchomienie
* **Na komputerze:** otwórz `index.html` w Chrome/Edge (klikanie myszą działa jak dotyk). Lektor wymaga polskiego głosu w systemie.
* **Na iPadzie:** otwórz adres https apki w Safari → Udostępnij → „Do ekranu początkowego”. Działa offline po pierwszym uruchomieniu.
* Panel rodzica: przytrzymaj **lewy górny róg** przez 3 sekundy.

## Struktura
```
index.html      – cała apka (HTML + CSS + JS)
manifest.json   – nazwa, ikona, orientacja pozioma
sw.js           – pamięć podręczna offline
icons/          – ikony apki
assets/         – TWOJE obrazki (patrz PROMPTS.md); apka wykrywa je sama
tools/cut_sheets.py – tnie arkusze postaci 2×2 na sprite'y i usuwa białe tło
DESIGN.md / PROMPTS.md – projekt i prompty
```

## Własne obrazki
Wygeneruj obrazki według `PROMPTS.md` i wrzuć do `assets/`. Nazwy, których szuka apka:

| Plik | Użycie |
|---|---|
| `bg_start.jpg`, `bg_camp.jpg`, `bg_dig.jpg`, `bg_album.jpg` | tła ekranów |
| `bg_trex.jpg`, `bg_trice.jpg`, `bg_brachio.jpg` | siedliska (ożywienie, karta, gierka) |
| `trex_idle.png`, `trex_roar.png`, `trex_walk1.png`, `trex_walk2.png` | pozy T-rexa (wycięte z arkusza) |
| `trice_*.png`, `brachio_*.png` | analogicznie |
| `skel_trex.png`, `skel_trice.png`, `skel_brachio.png` | szkielety |
| `kostek_wave.png`, `kostek_point.png`, `kostek_idle.png` | maskotka |
| `food_meat.png`, `food_fern.png`, `food_leaves.png`, `baby_trice.png` | przedmioty |

Arkusze `sheet_*.png` (2×2) tnij skryptem: `python tools/cut_sheets.py assets/sheet_trex.png trex`.
Brakujące pliki są zastępowane rysunkami SVG wbudowanymi w apkę.

## Dodanie nowego dinozaura
W `index.html` znajdź `const DINOS = [` i dodaj wpis według wzoru (nazwa, zdania lektora, kolory, gierka).
Kopiec w obozie i miejsce w albumie pojawią się same. Rysunek SVG: dodaj funkcję w `ART` o tym samym `id`
(albo dostarcz obrazki `id_idle.png` itd.). Gierkę wybierasz z istniejących (`steps`, `eggs`, `leaves`) lub dopisujesz nową w `GAMES`.
