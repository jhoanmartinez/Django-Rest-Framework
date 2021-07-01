from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from snippets.serializers import *
from snippets.models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


class SnippetList(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


    def get(self, request, format=None):
        """
        snnipets list
        """
        if request.method == "GET":
            snnipets = Snippet.objects.all()
            serializer = SnippetSerializer(snnipets, many=True)
            return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def post(self, request, format=None):
        """
        Create new snippet
        """
        if request.method == "POST":
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










    
    



