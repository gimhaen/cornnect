from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
=======
app_name = 'movies'

urlpatterns = [
    path('box-office/', views.box_office, name='box_office'),
]
>>>>>>> ongyeom
