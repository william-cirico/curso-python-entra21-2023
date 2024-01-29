from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Product, SupplierProduct
from .forms import ProductForm, SupplierProductFormSet
from django.db import IntegrityError


def index(request):
    products = Product.objects.order_by("-id")

    # Aplicando a paginação
    paginator = Paginator(products, 2)
    # /Produtoes?page=1 -> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"products": page_obj}

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
        .filter(Q(name__icontains=search_value) |
                Q(category__name__icontains=search_value)) \
        .order_by("-id")

    # Criando o paginator
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"products": page_obj}

    return render(request, "products/index.html", context)


def create(request):
    form_action = reverse("products:create")
    # POST
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()

            supplier_product_formset = SupplierProductFormSet(
                request.POST, instance=product)

            if supplier_product_formset.is_valid():
                supplier_product_formset.save()
                messages.success(
                    request, "O produto foi cadastrado com sucesso!")
            else:
                product.delete()
                messages.error(
                    request, "Falha ao cadastrar os fornecedores do produto.")

            return redirect("products:index")

        messages.error(
            request, "Falha ao cadastrar o produto. Verifique o preenchimento dos campos.")

        supplier_product_formset = SupplierProductFormSet(request.POST)

        context = {"form": form, "supplier_product_formset":
                   supplier_product_formset, "form_action": form_action}

        return render(request, "products/create.html", context)

    # GET
    form = ProductForm()
    supplier_product_formset = SupplierProductFormSet()

    context = {"form": form, "supplier_product_formset": supplier_product_formset,
               "form_action": form_action}

    return render(request, "products/create.html", context)


def update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form_action = reverse("products:update", args=(slug,))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        supplier_product_formset = SupplierProductFormSet(
            request.POST, instance=product)

        if form.is_valid():
            try:
                if form.cleaned_data["photo"] is False:
                    product.thumbnail.delete(save=False)

                form.save()

                if supplier_product_formset.is_valid():
                    supplier_product_formset.save()
                    messages.success(request, "Produto atualizado com sucesso")
                    return redirect("products:index")
                else:
                    messages.error(
                        request, "Falha ao atualizar o produto - Formulário de fornecedores inválido.")

            except IntegrityError:
                messages.error(
                    request, "Falha ao atualizar o produto - Não é possível ter o mesmo fornecedor para o mesmo produto mais de uma vez.")
        else:
            messages.error(
                request, "Falha ao atualizar o produto - Formulário inválido.")
        
        
        supplier_product_formset = SupplierProductFormSet(instance=product)
        context = {
            "form_action": form_action,
            "form": form,
            "supplier_product_formset": supplier_product_formset
        }
        
        return render(request, "products/create.html", context)


    form = ProductForm(instance=product)
    supplier_product_formset = SupplierProductFormSet(instance=product)

    context = {
        "form_action": form_action,
        "form": form,
        "supplier_product_formset": supplier_product_formset
    }

    return render(request, "products/create.html", context)


@require_POST
def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()

    return redirect("products:index")

@require_POST
def delete_supplier_from_product(request, id):
    supplier_product = get_object_or_404(SupplierProduct, pk=id)
    supplier_product.delete()
    
    return JsonResponse({"message": "success"})

@require_POST
def toggle_enabled(request, id):
    product = get_object_or_404(Product, pk=id)

    product.enabled = not product.enabled
    product.save()

    return JsonResponse({"message": "success"})

@require_GET
def get_suppliers_from_product(request, id):
    suppliers = SupplierProduct.objects.filter(product__id = id)

    # Serializando os dados
    data = [{
        "id": supplier.supplier.id,
        "name": supplier.supplier.fantasy_name,
        "price": supplier.price
    } for supplier in suppliers]
    
    return JsonResponse(data, safe=False)
