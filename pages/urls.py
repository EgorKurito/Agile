from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='page_home'),
    path('about/', views.AboutPAgeView.as_view(), name='page_about')
]