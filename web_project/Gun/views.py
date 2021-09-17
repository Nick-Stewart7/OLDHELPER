import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Prepare to die Dragun")

def gunDisplay(request, name):
    return render(
        request,
        'Gun/gunDisplay.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


# Create your views here.
