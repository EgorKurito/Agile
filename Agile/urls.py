from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls')),
    path('calendar/', include('task_planner.urls')),
    path('pages/', include('pages.urls')),
]
