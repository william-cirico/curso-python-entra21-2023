from django.db import models
from suppliers.models import Supplier
from .product import Product
        

class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.product} - {self.supplier}"
    
    class Meta:
        unique_together = [["supplier", "product"]]
        verbose_name = "Fornecedor_Produto"
        verbose_name_plural = "Fornecedores_Produtos"
    