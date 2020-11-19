from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.views.generic import *
from pullUps.serializers import *
from django.http import JsonResponse
from .models import Excercise, Training, ExcerciseSet, ExcerciseBlock, ExcerciseBlockSets
from .forms import InputExcerciseSetForm, InputExcerciseBlockForm, InputTrainingForm
from pullUps.excercise.forms import InputExcerciseForm
from rest_framework.response import Response
from rest_framework.views import APIView
from pullUps.excercise.views import *

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


def training_list(request):
    trainingList = Training.objects.all()
    return render(request, 'training/index.html', {"showAll": trainingList})


def training_new(request):
    form = InputTrainingForm()
    return render(request, 'training/new.html', {'form': form})

def training_create(request):
    form = InputTrainingForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    print('form validation ={}'.format(form.is_valid()))
    if form.is_valid():
        print('form is valid')
        training = form.save().save()
        return redirect('training_list')
    else:
        print('form is not valid')
        print(form)
        print("errors:\n")
        print(form.errors)
        return render(request, 'training/new.html', {'form': form})

def training_show(request, pk):
    training = Training.objects.get(pk=pk)
    print(training)
    print(training.name)
    print(training.blocks)
    return render(request, 'training/show.html', {"training_show": training})

def training_edit(request, pk):
    training = get_object_or_404(Training, pk=pk)
    print(training)
    form  = InputTrainingForm(instance=training)
    return render(request, 'training/edit.html', {'form': form, 'training': training})

def training_update(request, pk):
    oldTraining = get_object_or_404(Training, pk=pk)
    form  = InputTrainingForm(request.POST, instance=oldTraining)
    if form.is_valid():
        newTraining = form.save()
        newTraining.save()
        return redirect('training_list')
    else:
        return render(request, 'training/edit.html', {'form': form, 'training_update': oldTraining})

def training_delete(request, pk):
    training = get_object_or_404(Training, pk=pk)
    print(training)
    training.delete()
    return redirect('training_list')

class TrainingView(APIView):
    """
    Returns an Training.
    """
    def get(self, request, pk, format=None):
        """
        Return an Training.
        """
        print(pk)
        training = Training.objects.get(pk=pk)
        serializedTraining = TrainingSerializer(training)
        return Response(serializedTraining.data)

def excercise_set_list(request):
    excercise_sets = ExcerciseSet.objects.all()
    return render(request, 'excercise_set/index.html', {"showAll": excercise_sets})


def excercise_set_new(request):
    form = InputExcerciseSetForm()
    return render(request, 'excercise_set/new.html', {'form': form})

def excercise_set_newForm(request):
    print(request)
    form = InputExcerciseSetForm()
    return render(request, 'excercise_set/form.html', {'formSet': form})

def excercise_set_create(request):
    form  = InputExcerciseSetForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    if form.is_valid():
        excercise_sets = form.save(commit=False)
        excercise_sets.save()
        return redirect('excercise_set_list')
    else:
        return render(request, 'excercise_set/new.html', {'form': form})

def excercise_set_show(request, pk):
    excercise_sets = ExcerciseSet.objects.get(pk=pk)
    return render(request, 'excercise_set/show.html', {"excercise_set_show": excercise_set_show})

def excercise_set_edit(request, pk):
    excercise_set = get_object_or_404(ExcerciseSet, pk=pk)
    form  = InputExcerciseSetForm(instance=excercise_set)
    return render(request, 'excercise_set/edit.html', {'form': form, 'excercise_set': excercise_set})

def excercise_set_update(request, pk):
    oldExcerciseSet = get_object_or_404(ExcerciseSet, pk=pk)
    form  = InputExcerciseSetForm(request.POST, instance=oldExcerciseSet)
    if form.is_valid():
        newExcerciseSet = form.save(commit=False)
        newExcerciseSet.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercise_set/edit.html', {'form': form, 'excercise_set_update': oldExcerciseSet})

def excercise_set_delete(request, pk):
    excercise_sets = get_object_or_404(ExcerciseSet, pk=pk)
    print(excercise_sets)
    excercise_sets.delete()
    return redirect('excercise_set_list')

class ExcerciseSetView(APIView):
    """
    Returns an excerciseSet.
    """
    def get(self, request, pk, format=None):
        """
        Return an excerciseSet.
        """
        print(pk)
        excerciseSet = ExcerciseSet.objects.get(pk=pk)
        serializedExcerciseSet = ExcerciseSetSerializer(excerciseSet)
        return Response(serializedExcerciseSet.data)


