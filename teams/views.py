from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from teams.models import Team, TemporaryUser, RiallyUser
from teams.forms import TemporaryUserForm, TemporaryUserConfirmForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm

from rially.decorators import require_team_captain
import random
import string

def my_team(request):
    return render(request, 'my_team.html')

@require_team_captain(login_url="/login")
def delete(request, teamId, userId):
    team = get_object_or_404(Team, pk=teamId)

    riallyuser = get_object_or_404(team.riallyuser_set, pk=userId)
    riallyuser.user.delete()
    riallyuser.delete()

    return HttpResponseRedirect(reverse('teams.views.my_team'))

def team_confirm(request, slug):
    temp_user = get_object_or_404(TemporaryUser, email_link=slug)

    if request.method == 'POST':
        form = TemporaryUserConfirmForm(request.POST)
        if form.is_valid():
            # sla deze instance op
            instance = form.save()
            # daarnaast ook zijn emailadres
            instance.email = temp_user.email
            instance.save()

            # maak dan een nieuwe rially_user voor deze user
            rially_user = RiallyUser(user=instance, team=temp_user.team, is_team_captain=temp_user.becomes_team_captain)
            rially_user.save()

            # verwijder dan de temp_user zodat men zich niet twee keer aanmeld
            temp_user.delete()

            # stuur ze dan maar weer weg
            return HttpResponseRedirect(reverse('teams.views.my_team'))
    else:
        form = TemporaryUserConfirmForm() # An unbound form

    return render(request, 'temporary_user_confirm_form.html', {
        'form': form,
    })

class TemporaryUserCreateView(CreateView):
    model = TemporaryUser
    form_class = TemporaryUserForm
    template_name = 'temporary_user_form.html'
    fields = ['email']

    def form_valid(self, form):
        form.instance.team = self.request.user.riallyuser.team
        form.instance.email_link = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(64))
        form.save()

        email = render_to_string('confirm_email.txt', {'team': form.instance.team, 'email_link': form.instance.get_absolute_url()})

        send_mail('Toegevoegd aan een Rially team!', email, 'rially@inter-actief.net',
    [form.instance.email], fail_silently=False)
        return super(TemporaryUserCreateView, self).form_valid(form)

    def get_success_url(self):
        team = self.request.user.riallyuser.team

        return reverse('teams.views.my_team')

class TeamView(ListView):
    template_name = 'team_list.html'
    context_object_name = 'team_list'
    model = Team

class TeamDetail(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'
