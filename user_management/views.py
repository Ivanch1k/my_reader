from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from user_management.tasks import task_hello
# Create your views here.


@api_view(["GET", ])
def hello(request):
    task = task_hello.delay()
    print(task.get())
    return HttpResponse('hi :)')
