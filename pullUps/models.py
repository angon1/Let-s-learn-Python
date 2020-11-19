from django.db import models
from pullUps.excercise.models import *

# Create your models here.



class ExcerciseSet(models.Model):
    repsCount = models.IntegerField()
    usedExcercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, null=True)
    breakTimeAfterSet = models.IntegerField()

    def getReps(self):
        return self.repsCount    #przenieść do blocks

    def __str__(self):
        return 'Used excercise:  {} reps:  {} break after set: {}'.format(self.usedExcercise, self.repsCount, self.breakTimeAfterSet)



class ExcerciseBlock(models.Model):
    breakTimeAfterBlock = models.IntegerField()
    usedExcerciseSets = models.ManyToManyField(ExcerciseSet, through='ExcerciseBlockSets', blank=True)

    def __str__(self):
        return ' break after block: {}\nsets count: {}'.format(self.breakTimeAfterBlock, self.usedExcerciseSets.count())

class ExcerciseBlockSets(models.Model):
    blockKey = models.ForeignKey(ExcerciseBlock, on_delete=models.CASCADE, unique=False)
    setKey = models.ForeignKey(ExcerciseSet, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return 'My id: {} ::: blockKey:  {}   - setKey {}\n'.format(self.pk, self.blockKey.pk, self.setKey.pk)

class Training(models.Model):
    blocks = models.ManyToManyField(ExcerciseBlock, unique=False)
    name = models.CharField(max_length=150)
    #todo latwy sposob wyswietlenia cwiczen uzytych w treningu

    def __str__(self):
        return 'Training: {} Blocks count used: {}'.format(self.name, self.blocks.count())
