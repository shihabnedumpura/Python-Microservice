from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class User(models.Model):
     pass