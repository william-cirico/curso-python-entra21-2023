from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.product import SupplierProductSerializer, ProductSerializer
from products.models.product import Product
from products.models.supplier_product import SupplierProduct


@api_view(["DELETE"])
def delete_supplier_from_product(request, pk):
    """
    Remove um fornecedor de um produto
    """
    try:
        supplierProduct = SupplierProduct.objects.get(pk=pk)
    except SupplierProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    supplierProduct.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_suppliers_from_product(request, pk):
    """
    Obtém os fornecedores de um produto.
    """
    suppliers = SupplierProduct.objects.filter(product__id=pk)
        
    serializer = SupplierProductSerializer(suppliers, many=True)
        
    return Response(serializer.data)


@api_view(["PUT"])
def toggle_product_active(request, pk):
    """
    Atualiza o estado de ativo de um produto.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.is_active = not product.is_active
    product.save()
    
    serializer = ProductSerializer(product)
    
    return Response(serializer.data)