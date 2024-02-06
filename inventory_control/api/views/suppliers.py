from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.supplier import SupplierSerializer
from suppliers.models import Supplier


@api_view(["PUT"])
def toggle_supplier_active(request, pk):
    """
    Atualiza o estado de ativo de um fornecedor.
    """
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    supplier.is_active = not supplier.is_active
    supplier.save()
    
    serializer = SupplierSerializer(supplier)
    
    return Response(serializer.data)