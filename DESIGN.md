# Dino Odkrywca – projekt (etap 1)

Wersja tekstowa strony projektu. Makiety ekranów są na stronie w Claude (artefakt „Dino Odkrywca”).

Dino Odkrywca

Apka dla 3-latka · iPad · projekt do komentarzy

# Dino Odkrywca

Dziecko wykopuje skamielinę, ożywia dinozaura, poznaje jego głos, jedzenie i wielkość, a potem bawi się z nim w krótką gierkę. Trzy dinozaury na start: Tyranozaur, Triceratops i Brachiozaur.

iPad poziomoPWA, offlinePolski lektorGrafiki AI (Ty generujesz)Naklejki + blokada rodzicielskanazwa robocza – do zmiany

**Co jest w tym dokumencie** Pełny projekt: przepływ ekranów, makiety każdego ekranu, zasady rozgrywki, treści dla trzech dinozaurów, dźwięk, styl, lista assetów z gotowymi promptami oraz architektura techniczna. Na końcu są pytania, na które potrzebuję odpowiedzi przed etapem 2 (budowa).

1

## Założenia dla 3-latka

Trzylatek nie czyta, ma krótką uwagę (2–5 minut na aktywność), trafia palcem z dokładnością około 2 cm i frustruje się, gdy coś „nie działa”. Z tego wynikają twarde zasady, które obowiązują na każdym ekranie:

**Zero czytania**

Każdy przycisk to obrazek lub ikona. Tekst pojawia się tylko jako ozdoba, a wszystko istotne mówi lektor.

**Wielkie cele dotyku**

Minimum 120 pt (ok. 2,1 cm na iPadzie) dla każdego elementu klikalnego. Główne przyciski 180–220 pt.

**Nie da się przegrać**

Brak czasu, brak punktów, brak „źle”. Każde dotknięcie coś robi: dźwięk, ruch, błysk.

**Podpowiedź po 12 s**

Gdy dziecko nic nie robi, animowana rączka pokazuje, gdzie dotknąć, a lektor powtarza polecenie.

**Zawsze ta sama droga powrotu**

Biała okrągła strzałka w lewym dolnym rogu na każdym ekranie poza startowym.

**Nic nie znika przypadkiem**

Brak gestów wielopalcowych, brak przeciągania jako jedynej drogi. Reset i ustawienia tylko dla rodzica (przytrzymanie 3 s).

Jedna sesja zabawy to pętla: **wykopalisko → ożywienie → poznawanie → gierka → naklejka**. Trwa 4–6 minut dla jednego dinozaura, więc trzy dinozaury dają kwadrans „pierwszego przejścia”, a potem dziecko wraca do ulubionych gierek z albumu.

2

## Przepływ ekranów

Siedem ekranów, z czego dziecko widzi sześć. Strzałka „wróć” zawsze prowadzi o jeden krok wstecz, a z obozu na start. Odkryty dinozaur trafia do albumu, z którego można wejść w jego kartę bez ponownego kopania.

**E1 Start** logo, „Graj”, album

**E2 Obóz** 3 kopce wykopalisk

**E3 Wykopalisko** szczotkowanie kości

**E4 Ożywienie** szkielet → dinozaur

**E5 Karta dinozaura** głos, jedzenie, wielkość, ciekawostka

**E6 Gierka** inna dla każdego

**E7 Album** naklejki, powrót do E5

**E8 Rodzic** ukryte: dźwięk, reset

Kolejność E2 → E3 → E4 → E5 → E6 jest liniowa i prowadzona głosem, żeby dziecko nie musiało niczego wybierać poza tym, który kopiec kopie. Album (E7) i ustawienia (E8) są dostępne z E1 i E2.

3

## Ekrany – makiety

Makiety pokazują układ i wielkość elementów, nie finalną grafikę. Zielone kształty to miejsca na Twoje obrazki AI; przyciski i drobne elementy narysuję sam w SVG, żeby były ostre i animowalne. Proporcje 4:3 jak iPad w poziomie.

### E1 · Start

**E1.** Jeden wielki zielony przycisk. Po wejściu lektor: „Cześć! Zostań odkrywcą dinozaurów. Dotknij zielonego guzika.” Maskotka (mały odkrywca w kapeluszu) macha; brachiozaur w tle mruga. Ikona koła zębatego jest niewidoczna dla dziecka – reaguje tylko na przytrzymanie rogu ekranu przez 3 s.

