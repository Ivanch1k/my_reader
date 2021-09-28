from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http.response import HttpResponse

import my_reader.settings
from user_management.tasks import task_hello
import requests
# Create your views here.


@api_view(["GET", ])
def hello_celery(request):
    task = task_hello.delay()
    print(task.get())
    return HttpResponse('hi :)')


@api_view(["GET", ])
@permission_classes([AllowAny])
def hello(request):
    print(request.GET)
    print(request.data)
    return HttpResponse('hi :)')


@api_view(["GET", ])
@permission_classes([AllowAny])
def authorize(request):
    response = requests.get("https://github.com/login/oauth/authorize", params=my_reader.settings.GITHUB_CLIENT_ID)
    print(response)
    return Response(response)


@api_view(["GET", ])
@permission_classes([AllowAny])
def authorized(request):
    code = request.GET['code']
    data = {
        "client_id": my_reader.settings.GITHUB_CLIENT_ID,
        "client_secret": my_reader.settings.GITHUB_CLIENT_SECRET,
        "redirected_uri": "http://localhost:8000/authorized/",
        "code": code
    }
    response = requests.post("https://github.com/login/oauth/access_token", data=data)
    print(response.json())
    return Response(response.json())
