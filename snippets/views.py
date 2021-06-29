from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.serializers import *
from snippets.models import *

@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    snnipets list
    """
    if request.method == "GET":
        snnipets = Snippet.objects.all()
        serializer = SnippetSerializer(snnipets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snnipet = Snippet.objects.filter(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SnippetSerializer(snnipet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snnipet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        snnipet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









    
    



