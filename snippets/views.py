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
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'snippets':reverse('snippetd', request=request, format=format)
        "list":"snippets/",
        "detail":"snippets/id/",
        "highlighted":"snippets/id/highlight/",
    })

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    









    
    



