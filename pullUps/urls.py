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


    path('training/index', views.training_list, name='training_list'),
    path('training/<int:pk>/show', views.training_show, name='training_show'),
    path('training/new', views.training_new, name='training_new'),
    path('training/create', views.training_create, name='training_create'),
    path('training/<int:pk>/edit', views.training_edit, name='training_edit'),
    path('training/<int:pk>/update', views.training_update, name='trainings_update'),

    path('excercise_blocks/index', views.excercise_blocks_list, name='excercise_blocks_list'),
    path('excercise_blocks/<int:pk>/show', views.excercise_blocks_show, name='excercise_blocks_show'),
    path('excercise_blocks/new', views.excercise_blocks_new, name='excercise_blocks_new'),
    path('excercise_blocks/create', views.excercise_blocks_create, name='excercise_blocks_create'),
    path('excercise_blocks/<int:pk>/edit', views.excercise_blocks_edit, name='excercise_blocks_edit'),
    path('excercise_blocks/<int:pk>/update', views.excercise_blocks_update, name='excercise_blocks_update'),

    path('excercise_sets/index', views.excercise_sets_list, name='excercise_sets_list'),
    path('excercise_sets/<int:pk>/show', views.excercise_sets_show, name='excercise_sets_show'),
    path('excercise_sets/new', views.excercise_sets_new, name='excercise_sets_new'),
    path('excercise_sets/create', views.excercise_sets_create, name='excercise_sets_create'),
    path('excercise_sets/<int:pk>/edit', views.excercise_sets_edit, name='excercise_sets_edit'),
    path('excercise_sets/<int:pk>/update', views.excercise_sets_update, name='excercise_sets_update'),


]
