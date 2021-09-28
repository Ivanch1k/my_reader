from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User, Group


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )
