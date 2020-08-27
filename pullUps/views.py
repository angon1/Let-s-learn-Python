from django.shortcuts import render, redirect, get_object_or_404
from pullUps.models import Excercise, Training, ExcerciseSet, ExcerciseBlock
from .forms import InputExcerciseForm, InputExcerciseSetForm, InputExcerciseBlockForm, InputTrainingNameForm, InputTrainingBlocksForm

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

def main_page(request):
    return render(request, 'main.html')

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
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
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





def training_list(request):
    trainingList = Training.objects.all()
    return render(request, 'trainings/index.html', {"showAll": trainingList})


def training_new(request):
    formName = InputTrainingNameForm()
    formBlocks = InputTrainingBlocksForm()
    return render(request, 'trainings/new.html', {'formName': formName, 'formBlocks': formBlocks})

def training_create(request):
    formName = InputTrainingNameForm(request.POST)
    formBlocks = InputTrainingBlocksForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(formName, request, request.POST))

    if 'addBlock' in request.POST:
        if formBlocks.is_valid():
            trainingName = formName.save(commit=False)
            training = formBlocks.save(commit=False)
            training.save()
            trainingName.save()
            return render(request, 'trainings/edit.html', {'formName': formName, 'formBlocks': formBlocks})
    elif 'saveTraining' in request.POST:
        if formBlocks.is_valid():
            trainingName = formName.save(commit=False)
            training = formBlocks.save(commit=False)
            training.save()
            trainingName.save()
            return redirect('training_list')
    else:
        return render(request, 'trainings/new.html', {'formName': formName, 'formBlocks': formBlocks})

# if request.method == 'POST':
#         if 'addBlock' in request.POST:
#             # bannedphraseform = BannedPhraseForm(request.POST, prefix='banned')
#             # if bannedphraseform.is_valid():
#             #     bannedphraseform.save()
#             expectedphraseform = ExpectedPhraseForm(prefix='expected')
#         elif 'saveTraining' in request.POST:
#             # expectedphraseform = ExpectedPhraseForm(request.POST, prefix='expected')
#             # if expectedphraseform.is_valid():
#             #     expectedphraseform.save()
#             bannedphraseform = BannedPhraseForm(prefix='banned')
#     else:

def training_show(request, pk):
    #tbd
    print( " " )

def training_edit(request, pk):
    training = get_object_or_404(Training, pk=pk)
    formName = InputTrainingNameForm()
    formBlocks = InputTrainingBlocksForm()
    return render(request, 'trainings/new.html', {'formName': formName, 'formBlocks': formBlocks})


def training_update(request, pk):
    #tbd
    print( " " )


def excercise_sets_list(request):
    excercise_sets = ExcerciseSet.objects.all()
    return render(request, 'excercise_sets/index.html', {"showAll": excercise_sets})


def excercise_sets_new(request):
    form = InputExcerciseSetForm()
    return render(request, 'excercise_sets/new.html', {'form': form})

def excercise_sets_create(request):
    form  = InputExcerciseSetForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    if form.is_valid():
        excercise_sets = form.save(commit=False)
        excercise_sets.save()
        return redirect('excercise_sets_list')
    else:
        return render(request, 'excercise_setss/new.html', {'form': form})

def excercise_sets_show(request, pk):
    excercise_sets = ExcerciseSet.objects.get(pk=pk)
    return render(request, 'excercise_sets/show.html', {"excercise_sets_show": excercise_sets})

def excercise_sets_edit(request, pk):
    #tbd
    print( " " )

def excercise_sets_update(request, pk):
    #tbd
    print( " " )



def excercise_blocks_list(request):
    excercise_blocks = ExcerciseBlock.objects.all()
    return render(request, 'excercise_blocks/index.html', {"showAll": excercise_blocks})


def excercise_blocks_new(request):
    form = InputExcerciseBlockForm()
    return render(request, 'excercise_blocks/new.html', {'form': form})

def excercise_blocks_create(request):
    form  = InputExcerciseBlockForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    if form.is_valid():
        excercise_blocks = form.save(commit=False)
        excercise_blocks.save()
        return redirect('excercise_blocks_list')
    else:
        return render(request, 'excercise_blocks/new.html', {'form': form})

def excercise_blocks_show(request, pk):
    excercise_block = ExcerciseBlock.objects.get(pk=pk)
    return render(request, 'excercise_blocks/show.html', {"excercise_blocks_show": excercise_block})

def excercise_blocks_edit(request, pk):
    #tbd
    print( " " )

def excercise_blocks_update(request, pk):
    #tbd
    print( " " )
