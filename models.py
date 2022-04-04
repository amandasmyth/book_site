from django.db import models


# Create your models here.
class Author(models.Model):

    about = models.TextField()
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)


def __str__(self):
        return self.about




