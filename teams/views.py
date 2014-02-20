from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from teams.models import Team, TemporaryUser
from teams.forms import TemporaryUserForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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

class TemporaryUserCreateView(CreateView):
    model = TemporaryUser
    form_class = TemporaryUserForm
    template_name = 'temporary_user_form.html'
    fields = ['email']

    def form_valid(self, form):
        form.instance.team = self.request.user.riallyuser.team
        form.instance.email_link = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(64))
        form.save()

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
