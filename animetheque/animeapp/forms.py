from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AnimeForm(ModelForm):
    class Meta:
        model = models.Anime
        fields = ['title', 'release_date', 'duration', 'resume', 'studio']
        labels = {
            'title': _('Titre'),
            'release_date': _('Date de parution'),
            'duration': _('Durée'),
            'resume': _('Résumé'),
            'studio': _('Studio'),
        }
        help_texts = {
            'title': _('Entrez le titre de l\'anime'),
            'release_date': _('Entrez la date de parution'),
            'duration': _('Entrez la durée de l\'anime'),
            'resume': _('Entrez le résumé de l\'anime'),
            'studio': _('Entrez le studio de production'),
        }
        error_messages = {
            'titre': {
                'max_length': _("Le titre est trop long."),
            }
        }


class StudioForm(ModelForm):
    class Meta:
        model = models.Studio
        fields = ['name', 'creation_date', 'address']
        labels = {
            'name': _('Nom'),
            'creation_date': _('Date de création'),
            'address': _('Adresse'),
        }
        help_texts = {
            'name': _('Entrez le nom du studio'),
            'creation_date': _('Entrez la date de création'),
            'address': _('Entrez l\'adresse du studio'),
        }
        error_messages = {
            'name': {
                'max_length': _("Le nom du studio est trop long."),
            },
            'address': {
                'max_length': _("L'adresse du studio est trop long."),
            },
        }

