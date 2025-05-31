from django.urls import path 
from . import views 

urlpatterns = [
    path('magazines/', views.getMagazines, name="magazines"),
    path('magazine/<slug:slug>/', views.getMagazineInfo, name="magazine"),
    path('author/<str:username>/', views.getAuthorInfo, name="author"),
    path('author/<str:username>/publications/', views.getAuthorPublications, name="authorPublications"),
]