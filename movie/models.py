from django.db import models

from basic.models import BasicModel


class Film(BasicModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    img = models.CharField(max_length=200, null=True)
    video = models.CharField(max_length=200, null=True)
    suppose_num = models.IntegerField(default=0)
    download_num = models.IntegerField(default=0)
    main_page = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Comment(BasicModel):
    id = models.AutoField(primary_key=True)
    movie_id = models.IntegerField
    context = models.TextField
    checked = models.IntegerChoices('0', '1')
