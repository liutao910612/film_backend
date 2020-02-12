from django.contrib import admin
from django.urls import path, re_path

from movie import views
from movie.views import FilmView

urlpatterns = [

    # you can user reverse() to get url ,for example: reverse('support-film', args=(112,))
    path('support', views.support_film, name='support-film'),
    re_path(r'^list/(?P<page>[1-9]\d*)/(?P<amount>[1-9]\d*)/$', views.get_films),
    path('',FilmView.as_view())

]
