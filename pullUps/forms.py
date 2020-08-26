from django import forms
from .models import Excercise, Training, ExcerciseSet, ExcerciseBlock

class InputTrainingNameForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('name',)

class InputTrainingBlocksForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('blocks',)


class InputExcerciseForm(forms.ModelForm):

    class Meta:
        model = Excercise
        fields = ('name',)


class InputExcerciseSetForm(forms.ModelForm):

    class Meta:
        model = ExcerciseSet
        fields = ('repsCount', 'usedExcercise', 'breakTimeAfterSet')
        labels = {
            'repsCount': 'Powtorzenia',
            'usedExcercise': 'Ćwiczenie',
            'breakTimeAfterSet': 'Przerwa',
        }


class InputExcerciseBlockForm(forms.ModelForm):

    class Meta:
        model = ExcerciseBlock
        fields = ('breakTimeAfterBlock', 'usedExcerciseSet', 'countOfSets')
        labels = {
            'breakTimeAfterBlock': 'Przerwa po bloku',
            'usedExcerciseSet': 'set do bloku',
            'countOfSets': 'Ile powtorzen setu',
        }
    # repsCount = models.IntegerField()
    # usedExcercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, null=True)
    # breakTimeAfterSet = models.IntegerField()

    # class InputExcerciseForm(forms.ModelForm):

    # class Meta:
    #     model = Excercise
    #     fields = ('name',)
