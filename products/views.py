from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from products.serializers import RegistrationSerializer

# Create your views here.

@api_view(['POST'])
# enable permissions for registration to all
@permission_classes([])
def registration_view(request):
    registration_data = request.data

    serializer = RegistrationSerializer(data=registration_data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
