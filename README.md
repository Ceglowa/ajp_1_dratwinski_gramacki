# Zadanie 1
## Zestawienie środowiska do analizy morfo-syntaktycznej języka polskiego

### Budowa własnego segmentatora

W ramach zadania zaproponowano implementację prostego segmentatora hierarchicznego dzielącego tekst na zdania i wyrazy. Zastosowano podejście regułowe.

#### Podział na zdania

Zdania wyodrębnione są za pomocą 3 znaków: [.!?]. Dodatkowo zdefiniowano reguły opisujące sytuację, kiedy te znaki nie oznaczają końca zdania:

* brak spacji po znaku przestankowym [.!?]
* znajdują się na końcu jednego ze skrótów zdefiniowanych w segmentatorze (przykładowo: itp. itd. ur.)

#### Podział na słowa

Słowa znajdowane są w dwóch krokach. Początek słowa to pierwszy znak będący literą lub cyfrą. Koniec słowa zdefiowany jest jako pierwszy po początku znak nie będący jednym z powyższych. Dodatkowo jeżeli pomiędzy dwoma znakami należącymi do słowa znajduje się coś innego niż spacja, nie następuje w tym miejscu podział. Przykład działania segmentatora przedstawiono poniżej.

##### Tekst wejściowy

Albert Einstein (ur. 14 marca 1879 w Ulm, zm. 18 kwietnia 1955 w Princeton) – fizyk teoretyczny i laureat Nagrody Nobla w dziedzinie fizyki za 1921 rok, w uznaniu za „wkład do fizyki teoretycznej, zwłaszcza opis prawa efektu fotoelektrycznego”. Twórca szczególnej teorii względności i autor wynikającej z niej równoważności masy i energii, sformułowanej słynnym wzorem E=mc2. Twórca ogólnej teorii względności i opartych na niej pierwszych modeli kosmologicznych oraz przewidywań dotyczących fal grawitacyjnych. Współtwórca teorii fotonu i dualizmu korpuskularno-falowego światła, a przez to mechaniki kwantowej. Jednocześnie – czołowy krytyk jej najczęstszej, kopenhaskiej interpretacji i współautor paradoksu EPR. Odkrywca emisji wymuszonej, statystyki Bosego-Einsteina i możliwości istnienia kondensatu Bosego-Einsteina. Zwykle jest uznawany za niemieckiego fizyka żydowskiego pochodzenia.

##### Wynik działania segmentatora

```json
[
   {
      "text":"Albert Einstein (ur. 14.03.1879 w Ulm, zm. 18.04.1955 w Princeton) – fizyk teoretyczny i laureat Nagrody Nobla w dziedzinie fizyki za 1921 rok, w uznaniu za „wkład do fizyki teoretycznej, zwłaszcza opis prawa efektu fotoelektrycznego”.",
      "words":[
         "Albert",
         "Einstein",
         "ur",
         "14.03.1879",
         "w",
         "Ulm",
         "zm",
         "18.04.1955",
         "w",
         "Princeton",
         "fizyk",
         "teoretyczny",
         "i",
         "laureat",
         "Nagrody",
         "Nobla",
         "w",
         "dziedzinie",
         "fizyki",
         "za",
         "1921",
         "rok",
         "w",
         "uznaniu",
         "za",
         "wkład",
         "do",
         "fizyki",
         "teoretycznej",
         "zwłaszcza",
         "opis",
         "prawa",
         "efektu",
         "fotoelektrycznego"
      ]
   },
   {
      "text":"Twórca szczególnej teorii względności i autor wynikającej z niej równoważności masy i energii, sformułowanej słynnym wzorem E=mc2.",
      "words":[
         "Twórca",
         "szczególnej",
         "teorii",
         "względności",
         "i",
         "autor",
         "wynikającej",
         "z",
         "niej",
         "równoważności",
         "masy",
         "i",
         "energii",
         "sformułowanej",
         "słynnym",
         "wzorem",
         "E=mc2"
      ]
   },
   {
      "text":"Twórca ogólnej teorii względności i opartych na niej pierwszych modeli kosmologicznych oraz przewidywań dotyczących fal grawitacyjnych.",
      "words":[
         "Twórca",
         "ogólnej",
         "teorii",
         "względności",
         "i",
         "opartych",
         "na",
         "niej",
         "pierwszych",
         "modeli",
         "kosmologicznych",
         "oraz",
         "przewidywań",
         "dotyczących",
         "fal",
         "grawitacyjnych"
      ]
   },
   {
      "text":"Współtwórca teorii fotonu i dualizmu korpuskularno-falowego światła, a przez to mechaniki kwantowej.",
      "words":[
         "Współtwórca",
         "teorii",
         "fotonu",
         "i",
         "dualizmu",
         "korpuskularno-falowego",
         "światła",
         "a",
         "przez",
         "to",
         "mechaniki",
         "kwantowej"
      ]
   },
   {
      "text":"Jednocześnie – czołowy krytyk jej najczęstszej, kopenhaskiej interpretacji i współautor paradoksu EPR.",
      "words":[
         "Jednocześnie",
         "czołowy",
         "krytyk",
         "jej",
         "najczęstszej",
         "kopenhaskiej",
         "interpretacji",
         "i",
         "współautor",
         "paradoksu",
         "EPR"
      ]
   },
   {
      "text":"Odkrywca emisji wymuszonej, statystyki Bosego-Einsteina i możliwości istnienia kondensatu Bosego-Einsteina.",
      "words":[
         "Odkrywca",
         "emisji",
         "wymuszonej",
         "statystyki",
         "Bosego-Einsteina",
         "i",
         "możliwości",
         "istnienia",
         "kondensatu",
         "Bosego-Einsteina"
      ]
   }
]
```


