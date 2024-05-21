# movies/views.py
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor, Director, Genre
from .serializers import MovieSerializer, GenreSerializer
import pprint

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


# 박스오피스
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





# 영화 불러오기 함수
def popluar_movies(request) : 
    ##장르 불러오기
    # url = "https://api.themoviedb.org/3/genre/movie/list?"
    # API_KEY = "68992e4014416feadeedd858d35551c8"
    # headers = {
    #     "accept": "application/json",
    #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ODk5MmU0MDE0NDE2ZmVhZGVlZGQ4NThkMzU1NTFjOCIsInN1YiI6IjY2MzVkZDBhMzU4ZGE3MDEyNzU1Yjk4ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZunSOFVvloD2rKBlNBjxl0yNl6VEzYh3TTCMJH4omA0"
    # }
    # params = {
    #         "api_key": API_KEY,
    #         "language": 'ko-KR',
    #     }

    # response = requests.get(url, headers=headers, params=params).json()
    # serializer = GenreSerializer(data=response['genres'], many=True)
    # if serializer.is_valid():
    #     genre = serializer.save()
    #     print(genre)    

    #----------------------------------------------------
    
    print('-------')
    
    url = "https://api.themoviedb.org/3/movie/popular?language=ko_KR&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ODk5MmU0MDE0NDE2ZmVhZGVlZGQ4NThkMzU1NTFjOCIsInN1YiI6IjY2MzVkZDBhMzU4ZGE3MDEyNzU1Yjk4ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZunSOFVvloD2rKBlNBjxl0yNl6VEzYh3TTCMJH4omA0"
    }
    API_KEY = "68992e4014416feadeedd858d35551c8"
    
    for i in range(1, 2) :
        params = {
            "api_key": API_KEY,
            "language": 'ko-KR',
            "page": i
        }
                
        response = requests.get(url, headers=headers, params=params)
        
        tmdb_movies = response.json().get('results', [])
        
        #내감 만든 시리얼 라이저에 넣을 딕셔너리 데이터
        #저장 
   
        for tmdb_movie in tmdb_movies:
            # pprint.pprint(tmdb_movie)
            movie_data = {
                'tmdb_id': tmdb_movie['id'],
                'title': tmdb_movie['title'],
                'description': tmdb_movie['overview'],
                'genre': tmdb_movie.get('genre_ids', []),
                'release_year': tmdb_movie['release_date'].split('-')[0],
                'running_time': tmdb_movie.get('runtime', -1),
                'poster_image': f"https://image.tmdb.org/t/p/w500{tmdb_movie['poster_path']}",
            }

            
            
            detail_url = f"https://api.themoviedb.org/3/movie/{tmdb_movie['id']}?"

            detail_headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ODk5MmU0MDE0NDE2ZmVhZGVlZGQ4NThkMzU1NTFjOCIsInN1YiI6IjY2MzVkZDBhMzU4ZGE3MDEyNzU1Yjk4ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZunSOFVvloD2rKBlNBjxl0yNl6VEzYh3TTCMJH4omA0"
            }
            detail_params = {
                "api_key": API_KEY,
                "language": 'ko-KR',
            }
            detail_response = requests.get(detail_url, headers=detail_headers, params=detail_params).json()
            movie_data['running_time'] = detail_response['runtime']
            pprint.pprint(detail_response)

            # pprint.pprint(tmdb_movie)
            # ['id', 'title', 'description', 'genre', 'release_year', 'running_time', 'director', 'actors', 'poster_image', 'likes_count', 'talks_count']
            serializer = MovieSerializer(data=movie_data)
            # print(serializer.data)
            print('1')
            if serializer.is_valid():
                print('2')
                movie = serializer.save()
                genres = tmdb_movie.get('genres', [])
                for genre_data in genres:
                    genre = Genre.objects.get_or_create(name=genre_data['name'])
                    movie.genres.add(genre)

            if serializer.is_valid():
                serializer.save() 
            else:
                print(serializer.errors)
            

    return JsonResponse(serializer.data)

