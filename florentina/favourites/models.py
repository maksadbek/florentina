from django.db import models
from accounts.models import CustomUser
from flowers.models import Flower

class Favourite(models.Model):
    user = models.ForeignKey(CustomUser)
    flower = models.ForeignKey(Flower)
    created_at = models.DateTimeField(auto_now_add=True)
