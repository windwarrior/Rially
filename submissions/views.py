from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from submissions.forms import SubmissionForm
from submissions.models import Submission, Assignment
from rially.decorators import require_team_captain, require_riallyuser

def index(request):
    return render(request, 'submissions.html')

class SubmissionCreate(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission_form.html'
    success_url = reverse_lazy('submission_list')
    fields = ['photo', 'assignment', 'modifiers']

    def get_form(self, form_class):
        result = super(SubmissionCreate, self).get_form(form_class)
        result.instance.team = self.request.user.riallyuser.team
        return result

    @method_decorator(require_riallyuser)
    def dispatch(self, *args, **kwargs):
        return super(SubmissionCreate, self).dispatch(*args, **kwargs)

class SubmissionUpdate(UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submission_form.html'
    success_url = reverse_lazy('submission_list')
    fields = ['photo', 'assignment', 'modifiers']

    @method_decorator(require_riallyuser)
    def dispatch(self, *args, **kwargs):
        return super(SubmissionUpdate, self).dispatch(*args, **kwargs)

class SubmissionDelete(DeleteView):
    template_name = 'submission_confirm.html'
    success_url = reverse_lazy('submission_list')
    model = Submission

    @method_decorator(require_riallyuser)
    def dispatch(self, *args, **kwargs):
        return super(SubmissionDelete, self).dispatch(*args, **kwargs)

class SubmissionTeamView(ListView):
    template_name = 'submission_list.html'
    context_object_name = 'submission_list'

    def get_queryset(self):
        self.team = None
        if hasattr(self.request.user, "riallyuser"):
            self.team = self.request.user.riallyuser.team

        self.submissions = Submission.objects.filter(team=self.team)
        #self.submissions = Submission.objects.all()

        return self.submissions

class AssignmentView(ListView):
    template_name = 'assignment_list.html'
    context_object_name = 'assignment_list'
    model = Assignment
