from django.db import models
from products.models.category import Category
from suppliers.models import Supplier
from PIL import Image
from django.utils.text import slugify
import os
from io import BytesIO
from django.core.files.base import ContentFile

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.CharField(max_length=255, blank=True)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_perishable = models.BooleanField()
    expiration_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="products", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    suppliers = models.ManyToManyField(Supplier, through="SupplierProduct", through_fields=("product", "supplier"), blank=True)
    
    def __str__(self):
        return self.name
    
    def _delete_file_if_exists(self, file):
        if file and os.path.isfile(file.path):
            os.remove(file.path)

    def _update_is_perishable(self):
        self.is_perishable = bool(self.expiration_date)

    def _create_thumbnail(self):
        if not self.photo:
            return

        img = Image.open(self.photo)
        size = (30, 30)
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, img.format, quality=85)

        self.thumbnail.save(f"{self.slug}_thumb.jpg", ContentFile(thumb_io.getvalue()), save=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self._update_is_perishable()

        # Salvar o produto primeiro para garantir que temos um arquivo de foto
        super(Product, self).save(*args, **kwargs)

        # Criar e salvar a thumbnail
        self._create_thumbnail()

        # Salvar o produto novamente para registrar a thumbnail
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self._delete_file_if_exists(self.photo)
        self._delete_file_if_exists(self.thumbnail)
        super().delete(*args, **kwargs)
        
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"