from django.urls import path
from django.views.generic import RedirectView

from users.views.user_management import UserListView, UserUpdateView, UserCreateView, UserDeleteView, UserSearchView
from users.views.auth import UserLoginView, UserLogoutView
from django.contrib.auth.views import PasswordChangeView

app_name = "users"
urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("usuarios/", UserListView.as_view(), name="index"),
    path("usuarios/cadastro/", UserCreateView.as_view(), name="create"),
    path("users/<int:pk>/delete", UserDeleteView.as_view(), name="delete"),
    path("users/search", UserSearchView.as_view(), name="search"),
    path("usuarios/<int:pk>/", UserUpdateView.as_view(), name="update"),
    path("", RedirectView.as_view(url="login/", permanent=True)),
]
