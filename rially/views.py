from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')
