# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    info = models.TextField()
    img = models.ImageField(upload_to='images/%Y/%m/%d')
    category = models.ForeignKey(Category, null=True)
    type = models.ForeignKey(Type, null=True)
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())
    popularity = models.IntegerField()
    

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Flower, self).save(*args, **kwargs)
