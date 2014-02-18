from django.forms import ModelForm, Select, SelectMultiple
from submissions.models import Submission
from submissions.widgets import ImageUploadWithPreviewWidget

from form_utils.widgets import ImageWidget

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        widgets = {
#            'photo': ImageWidget,
            'assignment': Select(attrs={'class': 'form-control'}),
            'modifiers': SelectMultiple(attrs={'class': 'form-control'})
        }
