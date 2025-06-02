from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('csrf/', views.get_csrf_token, name='get-csrf'),
    path('magazines/', views.getMagazines, name="magazines"),
    path('categories/', views.get_categories, name="categories"),
    path('author/<str:username>/', views.getAuthorInfo, name="author"),
    path('authorImage/<str:username>/', views.getAuthorImgUrl, name="get_author_image"),
    path('magazine/create', views.createMagazine, name="create_magazine"),
    path('magazines/<slug:slug>/', views.getMagazineInfo, name="magazine"),
    path('author/<str:username>/publications/', views.getAuthorPublications, name="authorPublications"),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)