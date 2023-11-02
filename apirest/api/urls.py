from django.urls import path
from . import views

urlpatterns = [
    path('taskget', views.getTask),
    path('taskpost', views.postTask),
    path('taskput/<int:pk>', views.putTask),
    path('taskdelete/<int:pk>', views.deleteTask),
]