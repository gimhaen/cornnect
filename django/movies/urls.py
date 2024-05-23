from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('box-office/', views.box_office, name='box_office'),
    path('<int:tmdb_id>/review/', views.review_create, name="review_create"),
    path('reviews/', views.reviews, name="reviews"),
    path('search/', views.search, name='search'),
    path('<int:tmdb_id>/', views.movie_detail, name="movie_detail"),
    path('<int:tmdb_id>/talks/', views.talks, name="talks"),
    path('<int:tmdb_id>/talk/<int:talk_id>/', views.talk_delete, name="talk_delete"),
    path('<int:tmdb_id>/talk/create/', views.talk_create, name="talk_create"),
    path('popular_movies/', views.popular_movies, name="popular_movies"),
]
