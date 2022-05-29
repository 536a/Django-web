from django.forms import ModelForm
from .models import *

class AddNewExhibitionForm(ModelForm):

    class Meta:
        model = Exhibitions
        fields = ['name', 'description', 'release_date','thumbnail']