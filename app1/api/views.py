from app1.models import User
from app1.api.serializers import UserSerializers
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    # authentication_classes=[SessionAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    