from django.urls import path
from . import views


urlpatterns = [
    path('', views.training, name='training'),
    path('pullUps/new', views.training_new, name='training_new'),
    path('excercise/<int:pk>', views.excercise_show, name='excercise_show'),
    path('excercise/<int:pk>/edit', views.excercise_edit, name='excercise_edit'),
]