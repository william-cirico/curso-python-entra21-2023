from django.db import models
from django.utils.text import slugify


class Supplier(models.Model):
    STATE_CHOICES = {
        "AC": "Acre",
        "AL": "Alagoas",
        "AP": "Amapá",
        "AM": "Amazonas",
        "BA": "Bahia",
        "CE": "Ceará",
        "ES": "Espírito Santo",
        "GO": "Goiás",
        "MA": "Maranhão",
        "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul",
        "MG": "Minas Gerais",
        "PA": "Pará",
        "PB": "Paraíba",
        "PR": "Paraná",
        "PE": "Pernanbuco",
        "PI": "Piauí",
        "RJ": "Rio de Janeiro",
        "RN": "Rio Grande do Norte",
        "RS": "Rio Grande do Sul",
        "RO": "Rondônia",
        "RR": "Roraima",
        "SC": "Santa Catarina",
        "SP": "São Paulo",
        "SE": "Sergipe",
        "TO": "Tocantins",
        "DF": "Distrito Federal",
    }

    company_name = models.CharField(max_length=255, unique=True)
    fantasy_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    representative = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    zipcode = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    phone = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fantasy_name)
        super(Supplier, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
