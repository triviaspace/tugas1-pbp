from django.urls import path
from todolist.views import *

# TODO: Implement Routings Here
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('selesai/<int:pk>', task_selesai, name='task-selesai'),
    path('undo/<int:pk>', undo_task, name='undo-task'),
    path('hapus/<int:pk>', hapus_task, name='hapus-task'),
    path('json/', todolist_ajax, name='todolist_ajax'),
    path('show/json/', show_todolist_ajax, name='show_todolist_ajax'),
    path('add/', add_task_ajax, name='add_task_ajax'),


]
