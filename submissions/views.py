from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from submissions.forms import SubmissionForm
from submissions.models import Submission, Assignment
from rially.decorators import require_team_captain

def index(request):
    return render(request, 'submissions.html')

#def new(request):
#    if request.method == 'POST':
#        form = SubmissionForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('submissions.views.index'))
#    else:
#        form = SubmissionForm()
#
#    return render(request, 'new_photo.html', {
#        'form': form,
#    })

class SubmissionCreate(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission_form.html'
    success_url = reverse_lazy('submission_list')
    fields = ['photo', 'assignment', 'modifiers']

class SubmissionUpdate(UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission_form.html'
    success_url = reverse_lazy('submission_list')
    fields = ['photo', 'assignment', 'modifiers']

class SubmissionDelete(DeleteView):
    template_name = 'submission_confirm.html'
    success_url = reverse_lazy('submission_list')
    model = Submission

class SubmissionTeamView(ListView):
    template_name = 'submission_list.html'
    context_object_name = 'submission_list'

    def get_queryset(self):
        self.team = None
        if self.request.user.riallyuser:
            self.team = self.request.user.riallyuser.team

        # self.submissions = Submission.objects.filter(team=self.team)
        self.submissions = Submission.objects.all()

        return self.submissions

class AssignmentView(ListView):
    template_name = 'assignment_list.html'
    context_object_name = 'assignment_list'
    model = Assignment
