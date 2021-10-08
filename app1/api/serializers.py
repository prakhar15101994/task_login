from rest_framework import serializers
from app1.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password', 'address']