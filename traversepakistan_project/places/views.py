from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.templatetags.static import static
from django.conf import settings
import os, sys
from models import Place

def index(request):
    return HttpResponse("Places hello")

def details(request):
    place_name = request.GET.get('name', '')
    place = Place.objects.get(name=place_name)
    images_directory = os.path.join(settings.STATICFILES_DIRS[0], 'images')

    images = []
    thumbnails = []
    for filename in os.listdir(os.path.join(images_directory, 'gallerys', place_name)):
        images.append(static('images/gallerys/' + place_name + '/' + filename))
        thumbnails.append(static('images/gallery-thumbnails/' + place_name + '/' + filename))

    context_dict = {
        'place': place,
        'galleryZip': zip(images, thumbnails)
    } 

    print >> sys.stderr, zip(images, thumbnails)

    return render(request, 'places/details.html', context_dict)