### E2 · Obóz wykopaliskowy

**E2.** Trzy kopce ziemi z wystającą kością i chorągiewką. Lektor: „Gdzieś tu śpią kości dinozaurów. Dotknij kopca, żeby zacząć kopać.” Kopiec z odkrytym dinozaurem pokazuje jego naklejkę – dotknięcie prowadzi od razu do karty (E5). Nieodkryte kopce lekko „oddychają”, żeby przyciągać wzrok. Kolejność dowolna; dziecko wybiera samo.

### E3 · Wykopalisko

**E3.** Cała środkowa część to warstwa piasku (Canvas) narysowana na szkielecie. Przesuwanie palcem wyciera piasek pędzlem o dużej średnicy (ok. 90 pt), z sypiącymi się ziarenkami i dźwiękiem „szszsz”. Gdy odsłonięte jest 75% szkieletu, reszta piasku sama się rozsypuje (dziecko nie musi być dokładne), kości „wskakują” na miejsce z kliknięciem i lektor mówi: „Brawo! Znalazłeś wszystkie kości!”. Przejście do E4 następuje automatycznie po 1,5 s.

### E4 · Ożywienie

**E4.** Ekran bez przycisków – 4-sekundowa animacja nagrody. Szkielet unosi się, obłok kurzu, iskierki, i z chmury wyłania się kolorowy dinozaur, który robi krok i ryczy. Lektor: „To Tyranozaur!”. Potem automatycznie E5. Dotknięcie ekranu w trakcie nic nie psuje (pomija tylko do końca animacji).

### E5 · Karta dinozaura

**E5.** Cztery okrągłe przyciski w rogach (nie zasłaniają dinozaura) i jeden wielki „Zagraj”. Każdy przycisk uruchamia scenkę zamiast tekstu: _Głos_ – dino otwiera paszczę i ryczy (przycisk można klikać bez końca, to ulubione); _Jedzenie_ – z boku wjeżdża jego jedzenie, dino je gryzie i mlaska, lektor mówi jedno zdanie; _Wielkość_ – obok dinozaura staje maskotka-dziecko i coś znajomego (samochód, dom), dino wygląda na naprawdę wielkiego, lektor: „Tyranozaur był długi jak autobus!”; _Ciekawostka_ – jedno zdanie z lektorem i drobną animacją (np. T-rex macha malutkimi rączkami). Dziecko może dotknąć samego dinozaura – wtedy reaguje łaskotaniem (chichot, podskok).

### E6 · Gierka (przykład: Brachiozaur)

**E6.** Wspólny schemat wszystkich gierek: na ekranie jest 5 celów, każde dotknięcie daje natychmiastową reakcję dinozaura i dźwięk, po 5 trafieniach następuje mała fiesta (konfetti z liści, taniec dinozaura, fanfara) i lektor chwali. Potem cele pojawiają się od nowa, więc można grać w nieskończoność. Szczegóły trzech gierek w sekcji 4.

### E7 · Album naklejek

**E7.** Trzy miejsca na naklejki (rozmiar ok. 240 pt). Odkryte naklejki lekko się kołyszą; nieodkryte to szary cień ze znakiem zapytania – dotknięcie go przenosi do obozu (E2) na odpowiedni kopiec. Nowa naklejka „przylatuje” do albumu z animacją po pierwszym ukończeniu gierki.

### E8 · Panel rodzica

Ukryty za przytrzymaniem prawego górnego rogu przez 3 s (na E1 lub E2). Prosty biały panel z trzema przełącznikami: **lektor** (wł./wył.), **muzyka w tle** (wł./wył.), **głośność efektów** , oraz przycisk **Zacznij od nowa** z potwierdzeniem. Tekst jest tu dozwolony, bo to ekran dla dorosłego. Dodatkowo krótka instrukcja: jak włączyć „Dostęp nadzorowany” na iPadzie, żeby dziecko nie wyszło z apki.

4

## Mini-gry – jedna na dinozaura

Każda gierka uczy jednej rzeczy o dinozaurze (co je, jak się porusza, gdzie żył) i wymaga tylko dotykania. Żadna nie ma przegranej ani limitu czasu. Wspólna struktura: 5 celów → fiesta → nowa runda.

