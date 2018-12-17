from django.urls import path

from . import views

app_name = 'task_planner'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
