from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('box-office/', views.box_office, name='box_office'),
]