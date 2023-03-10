import re
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.forms import LogMessage
from django.utils.timezone import datetime
from django.shortcuts import render
from django.views.generic import ListView
from .forms import CreatePollForm
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .models import Employee

def home(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request, "hello/about.html")
def contact(request):
    return render(request, "hello/contact.html")
def polls(request):
    return render(request,  "hello/polls.html")
def questions(request):
    return render(request, "hello/Questions.html")
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'hello/create.html', context)

def results(request):
    context = {}
    return render(request, 'hello/results.html', context)

def vote(request):
    context = {}
    return render(request, 'hello/vote.html', context)
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': self.pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'
    #now = datetime.now()
    #formatted_now = now.strftime("%A, %B %d, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    #match_object = re.match("[a-zA-Z]+", name)

    #if match_object:
     #   clean_name = match_object.group(0)
    #else:
     #   clean_name = "Friend"

    #content = "Hello there, " + clean_name + "! It's " + formatted_now
    #return HttpResponse(content)