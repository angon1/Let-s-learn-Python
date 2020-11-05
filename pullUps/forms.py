from django import forms
from .models import Excercise, Training, ExcerciseSet, ExcerciseBlock

class InputTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('name', 'blocks')
        labels = {
            'name': 'Nazwa',
            'blocks': 'Bloki',
        }

class InputExcerciseSetForm(forms.ModelForm):
    class Meta:
        model = ExcerciseSet
        fields = ('repsCount', 'usedExcercise', 'breakTimeAfterSet',)
        labels = {
            'repsCount': 'Powtorzenia',
            'usedExcercise': 'Ćwiczenie',
            'breakTimeAfterSet': 'Przerwa',
        }

class InputExcerciseBlockForm(forms.ModelForm):
    class Meta:
        model = ExcerciseBlock
        fields = ('breakTimeAfterBlock', 'usedExcerciseSets',)
        labels = {
            'breakTimeAfterBlock': 'Przerwa po bloku',
            'usedExcerciseSets': 'set do bloku',
        }
