from django.db import models

class Excercise(models.Model):
    name = models.TextField()

    # def get_queryset(self):
    #     return self.model.objects.filter(name=self.request.name)

    def __str__(self):
        return self.name
