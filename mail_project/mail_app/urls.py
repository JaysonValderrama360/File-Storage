from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('view', views.show_file, name="home"),
]
