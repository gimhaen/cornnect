from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(pk=user.pk).exists()
