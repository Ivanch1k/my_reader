from django.shortcuts import render
from django.contrib.auth.models import User, Group
from oauth.serializers import UserSerializer, GroupSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope


# Create your views here.
class UserDetails(RetrieveAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(ListCreateAPIView):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(ListAPIView):
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(["POST"])
def send_request_to_git_hub(request):

    return Response("success")
