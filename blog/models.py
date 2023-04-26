from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro= models.TextField()
    body = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
