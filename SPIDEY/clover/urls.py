
from django.urls import path
from .views import index,sample,update_task,delete_task


urlpatterns = [
    path('',index,name='index'),
    path('sample',sample,name='sample'),
    path('update_task/<int:task_id>/',update_task,name='update_task'),
    path('delete_task/<int:task_id>/',delete_task,name='delete_task'),
]