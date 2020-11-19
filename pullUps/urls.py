from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='root_path'),
    path('main', views.main_page, name='main_page'),
    path('excercises/<int:pk>/show', views.excercise_show, name='excercise_show'),
    path('excercises/new', views.excercise_new, name='excercise_new'),
    path('excercises/create', views.excercise_create, name='excercise_create'),
    path('excercises/<int:pk>/edit', views.excercise_edit, name='excercise_edit'),
    path('excercises/<int:pk>/update', views.excercise_update, name='excercise_update'),
    path('excercises/<int:pk>/delete', views.excercise_delete, name='excercise_delete'),
    path('excercises/', views.excercise_list, name='excercise_list'),
    path('excercises/<int:pk>/serialize', views.ExcerciseView.as_view(), name='excercise_serialize'),


    path('training/index', views.training_list, name='training_list'),
    path('training/<int:pk>/show', views.training_show, name='training_show'),
    path('training/new', views.training_new, name='training_new'),
    path('training/create', views.training_create, name='training_create'),
    path('training/<int:pk>/edit', views.training_edit, name='training_edit'),
    path('training/<int:pk>/update', views.training_update, name='training_update'),
    path('training/<int:pk>/delete', views.training_delete, name='training_delete'),
    path('training/<int:pk>/serialize', views.TrainingView.as_view(), name='training_serialize'),

    path('excercise_blocks/index', views.excercise_block_list, name='excercise_block_list'),
    path('excercise_blocks/<int:pk>/show', views.excercise_block_show, name='excercise_block_show'),
    path('excercise_blocks/new', views.excercise_block_new, name='excercise_block_new'),
    path('excercise_blocks/create', views.excercise_block_create, name='excercise_block_create'),
    path('excercise_blocks/<int:pk>/edit', views.excercise_block_edit, name='excercise_block_edit'),
    path('excercise_blocks/<int:pk>/update', views.excercise_block_update, name='excercise_block_update'),
    path('excercise_blocks/<int:pk>/delete', views.excercise_block_delete, name='excercise_block_delete'),
    path('excercise_blocks/<int:pk>/serialize', views.ExcerciseBlockView.as_view(), name='excercise_block_serialize'),
    path('excercise_blocks/form', views.excercise_block_newForm, name='excercise_block_newForm'),

    path('excercise_sets/index', views.excercise_set_list, name='excercise_set_list'),
    path('excercise_sets/<int:pk>/show', views.excercise_set_show, name='excercise_set_show'),
    path('excercise_sets/new', views.excercise_set_new, name='excercise_set_new'),
    path('excercise_sets/create', views.excercise_set_create, name='excercise_set_create'),
    path('excercise_sets/<int:pk>/edit', views.excercise_set_edit, name='excercise_set_edit'),
    path('excercise_sets/<int:pk>/update', views.excercise_set_update, name='excercise_set_update'),
    path('excercise_sets/<int:pk>/delete', views.excercise_set_delete, name='excercise_set_delete'),
    path('excercise_sets/<int:pk>/serialize', views.ExcerciseSetView.as_view(), name='excercise_set_serialize'),
    path('excercise_sets/form', views.excercise_set_newForm, name='excercise_set_newForm'),

]
