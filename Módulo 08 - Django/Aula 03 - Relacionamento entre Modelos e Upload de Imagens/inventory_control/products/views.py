from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.order_by("-id")
        
    # Aplicando a paginação
    paginator = Paginator(products, 2)
    # /Produtoes?page=1 -> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "products": page_obj }
    
    return render(request, "products/index.html", context)

def search(request):
    # Obtendo o valor da requisição (Formulário)
    search_value = request.GET.get("q").strip()
    
    # Verificando se algo foi digitado
    if not search_value:
        return redirect("products:index")
    
    # Filtrando os Produtoes
    # O Q é usado para combinar filtros (& ou |)
    products = Product.objects \
        .filter(name__icontains=search_value) \
        .order_by("-id")
    
    # Criando o paginator
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "products": page_obj }
    
    return render(request, "products/index.html", context)

def create(request):
    form_action = reverse("products:create")
    #POST
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "O produto foi cadastrado com sucesso!")
            
            return redirect("products:index")
        
        messages.error(request, "Falha ao cadastrar o produto. Verifique o preenchimento dos campos.")
        
        context = { "form": form, "form_action": form_action }
        
        return render(request, "products/create.html", context)
    
    # GET
    form = ProductForm()
    
    context = { "form": form, "form_action": form_action }
    
    return render(request, "products/create.html", context)

def update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form_action = reverse("products:update", args=(slug,)) # Obtendo a URL da rota de atualização
    
    # POST
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        
        if form.is_valid():
            form.save()            
            messages.success(request, "Produto atualizado com sucesso")            
            return redirect("products:index")
        
        context = {
            "form_action": form_action,
            "form": form
        }
        
        return render(request, "products/create.html", context)
    
    # GET
    form = ProductForm(instance=product)
    
    context = {
        "form_action": form_action,
        "form": form,
    }
    
    return render(request, "products/create.html", context)

@require_POST
def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    
    return redirect("products:index")

@require_POST
def toggle_enabled(request, id):
    product = get_object_or_404(Product, pk=id)
    
    product.enabled = not product.enabled
    product.save()
    
    return JsonResponse({ "message": "success" })