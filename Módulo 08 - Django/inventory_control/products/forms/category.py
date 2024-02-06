from django import forms

from products.models.category import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {
            "name": "Nome",
            "description": "Descrição"
        }
        error_messages = {
            "name": {
                "unique": "Já existe uma categoria com esse nome"
            }
        }