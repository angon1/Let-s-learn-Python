from django import forms
from .models import Excercise, Training

class InputTrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('name',)

class InputExcerciseForm(forms.ModelForm):

    class Meta:
        model = Excercise
        fields = ('name',)


    # class InputExcerciseForm(forms.ModelForm):

    # class Meta:
    #     model = Excercise
    #     fields = ('name',)