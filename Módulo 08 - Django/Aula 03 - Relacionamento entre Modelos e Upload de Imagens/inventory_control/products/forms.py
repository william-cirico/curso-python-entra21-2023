from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
        # error_messages = {
        #     "company_name": {
        #         "unique": "A razão social já existe",
        #         "max_length": "O tamanho máximo da razão social é 255 caracteres",                
        #     }
        # }
    