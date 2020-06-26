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

    def getReps(self):
        return self.reps

class ExcerciseBlock(models.Model):
    repsNumber = models.IntegerField()
    breakTime = models.IntegerField()
    excercise = models.ManyToManyField(ExcerciseSet)
    block = []
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

