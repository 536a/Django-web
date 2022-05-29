
# Create your models here.
from django.db import models
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy as _

class PiecePermissions(models.Model):

    sender = models.IntegerField()
    receiver = models.IntegerField()
    exh_id = models.IntegerField()
    date = models.DateTimeField(_('date joined'),auto_now_add=True)
    is_active = models.BooleanField(default = 1)

    REQUIRED_FIELDS = []

    def str(self):
        return self.name


class Follows(models.Model):
	
	follower_id = models.IntegerField()
	followed_id = models.IntegerField()

	REQUIRED_FIELDS = []

	


class Likes(models.Model):

	liker_id = models.IntegerField()
	piece_id = models.IntegerField()

	REQUIRED_FIELDS = []

	


class Comments(models.Model):
	commentator_id = models.IntegerField()
	piece_id = models.IntegerField()
	comment = models.CharField(max_length=300)
	date = models.DateTimeField(auto_now_add=True)

	REQUIRED_FIELDS = []

	
class Interests(models.Model):
	user_id = models.IntegerField()
	painting = models.IntegerField(default=0)
	sculpture = models.IntegerField(default=0)
	photograph = models.IntegerField(default=0)
	tile = models.IntegerField(default=0)
	leather = models.IntegerField(default=0)
	ceramic = models.IntegerField(default=0)
	carving = models.IntegerField(default=0)
	glass = models.IntegerField(default=0)
	marbling = models.IntegerField(default=0)

	REQUIRED_FIELDS = []