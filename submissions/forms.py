from django.forms import ModelForm
from submissions.models import Photo
from submissions.widgets import ImageUploadWithPreviewWidget

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        widgets = {
            'photo': ImageUploadWithPreviewWidget
        }
