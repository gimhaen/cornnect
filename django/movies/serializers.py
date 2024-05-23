# movies/serializers.py
from rest_framework import serializers
from .models import Movie, Actor, Director, Genre, Review, Talk
from accounts.models import CustomUser

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    director = DirectorSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = ['likes_count', 'talks_count',]

class ReviewSerialzer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = "__all__"

    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['movie', 'review_image']
        
class TalkSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = "__all__"
    user = UserSerializer(read_only=True)

    class Meta:
        model = Talk
        fields = '__all__'
        read_only_fields = ['movie', 'user']
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = CustomUser
    #         fields = "__all__"
        
    # user = UserSerializer(read_only=True)
    # movie = MovieSerializer(read_only=True)
    # class Meta:
    #     model = Talk
    #     fields = '__all__'