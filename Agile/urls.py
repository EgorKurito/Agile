from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todolist.urls')),
    path('pages/', include('pages.urls')),
    path('message/', include('posts.urls')),
    path('blog/', include('blog.urls')),
]
