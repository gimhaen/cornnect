# movies/views.py
import requests
import pprint
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q, Case, When, Value, IntegerField
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response

from .models import *
from .serializers import *

# 박스오피스
@api_view(['GET'])
def box_office(request):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    params = {
        'key': '2083a37ad3c34c2ad3a8f96bbbaeba31',
        'targetDt': '20190102'  # 기본값으로 오늘 날짜를 설정합니다.
    }
    # response = requests.get(url)
    # request.GET.get('targetDt', '20230501')
    response = requests.get(url, params=params)
    # print(response)
    data = response.json()
    return JsonResponse(data)

# 영화 검색 
def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('searchTerm', '')
        search_results = Movie.objects.filter(
    Q(title__icontains=search_term) |
    Q(actors__name__icontains=search_term) |
    Q(director__name__icontains=search_term) |
    Q(genres__name__icontains=search_term),
    # tmdb_id__in=Movie.objects.values('tmdb_id')
).distinct()[:50]
       
        
        serializer = MovieSerializer(search_results, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)

# 영화 상세

def movie_detail(request, tmdb_id):
    print('-')
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    print(movie)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def review_create(request, movie_id):
    # print('dd')
    movie = Movie.objects.get(pk=movie_id)
    print(movie)
    if request.method == 'GET' :
        print(movie.review_set.all())
        
    elif request.method == 'POST' :
        # print('22')
        # print(request.FILES.get('review_image'))
        serialzer = ReviewSerialzer(data=request.data)
        if serialzer.is_valid(raise_exception=True):
            serialzer.save(movie=movie, user=request.user, review_image=request.FILES.get('review_image'))
            return Response(serialzer.data)

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def reviews(request):
    reviews = Review.objects.all()
    serialzer = ReviewSerialzer(reviews, many=True)
    
    return Response(serialzer.data)

# 영화 검색 
def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('searchTerm', '')
        search_results = Movie.objects.filter(
    Q(title__icontains=search_term) |
    Q(actors__name__icontains=search_term) |
    Q(director__name__icontains=search_term) |
    Q(genres__name__icontains=search_term),
    # tmdb_id__in=Movie.objects.values('tmdb_id')
).distinct()[:50]
       
        
        serializer = MovieSerializer(search_results, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'POST 요청이 필요합니다.'}, status=400)

# 영화 상세

def movie_detail(request, tmdb_id):
    print('-')
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    print(movie)
    serializer = MovieSerializer(movie)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def talk_create(request, tmdb_id):
    print(tmdb_id)
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    serializer = TalkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def talk_delete(request, tmdb_id, talk_id):
    print('DELETE')
    print(tmdb_id)
    print(talk_id)
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    talk = get_object_or_404(Talk, id=talk_id, movie=movie)
    if talk.user != request.user:
        return Response({'error': 'You are not allowed to delete this talk.'}, status=status.HTTP_403_FORBIDDEN)
    talk.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def talks(request, tmdb_id):
    print(tmdb_id)
    movie = get_object_or_404(Movie, tmdb_id=tmdb_id)
    talks = movie.talks.all().order_by('-created_at')
    serializer = TalkSerializer(talks, many=True)
    return Response(serializer.data)

