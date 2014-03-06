from django.forms import ModelForm, Select, SelectMultiple, ValidationError
from submissions.models import Submission, Modifier
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

        print(submission_set)

        used_modifiers = Modifier.objects.filter(can_occur_multiple=False, submission__in=submission_set)

        double_modifiers = [m for m in cleaned_data.get("modifiers") if m in used_modifiers]

        print(used_modifiers.query)

        print(used_modifiers)
        # this could be sooo much more neat, but can't figure out how
        if double_modifiers:
            raise ValidationError({'modifiers': ["Je hebt een van de modifiers al eerder gebruikt: " + ",".join([str(d) for d in double_modifiers]),]})

        return cleaned_data

        
        
