from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from . import models


class MovieForm(ModelForm):
    class Meta:
        model = models.Movie
        fields = [
            'name', 'tagline', 'alternate_name',
            'release_date', 'plot', 'genre'
        ]

CharacterFormSet = inlineformset_factory(models.Movie, models.Character, fields=('actor', 'name'), extra=2)