### Brachiozaur · „Listki z drzew”

Scena
    Brachiozaur stoi po lewej, po prawej dwa wysokie drzewa (araukarie) z pięcioma podświetlonymi kępkami liści na różnych wysokościach.
Ruch dziecka
    Dotknięcie kępki liści.
Reakcja
    Szyja wyciąga się do listka (animacja 0,6 s), „chrup”, listek znika, dino przeżuwa z zadowoloną miną; licznik na górze zapełnia jeden liść.
Fiesta
    Po 5 listkach brzuszek dinozaura lekko rośnie, dino robi „beknięcie” (dzieci to uwielbiają), z drzew sypią się liście-konfetti, lektor: „Brachiozaur jest najedzony! Jadł liście z samych czubków drzew.”
Czego uczy
    Długa szyja służy do sięgania wysoko; jadł rośliny.

### Triceratops · „Jajka w paprociach”

Scena
    Łąka z kępami paproci, w środku gniazdo z patyków. Triceratops-mama stoi obok gniazda i kiwa głową.
Ruch dziecka
    Dotknięcie kępy paproci – paprocie rozchylają się i wyskakuje jajko (w 5 z 7 kęp; w pozostałych motyl albo żaba, dla śmiechu).
Reakcja
    Jajko samo toczy się do gniazda (nie trzeba przeciągać), „plum”, mama sapie radośnie i macha kryzą.
Fiesta
    Po 5 jajkach wszystkie pękają i wychodzą maleńkie triceratopsy, piszczą i tuptają wokół mamy. Lektor: „Triceratopsy żyły w rodzinach i pilnowały swoich jajek.”
Czego uczy
    Dinozaury wykluwały się z jaj; triceratops był łagodnym roślinożercą i żył w stadzie.

### Tyranozaur · „Wielkie kroki”

Scena
    Ścieżka przez las nad rzeką, T-rex stoi po lewej. Na ścieżce pojawia się po jednym świecącym śladzie stopy.
Ruch dziecka
    Dotknięcie śladu.
Reakcja
    T-rex robi ciężki krok w to miejsce: „BUM”, ekran lekko drży, z drzew zrywają się ptaki, z kałuży pryska woda. Pojawia się kolejny ślad. Lektor liczy kroki: „Jeden… dwa… trzy…”.
Fiesta
    Po 5 krokach T-rex dochodzi do polany, staje, otwiera paszczę i ryczy tak, że liście lecą z drzew, a dziecko może „ryczeć razem” naciskając ekran. Lektor: „Tyranozaur miał wielkie nogi i tupał tak, że drżała ziemia!”
Czego uczy
    Był ogromny i ciężki, chodził na dwóch nogach; przy okazji liczenie do pięciu.

**Do decyzji** Celowo omijam polowanie w gierce T-rexa – dla 3-latka „tupanie i ryczenie” jest równie ekscytujące, a nie budzi lęku. Na karcie E5 jedzenie T-rexa pokazuję jako wielki rysunkowy udziec (jak z kreskówek), bez ofiar. Daj znać, jeśli wolisz inaczej.

5

## Treści o dinozaurach

Wszystko, co mówi lektor, mieści się w jednym prostym zdaniu. Liczby zamieniam na porównania, które 3-latek zna z podwórka. Fakty są zgodne z aktualną wiedzą, ale uproszczone.

### Tyranozaur (T-rex)

Powitanie
    „To Tyranozaur! Król dinozaurów.”
Głos
    Niski, głęboki ryk przechodzący w warkot. „Tyranozaur ryczał najgłośniej ze wszystkich.”
Jedzenie
    Mięso (rysunkowy udziec). „Tyranozaur jadł mięso. Miał zęby wielkie jak banany!”
Wielkość
    Obok: dziecko-maskotka i autobus. „Był długi jak autobus i wysoki jak dom.”
Ciekawostka
    Macha malutkimi rączkami. „Miał ogromne nogi, ale rączki maleńkie – nie sięgał nimi nawet do pyszczka!”
Siedlisko (tło)
    Gęsty las nad rzeką, ciepłe popołudniowe światło.
Kolor
    Ciepły rdzawy brąz z kremowym brzuchem, ciemniejsze pasy na grzbiecie.

### Triceratops

Powitanie
    „To Triceratops! Ma trzy rogi.”
