import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.views.generic import ListView
from Gun.models import Gun

class GunListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Gun

    def get_context_data(self, **kwargs):
        context = super(GunListView, self).get_context_data(**kwargs)
        return context
def home(request):
    return render(request, 'Gun/home.html')
def about(request):
    return render(request, "Gun/about.html")


# Create your views here.
