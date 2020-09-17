from django.db import models

# Create your models here.

class Excercise(models.Model):
    name = models.TextField()

    # def get_queryset(self):
    #     return self.model.objects.filter(name=self.request.name)

    def __str__(self):
        return self.name

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
    usedExcerciseSets = models.ManyToManyField(ExcerciseSet)

    def __str__(self):
        return ' break after block: {}\nsets count: {}'.format(self.breakTimeAfterBlock, self.usedExcerciseSets.count())

class Training(models.Model):
    blocks = models.ManyToManyField(ExcerciseBlock)
    name = models.TextField()
    #todo latwy sposob wyswietlenia cwiczen uzytych w treningu

    def __str__(self):
        return 'Training: {} Blocks count used: {}'.format(self.name, self.blocks.count())
