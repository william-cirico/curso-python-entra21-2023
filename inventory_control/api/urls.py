from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views.products import toggle_product_active, get_suppliers_from_product, delete_supplier_from_product
from .views.users import toggle_user_active
from .views.suppliers import toggle_supplier_active
from .views.categories import CategoryList, CategoryDetail
from .views.root import api_root

app_name = "api"
urlpatterns = [
    path("", api_root),
    path("users/<int:pk>/toggle_active/", toggle_user_active, name="toggle_user_active"),
    path("suppliers/<int:pk>/toggle_active/", toggle_supplier_active, name="toggle_supplier_active"),
    path("products/<int:pk>/suppliers/", get_suppliers_from_product, name="get_suppliers_from_product"),
    path("products/<int:pk>/", toggle_product_active, name="toggle_product_active"),
    path("products-suppliers/<int:pk>/", delete_supplier_from_product, name="delete_supplier_from_product"),
    path("categories/", CategoryList.as_view(), name="categories-list"),
    path("categories/<int:pk>/", CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