Głos
    Głębokie sapnięcie i pomruk jak u nosorożca. „Triceratops sapał i pomrukiwał.”
Jedzenie
    Paprocie i krzaki. „Triceratops jadł rośliny – paprocie i krzaczki – i miał dziób jak papuga!”
Wielkość
    Obok: dziecko i samochód osobowy. „Był ciężki jak dwa słonie i dłuższy niż samochód.”
Ciekawostka
    Kryza błyska kolorami. „Ta wielka tarcza na głowie to kryza – chroniła szyję i była bardzo kolorowa.”
Siedlisko (tło)
    Słoneczna łąka z paprociami i kwiatami, w tle góry, poranek.
Kolor
    Zielono-oliwkowy z pomarańczowo-żółtą kryzą i jasnym brzuchem.

### Brachiozaur

Powitanie
    „To Brachiozaur! Ma najdłuższą szyję.”
Głos
    Łagodne, niskie trąbienie (jak daleki róg). „Brachiozaur trąbił cicho i łagodnie.”
Jedzenie
    Liście z czubków drzew. „Brachiozaur jadł liście z samych czubków drzew – przez cały dzień!”
Wielkość
    Obok: dziecko i czteropiętrowy dom. „Był wysoki jak dom z czterema piętrami!”
Ciekawostka
    Szyja unosi się nad chmurkę. „Jego szyja była dłuższa niż cały autobus.”
Siedlisko (tło)
    Jezioro z wysokimi araukariami, delikatna mgła, ciepłe światło zachodu.
Kolor
    Miękka niebieskoszara zieleń z jaśniejszym brzuchem i delikatnymi cętkami.

Łatwo dodać kolejne dinozaury: każdy to jeden wpis w pliku danych (nazwa, 5 zdań, 4 obrazki, nazwa gierki) plus kopiec w obozie. Stegozaur i Pterodaktyl to naturalni kandydaci na wersję 2.

6

## Dźwięk i głos

Dźwięk robi w tej apce połowę roboty, bo dziecko nie czyta. Trzy warstwy:

Warstwa| Jak zrobione| Uwagi  
---|---|---  
**Lektor**|  Web Speech API, głos `pl-PL` systemowy (na iPadzie „Zosia”, w Chrome „Google polski”). Wszystkie kwestie w jednym pliku tekstowym, łatwo je edytować.| iPad wymaga pierwszego dotknięcia zanim zacznie mówić – dlatego E1 ma jeden guzik. Głos syntezowany jest poprawny, ale nie ciepły; w każdej chwili można podmienić na Twoje nagrania (te same nazwy kwestii).  
**Głosy dinozaurów**|  Syntezowane w Web Audio: T-rex = niski piłokształtny ton z opadającą wysokością, szumem i przesterem; Triceratops = krótkie „sapnięcia” z filtrowanego szumu i basu; Brachiozaur = łagodny glissando sinusa z pogłosem.| Każdy ryk ma losowe drobne różnice, więc nigdy nie brzmi identycznie. Zero plików do pobrania. Jeśli znajdziesz ładne nagrania, podmiana to jedna linijka.  
**Efekty i muzyka**|  Krótkie syntetyczne „popy”, dzwonki, chrupnięcia, tupnięcia, fanfara z 4 nut. Muzyka w tle: cicha, wolna pętla marimba + flet (syntezowana), domyślnie włączona, wyłączana w panelu rodzica.| Efekty są zawsze o połowę cichsze od lektora, żeby polecenia było słychać.  
  
7

## Styl graficzny

Kierunek: ręcznie malowana kreskówka z lat 90. – miękkie, nasycone kolory, wyraźne, zaokrąglone sylwetki, duże wyraziste oczy, ciepłe światło. Dinozaury są _przyjazne i pucołowate_ , nawet T-rex – groźny jest co najwyżej „na niby”. Żadnych ostrych zębów w zbliżeniu, żadnej krwi, żadnych ciemnych scen.

### Paleta

__#F5A524 słońce · guziki

__#2F9E5B liść · „Graj”

__#4FB3C8 niebo

__#C4643A glina · T-rex

__#E9D6A8 piasek

__#5B3A1F kora · kontury

