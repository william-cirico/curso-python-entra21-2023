from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    sale_price = models.DecimalField()
    is_perishable = models.BooleanField()
    expiration_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="products", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="thumbnails", blank=True)
    enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Gerando slug
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
        # Gerando thumbnail
        img = Image.open(self.photo.path)
        
        # Redimensionar a imagem
        size = (30,30)
        img.thumbnail(size)
        
        # Salvar a imagem redimensionada
        thumb_io = BytesIO()
        img.save(thumb_io, img.format, quality=85)
        
        # Criar um nome para a thumbnail
        name, extension = os.path.splitext(self.photo.name)
        thumb_filename = f"{name}_thumb{extension}"
        
        # Salvando a miniatura
        self.thumbnail.save(thumb_filename, ContentFile(thumb_io.getvalue()), save=False)
        super(Product, self).save(*args, **kwargs)
        
        
        
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"