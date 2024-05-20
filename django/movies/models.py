from django.db import models
from django.contrib.auth.models import User
from .models import Actor, Director

# 영화
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    running_time = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    poster_image = models.ImageField(upload_to='movie_posters/')
    likes_count = models.IntegerField(default=0)
    talks_count = models.IntegerField(default=0)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='actor_profiles/', null=True, blank=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='director_profiles/', null=True, blank=True)

    def __str__(self):
        return self.name


class MovieTalk(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='talks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='talks')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class Wishlist(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='wishlisted')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlisted_movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} added {self.movie.title} to their wishlist"



# 리뷰(유저-영화)
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    content = models.CharField(max_length=100)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"


class LikeReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.review.movie.title}"


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.review.movie.title}"