Zasady dla interfejsu: przyciski to okrągłe „cukierki” z grubym dolnym cieniem (wciskają się przy dotknięciu), ikony białe lub ciemnobrązowe, bez cienkich linii. Napisy ozdobne krojem zaokrąglonym (Fredoka – ten sam co nagłówki tej strony). Tła mają zawsze spokojną dolną jedną trzecią, żeby dinozaur i przyciski nie ginęły w szczegółach.

### Maskotka

Mały odkrywca w za dużym kapeluszu safari, z pędzelkiem – roboczo **Kostek** (od „kości”). Pojawia się na starcie, przy porównaniu wielkości i w podpowiedziach (rączka wskazująca). Jeśli chcesz, może to być postać przypominająca Twojego syna – wtedy potrzebuję 2–3 słów opisu (kolor włosów, ulubiony kolor koszulki).

8

## Assety i prompty do generatora

Podział pracy: Ty generujesz **19 obrazków** według poniższych promptów i wrzucasz je do folderu `D:\01_AI\personal_dinogame\assets\` pod podanymi nazwami. Ja robię resztę: wycinam pozy z arkuszy, usuwam tła, robię naklejki, przyciski, liście, jajka, ślady, obiekty do porównania wielkości, ikony i wszystkie animacje. Do czasu dostarczenia obrazków apka działa na moich zastępczych rysunkach SVG, więc etap 2 nie musi czekać.

**Trzy triki, które oszczędzą Ci godzin**

**Arkusze postaci zamiast pojedynczych póz.** Jeden obrazek z czterema pozami w siatce 2×2 daje spójnego dinozaura – generatory nie potrafią powtórzyć postaci między osobnymi obrazkami. Ja pokroję arkusz na sprite'y.

**Jednolite białe tło, nie „przezroczyste”.** Generatory kłamią o przezroczystości. Proś o płaskie białe tło bez cienia na ziemi – usunę je automatycznie.

**Generuj kilka wariantów, wybieraj jeden.** Zwykle 1 z 4 propozycji jest dobra. Ważne: paszcza zamknięta w pozie „idle”, całe ciało w kadrze, bok prawy (dinozaur patrzy w prawo).

### Wspólny opis stylu

Ten fragment jest na końcu każdego promptu jako `{STYL}`. Jeśli generator ma pole „stylu” lub referencji, wklej go tam raz.

**{STYL}**
    
    
    hand-painted 2D cartoon illustration in the style of 1990s Disney animated films (The Lion King, Tarzan era), warm saturated colors, soft painterly shading, bold rounded shapes, cute and friendly, children's picture book look, no text, no letters, no watermark, no signature

Midjourney: dodaj na końcu `--ar 4:3 --no text, letters, watermark, blur, scary, blood` (dla arkuszy `--ar 1:1`). ChatGPT / DALL-E / Ideogram: wklej cały prompt jak leci, a proporcje wybierz w interfejsie (poziomo 4:3 dla teł, kwadrat dla arkuszy).

### Tabela assetów

Plik| Co to| Format| Gdzie użyte  
---|---|---|---  
`bg_start.jpg`| tło ekranu startowego| 2048×1536| E1  
`bg_camp.jpg`| obóz wykopaliskowy| 2048×1536| E2  
`bg_dig.jpg`| piaszczysty dół z góry| 2048×1536| E3  
`bg_trex.jpg`| las nad rzeką| 2048×1536| E4, E5, E6 T-rex  
`bg_trice.jpg`| łąka z paprociami| 2048×1536| E4, E5, E6 Triceratops  
`bg_brachio.jpg`| jezioro z araukariami| 2048×1536| E4, E5, E6 Brachiozaur  
`bg_album.jpg`| drewniana tablica / kartka notesu| 2048×1536| E7  
`sheet_trex.png`| arkusz 4 póz T-rexa| 2048×2048, białe tło| wszędzie  
`sheet_trice.png`| arkusz 4 póz Triceratopsa| 2048×2048, białe tło| wszędzie  
`sheet_brachio.png`| arkusz 4 póz Brachiozaura| 2048×2048, białe tło| wszędzie  
`sheet_kostek.png`| arkusz 3 póz maskotki| 2048×2048, białe tło| E1, E5, podpowiedzi  
`skel_trex.png`| szkielet T-rexa| 2048×1536, białe tło| E3, E4  
`skel_trice.png`| szkielet Triceratopsa| 2048×1536, białe tło| E3, E4  
`skel_brachio.png`| szkielet Brachiozaura| 2048×1536, białe tło| E3, E4  
`food_meat.png`| rysunkowy udziec| 1024×1024, białe tło| E5 T-rex  
`food_fern.png`| kępa paproci| 1024×1024, białe tło| E5, E6 Triceratops  
`food_leaves.png`| gałązka z liśćmi| 1024×1024, białe tło| E5, E6 Brachiozaur  
`baby_trice.png`| mały triceratops z jajka| 1024×1024, białe tło| E6 Triceratops  
`icon.png`| ikona apki na ekran iPada| 1024×1024| ekran główny iPada  
  
### Prompty · tła (7)

**bg_start.jpg**
    
    
    Wide landscape background for a children's game: a lush prehistoric jungle valley at golden sunset, a friendly round volcano with a tiny puff of smoke far in the distance, giant ferns and palm trees framing the sides, a calm open grassy clearing filling the lower third of the image, no animals, no characters, {STYL}

**bg_camp.jpg**
    
    
    Wide landscape background for a children's game: a cozy paleontologist camp in a sunny desert canyon, a small beige tent and a cute rounded jeep on the left, wooden crates and a shovel, red rock cliffs in the background, wide empty flat sandy ground filling the lower half of the image (dig sites will be added later), no animals, no characters, {STYL}

**bg_dig.jpg**
    
    
    Top-down view of a shallow rectangular excavation pit in warm golden sand for a children's game, soft painted sand texture with a few small pebbles near the edges, wooden plank border around the pit, the center of the pit is plain and empty, no bones, no animals, no characters, no tools, {STYL}

**bg_trex.jpg**
    
    
    Wide landscape background for a children's game: a dense prehistoric forest beside a gentle river, tall conifer trees and ferns, warm late afternoon light with sun rays, a wide flat forest path across the lower third of the image, calm and friendly mood, no animals, no characters, {STYL}

**bg_trice.jpg**
    
    
    Wide landscape background for a children's game: a sunny prehistoric meadow full of ferns and small colorful flowers, soft rolling hills and blue mountains in the distance, bright morning light, a wide open flat grassy area filling the lower third of the image, no animals, no characters, {STYL}

**bg_brachio.jpg**
    
    
    Wide landscape background for a children's game: a calm prehistoric lake with very tall araucaria trees on the right side, soft mist over the water, warm sunset sky with pink clouds, a wide flat sandy shore across the lower third of the image, no animals, no characters, {STYL}

**bg_album.jpg**
    
    
    Flat background for a children's sticker album: an open page of a paleontologist's field notebook made of warm cream paper with a subtle texture, a wooden desk visible around the edges, a small pencil and a magnifying glass in one corner, the center of the page is completely empty, no text, no drawings in the center, {STYL}

### Prompty · arkusze postaci (4)

**sheet_trex.png**
    
    
    Character sheet of a cute friendly Tyrannosaurus rex for a children's game, the same character shown four times in a 2x2 grid: top-left standing idle with closed mouth and a gentle smile, top-right roaring with mouth wide open, bottom-left mid-step walking with the left leg forward, bottom-right mid-step walking with the right leg forward. Full body, side view facing right, chubby proportions, big round expressive eyes, tiny stubby arms, warm rusty brown skin with a cream belly and darker stripes on the back, {STYL}, isolated on a plain flat white background, no ground shadow, each pose fully visible with empty space around it

**sheet_trice.png**
    
    
    Character sheet of a cute friendly Triceratops for a children's game, the same character shown four times in a 2x2 grid: top-left standing idle with closed beak and a gentle smile, top-right head raised with mouth open calling, bottom-left mid-step walking with the left legs forward, bottom-right mid-step walking with the right legs forward. Full body, side view facing right, chubby proportions, big round expressive eyes, three short rounded horns and a big colorful orange-yellow neck frill, olive green skin with a light belly, {STYL}, isolated on a plain flat white background, no ground shadow, each pose fully visible with empty space around it

**sheet_brachio.png**
    
    
    Character sheet of a cute friendly Brachiosaurus for a children's game, the same character shown four times in a 2x2 grid: top-left standing idle with the long neck raised and a gentle smile, top-right neck stretched up and forward with mouth open reaching for leaves, bottom-left mid-step walking with the left legs forward, bottom-right mid-step walking with the right legs forward. Full body, side view facing right, chubby proportions, big round expressive eyes, very long neck and small head, soft blue-grey-green skin with a lighter belly and gentle spots, {STYL}, isolated on a plain flat white background, no ground shadow, each pose fully visible with empty space around it

**sheet_kostek.png**
    
    
    Character sheet of a cute little child explorer for a children's game, about three years old, wearing an oversized beige safari hat, a green t-shirt and shorts, holding a small paint brush, the same character shown three times in a row: left standing and waving happily, middle pointing forward with one finger, right standing with hands on hips smiling proudly. Full body, front view, big round expressive eyes, {STYL}, isolated on a plain flat white background, no ground shadow, each pose fully visible with empty space around it

Jeśli maskotka ma przypominać Twojego syna, dopisz kolor włosów i ubranie – np. „short blond hair, red t-shirt with a dinosaur print”.

### Prompty · szkielety (3)

Szkielet ma mieć tę samą pozę co dinozaur w pozycji „idle” z arkusza (bok, patrzy w prawo, ogon za sobą), bo w E4 jeden przenika w drugi.

**skel_trex.png**
    
    
    Cartoon fossil skeleton of a Tyrannosaurus rex for a children's game, full body, side view facing right, standing idle pose with the tail stretched out behind and the head level, simplified friendly cartoon anatomy with thick rounded cream-white bones and soft shading, big empty eye socket, {STYL}, isolated on a plain flat white background, no ground shadow, whole skeleton visible with empty space around it

**skel_trice.png**
    
    
    Cartoon fossil skeleton of a Triceratops for a children's game, full body, side view facing right, standing idle pose on four legs with the tail stretched out behind, big skull with three horns and a wide frill, simplified friendly cartoon anatomy with thick rounded cream-white bones and soft shading, {STYL}, isolated on a plain flat white background, no ground shadow, whole skeleton visible with empty space around it

**skel_brachio.png**
    
    
    Cartoon fossil skeleton of a Brachiosaurus for a children's game, full body, side view facing right, standing idle pose on four legs with the very long neck raised and the tail stretched out behind, small skull, simplified friendly cartoon anatomy with thick rounded cream-white bones and soft shading, {STYL}, isolated on a plain flat white background, no ground shadow, whole skeleton visible with empty space around it

### Prompty · przedmioty i ikona (5)

**food_meat.png**
    
    
    A single big cartoon meat drumstick on a bone, like in classic cartoons, juicy and appetizing, rounded shapes, {STYL}, isolated on a plain flat white background, no ground shadow, centered

**food_fern.png**
    
    
    A single lush green fern bush with a few tiny pink flowers, rounded friendly shapes, {STYL}, isolated on a plain flat white background, no ground shadow, centered

**food_leaves.png**
    
    
    A single small tree branch with a round cluster of fresh green leaves, rounded friendly shapes, {STYL}, isolated on a plain flat white background, no ground shadow, centered

**baby_trice.png**
    
    
    A tiny cute baby Triceratops hatchling with a piece of eggshell on its head, chubby, big round eyes, tiny horn bumps, olive green with a light belly, side view facing right, {STYL}, isolated on a plain flat white background, no ground shadow, centered

**icon.png**
    
    
    App icon for a children's dinosaur game: a cute friendly Tyrannosaurus rex head smiling, front view, on a round bright sunny yellow badge with a thick white border, simple bold shapes readable at small size, {STYL}, no text, square format

9

## Technika · iPad i PWA

Cała apka to jeden plik `index.html` (HTML + CSS + JavaScript, bez frameworków i bez budowania) plus folder z Twoimi obrazkami, `manifest.json` i `sw.js`, dzięki którym Safari pozwala „dodać do ekranu głównego” i uruchamiać bez internetu.
    
    
    D:\01_AI\personal_dinogame\
      index.html      – cała apka
      manifest.json   – nazwa, ikona, orientacja pozioma, pełny ekran
      sw.js           – pamięć podręczna do pracy offline
      assets\         – Twoje obrazki (patrz tabela)
      DESIGN.md       – ten projekt w wersji tekstowej
      PROMPTS.md      – same prompty

Temat| Rozwiązanie  
---|---  
Rozdzielczość| Scena projektowana w stałym układzie 1024×768 pt i skalowana do ekranu (na iPadach 4:3 bez pasków; w przeglądarce na PC z paskami po bokach). Obrazki w 2× (2048 px) dla ekranu Retina.  
Dotyk vs mysz| Pointer Events – ten sam kod obsługuje palec na iPadzie i mysz w Chrome. Wyłączone: powiększanie szczypaniem, przybliżanie podwójnym dotknięciem, zaznaczanie tekstu, menu kontekstowe po przytrzymaniu.  
Orientacja| W manifeście `landscape`; jeśli iPad jest pionowo, apka pokazuje obrazek „obróć mnie” z animowanym iPadem.  
Dźwięk na iOS| Safari blokuje dźwięk do pierwszego dotknięcia – pierwsze dotknięcie „Graj” odblokowuje Web Audio i lektora, wszystko dalej gra bez przeszkód.  
Wykopalisko| Element `<canvas>` z warstwą piasku; palec „wyciera” piksele (tryb destination-out); postęp mierzony próbkowaniem co 200 ms.  
Animacje| CSS (oddychanie, mruganie, przyciski) + krótkie sekwencje w JavaScript (chód z 2 klatek, szyja, kroki). Sprite'y w PNG z przezroczystością wycięte z arkuszy.  
Postęp| `localStorage`: które dinozaury odkryte, ustawienia rodzica. Reset z panelu rodzica.  
Offline| Service worker cache'uje wszystko przy pierwszym uruchomieniu (ok. 15–25 MB z obrazkami).  
Instalacja na iPadzie| Otwierasz adres w Safari → Udostępnij → „Do ekranu początkowego”. Apka uruchamia się na cały ekran z własną ikoną. Do tego potrzebny jest adres https – patrz pytanie 5 poniżej.  
Blokada wyjścia| Instrukcja włączenia „Dostępu nadzorowanego” (Ustawienia → Dostępność) w panelu rodzica; to jedyny skuteczny sposób na iPadzie.  
  
10

## Pytania do Ciebie przed etapem 2

  * **Nazwa i imię.** „Dino Odkrywca” zostaje? Czy lektor ma witać syna po imieniu („Cześć, …!”) i czy maskotka ma go przypominać?
  * **Generator obrazków.** Midjourney, ChatGPT, czy coś innego? Dopasuję składnię promptów (parametry, proporcje) do tego narzędzia.
  * **Jedzenie T-rexa.** Rysunkowy udziec bez ofiar (moja propozycja), czy inaczej?
  * **Muzyka w tle.** Cicha pętla domyślnie włączona, czy w ogóle bez muzyki?
  * **Hosting dla iPada.** Najprościej: darmowe GitHub Pages (adres https, instalacja PWA działa). Alternatywa: serwer na Twoim PC w domowej sieci (bez https instalacja jest ograniczona). Masz konto GitHub?
  * **Kolejność kopców.** Dowolna (moja propozycja) czy wymuszona po kolei?
  * **Panel rodzica.** Wystarczy przytrzymanie rogu 3 s, czy wolisz dodatkowo proste zadanie „ile to 2+3” jak w innych apkach dziecięcych?



11

## Plan etapów 2 i 3

Etap 2a

**Szkielet apki**

Wszystkie ekrany, nawigacja, skalowanie, przyciski, lektor, zastępcze rysunki SVG. Klikalne w przeglądarce od razu.

Etap 2b

**Wykopalisko i ożywienie**

Canvas z piaskiem, postęp, animacja kości i przemiany, syntezowane ryki.

Etap 2c

**Karty i trzy gierki**

Scenki głos/jedzenie/wielkość/ciekawostka, „Listki”, „Jajka”, „Wielkie kroki”, album z naklejkami, panel rodzica.

Etap 2d

**Twoje obrazki + PWA**

Wycięcie sprite'ów z arkuszy, podmiana placeholderów, manifest, service worker, ikona.

Etap 3

**Testy**

Ja: automatyczne przeklikanie każdego ekranu w przeglądarce ze zrzutami. Ty: iPad z dzieckiem – dostaniesz krótką listę, na co patrzeć (czy trafia w przyciski, czy rozumie polecenia).

Po Twoich komentarzach zaktualizuję ten dokument i zaczynamy etap 2a – pierwsza klikalna wersja powstanie w folderze projektu, więc możesz ją otworzyć w przeglądarce od razu, zanim jeszcze będą obrazki.
