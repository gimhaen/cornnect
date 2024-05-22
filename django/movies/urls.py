from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('box-office/', views.box_office, name='box_office'),
    path('popular_movies/', views.popular_movies, name="popular_movies"),
    path('search/', views.search, name='search'),
    
]
