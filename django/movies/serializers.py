# movies/serializers.py
from rest_framework import serializers
from .models import Movie, Actor, Director, Genre

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'profile_image']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'profile_image']

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ['likes_count', 'talks_count', 'director', 'actors']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
