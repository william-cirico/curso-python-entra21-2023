from django.db.models import Q
from django.contrib import messages
from products.models.product import Product
from products.forms.product import ProductForm
from products.forms.supplier_product import SupplierProductFormSet
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db import transaction, IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 100
    template_name = "products/index.html"
    ordering = "-id"


class ProductSearchView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/index.html"
    paginate_by = 100
    ordering = "-id"
    
    def get_queryset(self):
        search_value = self.request.GET.get("q").strip()
        
        if search_value:
            return Product.objects.filter(
                Q(name__icontains=search_value) |
                Q(category__name__icontains=search_value)).order_by("-id")
        else:
            return Product.objects.all()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"
    success_url = reverse_lazy("products:index")
    
    def form_valid(self, form):
        with transaction.atomic():
            response = super().form_valid(form)
            supplier_product_formset = SupplierProductFormSet(self.request.POST, instance=self.object)
            
            if supplier_product_formset.is_valid():
                supplier_product_formset.save()
                messages.success(self.request, "Produto cadastrado com sucesso!")
                return response
            else:
                messages.error(self.request, "Falha ao cadastrar os fornecedores do produto.")
                return self.form_invalid(form)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context["supplier_product_formset"] = SupplierProductFormSet(self.request.POST)
        else:
            context["supplier_product_formset"] = SupplierProductFormSet()
        
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/update.html"
    success_url = reverse_lazy("products:index")
    
    def form_valid(self, form):
        with transaction.atomic():
            response = super().form_valid(form)
            supplier_product_formset = SupplierProductFormSet(self.request.POST, instance=self.object)
            
            if supplier_product_formset.is_valid():
                try:
                    supplier_product_formset.save()
                    messages.success(self.request, "Produto atualizado com sucesso!")
                except IntegrityError:
                    messages.error(self.request, "Existem fornecedores duplicados.")
                    return self.form_invalid(form)
                
                return response
            else:
                messages.error(self.request, "Falha ao cadastrar os fornecedores do produto.")
                return self.form_invalid(form)
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context["supplier_product_formset"] = SupplierProductFormSet(self.request.POST, instance=self.object)
        else:
            context["supplier_product_formset"] = SupplierProductFormSet(instance=self.object)
        
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("products:index")
