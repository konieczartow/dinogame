# Dino Odkrywca — wygenerowane assety

## Status

Na razie powstała tylko jedna próbka T-rexa do akceptacji kierunku graficznego. Użytkownik ma zatwierdzić styl przed generowaniem pełnego zestawu 19 obrazków z `../PROMPTS.md`. Nie traktować próbki jako zaakceptowanego finalnego assetu ani gotowego arkusza animacji.

## Dostarczona próbka

- `preview/trex_idle_v01.png` — jeden T-rex, spokojna poza, zamknięta paszcza, całe ciało skierowane w prawo.
- `preview/trex_idle_v01.prompt.txt` — dokładny prompt użyty do generacji.
- Generator: wbudowane narzędzie `image_gen`; data: 2026-09-08.
- Rzeczywisty rozmiar wyjściowy: **1254 × 1254 px**, PNG RGB, bez kanału alfa. W promptcie zamówiono 2048 × 2048; narzędzie zwróciło mniejszą próbkę. Nie powiększano jej.
- Jasne, niemal białe tło jest częścią obrazu, nie przezroczystością. Przed integracją finalne sprite'y będą wymagały wycięcia i kontroli krawędzi.

## Ustalenia użytkownika

- Najpierw jeden duży T-rex do oceny wyglądu, później cały komplet po potwierdzeniu.
- Styl zgodny z dokumentem: klasyczna ręcznie malowana animacja 2D z lat 90., ciepłe nasycone kolory, miękkie cieniowanie, przyjazne i pucołowate postacie, nadal wyraźnie dinozaury.
- T-rex: rdzawobrązowy, kremowy brzuch, ciemniejsze pręgi, brązowe kontury.
- Maskotka Kostek ma przypominać dziecko użytkownika. **Opis wyglądu jeszcze nie został podany**; uzyskać go przed generowaniem maskotki.
- Nowe obrazy trzymać w tym osobnym folderze. Integracją z aplikacją zajmie się Claude.

## Wymagania kolejnego etapu

Lista i oryginalne nazwy 19 obrazów są w `../PROMPTS.md`; kontekst ekranów i paleta w `../DESIGN.md`. Docelowo: tła i szkielety 2048 × 1536; arkusze 2048 × 2048; przedmioty, mały triceratops i ikona 1024 × 1024. Każdy wynik sprawdzić pod kątem rzeczywistych wymiarów i formatu.

Arkusze dinozaurów: cztery równe ćwiartki 2 × 2: górna lewa idle, górna prawa roar, dolna lewa walk1, dolna prawa walk2. W każdej ćwiartce pełne ciało z zapasem, identyczna postać i skala, bez podpisów i linii podziału. Maskotka: trzy pozy w jednym rzędzie, więc wymaga osobnego podziału, a nie domyślnego cięcia 2 × 2.

Po akceptacji używać próbki jako odniesienia dla wyglądu, palety i kreski. Szkielety powinny odpowiadać sylwetce i pozie idle właściwego dinozaura. Przy animacji zachować wspólne płótno i poziom stóp, aby kolejne klatki nie zmieniały skali ani nie podskakiwały wskutek kadrowania.

`tools/cut_sheets.py` w katalogu projektu usuwa białe tło od brzegu i nadpisuje kanał alfa; nie uruchamiać go na gotowych przezroczystych sprite'ach bez dostosowania. Zamknięte białe przestrzenie, zwłaszcza między kośćmi, wymagają kontroli na kolorowym tle. Jasne kości nie powinny zlewać się z bielą.

Aplikacja korzysta z osobnych plików `trex_idle.png`, `trex_roar.png`, `trex_walk1.png`, `trex_walk2.png` i analogicznie dla `trice` oraz `brachio`; sama nie korzysta z arkuszy. Oczekuje finalnych obrazków w `assets/`. Przy podmianie grafiki sprawdzić wersję pamięci offline w `sw.js`, by iPad pobrał nowe pliki. `bg_dig.jpg` jest obecnie wykrywane w kodzie, lecz nie jest wyświetlane jako tło wykopu.

Kod aplikacji i dotychczasowy katalog `assets/` nie zostały zmienione w tym etapie.
