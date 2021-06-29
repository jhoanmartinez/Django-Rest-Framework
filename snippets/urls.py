from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list, name="snippet_list_name"),
    path('snippets/<int:pk>/', views.snippet_detail, name="snippet_detail"),
]