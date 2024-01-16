from django.urls import path
from . import views

app_name = "suppliers"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/delete", views.delete, name="delete")
]
