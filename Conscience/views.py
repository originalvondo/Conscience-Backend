from django.shortcuts import render
from django.http import JsonResponse
from .models import Author, Magazine
from django.shortcuts import get_object_or_404

# Create your views here.
def getMagazines(request):
    magazines = Magazine.objects.all()
    allMagazines = [
        {
            "id": magazine.id,
            "title": magazine.title,
            "slug": magazine.slug,
            "about": magazine.about,
            "content": magazine.excerpt,  
            "author": magazine.author.username, 
            "date": magazine.date.strftime("%d, %B %Y"),  
            "readTime": magazine.read_time,
            "category": magazine.category.name, 
            "coverImage": magazine.cover_image,
            "featured": magazine.featured,
        }
        for magazine in magazines
    ]
    return JsonResponse(allMagazines, safe=False)

def getMagazineInfo(request, slug):
  magazineObject = Magazine.objects.get(slug=slug)
  magazine = {
    "id": magazineObject.id,
    "title": magazineObject.title,
    "slug": magazineObject.slug,
    "about": magazineObject.about,
    "content": magazineObject.content,
    "author": magazineObject.author.username,
    "date": magazineObject.date.strftime("%d, %B %Y"),
    "readTime": magazineObject.read_time,
    "category": magazineObject.category.name,
    "coverImage": magazineObject.cover_image,
    "featured": magazineObject.featured
  }

  return JsonResponse(magazine)

def getAuthorInfo(request, username):
  author = Author.objects.get(username=username)
  authorInfo = {
    "author" : {
        "name": author.name,
        "username": author.username ,
        "bio": author.bio,
        "image": author.image,
        "location": author.location,
        "email": author.email,
        "website": author.website,
        "totalArticles": author.total_articles,
        "articles": [
          1, 231, 52 # article id's
        ]
      }       
    }
  
  return JsonResponse(authorInfo)


def getAuthorPublications(request, username):
    author = get_object_or_404(Author, username=username)
    authorPublications = Magazine.objects.filter(author=author)

    magazines = [
      {
        "id": magazine.id,
        "title": magazine.title,
        "slug": magazine.slug,
        "about": magazine.about,
        "content": magazine.excerpt,  
        "author": magazine.author.username,  
        "date": magazine.date.strftime('%Y-%m-%d'), 
        "readTime": magazine.read_time,
        "category": magazine.category.name,  
        "coverImage": magazine.cover_image,
        "featured": magazine.featured,
      }
        for magazine in authorPublications
    ]

    return JsonResponse(magazines, safe=False)
