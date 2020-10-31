# Zadanie 1
## Zestawienie środowiska do analizy morfo-syntaktycznej języka polskiego

### Budowa własnego segmentatora

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

| Tager | Accuracy |
| --- | --- |

### Porównanie tagerów jako narzędzi do preprocessingu w zadaniu klasyfikacji tekstów
