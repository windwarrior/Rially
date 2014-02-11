from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from submissions.forms import PhotoForm

def index(request):
    return render(request, 'submissions.html')

def new(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submissions.views.index'))
    else:
        form = PhotoForm()

    return render(request, 'new_photo.html', {
        'form': form,
    })
