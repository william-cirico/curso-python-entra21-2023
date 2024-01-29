from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import SupplierProduct
from .serializers import SupplierProductSerializer
from django.http import Http404

class SupplierProductList(APIView):
    """Lista todos os fornecedores de um produto"""
    def get(self, request, id, format=None):
        supplierProducts = SupplierProduct.objects.filter(product__id=id)
        serializer = SupplierProductSerializer(supplierProducts, many=True)
        
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        try:
            supplierProduct = SupplierProduct.objects.get(id=id)
            supplierProduct.delete()
        except SupplierProduct.DoesNotExist:
            raise Http404
