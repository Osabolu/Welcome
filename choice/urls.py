from django.urls import path
from choice import views

urlpatterns = [
    path("choice/", views.choice, name="choice"),
]