from django.contrib import admin
from django.urls import path, re_path

from movie import views

urlpatterns = [
    path('support/<int:user_id>', views.support_film),
    re_path(r'^list/(?P<page>[1-9]\d*)/(?P<amount>[1-9]\d*)/$', views.get_films),

]
