from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    title = models.CharField(max_length=50,)
    author = models.ForeignKey(User, related_name='posts')
    date_created = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title



