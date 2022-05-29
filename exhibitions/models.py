from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.utils.translation import gettext_lazy as _



class Exhibitions(models.Model):
  
    release_date = models.DateField()
    name = models.CharField(max_length=100)
    owner_id = models.IntegerField()
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to='exhibitions/thumbnails')
    

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
    