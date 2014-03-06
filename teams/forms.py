from django.forms import ModelForm, EmailInput, TextInput, PasswordInput, RegexField, CharField, EmailField, ValidationError
from teams.models import TemporaryUser, Team
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class TemporaryUserForm(ModelForm):
    class Meta:
        model = TemporaryUser
        fields = ['email']
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'})
        }

# adapted from the UserCreationForm from django
class TemporaryUserConfirmForm(UserCreationForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(label=_("Password"),
        widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label=_("Password confirmation"),
        widget=PasswordInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the same password as above, for verification."))


class TeamCreateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = Team
        fields = ['team_name']
