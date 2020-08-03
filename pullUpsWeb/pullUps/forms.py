from django import forms
from .models import Excercise

class InputTraining(forms.ModelForm):

    class Meta:
        model = Excercise
        fields = ('name',)

class InputExcercise(forms.ModelForm):

    class Meta:
        model = Excercise
        fields = ('name',)