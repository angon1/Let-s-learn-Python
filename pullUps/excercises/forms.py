from django import forms
from .models import Excercise

class InputExcerciseForm(forms.ModelForm):
    class Meta:
        model = Excercise
        fields = ('name',)
