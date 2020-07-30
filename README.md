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

