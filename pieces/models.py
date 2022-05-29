from django.db import models
from django.utils.translation import gettext_lazy as _

piece_choices={
    ('resim','RESİM'),
    ('heykel','HEYKEL'),
    ('fotograf','FOTOĞRAF'),
    ('cini','ÇİNİ'),
    ('deri','DERİ'),
    ('seramik', 'SERAMİK'),
    ('oymacılık', 'OYMACILIK'),
    ('cam', 'CAM'),
    ('ebru', 'EBRU')
}

class Pieces(models.Model):
    exhibition_id = models.IntegerField(null=True,blank=True)
    name = models.CharField( max_length=100)
    owner_id = models.IntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20,choices=piece_choices,default='resim')
    click_counter = models.IntegerField(default = 0)
    picture_url = models.ImageField(upload_to='pieces/')
    price = models.CharField(default="Belirtilmemiş",max_length=20)
    release_date = models.DateField()
    

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
    