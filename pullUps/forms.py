from django import forms
from .models import Excercise, Training, ExcerciseSet

class InputTrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('name',)

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

    # repsCount = models.IntegerField()
    # usedExcercise = models.ForeignKey(Excercise, on_delete=models.CASCADE, null=True)
    # breakTimeAfterSet = models.IntegerField()

    # class InputExcerciseForm(forms.ModelForm):

    # class Meta:
    #     model = Excercise
    #     fields = ('name',)
