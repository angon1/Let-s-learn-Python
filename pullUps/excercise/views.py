from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.views.generic import *
from pullUps.serializers import *
from django.http import JsonResponse
from pullUps.excercise.models import Excercise
from .forms import InputExcerciseForm
from rest_framework.response import Response
from rest_framework.views import APIView


def excercise_list(request):
    excerciseList = Excercise.objects.all()
    return render(request, 'excercise/index.html', {"showAll": excerciseList})

def excercise_show(request, pk):
    excercise = Excercise.objects.get(pk=pk)
    return render(request, 'excercise/show.html', {"excercise_show": excercise})



    # excerciseList = Excercise.objects.all()
    # return render(request, 'pullUps/show.html', {"bla": exampleVar, "showAll": excerciseList})


def excercise_new(request):
    form = InputExcerciseForm()
    return render(request, 'excercise/new.html', {'form': form})

def excercise_create(request):
    form  = InputExcerciseForm(request.POST)
    print ('form =  {}  \n request = {} \n request.post= {}'.format(form, request, request.POST))
    if form.is_valid():
        excercise = form.save(commit=False)
        excercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercise/new.html', {'form': form})

    # return render(request, 'excercise/new.html', {'form': form})


def excercise_edit(request, pk):
    excercise = get_object_or_404(Excercise, pk=pk)
    form  = InputExcerciseForm(instance=excercise)
    return render(request, 'excercise/edit.html', {'form': form, 'excercise': excercise})

def excercise_update(request, pk):
    oldExcercise = get_object_or_404(Excercise, pk=pk)
    form  = InputExcerciseForm(request.POST, instance=oldExcercise)
    if form.is_valid():
        newExcercise = form.save(commit=False)
        newExcercise.save()
        return redirect('excercise_list')
    else:
        return render(request, 'excercise/edit.html', {'form': form, 'excercise': oldExcercise})


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
        Return a list of all excercise.
        """
        print(pk)
        excercises = Excercise.objects.get(pk=pk)
        serializedExcercises = ExcerciseSerializer(excercises)
        return Response(serializedExcercises.data)
