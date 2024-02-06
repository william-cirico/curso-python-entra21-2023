from rest_framework import serializers

from products.models.supplier_product import SupplierProduct
from products.models.product import Product
     
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
              
class SupplierProductSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField()
    
    class Meta:
        model = SupplierProduct
        fields = ["id", "supplier", "price"]
        
    def get_supplier(self, obj):
        return obj.supplier.fantasy_name