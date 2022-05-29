from django.forms import ModelForm
from .models import *

class AddNewPieceForm(ModelForm):

    class Meta:
        model = Pieces
        fields = ['name','description','price','picture_url','category']