from django.urls import path
from jumia import views

urlpatterns = [
    path("jumia/",views.jumia, name="jumia"),
]