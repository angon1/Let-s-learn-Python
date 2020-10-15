from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.views.generic import *
from pullUps.serializers import *
from django.http import JsonResponse
from pullUps.models import Excercise, Training, ExcerciseSet, ExcerciseBlock, ExcerciseBlockSets
from .forms import InputExcerciseForm, InputExcerciseSetForm, InputExcerciseBlockForm, InputTrainingForm
from rest_framework.response import Response
from rest_framework.views import APIView

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


def excercise_delete(request, pk):
    excercise = get_object_or_404(Excercise, pk=pk)
    print(excercise)
    excercise.delete()
    return redirect('excercise_list')

class ExcerciseView(APIView):
    """
    Returns an excercise.
    """
    def get(self, request, pk, format=None):
        """
        Return a list of all excercises.
        """
        print(pk)
        excercises = Excercise.objects.get(pk=pk)
        serializedExcercises = ExcerciseSerializer(excercises)
        return Response(serializedExcercises.data)


def training_list(request):
    trainingList = Training.objects.all()
    return render(request, 'trainings/index.html', {"showAll": trainingList})


def training_new(request):
    form = InputTrainingForm()
    return render(request, 'trainings/new.html', {'form': form})

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
        return render(request, 'trainings/new.html', {'form': form})

def training_show(request, pk):
    training = Training.objects.get(pk=pk)
    print(training)
    print(training.name)
    print(training.blocks)
    return render(request, 'trainings/show.html', {"training_show": training})

def training_edit(request, pk):
    training = get_object_or_404(Training, pk=pk)
    print(training)
    form  = InputTrainingForm(instance=training)
    return render(request, 'trainings/edit.html', {'form': form, 'training': training})

def training_update(request, pk):
    oldTraining = get_object_or_404(Training, pk=pk)
    form  = InputTrainingForm(request.POST, instance=oldTraining)
    if form.is_valid():
        newTraining = form.save()
        newTraining.save()
        return redirect('training_list')
    else:
        return render(request, 'trainings/edit.html', {'form': form, 'training_update': oldTraining})

# def training_serialize(request, pk):
#     training = get_object_or_404(Training, pk=pk)
#     print(training)
#     print(training.name)
#     print(training.blocks.all())
#     for block in training.blocks.all():
#         print(block.pk)
#         for excSet in block.usedExcerciseSets.all():
#             print(excSet)
#             print("cos")
#     # block = get_object_or_404(ExcerciseBlock, pk=training.blocks.first())
#     # pk = map()
#     # print(block)
#     # blocks = serializers.serialize("json", [block])
#     trainingData = serializers.serialize("json", [training])
#     print(trainingData)
#     return JsonResponse({"data" : trainingData})

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

def excercise_sets_list(request):
    excercise_sets = ExcerciseSet.objects.all()
    return render(request, 'excercise_sets/index.html', {"showAll": excercise_sets})


def excercise_sets_new(request):
    form = InputExcerciseSetForm()
    return render(request, 'excercise_sets/new.html', {'form': form})

def excercise_sets_newForm(request):
    print(request)
    form = InputExcerciseSetForm()
    return render(request, 'excercise_sets/form.html', {'formSet': form})

def excercise_sets_create(request):
    form  = InputExcerciseSetForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    if form.is_valid():
        excercise_sets = form.save(commit=False)
        excercise_sets.save()
        return redirect('excercise_sets_list')
    else:
        return render(request, 'excercise_sets/new.html', {'form': form})

def excercise_sets_show(request, pk):
    excercise_sets = ExcerciseSet.objects.get(pk=pk)
    return render(request, 'excercise_sets/show.html', {"excercise_sets_show": excercise_sets_show})

def excercise_sets_edit(request, pk):
    excercise_set = get_object_or_404(ExcerciseSet, pk=pk)
    form  = InputExcerciseSetForm(instance=excercise_set)
    return render(request, 'excercise_sets/edit.html', {'form': form, 'excercise_set': excercise_set})

def excercise_sets_update(request, pk):
    oldExcerciseSet = get_object_or_404(ExcerciseSet, pk=pk)
    form  = InputExcerciseSetForm(request.POST, instance=oldExcerciseSet)
    if form.is_valid():
        newExcerciseSet = form.save(commit=False)
        newExcerciseSet.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercise_sets/edit.html', {'form': form, 'excercise_sets_update': oldExcerciseSet})

def excercise_sets_delete(request, pk):
    excercise_sets = get_object_or_404(ExcerciseSet, pk=pk)
    print(excercise_sets)
    excercise_sets.delete()
    return redirect('excercise_sets_list')

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


def excercise_blocks_list(request):
    excercise_blocks = ExcerciseBlock.objects.all()
    return render(request, 'excercise_blocks/index.html', {"showAll": excercise_blocks})


def excercise_blocks_new(request):
    form = InputExcerciseBlockForm()
    return render(request, 'excercise_blocks/new.html', {'form': form})

def excercise_blocks_newForm(request):
    print(request)
    form = InputExcerciseBlockForm()
    return render(request, 'excercise_blocks/form.html', {'formBlock': form})

def excercise_blocks_create(request):
    form  = InputExcerciseBlockForm(request.POST)
    if form.is_valid():
        usedBlocksList = request.POST.getlist("usedExcerciseSets")
        excercise_block = ExcerciseBlock.objects.create(breakTimeAfterBlock=request.POST.get("breakTimeAfterBlock"))
        for uSet in usedBlocksList:
            ExcerciseBlockSets(blockKey=excercise_block, setKey=ExcerciseSet.objects.get(id=uSet)).save()
        excercise_block.save()
        return redirect('excercise_blocks_list')
    else:
        return render(request, 'excercise_blocks/new.html', {'form': form})

def excercise_blocks_show(request, pk):
    excercise_block = ExcerciseBlock.objects.get(pk=pk)
    print(excercise_block)
    print(excercise_block.breakTimeAfterBlock)
    print(excercise_block.usedExcerciseSets)
    return render(request, 'excercise_blocks/show.html', {"excercise_blocks_show": excercise_block})

def excercise_blocks_edit(request, pk):
    excercise_block = get_object_or_404(ExcerciseBlock, pk=pk)
    print(excercise_block)
    print(excercise_block.breakTimeAfterBlock)
    print(excercise_block.usedExcerciseSets.all())
    form  = InputExcerciseBlockForm(instance=excercise_block)
    return render(request, 'excercise_blocks/edit.html', {'form': form, 'excercise_block': excercise_block})

def excercise_blocks_update(request, pk):
    oldExcerciseBlock = get_object_or_404(ExcerciseBlock, pk=pk)
    form  = InputExcerciseBlockForm(request.POST, instance=oldExcerciseBlock)
    if form.is_valid():
        newExcerciseBlock = form.save(commit=False)
        newExcerciseBlock.save()
        return redirect('excercise_blocks_list')
    else:
        return render(request, 'excercise_blocks/edit.html', {'form': form, 'excercise_blocks_update': oldExcerciseBlock})

def excercise_blocks_delete(request, pk):
    excercise_blocks = get_object_or_404(ExcerciseBlock, pk=pk)
    print(excercise_blocks)
    excercise_blocks.delete()
    return redirect('excercise_blocks_list')

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
