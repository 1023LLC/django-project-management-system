from django.urls import path

from . import views 



app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add'),
    path('<uuid:pk>/', views.project, name='project')
]