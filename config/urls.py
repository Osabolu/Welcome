
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("section/",include("choice.urls")),
    path("Home/", include("jumia.urls")),
]
