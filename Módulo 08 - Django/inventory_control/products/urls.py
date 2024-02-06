from django.urls import path
from .views.product_management import ProductListView, ProductDeleteView, ProductUpdateView, ProductCreateView, ProductSearchView
from .views.category_management import CategoryListView, CategoryDeleteView, CategoryUpdateView, CategoryCreateView, CategorySearchView

app_name = "products"
urlpatterns = [
    path("produtos/", ProductListView.as_view(), name="index"),
    path("produtos/cadastro", ProductCreateView.as_view(), name="create"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="delete"),
    path("products/search", ProductSearchView.as_view(), name="search"),
    path("products/<slug:slug>/", ProductUpdateView.as_view(), name="update"),
    path("categorias/", CategoryListView.as_view(), name="categories"),
    path("categories/search", CategorySearchView.as_view(), name="categories_search"),
    path("categorias/cadastro", CategoryCreateView.as_view(), name="create_category"),
    path("categorias/<int:pk>/", CategoryUpdateView.as_view(), name="update_category"),
    path("categories/<int:pk>/delete", CategoryDeleteView.as_view(), name="delete_category"),
]
