from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import HTML, Button, Column, Field, Layout, Row
from django import forms
from django.forms import inlineformset_factory

from .models import Product, SupplierProduct


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
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ""
 
           
class SupplierProductForm(forms.ModelForm):
    class Meta:
        model = SupplierProduct
        exclude = ["product"]
        widgets = {
            "price": forms.NumberInput(attrs={"placeholder": "Preço de compra"})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
       
    
SupplierProductFormSet = inlineformset_factory(
    Product,
    SupplierProduct,
    form=SupplierProductForm,
    extra=1,
    max_num=1,
    can_delete=True
)