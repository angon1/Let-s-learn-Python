# Let-s-learn-Python

Simple app to track pull up chalange.
Needed features:
1. Single training plan with:
  - number of sets, also with different rep/set
  - check-in button to automaticaly start break between sets
  - "Well done" message after completed training
2. Training plan for the whole training program.
3. Planning trainings in google calender. Updating the event after succesfuly finished training
4. Notifications when there is the time for the training.
5. Progression of the training

Co potrzebuję:

1. ćwiczenie
2. Serie - ile serii i jakiego ćwiczenia
3. Blok ćwiczeń
    - ile ćwiczeń w bloku
    - Ile serii danego ćwiczenia w bloku
    - Ile razy blok


### 31.05
1. Co zrobione:

- Dodane funkcje do tworzenia treningu, dodawania cwiczen
- Dodana funkcja do printowania treningu
- Test manualny

2. Napotkane problemy:
  - input - string to int
File "c:/python/Let-s-learn-Python/pullUps/training.py", line 24, in printMe
print("%s x %d" % (self.name, self.reps))
input z klawiatury w konsoli - znaleźć jak tu zmusić pythona, żeby liczby traktował jak liczby

Znalazłem rozwiązanie
reps = int(input(""))


3. Kolejne kroki: 02.06
- zainstalowac i przepiac sie na postgres  +
- poczytac jak django wykorzystuje templaty
- Zapis treningu do pliku (raport) - min
- Stworzenie bazy danych  +
- Funkcje do zapisu w bazie
- funkcje do odczytu z bazy
- Obsługa wielu treningów +
- Zapis treningów w kalendarzu googla +

3.1 Kolejne kroki: 11.06:
- Zrobić aplikację z tutoriala:
https://tutorial.djangogirls.org/pl/
- logowanie czasu w togglu



### 03.07
1. Co zrobione:

- Wstępnie uporządkowane modele:
  Struktury przygotowane, trzeba zrobic url i widoki i formularze do obslugi
- Porządkowanie pliku style.CSS:
  Dodałem kilka nowych klas (excercise_list, linksList, links) rzeby przygotować wstepny zarys konkretnego "widoku" - listy ćwiczeń.


2. Napotkane problemy:
  - Nie aktualizowaly się zmiany w plikach css:
Wyśrodkowanie container - done - po zmianach w pliku .css nie laduja sie zmiany na www ;/ -> znaleźć rozwiazanie
+Znalezione - trzeba kliknąć "disable cache" albo reloadować za pomocą "hard reload" - ctrl + shift + c
  -uladnic header i footer  --- w sumie, stopka jest ladna. Nie wiem co tam by dodać, bo nic nie potrzebuje poki co wiecej.




3. Kolejne kroki: 03.07
- dodać formularze, widoki i url do modeli
- Przenieść listę ćwiczeń ze strony głównej na osoby url


3.1 Kolejne kroki: 11.06:
- Zrobić aplikację z tutoriala:
https://tutorial.djangogirls.org/pl/
- logowanie czasu w togglu


### 10.08
1. Co zrobilem
- Przeniesienie listy do pliku index
- Zacząłem tworzyć templatki dla "Training" i podpinać pod to model. Do tego wszystkie widoki etc. Jest to cholernie czasochłonne i męczące. Nie ma dla tego jakiejś automatyzacji? xD


2. Napotkane problemy, wątpliwości etc
- Importowanie (przy formularzach na to wpadłem) - importuje pojedyncze formularze z pliku forms - czy da się gdzies ustawić "from plik import all"? - do sprawdzenia next time.



3. Co zrobić nastepnym razem - oraz kiedy?
- Wrzucenie obecnej apki w neta. Plan minimum
- Dokończyć templatki dla treningu i excercise set. Podpiąć odpowiednie formularze.
- Nauczyć się jak dobrze zrobić formularz z wieloma polami (np. excercise set: form dla cwiczenia, przerwy i powtórzeń i zapis 1 przyciskiem)
- Stworzyć formularze dla setów, bloków i treningów
- Kiedy: Po Spotkaniu produktywności we wtorek 11.08






20.08:

3. Co zrobić nastepnym razem - oraz kiedy?
-
- Dokończyć templatki dla treningu i excercise set i block Podpiąć odpowiednie formularze.
- Nauczyć się jak dobrze zrobić formularz z wieloma polami (np. excercise set: form dla cwiczenia, przerwy i powtórzeń i zapis 1 przyciskiem)  :)

- Stworzyć formularze dla setów, bloków i treningów
- Kiedy: Po Spotkaniu produktywności we wtorek 11.08



26.08:

Formularz bloku - zrobić obsługę nieskończonej pętli dodawania setów. Póki co jest tylko pojedynczy set i powtarzanie go. A tu mogą być różne sety. Po prostu podzielic na dwa formularze - jeden do dodawania przerwy po bloku, drugi - który będzie się renderował odpowiednią ilość razy - do wyboru setów.


10.09:




komendy na szybko:
heroku ps:scale web=1
git push heroku master
heroku logs --tail
heroku local
heroku run python manage.py migrate
