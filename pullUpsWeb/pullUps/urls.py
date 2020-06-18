from django.urls import path
from . import views


urlpatterns = [
    path('', views.training, name='training'),
    path('pullUps/new', views.training_new, name='training_new'),
]