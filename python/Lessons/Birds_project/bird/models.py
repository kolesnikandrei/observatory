from django.db import models

# Create your models here.


class Bird(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    color = models.CharField(max_length=30)
    body_length = models.IntegerField()
    wingspan = models.IntegerField()

    def __str__(self):
        return self.name