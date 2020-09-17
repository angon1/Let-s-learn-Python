from rest_framework import serializers
from pullUps.models import Excercise, ExcerciseSet, ExcerciseBlock, Training

# Create your models here.

class ExcerciseSerializer(serializers.ModelSerializer):
    """
    Serializing single excercise
    """

    class Meta:
        model = Excercise
        fields = ['name']


class ExcerciseSetSerializer(serializers.ModelSerializer):
    """
    Serializing single set
    """
    usedExcercise = ExcerciseSerializer()
    class Meta:
        model = ExcerciseSet
        fields = ['repsCount', 'usedExcercise', 'breakTimeAfterSet']


class ExcerciseBlockSerializer(serializers.ModelSerializer):
    """
    Serializing single Block
    """
    usedExcerciseSets = ExcerciseSetSerializer(many=True)
    class Meta:
        model = ExcerciseBlock
        fields = ['breakTimeAfterBlock', 'usedExcerciseSets']


class TrainingSerializer(serializers.ModelSerializer):
    """
    Serializing single Block
    """
    blocks = ExcerciseBlockSerializer(many=True)
    class Meta:
        model = Training
        fields = ['blocks', 'name']
