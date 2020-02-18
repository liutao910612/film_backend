from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('film_server/movie/',include("movie.urls")),
    path('film_server/account/',include("account.urls"))
]
