from django.forms import ModelForm, Select, SelectMultiple
from submissions.models import Submission
from submissions.widgets import ImageUploadWithPreviewWidget

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        widgets = {
            'photo': ImageUploadWithPreviewWidget,
            'assignment': Select(attrs={'class': 'form-control'}),
            'modifiers': SelectMultiple(attrs={'class': 'form-control'})
        }
