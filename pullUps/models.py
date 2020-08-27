from django.db import models

# Create your models here.

class Excercise(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


    # ExcerciseSet -> powinien być obiekt składający się z tych danych:
    # {excercise, repsy, przerwa}
class ExcerciseSet(models.Model):
    repsCount = models.IntegerField()
    usedExcercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, null=True)
    breakTimeAfterSet = models.IntegerField()

    def getReps(self):
        return self.repsCount    #przenieść do blocks

    def __str__(self):
        return 'Used excercise:  {} reps:  {} break after set: {}'.format(self.usedExcercise, self.repsCount, self.breakTimeAfterSet)


# ExcerciseBlock to powinien być obiekt składający się z: przerwy po bloku i listy ExcerciseSet
#   [ExcerciseSet, ExcerciseSet, ExcerciseSet     ]
#    repsNumber = models.IntegerField()      #przenieść do treningu
class ExcerciseBlock(models.Model):
    breakTimeAfterBlock = models.IntegerField()
    usedExcerciseSet = models.ManyToManyField(ExcerciseSet)
    block = []
    countOfSets = models.IntegerField()

    def __str__(self):
        return 'Used excercise:  {} countOfSets:  {} break after block: {}'.format(self.usedExcerciseSet, self.countOfSets, self.breakTimeAfterBlock)

    # Czy ja dobrze rozumiem, że w django w modelach nie daje funkcji na add?
    # def blockAdd(self, breakTimeAfterBlock, ExcerciseSet)
    #     block.append([ExcerciseSet(repsSet, usedExcercise(name), breakTimeAfterSet), breakTimeAfterBlock])

#TU MUSZĘ OGARNĄĆ JAK TO ZROBIĆ
    # def addExcercise(self, name, reps):
    #     self.excercise.append(ExcerciseSet(name, reps))

    # def getRepsNumber(self):
    #     return self.repsNumber

    # def getBreakTime(self):
    #     return self.breakTime

    # def getExcercises(self):
    #     return self.excercise

    # def __str__(self):
    #     return self.name

class Training(models.Model):
    blocks = models.ManyToManyField(ExcerciseBlock)
    name = models.TextField()

    def __str__(self):
        return 'Training: {} Excercises {}'.format(self.name, blocks)
