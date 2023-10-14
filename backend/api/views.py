from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from authentication.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, generics, filters
from django.shortcuts import get_object_or_404

#---------- users api ----------------
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserApiView(request, username):
    user = User.objects.get(username=username)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def UserIDApiView(request, pk):
    user = User.objects.get(id=pk)
    serializer = UsersSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdataUserApiView(request, pk):
    user = User.objects.get(id=pk)
    serializer = UsersSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name']

#------------- Profile API

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ProfilesApiView(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def ProfileApiView(request, user):
    profile = Profile.objects.get(user=user)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def UpdataProfileApiView(request, user):
    profile = Profile.objects.get(user=user)
    serializer = ProfileSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)