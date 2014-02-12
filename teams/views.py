from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from teams.models import Team

def all_teams(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', locals())

def my_team(request):
    return render(request, 'my_team.html')
