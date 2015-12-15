from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    img = models.ImageField(upload_to='images/%Y/%m/%d')
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())
    

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(News, self).save(*args, **kwargs)