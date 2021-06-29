from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from snippets.serializers import *
from snippets.models import *
from rest_framework.views import APIView


class SnippetList(APIView):
    def get(self, request, format=None):
        """
        snnipets list
        """
        if request.method == "GET":
            snnipets = Snippet.objects.all()
            serializer = SnippetSerializer(snnipets, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        if request.method == "POST":
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, request, pk, format=None):
        try:
            snnipet = Snippet.objects.filter(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(self, pk, request, format=None)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(self, request, pk, format=None)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










    
    



