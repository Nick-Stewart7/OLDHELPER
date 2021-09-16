from django.urls import path
from Gun import views

urlpatterns = [
    path("", views.home, name="home"),
]