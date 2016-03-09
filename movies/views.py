from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . import forms, models


# Create your views here.

class MovieCreateView(CreateView):
    model = models.Movie
    form_class = forms.MovieForm
    success_url = '/moviedb/movies/%d/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        character_form = forms.CharacterFormSet()
        return self.render_to_response(self.get_context_data(form=form, character_form=character_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        character_form = forms.CharacterFormSet(self.request.POST)
        if (form.is_valid() and character_form.is_valid()):
            return self.form_valid(form, character_form)
        else:
            return self.form_invalid(form, character_form)

    def form_valid(self, form, character_form):
        self.object = form.save()
        character_form.instance = self.object
        character_form.save()
        return HttpResponseRedirect(self.get_success_url() % self.object.pk)

    def form_invalid(self, form, character_form):
        return self.render_to_response(self.get_context_data(form=form, character_form=character_form))


class MovieDetailView(DetailView):
    model = models.Movie


class MovieListView(ListView):
    model = models.Movie
