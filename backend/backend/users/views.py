from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .models import User


@api_view(['POST'])
def register(request):
    md = request.data
    if md['password'] != md['password_conform']:
        raise APIException('Password not equal')
    print(md)
    return Response('OK')


@api_view(['GET'])
def users(request):
    all_users = User.objects.all()
    return Response(all_users)