## 영화데이터 불러오기 함수
def popular_movies(request) : 
    API_KEY = "68992e4014416feadeedd858d35551c8"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ODk5MmU0MDE0NDE2ZmVhZGVlZGQ4NThkMzU1NTFjOCIsInN1YiI6IjY2MzVkZDBhMzU4ZGE3MDEyNzU1Yjk4ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZunSOFVvloD2rKBlNBjxl0yNl6VEzYh3TTCMJH4omA0"
    }
    
    # 장르 불러오기
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
            "api_key": API_KEY,
            "language": 'ko-KR',
        }

    genre_response = requests.get(genre_url, headers=headers, params=params).json()
    serializer = GenreSerializer(data=genre_response['genres'], many=True)
    if serializer.is_valid():
        genre = serializer.save()    

   
    # 인기 영화 불러오기
    popular_url = "https://api.themoviedb.org/3/movie/popular"
    
    for i in range(1, 51) : # 페이지 수 조정
        params = {
            "api_key": API_KEY,
            "language": 'ko-KR',
            "page": i
        }
                
        popular_response = requests.get(popular_url, headers=headers, params=params)
        
        tmdb_movies = popular_response.json().get('results', [])
        
        #내가 만든 시리얼 라이저에 넣을 딕셔너리 데이터 저장
        for tmdb_movie in tmdb_movies:
            genre_ids = tmdb_movie.get('genre_ids', [])
            genres = Genre.objects.filter(id__in=genre_ids)
            # pprint.pprint(tmdb_movie)

            movie_data = {
                'tmdb_id': tmdb_movie['id'],
                'title': tmdb_movie['title'],
                'description': tmdb_movie['overview'],
                # 'genre': tmdb_movie.get('genre_ids', []),
                'release_year': tmdb_movie['release_date'].split('-')[0],
                'running_time': tmdb_movie.get('runtime', 0),
                'poster_image': f"https://image.tmdb.org/t/p/w500{tmdb_movie['poster_path']}",
                'director': None,
                'actors': [],
            }
            


            
            # 영화 상세 정보 가져오기
            detail_url = f"https://api.themoviedb.org/3/movie/{tmdb_movie['id']}"
            
            detail_params = {
                "api_key": API_KEY,
                "language": 'ko-KR',
            }
            detail_response = requests.get(detail_url, headers=headers, params=detail_params).json()
            # print(detail_response)
            movie_data['running_time'] = detail_response.get('runtime', 0)
            # pprint.pprint(detail_response)

            # pprint.pprint(tmdb_movie)
            # ['id', 'title', 'description', 'genre', 'release_year', 'running_time', 'director', 'actors', 'poster_image', 'likes_count', 'talks_count']
    
            serializer = MovieSerializer(data=movie_data)
            # print(movie_data)
            # print(serializer.data)
            if serializer.is_valid():      
                movie = serializer.save()
                
                # 장르를 영화에 추가
                genre_ids = tmdb_movie.get('genre_ids', [])
                genres = Genre.objects.filter(id__in=genre_ids)
                movie.genres.set(genres)
                movie.save()
                
                
                # print(movie)
            # if serializer.is_valid():
            #     serializer.save() 
            else:
                print('error')
                print(serializer.errors)
                continue
            
            
            
            ## 배우, 감독 정보 가져오기
            credits_url = f"https://api.themoviedb.org/3/movie/{tmdb_movie['id']}/credits"
            credits_params = {
                "api_key": API_KEY,
                "language": 'ko-KR',
            }
            credits_response = requests.get(credits_url, headers=headers, params=credits_params).json()
            cast = credits_response.get('cast', [])[:5]
            crew = credits_response.get('crew', [])
            tmdb_id = credits_response.get('id')
            # print(tmdb_id)
            
            # 배우 정보 추출
            for actor_data in cast:
                actor_info = {
                    'tmdb_id': tmdb_id,
                    'name': actor_data['name'],
                    'profile_image': f"https://image.tmdb.org/t/p/w500{actor_data['profile_path']}"
                }
                # print(f'actor_info: {actor_info}')
                serializer = ActorSerializer(data=actor_info)
                if serializer.is_valid() :
                    actor = serializer.save()
                    movie.actors.add(actor)
                    movie.save()

            
            # 감독 정보 추출
            for crew_data in crew:
                if crew_data['department'] == 'Directing' and crew_data['job'] == 'Director':
                    director_info = {
                        'tmdb_id': tmdb_id,
                        'name': crew_data['name'],
                        'profile_image': f"https://image.tmdb.org/t/p/w500{crew_data['profile_path']}"
                    }
                    serializer = DirectorSerializer(data=director_info)
                    if serializer.is_valid() :
                        director = serializer.save()
                        movie.director = director
                        movie.save()
                    
                    
    return JsonResponse(serializer.data)
