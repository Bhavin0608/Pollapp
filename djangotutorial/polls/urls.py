from django.urls import path

from . import views
# Empty means "" homepage
urlpatterns = [
    path("", views.index, name="index"), 
]