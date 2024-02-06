from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["username"].help_text = "Informe um endereço de e-mail válido como usuário."
        
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get("password")
        
        # Criptografando a senha
        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user
        
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        
        if first_name == last_name:
            self.add_error("first_name", ValidationError("O primeiro nome não pode ser igual ao último nome."))
            self.add_error("last_name", ValidationError("O primeiro nome não pode ser igual ao último nome."))
        
        # Validar se o username é um e-mail válido
        username = self.cleaned_data.get("username")
        
        try:
            validate_email(username)
        except ValidationError:
            self.add_error("username", ValidationError("Informe um endereço de e-mail válido para o nome de usuário."))

        
        return super().clean()
    

class UpdateUserForm(CreateUserForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "is_active"]
        widgets = {
            "password": forms.PasswordInput()
        }