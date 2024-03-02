from django.urls import path

from . import views



app_name = 'todolist'


urlpatterns = [
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.todolist, name='todolist')
]