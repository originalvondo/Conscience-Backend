from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('csrf/', views.get_csrf_token, name='get-csrf'),
    path('magazines/', views.getMagazines, name="magazines"),
    path('magazine/<slug:slug>/', views.getMagazineInfo, name="magazine"),
    path('magazine/create', views.createMagazine, name="create_magazine"),
    path('author/<str:username>/', views.getAuthorInfo, name="author"),
    path('author/<str:username>/publications/', views.getAuthorPublications, name="authorPublications"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
