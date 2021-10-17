from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, JobSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer



class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request):
        serializer = PostSerializer(
        data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(company=request.user)
        return Response(serializer.data)
