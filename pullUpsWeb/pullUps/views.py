from django.shortcuts import render, redirect, get_object_or_404
from pullUps.models import Excercise
from .forms import InputTraining, InputExcerciseForm

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
    return render(request, 'excercises/index.html', {"showAll": excerciseList})

def excercise_show(request, pk):
    excercise = Excercise.objects.get(pk=pk)
    return render(request, 'excercises/show.html', {"excercise_show": excercise})



    # excerciseList = Excercise.objects.all()
    # return render(request, 'pullUps/show.html', {"bla": exampleVar, "showAll": excerciseList})

    
def excercise_new(request):
    form = InputExcerciseForm()
    return render(request, 'excercises/new.html', {'form': form})

def excercise_create(request):
    form  = InputExcerciseForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, requ))
    if form.is_valid():
        excercise = form.save(commit=False)
        excercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercises/new.html', {'form': form})

    # return render(request, 'excercises/new.html', {'form': form})


def excercise_edit(request, pk):
    excercise = get_object_or_404(Excercise, pk=pk)
    form  = InputExcerciseForm(instance=excercise)
    return render(request, 'excercises/edit.html', {'form': form, 'excercise': excercise})

def excercise_update(request, pk):
    oldExcercise = get_object_or_404(Excercise, pk=pk)
    form  = InputExcerciseForm(request.POST, instance=oldExcercise)
    if form.is_valid():
        newExcercise = form.save(commit=False)
        newExcercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercises/edit.html', {'form': form, 'excercise': oldExcercise})