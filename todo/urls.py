from django.urls import path 
from . import views 

urlpatterns = [
    #add task
    path('addtask/', views.addtask, name='addtask'),
    #mark_as_done
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    #mark_as_undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
    #edit feature
    path('edit_task/<int:pk>',views.edit_task,name= 'edit_task'),
    #delete_task
    path('delete_task/<int:pk>',views.delete_task,name= 'delete_task')


]
