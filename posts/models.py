from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=0)