### Porównanie tagerów na danych z konkursu PolEval 2017

Do porównania wybrano 3 tagery:

* MorphoDita
* WCRFT2
* KRNNT

Porównania dokonywano na danych z edycji 2017 konkursu PolEval ([link](http://2017.poleval.pl/index.php/tasks/)). Ze względu na użycie tagerów dostępnych przez API, a w związku z tym pracujących na surowym tekście, wykorzystano dane do zadania c. Korzystano z danych testowych, ponieważ niektóre z testowanych tagerów brały udział w konkursie, a co za tym idzie mogły być budowane na danych treningowych.

Ewaluacji dokonano korzystając ze skryptu ewaluacyjnego udostępnionego w ramach konkursu PolEval ([link](http://2017.poleval.pl/task1/tagger-eval.py))

Dodatkowo tager KRNNT zwracał dane w nieobsługiwanym przez ewaluator, dlatego konieczne było napisanie parsera do formatu ccl ([code](utils/converter.py))

#### Wyniki

Wyniki ewaluacji przedstawiono w tabeli poniżej.

| Tager | POS Accuracy | Lemmatization Accuracy | Overall accuracy |
| --- | ---: | ---: | ---: |
| KRNNT | 92.6242% | 97.0431% | 94.8337% |
| MorphoDita | 89.7979% | 96.4917% | 93.1448% |
| WCRFT2 | 64.5684% | 90.7122% | 77.6403% |


### Porównanie tagerów jako narzędzi do preprocessingu w zadaniu klasyfikacji tekstów

Testowane powyżej tagery zostały wykorzystane do ekstrakcji cech z dokumentów tekstowych na potrzeby problemu klasyfikacji. Korzystając z oznaczeń gramatycznych tagerów budowano reprezentację *bag-of-words* wykorzystywaną później przez klasyfikator bayesowski (implementacja *MultinomialNB* z pakietu *scikit-learn*).

#### Dane

Do klasyfikacji wykorzystano korpus Wikipedii w języku polskim dostępny w CLARIN-PL. Zawiera on ~9,5 tys. tekstów z 34 tematów i podzielony jest na zbiór treningowy i testowy. 

#### Proces przetwarzania tekstów

Przygotowanie reprezentacji tekstu w postaci wektora było realizowane w następujący sposób:

1. Analiza z wykorzystaniem tagera dokonującego segmentacji, wydobycia form bazowych wyrazów oraz oznaczenia części mowy.

1. Filtrowanie wyrazów do części mowy. Przetestowano trzy warianty:

    * rzeczowniki (tagi: *subst*, *depr*, *ger*)
    * czasowniki (tagi: *fin*, *praet*, *impt*, *imps*, *inf*)
    * przymiotniki i imiesłowy przymiotnikowe (tagi: *adj*, *adja*, *adjp*, *adjc*, *pact*, *ppas*)
    
1.  Kodowanie do reprezentacji *bag-of-words* z wykorzystaniem klasy *CountVectorizer* z pakietu *scikit-learn* 

#### Wyniki klasyfikacji

Porównanie skuteczności klasyfikatorów przedstawiono w tabeli poniżej.

| | Nouns | Verbs | Adjectives |
|---|---:|---:|---:|
|KRNNT| 87% | 43% | 76% |
|MorphoDita| 87% | 43% | 77% |
|wcrft2| 87% | 42% | 77% |

Dobrór tagera nie miał wpływu na jakość działania klasyfikatora. Duże znaczenie miał natomiast dobór części mowy. Zdecydowanie najlepsze rezultaty osiągnięto stosując rzeczowniki. Pokrywa się to z oczekiwaniami, ponieważ to rzeczowniki wużyte w tekście wydają się mieć największy związek z tematyką tekstu. Ciekawy jest wysoki wynik klasyfikacji z wykorzystaniem przymiotników. Słaba skuteczność czasowników może wynikać z dużej liczby tych wyrazów powtarzających się w większości tekstów przez co nie wnoszą one rozróżnienia między tematami.
