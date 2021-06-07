from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=300)