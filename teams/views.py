from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from teams.models import Team

from rially.decorators import require_team_captain

def all_teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', locals())

def my_team(request):
    return render(request, 'my_team.html')

@require_team_captain(login_url="/login")
def delete(request, teamId, userId):
    team = get_object_or_404(Team, pk=teamId)

    riallyuser = get_object_or_404(team.riallyuser_set, pk=userId)
    riallyuser.user.delete()
    riallyuser.delete()

    return HttpResponseRedirect(reverse('teams.views.my_team'))
