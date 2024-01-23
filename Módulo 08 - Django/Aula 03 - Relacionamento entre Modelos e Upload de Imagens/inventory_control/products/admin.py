from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sale_price", "is_perishable", "expiration_date", "enabled"]
    exclude = ["slug", "thumbnail"]
    ordering = ["-id"] # Padrão
    list_filter = ["enabled"]
    search_fields = ["name"]
    list_display_links = ["name"]
    list_editable = ["sale_price", "is_perishable", "expiration_date", "enabled"]
    list_per_page = 100
    list_max_show_all = 1000