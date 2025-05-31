from django.shortcuts import render
from django.http import JsonResponse
from .models import Author, Magazine
from django.shortcuts import get_object_or_404

# Create your views here.
allMagazines = [
    {
    "id": 1,
    "title": "A (Worthless)? war on drugs?",
    "slug": "war-on-drugs",
    "about": "A war on drugs for what?",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "tanvir",
    "date": "15, March 2025",
    "readTime": "7 min",
    "category": "Thoughts",
    "coverImage": "https://images.unsplash.com/photo-1582562124811-c09040d0a901?w=400&h=300&fit=crop",
    "featured": True
  },
  {
    "id": 2,
    "title": "Don't close your eyes",
    "slug": "dont-close-your-eyes",
    "about": "A powerful visual journey through contemporary art that challenges viewers to confront uncomfortable truths about society.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "Tanvirul islam",
    "date": "15, March 2024",
    "readTime": "5 min",
    "category": "ART",
    "coverImage": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=400&h=300&fit=crop",
    "featured": False
  },
  {
    "id": 3,
    "title": "The best art museums",
    "slug": "best-art-museums",
    "about": "A curated guide to the world's most influential art museums and the masterpieces that define our cultural heritage.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "Tanvirul Islam",
    "date": "15, March 2024",
    "readTime": "10 min",
    "category": "CULTURE",
    "coverImage": "https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=400&h=300&fit=crop",
    "featured": True
  },
  {
    "id": 5,
    "title": "The devil is the details",
    "slug": "devil-details",
    "about": "An intimate look at how small elements in art and design create profound impact and emotional resonance.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "Tanvirul Islam",
    "date": "15, March 2024",
    "readTime": "12 min",
    "category": "ART",
    "coverImage": "https://images.unsplash.com/photo-1649972904349-6e44c42644a7?w=400&h=300&fit=crop",
    "featured": False
  },
  {
    "id": 6,
    "title": "An indestructible hope",
    "slug": "indestrictible-hope",
    "about": "Stories of human resilience and the unbreakable spirit that emerges in times of crisis and transformation.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "Tanvirul Islam",
    "date": "15, March 2024",
    "readTime": "8 min",
    "category": "ART",
    "coverImage": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=400&h=300&fit=crop",
    "featured": True
  },
  {
    "id": 7,
    "title": "Street art festival",
    "slug": "art-festival",
    "about": "Documenting the vibrant street art scene and the artists who transform urban landscapes into living galleries.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "author": "Tanvirul Islam",
    "date": "15, March 2024",
    "readTime": "6 min",
    "category": "PHOTOGRAPHY",
    "coverImage": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=300&fit=crop",
    "featured": False
  }   
]

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
    "content": magazineObject.excerpt,
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
