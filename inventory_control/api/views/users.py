from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from api.serializers.user import UserSerializer

@api_view(["PUT"])
def toggle_user_active(request, pk):
    """
    Atualiza o estado de ativo de um usuário.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.is_active = not user.is_active
    user.save()
    
    # Serializando os dados do usuário
    serializer = UserSerializer(user)
    
    return Response(serializer.data)