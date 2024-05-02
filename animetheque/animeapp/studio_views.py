from django.shortcuts import render
from .forms import StudioForm
from . import models
# Create your views here.


def home(request):
    studios = models.Studio.objects.all()
    return render(request, 'animeapp/studio/home.html', {'studios': studios})


def add_studio(request):
    form = StudioForm()
    return render(request, 'animeapp/studio/add.html', {'form': form})


def processing(request):
    lform = StudioForm(request.POST)
    if lform.is_valid():
        studio = lform.save()
        return render(request, 'animeapp/studio/success.html', {'Studio': studio})
    else:
        return render(request, 'animeapp/studio/add.html', {'form': lform})

