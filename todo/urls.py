from django.urls import path
from . import views

urlpatterns = [
    path('addtask/',views.addTask,name='add-task'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('delete_task/<int:pk>/',views.deleteTask,name='delete_task'),
    path('mark_as_incomplete/<int:pk>/',views.markAsIncomplete, name='mark_as_incomplete'),
    path('edit_task/<int:pk>/',views.editTask,name='edit_task'),
    path('update_task/<int:pk>/',views.updateTask,name='update_task')
]