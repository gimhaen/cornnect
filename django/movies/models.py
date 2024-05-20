from django.db import models
from django.conf import settings
<<<<<<< HEAD

# 영화
class Movie(models.Model):
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField('Actor', related_name='movies')
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    running_time = models.IntegerField()
    poster_image = models.ImageField(upload_to='movie_posters/')
    reviews_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    talks_count = models.IntegerField(default=0)

=======
>>>>>>> ongyeom

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

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    running_time = models.IntegerField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')
    actors = models.ManyToManyField('Actor', related_name='movies')
    poster_image = models.ImageField(upload_to='movie_posters/')
    likes_count = models.IntegerField(default=0)
    talks_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class MovieTalk(models.Model):
<<<<<<< HEAD
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='talks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='talks')
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='talks')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_talks')
>>>>>>> ongyeom
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"

class MovieTalkReply(models.Model):
    movie_talk = models.ForeignKey('MovieTalk', on_delete=models.CASCADE, related_name='replies')
<<<<<<< HEAD
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='replies')
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_talk_replies')
>>>>>>> ongyeom
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie_talk.content[:10]}..."

class MovieTalkLike(models.Model):
    movie_talk = models.ForeignKey('MovieTalk', on_delete=models.CASCADE, related_name='likes')
<<<<<<< HEAD
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
=======
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_talk_likes')
>>>>>>> ongyeom
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.movie_talk.content[:10]}..."

class Wishlist(models.Model):
<<<<<<< HEAD
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='wishlisted')
=======
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='wishlisted')
>>>>>>> ongyeom
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlisted_movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} added {self.movie.title} to their wishlist"

class Review(models.Model):
<<<<<<< HEAD
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
=======
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
>>>>>>> ongyeom
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    content = models.CharField(max_length=10000)
    review_image = models.ImageField(upload_to='movie_reviews/')
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"

class ReviewLike(models.Model):
<<<<<<< HEAD
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='likes')
=======
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
>>>>>>> ongyeom
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='liked_reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.review.movie.title}"

class ReviewReply(models.Model):
<<<<<<< HEAD
    review = models.ForeignKey('Review', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
=======
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_comments')
>>>>>>> ongyeom
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.review.movie.title}"
