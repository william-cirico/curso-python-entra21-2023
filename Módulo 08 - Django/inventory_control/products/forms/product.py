from django import forms

from products.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["enabled", "thumbnail", "slug", "suppliers"]
        labels = {
            "name": "Nome",
            "description": "Descrição",
            "sale_price": "Preço de venda",
            "category": "Categoria",
            "expiration_date": "Data de expiração",
            "photo": "Imagem do produto",
            "enabled": "Ativo",
            "suppliers": "Fornecedores"
        }
        widgets = {
            "expiration_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }
    