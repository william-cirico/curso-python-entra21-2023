from django.contrib import messages
from products.models.category import Category
from products.forms.category import CategoryForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = 100
    template_name = "categories/index.html"
    ordering = "-id"


class CategorySearchView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "categories/index.html"
    paginate_by = 100
    ordering = "-id"
    
    def get_queryset(self):
        search_value = self.request.GET.get("q").strip()
        
        if search_value:
            return Category.objects.filter(name__icontains=search_value).order_by("-id")
        else:
            return Category.objects.all()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/create.html"
    success_url = reverse_lazy("products:categories")
    
    def form_valid(self, form):
        messages.success(self.request, "Categoria cadastrada com sucesso!")
            
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/update.html"
    success_url = reverse_lazy("products:categories")
    
    def form_valid(self, form):
        messages.success(self.request, "Categoria atualizada com sucesso!")
            
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("products:categories")
