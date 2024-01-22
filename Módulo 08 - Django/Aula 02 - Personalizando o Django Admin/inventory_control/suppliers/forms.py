from django import forms
from .models import Supplier
import re

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        
        error_messages = {
            "company_name": {
                "unique": "A razão social já existe",
                "max_length": "O tamanho máximo da razão social é 255 caracteres",                
            }
        }
    
    # clean_<nome_campo>
    def clean_cnpj(self):
        # Obtendo o valor que foi digitado no formulário
        cnpj = self.cleaned_data.get("cnpj", "")
        
        # Removendo valores não númericos
        cnpj = re.sub("[^0-9]", "", cnpj)
        
        return cnpj
    
    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        
        # Removendo valores não númericos
        phone = re.sub("[^0-9]", "", phone)
        
        return phone
    
    def clean_zipcode(self):
        zipcode = self.cleaned_data.get("zipcode", "")
        
        # Removendo valores não númericos
        zipcode = re.sub("[^0-9]", "", zipcode)
        
        return zipcode
    