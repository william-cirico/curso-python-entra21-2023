from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "api"
urlpatterns = [
    path("products/<int:id>/suppliers", views.SupplierProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
