# movies/views.py
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Movie
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view

def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_detail.html', context)

@api_view(['GET'])
def box_office(request):
    print('dfdfdf')
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    params = {
        'key': '2083a37ad3c34c2ad3a8f96bbbaeba31',
        'targetDt': '20190102'  # 기본값으로 오늘 날짜를 설정합니다.
    }
    # response = requests.get(url)
    # request.GET.get('targetDt', '20230501')
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    return JsonResponse(data)
