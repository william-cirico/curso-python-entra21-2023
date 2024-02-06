from django.urls import path
from . import views
from .views import SupplierDeleteView, SupplierListView, SupplierCreateView, SupplierSearchView, SupplierUpdateView

app_name = "suppliers"
urlpatterns = [
    path("", SupplierListView.as_view(), name="index"),
    path("cadastro", SupplierCreateView.as_view(), name="create"),
    path("<int:pk>/delete", SupplierDeleteView.as_view(), name="delete"),
    path("search", SupplierSearchView.as_view(), name="search"),
    path("<slug:slug>/", SupplierUpdateView.as_view(), name="update"),
]