def excercise_block_list(request):
    excercise_blocks = ExcerciseBlock.objects.all()
    return render(request, 'excercise_block/index.html', {"showAll": excercise_blocks})


def excercise_block_new(request):
    form = InputExcerciseBlockForm()
    return render(request, 'excercise_block/new.html', {'form': form})

def excercise_block_newForm(request):
    print(request)
    form = InputExcerciseBlockForm()
    return render(request, 'excercise_block/form.html', {'formBlock': form})


def excercise_block_add_to_base(breakTimeAfterBlock, usedBlocksList):
    excercise_block = ExcerciseBlock.objects.create(breakTimeAfterBlock=breakTimeAfterBlock)
    for uSet in usedBlocksList:
        ExcerciseBlockSets(blockKey=excercise_block, setKey=ExcerciseSet.objects.get(id=uSet)).save()
    excercise_block.save()

def excercise_block_handle(data):
    newSetsRepsCount = data.getlist("repsCount")
    newSetsExcercises = data.getlist("usedExcercise")
    newSetsBreakAfterSet = data.getlist("breakTimeAfterSet")
    newSetsSequence = data.getlist("sequence")

    print("\n dlugosc hehe {}\n".format(newSetsExcercises))
    usedBlocksList = data.getlist("usedExcerciseSets")
    for nSet in range(len(newSetsExcercises)):
        print("\nsqeuenceNb = {} \n ".format(int(newSetsSequence[nSet])))
        newSetAdd = ExcerciseSet.objects.create(repsCount=newSetsRepsCount[nSet], usedExcercise=Excercise.objects.get(id=newSetsExcercises[nSet]), breakTimeAfterSet=newSetsBreakAfterSet[nSet])
        usedBlocksList.insert(int(newSetsSequence[nSet]),newSetAdd.pk)
        print("\n set nowy set set set = {}".format(newSetAdd))
    excercise_block_add_to_base(data.get("breakTimeAfterBlock"), usedBlocksList)


def excercise_block_create(request):
    form  = InputExcerciseBlockForm(request.POST)
    print ('request.post= \n{}\n'.format(request.POST))

    if form.is_valid():
        excercise_block_handle(request.POST)
        return redirect('excercise_block_list')
    else:
        return render(request, 'excercise_block/new.html', {'form': form})

def excercise_block_show(request, pk):
    excercise_block = ExcerciseBlock.objects.get(pk=pk)
    print(excercise_block)
    print(excercise_block.breakTimeAfterBlock)
    print(excercise_block.usedExcerciseSets)
    return render(request, 'excercise_block/show.html', {"excercise_block_show": excercise_block})

def excercise_block_edit(request, pk):
    excercise_block = get_object_or_404(ExcerciseBlock, pk=pk)
    print(excercise_block)
    print(excercise_block.breakTimeAfterBlock)
    print(excercise_block.usedExcerciseSets.all())
    form  = InputExcerciseBlockForm(instance=excercise_block)
    return render(request, 'excercise_block/edit.html', {'form': form, 'excercise_block': excercise_block})

def excercise_block_update(request, pk):
    oldExcerciseBlock = get_object_or_404(ExcerciseBlock, pk=pk)
    form  = InputExcerciseBlockForm(request.POST, instance=oldExcerciseBlock)
    if form.is_valid():
        newExcerciseBlock = form.save(commit=False)
        newExcerciseBlock.save()
        return redirect('excercise_block_list')
    else:
        return render(request, 'excercise_block/edit.html', {'form': form, 'excercise_block_update': oldExcerciseBlock})

def excercise_block_delete(request, pk):
    excercise_blocks = get_object_or_404(ExcerciseBlock, pk=pk)
    print(excercise_blocks)
    excercise_blocks.delete()
    return redirect('excercise_block_list')

class ExcerciseBlockView(APIView):
    """
    Returns an excerciseBlock.
    """
    def get(self, request, pk, format=None):
        """
        Return an excerciseBlock.
        """
        print(pk)
        excerciseBlock = ExcerciseBlock.objects.get(pk=pk)
        serializedExcerciseBlock = ExcerciseBlockSerializer(excerciseBlock)
        return Response(serializedExcerciseBlock.data)



# def YOUR_VIEW_DEF(request):
#     YOUR_OBJECT.objects.filter(pk=pk).update(views=F('views')+1)
#     return HttpResponseRedirect(request.GET.get('next'))
