from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .serializers import UserSerializer

from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create':
#             permission_classes = [AllowAny]
#         elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [IsLoggedInUserOrAdmin]
#         elif self.action == 'list' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)
