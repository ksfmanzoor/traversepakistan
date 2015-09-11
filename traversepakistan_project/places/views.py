from django.shortcuts import render
from django.http import HttpResponse, Http404
from models import Place

def index(request):
    return HttpResponse("Places hello")

def details(request):
    try:
        place_name = request.GET.get('name', '')
        place = Place.objects.get(name=place_name)

        context_dict = {
                'place_title': place.title,
                'place_subtitle': place.subtitle,
                }
    except:
        raise Http404("Place does not exist")

    return render(request, 'places/details.html', context_dict)
