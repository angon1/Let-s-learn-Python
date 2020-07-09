from django.db import models

# Create your models here.

class Excercise(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class ExcerciseSet(models.Model):
    reps = models.IntegerField()
    # usedExcercise = models.ManyToManyField(Excercise)
    usedExcercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, null=True)
    # ExcerciseSet -> powinien być obiekt składający się z tych danych:
    # {excercise, repsy, przerwa}
    def getReps(self):
        return self.reps    #przenieść do blocks

class ExcerciseBlock(models.Model):
    repsNumber = models.IntegerField()      #przenieść do treningu
    breakTime = models.IntegerField()
    excercise = models.ManyToManyField(ExcerciseSet)
    block = []
    # ExcerciseBlock to powinien być obiekt składający się z: przerwy po bloku i listy ExcerciseSet
    #   [ExcerciseSet, ExcerciseSet, ExcerciseSet     ]
    name = models.TextField()

#TU MUSZĘ OGARNĄĆ JAK TO ZROBIĆ
    # def addExcercise(self, name, reps):
    #     self.excercise.append(ExcerciseSet(name, reps))

    def getRepsNumber(self):
        return self.repsNumber

    def getBreakTime(self):
        return self.breakTime
    
    def getExcercises(self):
        return self.excercise


    def returnMe(self):
        self.block = [name, repsNumber, breakTime, excercise]
        return self.block

    def __str__(self):
        return self.name

class Training(models.Model):
    blocks = models.ManyToManyField(ExcerciseBlock)
    name = models.TextField()
    #Training to powinien być obiekt składający się z:
    # Listy bloków z powtórzeniami (jak blok ID jest na liście x razy, to liczymy że "powtarza się 3 razy")
    #

    # def addBlock(self):
        # self.repsNumber = int(input("Podaj liczbę powtorzeń bloku cwiczen: \n"))
        # self.breakTime = int(input("Podaj czas przerwy między powtórzeniami bloku: \n"))
        # self.blocks.append(ExcerciseBlock(self.repsNumber, self.breakTime))
        # while 0 == 0:
        #     self.name = input("Wprowadź nazwe cwiczenia. Jesli nie chcesz dodawac cwiczen do bloku, wpisz 0: \n")
        #     if "0" == self.name:
        #         break
        #     self.reps = int(input("Wprowadź liczbę powtórzeń: "))
        #     self.blocks[-1].addExcercise(self.name, self.reps)
        # print("Blok dodany")

    def __str__(self):
        return self.name

