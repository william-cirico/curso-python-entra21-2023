from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import SupplierForm
from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers/index.html"
    paginate_by = 100
    ordering = "-id"
    

class SupplierSearchView(ListView):
    model = Supplier
    template_name = "suppliers/index.html"
    paginate_by = 100
    ordering = "-id"
    
    def get_queryset(self):
        search_value = self.request.GET.get("q").strip()
        
        if search_value:
            return Supplier.objects.filter(
                Q(company_name__icontains=search_value) |
                Q(fantasy_name__icontains=search_value)).order_by("-id")
        else:
            return Supplier.objects.all()
    

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/create.html"
    success_url = reverse_lazy("suppliers:index")
    
    def form_valid(self, form):
        messages.success(self.request, "Fornecedor cadastrado com sucesso!")
        
        return super().form_valid(form)
    

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/update.html"
    success_url = reverse_lazy("suppliers:index")


class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy("suppliers:index")