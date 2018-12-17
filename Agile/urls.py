from django.contrib import admin
from django.urls import path, include
from todolist.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', index, name='todolist'),
    path('calendar/', include('task_planner.urls')),
]
