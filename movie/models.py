from django.db import models


class BasicModel(models.Model):

    pass


# Create your models here.
class Film(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    video = models.CharField(max_length=200)
    suppose_num = models.IntegerField(default=0)
    download_num = models.IntegerField(default=0)
    main_page = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)
    add_user = models.IntegerField
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.IntegerField

    def __str__(self):
        return self.name

