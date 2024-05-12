from django.shortcuts import render, HttpResponseRedirect
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


def show_studio(request, id):
    studio = models.Studio.objects.get(id=id)
    return render(request, 'animeapp/studio/show.html', {'studio': studio})


def update_studio(request, id):
    studio = models.Studio.objects.get(id=id)
    form = StudioForm(instance=studio)
    return render(request, 'animeapp/studio/update.html', {'form': form, 'studio': studio})


def processing_update(request, id):
    studio = models.Studio.objects.get(id=id)
    lform = StudioForm(request.POST, instance=studio)
    if lform.is_valid():
        studio = lform.save()
        return HttpResponseRedirect("/studio/")
    else:
        return render(request, 'animeapp/studio/update.html', {'form': lform, 'studio': studio})


def delete_studio(request, id):
    studio = models.Studio.objects.get(id=id)
    studio.delete()
    return HttpResponseRedirect("/studio/")

