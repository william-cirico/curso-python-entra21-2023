from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.create, name="create"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("search", views.search, name="search"),
    path("<int:id>/toggle_enabled", views.toggle_enabled, name="toggle_enabled"),
    path("<slug:slug>/", views.update, name="update"),
    path("<int:id>/remove_supplier", views.delete_supplier_from_product, name="delete_supplier"),
    path("<int:id>/suppliers", views.get_suppliers_from_product, name="suppliers"),
]
