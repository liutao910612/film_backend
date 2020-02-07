from django.db import models


class BasicModel(models.Model):
    add_time = models.DateTimeField(auto_now_add=True, null=True)
    add_user = models.IntegerField(null=True)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.IntegerField(null=True)
    is_deleted = models.IntegerField(choices=('0', '1'), null=True)

    class Meta:
        abstract = True


class Film(BasicModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200,null=True)
    video = models.CharField(max_length=200,null=True)
    suppose_num = models.IntegerField(default=0)
    download_num = models.IntegerField(default=0)
    main_page = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Comment(BasicModel):
    id = models.AutoField(primary_key=True)
    movie_id = models.IntegerField
    context = models.TextField
    check = models.IntegerField(choices=('0', '1'))
