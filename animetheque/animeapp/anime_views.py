from django.shortcuts import render, HttpResponseRedirect
from .forms import AnimeForm
from . import models
# Create your views here.


def home(request):
    animes = models.Anime.objects.all()
    return render(request, 'animeapp/anime/home.html', {'animes': animes})


def add_anime(request):
    form = AnimeForm()
    return render(request, 'animeapp/anime/add.html', {'form': form})


def processing(request):
    lform = AnimeForm(request.POST)
    if lform.is_valid():
        lform.save()
        return render(request, 'animeapp/anime/success.html', {'Anime': lform.cleaned_data})
    else:
        return render(request, 'animeapp/anime/error.html')


def update_anime(request, id):
    anime = models.Anime.objects.get(id=id)
    form = AnimeForm(instance=anime)
    return render(request, 'animeapp/anime/update.html', {'form': form, 'anime': anime})


def processing_update(request, id):
    lform = AnimeForm(request.POST)
    if lform.is_valid():
        Anime = lform.save(
            commit=False)  # création d'un objet Livre avec les données du formulaire mais sans l'enregistrer dans la base.
        Anime.id = id  # modification de l'id de l'objet
        Anime.save()  # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect("/anime/")  # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "animeapp/anime/update.html", {"form": lform, "id": id})


def show_anime(request, id):
    anime = models.Anime.objects.get(id=id)
    return render(request, 'animeapp/anime/show.html', {'anime': anime})


def delete_anime(request, id):
    anime = models.Anime.objects.get(id=id)
    anime.delete()
    return HttpResponseRedirect("/anime/")