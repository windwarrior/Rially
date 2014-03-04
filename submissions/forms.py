from django.forms import ModelForm, Select, SelectMultiple, ValidationError
from submissions.models import Submission
from submissions.widgets import ImageUploadWithPreviewWidget

#from form_utils.widgets import ImageWidget

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['photo','assignment','modifiers']
        widgets = {
#            'photo': ImageWidget,
            'assignment': Select(attrs={'class': 'form-control'}),
            'modifiers': SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super(SubmissionForm, self).clean()

        submission_set = Submission.objects.filter(team=self.instance.team)

        # check whether it is an update, then exclude that entry from our checks
        if hasattr(self, 'instance') and self.instance.pk is not None:
            submission_set = submission_set.exclude(pk=self.instance.pk)

        # check that they don't submit this assignment twice
        if submission_set.filter(assignment=cleaned_data.get('assignment')).exists():
            raise ValidationError({'assignment': ["Je hebt deze opgave al ingeleverd",]})

        # check that they don't reuse modifiers

        submission_set = submission_set.filter(modifiers__in=cleaned_data.get("modifiers"))

        # this could be sooo much more neat, but can't figure out how
        if submission_set.exists():
            for submission in submission_set:
                for modifier in submission.modifiers.all():
                    if not modifier.can_occur_multiple:
                        raise ValidationError({'modifiers': ["Je hebt een van de modifiers al eerder gebruikt",]})

        return cleaned_data

        
        
