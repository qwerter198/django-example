import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from app.forms import MomentForm


# Create your views here.

def welcome(request):
    return HttpResponse("<h1>Welcome to my project!</h1>")


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('first-url'))
    else:
        form = MomentForm()
        PROJECT_ROOT = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})
