from django.shortcuts import render, redirect
from pullUps.training import Training
from pullUps.models import Excercise
from .forms import InputTraining

# Create your views here.

def training(request):
    exampleVar = Training.printMeVoid()
    return render(request, 'pullUps/training.html', {"bla": exampleVar, "showAll": Excercise.objects.all()})

def training_new(request):
    if request.method == "POST":
        form = InputTraining(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.save()
            # return redirect('training_detail', pk=training.pk)
            return redirect('training')
    else:
        form = InputTraining()
    return render(request, 'pullUps/training_new.html', {'form': form})
