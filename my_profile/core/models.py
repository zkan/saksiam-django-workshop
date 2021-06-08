from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300)
    short_bio = models.TextField()
    github_url = models.CharField(max_length=300)
    facebook_url = models.CharField(max_length=300)
    twitter_url = models.CharField(max_length=300)


class Subscriber(models.Model):
    email = models.EmailField()
