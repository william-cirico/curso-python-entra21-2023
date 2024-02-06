from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import CreateUserForm, UpdateUserForm


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "users/create.html"
    success_url = reverse_lazy("users:index")
    
    def form_valid(self, form):
        # Salvando o usuário no BD
        response = super().form_valid(form)
        
        # Obtendo o e-mail do usuário através do formulário
        user_email = form.cleaned_data.get("username")
        
        # Conteúdo do e-mail
        subject = "IStock - Cadastro realizado com sucesso!"
        message = "Parabéns! O seu cadastro no IStock foi realizado com sucesso!"
        from_email = None # Irá utilizar o settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email] # Destinatários
        
        # Enviando o e-mail
        send_mail(subject, message, from_email, recipient_list)
        
        messages.success(self.request, "O usuário foi cadastrado com sucesso!")
        
        return response
    

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users:index")
    

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/index.html"
    paginate_by = 100
    ordering = "-id"
    

class UserSearchView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/index.html"
    paginate_by = 100


    def get_queryset(self):
        search_value = self.request.GET.get("q").strip()
        
        if search_value:
            return User.objects.filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)).order_by("-id")
        else:
            return User.objects.all()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UpdateUserForm
    model = User
    template_name = "users/update.html"
    success_url = reverse_lazy("users:index")