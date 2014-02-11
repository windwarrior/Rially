from django.forms import ModelForm
from submissions.models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
