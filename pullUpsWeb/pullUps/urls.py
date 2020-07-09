from django.urls import path
from . import views


urlpatterns = [
    path('', views.excercise_list, name='excercise_list'),
    # path('pullUps/new', views.training_new, name='training_new'),
    path('excercises/<int:pk>/show', views.excercise_show, name='excercise_show'),
    # path('excercises/show/<int:pk>/edit', views.excercise_edit, name='excercise_edit'),
    path('excercises/new', views.excercise_new, name='excercise_new'),
    path('excercises/create', views.excercise_create, name='excercise_create'),
    path('excercises/<int:pk>/edit', views.excercise_edit, name='excercise_edit'),
    path('excercises/<int:pk>/update', views.excercise_update, name='excercise_update'),
    path('excercises/', views.excercise_list, name='excercise_list'),
]