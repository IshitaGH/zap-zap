# from backend.zap_zap import api
from re import search
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User, Profile
from photo_upload.models import Target
from .serializers import TargetSerializer, UserSerializer, ProfileSerializer
import logging
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json
from django.http import JsonResponse

# from backend.zap_zap.api import serializers

# from backend.zap_zap.api import serializers
# from backend.zap_zap.api import serializers
# from backend.zap_zap.api import serializers

# add stuff like post, put delete
@api_view(['GET'])
def get_user_data(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

# TODO: does posting the user, also post the profile?
# TODO: FIX!!!! does not currently save any data to the database?
@api_view(['POST'])
def add_user(request):
    body = request.data
    username = body['username']
    password = body["password"]

    user = User.objects.create(username=username, password=password)
    user.save()
    
    return Response("cool")

@api_view(['GET'])
def get_profile_data(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many = True)
    return Response(serializer.data)

# @api_view(['POST'])
# def add_profile(request):
#     serializer = ProfileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['GET'])
def get_target_data(request):
    targets = Target.objects.all()
    serializer = TargetSerializer(targets, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def add_target(request):
    serializer = TargetSerializer(data=request.data)
    if serializer.is_valid():
        print("fdsa")
        print()
        print()
        print()
        serializer.save()
    return Response(serializer.data)
    # data = JSONParser().parse(request)
    # serializer = TargetSerializer(data=data)
    # if serializer.is_valid():
    #     TargetSerializer.save()
    #     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
    # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)