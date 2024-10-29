from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:500] + "  ..."