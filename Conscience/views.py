import json
from django.http import JsonResponse
from django.utils.text import slugify
from django.middleware.csrf import get_token
from .models import Author, Magazine, Category
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

# Create your views here.
def getMagazines(request):
    magazines = Magazine.objects.all()
    allMagazines = [
        {
            "id": magazine.id,
            "title": magazine.title,
            "slug": magazine.slug,
            "about": magazine.about,
            "content": magazine.content,  
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

def getAuthorsInfo(request): 
  authors = Author.objects.all()
  allAuthors = []
  for author in authors: 
    authorData = {
      "name": author.name,
      "username": author.username,
      "articles": list(author.magazines.all().values_list('title', flat="true")),
      "categories": ["art", "thoughts", "creativity"], 
      "bio": author.bio
    }
    allAuthors.append(authorData)

  return JsonResponse(allAuthors, safe=False)

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
        "totalArticles": len(list(author.magazines.all().values_list('title', flat="true"))),
        "articles": [
          article.id for article in author.magazines.all()
        ]
      }       
    }
  
  return JsonResponse(authorInfo)

def getAuthorImgUrl(request, username):
  author = Author.objects.get(username=username)
  imgUrl = author.image
  return JsonResponse(imgUrl, safe=False)

def getAuthorPublications(request, username):
    author = get_object_or_404(Author, username=username)
    authorPublications = Magazine.objects.filter(author=author)

    magazines = [
      {
        "id": magazine.id,
        "title": magazine.title,
        "slug": magazine.slug,
        "about": magazine.about,
        "content": magazine.content,  
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

@ensure_csrf_cookie
def get_csrf_token(request):
    # This will set the csrftoken cookie AND return the token
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def createMagazine(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    title         = data.get('title', '').strip()
    about         = data.get('about', '')
    content       = data.get('content', '')
    author_slug   = data.get('author')     
    category_name = data.get('category')  
    cover_image   = data.get('cover_image', '')
    date_str      = data.get('date')
    
    # minimal required-field check
    if not (title and author_slug and category_name and date_str):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    # lookup by slug / name
    author   = get_object_or_404(Author, username=author_slug)
    category = get_object_or_404(Category, name=category_name)

    
    date = parse_datetime(date_str)
    if date is None:
        return JsonResponse({'error': 'Invalid date format'}, status=400)

    mag = Magazine(
        title=title,
        about=about,
        content=content,
        author=author,
        date=date,
        category=category,
        cover_image=cover_image,
        featured=False,
    )
    mag.slug = slugify(title)
    mag.save()
    
    print(f"model saved")

    return JsonResponse({
        'id': mag.id,
        'slug': mag.slug,
        'created_at': mag.created_at.isoformat(),
    }, status=201)
    
def get_categories(request):
  categores = [category.name for category in Category.objects.all()]
  return JsonResponse(categores, safe=False)