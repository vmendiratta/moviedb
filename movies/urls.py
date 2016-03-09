from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/$',
        views.MovieListView.as_view(),
        name='movie-list'),
    url(r'^movies/add/$',
        views.MovieCreateView.as_view(),
        name='movie-create'),
    url(r'^movies/(?P<pk>[0-9]+)/$',
        views.MovieDetailView.as_view(),
        name='movie-detail'),
]
