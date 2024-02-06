from crispy_forms.helper import FormHelper
from django import forms
from django.forms import inlineformset_factory

from products.models.product import Product
from products.models.supplier_product import SupplierProduct

           
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