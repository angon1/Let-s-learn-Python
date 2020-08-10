from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='root_path'),
    path('main', views.main_page, name='main_page'),
    path('excercises/<int:pk>/show', views.excercise_show, name='excercise_show'),
    path('excercises/new', views.excercise_new, name='excercise_new'),
    path('excercises/create', views.excercise_create, name='excercise_create'),
    path('excercises/<int:pk>/edit', views.excercise_edit, name='excercise_edit'),
    path('excercises/<int:pk>/update', views.excercise_update, name='excercise_update'),
    path('excercises/', views.excercise_list, name='excercise_list'),


    path('trainings/index', views.trainings_list, name='trainings_list'),
    # path('trainings/<int:pk>/show', views.trainings_show, name='trainings_show'),
    path('trainings/new', views.trainings_new, name='trainings_new'),
    path('trainings/create', views.trainings_create, name='trainings_create'),
    # path('trainings/<int:pk>/edit', views.trainings_edit, name='trainings_edit'),
    # path('trainings/<int:pk>/update', views.trainings_update, name='trainings_update'),
]