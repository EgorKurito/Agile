from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_home'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='blog_post_detail'),
]
