from django.shortcuts import render, redirect
from pullUps.models import Excercise
from .forms import InputTraining, InputExcercise

# Create your views here.



# def training(request):
#     excerciseList = Excercise.objects.all()
#     return render(request, 'pullUps/training.html', {"showAll": excerciseList})

# def training_new(request):
#     if request.method == "POST":
#         form = InputTraining(request.POST)
#         if form.is_valid():
#             training = form.save(commit=False)
#             training.save()
#             # return redirect('training_detail', pk=training.pk)
#             return redirect('training')
#     else:
#         form = InputTraining()
#     return render(request, 'pullUps/training_new.html', {'form': form})

def excercise_list(request):
    excerciseList = Excercise.objects.all()
    return render(request, 'excercises/list.html', {"showAll": excerciseList})

def excercise_show(request, pk):
    excercise = Excercise.objects.get(pk=pk)
    return render(request, 'excercises/show.html', {"excercise_show": excercise})

def excercise_edit(request, pk):
    form = InputExcercise()
    excercise = Excercise.objects.get(pk=pk)
    return render(request, 'excercises/edit.html', {'form': form, 'excercise': excercise})

    # excerciseList = Excercise.objects.all()
    # return render(request, 'pullUps/show.html', {"bla": exampleVar, "showAll": excerciseList})

    
def excercise_new(request):
    form = InputExcercise()
    return render(request, 'excercises/new.html', {'form': form})

def excercise_create(request):
    form  = InputExcercise(request.POST)
    if form.is_valid():
        excercise = form.save(commit=False)
        excercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercises/new.html', {'form': form})

    # return render(request, 'excercises/new.html', {'form': form})

def excercise_update(request):
    form  = InputExcercise(request.POST)
    if form.is_valid():
        excercise = form.save(commit=False)
        excercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercises/edit.html', {'form': form})