from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('box-office/', views.box_office, name='box_office'),
    path('<int:movie_id>/review/', views.review_create, name="review_create"),
    path('reviews/', views.reviews, name="reviews"),
    path('search/', views.search, name='search'),
    path('<int:tmdb_id>/', views.movie_detail, name="movie_detail"),
    path('popular_movies/', views.popular_movies, name="popular_movies"),
]
