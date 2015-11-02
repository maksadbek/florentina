from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    info = models.TextField()
    img = models.TextField()
